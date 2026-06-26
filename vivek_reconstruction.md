# ClaudeCodeLM — Polished Reconstruction (the yardstick)

> A clean synthesis of Vivek's first-principles reconstruction of the project (2026-06-25), reconciled against what's on disk, with his three final positioning decisions folded in. This is the ground-truth reference the website section prose is audited against. Where the prose disagrees with this file, the prose is wrong.

## 1. Premise — why the project exists

NotebookLM (Google) is an AI-augmented **information-ingestion** tool. You upload a paper PDF (or any document) and it produces a two-host conversational podcast — later also a video — giving a high-level summary. Its real value is triage: it expands the space of papers you can consume and helps you decide whether to print-and-read-deeply, engage further, or just take it as a good listen. Vivek discovered it via an APS March Meeting.

As Vivek moved into agentic coding and his skill library grew (download papers, bibliographies, OpenAlex lookups, hallucination/citation checks, coding), NotebookLM became the one step he **couldn't** fold into that workflow — especially because he wants to do this **while walking**, via Telegram + remote control, not at a desk. Every part of the pocket workflow works mid-walk except generating the podcast.

## 2. The gap, and the escalation toward a clean solution

NotebookLM is a **web product**: you upload a PDF in a browser. That's natural for a human but the wrong shape for Claude, which is at its core a **coding agent** — driving a web UI through Chrome MCP is clumsy. The clean alternative would be **programmatic** (an API call). But:

- There is **no good, exposed NotebookLM API**. What exists is either (a) reverse-engineered community wrappers (e.g. Podcastfy / an ElevenLabs path) that can fire the request but can't signal when the audio is done, or (b) Google's official API — enterprise-only, apply-and-wait.
- Even with a programmatic call, the **information-expert principle** bites: NotebookLM is the entity that *holds the information*, so a non-holder (Claude on the web, or Claude blocked on an API request) is stuck polling/waiting to learn when it's done — the same drawback Vivek hits as a human. The fix for the *blocking* is a **background agent** that absorbs the wait so the main session stays free.
- But the reliable-API-driven-by-a-background-agent target **doesn't exist** (the API is either hacky or gated).

## 3. The pivot — what ClaudeCodeLM IS

Since the clean external path doesn't exist, the project **builds the podcast itself inside Claude Code**: background agents don't call an external API — they **create** the podcast from scratch, and when it's done, you know it's done. On top of that sits a repertoire of delivery skills (email, upload to Google Drive).

**Identity (positioning — AFFIRMATIVE framing; keep it light on the site):** ClaudeCodeLM has the **texture/shape of a product** — it does what NotebookLM does, and the ElevenLabs emotional layer makes it product-grade. But instead of handing you a hosted product, it hands you the **blueprint for a highly customizable skill** that drops straight into a coding-agent workflow. The message is an *advantage, not an absence*: if your workflow is coding-agent-based, you don't need the product — you get the thing in the form that makes your agents happy. It ships as a **git repository** (clone it, have Claude read it, reshape it). **AVOID the negation "a skill, not a product"** — it invites the "just a skill = lesser" misread, which is especially wrong given the emotional layer makes it product-grade. Mention lightly; NO Vercel / marketplace / NPX mechanics.

## 4. The architecture (the HOW) — three principles

1. **Efficiency → background agents + parallelization.** The main agent shouldn't do the work (keep it free) = efficiency; extend that → parallelize where possible.
2. **Accuracy → no hallucinations** (see §5 for the honest framing).
3. **Scaffolding → the emotional layer.** Distinct from NotebookLM, this is a **one-host** podcast (not two-host).

**Pipeline:** Ingest paper/article → **sections identified and processed in parallel** (a per-section swarm) → a single **synthesizer** stitches the per-section explanations into one flowing draft. Then a deliberate **conversion of form** via a specific system prompt: *highly accessible yet very accurate — not watered down, not diluted — bringing out the core message while stripping verbosity* (extracting signal from noise for a first-pass audio consumption). Then the hallucination check (§5), then the **emotional layer** via the ElevenLabs MCP (emotion tagging), then **upload/share** via Google Workspace (Claude's own GWS account).

**Duration:** the practical selling point is simply **shorter than NotebookLM**. (Verified actual range 14.2–17.4 min, clustering 16–17; lead with "shorter than NotebookLM," not specific minutes.)

## 5. Hallucination — the honest framing (no overclaim)

Be honest: there is **no guarantee** of hallucination-freeness, and **no formal accuracy testing** was ever run. What is truthfully supportable:

- The paper-reading guard skills (`find-evidence-in-paper`, `ask-question-about-paper`) do **not** enforce accuracy by design. They earned trust because Vivek **validated** them in their original workflow — extract everything from a PDF (equations, text, prose, code, references) via agentic-vision + Python PDF, query it programmatically, then re-render a reconstructed PDF with pop-ups (his questions + Claude's comments) highlighted in colors, tested across many papers until "bulletproof."
- The specific example podcasts shared on the site are on **papers Vivek knows**, and they check out as accurate.

So the claim is **best-effort, validated-in-one-place** — explicitly *not* a guarantee. → On the site, **"no hallucination room" is an overclaim to soften.**

## 6. The three final positioning decisions (for "what we put up")

1. **Duration** — lead with "shorter than NotebookLM"; don't belabor the exact minutes.
2. **Hallucination** — honest best-effort, validated in one place, no guarantee. "It is what it is, so we say it that way."
3. **Product-shaped blueprint** (NOT "skill, not a product") — frame affirmatively: it has the shape/texture of a product, delivered as the *blueprint for a customizable skill* that fits a coding-agent workflow — "we give it to you in the form that makes your agents happy." Defining by negation ("not a product") invites the "just a skill = lesser" misread; avoid it. No Vercel/marketplace/NPX talk.
