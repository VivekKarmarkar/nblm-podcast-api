# Hallucination Audit — Physics Informed Deep Learning (Part I) Podcast

## Summary

24 substantive claims in `narrative_refined.md` were checked against the source paper PDF (`papers/arxiv_1711.10561.pdf`) using the `find-evidence-in-paper` skill. Verbatim journal entries with verifiable excerpts and page references are at:

`reconstruction/arxiv_1711.10561/find-evidence-in-paper_arxiv_1711.10561.md`

**Result: 23 of 24 claims SUPPORTS, 1 of 24 PARTIALLY_SUPPORTS (corrected in `narrative_final.md`).**

The narrative had zero outright hallucinations. One quantitative claim was loosened to a colloquial paraphrase.

## Corrections applied

### Correction 1 — Code-snippet line count

| Field | Value |
|---|---|
| Journal entry | #11 |
| Page | 5 (section 2.1 Burgers' Equation) |
| Original claim in `narrative_refined.md` | "the authors show an eight-line code snippet" |
| Paper says | The paper inlines a TensorFlow code snippet defining `def u(t, x)` (3 lines incl. signature) and `def f(t, x)` (7 lines incl. signature) — total ~10 lines of code, plus a blank line and explanatory prose between them. |
| Issue | "Eight lines" is a precise quantitative claim that doesn't match a clean line count of the snippet as printed. |
| Correction | Replaced with: "the authors inline a tiny TensorFlow snippet, basically two short functions, to make the point". Still faithful to the paper's stated motivation ("to highlight the simplicity in implementing this idea") and avoids over-precise quantification. |

## All claims verified (clean list)

Each entry below corresponds to a journal entry in `reconstruction/arxiv_1711.10561/find-evidence-in-paper_arxiv_1711.10561.md`. Read the journal for verbatim excerpts and full evidential commentary.

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Authors: Raissi, Perdikaris, Karniadakis (2017) | 1 | supports |
| 2 | Authors coined "physics informed neural networks" / PINN | 1 | supports |
| 3 | PINNs respect symmetry/invariance/conservation principles | 3 | supports |
| 4 | Method uses automatic differentiation; paper calls auto-diff "underused" in scientific computing | 3 | supports |
| 5 | Physics prior acts as regularization that constrains admissible solutions | 2 | supports |
| 6 | Burgers' equation arises in fluid mechanics, nonlinear acoustics, gas dynamics, traffic flow | 4 | supports |
| 7 | Low-viscosity Burgers develops shocks notoriously hard for classical numerics | 5 | supports |
| 8 | Burgers PINN: 9 layers × 20 neurons, Nu=100, 10,000 collocation points | 6, 8 | supports |
| 9 | Burgers result: 6.7e-4 relative L2 error, ~60s on Titan X GPU, two orders of magnitude better than prior GP work | 7, 8 | supports |
| 10 | Prediction is mesh-free / no spatio-temporal discretization | 7 | supports |
| 11 | A short TensorFlow code snippet is shown to highlight implementation simplicity | 5 | partially_supports → CORRECTED in narrative_final.md |
| 12 | Schrödinger applications: quantum mechanics, optical fibers, Bose-Einstein condensates | 9 | supports |
| 13 | Schrödinger PINN used 20,000 collocation points (Latin Hypercube Sampling) | 11, 12 | supports |
| 14 | Schrödinger result: relative L2 error 1.97e-3 | 11 | supports |
| 15 | In higher dimensions, collocation points grow exponentially (curse of dimensionality) | 11 | supports |
| 16 | Discrete-time PINN used implicit Runge-Kutta with 500 stages — first ever | 14 | supports |
| 17 | Theoretical time-stepping error for q=500, Δt=0.8 is ≈ 10⁻⁹⁷ | 14 | supports |
| 18 | Discrete-time Burgers: single-step t=0.1→0.9, relative L2 error 8.2e-4 | 15 | supports |
| 19 | Allen-Cahn describes phase separation in multi-component alloy systems | 17 | supports |
| 20 | Allen-Cahn discrete-time PINN: 200 sparse measurements, captures sharp internal layers in one step | 18 | supports |
| 21 | PINNs not replacements for classical numerical methods; pitch is coexistence | 20 | supports |
| 22 | No uncertainty quantification — flagged as future work, contrasted with Gaussian processes | 20 | supports |
| 23 | Schrödinger has complex-valued solutions with periodic boundary conditions | 9 | supports |
| 24 | Standard ML methods lack robustness in the small-data regime typical of physical systems | 2 | supports |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or analogy and was not put through the skill:

- **Hook analogies** ("fireplace poker in coals", "drum head ripples", "pollutant smearing down a river", "wave function spreads through space", "air flows around a wing", "blood flows through an aorta", "wildfire across a hillside", "jet engine part") — pedagogical scaffolding, not claims about the paper.
- **"Joseph Fourier wrote down an equation"** — well-known historical fact (Fourier's analytical theory of heat, 1822). Independently verifiable, and the paper itself does not name Fourier.
- **"Modern machine learning crushes image recognition, language, genomics"** — broad introductory framing of the ML moment. The paper's intro itself does cite image recognition [1], NLP [2], cognitive science [3], and genomics [4], so this framing is supported in spirit (page 1).
- **"PINNs have spread across CFD, biomechanics, geophysics, climate, electromagnetics, materials science"** — observation about post-2017 follow-up work in the field, not a claim made by the paper itself. Independently verifiable from the broader scientific machine learning literature.
- **"The equation isn't something you solve, it's something you ENFORCE"** — narrator's reframing of the paper's central conceptual move. Supported in spirit by the paper's framing of the physics term as a constraint inside the loss function.
- **"Hundreds of follow-up papers, whole conferences"** — qualitative summary of post-publication impact; not a claim about this paper specifically.
- **Author intent attributions** ("the authors are very clear", "the authors call this out as a pressing open question") — narrative paraphrasing of the explicit text on page 20 (Section 4 Summary and Discussion + future-work paragraph), which IS the source.
- **Closing reflection** ("the bar with heat creeping along it ... they live in the same loss function") — clearly framed as the narrator's synthesis, not a quoted claim.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/arxiv_1711.10561.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py` for all 22 pages.
2. For each substantive claim, locating the verbatim supporting excerpt via `grep` across all per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` to append each verified claim as an indexed journal entry, with the verbatim excerpt, the page number, the section context, and AI commentary about the evidential relationship.
4. Where the evidential relationship was `partially_supports` (claim 11), the narrative was loosened to a faithful approximation in `narrative_final.md` and the change logged here.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. One quantitative over-precision loosened. Safe to ship to TTS.
