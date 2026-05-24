# §4.4-4.5 — JEPA (the CENTERPIECE)

## What this section does
This is the heart of the technical proposal: **Joint Embedding Predictive Architecture** — JEPA. LeCun calls it "the centerpiece of this paper."

## The problem JEPA solves
When you train a system to predict the future — say, the next frame of video — you have a choice. You can train it to predict the **literal future** (every pixel of the next frame), or you can train it to predict an **abstract representation** of the future (only the things that actually matter for the task).

The first approach is generative — it tries to draw the future. Think: an image generator hallucinating the next video frame. The problem is, the world has a lot of unpredictable details. The exact texture of the grass. The exact ripple of a leaf in the wind. Most of those details don't matter for what you actually care about. But the generative model wastes its capacity trying to predict them anyway. And it fundamentally can't handle the uncertainty — most generative models for high-dimensional continuous data produce blurry averages of all the things that might happen, not crisp options.

The second approach — predicting an abstract representation — is what JEPA does. **JEPA does not generate. It does not draw the future. It just predicts the relevant features of the future.**

## How JEPA works (in plain English)
Two inputs: x (past or context) and y (future or related signal).

Two encoders, one per input, each producing a representation. The encoder for x produces sx, the encoder for y produces sy. These encoders can be different — and that's deliberate. The encoder for y can choose to throw out details that aren't worth predicting.

A **predictor module** then predicts sy from sx. The prediction quality — how close the prediction comes to the actual sy — is the **energy**. Low energy = good prediction = match.

Crucially, the predictor can take a **latent variable z** that captures the irreducible uncertainty. The future is not deterministic; z is a knob that, when varied, produces different plausible futures.

## Why this is a big deal
Three reasons:

1. **It throws away irrelevant detail by design.** The encoder for y can be trained to make sy invariant to details that don't matter, so the model isn't burning capacity predicting things it shouldn't care about.

2. **It handles multi-modal futures.** Real futures are not unique — the car at the fork might go left or right. JEPA captures that either by encoder invariance (the same sy for both branches) or by varying the latent variable z.

3. **It can be trained non-contrastively.** This is the technical breakthrough LeCun is most excited about. Most self-supervised methods either need a generative target (predict every pixel) or need contrastive negative examples (find anchor pairs and push apart negative pairs). JEPA can be trained with neither — using methods like **VICReg** (Variance-Invariance-Covariance Regularization) and Barlow Twins, which keep the representations from collapsing by enforcing variance and decorrelation across the batch.

## The four training criteria
1. sx is maximally informative about x
2. sy is maximally informative about y
3. sy is easily predictable from sx
4. z carries minimal information (so it doesn't "cheat" by encoding everything)

Criteria 1+2 keep the representations from collapsing (becoming constant). Criterion 3 enforces predictability. Criterion 4 keeps the latent variable from sneaking around the rest of the system.

## Why this matters for the podcast
JEPA is the most jargon-heavy section. The podcast needs to land just the conceptual punch: **don't try to predict every pixel of the future. Throw away the stuff that doesn't matter. Predict only the parts that do.** And: **the same idea, stacked in layers, gives you abstraction.**
