# §3.1 — Mode-1 vs Mode-2 (REACTIVE vs DELIBERATIVE)

## What this section does
LeCun gives the architecture two distinct operating modes, borrowed by analogy from Daniel Kahneman's *Thinking, Fast and Slow*:

- **Mode-1** — fast, reactive, no planning. Equivalent to Kahneman's "System 1."
- **Mode-2** — slow, deliberate, planning via simulation. Equivalent to Kahneman's "System 2."

## Mode-1 (reactive)
Perception sees the world → policy module immediately produces an action. No world-model simulation involved. No imagining what happens next. Just: state in, action out, done.

Example: catching a falling glass. You don't deliberate. The world model isn't queried. The policy module fires.

## Mode-2 (deliberative)
This is the real engine. Seven steps:
1. **Perception** — extract the current world state.
2. **Action proposal** — the actor proposes an initial sequence of actions stretching out into the future.
3. **Simulation** — the world model rolls forward, predicting the sequence of future states the actions would produce.
4. **Evaluation** — the cost module scores every predicted future state and adds them up.
5. **Planning** — the actor refines the action sequence, gradient-descending on the cost, until the sequence is as low-cost as it can make it.
6. **Acting** — the first action in the optimal sequence is sent to the body.
7. **Memory** — every state-cost pair gets stored for later training of the critic.

This is **model-predictive control with receding horizon** — a classical control theory technique. The novelty here isn't the loop; it's that **the world model and the cost are learned from data**, not hand-coded.

## The trade-off
Mode-2 is expensive. It uses the world model engine, of which there is only one, and it has to run for many simulated time steps. So the agent can only deliberate about one complex task at a time. Just like humans can only really focus on one thing.

Mode-1 is cheap but inflexible. The agent might have multiple policy modules running in parallel, each specialized for a familiar task.

## The trick — Mode-2 distills into Mode-1
Here's an elegant bit. The agent can use Mode-2 to figure out the right thing to do in a new situation, then **train a policy module** to mimic that optimal Mode-2 output. After enough practice, the policy module learns to produce the right action on its own, reactively, and the agent can drop into Mode-1 for that situation. This is **how skills become automatic**.

A teen learning to drive: at first, every turn is Mode-2. Slow, deliberate, thinking through everything. After enough practice, it gets compiled into Mode-1. You're doing it without thinking.

## Reasoning as energy minimization
LeCun reframes reasoning broadly. "Reasoning" in this architecture is any process of searching for a low-energy configuration of latent variables and actions. Logic-based reasoning is just one special case. The deep-learning version is: find the sequence of actions (and the values of any latent variables) that, when run through the world model, minimize the cost.

## Why this matters for the podcast
The Mode-1 / Mode-2 split is intuitive and easy to land. Use the catching-a-falling-glass vs deliberating-which-route-to-drive-home contrast. The Mode-2-distills-to-Mode-1 mechanism is the most viscerally satisfying piece of the whole architecture and worth highlighting.
