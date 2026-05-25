# Hallucination Audit — Fourier Neural Operator Podcast (Li et al. 2020/2021)

## Summary

26 substantive claims in `narrative_refined.md` were checked against the source paper PDF using the `find-evidence-in-paper` skill. Verbatim journal entries with verifiable excerpts and page references are at:

`reconstruction/arxiv_2010.08895/find-evidence-in-paper_arxiv_2010.08895.md`

**Result: 25 of 26 claims SUPPORTS, 1 of 26 OVERSTATED (corrected in `narrative_final.md`).**

The narrative had zero outright hallucinations. One quantitative claim about competing methods on Navier-Stokes was overstated and was tightened in `narrative_final.md`.

## Corrections applied

### Correction 1 — Competing methods' error on turbulent Navier-Stokes

| Field | Value |
|---|---|
| Journal entry | #24 (cross-referenced against Table 1 on page 8) |
| Page | 3 (Contributions) and 8 (Table 1) |
| Original claim in `narrative_refined.md` | "The competing methods? Twenty percent and up." |
| Paper says (verbatim from Table 1, viscosity 1e-4, N=10000) | U-Net: 0.1190 (11.9% error), TF-Net: 0.1168 (11.7% error), ResNet: 0.2311 (23.1% error). FNO-3D: 0.0820 (8.2%). |
| Issue | "Twenty percent and up" only applies to ResNet; U-Net and TF-Net both land at ~12%, not above 20%. The original phrasing overstates how far behind ALL competitors were. |
| Correction | Replaced with: "The competing image-style networks all land at twelve percent or higher, with the weakest of them above twenty." |

### Note on Correction 2 — Initially flagged, then RETRACTED

| Field | Value |
|---|---|
| Journal entry | #12 (initial flag) → #13 (retraction) |
| Claim | "Beats every competitor by close to a factor of ten. Almost an order of magnitude." (Darcy Flow) |
| Initially flagged because | The paper's "Our Contributions" bullet mentions "60% lower" error on Darcy at fixed resolution. 60% is a factor of 2.5 reduction, not a factor of 10. |
| Retraction reason | Section 5.2 (page 8) of the paper itself reads: "The proposed Fourier neural operator obtains nearly one order of magnitude lower relative error compared to any benchmarks." The narrative's "almost an order of magnitude" is therefore the paper's own phrasing. No correction needed. |

## All claims verified (clean list)

Each entry below corresponds to a journal entry in `reconstruction/.../find-evidence-in-paper_arxiv_2010.08895.md`. Read the journal for verbatim excerpts and full evidential commentary.

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Lead author Zongyi Li; Caltech and Purdue affiliations; Anandkumar group | 1 | supports |
| 2 | Published at ICLR 2021 | 1 (banner) | supports |
| 3 | Classical NNs learn finite-dim mappings; neural operators learn function-space mappings | 1 | supports |
| 4 | Up to 3 orders of magnitude faster than traditional PDE solvers | 1 | supports |
| 5 | First ML method to model turbulent flows with zero-shot super-resolution | 1 | supports |
| 6 | Airfoil design as motivating example (inverse problem needing thousands of forward evals) | 1 | supports |
| 7 | Traditional FEM/FDM trade-off: coarse=fast/inaccurate vs fine=accurate/slow | 1 | supports |
| 8 | Classical NNs tied to a specific discretization | 1 | supports |
| 9 | Neural-FEM trains one network per PDE instance | 2 | supports |
| 10 | First work to learn resolution-invariant operator for turbulent Navier-Stokes | 3 | supports |
| 11 | Zero-shot super-resolution: train low, evaluate high | 3 | supports |
| 12 | 30%/60%/30% error reduction at fixed 64x64 | 3 | supports (with caveat → see entry 13) |
| 13 | Darcy: "nearly one order of magnitude" lower error | 8 | supports |
| 14 | 0.005s inference vs 2.2s pseudo-spectral on 256x256 grid | 3 | supports |
| 15 | Integral kernel parameterized directly in Fourier space | 1 | supports |
| 16 | kmax_j = 12 sufficient for all tasks | 6 | supports |
| 17 | Fourier layers are discretization-invariant by construction | 6 | supports |
| 18 | Trained on 64x64x20, evaluated on 256x256x80 super-resolution test | 9 | supports |
| 19 | Bayesian inverse problem: 2.5 min (FNO) vs >18 hours (solver) | 9 | supports |
| 20 | 25,000 MCMC samples + 5,000 burn-in = 30,000 forward evals | 9 | supports |
| 21 | N=10,000 training pairs needed for hardest Navier-Stokes regime | 9 | supports |
| 22 | Base FFT version requires uniform discretization | 6 | supports |
| 23 | Non-periodic BCs handled via local W (bias) transform | 9 | supports |
| 24 | <1% error at viscosity 1e-3; 8% error at viscosity 1e-4 (full time series) | 3 | supports → competing-methods quantification CORRECTED in narrative_final.md |
| 25 | Fourier layer filters higher modes, keeps lower modes | 4 | supports |
| 26 | FNO is the only benchmark that does zero-shot super-resolution (spatial AND temporal) | 9 | supports |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or analogy and was not put through the skill:

- **"Coffee swirling in a glass" / cream curl analogy** — pedagogical scaffolding to hook the listener on turbulence as a phenomenon, not a claim about the paper.
- **"Like teaching someone to read using only one font and watching them get baffled by Helvetica"** — analogy for grid-dependence, not a paper claim.
- **"Like switching between hearing a chord as a single sound versus picking out individual notes"** — analogy for the Fourier representation flip, not a paper claim.
- **"The prism" / "Red at one end, violet at the other"** — pedagogical analogy for spectral decomposition, not a paper claim.
- **"Vortices that were blurry blobs on the coarse grid resolved into crisp swirling tendrils on the fine grid"** — visual description of Figure 1's qualitative content (Figure 1 caption says "Ground truth on top and prediction on bottom; trained on 64×64×20 dataset; evaluated on 256×256×80"). The qualitative claim that fine-grid evaluation produces sharper structure is consistent with the figure.
- **Closing reflections** ("the door is open. And once a door like that is open, you don't close it again") — explicitly framed as narrator's takeaway, not a paper claim.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/arxiv_2010.08895.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py` (16 pages).
2. For each substantive claim, locating the verbatim supporting excerpt via `grep` across the per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` to append each verified claim as an indexed journal entry, with the verbatim excerpt, the page number, the section context, and AI commentary on the evidential relationship.
4. Where the evidential relationship was an overstatement (claim 24), the narrative was corrected and the correction logged here.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. One quantitative overstatement corrected. Safe to ship to TTS.
