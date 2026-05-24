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

## The worked example

The repo contains a complete pipeline run against **Berthy T. Feng, Alexander C. Ogren, Chiara Daraio, Katherine L. Bouman, "Visual Vibration Tomography: Estimating Interior Material Properties from Monocular Video"** (CVPR 2022, DOI [10.1109/cvpr52688.2022.01575](https://doi.org/10.1109/cvpr52688.2022.01575)).

Walk the artifacts in this order to retrace the run:

1. `problem_statement_podcast_from_scratch.md` — the spec the run was fired against
2. `section_explanations/00_abstract.md` through `08_conclusion.md` — what Phase 1 produced
3. `draft_story.md` — Phase 2 synthesis
4. `narrative_refined.md` — Phase 3 refinement
5. `reconstruction/10.1109_cvpr52688.2022.01575/find-evidence-in-paper_10.1109_cvpr52688.2022.01575.md` — **the load-bearing audit trail** — 17 journal entries
6. `hallucination_audit.md` — how the audit consumed the journal to produce corrections
7. `narrative_final.md` — the narrative actually narrated in the v4 podcast (13,457 chars, ~14:35 audio at TTS speed 0.85)

The MP3 itself is not in this repo (binary, large, easier to regenerate than to version).

## Hallucination prevention, concretely

The core architectural claim is that hallucination is not a hand-waving aspiration — it's prevented by a build step that writes its own audit trail to disk.

Phase 4 runs the `find-evidence-in-paper` skill (or its sibling `ask-question-about-paper`) once per substantive claim in the narrative. Each invocation:

1. Reads the per-page raw text of the PDF (`reconstruction/<stem>/<stem>_page{N}_raw.txt`)
2. Searches for the verbatim passage that bears on the claim
3. Classifies the evidential relationship: **supports** / **contradicts** / **partially_supports** / **silent**
4. Appends one indexed YAML entry to `reconstruction/<stem>/find-evidence-in-paper_<stem>.md`

Each entry contains the claim, the verbatim excerpt, the page number, the section, surrounding context, and the AI commentary explaining the evidential relationship. The journal is append-only and human-auditable.

If the claim is `contradicted` or `silent` (paper does not address it), the narrative is corrected using the verbatim excerpt as the ground truth. The audit document (`hallucination_audit.md`) records every correction made, so the final narrative's relationship to the paper is traceable end-to-end.

For the Bouman VVT run, 17 journal entries were created (visible in `reconstruction/.../find-evidence-in-paper_*.md`). 16 returned `supports`; 1 returned `partially_supports` (a slight overgeneralization, softened in `narrative_final.md`). Zero `contradicted` claims survived to the final.

## Status

Working, with one paper successfully run end-to-end through v4 of the pipeline. The narrative quality has been iterated four times (v1 too dense → v2 still too academic → v3 "huge improvement" → v4 surgical jargon fix + slower pacing). The architecture, including the autonomous-background-agent pattern, has been validated end-to-end.

Next steps (see the two `..._learning.md` and `..._dogfood.md` files for details):
- **Diverse paper dogfooding** — run the pipeline on a span of papers (Mishra group's Neural Inverse Operator, Tao on AI, Karniadakis SPINN, LeCun world models, etc.) to build a corpus of per-paper artifacts the eventual `/podcastify` skill spec can draw on
- **Empirical style learning** (deferred) — transcribe existing NotebookLM-generated podcasts, pair them with their source papers, extract empirical patterns to replace the current a-priori delight brief

## Reproducing the pipeline

This repo doesn't ship as a CLI; it documents an architecture executed by a Claude Code session driving the listed skills. To reproduce a similar run you would need:

- A working [Claude Code](https://claude.com/claude-code) install
- The skills: `paper-download-hack`, `ask-question-about-paper`, `find-evidence-in-paper`, `text-to-highlight-in-paper`, `audify`, `upload-and-share`, `swarm`, `new-md`
- `OPENAI_API_KEY` in env (for `audify`)
- A Google Workspace CLI (`gws`) auth set up if you want `/upload-and-share`
- `pdftotext`, `ffmpeg`, and a recent Python 3 on PATH

Fire the pipeline against a paper by giving the spec file to Claude Code as a `/goal` and letting the autonomous background agent in `problem_statement_podcast_from_scratch.md` run it.

## License

No license declared. This is a personal research-engineering experiment; reach out before reusing.

## Author

[Vivek Karmarkar](https://github.com/VivekKarmarkar). Built collaboratively with Claude (Opus 4.7, 1M context) over a single iterative session on 2026-05-23/24.
