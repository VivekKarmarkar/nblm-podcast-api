# Draft Story — Visual Vibration Tomography

(Synthesized from 9 per-section explanations. This is the connective-tissue first pass that Phase 3 will tighten into the final narrative.)

## The hook

You know how you tap a watermelon to see if it's ripe? You're doing material physics. You're hearing how stiff and how dense it is. Now imagine that, but with a camera instead of your fingers, and instead of a watermelon — a Jello cube with a chunk of clay hidden inside.

## Why this matters

Knowing what things are made of, without breaking them open, is a huge deal. Engineers call it non-destructive testing. The current tools are great but expensive — laser vibrometers and contact sensors. And they mostly tell you "the object's average stiffness is X." They don't usually map out the interior.

Cameras, on the other hand, are everywhere. If you could squeeze the same information out of a regular video — no special hardware, no laser, no contact — that opens up a whole new way to inspect the world around you.

## What the authors did

They built a method called visual vibration tomography. It takes a single ordinary monocular video of an object vibrating slightly. From that video, it estimates the stiffness (Young's modulus) and density throughout the entire 3D interior of the object — even regions never directly seen in the video.

## How it works (the two-stage trick)

Stage one. Pull the tiny vibrations out of the video. The motions are way below the size of a single pixel — down to one thousandth of a pixel. They use a phase-based motion extraction technique borrowed from earlier work. Out of that step you get motion fields. Then a Fourier transform turns those motion fields into a list of mode shapes and frequencies — the patterns the object likes to vibrate in.

Stage two. Take those observed modes and solve for the material map inside the object. They set this up as an optimization problem: find the stiffness/density map whose predicted modes best match what the camera saw. Because the camera only sees one side, only catches slow modes, and is noisy, the math is ill-posed. They handle that with smoothness regularization (spatial variations in material should be gradual) and by iteratively recovering the missing 3D mode information alongside the material map itself.

## How they proved it works

Three layers of testing:

1. Simulation. Build virtual cubes with known interior defects, simulate their vibration, run the pipeline, and see if the algorithm recovers the truth. It does — better when given more modes, worse when the defect is in a part of the cube that barely moves (like the fixed base). Also worked on the Stanford Bunny shape.

2. Real drums. Stretch rubber over a frame, glue defects underneath, vibrate with a loudspeaker, record with a high-speed camera. The pipeline correctly recovers the shape and location of the hidden defects. Gel defects show up as filled regions in both stiffness and density; rigid acrylic defects show up as edge outlines.

3. Real Jello cube. The headline experiment. Embed a clay chunk inside a Jello cube. Record three videos of plucking different corners. Recover six clean modes. Run the pipeline. The reconstruction shows a defect in roughly the right place at roughly the right size, and looks much more like a simulated cube-with-clay-defect than a simulated homogeneous cube. Invisible interior defect, found from video alone.

## What they ran into

- Damping eats modes. Jello damps heavily, so you don't get many modes to work with, so the reconstruction is coarse.
- You only see one side of the object. Modes near the unseen surfaces or near fixed boundaries are harder to recover.
- You need to roughly know the object's geometry going in.
- They validated with a high-speed lab camera, not a phone yet.

## Where this leaves us

Proof of concept. Works in the regime they tested. Big future direction: get this running on consumer cameras (phones), and integrate it with light excitation (mechanical vibration tables) so you can grab more modes even from heavily damped materials. The dream is everyday cameras becoming everyday material-inspection tools.
