# nblm-podcast-api

A paper-to-podcast pipeline that turns a research-paper PDF into a single-host narrative audio episode, with hallucination prevention built into the architecture.

## Overview

Most "AI podcast" tools are black boxes — give them a paper, get back an audio file, hope the contents aren't drifting from what the paper actually says. This project is the opposite: a composable pipeline of [Claude Code](https://claude.com/claude-code) skills where every substantive factual claim in the final narrative is **grounded in a verbatim excerpt** from the source PDF, with the grounding evidence written to disk as part of the build.

The aesthetic target is something like NotebookLM's two-host podcasts, transposed to single-host narration via OpenAI TTS. The accuracy guarantee is something NotebookLM doesn't offer: a per-paper journal file with one indexed YAML entry per claim, each containing the claim, the verbatim PDF excerpt that bears on it, the page citation, and the AI's classification of the evidential relationship (supports / contradicts / partially_supports / silent).

This repo is the **specification, intermediate artifacts, and worked example** for that pipeline. It is not a packaged tool you can `pip install`. It documents an architecture and one working run of it.

## The pipeline (7 phases)

| Phase | What happens | Load-bearing skill |
|---|---|---|
| 0 | Download the paper PDF | `paper-download-hack` (curl → Unpaywall → Playwright → Sci-Hub cascade) |
| 1 | Section discovery + per-section explanations | parallel agent swarm |
| 2 | Synthesize per-section explanations into one story draft | one synthesizer agent |
| 3 | Refine into a hook + 6-beat narrative arc | Claude orchestrator |
| 4 | Hallucination check — generate verification questions, ground each against the PDF | `find-evidence-in-paper`, `ask-question-about-paper` |
| 5 | Convert verified narrative to MP3 | `audify` (OpenAI TTS) |
| 6 | Deliver | `upload-and-share` (Google Drive) — optional, often handled as a separate composition |

The "delight brief" applied to all prose-generating phases: target 12–14 min audio, zero direct quotes (conversational paraphrase only), zero math notation, second-person address, sensory hooks, surprise-callouts, no academic register, technical terms either avoided or introduced with analogies the way `mode` is introduced with guitar / wineglass / drum examples.

## What's in this repo

```
problem_statement.md                    Original motivation: the 4-level escalation ladder
                                        from computer-use to background-agent architecture
problem_statement_podcast_from_scratch.md  The actual build spec — 7 phases, delight brief
CLAUDE.md                               Project-level rules + the load-bearing skills list

phase1_verdict.md                       Output of the Phase 1 feasibility swarm
                                        (8 research agents on Google's NotebookLM API)
phase1_5_recommendation.md              Output of the Phase 1.5 substitute-research swarm
                                        (Podcastfy vs ElevenLabs vs build-it-ourselves)

section_explanations/                   Per-section breakdowns of the worked example
                                        (Bouman et al., Visual Vibration Tomography, CVPR 2022)
draft_story.md                          Phase 2 synthesizer output
narrative_refined.md                    Phase 3 hook + arc draft
narrative_final.md                      Post-hallucination-check, the narrative actually
                                        narrated in the podcast
hallucination_audit.md                  The audit log citing journal entries

reconstruction/<paper-stem>/
  find-evidence-in-paper_<paper-stem>.md   The load-bearing journal — N indexed YAML
                                            entries, each with verbatim PDF excerpt +
                                            page citation + evidential classification

papers_to_sample_and_dogfood.md         Future-work: papers to run the pipeline on next
notebooklm_audio_data_driven_learning.md Future-work: transcribe existing NotebookLM
                                        outputs to empirically ground the delight brief
                                        (deferred until GPU setup)

affection.md                            A separate, less serious tradition
```

The actual paper PDFs, the per-page raw text files, and the generated MP3s are deliberately **not** tracked in git (see `.gitignore`) — papers are copyright-sensitive, MP3s are large binary artifacts, and the per-page raw text is essentially the full paper text in plain form.

## The worked examples

The repo contains complete pipeline runs against **six** papers, exercising every part of the architecture.

