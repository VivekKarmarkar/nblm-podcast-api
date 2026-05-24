journal_metadata:
  paper: lecun_path_to_autonomous_machine_intelligence
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: Yann LeCun is affiliated with Meta as well as NYU's Courant Institute.
excerpt: |2-
   Courant Institute of Mathematical Sciences, New York University yann@cs.nyu.edu
                     Meta - Fundamental AI Research yann@fb.com
location:
  page_pdf: 1
  page_printed: 1
  section: Front matter / author affiliations
  surrounding_context: Affiliation block under the author name on the title page.
comments: SUPPORTS. Both affiliations appear verbatim. Confirms that LeCun is a Meta
  researcher (as well as NYU), supporting the narrative phrasing that he is 'Meta's
  chief AI scientist' (the specific job-title 'chief AI scientist' is a separate well-known
  biographical fact; this paper grounds the Meta affiliation directly).
---
index: 2
date: '2026-05-24'
status: matched
request: The paper is a position paper, not a results paper, and is dated June 2022.
excerpt: |-
  This document is not a technical nor scholarly paper in the traditional sense, but a position
  paper expressing my vision for a path towards intelligent machines that learn more like
  animals and humans
location:
  page_pdf: 1
  page_printed: 1
  section: 1 Prologue
  surrounding_context: Opening of Prologue (Section 1) immediately under abstract.
comments: SUPPORTS. Verbatim 'position paper'. The June 2022 date is in the front
  matter header ('June 27, 2022'). Confirms the narrative's framing of the work as
  a research-vision sketch rather than a results paper.
---
index: 3
date: '2026-05-24'
status: matched
request: An adolescent learns to drive a car in about 20 hours of practice, while
  current ML systems need very large numbers of trials.
excerpt: |-
  How is it possible for an adolescent to learn to drive a car in about 20 hours of practice
  and for children to learn language with what amounts to a small exposure. How is it that
  most humans will know how to act in many situation they have never encountered? By
  contrast, to be reliable, current ML systems need to be trained with very large numbers of
  trials so that even the rarest combination of situations will be encountered frequently during
  training.
location:
  page_pdf: 2
  page_printed: 2
  section: 2 Introduction
  surrounding_context: Opening of Section 2 Introduction.
comments: 'SUPPORTS. Verbatim ''20 hours of practice'', ''very large numbers of trials''.
  Confirms both halves of the narrative''s contrast: humans learn fast, ML needs huge
  data.'
---
index: 4
date: '2026-05-24'
status: matched
request: The answer to why humans/animals learn so much faster than AI may lie in
  their ability to learn world models — internal models of how the world works.
excerpt: |-
  The answer may lie in the ability of humans and many animals to learn world models,
  internal models of how the world works.
location:
  page_pdf: 2
  page_printed: 2
  section: 2 Introduction
  surrounding_context: After the human-vs-ML contrast paragraph.
comments: SUPPORTS. Verbatim — this is the THESIS sentence of the paper. The narrative's
  central claim that 'the missing thing is a world model' is taken word-for-word from
  this line.
---
index: 5
date: '2026-05-24'
status: matched
request: There is a chart in the paper (from Emmanuel Dupoux) showing the age at which
  infants acquire various concepts.
excerpt: |-
  Figure 1:      This chart, (courtesy of Emmanuel Dupoux), indicates at what age infants generally
  acquire various concepts about how the world works. It is consistent with the idea that abstract
  concepts, such as the fact that objects are subject to gravity and inertia, are acquired on top of less
  abstract concepts, like object permanence and the assignment of objects to broad categories.
location:
  page_pdf: 4
  page_printed: 4
  section: Figure 1 caption / §2.2 Hierarchies of Models
  surrounding_context: Caption to Figure 1 (developmental chart of infant concept
    acquisition).
