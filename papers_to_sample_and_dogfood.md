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

Awaiting Vivek to fire the first paper from this list via voice message after he's done listening to v4 of the Bouman podcast.
