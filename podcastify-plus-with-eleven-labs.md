# podcastify-plus with ElevenLabs

> **Created:** 2026-05-24
> **Owner:** VivekKarmarkar
> **Scope:** Close the emotional-flatness gap in the existing 3 podcastify skills by adding an ElevenLabs-enhanced sibling trio. Roadmap ends at the Nakamura-Uhlmann smoke test.

## Motivation

The 3 currently-shipped podcastify skills (`/podcastify`, `/podcastify-and-share`, `/download-podcastify-and-share`) work end-to-end and produce competent OpenAI-TTS audio at voice `nova` @ speed 0.85. Quality on content + pacing matches or beats NotebookLM in places. **Remaining gap: emotional regulation.**

Positives of current state:
- Personality comes through (e.g., "the engineering is delicious" line in the Bouman VSWE podcast).
- Pacing is comprehensible.

Negatives:
- Emotionally flat / monotonous.
- Uncanny-valley feel persists.

ElevenLabs offers credible upgrade paths: (a) a model that supports inline emotion-tag insertion via an f-string-like bracket syntax, (b) voices that beat `nova` on warmth, and (c) other fine-tuning knobs.

## Cardinal constraint (Unix philosophy)

**Do NOT touch the existing 3 skills.** Build the ElevenLabs layer as 3 NEW sibling skills with `-plus` suffix. The "+" means **ElevenLabs-enhanced**.

```
podcastify                        ──→  podcastify-plus
podcastify-and-share              ──→  podcastify-plus-and-share
download-podcastify-and-share     ──→  download-podcastify-plus-and-share
```

The existing trio stays untouched as the OpenAI-TTS baseline. The `-plus` trio adds the emotion-layering step.

## Roadmap

### Phase 1 — ElevenLabs capability research

**Goal:** Understand what ElevenLabs actually offers before writing any integration code.

| Task | Description |
|------|-------------|
| `/niche-library-research` on ElevenLabs | Dispatch research agents at the ElevenLabs documentation. Surface: the emotion-tag-in-prompt model (the f-string-like bracket syntax for inserting emotions), voices that beat `nova` on warmth, other fine-tuning knobs (stability, similarity-boost, style, speaker-boost, model selection). |
| `/swarm` to find ElevenLabs docs MCP | Spin up agents with high preference on ElevenLabs official site + MCP marketplaces. Question: does ElevenLabs ship an official docs MCP (LiveKit-style)? If yes, install it and use it for the rest of this project. **Load-bearing: the agent focused on the ElevenLabs OFFICIAL docs is weighted more heavily than the others.** |

**Exit criteria:**
- [ ] Confirmed which ElevenLabs model supports inline emotion tagging + the exact syntax
- [ ] Identified the warm-Nova-replacement voice
- [ ] Documented the fine-tuning surface (stability, similarity, etc.)
- [ ] Docs MCP status known (installed if available)

---

### Phase 2 — One-paper manual experimentation

**Goal:** I personally develop a sense of how ElevenLabs needs to be wielded to produce emotionally-rich podcasts. **ZERO feedback loop with Vivek during this phase.**

| Task | Description |
|------|-------------|
| Download one paper | `/paper-download-hack` to grab ONE paper — FNO (Fourier Neural Operator) OR DeepONet, I pick. |
| Baseline podcast | `/podcastify` → produces `narrative_final.md` + baseline `podcast.mp3` in cwd (background agent). |
| ElevenLabs experimentation | I personally take `narrative_final.md` and produce an ElevenLabs-enhanced mp3. Layer in emotion tags, pick the warm voice, tune fine-grain knobs. This is hands-on exploration. |
| Share | `/upload-and-share` to deliver the enhanced mp3 to `vivekjobapp123@gmail.com`. **I do NOT wait for feedback.** Vivek is not in the loop. |

**Exit criteria:**
- [ ] One ElevenLabs-enhanced mp3 in Drive, shared with `vivekjobapp123@gmail.com`
- [ ] I have a clear, internalized sense of the emotion-tagging workflow

---

### Phase 3 — Background-agent feasibility gate (make-or-break)

**Goal:** Determine whether the full ElevenLabs enhancement can run end-to-end inside a background agent.

| Task | Description |
|------|-------------|
| Feasibility investigation | Can a background agent autonomously: (a) call the ElevenLabs API with the right model and emotion tags, (b) iterate on output if needed, (c) produce a final enhanced mp3 without human intervention? |
| Gate decision | **If NO:** the whole project is pointless without background-agent autonomy — TERMINATE. Surface the blocker honestly, stop. Vivek will redirect via a fresh `/goal`. **If YES:** proceed to Phase 4. |

