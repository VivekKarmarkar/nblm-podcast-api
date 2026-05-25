# Draft Story — VSWE

## The one load-bearing message
Visible RIPPLES on a surface — captured in an ordinary video — leak quantitative information about the THICKNESS and STIFFNESS of what's underneath. The Caltech group built a method that reads that information out. Validated on gelatin phantoms (within 1.2% of professional stiffness measurements) and a simulated human leg (recovers thickness maps from a sliding video window). The continuation of the Visual Vibration Tomography story, but with a critical scaling advantage: you don't need to model the WHOLE object anymore. You can target a SECTION.

## The arc

### Hook: The Massage Gun
A massage gun on your calf. Ripples spreading out on your skin. Those ripples carry information about how thick your soft tissue layer is, and how stiff it is — they have to, because the underlying anatomy is what shapes how the wave moves. The wild claim: a regular video of those ripples, plus the right software, could read off those numbers. No ultrasound. No technician. Just a video.

### Why this matters
- Tissue stiffness changes with tumors, muscle disease, liver disease — meaningful medical signal
- Current tools: ultrasound elastography, MR elastography. Expensive. Require a trained operator.
- VSWE: just a video. If it works, regular at-home screening becomes possible.
- Other applications: gesture recognition (computers reading muscle state), structural inspection.

### The VVT-to-VSWE evolution (the bridge to prior listeners)
Same Caltech group, same Berthy Feng + Katie Bouman. Previous work (VVT, 2022) recovered material properties from MODES — whole-object vibrations. Beautiful proof of concept, but limited: only worked on small finite objects whose entire geometry you'd modeled. A Jello cube, a Stanford bunny.

VSWE: same big idea (videos can see inside things) — but uses WAVES instead of MODES. Waves are travel-along-the-surface, not stand-still-as-the-whole-object. The scaling unlock: you can characterize a SECTION of a much larger or complicated thing. A patch on a leg. A region of a bridge.

### The core technical idea (light touch)
1. Surface waves carry information — there's a precise math relationship between (thickness, stiffness of layers below) and (which wavelengths travel at which speeds on the surface). Engineers call that pattern a "dispersion relation" — the wave fingerprint.
2. To recover the dispersion fingerprint from a video: extract sub-pixel motion (using the same trick as VVT — phase-based motion processing, sensitive to motion smaller than a single pixel), then break the resulting motion field into its spatial and temporal frequencies.
3. To recover thickness and stiffness from the dispersion fingerprint: simulate what fingerprint each candidate (thickness, stiffness) would produce, compare to the observed fingerprint, find the match. The metric they ended up using to compare fingerprints is borrowed from image quality assessment — SSIM, normally used to grade how similar two photos look. Wave fingerprints reasoned about like photos.

### Validation 1: Simulations
Plane-strain physics simulations. Method detects 5% changes in thickness and stiffness. That's the resolution floor.

### Validation 2: Gelatin phantoms (the kitchen-grade experiment)
- Three gelatin samples, three thicknesses, made by pouring different volumes into the same container.
- Sprinkled GARLIC POWDER on top for texture (otherwise the surface is too smooth to track).
- Excited waves with a shaker, recorded with a high-speed camera at 600 FPS.
- Measured thickness with calipers. Measured stiffness with rheometry (the lab standard).
- VSWE recovers all three thicknesses, well within the caliper confidence interval.
- VSWE recovers stiffness within 1.2% of the rheometry measurement.

### Validation 3: 3D simulated human leg
- Real anatomical leg geometry from the Visible Human Project dataset.
- Full 3D physics simulation of waves traveling on the skin.
- Sliding observation window across the calf — at each location, recover the local thickness.
- The inferred thickness map TRACKS the actual changing thickness of the soft tissue layer.
- For the lower calf near the ankle (where tissue thickness varies a lot), VSWE recovers the dramatically different thicknesses correctly.

### The scaling story (characteristic numbers)
The team derived a set of dimensionless ratios that govern the method's performance. If you preserve those ratios, VSWE applies to objects at very different scales — bigger or smaller, denser or lighter. They demonstrated this with a 10× scale change. Practical implication: the method isn't stuck at any one regime. Adjust the camera and observation window appropriately, and you can apply it to anything that hosts surface waves.

### Limitations (be honest)
- Assumes isotropic, linear-elastic materials (small motions, same behavior in all directions)
- Assumes the layer model is correct (soft on hard, with the hard layer modeled as motionless)
- Density and Poisson's ratio assumed known constants
- Validated with a HIGH-SPEED camera in a lab setup, not phones yet
- Some boundary artifacts near the edges of the observation window

### The big picture close
VVT showed that videos can see inside objects. VSWE shows videos can see inside SECTIONS of arbitrarily large things — and can do so via surface waves rather than whole-object vibrations. The dream of a world where you don't need expensive specialized equipment to look inside a structure or a body part — where the camera you already carry, plus the right software, is enough — gets meaningfully closer.

A regular video of a ripple. A computer. Out comes a number: how thick, how stiff. From the surface, what's underneath.
