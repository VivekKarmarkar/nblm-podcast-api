# Phase 1.5 Recommendation — Podcastfy (B) vs ElevenLabs GenFM (C)

**Run date:** 2026-05-23
**Trigger:** Vivek ruled out path A (AutoContent API — cost) and the official Google Audio Overview API (inaccessible, functionally incomplete, $1,620/yr enterprise floor). Phase 1.5 deep-dove the remaining viable substitutes.
**Execution:** swarm of 8 parallel research agents — 3 lanes per library (docs+github, real-world usage, community sentiment) + 2 community-comparison agents (written, video/social).

---

## Headline recommendation

**Start with B (Podcastfy). Add C (ElevenLabs Studio Podcast) as an optional second backend later, only if voice quality becomes a real-use blocker.**

Rationale in one paragraph: Podcastfy is free, BYO-keys (you already have Gemini + Anthropic + can use Edge TTS for $0), runs locally, supports PDF natively, and the engineering work to wrap it in an async-orchestrating MCP is the *exact* L4-background-agent layer your motivation document calls for — so the wrapper effort isn't a tax, it's the deliverable. ElevenLabs Studio gives better voice quality and proper async-on-the-wire, but costs money, may be allowlist-gated for your account, and reduces the wrapper to a thin pass-through which doesn't teach you the L4 architecture as cleanly. If voice quality on Podcastfy turns out to be unacceptable in real use, a second ElevenLabs backend variant slots into the same MCP interface in <1 day of work.

---

## Side-by-side comparison

| Axis | **B — Podcastfy** | **C — ElevenLabs Studio Create Podcast** |
|---|---|---|
| **Cost per 10-min episode** | **$0** with Gemini free tier + Edge TTS / **$2–5** with Gemini + ElevenLabs TTS | **$0.85** (Flash model overage) / **$1.70** (Multilingual v2 overage) / **$22/mo** Creator tier = 26 episodes covered |
| **Free tier viability** | True $0 path exists | 20k chars/mo = ~1.2 podcasts/month; **no commercial use** below Starter ($6/mo) |
| **Async API surface** | ❌ **Synchronous-blocking** — `generate_podcast()` and FastAPI `/generate` both block ~5 min until done. No job queue, no status endpoint, no webhook. YOU build the async layer. | ✅ **Proper async** — POST returns `project_id` immediately; poll `GET /v1/studio/projects/{id}` or use `callback_url` webhook. Status enum: `pending → creating → finished | failed`. |
| **MCP availability** | ❌ Greenfield — NO Podcastfy MCP wrapper exists | ❌ `elevenlabs/elevenlabs-mcp` (official, v0.9.1) **does NOT expose Create Podcast** — only TTS primitives. Need thin custom wrapper around `client.studio.create_podcast()` from the Python SDK. |
| **Allowlist gate** | None | ⚠️ **CONTRADICTORY EVIDENCE** — elevenlabs-community agent quoted the docs saying "Your workspace must be allowlisted to use this feature"; elevenlabs-docs-github agent's deeper docs read did NOT find this restriction. **Vivek must verify before betting on C.** |
| **Input formats** | PDF (PyMuPDF built-in), URL, YouTube, plain text, local images, topics (with web search) | text, URL, EPUB, PDF, TXT, HTML, existing-project reference |
| **Voice configuration** | 5 TTS providers × per-provider voice choice; full conversation_config knobs (style, roles, dialogue structure, engagement techniques, creativity slider, word_count, language) | exactly 2 voices in `conversation` mode (host_voice_id + guest_voice_id from ~1000 ElevenLabs voices), or 1 voice in `bulletin` mode; `instructions_prompt` up to 3000 chars, `duration_scale` short/default/long, `quality_preset` standard/high/ultra/ultra_lossless |
| **Voice quality** | Mid — creator's own README admits "NotebookLM's AI-generated voices remain unparalleled in quality." Quality varies wildly by TTS provider chosen. | High — industry-leading TTS. XDA: "had human-like elements, sounded natural, engaging." Better raw voice than NotebookLM. |
| **Conversational dynamics** | Depends on LLM script; out-of-box mid-tier | High but "more like two presenters taking turns than two friends bantering" per UX Tigers / Nielsen Norman roundup |
| **Multilingual** | Yes via provider choice | 32 languages native |
| **Self-hosted / vendor-locked** | Fully self-hosted | Vendor-locked (hosted REST API); SDK migrating away requires rewriting orchestration |
| **API stability** | Library API stable, but bus-factor-1 maintainer risk | ElevenLabs ships breaking changes ~quarterly (documented changelog). API is stable in cadence, just churny. |
| **Project health signal** | 6.3k stars, 13-month silent gap on PyPI, recent commits are README polish, 84 open issues, JOSS submission stuck in "query-scope" pre-review limbo, maintainer admitted he can't keep up | ElevenLabs is a vendor-backed core product; Python SDK v2.49.1 shipped **2026-05-21 (4 days ago)** with `client.studio.create_podcast()` confirmed present |
| **Engineering work for Phase 2 MCP** | ~1–2 days: write async-orchestration wrapper (subprocess + job tracking + file watcher) + MCP interface | ~0.5–1 day: thin MCP wrapper around official Python SDK (async handled by ElevenLabs) |
| **Side benefit** | Fills "academic paper-to-podcast" vertical that has no consolidated tool. Zero academic users of Podcastfy currently — Vivek's pipeline would be novel. | None comparable. ElevenLabs has Perplexity's "Discover Daily" as flagship reference; academic vertical is unrepresented but ElevenLabs isn't well-positioned to fill it. |

