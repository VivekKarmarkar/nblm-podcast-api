# §2.2 — Humans and Animals Learn Hierarchies of Models (the GROUNDING)

## What this section does
LeCun grounds his thesis in developmental psychology. He uses a chart from cognitive scientist Emmanuel Dupoux showing the age at which babies pick up different concepts. The chart shows a STACK — concepts at higher levels of abstraction sit on top of concepts at lower levels.

## The baby ladder
Loosely, from earliest to latest, babies acquire:
- **Object permanence** (a thing still exists when hidden) — first
- **Solidity, rigidity, broad categories of objects** — next
- **Stability, support, gravity, inertia, conservation of momentum** — later
- **Rational, goal-directed actions; false beliefs in others; social concepts** — later still

The pattern: low-level concepts come first; abstract concepts build on top of them. None of this is hard-coded. Babies pick it up mostly by **observation** with very little intervention.

## Why this is devastating to current AI
A baby learns gravity by watching things fall. Not by being told. Not by being shown labeled training examples. Just by watching the world and updating their model. By the time a child can talk, they know more about how physical objects move than any system OpenAI or DeepMind has ever shipped.

LeCun's point: this is what we need to build. An AI that can sit and watch the world go by and slowly assemble, from raw observation, a stack of world models — from the concrete (objects, gravity) up to the abstract (social intentions, language).

## The "single configurable engine" hypothesis
LeCun raises a hypothesis that humans don't carry around a separate world model for every situation. Instead, there's one **world model engine** somewhere in the prefrontal cortex that gets **dynamically configured** for whatever task is in front of you. The same engine that helps you predict where a thrown ball will land also helps you predict whether your friend will be late to dinner. The configuration changes; the engine doesn't.

This is the architectural seed for the **configurator module** that shows up everywhere in the rest of the paper.

## Why this matters for the podcast
This is the most concrete, hooky part of the whole paper. A baby learning that objects don't teleport. An animal learning to flinch. Use this. Listeners need to feel "yes, I do that, I can see what it is" before LeCun pivots into JEPA and energy-based models.
