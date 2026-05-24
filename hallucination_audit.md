# Hallucination Audit — Visual Vibration Tomography Podcast (v3)

## Summary

17 substantive claims in `narrative_refined.md` were checked against the source paper PDF using the `find-evidence-in-paper` skill. Verbatim journal entries with verifiable excerpts and page references are at:

`reconstruction/10.1109_cvpr52688.2022.01575/find-evidence-in-paper_10.1109_cvpr52688.2022.01575.md`

**Result: 16 of 17 claims SUPPORTS, 1 of 17 PARTIALLY_SUPPORTS (corrected).**

The narrative had zero outright hallucinations. One claim was a slight overgeneralization that was tightened in `narrative_final.md`.

## Corrections applied

### Correction 1 — Jello-cube excitation specifics

| Field | Value |
|---|---|
| Journal entry | #11 |
| Page | 7 (section 6.2 Real Cubes) |
| Original claim in `narrative_refined.md` | "Six clean modes, from three videos of plucking different corners." |
| Paper says (verbatim) | "We recorded three videos of the cube under different initial deformation conditions (e.g., in one video, we lifted and then quickly released the top-front corner of the cube)." |
| Issue | The narrative said "plucking different corners" (plural) but the paper specifies "different initial deformation conditions" and only gives ONE corner-lift example. Saying "different corners" overgeneralizes a single example into a pattern not explicitly stated. |
| Correction | Replaced with: "Six clean modes, from three videos of the cube wobbling in different ways — in one of them, the team lifted and quickly released the top-front corner." |

## All claims verified (clean list)

Each entry below corresponds to a journal entry in `reconstruction/.../find-evidence-in-paper_*.md`. Read the journal for verbatim excerpts and full evidential commentary.

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Authors: Berthy Feng, Alexander Ogren, Chiara Daraio, Katie Bouman (Caltech) | 1 | supports |
| 2 | Method estimates 3D Young's modulus + density from monocular video | 1 | supports |
| 3 | Sub-pixel motion extraction works down to 0.001 pixel | 3 | supports |
| 4 | Motion extraction uses phase-based + complex steerable pyramid | 3 | supports |
| 5 | Nyquist limit: modes only observable below FPS/2 | 3 | supports |
| 6 | Optimization uses total-squared-variation regularization for spatial smoothness | 4 | supports |
| 7 | Tested on the Stanford Bunny | 5 | supports |
| 8 | Real drum defects were nail-hardening gel and acrylic plastic | 7 | supports |
| 9 | Drums were excited via loudspeaker (frequency sweep 50-1000 Hz) | 13 (Supp.) | supports |
| 10 | Jello-cube reconstruction used 6 modes from 3 videos of different excitations | 7 | partially_supports → CORRECTED in narrative_final.md |
| 11 | Real Jello reconstruction matches simulated-with-defect more than simulated-homogeneous | 8 (Fig. 11 caption) | supports |
| 12 | Method assumes materials are isotropic and linear elastic | 8 | supports |
| 13 | Method requires geometry to be roughly known ahead of time | 8 | supports |
| 14 | Validated with high-speed camera, not yet consumer cameras | 8 | supports |
| 15 | Gel defects fill the density map; acrylic only shows on edges (acrylic too stiff to bend along) | 7 | supports |
| 16 | Drum frame was a 4"x4" PVC adaptor with stretched rubber | 13 (Supp.) | supports |
| 17 | Traditional NDT mostly gives only homogenized material properties | 1 | supports |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or analogy and was not put through the skill:

- **Katie Bouman's black-hole imaging fame** — well-known biographical fact about the researcher (EHT collaboration, 2019). Independently verifiable, not a claim about THIS paper.
- **Analogies** ("like splitting white light into a rainbow with a prism", "tap a watermelon to see if it's ripe", "guitar string at a particular pitch") — pedagogical scaffolding, not claims about the paper.
- **Closing speculation** ("imagine a world where..." and "we're closer than you'd guess") — clearly framed as the narrator's reflection, not a claim made by the authors.
- **Author intent attributions** ("the authors are also clear about what they haven't yet done") — narrative summary supported in spirit by section 7 (Limitations) which is exactly the source.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/10.1109_cvpr52688.2022.01575.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py`.
2. For each substantive claim, locating the verbatim supporting excerpt via grep across all per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` to append each verified claim as an indexed journal entry, with the verbatim excerpt, the page number, the section context, and AI commentary about the evidential relationship.
4. Where the evidential relationship was `partially_supports` (claim 10), the narrative was corrected and the correction logged here.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. One overgeneralization corrected. Safe to ship to TTS.
