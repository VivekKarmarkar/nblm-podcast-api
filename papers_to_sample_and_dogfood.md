# Papers to Sample and Dogfood

**Captured:** 2026-05-24
**Context:** After v3/v4 of the paper-to-podcast pipeline landed well on Bouman's *Visual Vibration Tomography*, the next step is to run the same pipeline on a diverse spread of papers Vivek personally wants to listen to or already understands well. Knowing the paper well lets Vivek spot subtle errors in the podcast that he couldn't catch in a paper he was learning from. The accumulated runs become a corpus that informs the eventual `/podcastify` skill spec.

## Workflow

Per paper:
1. Vivek voice-messages the paper reference (title + first author, or DOI, or arXiv ID).
2. Claude fires the same autonomous background pipeline used for v3/v4.
3. ~15-20 min later, the mp3 lands locally (or in Drive depending on workflow at the time).
4. Vivek listens and judges.
5. Artifacts from each run (per-section explanations, narrative_final.md, hallucination journal, mp3) accumulate in a per-paper subfolder so we can compare across the corpus later.

## Initial paper list (Vivek's picks)

These are papers Vivek named on 2026-05-24 as good dogfood candidates:

1. **Neural Inverse Operator** — Siddharth Mishra's group
2. **Inverse elasticity** — Nakamura / Ulm / "the inverse theorem" (need to disambiguate which exact paper at run time)
3. **Terence Tao on AI in this age** — Tao's recent essay/paper on AI's role in mathematics
4. **AI and creativity papers** — a few dense / boring-on-purpose ones; useful stress tests for the delight rewrite
5. **Karniadakis SPINN / Physics-Informed Neural Networks** — Karniadakis is the main person; SPINN or PINN paper
6. **Yann LeCun's 2022 world models paper** — "A Path Towards Autonomous Machine Intelligence" or similar

Span deliberately: pure math (Tao), applied physics (Mishra/Karniadakis), continuum mechanics (Nakamura/Ulm), philosophy-of-AI (LeCun/Tao), and the dense/boring stress test. This range exposes how the pipeline performs across paper personalities.

## Goal of the corpus

After 5-10 papers run through, patterns become legible:
- Which section structures the section-discoverer handles well vs poorly
- Which paper types (theory vs experiment vs survey) need different delight-brief tuning
- Which hooks work for different domains
- What recurring hallucination types show up across the journal entries
- Where the audify pacing needs adjustment per domain
- Whether one "delight brief" generalizes or whether the skill needs per-domain knobs

The accumulated data then informs the `/podcastify` skill spec — what knobs it exposes, what defaults it sets per detected paper-type, what the failure modes are.

## Status

✅ **5 of 6 candidates run successfully on 2026-05-24** via the multi-paper parallel pipeline. Entry #4 ("AI and creativity papers") deliberately skipped — it's a category, not a specific paper, so paper-download-hack would have had to guess. See Results below.

## Results (2026-05-24 multi-paper parallel run)

5 background agents in genuine parallel. Single orchestrator dispatch. Wall-clock ~17 minutes for all 5 to complete. 113 journal entries total. 4 corrections applied. 0 outright hallucinations. Audio consistently 16–17:12 min per podcast at voice nova + audify --speed 0.85.

The split (deliberate A/B for the two envisioned skills):

### Share-variant (agents did upload-and-share themselves — `podcastify-and-share` rehearsal)

| # | Paper | Drive link | mp3 | Journal | Notes |
|---|---|---|---|---|---|
| 1 | Mishra — Neural Inverse Operators for Solving PDE Inverse Problems (Molinaro/Yang/Engquist/Mishra, arXiv 2301.11167) | https://drive.google.com/file/d/1TumZY6SXU35jjjLw0XYIdI0pOQ01RF8J/view?usp=drivesdk | 15.5 MB / 16:11 | 23 entries: 22 supports, 1 partially_supports → CORRECTED (Maxwell's-equations → elliptic equation for EIT, paper never names Maxwell) | Vivek listened and called out the N-to-D operator explanation as teaching him something NotebookLM hadn't |
| 3 | Tao — Mathematical methods and human thought in the age of AI (arXiv 2603.26524) | https://drive.google.com/file/d/1ZVAfUlp7ewvbBY1QiS1dpZFlGLxodn_e/view?usp=drivesdk | ~16 MB | 20/20 supports + 2 defensive tightenings logged | Hook: 3 AI agents interrupting the authors; close: genie + clear the smoke |
| 6 | LeCun — A Path Towards Autonomous Machine Intelligence (OpenReview BZ5a1r-kVsf, v0.9.2 June 2022) | https://drive.google.com/file/d/1QcAR9pUaHmh2uX5AFI_DDnocX5ulb7Fl/view?usp=drivesdk | 16.5 MB / 17:12 | 26/26 supports, zero corrections | Hook: sippy cup; close: "go watch a kid drop a cup, that's the benchmark." Also: the cheeky "no frontier lab has shipped this" line conveniently leaves out Anthropic |

All three shared with `vivekjobapp123@gmail.com` (reader role).

### Local-variant (mp3 sits in `runs/<slug>/podcast.mp3` for Vivek to triage — `podcastify` rehearsal)

| # | Paper | Local mp3 path | Journal | Notes |
|---|---|---|---|---|
| 2 | Nakamura-Uhlmann — Global uniqueness for an inverse boundary problem arising in elasticity (DOI 10.1007/BF01231541, 1994 Inventiones) | `runs/nakamura_ulm_inverse_elasticity/podcast.mp3` (15.0 MB / 16:23) | 20/20 supports, zero corrections | "Ulm" → "Uhlmann" disambiguation made (voice transcription dropped the "hmann"). Diagonalization framed as "tangled piano whose strings sympathetically vibrate." Closer: "Push on it. Watch how it pushes back. The inside is right there, in the reply." |
| 5 | Karniadakis — Physics Informed Deep Learning Part I (Raissi/Perdikaris/Karniadakis, arXiv 1711.10561, 2017) | `runs/karniadakis_pinn/podcast.mp3` (15.2 MB / 16:10) | 24 entries: 23 supports, 1 partially_supports → CORRECTED ("eight-line code snippet" → "tiny TensorFlow snippet, basically two short functions") | Hook: iron poker in coals → Fourier's heat equation → ML cultural gap |

### Entry #4 status

Entry #4 "AI and creativity papers" was not run because it's a category description, not a paper reference. paper-download-hack would have done a Crossref search and picked something arbitrary. The category is preserved here as **STILL PENDING** — if Vivek wants to fire it later, he should provide a concrete title (e.g., "Boden 2003 The Creative Mind," "Bengio 2023 creativity and deep learning," or whichever specific paper he had in mind).

## Verdict from the run

Cross-paper delight brief generalizes well across pure math (Nakamura-Uhlmann), applied physics (Karniadakis), ML (Mishra), AI philosophy (Tao, LeCun), and continuum mechanics. The single delight brief held without per-domain tuning. Information-expert principle (agents do their own upload-and-share) validated.

Per the `roadmap.md`, the next step is to package the proven pipeline as 3 globally-available skills (`/podcastify`, `/podcastify-and-share`, `/download-podcastify-and-share`).
