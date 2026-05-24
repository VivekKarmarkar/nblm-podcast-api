# Draft Story — "Mathematical methods and human thought in the age of AI" (Tao + Klowden, 2026)

## Core narrative arc

The essay is a working mathematician's honest attempt to think through what AI is doing to the practice of mathematics — and from that vantage, what it might be doing to the practice of intellectual work generally. It is not a tech-utopian or tech-doomer take. It is a philosophical essay by someone (Terence Tao, perhaps the most decorated living mathematician, with humanities scholar Tanya Klowden) who actually USES these tools daily and has been forced by their proliferation to think hard about them.

The arc:
1. Where things were before AI — mathematics had a fragile but workable set of standards (rigorous proof in principle, "smell test" intuition in practice).
2. What AI is changing — proofs can now be produced WITHOUT understanding; formal verification can pass a "soulless" proof; AI hallucinates basic facts while solving olympiad problems; circular citation loops are forming; entry-level jobs are vanishing.
3. What humans should do — short-term: AI as vanilla extract (a small enhancement, not the dish). Medium-term: AI as red team (critic, not creator). Long-term: a Copernican view — accept that other forms of intelligence now exist in the same ontological category as ours, with complementarities and differences, neither replacing nor being below us.
4. The closing image: we can never put the genie back in the bottle, but we can yet clear the smoke away.

## Drafting the spoken narrative

### Opening hook

The essay opens with a remarkable little joke. Tao and Klowden write that while composing this very paper using standard tools, no fewer than three different digital agents inserted themselves into the narrative UNSOLICITED. A footnote adds: "Any and all of these AI 'contributions' were promptly removed from the text."

That is the right hook for the podcast. Two of the most thoughtful living writers on the philosophy of mathematics sat down to write an essay on AI, and AI kept trying to write the essay FOR them. It is comic, it is concrete, it is the perfect entry into a piece that is fundamentally about the messy real-world experience of trying to work alongside these tools.

### Why mathematics is the right lens

The essay's choice of MATHEMATICS as its "sandbox" for thinking about AI is not arbitrary. Math is the field with the highest standards of objective truth — the field where, in principle, every claim can be checked. So it is the cleanest possible laboratory for asking: what happens when machines start producing intellectual work?

Tao and Klowden are careful to note that broad philosophical questions about AI are extremely complex, that they don't pretend to have definitive answers, and that the pace of change means anything they say risks being overtaken by next month's breakthrough. But: math has been here before (computer-assisted proofs were once controversial too) and math has the cleanest test for whether AI-generated reasoning is correct (you can mechanically check it).

The big observation, made in the math-as-sandbox section: AI can now solve hard math problems with verifiable proofs, without doing anything like what a human mathematician would do — no special cases, no working examples, no building intuition. The PROOF is correct. The PATH to the proof is foreign. This is what they call the decoupling between "the ability to prove theorems" and "the reasoning processes needed to discover and understand such proofs."

### The smell test

Mathematicians have always known that perfect rigor is an ideal, not a reality. Most papers have small errors. Some have big ones. The way the community functions in practice is through a kind of taste, an intuition Tao calls a "smell test" (borrowing from "code smell" in software engineering). An experienced mathematician can often tell, before reading a proof line by line, whether it is likely to be right — whether it has the right shape, the right load-bearing structure, the right surprises in the right places.

A good proof, per Thurston, doesn't just SHOW that a result is true. It tells you WHY. It tells you which parts of the argument are doing the heavy lifting, which are routine, which are new. It builds the kind of understanding that lets a human reader generalize the argument to other settings, find connections to other parts of math.

AI can produce proofs that pass formal verification and yet have no smell. They have the right typesetting, the right notation, the right step-by-step structure — but they offer no insight, no narrative, no sense of what was actually going on. Tao gives a specific example: AlphaProof generated formally-verified solutions to International Mathematical Olympiad problems in 2024 that contained "numerous redundant or inexplicable steps."

The proofs are right. The proofs are odorless.

### Where things break

Several concrete failure modes:

1. **The Fermat's Last Theorem trap.** Formal verification only verifies that the formal proof establishes the formal STATEMENT. It cannot catch errors in TRANSLATION between an informal English statement and its formalization. If an AI assumes that "natural numbers" includes zero, it can produce a formally-certified proof that Fermat's Last Theorem is FALSE. The math is impeccable. The math just isn't answering the question Fermat asked.

2. **Citogenesis.** Tao tried to use AI deep-research tools to systematically report the known literature on open math problems. The tools worked well. Then he noticed: those AI-generated reports were now being USED by the same deep-research tools as authoritative sources for future searches. Adding the reports actively INTERFERED with finding genuinely new literature. The tools were citing themselves.

