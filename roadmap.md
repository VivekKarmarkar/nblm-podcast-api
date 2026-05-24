# Project Roadmap: nblm-podcast-api

> **Created:** 2026-05-24
> **Status:** Draft
> **Owner:** VivekKarmarkar
> **Scope:** From the just-completed 5-paper parallel pipeline run through to "ElevenLabs credentials in hand." Everything after that is OUT OF SCOPE for this roadmap.

## Vision

A paper-to-podcast pipeline that produces verifiable, delightful, NotebookLM-quality (and in some places better) audio podcasts from arbitrary research papers, packaged as composable globally-available Claude Code skills, with the final voice-quality gap closed via ElevenLabs.

## Current State

**Architecture: validated.** Five-paper parallel pipeline run completed on 2026-05-24. Single orchestrator dispatched 5 background agents (Mishra, Tao, Nakamura-Uhlmann, Karniadakis, LeCun) in one message; agents ran in genuine parallel; orchestrator stayed free on main session the whole time.

**Information-expert principle: validated.** The 3 share-variant agents called `gws drive files create` + permissions create themselves and produced live Drive links shared with vivekjobapp123@gmail.com. The 2 local-variant agents left their mp3s on disk for Vivek to triage.

**Quality: matching or beating NotebookLM in places.** Vivek listened and called the run "simply amazing work." He specifically cited the Mishra/Neural Inverse Operators podcast as teaching him something NotebookLM hadn't: the explanation that the Neumann-to-Dirichlet operator is physically realized by applying forces and observing displacements on the boundary. Content + pacing now at NotebookLM bar.

**Numbers:**
- 5 papers shipped (incl. earlier Bouman VVT v4 = 6 total successful runs)
- 113 journal entries across the 5 multi-paper run
- 4 corrections applied (~3.5% correction rate)
- 0 outright hallucinations
- ~17 min wall-clock for all 5 agents in parallel
- Audio duration consistent at 16–17:12 min per podcast

