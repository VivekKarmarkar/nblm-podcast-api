# Hallucination Audit — VSWE Podcast (Bouman group, ICCV 2025)

## Summary

29 substantive claims in `narrative_refined.md` were checked against the source paper PDF (arXiv:2507.09207) using the `find-evidence-in-paper` skill. Verbatim journal entries with verifiable excerpts and page references are at:

`reconstruction/arxiv_2507.09207/find-evidence-in-paper_arxiv_2507.09207.md`

**Result: 28 of 29 claims SUPPORTS, 1 of 29 PARTIALLY_SUPPORTS (one tightening applied).**

The narrative had zero outright hallucinations. One claim about technique-specific resolution required a minor framing tightening in `narrative_final.md`.

## Corrections applied

### Tightening 1 — Sub-pixel motion resolution scoping

| Field | Value |
|---|---|
| Journal entry | #29 |
| Page | 3 (section 4.1.1 Motion extraction) |
| Original claim in `narrative_refined.md` | "The same technique they used for the Jello cube — developed in earlier research by Katie Bouman's collaborators — can detect motion on the order of one thousandth of a pixel." |
| Paper says (verbatim) | "we use phase-based motion processing [43], which is sensitive to sub-pixel displacements" — VSWE describes the technique as "sub-pixel" but does NOT quantify the resolution. |
| Issue | The "0.001 pixel" specific figure is a documented property of the underlying phase-based technique (Wadhwa et al. 2013, ref [43]) and was quantified in the predecessor VVT paper. The narrative's framing as "the technique they used... CAN detect motion on the order of one thousandth of a pixel" was technically accurate as a description of the technique's capability, but the framing could be clearer that this is a published property of the technique, not a VSWE-specific measurement. |
| Tightening | Replaced "The same technique they used for the Jello cube" with "The same family of techniques they used for the Jello cube — phase-based motion processing — has been shown to detect motion on the order of one thousandth of a pixel." This makes clearer that the resolution is a published characteristic of the technique family, not a VSWE-specific claim. |

## All claims verified (clean list)

Each entry below corresponds to a journal entry in `reconstruction/arxiv_2507.09207/find-evidence-in-paper_arxiv_2507.09207.md`. Read the journal for verbatim excerpts and full evidential commentary.

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Authors: Ogren, Feng, Ahn, Bouman, Daraio (Caltech) | 1 | supports |
| 2 | VSWE infers thickness + stiffness from a video of surface waves | 1 | supports |
| 3 | Massage gun on calf produces ripples conveying info about fat/muscle/bone | 1 | supports |
| 4 | Tumors, musculoskeletal degeneration, liver disease change tissue properties | 1 | supports |
| 5 | Current elastography requires expensive equipment + trained specialists | 2 | supports |
| 6 | VVT recovers material properties via global vibrational modes (needs whole object) | 2 | supports |
| 7 | VSWE targets local regions with simpler geometry (the structural advance) | 2 | supports |
| 8 | Thickness and stiffness fully determine the dispersion relation | 2 | supports |
| 9 | Motion extraction uses phase-based motion processing + complex steerable pyramid | 3 | supports |
| 10 | 2D FFT decomposes motion into spatial (γ) and temporal (ω) frequencies | 3 | supports |
| 11 | SSIM is the chosen objective function (image-similarity reasoning) | 4 | supports |
| 12 | Optimization is solved via grid search over (T, E) | 4 | supports |
| 13 | Method is sensitive to 5% changes in true parameters | 4 | supports |
| 14 | Three gelatin phantoms (1000, 1100, 1500 mL) → three thicknesses | 5 | supports |
| 15 | Garlic powder sprinkled on gelatin for motion-extraction texture | 5 | supports |
| 16 | Shaker excitation + high-speed camera at 600 FPS for ~4 seconds | 5 | supports |
| 17 | Stiffness recovered within 1.2% error of rheometry range | 6 | supports |
| 18 | Calipers for thickness ground truth, rheometry for stiffness ground truth | 5 | supports |
| 19 | As samples warmed, stiffness decreased; VSWE tracked the change | 6 | supports |
| 20 | Leg model from Visible Human Project; full 3D physics simulation | 6 | supports |
| 21 | Sliding observation window across upper calf tracks changing thickness | 7 | supports |
| 22 | Three lower-calf windows correctly recover very different thicknesses | 7 | supports |
| 23 | Assumes isotropic linear-elastic materials | 2 | supports |
| 24 | Assumes bone is much stiffer than tissue, modeled as motionless | 3 | supports |
| 25 | Characteristic numbers allow VSWE to extend to vastly different parameter ranges | 8 | supports |
| 26 | SSIM was the winner over curve-based, MSE, and PSNR objectives | 6 | supports |
| 27 | VVT predecessor paper: Feng et al., CVPR 2022 (same team) | 9 | supports |
| 28 | Closing claim: "everyday visual data to reveal critical information deep beneath the skin" | 8 | supports |
| 29 | Phase-based technique detects motion on the order of 0.001 pixel | 3 | partially_supports → tightened in narrative_final.md |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or analogy and was not put through the skill:

- **Katie Bouman's black-hole imaging fame** — well-known biographical fact about the researcher (EHT collaboration, 2019). Independently verifiable, not a claim about THIS paper.
- **Description of the VVT Jello cube experiment** ("they demonstrated it by burying a piece of clay deep inside a Jello cube... the computer handed back a 3D map of the cube's insides") — described as PRIOR work (the predecessor VVT paper), grounded in the v4 podcast's audited claims. Used as backstory framing, not as a VSWE-specific claim.
- **Analogies** ("ripples on a pond, but on a solid material", "splitting white light into a rainbow with a prism", "your ear picking notes out of a chord") — pedagogical scaffolding, not claims about the paper.
- **Closing speculation** ("imagine a world where..." and "we're closer than you'd guess") — clearly framed as the narrator's reflection, not a claim made by the authors.
- **"Hundred-thousand-dollar machine"** — order-of-magnitude framing for medical imaging equipment cost. Not a specific paper claim; consistent with general knowledge about MRI/ultrasound capital costs.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/arxiv_2507.09207.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py` for all 11 pages.
2. For each substantive claim, locating the verbatim supporting excerpt via grep across all per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` to append each verified claim as an indexed journal entry, with the verbatim excerpt, the page number, the section context, and AI commentary about the evidential relationship.
4. Where the evidential relationship was `partially_supports` (claim 29, the sub-pixel resolution figure), the narrative framing was tightened and the change logged here.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. One framing tightening applied to the sub-pixel-resolution figure to make clear it's a published property of the technique family. Safe to ship to TTS.
