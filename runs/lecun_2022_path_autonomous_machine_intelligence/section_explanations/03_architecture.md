# §3 — The Model Architecture (the BLUEPRINT — Figure 2)

## What this section does
LeCun lays out the box-and-arrow diagram for an autonomous intelligent agent. Six modules, all differentiable so gradient signals can flow through them. The diagram is Figure 2.

## The six modules (and what they do, in plain English)

1. **Configurator** — the executive. Looks at the task and tunes the parameters of all the other modules to fit that task. Analogy: like a director on a film set, telling cameras and lights what to do for this particular shot. The most mysterious module in the paper — LeCun admits later that "precisely how to do that is not specified."

2. **Perception** — eyes and ears. Reads from sensors and estimates the current state of the world. The configurator primes it to pick out only what's relevant to the current task — you don't notice the wallpaper when you're trying to catch a falling glass.

3. **World Model** — the **most complex piece**. Does two jobs: (a) fills in missing information about the present (you can't see behind you, but you know roughly what's there); (b) predicts plausible future states of the world. Crucially, the world model can produce **multiple** predictions because the world is not perfectly predictable.

4. **Cost / Energy module** — the unhappiness meter. Outputs a single number called "energy" measuring how uncomfortable the agent is. The agent's whole job is to take actions that minimize this energy over time. Two sub-modules:
   - **Intrinsic Cost** — hard-wired, immutable. This is where pain, pleasure, hunger, satiety, curiosity live. The shape of this module determines the personality of the agent.
   - **Trainable Critic** — learns to predict future intrinsic cost. So you can anticipate that the cookie tin will be empty before you reach for it.

5. **Short-term Memory** — keeps track of past, current, and predicted future states + their costs. Analogous to the hippocampus.

6. **Actor** — proposes action sequences, hands them to the world model for evaluation, then sends the best first action to the body. Two sub-components:
   - A **policy module** for quick reactive responses (think: catching a falling glass without thinking)
   - An **action optimizer** for deliberate, multi-step planning

## Why every module is differentiable
Because differentiability lets you back-propagate gradients of cost through the whole graph — through the actor, the world model, the perception — and learn from the signal. Non-differentiable pieces would break the learning chain. This is LeCun's bet that gradient-based learning, scaled appropriately, is the only thing that's going to work.

## The big idea
This is not just a neural net. It's a **cognitive architecture**. Modules with distinct functions, learnable parameters, and gradient signals flowing through the whole thing. It looks more like a control loop with a brain in the middle than like a stack of transformer layers.

## Why this matters for the podcast
The listener needs to come away with one image: a perception module, a world model, an actor, and a cost meter, all wired so the actor can imagine moves, run them through the world model, see what cost they incur, and pick the cheapest one. That's the architecture. That's the bet.
