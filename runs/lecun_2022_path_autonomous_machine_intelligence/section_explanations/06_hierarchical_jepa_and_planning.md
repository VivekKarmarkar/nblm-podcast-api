# §4.6-4.7 — Hierarchical JEPA + Hierarchical Planning

## What this section does
JEPA, but stacked. Multiple layers, each operating at a different level of abstraction and a different time scale.

## The intuition (LeCun's driving example)
Driving a car:
- Over the next few seconds, with the steering wheel and pedals as inputs, you can predict your car's exact trajectory pretty accurately. Low-level, short-term.
- Over the next thirty minutes, you cannot predict the exact trajectory — too many unknowns (other cars, lights, pedestrians). But you can predict, at a much coarser level, that you'll arrive at your destination within a predictable time window. High-level, long-term.

H-JEPA captures both:
- **JEPA-1** at the bottom — fine details, short horizon
- **JEPA-2** above it — coarser details, longer horizon
- Possibly more levels above that

The higher levels feed off the lower levels' representations, but throw away even more detail to extend the horizon further. This is exactly the baby-ladder of concepts: each abstraction layer sits on top of more concrete ones.

## Why hierarchy enables planning
If your world model only predicts at the millisecond level, planning a 30-minute commute requires unrolling 1,800,000 steps. That's a non-starter.

But if your world model also predicts at the level of "drive to the train station, catch a train, walk to the office," the high-level plan is three steps. Each of those three steps then gets expanded into sub-plans, instantiated only when the lower-level perception fills in the details — what door you actually need to open, what color the traffic light is right now.

This is **hierarchical planning** — the kind humans do all the time, almost without noticing.

## Hierarchical Mode-2 reasoning
The same idea applied to Mode-2:
- Top level proposes a sequence of high-level actions (the abstract plan)
- Each high-level action becomes the goal for the next level down
- That level proposes a more detailed action sequence to achieve its goal
- This cascades all the way down to millisecond-level muscle controls

This solves a long-standing problem in AI: hierarchical planning has historically required the intermediate action vocabulary to be **pre-defined by hand**. LeCun's bet is that with H-JEPA, those intermediate vocabularies can be **learned**.

## Why this matters for the podcast
The driving example is gold — use it. Listeners commute. They get it. The point to land: a smart system has to plan at multiple altitudes simultaneously, and the architecture for doing that is built right into stacking JEPA layers.
