# §1-2.1 — Prologue + Introduction + Learning World Models (the THESIS)

## Setup
The paper is a **position paper**, not a results paper. LeCun is sketching what he thinks the field needs to do to get past current AI's limitations.

## The central question
> "How is it possible for an adolescent to learn to drive a car in about 20 hours of practice and for children to learn language with what amounts to a small exposure... By contrast, to be reliable, current ML systems need to be trained with very large numbers of trials..."

A teenager learns to drive in ~20 hours. A self-driving car needs millions of simulated miles and engineers hard-wiring hundreds of behaviors — and still can't match human reliability. Why?

## The thesis in one sentence
**Humans and animals learn world models — internal models of how the world works — and current AI systems do not.**

LeCun:
> "The answer may lie in the ability of humans and many animals to learn world models, internal models of how the world works."

A world model is the thing that lets you, a human, predict outcomes without trying them. You don't crash your car to learn what crashing feels like. You watch a ball roll off a table and know it will fall before it does. You understand gravity, inertia, momentum, even if you can't name them. That predictive engine is what current AI lacks.

## Three challenges LeCun frames
1. How do machines learn to represent and predict the world **by observation** (not by expensive interaction)?
2. How do they **reason and plan** in ways compatible with gradient-based learning (the only training method we know how to scale)?
3. How do they learn **hierarchical** representations — concepts at multiple levels of abstraction and multiple time scales?

## Common sense
LeCun's definition is operational: common sense is the ability to use models of the world to fill in blanks — predicting the future, completing missing information, filtering out interpretations that don't fit.

Current AI, including big LLMs, has only the most surface-level version of this. The model that knows trillions of word patterns still doesn't know, in a grounded way, that water flows downhill or that an object hidden behind another object is still there.

## The pitch
The paper is going to propose:
- An overall **cognitive architecture** of differentiable modules
- A specific architecture called **JEPA** (Joint Embedding Predictive Architecture) for the world-model module
- A **non-contrastive self-supervised learning** recipe that lets the system learn representations that are both informative and predictable
- A way to make JEPA **hierarchical** so it can plan over long horizons

## Why this matters for the podcast
This is the spine. Everything LeCun proposes — the modules, JEPA, the hierarchies — is in service of building world models that can be learned by observation. That's the thesis. The podcast must lead with this.
