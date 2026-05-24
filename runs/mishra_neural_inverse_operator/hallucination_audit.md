# Hallucination Audit — Neural Inverse Operators Podcast

## Summary

23 substantive claims in `narrative_refined.md` were checked against the source paper PDF (arxiv 2301.11167) using verbatim text retrieval over per-page raw extracts. Journal entries with verifiable excerpts and page references live at:

`reconstruction/arxiv_2301.11167/find-evidence-in-paper_arxiv_2301.11167.md`

**Result: 22 of 23 claims SUPPORTS, 1 of 23 PARTIALLY_SUPPORTS (corrected).**

Zero outright hallucinations. One physicist-shorthand overgeneralization tightened in `narrative_final.md`.

## Corrections applied

### Correction 1 — Governing equation for EIT

| Field | Value |
|---|---|
| Journal entry | #23 |
| Page | 3 (section 2.2 Calderon Problem, EIT) |
| Original claim in `narrative_refined.md` | "Maxwell's equations for electrical tomography" |
| Paper says (verbatim) | "the associated PDE (1) is the following elliptic equation, -nabla . a(z) nabla u = 0, z in D" |
| Issue | The paper formulates the EIT forward problem as a static elliptic Poisson-type equation with variable conductivity, not as full Maxwell's equations. The elliptic equation is derivable from Maxwell's under the quasi-static approximation, but the paper itself never names Maxwell's equations. The narrative's phrasing was defensible physicist's shorthand but slightly overgeneralized. |
| Correction | Replaced "Maxwell's equations for electrical tomography" with "an elliptic equation for electrical tomography" to match the paper's framing precisely. |

## All claims verified (clean list)

Each row corresponds to a journal entry in `reconstruction/arxiv_2301.11167/find-evidence-in-paper_arxiv_2301.11167.md`. Read the journal for verbatim excerpts and full evidential commentary.

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Authors: Roberto Molinaro, Yunan Yang, Bjorn Engquist, Siddhartha Mishra | 1 | supports |
| 2 | Affiliations: Molinaro/Mishra at ETH Zurich; Yang at ITS / ETH Zurich; Engquist at UT Austin | 1 | supports |
| 3 | The PDE inverse problems considered map operators to functions | 1 | supports |
| 4 | NIO is the proposed architecture, based on a composition of DeepONets and FNOs | 1 | supports |
| 5 | The composition is DeepONet first, then FNO (stacking order) | 6 | supports |
| 6 | DeepONet is linear in trunk basis, can't do nonlinear mode mixing — FNO is needed for that and final inversion | 6 | supports |
| 7 | The motivating mathematical derivation is done for the inverse wave scattering / Helmholtz problem | 5 | supports |
| 8 | Randomized batching is the training trick — random sample count per training iteration | 7 | supports |
| 9 | NIO tested on 4 problems: Calderon/EIT, inverse wave scattering (Helmholtz), optical imaging (RTE), seismic imaging (acoustic wave) | 9 | supports |
| 10 | Two baselines: DeepONet with CNN branch + fully convolutional image-to-image network | 7 | supports |
| 11 | NIO outperformed baselines significantly on all four problems | 9 | supports |
| 12 | D-bar method on heart-and-lungs EIT phantom has 8.75% error vs. NIO's much lower error | 7 | supports |
| 13 | NIO robust to noise, grid resolution changes, random sensor locations at test time | 8 | supports |
| 14 | NIO degrades gracefully under varying input-sample count; baselines collapse by almost an order of magnitude | 8-9 | supports |
| 15 | NIO vs PDE-constrained optimization on inverse wave scattering: 2.3% vs 11.1% L1 error | 9 | supports |
| 16 | NIO inference <1 sec on CPU; PDE-constrained optimization 8.5 hrs on GPU; NIO 5x more accurate, 4 orders of magnitude faster | 9 | supports |
| 17 | DeepONets and FNOs only map functions to functions, must be adapted for operator-to-function inverse problems | 5 | supports |
| 18 | EIT (Calderon problem) is governed by an elliptic PDE | 3 | supports |
| 19 | This is the first end-to-end machine-learning framework for learning maps between operators and functions | 9 | supports |
| 20 | Classical alternative is iterative PDE-constrained optimization — expensive because each iteration applies forward + adjoint PDE solvers | 1 | supports |
| 21 | Future work: other architectures (LOCA, VIDON, graph-based), 3D scaling for seismic, theoretical approximation bounds | 9 | supports |
| 22 | NIO is several orders of magnitude faster than existing direct and PDE-constrained optimization methods | 1 | supports |
| 23 | Narrative said "Maxwell's equations for electrical tomography" — paper says elliptic equation, never names Maxwell's | 3 | partially_supports -> CORRECTED in narrative_final.md |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or pedagogical scaffolding and was not put through the skill:

- **Opening scenarios (doctor with scan, oil-exploration team, earthquake scientist, materials engineer)** — pedagogical setup illustrating the abstract problem family. These professions and instruments are real, but the paper itself only names the math and the standard benchmark applications (EIT, seismic imaging, optical tomography). Framing language, not load-bearing factual claim about the paper.
- **Analogies** ("eats functions", "square peg / round hole", "the architecture practically designs itself", "guess-and-check loop", "smoking gun") — pedagogical scaffolding, not factual claims.
- **Closing speculation** ("Think about what that means for somebody in a hospital, who used to wait overnight...", "we're not all the way there yet... but the recipe exists now") — clearly framed as the narrator's interpretation, not as a claim the authors make.
- **The "fifty years" historical timeline** for PDE-constrained optimization — rough order-of-magnitude pedagogical framing, defensible against the history of inverse problems (Tarantola, 1987; Chavent, 2010) but not a specific paper claim.
- **The four-step decomposition described in plain English** ("build a basis", "back out the equation's solution", "combine those pieces in a nonlinear way", "do one final inversion") — accurate paraphrase of the four building blocks the paper lists in section 3.3 (Basis Construction, PDE Solve, Mode Mixing, Matrix Inversion). The technical bullet list in the paper is rendered in conversational English; entry #6 captures the underlying mathematical justification.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/arxiv_2301.11167.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py` for all 35 pages.
2. For each substantive claim in `narrative_refined.md`, locating the verbatim supporting excerpt by grep across the per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` to append each verified claim as an indexed journal entry, with verbatim excerpt, page number, structural context, and AI commentary on the evidential relationship.
4. Where the evidential relationship was `partially_supports` (claim 23), the narrative was corrected and the correction is logged here.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. One physicist-shorthand overgeneralization corrected. Safe to ship to TTS.
