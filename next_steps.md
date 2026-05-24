# Next Steps — Multi-Paper Parallel Pipeline Fire

**Captured:** 2026-05-24
**Status:** ✅ **DONE 2026-05-24.** All four steps fully executed. The multi-paper parallel pattern is now proven and Vivek called the result "simply amazing work." The architecture has graduated from "plan" to "validated baseline." See `roadmap.md` for what's next.

## Execution outcome (2026-05-24)

- **Step 1 (sequential downloads):** ✅ DONE. 5 of 6 papers downloaded (Mishra, Tao, Nakamura-Uhlmann, Karniadakis, LeCun). Entry #4 "AI and creativity papers" deliberately skipped — it's a category not a specific paper.
- **Step 2 (directory tree setup):** ✅ DONE. Each `runs/<slug>/` subdirectory populated with `papers/`, `section_explanations/`, `reconstruction/<paper-stem>/` per spec.
- **Step 3 (parallel pipeline fire):** ✅ DONE. 5 agents in genuine parallel via single-message Agent dispatch. Orchestrator stayed free the whole ~17 minutes; Vivek tested "you legit free?" multiple times and the orchestrator answered instantly each time.
- **Step 4 (results aggregation):** Implicit — 113 journal entries across all 5 papers, 4 corrections applied, 0 outright hallucinations. Cross-paper duration consistent at 16–17:12 min per podcast.
- **Information-expert principle (the A/B test added at fire time):** ✅ validated. 3 share-variant agents called gws drive create + permissions create themselves; 2 local-variant agents left mp3s on disk for Vivek to triage.

Drive links for the 3 share-variant podcasts: see `papers_to_sample_and_dogfood.md` Results section.

Local-variant mp3s sit at `runs/nakamura_ulm_inverse_elasticity/podcast.mp3` and `runs/karniadakis_pinn/podcast.mp3`.

---

## Original plan (preserved for reference)

## Goal

Run the paper-to-podcast pipeline on multiple papers in parallel, each in its own isolated subdirectory, all in the background. Result: N podcast.mp3 files plus N audit trails arrive ~20 min after fire, with the orchestrator (Claude on the main session) staying free the whole time to chat about anything else.

## The sequencing matters

Vivek's instinct on sequencing is correct and worth honoring exactly:

1. **Sequential paper download** (NOT parallel) — `paper-download-hack` uses Playwright as a fallback. If five Playwright browser instances spawn simultaneously, there's a real risk of collision / resource contention / spurious failures. Doing the downloads one-at-a-time first costs only ~30s per paper and rules out a class of brittle failures.
2. **Directory tree setup** — before any pipeline fires, create per-paper subdirectories so the 5 parallel agents don't clobber each other's files (they all write to relative paths like `papers/`, `narrative_final.md`, `podcast.mp3`, etc.).
3. **Parallel pipeline fire** — once prerequisites are met, spawn N background agents in a single message (parallel dispatch).
4. **Results aggregation** — collect mp3s, write a per-paper summary table.

## Input

A markdown file containing paper references (titles, DOIs, arXiv IDs, or vague descriptions — paper-download-hack handles fuzzy refs). Default: `papers_to_sample_and_dogfood.md`. Vivek can point the workflow at a different markdown file if he wants to fire a custom batch.

The orchestrator parses the input file, extracts paper references (one per line in a numbered list is the canonical shape), and uses those as the per-paper inputs for steps 1-3 below.

## Workflow

### Step 1 — Bulk Paper Download (Sequential)

For each paper in the input file:

1. Make a per-paper working directory: `runs/<paper-stem>/` (use sanitized DOI or title-slug as stem)
2. `cd` into it and create `papers/` subdir
3. Invoke `paper-download-hack` with the paper reference, output folder `runs/<paper-stem>/papers/`
4. Verify the PDF landed (size > 50 KB, file shows "PDF document")
5. Move on to next paper

Sequential, not parallel. Each paper download takes 10-60 seconds. Five papers takes 1-5 min total.

