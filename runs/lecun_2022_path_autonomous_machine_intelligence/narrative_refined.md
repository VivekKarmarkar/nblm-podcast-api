Picture a one-year-old, sitting on a hardwood floor, with a sippy cup in their hands.

They lift the cup over the edge of the coffee table. They open their fingers. The cup falls. It bounces. The kid laughs. Then they pick it up and do it again. And again. And again. Their parent has put away the carpet for a reason.

What's actually happening, in the kid's head, is one of the most interesting things in the natural world. They are running an experiment. Each drop, they're getting a little better at predicting where the cup will land, how high it will bounce, whether it will spill. They are building, from scratch, by watching, a model of how things fall. Not because anyone is teaching them. Not because someone is giving them a reward each time. Just because that's what brains do. They sit there absorbing the world and assembling a little internal physics engine.

By the time that kid is three, they will know more about how physical objects move than any AI system OpenAI or DeepMind or Meta has ever shipped.

That's the paper. Or rather, that's the puzzle the paper is trying to crack. Yann LeCun, who is Meta's chief AI scientist, and is one of the godfathers of modern deep learning, wrote a position paper in 2022 — sixty-two pages of it — about why current AI is missing something fundamental and what an architecture for fixing it might look like. The missing thing has a name. He calls it a world model. An internal model of how the world works. The kind of thing the kid with the sippy cup is building, in real time, by dropping it on the floor.

LeCun's claim is that no AI system on the planet has one of these. Not the chatbots. Not the self-driving cars. Not the game-playing agents. They have other things — vast pattern-matching abilities, beautiful tricks with language — but the part that lets a child predict where a ball will land, or a squirrel plan a route to the high feeder, that part is not there.

Let's start with why it matters.

A teenager learns to drive a car in about twenty hours. A self-driving car needs millions of simulated miles, hundreds of behaviors hard-coded by engineers, supervisory data from human experts, the whole works — and still can't quite match what the teenager does. A child picks up language from, basically, just being around people speaking it. The current best language models have to be fed essentially everything humans have ever written. Why the gap?

LeCun's answer: humans and animals learn world models, and AI does not. You don't crash your car to learn that crashing is bad. You watch a ball roll off a table and you know it will fall before it does. You hear footsteps in the hallway and you know someone is coming, even though you can't see them. That predictive engine, running constantly in the background of your awareness, is the thing AI is missing.

There's a chart in the paper showing the order in which babies pick up concepts. Object permanence — things still exist when hidden — comes first. Then solidity, broad categories of objects. Then stability, support, gravity, inertia. Then the idea that other people have intentions. Then false beliefs, language, social rules. Each layer sits on top of the layers below. None of it is taught explicitly. Most of it is picked up in the first few months of life, by sitting there watching.

That stack — that ladder of concepts, built from the bottom up by passive observation — is what LeCun thinks AI needs to learn how to build. Not from labels. Not from rewards. From watching the world go by.

And here's a hypothesis he raises that ends up shaping the whole rest of the proposal. He thinks humans don't carry around a separate world model for every situation. He thinks there's just one engine, somewhere in the front of the brain, that gets reconfigured on the fly for whatever you're doing. The engine that predicts where a thrown ball will land is the same engine that predicts whether your friend will be late to dinner. The settings change. The hardware doesn't.

If that's how brains work, then a useful AI architecture should look the same way. One world model. Plus an executive — what LeCun calls a configurator — that retunes everything else depending on the task.

So what does the architecture actually look like? Picture a control loop with a brain in the middle. There are six modules.

There's a perception module that reads from sensors and figures out what's going on in the world right now. There's the configurator — the executive — that retunes everything based on the current task. There's a short-term memory that keeps track of what's happened and what might happen. There's an actor, which proposes things to do. There's a cost meter, which outputs a single number measuring how uncomfortable the agent is. The agent's whole job, in a sense, is to keep that number low. Pain pushes it up. Hunger pushes it up. Curiosity, in this architecture, brings it down. The shape of that cost meter determines the personality of the agent.

