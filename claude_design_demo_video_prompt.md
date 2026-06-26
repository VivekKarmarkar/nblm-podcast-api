# Claude Design — ClaudeCodeLM demo-video prompt

> Paste the **PROMPT** block below into Claude Design. It generates an animated HTML video. A separately-produced **architecture walkthrough video clip** gets composited into the reserved slot (scene 4) afterward, and **Matilda (ElevenLabs) narration + sound effects** are added later in post — so the generated video must contain **no baked-in audio**.

---

## PROMPT

Build an animated, self-playing **demo video as a single self-contained HTML file** for a project called **ClaudeCodeLM**.

**What ClaudeCodeLM is:** a Claude Code skill that turns any document — a research paper, an article, a web page, a legal doc, a tutorial — into a verified, single-host audio podcast. It's "NotebookLM, but built inside your coding agent." Background agents segment the document, analyze and synthesize it, check every substantive claim back against the source to keep it grounded, layer in emotional narration, and deliver the finished episode — autonomously, kicked off from a phone on a walk. It ships as a malleable git-repo blueprint, not a locked product.

**Audience:** AI startups, the NotebookLM team, anyone building document-analysis / agentic-AI tooling. **Tone:** confident, clean, a little playful — developer-conference energy.

**Visual style (match exactly — it must look continuous with the site):**
- Background `#0f1019` (near-black).
- Accents: orange `#f97316` (primary), blue `#38bdf8`, green `#4ade80`, amber `#fbbf24`.
- Font: **DM Sans** (Google Fonts).
- Smooth modern motion — fades, slides, subtle glows, particle / data-flow accents. Lots of breathing room, zero clutter.
- 16:9, 1920×1080.

**Structure (~75–90s total; every scene animates in and out, with explicit, editable durations):**
1. **Hook (5s):** a phone buzzing in a pocket, someone walking. Caption: "You're working on a research paper. While walking. Hands full."
2. **The gap (8s):** every step of the pocket research workflow runs from the sidewalk — except generating the NotebookLM-style podcast. Show that one broken link in the chain.
3. **The pivot (8s):** there was no clean API for it, so it got built from scratch — inside Claude Code. Caption: "Background agents that CREATE the podcast — not call an API."
4. **>>> ARCHITECTURE SECTION — RESERVED SLOT (≈30–45s) <<<** Leave a clearly-labeled **empty placeholder**: a full-bleed `#0f1019` rectangle (1920×1080) with a centered caption "ARCHITECTURE WALKTHROUGH — clip drops in here", a clean fade-in before and fade-out after, and a **fixed, explicit duration**. An externally-produced architecture walkthrough video will be composited into this slot. **Do NOT design the architecture diagram yourself** — just reserve the time and the frame.
5. **Grounded, honestly (8s):** "Every claim checked against the paper's own words. Best-effort, not magic — and honest about it."
6. **Outcome (8s):** a waveform / play affordance. "16 minutes. One host. Shorter than NotebookLM. Better, the first time he pressed play."
7. **What it is (6s):** "A skill, not a hosted product — a malleable blueprint. Clone it, point Claude at it, reshape it for your own agents."
8. **Outro (5s):** the **ClaudeCodeLM** wordmark + GitHub handle, fade to black.

**Critical constraints:**
- **No audio baked in.** Narration (ElevenLabs Matilda voice) and sound effects are added in post — design it silent-but-legible and pace it so a voiceover can ride on top.
- Make every scene's duration **explicit and editable** (e.g. data attributes or a clearly-commented timeline) so timing can be tuned in editing.
- The reserved architecture slot (scene 4) must stay an **empty, labeled placeholder of fixed duration** — do not fill it.
- **Single self-contained HTML file**, no external dependencies except the Google Font link.

---

## Post-production plan (after Claude Design returns the HTML)

1. Capture/render the Claude Design HTML to video (the scaffolding).
2. Composite the **architecture walkthrough clip** (produced via `/architectural-walkthrough-video`, based on the site's own diagram) into scene 4's reserved slot — `ffmpeg` overlay/concat at the slot's timestamps.
3. Add **Matilda (ElevenLabs MCP)** voiceover narration matching the scene captions + light sound effects.
4. `ffmpeg` (and Remotion if needed) for final edit, fades, encode.
5. Deliverable is **not committed to git** (too heavy). Upload to YouTube → embed the YouTube player in the site (light + port-friendly).