3. **The 4.4% mathematician.** Tao worries about a future flood of AI-generated papers that are technically correct, technically new, but contribute nothing to the broader fabric of mathematical understanding. Beautiful typesetting. No insight.

4. **The student who never learns.** Already, students reach for AI tools to do their assignments. They get verifiable answers. They never develop the underlying intuition.

### What about the rest of us?

The essay zooms out. The economic story: the Luddites, the original Nottingham textile workers, were not anti-progress in some philosophical sense — they were skilled workers facing existential threats to their livelihoods. Today, unlike in their time, skilled workers are being replaced not with cheaper humans but with AI. Entry-level jobs that used to be the on-ramp to careers are vanishing.

The environmental story: AI cannot be built in a garage like the personal computer was. The analogy Tao uses is the 19th-century transcontinental railroad — massive upfront capital, heavy infrastructure, finite resources captured by a few large players. As of writing, no AI model in operation has even offset its own resource consumption.

The digital divide: not only is there a divide between people who have access to AI and people who don't, but a subtler second divide where different models have "spiky" capabilities and someone locked into one model has an advantage over someone locked into another, even within the AI-have community.

But there's a path. Smaller community-maintained local models. Publicly-funded AI resources. Norms of disclosure. The aviation analogy: aviation used to be horrifically unsafe. Now it is the safest mode of long-distance transport. That transformation didn't happen by accident — it happened through training, regulation, hard-won best practices. Same could happen here. Wikipedia is offered as a recent precedent: chaotic at first, dismissed by academia, eventually accepted as a useful starting point with norms of "follow the secondary sources."

### The proposal

Three time horizons:

**Short term: vanilla extract.** Use AI like vanilla extract in baking. A little splash improves nearly any dish. Too much makes it inedible (footnote: 44% vanilla cake). For now, use AI to polish grammar, suggest structure for bullet points — small touches that enhance human-led work without replacing it.

**Medium term: AI on the red team.** From cybersecurity: blue team builds, red team attacks. Map this to intellectual work: AI is safe to use to CHECK human-generated content for errors, to verify, to suggest improvements. It is risky to use AI to GENERATE foundational content that the red team can't verify. AI as critic, not as creator.

**Long term: the Copernican move.** This is the essay's most beautiful philosophical proposal. We are used to thinking of human intelligence as the CENTER of the cognitive universe, with everything else measured against it. Just as humanity once thought Earth was the center of the cosmos, until Copernicus and his successors showed it wasn't. That dethronement felt threatening at first. It turned out to be liberating — and accurate. The proposal: accept that other forms of intelligence now exist alongside ours, neither below us nor identical to us, with their own structures and their own complementarities to ours. We can still PRIORITIZE the human, just as we still prioritize Earth, while also acknowledging that the universe is bigger than us.

A concrete example: chess. It has been decades since any human grandmaster could beat a chess engine. Chess didn't die. It transformed. Chess players use engines to train, to revisit old theory, to find weaknesses in supposedly invincible AI players, to invent new forms of competition. The game survived. The meaning of the game evolved.

### Closing

The essay ends with cautious optimism. The world has changed in ways "as alarming as they are beneficial." Collective effort is needed. We have not reached a tipping point of no return. Mathematics — verifiable, objective, low-stakes in a humanitarian sense — is the right place to experiment with these technologies and learn how to extrapolate the lessons to the broader human endeavor. "Though we will never get the genie back in the bottle, we are optimistic that, as our understandings and action rapidly advance, we can yet clear the smoke away and look toward a bright, if somewhat uncertain, future."

The genie-and-smoke image is the right place to land the podcast.

## Tonal notes for Phase 3

- This is an ESSAY, not an experimental paper. The arc must be IDEAS, not results.
- The single most quotable lens is the DECOUPLING (proof from understanding) + the SMELL TEST.
- The single best concrete anecdote for audio is the THREE AI AGENTS interrupting Tao's writing process.
- The single best closing image is the GENIE / CLEAR THE SMOKE AWAY.
- The single best mid-essay structural move is the THREE TIME HORIZONS (vanilla extract → red team → Copernican).
- Resist the urge to summarize EVERYTHING. The essay covers economics, environment, IP, citogenesis, Wikipedia, aviation, the Luddites, the railroad robber barons, Fermat's Last Theorem, AlphaProof, chess, Copernicus, Wall-E, the Tumblr 44% vanilla cake. Most of this should be left on the cutting-room floor. The podcast wants ONE clear thread, not a hash of all of Tao's opinions.
- The thread the podcast should commit to: AI is changing math practice by DECOUPLING PROOF FROM UNDERSTANDING, and the question is what humans should do about that. The smell test, the red-team framing, and the Copernican view are all in service of that thread. Everything else is supporting evidence to use sparingly.