comments: SUPPORTS. Verbatim attribution to Dupoux and verbatim 'object permanence',
  'gravity', 'inertia'. Confirms the narrative's baby-ladder description including
  the explicit stacking of abstract concepts on top of concrete ones.
---
index: 6
date: '2026-05-24'
status: matched
request: LeCun hypothesizes that humans have only one world model engine somewhere
  in their prefrontal cortex, which is dynamically configurable for the task at hand.
excerpt: |-
  One hypothesis in this paper is that animals and humans have only one world
  model engine somewhere in their prefrontal cortex. That world model engine is dynamically
  configurable for the task at hand. With a single, configurable world model engine, rather
  than a separate model for every situation, knowledge about how the world works may
  be shared across tasks.
location:
  page_pdf: 5
  page_printed: 5
  section: §2.2 Humans and Animals learn Hierarchies
  surrounding_context: The end of §2.2, just before the architecture proposal in §3.
comments: SUPPORTS. Verbatim 'one world model engine somewhere in their prefrontal
  cortex' and 'dynamically configurable'. Grounds the narrative's claim about LeCun's
  single-engine hypothesis.
---
index: 7
date: '2026-05-24'
status: matched
request: 'The proposed architecture has six modules: configurator, perception, world
  model, cost (with intrinsic cost + critic), short-term memory, and actor.'
excerpt: |-
  The configurator module takes inputs (not represented for clarity) from all other modules and
  configures them to perform the task at hand.
  The perception module estimates the current state of the world.
  The world model module predicts possible future world states as a function of imagined actions
  sequences proposed by the actor.
  The cost module computes a single scalar output called “energy” that measures the level of dis-
  comfort of the agent. It is composed of two sub-modules, the intrinsic cost, which is immutable (not
  trainable) and computes the immediate energy of the current state (pain, pleasure, hunger, etc), and
  the critic, a trainable module that predicts future values of the intrinsic cost.
  The short-term memory module keeps track of the current and predicted world states and as-
  sociated intrinsic costs.
  The actor module computes proposals for action sequences.
location:
  page_pdf: 6
  page_printed: 6
  section: Figure 2 caption
  surrounding_context: 'Caption for Figure 2: the system architecture diagram.'
comments: SUPPORTS. Verbatim. All six modules named, with the cost-module split into
  intrinsic-cost + critic also verbatim ('pain, pleasure, hunger'). Confirms the architecture-tour
  passage in the narrative.
---
index: 8
date: '2026-05-24'
status: matched
request: All modules in the proposed architecture are assumed to be differentiable
  so that gradient signals can flow through them.
excerpt: |-
  All modules in this model are as-
  sumed to be “differentiable”, in that a module feeding into another one (through an arrow connecting
  them) can get gradient estimates of the cost’s scalar output with respect to its own output.
location:
  page_pdf: 6
  page_printed: 6
  section: Figure 2 caption
  surrounding_context: First line of Figure 2 caption describing the architecture.
comments: SUPPORTS. Verbatim 'All modules in this model are assumed to be differentiable'.
  Confirms the narrative's claim that the modules are differentiable so gradients
  can flow.
---
index: 9
date: '2026-05-24'
status: matched
request: The world model is the most complex piece of the architecture, and one of
  its key functions is to predict plausible future world states.
excerpt: |-
  The world model module constitutes the most complex piece of the architecture. Its
  role is twofold: (1) estimate missing information about the state of the world not provided
  by perception, (2) predict plausible future states of the world.
location:
  page_pdf: 7
  page_printed: 7
  section: §3 A Model Architecture for Autonomous Intelligence
  surrounding_context: Description of the world model module.
comments: SUPPORTS. Verbatim 'the most complex piece of the architecture'. Confirms
  the narrative's framing of the world model as the central, hardest piece.
---
index: 10
date: '2026-05-24'
status: matched
request: The intrinsic cost module is hard-wired (immutable), and computes a scalar
  measuring instantaneous discomfort like pain, pleasure, and hunger.
