# Problem Statement — Podcast From Scratch

## Motivation

Phase 1 and Phase 1.5 of this project explored third-party podcast-generation backends (Google Audio Overview API, Podcastfy, ElevenLabs GenFM, etc.) as candidates for the NotebookLM-style podcast layer. All of them are black boxes with respect to the one quality dimension that actually matters for academic content: hallucination prevention. None of the candidates can prove their output is faithful to the source paper.

The pivot, articulated by Vivek on 2026-05-23: rather than search for a third-party solution, BUILD the pipeline from primitives we already own. Vivek has already built a suite of paper-reading skills (`ask-question-about-paper`, `find-evidence-in-paper`, `text-to-highlight-in-paper`, etc.) deliberately designed to prevent hallucination by grounding every claim in verbatim excerpts from the source PDF. Combined with the existing `audify` skill (OpenAI TTS, single-host narration) and `upload-and-share` (Google Drive delivery), the missing piece is a NARRATIVE-DRAFTING + HALLUCINATION-CHECK layer that ties these primitives together.

This problem statement specifies that layer.

The tradeoff being accepted explicitly: the output is a single-host narrator-style podcast, not a two-host conversational format. For a researcher consuming technical content while walking, a verified single voice beats two charming voices that hallucinate.

## Goal

Build a paper-to-podcast pipeline from scratch that:
1. Takes a paper PDF as input.
2. Produces an mp3 podcast as output.
3. Guarantees zero hallucination via cross-checking every substantive claim against the source PDF using existing paper-reading skills.
4. Composes existing skills as primitives — no new monolithic dependencies.
5. Runs end-to-end without user intervention when fired with `/goal`.

The first concrete test paper is Katie Bowman's "Visual Vibration Tomography."

## Pipeline

The pipeline has seven phases, executed in sequence. Phase 1 fans out parallel agents internally; Phase 2 is a single serialized synthesizer agent; Phases 3, 4, 5, 6 happen on the main session.

### Phase 0 — Paper download

Use the `paper-download-hack` skill to acquire Katie Bowman's "Visual Vibration Tomography" paper. The PDF should land in the project root (or a known subfolder if `paper-download-hack` has a default location). Record the absolute PDF path — downstream phases need it.

### Phase 1 — Parallel per-section explanation (backgrounded swarm)

First, a single preliminary agent scans the paper to discover its section structure (Introduction, Methods, Results, Discussion, etc.) by reading TOC and heading markers. It returns the list of sections with page ranges.

Then spawn N parallel agents in a swarm — one agent per discovered section. Each agent receives:
- The paper PDF path
- The section name and page range to focus on
- A common goal

The common goal for every agent: take the prose of the assigned section and produce an EXPLANATION that satisfies all of the following simultaneously:
- Technical accuracy is preserved at all costs — zero conceptual dilution
- Adheres to the paper's scientific standards
- Written in simple, easily accessible, engaging language
- Includes real-world examples and analogies where they aid comprehension
- Emphasizes the load-bearing points of the section
- Cites load-bearing context excerpts verbatim from the section when those excerpts are doing the conceptual heavy lifting

Each agent writes its output to a file (e.g., `section_explanations/{section_name}.md`) and reports completion. All agents run in parallel in the background — the main session does not block on their internal work, only on the swarm-level "all done" barrier.

### Phase 2 — Synthesizer agent (backgrounded, serialized after Phase 1)

A single synthesizer agent receives all per-section explanation files from Phase 1. Its job: combine them into a single unified STORY — not just concatenation, but a coherent narrative flow across sections. Output: a draft story document (e.g., `draft_story.md`).

This phase is serialized — it cannot run until all Phase 1 agents have completed.

### Phase 3 — Claude refines the narrative (main session)

Once the synthesizer's draft is in hand, control returns to the main session. Claude (orchestrator) reads the paper directly and refines the draft into the final narrative:

1. **Identify the ONE load-bearing message.** Good papers have a single core message; the narrative must be built around it. Claude reads the paper carefully and pins down what that message is.