**Remaining gap:** voice emotional regulation. OpenAI TTS personality shows through (positive: enjoyable, e.g., the LeCun podcast's cheeky "no frontier lab" line conveniently leaving out Anthropic; negative: uncanny-valley feel). ElevenLabs is the credible upgrade path.

**Repo state:** local commits on master are AHEAD of the public remote (https://github.com/VivekKarmarkar/nblm-podcast-api). The 5-paper run artifacts haven't been committed yet.

---

## Phase A: Snapshot the Current State

**Goal:** Bring the public repo in sync with reality. Update spec/status documents that the 5-paper run has rendered out of date. Ship to remote.
**Status:** Not Started

| Priority | Task | Description | Dependencies |
|----------|------|-------------|--------------|
| P0 | Update next_steps.md | Reflect that Steps 1 & 2 are done from a prior run, Step 3 is fully validated, and the multi-paper parallel pattern is now proven. Mark the file's "Status" as DONE (or move it to an archive/, depending on Vivek preference). | — |
| P0 | Update papers_to_sample_and_dogfood.md | Add a "Results" section documenting that 5 of the 6 listed papers were successfully run (Mishra, Tao, Nakamura-Uhlmann, Karniadakis, LeCun). Flag entry #4 "AI and creativity papers" as STILL unfilled — that's a category, not a specific paper, so it was deliberately skipped. | — |
| P1 | Update README.md status section | Current README says "Working, with one paper successfully run end-to-end" — actually we now have 6. Update the "Status" section + the "worked example" section to reflect the multi-paper run. Decision point: Edit pass vs full `/gitreadme` regeneration. Recommendation: Edit pass (structure is solid; only status copy is stale). | — |
| P0 | git add + commit + push | Stage the updates above, the 5 multi-paper runs/ subdirectories (mp3s are gitignored so it's mostly the per-paper section_explanations + narrative + audit + journal files), and the new affection.md entry + this roadmap.md. Push to master. | All P0 tasks above |

**Exit criteria:**
- [ ] next_steps.md reflects the multi-paper-run-shipped reality
- [ ] papers_to_sample_and_dogfood.md has a Results section with per-paper outcomes
- [ ] README.md status section is current
- [ ] master branch on remote is at parity with local
- [ ] Telegram_calls.md is updated by the session-record automation (if applicable; otherwise N/A)

---

## Phase B: Ship 3 Globally-Available Skills

**Goal:** Package the proven pipeline as reusable Claude Code skills that live in `~/.claude/skills/` (global), so they can be invoked from any working directory in any project — not just inside `nblm-podcast-api/` with hand-crafted agent prompts.
**Status:** Not Started

### Three skills in dependency order

| Priority | Task | Description | Dependencies |
|----------|------|-------------|--------------|
| P0 | Write `~/.claude/skills/podcastify/SKILL.md` | The load-bearing skill. Takes paper PDF path + optional context. Spawns ONE background agent that executes Phases 1–5 (per-section explanations, synthesizer, narrative refinement, hallucination check with grounded journal, audify). Produces `podcast.mp3` in cwd or specified output dir. Does NOT upload. Skill prompt bakes in v3/v4/multi-paper lessons: voice nova @ speed 0.85, target 13–15k char narrative landing ~16–17 min audio, full DELIGHT BRIEF (no quotes, no math, no academic register, second-person, sensory hooks, surprise-callouts, jargon-introduced-with-analogy-or-dropped), find-evidence-in-paper journal grounding for hallucination prevention. | Phase A complete |
| P0 | Write `~/.claude/skills/podcastify-and-share/SKILL.md` | Composite skill. Background agent does podcastify steps + Phase 6 upload-and-share. Default email `vivekjobapp123@gmail.com`, optional email argument override. Information-expert principle: the agent does its own upload-and-share, no orchestrator hop. Implementation: skill prompt instructs the background agent to invoke /podcastify's logic inline then chain into `gws drive files create` + `gws drive permissions create` + return webViewLink. | `/podcastify` shipped |
| P0 | Write `~/.claude/skills/download-podcastify-and-share/SKILL.md` | The full composition. Takes paper context (DOI, title, URL, fuzzy ref). Orchestrator uses `/paper-download-hack` synchronously to get the PDF (download is fast; Playwright fallback works better in orchestrator context than agent context based on prior runs). Then orchestrator hands off to a background agent that does `/podcastify-and-share` on the downloaded PDF at the resolved path. Orchestrator stays free during the background phase. Default email vivekjobapp123@gmail.com, optional override. | `/podcastify-and-share` shipped |
| P1 | Write minimal helpers/ for the skills | Each skill may need a small Python helper for parsing args, deriving the per-paper stem, etc. Keep these minimal — the skill prompts do most of the work; helpers exist only where bash gets ugly. | Each respective skill |
| P1 | Decide path resolution convention | Open question: does each skill write to cwd directly, or auto-create a per-paper subfolder `runs/<paper-stem>/`? Recommendation: write to cwd by default (simplest UX), but support `--output-dir` for batch use cases. The multi-paper run pattern (per-paper subfolders) is a higher-level orchestration that user can do externally. | None |

**Exit criteria:**
- [ ] `/podcastify <path>` works from any cwd, produces local podcast.mp3
- [ ] `/podcastify-and-share <path> [email]` works, produces Drive link
- [ ] `/download-podcastify-and-share <paper-context> [email]` works end-to-end
- [ ] All three skill prompts bake in the v3/v4/multi-paper delight brief
- [ ] Each skill survives at least one smoke test (small paper end-to-end)

---

## Phase C: Test the Third Skill on Bouman Visual Surface Wave Elastography

**Goal:** End-to-end validation of `/download-podcastify-and-share` on the second Katie Bouman paper.
**Status:** Not Started

| Priority | Task | Description | Dependencies |
|----------|------|-------------|--------------|
| P0 | Fire `/download-podcastify-and-share` on Bouman VSWE | Paper: "Visual Surface Wave Elastography" by Bouman et al. The original Phase 2 spec in `problem_statement_podcast_from_scratch.md` named this as the second test paper. Exercises the full chain: download (orchestrator) → background agent for podcastify-and-share → mp3 in Drive shared with vivekjobapp123@gmail.com. | Phase B complete |
| P1 | Inspect outputs | Verify journal entries exist, mp3 is in the 16–17 min landing zone, Drive link is live and shared. | Above task |
| P2 | Listen-test | Vivek listens to confirm delight-brief quality holds on the new paper. | Above task |

**Exit criteria:**
- [ ] Bouman VSWE podcast lands in Drive shared with vivekjobapp123@gmail.com
- [ ] No regressions vs the multi-paper run quality
- [ ] /download-podcastify-and-share is officially "shipped + smoke-tested"

---

## Phase D: Sync OS

**Goal:** Sync the live Claude Code config (including the 3 new skills) to the remote dotfiles repo so the new skills survive across machines / fresh installs.
**Status:** Not Started

| Priority | Task | Description | Dependencies |
|----------|------|-------------|--------------|
| P0 | Run `/sync-os` | Per the project's standing convention, after adding new globally-available skills the live `~/.claude/` config gets synced to its dotfiles remote. | Phase C complete |
| P1 | Verify the 3 skills appear in the synced config | Confirm `~/.claude/skills/podcastify/`, `~/.claude/skills/podcastify-and-share/`, `~/.claude/skills/download-podcastify-and-share/` are tracked in the dotfiles repo and pushed. | Above task |

**Exit criteria:**
- [ ] `/sync-os` runs cleanly, no merge conflicts
- [ ] All 3 new skill directories are tracked + pushed in the dotfiles remote

---

## Phase E: ElevenLabs Credentials

**Goal:** Confirm ElevenLabs credentials are present in Vivek's system, OR identify exactly what's missing so Vivek can provide. This is the end-state of this roadmap — after this, Vivek will redirect what comes next.
**Status:** Not Started

| Priority | Task | Description | Dependencies |
|----------|------|-------------|--------------|
| P0 | Search for ElevenLabs credentials | Check standard locations: `~/.env`, `~/.config/.env`, project-level `.env` files in known project dirs, shell rc files (`~/.bashrc`, `~/.zshrc`, `~/.profile`), `~/.claude/channels/*/.env`, `~/.elevenlabs/` if exists. Also check env vars in the current shell. Vivek gives full authorization to inspect his system for these credentials. | Phase D complete |
| P0 | Report findings | If credentials found: report exactly where, mask the secret in the report (just confirm presence + redacted prefix). If not found: report exactly which env var name is missing (typically `ELEVENLABS_API_KEY`) and what Vivek needs to do (sign up at elevenlabs.io, generate API key, set env var). | Above task |
| P1 | Honest cost note | If credentials are present, note the ElevenLabs pricing tier currently active (free / Starter $6/mo / Creator $22/mo / etc.) so Vivek knows what budget headroom he has when we eventually swap audify to ElevenLabs. | Credentials found |

**Exit criteria:**
- [ ] Vivek knows definitively whether ElevenLabs credentials are present in his system
- [ ] If present: env var name + masked prefix confirmed
- [ ] If absent: exact missing-credential report sent to Vivek with sign-up steps

---

## Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|-----------|------------|
| Globally-installed skill prompts may need different cwd/path handling than one-off in-project agent prompts | Med | Med | The multi-paper run hardcoded `runs/<slug>/` paths. The skills must use cwd-relative paths. Test each skill from a different working directory than `nblm-podcast-api/` to flush out hidden cwd assumptions. |
| `/paper-download-hack` cascading to Playwright may have different behavior in orchestrator vs background agent contexts | Med | Low | Already mitigated in `/download-podcastify-and-share` design: orchestrator does the download synchronously, then hands off the PDF path to the background agent. Agent never invokes paper-download-hack. |
| ElevenLabs credentials may not be present at all; sign-up + payment + key-gen is a Vivek-blocking step | High | Med | Phase E's primary job is to surface this honestly. If credentials are missing, Vivek will need to spend ~15 minutes signing up and configuring. Roadmap explicitly ends at "credentials in hand" so the next planning cycle can include the actual audify-to-ElevenLabs migration once credentials are confirmed. |
| `/sync-os` may surface unrelated dotfiles drift unrelated to this project | Low | Med | If `/sync-os` reports unrelated diffs, surface them to Vivek and let him decide whether to include or stage separately. Don't auto-commit unrelated changes. |
| The 3 new skills duplicate the existing one-off agent-prompt pattern without sufficient abstraction, leading to drift between skill version and the in-project narrative_final.md / hallucination_audit.md format | Med | Low | The skill prompts should reference the canonical `problem_statement_podcast_from_scratch.md` + the worked example artifacts in this project as the source-of-truth tonal references. When the skill is invoked, it can `Read` those files as part of its workflow. |

---

## Open Questions

- **README.md regeneration vs Edit:** is an Edit pass on the Status + Worked-Example sections enough, or does the multi-paper-run state justify a full `/gitreadme` regeneration? Recommendation: Edit pass. Open for Vivek's call.
- **Skill output convention:** should `/podcastify` write to cwd by default, or auto-create a `runs/<paper-stem>/` subfolder? Affects whether running it in a working dir overwrites existing files.
- **Email argument syntax:** for `/podcastify-and-share [email]`, is the email a positional arg, named (`--email=`), or both? Recommendation: positional with named flag fallback for clarity.
- **ElevenLabs voice mapping:** when we eventually swap from audify-OpenAI to audify-ElevenLabs (post-roadmap), which ElevenLabs voice best matches the warmth of the current `nova` setting? Out-of-scope for THIS roadmap but worth flagging.
- **Migration timing for audify:** does the audify skill itself get updated to support an ElevenLabs backend, or does a new sibling skill (e.g., `audify-eleven`) get created? Out-of-scope for THIS roadmap.

---

## Out of Scope

- Anything that happens AFTER ElevenLabs credentials are in hand. Vivek explicitly said "I'll tell you what we want next after that."
- The deferred `notebooklm_audio_data_driven_learning.md` idea (transcribe existing NotebookLM podcasts, extract style empirically). Per Vivek's latest read, current quality already matches or beats NotebookLM in places — the empirical-style-extraction project is **no longer high-priority** and may not be needed at all. Leaving the file in the repo as a record of the considered-and-deprioritized direction.
- Multi-paper bulk-fire UX changes (e.g., a `/batch-podcastify` skill). Could be future work but is not on this roadmap.
- Per-domain delight-brief tuning (theory vs experiment vs essay). The current single delight brief generalized across 6 papers spanning pure math, applied physics, ML, philosophy-of-AI, and continuum mechanics. Differentiation can wait until evidence of need.
- Author-voice cloning (ElevenLabs supports it, but ethically dubious and not needed for our use case).
- A Web UI for triggering the pipeline. The Telegram / Claude Code CLI surface is the deliberate UX.