**Reference run (root-level artifacts):** Berthy T. Feng, Alexander C. Ogren, Chiara Daraio, Katherine L. Bouman, *"Visual Vibration Tomography: Estimating Interior Material Properties from Monocular Video"* (CVPR 2022, DOI [10.1109/cvpr52688.2022.01575](https://doi.org/10.1109/cvpr52688.2022.01575)). This is the canonical run, iterated through v1 → v4.

**Multi-paper parallel run (per-paper subdirectories under `runs/`):** Five more papers, spanning pure math, applied physics, ML, and AI philosophy, run as 5 background agents in genuine parallel via a single-message dispatch:

| Run dir | Paper |
|---|---|
| `runs/mishra_neural_inverse_operator/` | Molinaro/Yang/Engquist/Mishra — Neural Inverse Operators for Solving PDE Inverse Problems (arXiv 2301.11167) |
| `runs/nakamura_ulm_inverse_elasticity/` | Nakamura-Uhlmann — Global uniqueness for an inverse boundary problem arising in elasticity (1994 Inventiones) |
| `runs/tao_ai_in_this_age/` | Terence Tao — Mathematical methods and human thought in the age of AI (arXiv 2603.26524) |
| `runs/karniadakis_pinn/` | Raissi/Perdikaris/Karniadakis — Physics Informed Deep Learning Part I (arXiv 1711.10561) |
| `runs/lecun_2022_path_autonomous_machine_intelligence/` | Yann LeCun — A Path Towards Autonomous Machine Intelligence (OpenReview, June 2022) |

For any of the runs, walk the artifacts in this order to retrace:

1. `problem_statement_podcast_from_scratch.md` (root) — the spec the run was fired against
2. `section_explanations/` — what Phase 1 produced
3. `draft_story.md` — Phase 2 synthesis
4. `narrative_refined.md` — Phase 3 refinement
5. `reconstruction/<paper-stem>/find-evidence-in-paper_<paper-stem>.md` — **the load-bearing audit trail**, an indexed YAML journal
6. `hallucination_audit.md` — how the audit consumed the journal to produce corrections
7. `narrative_final.md` — the narrative actually narrated in the podcast

MP3s are not tracked in git (binary, large, easier to regenerate than to version). The Drive links for the share-variant podcasts are in `papers_to_sample_and_dogfood.md`.

## Hallucination prevention, concretely

The core architectural claim is that hallucination is not a hand-waving aspiration — it's prevented by a build step that writes its own audit trail to disk.

Phase 4 runs the `find-evidence-in-paper` skill (or its sibling `ask-question-about-paper`) once per substantive claim in the narrative. Each invocation:

1. Reads the per-page raw text of the PDF (`reconstruction/<stem>/<stem>_page{N}_raw.txt`)
2. Searches for the verbatim passage that bears on the claim
3. Classifies the evidential relationship: **supports** / **contradicts** / **partially_supports** / **silent**
4. Appends one indexed YAML entry to `reconstruction/<stem>/find-evidence-in-paper_<stem>.md`

Each entry contains the claim, the verbatim excerpt, the page number, the section, surrounding context, and the AI commentary explaining the evidential relationship. The journal is append-only and human-auditable.

If the claim is `contradicted` or `silent` (paper does not address it), the narrative is corrected using the verbatim excerpt as the ground truth. The audit document (`hallucination_audit.md`) records every correction made, so the final narrative's relationship to the paper is traceable end-to-end.

Across all 8 OpenAI-baseline runs (6 original + Bouman VSWE smoke test + FNO Phase 2 baseline): **~168 journal entries**, **5 corrections** applied, **0 outright hallucinations**. ~3% correction rate. For the reference Bouman VVT run alone: 17 entries, 16 supports + 1 partially_supports (the overgeneralization documented in `hallucination_audit.md`).

## Status

**Working, validated across 8 papers end-to-end, and now with an ElevenLabs-enhanced sibling track.** The reference Bouman VVT run was iterated v1 → v4 to tune the delight brief; the subsequent multi-paper parallel run shipped 5 more papers (Mishra, Tao, Nakamura-Uhlmann, Karniadakis, LeCun) using the v4-tuned brief in a single ~17 minute wall-clock parallel dispatch. Bouman VSWE was added as the smoke test of `/download-podcastify-and-share`. FNO (Li et al. ICLR 2021) was added as the Phase 2 manual ElevenLabs experimentation. The autonomous-background-agent architecture and the information-expert principle for upload-and-share were validated; the background-agent feasibility gate for ElevenLabs autonomy was also empirically passed.

Audio quality at voice `nova` + `audify --speed 0.85` lands consistently at 16–17 min per podcast. Content + pacing now match or beat NotebookLM in places — see e.g. the Mishra/N-to-D operator explanation that grounded the abstract operator-in / operator-out architecture as the physical "apply forces and watch displacements on the boundary" mapping.

**The ElevenLabs upgrade path has shipped.** Four new globally-available skills (`/audify-eleven`, `/podcastify-plus`, `/podcastify-plus-and-share`, `/download-podcastify-plus-and-share`) mirror the original audify + podcastify trio but use ElevenLabs `eleven_v3` with Matilda voice + inline audio tags (`[warmly]`, `[excited]`, `[awe]`, `[whispers]`, `[sighs]`, etc.) for emotional regulation. The existing 4 skills (`audify`, `podcastify`, `podcastify-and-share`, `download-podcastify-and-share`) remain untouched as the OpenAI-TTS baseline. See `podcastify-plus-with-eleven-labs.md` for the build roadmap and `runs/fno_li2020/narrative_v3_tagged.md` for the reference hand-crafted tagged-narrative format. Nakamura-Uhlmann was used as the Phase 5 smoke test of the shipped `/podcastify-plus-and-share` skill — 53 tags, 16:06 enhanced mp3, baseline preserved in parent dir.

Shipped via the `podcastify-plus-with-eleven-labs.md` roadmap (all 6 phases complete, 2026-05-24):
- ✅ Phase 1 ElevenLabs capability research (5 parallel lanes, official MCP confirmed, v3 tag taxonomy documented)
- ✅ Phase 2 FNO manual experimentation (baseline + hand-tagged + enhanced, shared to vivekjobapp123@gmail.com)
- ✅ Phase 3 background-agent feasibility gate (passed empirically on 700-char test narrative)
- ✅ Phase 4 4 -plus skills shipped (audify-eleven + 3 podcastify-plus variants)
- ✅ Phase 5 Nakamura-Uhlmann smoke test of `/podcastify-plus-and-share`
- ✅ Phase 6 closing sequence (sync-os + gitcommit + gitpush)

*No longer high-priority:* the originally-planned empirical-style-extraction project in `notebooklm_audio_data_driven_learning.md` — current quality already matches/beats NotebookLM in places, so transcribing NotebookLM episodes to learn its style isn't the right next investment.

## Reproducing the pipeline

This repo doesn't ship as a CLI; it documents an architecture executed by a Claude Code session driving the listed skills. To reproduce a similar run you would need:

- A working [Claude Code](https://claude.com/claude-code) install
- The skills: `paper-download-hack`, `ask-question-about-paper`, `find-evidence-in-paper`, `text-to-highlight-in-paper`, `audify`, `upload-and-share`, `swarm`, `new-md` (OpenAI-baseline track) — and for the ElevenLabs track: `audify-eleven`, `podcastify-plus`, `podcastify-plus-and-share`, `download-podcastify-plus-and-share`
- `OPENAI_API_KEY` in env (for `audify`) — and for the ElevenLabs track, `ELEVENLABS_API_KEY` (Starter tier or higher; free tier blocks API library voices with HTTP 402)
- A Google Workspace CLI (`gws`) auth set up if you want `/upload-and-share`
- `pdftotext`, `ffmpeg`, and a recent Python 3 on PATH (plus `pip install --user elevenlabs` for the ElevenLabs track)

Fire the pipeline against a paper by giving the spec file to Claude Code as a `/goal` and letting the autonomous background agent in `problem_statement_podcast_from_scratch.md` run it.

## License

No license declared. This is a personal research-engineering experiment; reach out before reusing.

## Author

[Vivek Karmarkar](https://github.com/VivekKarmarkar). Built collaboratively with Claude (Opus 4.7, 1M context) over iterative sessions on 2026-05-23/24, with the ElevenLabs-enhanced sibling track added on 2026-05-24.