excerpt: |-
  The Intrinsic Cost module is hard-wired (immutable, non trainable) and computes a
  single scalar, the intrinsic energy that measures the instantaneous “discomfort” of the agent
  – think pain (high intrinsic energy), pleasure (low or negative intrinsic energy), hunger, etc.
location:
  page_pdf: 7
  page_printed: 7
  section: §3 A Model Architecture for Autonomous Intelligence
  surrounding_context: Description of the intrinsic cost sub-module.
comments: SUPPORTS. Verbatim 'hard-wired (immutable)', 'pain', 'pleasure', 'hunger'.
  Confirms the narrative's claim about the intrinsic cost being hard-wired and the
  narrative's vocabulary for it.
---
index: 11
date: '2026-05-24'
status: matched
request: The trainable critic module predicts an estimate of future intrinsic energies
  (and so encodes anticipatory affect like fear/hope).
excerpt: |-
  The Trainable Critic module predicts an estimate of future intrinsic energies. Like the
  intrinsic cost, its input is either the current state of the world or possible states predicted by
  the world model.
location:
  page_pdf: 8
  page_printed: 8
  section: §3 A Model Architecture for Autonomous Intelligence
  surrounding_context: Description of the trainable critic sub-module.
comments: SUPPORTS. Verbatim 'predicts an estimate of future intrinsic energies'.
  The narrative's mapping of critic → fear/hope is paraphrase of LeCun's own brain-parallel
  discussion (§8.2) where he says 'fear or elation may be the result of anticipation
  of outcome by brain structures whose function is similar to the Trainable Critic.'
---
index: 12
date: '2026-05-24'
status: matched
request: Mode-1 is the reactive, fast mode analogous to Kahneman's System 1; Mode-2
  is the deliberate, planning mode analogous to System 2.
excerpt: |-
  We will call it “Mode-1”, by
  analogy with Kahneman’s “System 1”. The second mode involves reasoning and planning
  through the world model and the cost. It is akin to model-predictive control (MPC), a
  classical planning and reasoning paradigm in optimal control and robotics. We will call
  it “Mode-2” by analogy to Kahneman’s “System 2”.
location:
  page_pdf: 9
  page_printed: 9
  section: §3.1 Typical Perception-Action Loops
  surrounding_context: Introduction of Mode-1 vs Mode-2 terminology.
comments: SUPPORTS. Verbatim Mode-1 ↔ Kahneman's System 1, Mode-2 ↔ Kahneman's System
  2 + Mode-2 = MPC. Grounds the Kahneman-borrowing in the narrative.
---
index: 13
date: '2026-05-24'
status: matched
request: A Mode-2 plan can be distilled into a Mode-1 policy by training a reactive
  policy module to mimic the optimal Mode-2 action — a form of amortized inference.
excerpt: |-
  The system is run on Mode-2, producing an optimal action sequence (ǎ[0], . . . , ǎ[t], . . . , ǎ[T ]).
  Then, the parameters of the policy module A(s[t]) are updated to minimize a divergence
  measure between its output and the optimal action at that time D(ǎ[t], A(s[t])). Once
  properly trained, the policy module can be used to directly produce an action in Mode-1
location:
  page_pdf: 12
  page_printed: 12
  section: '§3.1.3 From Mode-2 to Mode-1: Learning New Skills'
  surrounding_context: Description of how Mode-2 reasoning trains a Mode-1 policy.
comments: 'SUPPORTS. Verbatim mechanism. Section title itself (''From Mode-2 to Mode-1:
  Learning New Skills'') endorses the narrative''s ''skills become automatic / compiled
  into Mode-1'' framing.'
---
index: 14
date: '2026-05-24'
status: matched
request: JEPA (Joint Embedding Predictive Architecture) is the centerpiece of the
  paper, and it does not generate y from x — it predicts the representation of y instead.
