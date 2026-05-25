# 02 — Introduction

## What it says
Surface wave behavior leaks info about subsurface properties. Examples:
- Ocean waves break differently depending on the seafloor depth. Watching them lets you infer the seafloor.
- Apply a massage gun to your calf → ripples on the skin reveal the layers of fat, muscle, bone beneath.

There's a precise mathematical relationship between (a) the THICKNESS and STIFFNESS of each subsurface layer and (b) how waves propagate on the surface.

## Motivation: tissue characterization
- Tumors, musculoskeletal degeneration, liver disease — all change tissue thickness or stiffness.
- Current tools (ultrasound elastography, MR elastography) need expensive specialized equipment AND a trained operator. Regular screening is infeasible.
- VSWE: use just a video camera to get coarse estimates of thickness and stiffness.

## Other applications
- Human-computer interaction: subsurface muscle stiffness inference could unlock gesture recognition modes.
- Biomechanics: many body regions are modeled as soft tissue layered atop bone — VSWE matches that model.

## The technical kernel
- Wave propagation through a medium is captured by a "dispersion relation"
- Under common biomechanical assumptions (soft layer on hard bone), the thickness T and stiffness E of the soft layer FULLY DETERMINE the dispersion relation
- Main idea: find the (T, E) pair whose theoretical dispersion relation best matches the one extracted from the video

## Conversational hook
The motivating concrete image is brilliant — a massage gun on your calf, ripples spreading out, and from a video of those ripples you could in principle read off how thick your soft tissue is and how stiff it is. That's the kind of thing currently locked behind a $50,000 machine and a trained technician.
