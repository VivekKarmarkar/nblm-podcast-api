# Limitations — what the paper doesn't pretend to do

The authors are explicit about what they haven't yet proved.

First, their math assumes the materials are isotropic and behave linearly elastically. "Isotropic" means the material reacts the same way no matter which direction you push it. Many real materials are mostly like this; some — like fiber composites — aren't. And "linear elastic" means the relationship between push and squish is a simple proportional one, which is only true when the motions are small. The whole pipeline relies on tiny vibrations, so this assumption is mostly self-fulfilling, but it does mean you can't analyze big floppy motions with this method.

Second, you have to know the object's geometry. At least roughly. You have to tell the algorithm "this is a cube of these approximate dimensions" or "this is the Stanford Bunny shape." The simulations show the method tolerates being a bit wrong about the geometry — up to thirty percent off in one dimension — but it can't figure out the shape from scratch.

Third, and most honestly: they validated their method using an expensive high-speed camera in a controlled lab setup. They have not yet demonstrated it on consumer-grade cameras. A phone camera brings additional headaches like image compression artifacts and more noise. The promise of "every camera could do this" is genuinely the goal, but it's not yet shown.

Fourth, and this is the hardest one: damping. Real-world objects don't ring forever. They damp out their vibrations quickly, and damping eats modes. Fewer modes means a fuzzier reconstruction. The Jello cube result is impressive precisely because Jello is so damped — but it's also coarse precisely because Jello is so damped. For really lossy materials, you might need to keep exciting them with mechanical vibration tables to get enough usable modes.

The honest framing: this is a proof of concept. It works in the regime they tested. There's clearly more engineering work between this and a phone app that x-rays your wooden beam.