excerpt: |-
  The centerpiece of this paper is the Joint Embedding Predictive Architecture (JEPA). JEPA
  is not generative in the sense that it cannot easily be used to predict y from x. It merely
  capture the dependencies between x and y without explicitly generating predictions of y.
location:
  page_pdf: 24
  page_printed: 24
  section: §4.4 Joint Embedding Predictive Architecture (JEPA)
  surrounding_context: Opening of the JEPA section.
comments: SUPPORTS. Verbatim 'centerpiece of this paper' and verbatim non-generative
  property. Grounds the narrative's claim that JEPA is the centerpiece and does not
  draw the future.
---
index: 15
date: '2026-05-24'
status: matched
request: The main advantage of JEPA is that it predicts in representation space, eschewing
  the need to predict every detail of y.
excerpt: |-
  The main advantage of JEPA is that it performs predictions in representation space,
  eschewing the need to predict every detail of y. This is enabled by the fact that the encoder
  of y may choose to produce an abstract representation from which irrelevant details have
  been eliminated.
location:
  page_pdf: 24
  page_printed: 24
  section: §4.4 Joint Embedding Predictive Architecture (JEPA)
  surrounding_context: Right after the JEPA energy equation block.
comments: SUPPORTS. Verbatim 'eschewing the need to predict every detail'. Confirms
  the narrative's intuition that JEPA throws away unpredictable junk.
---
index: 16
date: '2026-05-24'
status: matched
request: A latent variable z lets JEPA represent multi-modal futures (e.g., the car
  taking the left or right branch at a fork in the road).
excerpt: |-
  If x is a video clip of a car approaching a fork in the road, sx and sy may represent the position,
  orientation, velocity and other characteristics of the car before and after the fork, respectively, ig-
  noring irrelevant details such as the trees bordering the road or the texture of the sidewalk. z may
  represent whether the car takes the left branch or the right branch of the road.
location:
  page_pdf: 25
  page_printed: 25
  section: Figure 12 caption / §4.4
  surrounding_context: Figure 12 caption.
comments: SUPPORTS. The narrative uses 'the car at the fork might go left or right'
  as its analogy for the latent variable — this is LeCun's own running example from
  Figure 12, used verbatim in spirit.
---
index: 17
date: '2026-05-24'
status: matched
request: JEPA can be trained with non-contrastive methods like VICReg and Barlow Twins.
excerpt: Examples of such non-contrastive criteria for JEPA training include VICReg
  and Barlow Twins.
location:
  page_pdf: 26
  page_printed: 26
  section: Figure 13 caption / §4.5 Training a JEPA
  surrounding_context: Caption for Figure 13 on non-contrastive training.
comments: SUPPORTS. Verbatim. Grounds the narrative's claim that JEPA is trained non-contrastively
  with methods like VICReg.
---
index: 18
date: '2026-05-24'
status: matched
request: JEPA can be stacked hierarchically (Hierarchical JEPA or H-JEPA), with lower
  levels making short-term predictions and higher levels making longer-term predictions
  at higher abstraction.
excerpt: |-
  The ability of the JEPA to learn abstract representations in which accurate prediction can be per-
  formed allows hierarchical stacking. In this diagram JEPA-1 extracts low-level representations and
  performs short-term predictions. JEPA-2 takes the representations extracted by JEPA-1 as inputs
  and extracts higher-level representations with which longer-term predictions can be performed.
location:
  page_pdf: 30
  page_printed: 30
  section: Figure 15 caption / §4.6 Hierarchical JEPA (H-JEPA)
  surrounding_context: 'Caption for Figure 15: the H-JEPA stacking diagram.'
comments: SUPPORTS. Verbatim 'hierarchical stacking', 'short-term predictions', 'longer-term
  predictions'. Confirms the narrative's stacking-JEPAs-at-different-time-scales claim.
