# §8.3 — Scaling Is Not Enough / Reward Is Not Enough (the POLEMIC)

## What this section does
LeCun directly attacks two of the dominant narratives in current AI:
1. "We just need to scale up LLMs" (the OpenAI / Anthropic / scale-is-all-you-need camp)
2. "Reward is enough" (the DeepMind reinforcement-learning-can-do-anything camp)

He argues neither is sufficient. And, somewhat in passing, he also pushes back on the symbolic-AI revival camp (Marcus & Davis).

## Scaling is not enough — his two reasons

**Reason 1: Generative tokenized models can't handle continuous data well.**
LLMs work on discrete tokens (words). To represent uncertainty about which word comes next, the model outputs a probability distribution over the dictionary — simple enough. But for video, that doesn't work. Video is continuous and high-dimensional. You can't put a probability distribution over "all possible next frames" the way you can over "all possible next words." Generative models for continuous high-dimensional signals end up producing blurry averages of all the possible futures rather than a sharp, plausible one. JEPA exists exactly to dodge this — predict the *representation*, not the *signal*.

**Reason 2: They can't really reason.**
Current LLMs have no abstract latent variables to manipulate. They can't explore multiple interpretations of an input or search for an optimal sequence of actions toward a goal. You can't even *specify a goal* in their internal vocabulary — you can prompt them, but the model isn't computing how to minimize a cost. It's just continuing the text.

## Reward is not enough — his argument
In standard reinforcement learning, the agent only learns from sparse rewards observed after taking actions in the world. This is fine when the world is cheap to interact with (games), but it's catastrophic when the world is expensive or dangerous (the real world). A self-driving car learning purely by reward signal would have to crash thousands of times.

LeCun's architecture sidesteps this by doing **most of the learning at the level of the world model** — perception encoder + predictor — entirely from observation. By the time the agent acts in the world, it already has a model. The cost module is differentiable and known by the agent, not opaque and stochastic. The whole proposal is closer to **optimal control** than to RL.

He's not saying RL has no role — just that it's far from sufficient on its own.

## Symbol manipulation — not needed
LeCun briefly responds to the symbolic-AI revivalist position (Marcus, Davis): that current deep learning needs hard-wired symbolic circuitry to reason. His counter is implicit but throughout — the architecture proposes that **reasoning emerges from energy minimization in a learned latent space**. No hand-wired symbols required. Just a sufficiently powerful world model and an actor that can search through action sequences.

## §8.1 — What's missing
LeCun is explicit and frequent about what he hasn't solved:
- Can H-JEPA actually be trained from videos to learn a useful concept hierarchy? Open question.
- How to regularize the latent variable to minimize its information content? Multiple options floated (discrete, sparse, stochastic), none clearly best.
- How to do the actual optimization in Mode-2 when gradients are unhelpful? Mentions classical alternatives (DP, belief prop, MCTS, SAT) but doesn't pick.
- **The configurator module is the most mysterious.** It's supposed to identify subgoals and orchestrate everything. "Precisely how to do that is not specified."

## Why this matters for the podcast
The polemic is the most listener-friendly part of the paper. LeCun is essentially saying, "the AI you're hearing about every day isn't on the right path." That's a hook. And the honest "here's what's still mysterious" coda is the right way to land — not as a takedown, but as a researcher saying "this is where we are, this is what's missing, and that's the work."
