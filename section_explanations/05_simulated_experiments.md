# Simulated Experiments — testing in the lab before going to the real world

Before pointing this at a real Jello cube and praying, the authors stress-test the method in simulation. The advantage of simulation: you know exactly what the ground truth is, because you built it. You can ask, "did the algorithm recover what I planted?"

They simulate cubes. Each cube is a 10x10x10 grid of little voxels. Most of the voxels are set to the material properties of Jello. A few voxels — forming a "defect" — are set to the material properties of clay, which is much stiffer and much heavier than Jello. Then they run a physics simulator to compute how each cube would actually vibrate over six seconds, sampled 2000 times per second. From that they generate a video.

The video goes through the full pipeline. Out the other end pops a reconstructed material map. Then they compare it to the truth.

Couple of things you can play with. How many modes you give the algorithm. Where the defect is buried in the cube. How much damping the simulated cube has (damping is what makes vibrations die out over time — Jello has a lot of it).

The results are exactly the kind of results that build trust without overpromising. With only 8 modes, the algorithm gets a vague blob — yes, there's a defect, but the shape is fuzzy. With 15 or 20 modes, the defect's actual shape sharpens up. You can see it. The take-home is intuitive: more modes is more information, and more information makes a better reconstruction.

Defect location matters too. The bottom of the cube is held still in the simulation, which means it barely moves, which means there's no motion signal coming from down there. A defect near the bottom is harder to find than a defect near the top. The data has a blind spot, and the algorithm inherits it.

Then they get fancier. They run the method on the Stanford Bunny — yes, the famous bunny shape used in computer graphics — to show it isn't limited to cubes. They reconstruct material maps on the bunny's interior. Same idea, weirder geometry.

They also probe robustness. What if the algorithm thinks the cube is a little bigger than it really is? Turns out, even with thirty percent geometric error, the reconstruction still finds the defect. The method is forgiving of small mismatches in shape.

And the toughest test: damping. Real materials lose vibration energy as they wobble. A Jello cube damps so heavily that you can only catch a handful of modes before everything stops moving. The authors simulate this and show that even with as few as 7 to 15 observed modes from damped cubes, you still get a coarse defect reconstruction. Not a sharp one — but enough to say "yes, there's something here, and it's roughly this size in roughly this location."

This whole section is doing two jobs at once. It's validating that the algorithm works when it should. And it's mapping out exactly where it starts to break, so when they bring it to the real world later, they know what to expect.