---
index: 19
date: '2026-05-24'
status: matched
request: 'LeCun''s driving example: short-term you can predict the car''s exact trajectory,
  but at longer horizons you can only predict a coarser-grained outcome like arrival
  time.'
excerpt: |-
  Let’s take a concrete example. When driving a car, given a proposed sequence of actions
  on the steering wheel and pedals over the next several seconds, drivers can accurately
  predict the trajectory of their car over the same period. The details of the trajectory over
  longer periods are harder to predict because they may depend on other cars, traffic lights,
  pedestrians, and other external events that are somewhat unpredictable. But the driver
  can still make accurate predictions at a higher level of abstraction: ignoring the details of
  trajectories, other cars, traffic signals, etc, the car will probably arrive at its destination
  within a predictable time frame.
location:
  page_pdf: 31
  page_printed: 31
  section: §4.6 Hierarchical JEPA (H-JEPA)
  surrounding_context: LeCun's driving example illustrating hierarchical prediction.
comments: SUPPORTS. Verbatim driving example. The narrative uses this exact example
  to land H-JEPA — quoting from LeCun's own framing.
---
index: 20
date: '2026-05-24'
status: matched
request: Hierarchical planning enables decomposing a complex task like commuting into
  sub-tasks like driving to the train station, catching a train, etc.
excerpt: |-
  planning a complex task, like commuting to work, can be decomposed into driving to the
  train station, catching a train, etc. Driving to the train station can be decomposed into
  walking out of the house, starting the car, and driving.
location:
  page_pdf: 31
  page_printed: 31
  section: §4.6 / §4.7 Hierarchical Planning
  surrounding_context: End of §4.6, just before §4.7 Hierarchical Planning.
comments: SUPPORTS. Verbatim 'commuting to work', 'driving to the train station, catching
  a train'. Confirms the narrative's commute example for hierarchical planning.
---
index: 21
date: '2026-05-24'
status: matched
request: LeCun explicitly does not believe that scaling alone is enough for human-level
  AI.
excerpt: |-
  My position
  in this debate is that I do not believe that scaling is enough for two main reasons.
      First, current models operate on “tokenized” data and are generative. Every input
  modality must be turned into a sequence (or a collection) of “tokens” encoded as vectors.
  While this works well for text, which is already a sequence of discrete tokens, it is less
  suitable for continuous, high dimensional signals such as video.
location:
  page_pdf: 46
  page_printed: 46
  section: §8.3.1 Scaling is not enough
  surrounding_context: Opening of §8.3.1.
comments: SUPPORTS. Verbatim 'I do not believe that scaling is enough'. Confirms the
  narrative's polemical first prong against the scale-is-all-you-need camp, including
  the continuous-data-doesn't-fit-tokens argument.
---
index: 22
date: '2026-05-24'
status: matched
request: Current LLMs are only capable of very limited forms of reasoning because
  they lack abstract latent variables, making goal-directed action search essentially
  impossible.
excerpt: |-
  Second, current models are only capable of very limited forms of reasoning. The absence
  of abstract latent variables in these models precludes the exploration of multiple interpre-
  tations of a percept and the search for optimal courses of action to achieve a goal. In fact,
  dynamically specifying a goal in such models is essentially impossible.
location:
  page_pdf: 46
  page_printed: 46
  section: §8.3.1 Scaling is not enough
  surrounding_context: Second reason scaling is not enough.
comments: SUPPORTS. Verbatim 'dynamically specifying a goal in such models is essentially
  impossible'. Grounds the narrative's claim that LLMs cannot really plan or specify
  goals internally.
---
index: 23
date: '2026-05-24'
status: matched
request: Most learning in the proposed architecture takes place at the world-model
  level (entirely from observation), making the approach closer to optimal control
  than to reinforcement learning.
