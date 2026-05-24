# Real-World Experiments — drums and Jello

This is the section that turns the paper from "interesting math" into "wait, that actually worked." The authors take their pipeline out of simulation and into the real world. They run it on two physical setups: rubber drums with hidden defects, and an actual Jello cube with a clay defect buried inside.

## The drums

Imagine taking a thin rubber sheet and stretching it tight over a four-inch frame. That's their homemade drum. Then they secretly add a defect to the underside — either some painted-on nail-hardening gel (sticky and gloopy) or glued-on circles of acrylic plastic (hard and rigid). From above, the drum looks like a normal drum. You can't see the defect.

Then they vibrate the drum. To do this they aim a loudspeaker at it and play a sweep through a bunch of frequencies. The rubber shakes in response, and a high-speed camera records the whole show.

They record the drum twice — once before adding the defect, once after. Then they run the pipeline on both videos and compare the reconstructed material maps. And the defect appears. As a bright region in the stiffness map. Right where they hid it. The shape too — when the defect is a bar of gel, the reconstruction shows a bar. When it's a circle of acrylic, the reconstruction shows a circle. When they put two circles, two circles show up.

There's a fun subtlety. The gel defects light up across the entire defect region in both stiffness and density maps. The acrylic defects light up on the edges of the defect. The authors explain this: acrylic is so much stiffer than the rubber that it doesn't bend along — it sort of sits there as a rigid lump, and only the boundary with the flexible rubber shows up clearly. Different defect materials leave different signatures. Useful for identifying not just where, but what.

## The Jello cube

This is the headline experiment. They make a Jello cube. They embed a rectangular chunk of clay inside it before the Jello sets. The clay is way denser and stiffer than the Jello around it. From the outside, the cube just looks like a slightly opaque cube of Jello. The clay is completely invisible to a normal video.

Then they record three videos. Each one is of the cube wobbling after they pluck a different corner. Three different excitations means they can extract more independent modes, which the algorithm needs because Jello damps so heavily. Six clean modes total from those three videos.

Six is not a lot. Looking back at the simulation results, six modes only got them a coarse, blobby reconstruction. So they don't expect a crisp picture here either — they expect a blob.

And they get a blob. But the blob is exactly where the clay is. They compare the reconstruction from the real cube to two simulated cubes: one with a clay defect, one homogeneous Jello. The real cube's reconstruction looks much more like the defected simulation than the homogeneous one. The math says: yes, there's something inside that real cube. Yes, it's roughly where the clay was placed. Yes, it has roughly the right size.

If you're keeping score: a phone-grade kind of camera, an everyday object, and an invisible interior defect — and the method actually finds the defect. That's the demo. That's the result that should make you sit up.
