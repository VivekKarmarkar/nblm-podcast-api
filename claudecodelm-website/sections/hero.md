# Hero

## Current (from index.html)

**Title:** ClaudeCodeLM

**Tagline:** "The pocket-only paper-reading workflow has one layer that breaks: generating a NotebookLM audio podcast while walking. The motivation for this project was finding a clean way to delegate that step. The search returned nothing usable. This page is what got built instead."

**Tags:** Claude Code · ElevenLabs eleven_v3 · OpenAI TTS · Research Papers · Single-Host Audio · AI Startup

## Audit (against the yardstick — vivek_reconstruction.md)

- **Name "ClaudeCodeLM": KEEP.** Confirmed intentional — Vivek re-derived it himself from first principles (§3). It lands.
- **Category miscommunication in the last line.** "This page is what got built instead" frames the deliverable as *a page / an artifact*. Per §3 + §6.3, the actual identity is **a Claude Code skill — a malleable blueprint shipped as a git repo**, not a page. This is the single biggest framing fix: a reader (esp. the "AI Startup" audience tag) should come away knowing it's *a skill you can clone and run*, not just a showcase page.
- **Tagline body is accurate** on the premise (no clean way to delegate → search returned nothing usable, §2). Keep that spine.
- **Missing positioning:** the "shorter than NotebookLM" hook (§6.1) and the skill/blueprint identity (§6.3, light touch).

## Proposed

**Title:** ClaudeCodeLM *(unchanged)*

**Tagline (rewrite of the last line; keep it light on the skill framing):**
"The pocket-only paper-reading workflow has one layer that breaks: generating a NotebookLM-style audio podcast while walking. There's no clean way to delegate that step — no usable API, nothing to install and forget. So it stopped being a thing to delegate and became a Claude Code skill that builds the podcast itself — clone it, point it at a paper, get an episode back."

**Tags:** unchanged (they already carry the right signals; "Single-Host Audio" + "AI Startup" are good).

## LOCKED — applied to index.html 2026-06-25

Final tagline (live):
"The step-count-driven, voice-first research workflow has one layer that breaks: generating a NotebookLM audio podcast while walking. The motivation for this project was finding a clean way to delegate that step. The search returned nothing usable — so it got built from scratch. It has the shape of a product, but it's the blueprint for a customizable skill that makes your AI agents happy… if you live in coding agents… 🙂"

Changes vs original: (1) "pocket-only paper-reading workflow" → "step-count-driven, voice-first research workflow" (research, not just paper-reading — it often leads into coding); (2) "This page is what got built instead" → the affirmative product-shaped-blueprint close (no negation). Title "ClaudeCodeLM" and tags unchanged.
