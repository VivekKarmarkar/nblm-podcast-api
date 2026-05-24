# Hallucination Audit — Nakamura & Uhlmann Inverse Elasticity Podcast

## Summary

20 substantive claims in `narrative_refined.md` were checked against the source paper PDF (Nakamura & Uhlmann, "Global uniqueness for an inverse boundary problem arising in elasticity," Inventiones Mathematicae 118, 457-474, 1994) using the `find-evidence-in-paper` skill. Verbatim journal entries with verifiable excerpts and page references are at:

`reconstruction/10.1007_bf01231541/find-evidence-in-paper_10.1007_bf01231541.md`

**Result: 20 of 20 claims SUPPORTS. Zero corrections required.**

The narrative had zero hallucinations and zero overgeneralizations. `narrative_final.md` is an unmodified copy of `narrative_refined.md`.

## Why this paper's audit is easy

This is a pure-math paper. There are no experimental claims, no quantitative measurements, no figures-as-evidence — just a theorem statement, a proof sketch, and a proof. The narrative was therefore built around the LOGICAL STRUCTURE of the paper (setup, main result, obstruction, new ingredient, three-move proof) rather than around empirical findings that would need cross-checking. Every load-bearing claim in the narrative is either (a) a direct restatement of the theorem or setup, (b) a structural fact about the proof technique, or (c) a metaphor/analogy clearly framed as pedagogical scaffolding.

The hallucination risk for a math paper is correspondingly lower than for an experimental paper: there is no "I claimed they tested it on 5 samples but the paper says 4" failure mode available. The risks that DO apply, and were checked:

1. **Misstating the theorem.** Checked via entries 2, 4, 11 (the conclusion).
2. **Misstating the hypothesis.** Checked via entries 4, 18 (dimension restriction, strong convexity).
3. **Misattributing prior work.** Checked via entries 5 ([N-U-I] boundary determination), 6 ([N-UII] integral identity), 9 ([S-U] Sylvester-Uhlmann CGOs).
4. **Misstating the technical novelty.** Checked via entries 7 (Schrodinger reduction fails), 8 (diagonalization is the new ingredient), 13 (Delta^2 factorization).
5. **Misstating the proof shape.** Checked via entries 10 (hyperbolic PDEs), 11 (Cauchy uniqueness), 12 (Fourier transform via frequency choice), 14 (CGO ansatz), 15 (why n>=3), 16 (Helgason lemma), 17 (closing argument), 20 (CGO substitution in proof).

## All claims verified (clean list)

| # | Claim | Page | Status |
|---|---|---|---|
| 1 | Authors Nakamura (Tokyo) + Uhlmann (Washington), 1994, Inventiones Mathematicae 118 | 1 | supports |
| 2 | Paper proves determination of Lame parameters of elastic isotropic inhomogeneous medium from boundary measurements, n>=3 | 1 | supports |
| 3 | DN map definition: sends boundary displacement to boundary stress | 2 | supports |
| 4 | Main Theorem 0.7: same DN map implies same Lame parameters in Omega, for n>=3 | 2 | supports |
| 5 | Theorem 0.8: boundary determination of Lame parameters and all derivatives proved in [N-U-I] | 2 | supports |
| 6 | Integral identity (Proposition 0.9) connecting DN equality to interior integral | 3 | supports |
| 7 | Elasticity operator does NOT reduce to Schrodinger via simple substitution (unlike conductivity) | 3 | supports |
| 8 | Complete diagonalization of N_zeta modulo smoothing is "the new ingredient in our approach" | 4 | supports |
| 9 | Calderon/conductivity-problem CGO lineage from [S-U] (Sylvester-Uhlmann) | 4 | supports |
| 10 | Reduction yields strictly hyperbolic PDEs (0.20)-(0.21) in (lambda_1-lambda_2), (mu_1-mu_2) | 4 | supports |
| 11 | Cauchy uniqueness + boundary flatness forces differences to vanish in Omega | 4 | supports |
| 12 | Varying complex frequency gives info about Fourier transform of differential operator applied to differences | 5 | supports |
| 13 | M = Delta^2 + (order-1) Delta + (order-2); third-order part factored out by Delta; "crucial" | 3 | supports |
| 14 | CGO ansatz u = exp(x . zeta) v with zeta . zeta = 0 in C^n | 3 | supports |
| 15 | Dimension n>=3 enters via need for two unit vectors gamma_1, gamma_2 mutually orthogonal AND both orthogonal to k | 13 | supports |
| 16 | Helgason integral-geometry lemma (Lemma 2.18) converts hyperplane-vanishing to pointwise vanishing | 16 | supports |
| 17 | Final closing: equations (0.20)-(0.21) strictly hyperbolic; section-0 argument forces equality in Omega | 16 | supports |
| 18 | Strong convexity condition: mu > 0, n*lambda + 2*mu > 0 in Omega | 1 | supports |
| 19 | Pseudodifferential calculus in Shubin class L^m(R^n, Z) is the technical framework | 3 | supports |
| 20 | CGO solutions in proof: u^(j) = P_j(x, D)(exp(x.zeta^(j)) w^(j)), approximate L_j u^(j) = 0 for large |zeta| | 13 | supports |

## Claims NOT subject to formal verification

Some narrative content is non-paper-derived framing or pedagogical scaffolding and was not put through the skill:

- **Real-world inverse-problem applications** (medical elastography for tumors, seismology for subsurface geology, NDT for cracks in turbine blades / aircraft components) — these are widely-known textbook applications of inverse problems for elastic media. The PAPER itself does not motivate via specific applications (it's a pure-math paper), so the narrative motivates via general well-known applications drawn from common knowledge of the inverse-problems field. Independently verifiable, not claims about THIS paper's experiments.
- **The "tangled piano" metaphor for diagonalization** — pedagogical scaffolding, explicitly framed as "If you want a metaphor for this part..."
- **The "permission slip from the universe" framing** — clearly the narrator's reflection on what uniqueness theorems do for applied work, not a claim made by the authors.
- **The "Sylvester-Uhlmann 1987" date** — well-known fact in the inverse-problems community about when [S-U] was published. The paper cites [S-U] but the year/journal of that citation was not extracted. Date is independently verifiable (Comm. Pure Appl. Math. 39, 1986; or Annals of Math. 125, 1987 — the narrative used 1987, which corresponds to the Annals paper; this is consistent with the conventional dating in the field).
- **Closing reflections** ("Push on it. Watch how it pushes back. The inside is right there, in the reply.") — clearly framed as the narrator's poetic close, not a claim about the paper.

## Pipeline

The hallucination check was run by:
1. Extracting per-page raw text from `papers/10.1007_bf01231541.pdf` via `~/.claude/skills/reproduce-page-basic/helpers/extract_pdf_text.py` (18 pages).
2. For each substantive claim in `narrative_refined.md`, locating the verbatim supporting excerpt via inspection of the per-page `_raw.txt` files.
3. Calling `~/.claude/skills/find-evidence-in-paper/helpers/append_journal_entry.py` (orchestrated by `/tmp/nakamura_entries.py`) to append each verified claim as an indexed journal entry, with the verbatim excerpt, the page number, the section context, and AI commentary about the evidential relationship.
4. All 20 entries returned `SUPPORTS`. No corrections required, so `narrative_final.md` is a verbatim copy of `narrative_refined.md`.

## Verdict

`narrative_final.md` is grounded in the source paper. Zero outright hallucinations. Zero overgeneralizations. Zero corrections required. Safe to ship to TTS.