---

## Why "start with B, optionally add C"

Five reasons:

1. **The free path is genuinely free.** Gemini 2.5 Flash-Lite (free tier covers hobbyist volume) + Edge TTS (free, no key required) = $0 per podcast. You don't need to spend anything to validate the workflow end-to-end.

2. **The MCP wrapper effort IS the L4 architecture layer.** Your motivation document said L4 = "background agent making the L3 API call; main session keeps moving; agent absorbs the wait." Because Podcastfy is sync-blocking, the MCP wrapper has to provide the entire async-orchestration layer — which is exactly what L4 describes. With ElevenLabs Studio, that layer is given to you by the API, so the MCP wrapper becomes a near-trivial pass-through. **You learn more architecture from path B.**

3. **B and C share an MCP interface shape.** Both can expose `create_podcast(source, options)` returning a job_id, `get_podcast_status(job_id)`, `download_podcast(job_id)`. So building B first doesn't lock you out of C — adding ElevenLabs as a second backend variant later is small, focused work that swaps the orchestration internals while keeping the MCP tool surface identical.

4. **Voice quality may not be the bottleneck for YOUR use case.** Your use case is paper-to-podcast for personal walking-around listening, not publication. The Pitt/AGU and Lennart Nacke academic accuracy findings on NotebookLM suggest that *accuracy* — not voice naturalness — is what matters when consuming research content via audio. Podcastfy's "configurable LLM + transparent script" architecture lets you pin the LLM step to a model you trust (Claude, Gemini), inspect the script before TTS, and even regenerate from the script alone. ElevenLabs' opaque script generation gives you voice quality at the cost of script auditability.

5. **The Vivek-specific cost picture favors B-first.** You said no to AutoContent at €24–166/mo. ElevenLabs' Creator tier is $22/mo — adjacent to the same objection. Path B can be validated at $0, deferring the cost question until you actually know voice quality is a problem in practice.

---

## What Phase 2 looks like, concretely, if you pick path B

**Stack:**
- Python 3.11+ venv (heavy install ~2GB after Playwright Chromium)
- `pip install podcastfy` + `ffmpeg` system dep
- Gemini API key (free tier) for LLM; Edge TTS (free, no key) or OpenAI TTS (paid, you already have key) for TTS
- A thin Python MCP server (FastMCP) exposing three tools:
  - `create_podcast(source_path_or_url, options)` → returns `{job_id, status: "queued"}`
  - `get_podcast_status(job_id)` → returns `{status, progress, audio_path_if_done}`
  - `download_podcast(job_id)` → returns local file path