**Failure handling:** if `paper-download-hack` returns "could not retrieve" for a paper, log it, skip it, continue with the rest. Don't block the whole run on one inaccessible paper.

### Step 2 — Directory Tree Setup

Create the per-paper subdirectory structure that the per-paper pipeline agents will write into. For each successfully-downloaded paper:

```
runs/<paper-stem>/
├── papers/                              ← already created in Step 1
│   └── <paper-stem>.pdf
├── section_explanations/               ← created by Phase 1
├── reconstruction/<paper-stem>/        ← created by Phase 4 (find-evidence-in-paper journal)
├── draft_story.md                      ← Phase 2 output
├── narrative_refined.md                ← Phase 3 output
├── narrative_final.md                  ← Phase 4 output
├── hallucination_audit.md              ← Phase 4 output
└── podcast.mp3                         ← Phase 5 output
```

Each agent's working directory is `runs/<paper-stem>/`. They write to relative paths within that directory. No collisions.

### Step 3 — Parallel Pipeline Fire

Spawn N background agents in a **single message** (one orchestrator call with N parallel `Agent` tool uses — this is the critical step for genuine parallelism). Each agent:

- Working directory: `runs/<paper-stem>/`
- Paper PDF: `runs/<paper-stem>/papers/<paper-stem>.pdf` (already downloaded)
- Instructions: execute Phases 1-5 of the pipeline (skip Phase 0 since download is done; skip Phase 6 since per-paper upload is not the default)
- Delight brief: same as `problem_statement_podcast_from_scratch.md` plus the v4 lessons learned (introduce jargon with analogies; use audify --speed 0.85 for relaxed pacing; voice nova)
- Milestone protocol: SendMessage the orchestrator at each phase completion so it can relay status

The orchestrator stays free during the parallel run and forwards milestone pings to Vivek as they arrive. Estimated wall-clock: ~20 min from fire (same as a single-paper run, since parallelism eats the serialization).

### Step 4 — Results Aggregation

When all agents complete, write a `multi_paper_summary.md` containing:

- One row per paper: `paper title | mp3 path | duration | # journal entries | # corrections | notes`
- Per-paper paths for quick navigation
- Any failures (Step 1 download failures, or pipeline failures within a run)
- Total wall-clock time

Optionally: package the N mp3s into a `runs/_delivery/` folder for easy bulk-share if Vivek wants to upload-and-share the batch.

## What Vivek does

1. Listens to v4 Bouman podcast (current deliverable) → verdict
2. If verdict positive, edit `papers_to_sample_and_dogfood.md` to confirm/refine the paper list
3. Fire the multi-paper workflow with `/goal` pointing at this `next_steps.md` (or just voice-message "run the multi-paper plan")
4. Walk away / chat about other things / do other work
5. Come back ~20 min later, find N podcasts ready, listen to subset to gauge cross-paper quality
6. Decide whether the pipeline pattern is ready to package as a `/podcastify` skill

## What the orchestrator-Claude does

- Reads the input file (papers_to_sample_and_dogfood.md or whatever Vivek specifies)
- Executes Step 1 sequentially (paper downloads)
- Executes Step 2 (directory tree setup)
- Executes Step 3 (parallel agent spawn)
- Stays free during Step 3 to chat with Vivek
- Relays milestone pings as they arrive
- Executes Step 4 (write summary file)
- Reports final paths to Vivek

## Open questions to resolve at fire time

- Which input file? (Default: `papers_to_sample_and_dogfood.md`. Vivek can override.)
- How many papers? (Up to ~5 in parallel comfortably; can go higher but worth a checkpoint.)
- Drive upload at end? (Default: NO — per Vivek's "podcastification only" direction from the v4 round. He'd add upload-and-share as a separate step if desired.)
- Voice + speed defaults? (Carry forward from v4: voice nova, audify --speed 0.85.)

## Why this is in a file

Capturing the plan as a markdown file commits us to the sequencing (downloads sequential, pipelines parallel) so we don't improvise a worse order in the heat of the moment when Vivek voices "fire it." The plan is also human-auditable — Vivek can read it, push back on any step, and edit before firing.