2. **Write the hook.** Without diluting technical accuracy, write an opening paragraph that lays out the core message in fun, easily accessible, super-engaging language. Use analogies. Use real-world examples. Emphasize importance. Make it a little dramatic. The hook must do the work of pulling the listener in immediately.

3. **Build the story arc** from the hook onward:
   - Background — why does this matter at all?
   - What are the authors doing?
   - How do they do it?
   - How do they prove it?
   - What difficulties did they encounter?
   - Where does that leave us?

Write the refined narrative to `narrative_refined.md`.

### Phase 4 — Hallucination check

Pass the refined narrative to a swarm of CHECKER AGENTS. Each agent receives a chunk of the narrative (parallel per chunk for speed). For each chunk, the agent:
- Splits the chunk into individual substantive claims
- For each claim, generates a VERIFICATION QUESTION designed to surface whether the claim is supported by the paper
- Returns a list of `(claim, question)` pairs

Once all checker agents return, Claude (orchestrator) takes the full list of questions and runs them through the paper-reading skills:
- `ask-question-about-paper` for direct-answer questions
- `find-evidence-in-paper` for evidence-of-support questions

For each `(claim, question)` pair:
- If the paper supports the claim → keep the claim
- If the paper contradicts the claim → correct the claim using the verbatim excerpt returned by the skills
- If the paper is silent → flag the claim, decide whether to remove it or weaken it to a clearly-hedged statement

Write the corrected narrative to `narrative_final.md`.

Write a hallucination audit log to `hallucination_audit.md`. The audit must contain either:
- "Zero hallucinations detected — all N claims verified against the source PDF" with the list of (claim, supporting excerpt, page) triples, OR
- A full list of corrections made: original claim, why it was wrong, verbatim excerpt that grounds the correction, corrected text.

The audit log is non-negotiable — it is the proof that the pipeline did its job.

### Phase 5 — TTS

Use the `audify` skill on `narrative_final.md` to produce `podcast.mp3` in the project root. Default OpenAI TTS voice settings are fine unless the user specifies otherwise.

### Phase 6 — Delivery

Use the `upload-and-share` skill with the email `vivekjobapp123@gmail.com` to upload `podcast.mp3` to Google Drive and share it with Vivek. He will receive the mp3 on his phone and play it back.

## Background-agent / L4 architecture

The pipeline as specified above runs end-to-end synchronously within the `/goal` invocation. The Level-4 background-agent layer from the original `problem_statement.md` motivation — main session keeps moving while the podcast generates, user asks 20 minutes later — is satisfied automatically by Vivek's existing workflow pattern: he fires `/goal`, walks away, returns later, sees the deliverable. The autonomous `/goal` run IS the background agent in this context.

Future enhancement (not required for the first build): wrap the pipeline as an MCP server so it can be triggered from any session, not just `/goal`. Out of scope for this first pass.

## Files produced by the pipeline

In the project root unless otherwise noted:
- `Bowman_VVT.pdf` (or whatever path `paper-download-hack` lands on)
- `section_explanations/{section_name}.md` (one per discovered section)
- `draft_story.md` (synthesizer output)
- `narrative_refined.md` (Claude's refined story)
- `narrative_final.md` (post-hallucination-check final narrative)
- `hallucination_audit.md` (the audit log — load-bearing proof)
- `podcast.mp3` (the final audio)

## Skills used (load-bearing)

- `paper-download-hack` — Phase 0
- `swarm` — Phase 1 + Phase 4 (parallel agent orchestration)
- `ask-question-about-paper` — Phase 4 (hallucination verification)
- `find-evidence-in-paper` — Phase 4 (hallucination verification)
- `audify` — Phase 5
- `upload-and-share` — Phase 6

The pipeline must USE THESE SKILLS PROPERLY — they are the load-bearing primitives of the project. See `CLAUDE.md` in this directory for the directive.

## Success criteria

The /goal run is complete when all seven phases have executed in sequence, the audit log shows the hallucination check ran (and either passed or made corrections), and Vivek has received the mp3 in his email/Drive. Anything less is incomplete.