**Exit criteria:**
- [ ] Gate decision made with clear evidence
- [ ] If NO: roadmap halted, blocker surfaced
- [ ] If YES: green light for Phase 4

---

### Phase 4 — Ship 3 "+" skills (background-agent does everything)

**Goal:** Package the proven workflow as 3 globally-available skills where the **background agent does EVERYTHING** — podcastify pipeline + emotional layering + upload-and-share. Vivek is NEVER in the loop.

| Skill | What it does |
|-------|--------------|
| `/podcastify-plus <pdf-path>` | Background agent: full podcastify pipeline + ElevenLabs emotional layering. Outputs enhanced `podcast.mp3` in cwd. No upload. |
| `/podcastify-plus-and-share <pdf-path> [email]` | Composite. Background agent does everything in `/podcastify-plus` PLUS upload-and-share. Default email `vivekjobapp123@gmail.com`. |
| `/download-podcastify-plus-and-share <paper-ref> [email]` | Full chain from paper reference. Orchestrator does synchronous download via `/paper-download-hack`; background agent does the rest. |

These mirror the existing trio in structure. Only the audio-generation step differs: instead of `audify` (OpenAI TTS), the `-plus` variants invoke the ElevenLabs path with emotion layering.

**Exit criteria:**
- [ ] All 3 `-plus` skills written and live in `~/.claude/skills/`
- [ ] Each one is invocable from any cwd, fully autonomous (no orchestrator-side ElevenLabs calls)
- [ ] Existing 3 skills remain UNTOUCHED

---

### Phase 5 — Nakamura-Uhlmann smoke test

**Goal:** Validate `/podcastify-plus-and-share` end-to-end on a real paper.

| Task | Description |
|------|-------------|
| Fire `/podcastify-plus-and-share` on Nakamura-Uhlmann | Paper already downloaded at `runs/nakamura_ulm_inverse_elasticity/papers/`. Use the share variant (not the download variant — no download needed). Background agent produces the ElevenLabs-enhanced podcast, uploads, shares with `vivekjobapp123@gmail.com`. |

**Exit criteria:**
- [ ] Nakamura-Uhlmann enhanced podcast lands in Vivek's Drive
- [ ] Emotional regulation noticeably improved vs the baseline `nova` version
- [ ] No regressions in content accuracy (journal grounding still in place)

---

### Phase 6 — Closing sequence

**Goal:** Snapshot all work done in this roadmap — the 3 new `-plus` skills to dotfiles remote, the project-repo state (this roadmap doc + Phase 2/5 artifacts + any new runs/ subdirs) to the nblm-podcast-api remote.

| Task | Description |
|------|-------------|
| `/sync-os` | Sync `~/.claude/` to the `claude-code-os` dotfiles repo. Detects the 3 new `-plus` skills as drift, copies + commits + pushes. Updates dotfiles README skills count and table. |
| `/gitcommit` | Stage and commit nblm-podcast-api project state: this roadmap doc, any Phase 2 experimentation artifacts, the Phase 5 smoke-test run directory (Nakamura-Uhlmann enhanced version). |
| `/gitpush` | Push the project commit to the nblm-podcast-api remote on origin/master. |
| `/gitreadme` (conditional) | Only if the project README's "Status" or "worked example" sections are now stale because of the `-plus` work. Otherwise skip. |

**Exit criteria:**
- [ ] `claude-code-os/main` contains the 3 `-plus` skill directories + README updated
- [ ] nblm-podcast-api remote is at parity with local (roadmap doc + artifacts committed and pushed)
- [ ] Project README is current (regenerated only if needed)

---

## Out of scope

- Touching the existing 3 podcastify skills (forbidden by Unix-philosophy constraint).
- Author-voice cloning (ElevenLabs supports it; ethically dubious; not needed).
- Per-domain emotion-tag-tuning (theory vs experiment vs essay). Use one tuned profile until evidence of need.
- Additional test papers beyond Nakamura-Uhlmann. Roadmap explicitly ends there.

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| ElevenLabs has no MCP for docs | Low | Fall back to web research via `niche-library-research`. |
| Background agent can't autonomously drive ElevenLabs (Phase 3 gate fails) | High | Roadmap terminates honestly. No half-measures. |
| ElevenLabs cost per podcast is high enough to discourage routine use | Med | Phase 1 should surface the per-character cost so this is known. If prohibitive, Vivek decides whether to proceed. |
| Emotion-tag overuse produces cringe-rich output | Med | Phase 2's manual experimentation is exactly where this calibration happens. |