And at the center — the most complex piece — is the world model. The thing that, given what's happening now, predicts what might happen next. And critically, that can predict more than one thing, because the world isn't perfectly predictable.

Now here's how the loop runs. The actor proposes a sequence of actions. The world model rolls forward and predicts the chain of futures those actions would produce. The cost meter scores all those imagined futures. The actor refines the sequence to find the cheapest version. And the first action in that cheapest sequence is what actually gets sent out into the world.

That's deliberate, slow, simulate-and-pick behavior. LeCun calls it Mode-2. Borrowing the name from Daniel Kahneman's *Thinking, Fast and Slow* — this is the System 2, slow-thinking equivalent. It's what you do when you're driving home a new route and have to think about which lane to be in. It's the careful, costly, one-task-at-a-time mode.

There's also a fast mode. Mode-1. Perception sees the world, a policy module fires, an action goes out. No simulating. No planning. Catching a falling glass: Mode-1. The fast-thinking System 1 equivalent.

The most satisfying piece of the whole architecture is how these two modes connect. Mode-2 is expensive. You can only really do one at a time. But you can use Mode-2 to figure out the right thing to do in a new situation, and then **train** the fast policy module to mimic that output. After enough repetition, the policy module produces the right action on its own, reactively. The skill gets compiled into Mode-1. A teen learning to drive: at first, every turn is Mode-2. After a year, it's Mode-1. That's how skills become automatic.

OK. So that's the architecture. Modules. Loops. A fast mode and a slow mode. Now the hard part. How do you actually build the world model? The thing that, given what's happening right now, predicts what might happen next.

LeCun's central proposal for this is something he calls a JEPA. Joint Embedding Predictive Architecture. He calls it the centerpiece of the paper.

Here's the problem it solves. Imagine you want to train a system to predict the next frame of video. The obvious thing to do is have it generate the next frame, pixel by pixel, and then check whether the prediction matches what actually came next. That's how a lot of current AI works. Generative prediction.

This has two huge problems. One — the system wastes enormous capacity trying to predict things that don't matter. The exact ripple of a leaf in the wind. The texture of the sidewalk. None of that is the point. But the system can't tell what's the point and what isn't, so it tries to predict all of it. Two — the future isn't unique. There isn't one right next frame. There are many plausible ones. The car at the fork might go left or right. Generative models, faced with this, tend to produce a blurry average of all the possibilities rather than a sharp, plausible one.

JEPA dodges both problems by doing something a little weird. It does NOT try to draw the future. It doesn't predict pixels at all. It predicts an abstract representation of the future. Just the parts that matter.

The way it works, in plain English. You have two snippets — past and future. You run each through an encoder that boils it down to a compact summary. Then a predictor module learns to predict the future's summary from the past's summary. If the prediction is close, the system is doing well.

And the magic is, the encoders can be trained to *throw away* the unpredictable junk. To produce summaries focused on what carries information. The system isn't burning cycles trying to predict leaves rippling, because the encoder has already decided leaves rippling aren't worth representing.

For the inherent uncertainty — the fact that the car might go left or right — there's a little knob, what LeCun calls a latent variable. Turn the knob and the predictor produces a different plausible future. Left branch. Right branch. Different settings, different futures.

And the training method is the technical breakthrough LeCun is most excited about. JEPA can be trained without making it predict pixels and without showing it pairs of negative examples. That matters because the usual methods break down on high-dimensional data like video. JEPA doesn't.

Now, the kicker. You can stack JEPAs. One on top of another. Each higher layer predicts at a longer horizon and a coarser level of abstraction.

LeCun's example is driving. Over the next few seconds, given your steering inputs, you can predict your car's trajectory pretty exactly. That's the bottom layer. Over the next thirty minutes, you can't predict the exact trajectory — there are too many unknowns. But you can predict, at a coarser level, that you'll arrive at your destination within a predictable window. That's the layer above.

