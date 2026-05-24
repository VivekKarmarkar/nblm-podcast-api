# NotebookLM Audio-Data-Driven Style Learning

**Captured:** 2026-05-24
**Status:** IDEA. Deferred — Vivek may come back to this AFTER setting up GPU/DPU infrastructure on the machine. (Whisper-quality transcription on dense academic content runs much faster on GPU; Vivek explicitly said he doesn't want to set that up right now and might return after.)

## The idea (Vivek's framing)

Vivek has generated many NotebookLM podcasts over time, each one based on a paper he gave NotebookLM as a source. Those podcasts are the *target style* we've been chasing in the paper-to-podcast pipeline — but until now, the delight brief in our pipeline has been Claude's a-priori guess at "what makes NotebookLM delightful." The proposed idea grounds that empirically:

1. **Collect** the existing NotebookLM mp3s Vivek has generated.
2. **Transcribe** each mp3 (Whisper, locally — requires GPU for speed; CPU is feasible but slow).
3. **Re-locate or re-download** each original source paper Vivek fed to NotebookLM.
4. **Pair** them: (paper PDF) → (NotebookLM-podcast transcript).
5. **Style-extract** via a background agent reading the (paper, transcript) pairs and identifying patterns:
   - Hook structures (how do they open?)
   - Transition phrases (how do they move between ideas?)
   - Technical-term-introduction conventions (when they introduce "mode" or "Fourier transform," HOW exactly?)
   - Conversational tics, two-host banter rhythms, callbacks
   - Length scaling — how does podcast length relate to paper density?
   - Source-fidelity patterns — how literal vs paraphrased?
   - "Inversion moments" — where the podcast says "wait, here's the surprising part" vs straight exposition
6. **Output**: `style-map.md` in the project root — a structured artifact that becomes a load-bearing input to future runs of the podcast pipeline (similar to how `CLAUDE.md` is load-bearing context for every session).

## The strategic shift

Right now the pipeline's delight brief is Claude's a-priori guess at NotebookLM style. After this idea ships, the delight brief becomes empirically grounded in actual NotebookLM examples Vivek values. Less guessing, more data.

## Honest caveats

1. **Single-host vs two-host transposition.** Audify produces single-host narration; NotebookLM is two-host conversational. Some style elements (banter rhythm, host roles) don't transfer directly. But the style elements that AREN'T host-specific (hook structures, term introductions, paraphrase patterns, conversational tone) DO transfer.

2. **Whisper transcription accuracy on technical terms.** Whisper mishears specialized vocabulary — "Young's modulus" might come out as "Young's modules" or worse. Mitigation: post-edit pass via the source paper text, especially for the technical-term inventory.

3. **Pairing manifest needed.** We need a way to map each mp3 to its source paper. Easiest: Vivek provides a manifest like `notebooklm_audios/<mp3>.txt` containing the paper title/DOI/path.

4. **AI-doing-AI-analysis bias.** The style extraction itself is an AI task with prior beliefs about what "style" means. Mitigation: keep raw transcripts + papers around as evidence, so any style-map claim can be challenged against source data.

## Why deferred

The bottleneck is Whisper transcription throughput. For ~10 NotebookLM podcasts of ~12 min each, CPU Whisper would take hours; GPU Whisper does it in minutes. Vivek explicitly said on 2026-05-24 that he doesn't want to set up GPU / DPU infrastructure right now and may come back to this project after that setup is done.

Until then, this is parked. The pipeline as it stands (v3/v4 quality) is good enough to start dogfooding on diverse papers, which itself accumulates empirical data — different empirical channel, no GPU required.

## When Vivek comes back

Concrete next steps when GPU is set up:
1. Choose Whisper model (whisper-large-v3 is current best; turbo variants are faster trade-off)
2. Vivek points me at the NotebookLM mp3 folder + provides the paper manifest
3. Single background agent does steps 2-6 above
4. Output `style-map.md` becomes a load-bearing context file for future pipeline runs (add it to project CLAUDE.md's "load-bearing files" list)
5. Next paper run uses the new empirical delight brief; compare quality before/after
