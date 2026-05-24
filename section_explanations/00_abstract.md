# Abstract — what the paper is about in one paragraph

You ever tap something to figure out what it's made of? Knock on a melon to see if it's ripe. Thump a watermelon. A real-life person can hear the difference between a hollow pumpkin and a dense one. That trick has a fancy engineering name. It's called non-destructive testing — figuring out what's inside something without cutting it open.

The catch is, the engineering version is expensive. Laser vibrometers. Specialized contact sensors. And even those usually only tell you "this object is roughly this stiff." They smear everything into one number for the whole thing.

This paper does something different. It uses a regular video — a monocular video, just one camera, no special hardware — and reads tiny vibrations on the surface of an object. From those vibrations alone, it estimates the stiffness and the density of every little chunk inside the object. Not just one number for the whole thing. A whole 3D map of what's inside.

The two things it's actually estimating are called Young's modulus, which is how stiff the material is, and density, which is how heavy it is per unit volume. The paper shows this works on simulated 3D shapes, on real rubber drum heads with hidden defects glued underneath, and — the showcase — on a real Jello cube with a chunk of clay buried inside it. From the video alone, the method finds the clay.

The big bet: every camera you own could become an interior-imaging device.