- Background worker process (could be `subprocess.Popen` spawning Podcastfy, or a Celery/RQ worker if you want a real queue). Tracks job state in a SQLite file or in-memory dict. Watches `./data/audio/` for the mp3 to land.
- Integration with your existing `/upload-and-share` skill — when audio is ready, return the path, then user invokes upload-and-share.

**End-to-end user flow:**
1. Vivek (walking) voice-notes "make me a podcast on the Bowman paper I just downloaded"
2. Main session: calls `create_podcast(source_path="./bowman_VVT.pdf")` → gets job_id immediately
3. Main session continues with other work (or just ends the turn)
4. ~5 minutes later, Vivek (still walking) voice-notes "is the podcast ready?"
5. Main session: calls `get_podcast_status(job_id)` → finished, returns mp3 path
6. Main session: calls `/upload-and-share vivekjobapp123@gmail.com`
7. Vivek's phone gets the mp3, presses play, walks on

This is exactly the Level-4 flow from `problem_statement.md`. No clicking, no main-session polling, no blocking wait.

**Engineering estimate:** ~1–2 working days for a complete MCP wrapper, including manual test against the two Bowman papers spec'd in Phase 2 Test 1 + Test 2.

---

## What Phase 2 looks like, concretely, if you pick path C

**Stack:**
- Python 3.11+ venv
- `pip install elevenlabs` (v2.49.1)
- ElevenLabs API key (paid — Starter $6/mo or Creator $22/mo recommended; Free tier blocks commercial use)
- **Verify allowlist requirement** for Studio Create Podcast — contradictory evidence in our reports
- A thin Python MCP server exposing same three tools as path B
- Async handling: pass `callback_url` to ElevenLabs, run a tiny FastAPI webhook receiver, OR poll `GET /v1/studio/projects/{id}` every 30s

**Engineering estimate:** ~0.5–1 day. The async heavy lifting is handled by ElevenLabs' API; MCP wrapper is mostly pass-through.

**Hard prerequisites Vivek must verify before committing:**
- Workspace allowlist status for the Studio Podcast endpoint (community agent says it's required; docs-github agent didn't find this — go to dashboard and try a test call)
- Willingness to pay $6+/mo for commercial-use license (Free tier explicitly disallows commercial use)
- Acceptance of vendor lock-in (the wrapper effort is small but switching backends later means rewriting it)

---

## Open questions for Vivek

1. **Path confirmation:** Path B (Podcastfy) as the primary build target, with a second-pass evaluation of voice quality after first working podcast lands?
2. **Cost ceiling:** When you said "not willing to pay" for AutoContent (~€24/mo), what's the implicit number? Would $6–22/mo for ElevenLabs Creator/Starter cross the same line, or is "no monthly subscription at all" the principle?
3. **Voice quality threshold:** If Podcastfy + Edge TTS sounds robotic, would you accept paying ElevenLabs' overage ($0.85–$1.70 per 10-min podcast) on demand, or only as a subscription?
4. **Q4 from Phase 1 revisited:** With this clearer picture, do you want to keep the existing `notebooklm-mcp` as a Level-2 fallback, or cut the cord once Phase 2 ships?
5. **Academic-vertical positioning:** This research surfaced that nobody has built a consolidated "academic paper → podcast" pipeline. Would you want the MCP design to specifically optimize for that vertical (DOI/arXiv-aware ingestion, citation-preserving script gen, academic-tone host config), or keep it general-purpose with paper-to-podcast as one use case among many?

---

## Phase 1.5 termination

This document is the Phase 1.5 deliverable. Phase 2 spec depends on your answers to the 5 questions above. Once you confirm path B (or pivot to C), Phase 2 can begin — and per Phase 1 spec, that's: install/build MCP → Test 1 (main-session round-trip on Bowman "Visual Vibration Tomography") → Test 2 (background-agent round-trip on Bowman "Visual Surface Wave Elastography") with /upload-and-share at the end of each.

---

## Source attribution

All findings cited inline within the comparison table and analysis. Full agent reports are available in the session transcript. Eight agents, all gracefully shut down, team `phase1-5-substitute-research` deleted.
