# Architecture (Post-Pivot)

## Current (from index.html)

**Header:** "Architecture (Post-Pivot)"

**Legend:** Background Agent ("Level-4 architecture, applied to a from-scratch pipeline") · Paper-Reading Stack ("existing pocket-flow skills → hallucination prevention") · Markdown Context Store ("all artifacts persist as .md files on disk")

**Prose ¶A:** "This is Level 5 unpacked. The orange dashed box is the background agent. Inside, a seven-phase pipeline drafts a narrative from the paper, checks every substantive claim against the source PDF, layers in ElevenLabs audio tags, and synthesizes the final mp3."

**Prose ¶B:** "The blue dashed box is Vivek's pre-existing paper-reading skill stack — called from the hallucination-check phase to find verbatim grounding for every claim. The green cylinder on the right is the markdown context store, where every artifact persists as a versioned file."

**Diagram steps (stepData):** 1 Sections · 2 Synthesizer · 3 Narrative · 4 Hallucination Check · 5 Tag Enrichment · 6 audify-eleven · 7 Upload+Share · 8 ask-question-about-paper · 9 find-evidence-in-paper · 10 text-to-highlight-in-paper · 11 MD Context Store · 12 Paper PDF (input) · 13 Drive → Inbox (output).

## Audit (against the yardstick — vivek_reconstruction.md)

- **Overclaim language to soften (§5).** "checks **every** substantive claim against the source PDF" and "find verbatim grounding for **every** claim" read as an exhaustive guarantee. And the legend says the paper-reading stack delivers **"hallucination prevention."** Per §5 there is *no guarantee* — prefer "hallucination **check** / grounding" over "prevention," and "each substantive claim it can ground" over "every claim."
- **Parallelization is invisible — the main DIAGRAM gap (§4.1).** Efficiency → background agents **+ parallelization** is Vivek's principle #1. The diagram shows step 1 "Sections" as a single node feeding step 2 "Synthesizer." But the real shape is a **per-section swarm** (parallel agents, one per section) → a single synthesizer. The diagram should show that fan-out/fan-in so the efficiency/parallelization story is visible. (Vivek explicitly said: "also do that for the architectural diagram.")
- **The three principles aren't named.** §4 frames the whole architecture as efficiency (background + parallel) / accuracy (honest, §5) / scaffolding (the emotional layer, one host). A single framing sentence up top would tie the diagram to the "why."
- **Steps 5/6/7 (Tag Enrich → audify-eleven → Upload+Share) match §4.** Good. Step 4's "correct anything CONTRADICTED or SILENT" is an accurate mechanism — keep, but don't let the surrounding prose imply a guarantee.
- **Skill-not-product identity (§3, §6.3) is absent here too** — its main home is the Hero, but worth a thought whether a one-liner fits here (e.g., "the whole thing ships as a git-repo blueprint").

## Proposed

- **Legend:** "Paper-Reading Stack → grounding / hallucination check" (was "hallucination prevention").
- **¶A:** "…a seven-phase pipeline drafts a narrative from the paper, grounds its substantive claims back against the source PDF where it can, layers in ElevenLabs audio tags, and synthesizes the final mp3." (drop "every"/guarantee tone)
- **¶B:** "…called from the hallucination-check phase to find verbatim grounding for its claims." (drop "every claim")
- **DIAGRAM (flagged for the diagram pass, not prose):** show step 1 as a parallel per-section swarm fanning into the synthesizer — this is the one diagram edit that carries real meaning (the parallelization principle).
- **(optional) add a framing line:** "Three principles drive the shape: efficiency (a background agent, working in parallel), accuracy (grounded and honest about it), and scaffolding (the emotional, single-host layer)."

## APPLIED to index.html 2026-06-25 (prose only — diagram deferred)

- Legend: "existing pocket-flow skills → hallucination **prevention**" → "→ **grounding & hallucination check**" (no guarantee implied).
- ¶A: "**checks every substantive claim** against the source PDF" → "**grounds its substantive claims back** against the source PDF."
- ¶B: "find verbatim grounding for **every claim**" → "for **its claims**."
- DEFERRED to the diagram pass: show step 1 as a parallel per-section swarm → synthesizer (the parallelization/efficiency principle is currently invisible in the SVG).
- APPLIED: three-principles framing line added to ¶A (efficiency / accuracy / scaffolding).
- DIAGRAM EDITED (not deferred): step 1 "Sections" now renders as a parallel per-section swarm — stacked-sheet motif (vertical offset only, to clear the y=110 arrows) + "parallel per-section agents" sublabel + click-detail relabeled "Sections (parallel swarm)". Verified via Playwright screenshot at 1440px: no clutter, no arrow/text interception, no squish.
- Also fixed: the bottom SVG scaffold label "PAPER-READING SKILL STACK — HALLUCINATION **PREVENTION**" → "— HALLUCINATION **CHECK**" (consistency with the softened top legend).

## DIAGRAM FULLY REBUILT 2026-06-25 (per Vivek's 5-point critique, verified via Playwright @1440px)

1. All boxes shrunk (120×60 → 100×50; blue 160×60 → 156×54) for arrow breathing room.
2. Parallel swarm exaggerated: 4 stacked sheets on Sections + "parallel per-section agents" in bold amber (#fbbf24).
3. Serpentine: row 1 L→R, vertical drop (Halluc Check → Tag Enrich on the right), row 2 R→L, output to Drive moved bottom-LEFT (end of the S). Killed the diagonal.
4. Halluc Check → paper-reading: Manhattan route (horizontal out of orange box → vertical down at x=762 → horizontal into blue box).
5. Green MD lines → single junction node at (744,178) on the orange right edge; Halluc Check + Tag Enrich curve into it; it connects to the MD store. No crisscross.

Known: one clean blue×green crossing near the junction (flagged to Vivek, awaiting his call). Temp screenshots arch_diagram_v1–v4.png in project root — DELETE before any commit (untracked, not part of the site).

Round 2 tweaks (Vivek): (a) MD-store caption ".md files persist on disk" enlarged 9→11.5 + moved y184→200 (breathing room from cylinder); (b) "parallel per-section agents" → two lines, bigger, with ⭐ star; (c) pulsing amber glow on the Sections box (animate stroke-opacity 0.12↔0.7, 2.6s). Discussion point (blue×green crossing): Vivek floated a red-terminus data-flow hierarchy to resolve it; agreed to LEAVE the crossing — merging the two flows would falsely imply blue (skill-call) and green (data-persistence) are the same kind of flow; the crossing honestly depicts them as independent.

*Note: this was a full SVG body rewrite of the arch-canvas. defs (markers/filters) unchanged.*
