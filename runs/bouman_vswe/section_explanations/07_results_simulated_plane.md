# 07 — Results: Simulated Plane Strain (Sensitivity)

## Setup
Made a two-layer tissue model in COMSOL (a physics simulation package). Stiffness values set in the soft-tissue range (~10 kPa). Simulated the response to a CHIRP excitation (a swept-frequency signal) applied to one side of the surface. Used "plane strain" — a 2D simplification of 3D dynamics that assumes strain is constant in the depth direction.

## What they tested
For 5 distinct thicknesses × 4 distinct stiffness values, they perturbed each by ±5% and ±10% and asked: does VSWE detect the change?

## Result
Within each cluster (9 perturbations around each (T, E) center), VSWE-estimated parameters TRACK with changes in true parameters. The method picks up 5% changes. That's the sensitivity baseline.

## Conversational hook
This is the simulation-where-we-know-the-answer test. Same pattern as VVT: rehearse the physics with the right answer in hand, run the inversion pipeline, see if it gets the right answer back. They confirm: yes, it tracks parameter changes down to about 5%.

Important framing: this is the FLOOR of the method's resolution under best-case conditions (clean simulation, no real noise). Real data will be worse.
