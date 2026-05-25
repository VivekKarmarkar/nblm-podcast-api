#!/usr/bin/env python3
"""
audify_eleven — Convert a tagged narrative (Markdown/TXT) to MP3 via ElevenLabs.

Input: a .md or .txt file already enriched with eleven_v3 audio tags
(e.g. [warmly], [pause], [excited]). This script does NOT do tag enrichment —
that is upstream creative work (manual in Phase 2; agent-driven in Phase 4).

The script:
  1. Reads the tagged narrative.
  2. Chunks it under the 5000-char eleven_v3 cap (target 4500 with paragraph
     and sentence-boundary preference).
  3. Calls ElevenLabs text_to_speech.convert per chunk with prosodic continuity
     via previous_text / next_text overlap (~500 chars).
  4. Concatenates chunk MP3s losslessly via ffmpeg.

Usage:
    python3 audify_eleven.py INPUT.md [-o OUT.mp3] [--voice-id ID] [--model eleven_v3]
                              [--stability 0.5] [--similarity 0.75] [--style 0.0]
                              [--dry-run]

Default voice: Matilda (XrExE9yKIg1WjnnlVkGX) — warm middle-aged American female,
explicitly tagged "friendly, narration, calm" in the ElevenLabs default library;
best fit for long-form coffee-shop-friend science narration. Override via
--voice-id for other library voices (Sarah EXAVITQu4vr4xnSDxMaL nova-analog,
Lily pFZP5JQG7iQjIQuC4Bku British, Aria 9BWtsMINqrJLrRacOk9x most expressive).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings

# Eleven v3 hard cap is 5000 chars/request. Target lower to keep splits on
# paragraph / sentence boundaries.
CHUNK_TARGET = 4500
# Prosodic-continuity overlap fed to previous_text / next_text per chunk.
OVERLAP = 500

# Matilda — default-library, narration-tagged, warm middle-aged American female.
DEFAULT_VOICE_ID = "XrExE9yKIg1WjnnlVkGX"
DEFAULT_MODEL = "eleven_v3"
DEFAULT_OUTPUT_FORMAT = "mp3_44100_128"


# ───────────────────────── text extraction ─────────────────────────

def extract_text(path: Path) -> str:
    suf = path.suffix.lower()
    if suf in {".md", ".markdown", ".txt"}:
        return path.read_text(encoding="utf-8", errors="replace")
    raise ValueError(f"Unsupported input type: {suf} (use .md / .markdown / .txt)")


# ───────────────────────── light cleanup ─────────────────────────
# Tagged narratives are already polished. Only strip markdown structure that
# would be read aloud as junk. Leave [tag] brackets ALONE — those are payload.

_MD_STRIP = [
    (re.compile(r"^```.*?\n.*?^```", re.DOTALL | re.MULTILINE), ""),
    (re.compile(r"`([^`]+)`"), r"\1"),
    (re.compile(r"!\[[^\]]*\]\([^)]+\)"), ""),
    (re.compile(r"\[([^\]]+)\]\(([^)]+)\)"), r"\1"),  # markdown link: keep anchor text only
    (re.compile(r"^>\s?", re.MULTILINE), ""),
    (re.compile(r"^#{1,6}\s+", re.MULTILINE), ""),
    (re.compile(r"\*\*([^*\n]+)\*\*"), r"\1"),
    (re.compile(r"(?<!\w)\*([^*\n]+)\*(?!\w)"), r"\1"),
    (re.compile(r"_{2}([^_\n]+)_{2}"), r"\1"),
    (re.compile(r"^[\-*+]\s+", re.MULTILINE), ""),
    (re.compile(r"^\s*\|.*\|\s*$", re.MULTILINE), ""),
    (re.compile(r"^[-=]{3,}\s*$", re.MULTILINE), ""),
]


def clean_text(raw: str) -> str:
    text = raw
    for pat, repl in _MD_STRIP:
        text = pat.sub(repl, text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    return text.strip()


# ───────────────────────── chunking ─────────────────────────

_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z\"'(\[])")


def chunk_text(text: str, target: int = CHUNK_TARGET) -> list[str]:
    chunks: list[str] = []
    for para in re.split(r"\n{2,}", text):
        para = para.strip()
        if not para:
            continue
        if len(para) <= target:
            _append(chunks, para, target)
            continue
        sentences = _SENT_SPLIT.split(para)
        buf = ""
        for s in sentences:
            if len(buf) + len(s) + 1 <= target:
                buf = f"{buf} {s}".strip()
            else:
                if buf:
                    _append(chunks, buf, target)
                if len(s) > target:
                    for piece in _hard_split(s, target):
                        _append(chunks, piece, target)
                    buf = ""
                else:
                    buf = s
        if buf:
            _append(chunks, buf, target)
    return chunks


def _append(chunks: list[str], piece: str, target: int) -> None:
    piece = piece.strip()
    if not piece:
        return
    if chunks and len(chunks[-1]) + len(piece) + 2 <= target:
        chunks[-1] = f"{chunks[-1]}\n\n{piece}"
    else:
        chunks.append(piece)


def _hard_split(s: str, target: int) -> list[str]:
    words = s.split()
    out, buf = [], ""
    for w in words:
        if len(buf) + len(w) + 1 > target:
            out.append(buf)
            buf = w
        else:
            buf = f"{buf} {w}".strip()
    if buf:
        out.append(buf)
    return out


# ───────────────────────── TTS + assembly ─────────────────────────

def synthesize(chunks: list[str], out_path: Path, voice_id: str, model_id: str,
               stability: float, similarity: float, style: float) -> None:
    if not os.environ.get("ELEVENLABS_API_KEY"):
        raise RuntimeError("ELEVENLABS_API_KEY not set")

    client = ElevenLabs(api_key=os.environ["ELEVENLABS_API_KEY"])
    settings = VoiceSettings(
        stability=stability,
        similarity_boost=similarity,
        style=style,
        # NOTE: use_speaker_boost intentionally omitted — unsupported on eleven_v3.
        speed=1.0,
    )

    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        parts: list[Path] = []
        # NOTE: eleven_v3 rejects previous_text / next_text ("unsupported_model"
        # error verbatim from the API). Only v2-family models accept them.
        supports_continuity = not model_id.startswith("eleven_v3")
        for i, chunk in enumerate(chunks, 1):
            part = tmpdir / f"part_{i:04d}.mp3"
            print(f"  [{i}/{len(chunks)}] {len(chunk)} chars → {part.name}",
                  flush=True)
            kwargs = {
                "voice_id": voice_id,
                "model_id": model_id,
                "text": chunk,
                "output_format": DEFAULT_OUTPUT_FORMAT,
                "voice_settings": settings,
            }
            if supports_continuity:
                prev_text = chunks[i - 2][-OVERLAP:] if i >= 2 else None
                next_text = chunks[i][:OVERLAP] if i < len(chunks) else None
                if prev_text:
                    kwargs["previous_text"] = prev_text
                if next_text:
                    kwargs["next_text"] = next_text

            audio_iter = _call_with_backoff(client, kwargs)
            with open(part, "wb") as f:
                for piece in audio_iter:
                    if piece:
                        f.write(piece)
            parts.append(part)

        if len(parts) == 1:
            parts[0].replace(out_path)
            return

        concat_list = tmpdir / "list.txt"
        concat_list.write_text(
            "\n".join(f"file '{p.as_posix()}'" for p in parts)
        )
        subprocess.run(
            ["ffmpeg", "-y", "-f", "concat", "-safe", "0",
             "-i", str(concat_list), "-c", "copy", str(out_path)],
            check=True, capture_output=True,
        )


def _call_with_backoff(client: ElevenLabs, kwargs: dict, max_retries: int = 5):
    """Wrap text_to_speech.convert with exponential backoff for 429 + 5xx."""
    from elevenlabs.core.api_error import ApiError  # local import: SDK-internal
    delay = 2.0
    for attempt in range(1, max_retries + 1):
        try:
            return client.text_to_speech.convert(**kwargs)
        except ApiError as e:
            status = getattr(e, "status_code", None)
            if status == 429 or (status and 500 <= status < 600):
                if attempt == max_retries:
                    raise
                print(f"    HTTP {status} — backoff {delay:.1f}s (attempt {attempt}/{max_retries})",
                      flush=True)
                time.sleep(delay)
                delay *= 2
                continue
            raise


# ───────────────────────── CLI ─────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="Convert tagged narrative to MP3 via ElevenLabs.")
    ap.add_argument("input", type=Path, help=".md or .txt narrative (tagged)")
    ap.add_argument("-o", "--output", type=Path, default=None,
                    help="output MP3 path (default: <input>.mp3)")
    ap.add_argument("--voice-id", default=DEFAULT_VOICE_ID,
                    help=f"ElevenLabs voice_id (default: Matilda {DEFAULT_VOICE_ID})")
    ap.add_argument("--model", default=DEFAULT_MODEL,
                    help=f"model_id (default: {DEFAULT_MODEL})")
    ap.add_argument("--stability", type=float, default=0.5,
                    help="v3: 0.5 ≈ Natural; lower (~0.3) = Creative; higher (~0.7) = Robust")
    ap.add_argument("--similarity", type=float, default=0.75,
                    help="similarity_boost (default 0.75)")
    ap.add_argument("--style", type=float, default=0.0,
                    help="style (default 0.0 — v3 audio tags largely replace this)")
    ap.add_argument("--dry-run", action="store_true",
                    help="extract + chunk, print stats, don't call API")
    args = ap.parse_args()

    if not args.input.exists():
        print(f"error: {args.input} not found", file=sys.stderr)
        return 2

    out = args.output or args.input.with_suffix(".mp3")

    print(f"→ extracting {args.input.name}")
    raw = extract_text(args.input)
    text = clean_text(raw)
    chunks = chunk_text(text)

    total = sum(len(c) for c in chunks)
    print(f"→ {total:,} chars in {len(chunks)} chunk(s) (target ≤{CHUNK_TARGET}/chunk)")
    # eleven_v3 ≈ 1 credit per char.
    print(f"→ est. cost: {total:,} credits (model={args.model})")

    if args.dry_run:
        print("\n--- chunk sizes ---")
        for i, c in enumerate(chunks, 1):
            print(f"  [{i}] {len(c):,} chars")
        preview = text[:300].replace("\n", " ")
        print(f"\n--- preview ---\n{preview}…\n")
        return 0

    if not os.environ.get("ELEVENLABS_API_KEY"):
        print("error: ELEVENLABS_API_KEY not set", file=sys.stderr)
        return 2

    print(f"→ synthesizing → {out}")
    synthesize(chunks, out, args.voice_id, args.model,
               args.stability, args.similarity, args.style)
    size_kb = out.stat().st_size / 1024
    print(f"✓ wrote {out} ({size_kb:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
