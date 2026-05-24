# Draft Story — A Path Towards Autonomous Machine Intelligence (Yann LeCun, 2022)

## The thesis (the spine of the whole essay)

Current AI — the chatbots people are using every day, the self-driving cars in test fleets, the game-playing agents — is missing something fundamental. It does not have a **world model**. It does not, in any grounded way, know how the world works. It cannot predict what will happen next in the way a baby can after a few months of watching the world. It cannot plan the way a squirrel plans to get to the high feeder.

Yann LeCun, the chief AI scientist at Meta and one of the godfathers of modern deep learning, wrote a position paper in 2022 arguing that this is THE central problem in AI. Not making models bigger. Not generating more reward signals. Building systems that learn world models by observation. He calls it "the answer." It's the spine of the rest of the paper.

## How animals do it

An adolescent learns to drive in about twenty hours. Self-driving cars, by comparison, need millions of simulated miles and engineers hard-wiring hundreds of behaviors, and they still can't quite match a human. A child learns language with what amounts to a small exposure. GPT-style systems need everything humans have ever written.

How? LeCun's answer: humans and animals learn **world models** — internal models of how the world works. They learn that objects don't teleport. That things fall down. That dropped glasses break. That the friend who's late is probably in traffic. From watching the world, mostly without being told.

There's a developmental chart in the paper, from a cognitive scientist named Emmanuel Dupoux, showing the age at which babies acquire various concepts. It's a stack. Object permanence first. Then solidity, support, broad categories of objects. Then stability, gravity, inertia. Then rational goal-directed actions. Then social concepts, false beliefs, language. Each layer sits on top of the layer below. None of it taught explicitly. Mostly absorbed by sitting there watching the world go by.

That stack is the architecture of common sense. It's what AI doesn't have, and it's what LeCun wants to build.

## The "single engine" idea

Here's a hypothesis LeCun raises that shapes the whole rest of the paper: humans don't carry around a separate world model for every situation. There's **one** world model engine, somewhere in the prefrontal cortex, that gets **dynamically configured** for whatever task is in front of you. The engine that predicts where a thrown ball will land is the same engine that predicts whether your friend will be late to dinner. The settings change. The hardware doesn't.

If that's how brains work, then a useful AI architecture should look the same way: one world model, plus a *configurator* — an executive — that retunes everything else based on the task. This sets up the central blueprint of the paper.

## The architecture

LeCun proposes a cognitive architecture with six modules, all of them differentiable (so gradient signals can flow through them):

1. **The configurator** — the executive. Looks at the current task and tunes all the other modules accordingly.
2. **Perception** — reads from sensors, estimates the current state of the world, configured to pick out only what matters.
3. **The world model** — the most complex piece. Predicts plausible future states of the world. Can produce multiple predictions because the world isn't fully predictable.
4. **The cost module** — outputs a single scalar called "energy" measuring the agent's level of discomfort. The agent's whole job is to minimize this energy. Has an intrinsic part (hard-wired: hunger, pain, pleasure, curiosity) and a learnable part (a critic that predicts future intrinsic cost).
5. **Short-term memory** — keeps track of past, current, and predicted states.
6. **The actor** — proposes actions, hands them to the world model, picks the action sequence with the lowest expected cost, and sends the first action to the body.

It's not a stack of transformer layers. It's a control loop with a brain in the middle.

## Two modes of thinking

The actor can operate in two modes. LeCun borrows the names from Daniel Kahneman's *Thinking, Fast and Slow*:

- **Mode-1** is reactive. Perception sees the world, the policy module fires, an action goes out. No world model simulation. No planning. Catching a falling glass: Mode-1.

- **Mode-2** is deliberative. The actor proposes a sequence of actions stretching out into the future. The world model rolls forward and predicts the resulting sequence of states. The cost module scores them all. The actor refines the action sequence to minimize cost. The first action goes out. Driving home a new route: Mode-2.

This is **model-predictive control** — a classical control theory technique. The novelty is that the world model and the cost are *learned from data*, not hand-coded.

The most elegant bit: Mode-2 is expensive (you can only do one at a time), but the agent can use Mode-2 to figure out the right thing to do in a new situation and then **train a policy module to mimic the Mode-2 output**. After enough practice, the policy module produces the right action on its own, reactively, and the agent drops into Mode-1 for that situation. That's how a skill becomes automatic. A teen learning to drive: at first, every turn is Mode-2. After a year, it's Mode-1.

## JEPA — the centerpiece

The hardest technical piece, and the one LeCun calls "the centerpiece of this paper," is the architecture for the world model. He calls it **JEPA**: Joint Embedding Predictive Architecture.

The problem JEPA solves: when you train a system to predict the future — say, the next frame of video — you have a choice. You can train it to predict the literal future (every pixel of the next frame), or you can train it to predict an **abstract representation** of the future (only the things that matter).

Predicting every pixel is generative. It's what most current AI does. And it has two big problems. One, it wastes capacity trying to predict things that don't matter — the exact ripple of a leaf in the wind. Two, it fundamentally chokes on uncertainty. There isn't ONE correct next frame; there are many plausible ones. Generative models tend to produce a blurry average of all the possibilities rather than a sharp, plausible one.

