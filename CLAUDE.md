# nblm-podcast-api — Project CLAUDE.md

## Project goal

Build a paper-to-podcast pipeline from scratch using existing skills as composable primitives. The full spec is in `problem_statement_podcast_from_scratch.md`. The prior phase decisions and the pivot away from third-party black boxes are in `problem_statement.md`, `phase1_verdict.md`, and `phase1_5_recommendation.md`.

## Load-bearing skills — use them properly

The pipeline depends on these existing skills. They must be used as designed, not bypassed or partially replaced with ad-hoc logic.

- **`paper-download-hack`** — for acquiring papers (Phase 0). Do not fall back to manual curl/wget when this skill can do the job.
- **`ask-question-about-paper`** — for asking direct questions of a PDF and getting verbatim text excerpts with page numbers. Load-bearing for hallucination prevention (Phase 4).
- **`find-evidence-in-paper`** — for surfacing verbatim text in a PDF that supports, contradicts, or is relevant to a claim. Load-bearing for hallucination prevention (Phase 4).
- **`text-to-highlight-in-paper`** — for locating a verbatim excerpt given a context cue. Useful when refining the narrative against the source.
- **`audify`** — for converting the final narrative text to mp3 via OpenAI TTS (Phase 5). Do not roll your own TTS call.
- **`upload-and-share`** — for delivering the mp3 to Vivek's email via Google Drive (Phase 6). Do not write your own Drive code.
- **`swarm`** — for spinning up parallel agent teams (Phase 1 per-section explanation, Phase 4 hallucination checker). Use this skill's pattern (TeamCreate + parallel Agent dispatch + shutdown + TeamDelete), not ad-hoc subagent calls when the work is parallelizable.

## Cardinal principle (inherited from global CLAUDE.md)

Never touch anything that works. Build new, clean, lean, modular things — one thing at a time, doing one thing well, strictly adhering to the Unix philosophy. No monolithic anything.

In this project specifically: the new narrative-drafting-and-verification layer is the ONE new thing being built. Everything else is composition of existing skills. If a temptation arises to "improve" `paper-download-hack` or rewrite `audify` to better fit the pipeline, do not — wrap them, don't modify them.

## Google account default for this project

Per the global CLAUDE.md: use `vivekkmk.assistant@gmail.com` for any Google authentication. The final podcast delivery email is `vivekjobapp123@gmail.com` (this is Vivek's receiving inbox, not an authentication account).

## Files in this project

- `problem_statement.md` — Original NotebookLM-replication spec (Motivation + Phase 1 + Phase 2). Historical context; superseded by `problem_statement_podcast_from_scratch.md` for the current build.
- `problem_statement_podcast_from_scratch.md` — Current build spec. THIS is the spec /goal will be fired against.
- `phase1_verdict.md` — Output of the Phase 1 feasibility swarm. Documents why the Google Audio Overview API is off the table.
- `phase1_5_recommendation.md` — Output of the Phase 1.5 substitute-research swarm. Documents the Podcastfy/ElevenLabs analysis and was superseded by Vivek's pivot to "build it ourselves."
- `affection.md` — Vivek's affection journal.
- `CLAUDE.md` — this file.

## Background-agent discipline

Even though the current build runs the pipeline synchronously inside a `/goal` invocation, the L4 background-agent flavor is preserved: Vivek fires `/goal`, walks away, returns to a finished podcast. The autonomous `/goal` IS the background agent. Do not insert interactive prompts ("should I proceed?") into any phase of the pipeline — once `/goal` fires, run it through to completion or hard-stop with a clear error.