excerpt: |-
  The proposed architecture is designed to minimize the number of actions a system needs
  to take in the real world to learn a task. It does so by learning a world model that capture
  as much knowledge about the world as possible without taking actions in the world. It uses
  intrinsic costs that are differentiable functions of measured or predicted world states. This
  makes the proposal more similar to optimal control than to reinforcement learning. In the
  proposed model, much of learning takes place at the level of the world model (perceptual
  encoder and predictor).
location:
  page_pdf: 46
  page_printed: 46
  section: §8.3.2 Reward is not enough
  surrounding_context: Opening of §8.3.2.
comments: SUPPORTS. Verbatim 'more similar to optimal control than to reinforcement
  learning' and 'much of learning takes place at the level of the world model'. Grounds
  the narrative's second polemic claim that pure RL is wrong and observation-based
  world-model learning is right.
---
index: 24
date: '2026-05-24'
status: matched
request: Among the open questions, the configurator module is the most mysterious
  — precisely how it identifies subgoals is not specified.
excerpt: |-
  Of all the least understood aspects of the current proposal, the configurator module is the
  most mysterious. In particular, while planning a complex task, the configurator is supposed
  to identify sequences of subgoals and configure the agent to successively accomplish those
  subgoals. Precisely how to do that is not specified.
location:
  page_pdf: 44
  page_printed: 44
  section: §8.1 What is missing from the Proposed Model?
  surrounding_context: Limitations section, near the end of §8.1.
comments: SUPPORTS. Verbatim 'the configurator module is the most mysterious' and
  'Precisely how to do that is not specified'. Grounds the narrative's 'configurator
  is the most mysterious piece' line directly.
---
index: 25
date: '2026-05-24'
status: matched
request: 'LeCun maps architecture modules onto brain regions: perception ↔ sensory
  cortex, world model + critic ↔ prefrontal cortex, intrinsic cost ↔ basal ganglia
  + amygdala, short-term memory ↔ hippocampus, configurator ↔ prefrontal executive
  control.'
excerpt: |-
  The perception module corresponds to the visual, auditory, and other sensory areas
  of the cortex, as well as some of the association areas. The world model and the critic
  correspond to various part of the prefrontal cortex. The intrinsic cost module corresponds
  to structures in the basal ganglia involved in rewards, including the amygdala.
  The function of the short-term memory overlaps with what is known of the hippocampus. The
  configurator may correspond to structures in the prefrontal cortex that perform executive
  control and modulate attention.
location:
  page_pdf: 44
  page_printed: 44
  section: §8.2.1 Could this Architecture be the Basis of a Model of Animal Intelligence?
  surrounding_context: Brain-region speculation passage.
comments: SUPPORTS. Verbatim mapping of modules → brain regions (sensory cortex, prefrontal
  cortex, basal ganglia + amygdala, hippocampus). LeCun himself marks this as speculative;
  the narrative also flags it as speculative. Direct match.
---
index: 26
date: '2026-05-24'
status: matched
request: LeCun gestures, marked clearly as highly speculative, that the illusion of
  consciousness may be a side effect of a configurator-like module overseeing the
  brain — so a brain large enough for one world model per task would not need a configurator
  and the illusion of consciousness would disappear.
excerpt: |-
  A highly-speculative idea is that the illusion of consciouness
  may be a side-effect of a configurator-like module in the brain that oversees the function
  of the rest of brain and configures it for the task at hand. Perhaps if the brain were large
  enough to contain many independent, non-configurable world models, a configurator would
  be unnecessary, and the illusion of consciousness would disappear.
location:
  page_pdf: 44
  page_printed: 44
  section: §8.2.1 Could this Architecture be the Basis of a Model of Animal Intelligence?
  surrounding_context: Speculative passage about emotions and consciousness following
    the brain-region mapping.
comments: SUPPORTS. Verbatim 'highly-speculative idea', 'illusion of consciousness
  may be a side-effect of a configurator-like module', and the brain-size-counterfactual.
  Grounds the narrative's small consciousness remark — and the 'speculative' hedge
  in the narrative matches LeCun's own hedge.