JEPA takes the other path. It does **not** try to draw the future. It only predicts the parts of the future you should care about. There are two encoders — one for past, one for future — both producing compact representations. A predictor module predicts the future's representation from the past's representation. The closeness of the prediction is the "energy" — low energy means good prediction.

A latent variable handles the uncertainty. The future might go several ways; the latent variable is a knob, and when you turn it, the predictor produces different plausible futures.

Most importantly: JEPA can be trained without negative examples and without a generative target — a method called non-contrastive self-supervised learning, using techniques like VICReg. This is the technical breakthrough LeCun is most excited about, because it dodges the curse of dimensionality that breaks contrastive methods on high-dimensional data.

## Stacking JEPA — hierarchical world models

JEPA, stacked. Multiple layers, each at a different time scale.

LeCun uses driving as an example. Over the next few seconds, with the steering wheel and pedals as inputs, you can predict your car's exact trajectory. Low-level, short-term. Over the next thirty minutes, you can't predict the exact trajectory — too many unknowns. But you can predict, at a much coarser level, that you'll arrive at your destination within a predictable time. High-level, long-term.

H-JEPA captures both. JEPA-1 at the bottom does fine details, short horizon. JEPA-2 above it does coarser details, longer horizon. Possibly more levels above that. Each abstraction layer sits on the more concrete one below it — exactly like the baby-ladder of concepts from the developmental chart.

And this is what enables **hierarchical planning**. You can't unroll a thirty-minute commute one millisecond at a time. But you can plan it as "drive to the train station, catch a train, walk to the office" — three high-level steps — and let each step expand into sub-plans as you go, instantiated only when the lower-level perception fills in the details. This is how humans plan. The hard part — historically — is that the intermediate vocabulary of actions had to be hand-coded. LeCun's bet is that with H-JEPA, those intermediate vocabularies are learned from observation.

## The polemic — scaling is not enough; reward is not enough

LeCun directly takes on two of the dominant narratives in current AI.

The first: scale is all you need. Just make the models bigger. LeCun pushes back hard. Tokenized generative models — LLMs — work fine for discrete data like text, but they fundamentally can't handle high-dimensional continuous data like video. You can't represent the uncertainty over "all possible next frames" the way you can over "all possible next words." And LLMs have essentially no capacity to reason about goals or search through action sequences. You can't even specify a goal in their internal vocabulary.

The second: reward is enough. The reinforcement-learning-can-do-anything camp. LeCun's counter: pure RL requires the agent to learn by interacting with the world. That's fine in games. It's catastrophic in the real world — you can't crash self-driving cars thousands of times. The proposed architecture does most of the learning at the level of the world model, entirely from observation. By the time the agent acts, it already has a model. It's closer to optimal control than to RL.

He also waves off the symbolic-AI revivalist position. He doesn't think you need to bolt symbol manipulation onto deep learning. He thinks reasoning emerges naturally as energy minimization in a learned latent space, no hand-wired symbols required.

## What's still missing

The paper is honest about its open questions. LeCun is explicit:

- Can H-JEPA actually be trained from videos to learn a useful concept hierarchy? Open.
- How exactly should the latent variable be regularized to keep its information minimal? Several options, none clearly best.
- How should the actor do its optimization when gradients are unhelpful? Mentions classical alternatives (dynamic programming, MCTS, etc.) but doesn't pick.
- And the configurator — the executive module that's supposed to orchestrate everything — is, in his own words, "the most mysterious" piece. "Precisely how to do that is not specified."

He's not selling a finished product. He's selling a research program. Decades of work, in his estimate.

## The brain parallels and the consciousness gesture

Speculatively, LeCun maps each module of his architecture to a brain region. Perception is sensory cortex. World model and critic are prefrontal cortex. Intrinsic cost is basal ganglia and amygdala. Short-term memory is hippocampus. Actor is premotor cortex. The configurator is, again, prefrontal cortex executive control.

A small, striking remark: the architecture has only one world model engine, configured on the fly. That naturally explains why humans can only really focus on one complex task at a time. LeCun goes further, marked clearly as speculation: maybe the illusion of consciousness is itself a side effect of having a configurator-like module overseeing the brain. If brains were big enough to afford a separate world model per task, you wouldn't need a configurator, and maybe consciousness as we experience it would disappear.

And on emotions: an agent with an intrinsic cost (pain, hunger) and a trainable critic (fear, hope) would necessarily have something equivalent to emotions. Not bolted on. Constitutive of any agent built this way.

## The bottom line

LeCun's claim: the path to genuinely capable AI is not bigger models and not more reward. It's giving AI systems the ability to learn world models from observation — the way a baby learns physics by watching balls fall. That requires a particular kind of architecture (modular, differentiable, with explicit roles for perception, world model, cost, actor, configurator). It requires a particular kind of representation-learning machinery (JEPA, stacked into a hierarchy). And it requires a particular kind of training (non-contrastive, self-supervised).

None of it is built yet. Most of the open questions are still open. But the proposal is the most concrete sketch anyone has of what an architecture for common sense might actually look like.

If he's right, the AI of the next decade looks fundamentally different from the AI of the last few years. It still uses gradient descent. It still uses deep neural networks. But the thing it's *doing* — building, configuring, and querying a learned model of the world — is different in kind from what LLMs do.

And the test of whether he's right is whether anyone can actually build the thing.