Stack them. Now you have an architecture that can think about milliseconds at the bottom and about whole journeys at the top, at the same time. Which means you can plan at multiple altitudes simultaneously. You can't unroll a thirty-minute commute one millisecond at a time. But you can plan it as "drive to the train station, catch a train, walk to the office." Three high-level steps. And each step expands into sub-plans only when the lower-level perception fills in the local details. That's how humans plan. That's how a squirrel decides which branch of the tree to climb. And historically, every AI attempt at hierarchical planning has required the engineers to pre-define the intermediate vocabulary by hand. LeCun's bet is that with stacked JEPAs, the vocabulary is learned from observation.

OK. Step back. Where does this leave us with respect to the AI you actually read about every day?

LeCun is direct about this. He thinks the current dominant narratives in AI are wrong. He pushes back on two of them.

First — "we just need to scale up large language models." His position: scale isn't enough. LLMs work fine on discrete data like text, but they can't really handle high-dimensional continuous data like video, because you can't represent the uncertainty in the same clean way. And LLMs have essentially no capacity to plan or reason about goals. You can't even *specify a goal* in their internal vocabulary. You can prompt them, but they're not internally computing how to minimize a cost. They're just continuing the text.

Second — "reward is enough." The reinforcement-learning-can-do-anything position. His counter: pure RL requires the agent to learn by acting in the world. That's fine in games where you can simulate millions of trials cheaply. It's catastrophic in the real world. You can't crash self-driving cars thousands of times to teach them not to crash. The proposed architecture does most of the learning at the level of the world model, just from observation, before the agent acts at all.

He also waves off the idea that we need to bolt symbolic reasoning onto deep learning. He thinks reasoning emerges naturally as energy minimization in the learned latent space — finding the settings of the actor's actions and the latent variables that produce the lowest predicted cost. No hand-wired symbols required.

The paper is also genuinely honest about what's missing. LeCun doesn't pretend any of this is built yet. Can the stacked JEPA actually be trained from video to learn the kind of concept hierarchy a baby does? Open question. How exactly should the latent variable be regularized to keep it small and well-behaved? Several options, none clearly best. And the configurator — the executive that's supposed to orchestrate everything — is, in his own words, "the most mysterious" piece. Precisely how to do it is not specified.

He's not selling a finished product. He's selling a research program. Decades of work, in his own estimate.

There's one more thing worth flagging because it's quietly beautiful. LeCun, clearly marked as speculation, maps each module onto a region of the mammalian brain. The world model is prefrontal cortex. The intrinsic cost is basal ganglia and amygdala. Short-term memory is hippocampus. And the architecture has only ONE world model engine, configured on the fly — which naturally explains why humans can only really focus on one complex task at a time. He then goes a step further. Maybe what we experience as consciousness is itself a side effect of having a configurator-like module overseeing the brain. If the brain were big enough to afford a separate world model for every task, you wouldn't need a configurator. And maybe consciousness as we experience it would disappear.

That's a small remark in a long paper. But it's the kind of remark you remember.

On emotions, similarly: an agent built like this, with a cost meter that registers pain or hunger now and a critic that anticipates fear or hope later, would necessarily have something equivalent to emotions. Not bolted on. Constitutive. Emotion in this view is just what an active cost meter feels like from the inside.

So where does this leave you, as a listener?

LeCun's argument, the spine of the whole essay, is this. The path to AI that actually understands the world is not bigger models and not more reward. It is giving AI systems the ability to learn world models from observation — the way a one-year-old learns physics by dropping a sippy cup on the floor. That requires a particular kind of architecture — modular, differentiable, with explicit roles for perception, world model, cost, actor, configurator. It requires a particular kind of representation-learning machinery — JEPA, stacked into a hierarchy. And it requires a particular kind of training — non-contrastive, self-supervised, from raw observation, no labels needed.

None of it is built yet. Most of the open questions are still open. But this is the most concrete sketch anyone has of what an architecture for common sense might look like.

If LeCun is right — and you should treat this as a position paper, not a settled conclusion — the AI of the next decade looks fundamentally different from the AI of the last few years. It still uses neural networks. It still uses gradient descent. But what it's doing — building, configuring, querying a learned model of the world — is different in kind from what an LLM does.

The test of whether he's right is whether anyone can actually build the thing.

In the meantime — go watch a kid drop a cup on the floor. That's the benchmark. That's what we're trying to match.
