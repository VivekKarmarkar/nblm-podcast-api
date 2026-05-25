# 09 — Results: 3D Human Leg with Spatially-Varying Thickness

## Setup
Took an STL file of a real female human leg from the Visible Human Project dataset (Andreassen et al. 2023). Ran a FULL 3D physics simulation in COMSOL of the leg's response to a chirp excitation applied on the skin. For computational feasibility, used the lower half of the leg (calf region). No assumptions beyond linear elasticity.

## What they did
Considered tangential and normal displacements on the surface. Applied a SWEEPING OBSERVATION WINDOW across the upper calf region — at each window position, estimate the local thickness and stiffness.

## Results — Upper calf sweep
- Inferred thickness CHANGES as the window sweeps around the leg, tracking the changing thickness of the actual soft tissue layer (computed as the distance from skin to nearest bone point within each window).
- More error near the edges of the simulated domain. The authors attribute this to boundary effects in COMSOL.

## Results — Lower calf (3 distinct windows near ankle)
The lower calf has three notably different thickness subregions because tissue structure changes a lot near the ankle. They chose 3 distinct windows rather than a sweep. VSWE recovers the drastically different thicknesses for each subregion.

## Stiffness across the leg
The method also recovers the (constant) stiffness of the leg tissue. Doesn't change across the leg. Figure 1 (the teaser) showed this.

## Conversational hook
The leg experiment is the killer demonstration. It's a SIMULATION (not real video of a real leg), but it's a full 3D anatomical simulation — and VSWE's sliding window pulls the right thickness out of every location.

The framing for a layperson: imagine running this on a real video of your own calf. The output is a thickness map showing where your soft tissue is thicker (more flesh) vs thinner (closer to bone, like near the ankle). That's medically meaningful information — and it came from a video.
