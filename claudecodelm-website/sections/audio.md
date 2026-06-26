# Audio (player)

## Current (from index.html)

**Title:** 🎤 Listen — What Got Built
**Subtitle:** "A different artifact, not the original delegation target"
**Embedded file:** podcast.mp3
**Meta:**
- Paper — Nakamura & Uhlmann, *Global uniqueness for an inverse boundary problem arising in elasticity* (Inventiones, 1994)
- Voice — Matilda
- Model — eleven_v3
- Duration — 16:06
- Tags — 53 inline audio tags

## Audit (against the yardstick — vivek_reconstruction.md)

- **Duration "16:06": VERIFIED CORRECT.** ffprobe on `claudecodelm-website/podcast.mp3` = 16.1 min (966s) = 16:06. No data error.
- **Metadata (paper, voice, model, tags): accurate, keep.**
- **Subtitle is faintly apologetic.** "A different artifact, not the original delegation target" leans on the substitute/lesser framing. Per §3 and Vivek's "better than the original" reaction, the tone can be less of an apology — it's not a consolation prize, it's the thing that turned out to work (and arguably better: one host, shorter than NotebookLM, grounded).

## Proposed

- **Subtitle (reframe, optional):** "Not what was originally asked for — what turned out to work better." (or let the "What Got Built" title carry that and simplify the subtitle to: "Single host. Grounded in the paper. Shorter than NotebookLM.")
- **Everything else unchanged** (metadata verified accurate).

## APPLIED to index.html 2026-06-25 (Vivek 👍)

- Subtitle: "A different artifact, not the original delegation target" → "Single host · grounded in the paper · shorter than NotebookLM" (drops the apologetic ring; states what it is). Verified: renders on one line, no overflow.
- Metadata unchanged (verified accurate; player shows 16:05, label 16:06 — rounding, fine).
