A few honest caveats and an invitation to keep going.

First caveat. Like any data-driven method, this thing eats data. To learn that hardest turbulent regime, they needed ten thousand training pairs. Generating those pairs meant running a traditional solver ten thousand times — which is itself slow and expensive. So there's a real upfront cost. For really gnarly PDEs where even a few training samples are hard to come by, this approach as-is wouldn't work. A future direction is hybrid systems where the network learns from a small number of solver-generated samples and then bootstraps from there.

Second caveat. The basic version uses a fast wave-based transform that requires the grid to be uniform. If your geometry is irregular — like, you want to model fluid flow around a weird-shaped airplane wing where the mesh has to be denser near the wing surface — you need to do some adaptation. Not impossible. Not yet in the paper, either.

Third caveat. Standard wave-based techniques only work with periodic boundaries — imagine the rod loops back on itself like a circular track. Real physical problems often don't have that. The architecture handles this thanks to a small local adjustment that runs alongside the wave layer. It learns to keep track of the boundary. Both Darcy flow and the time-domain part of Navier-Stokes have non-periodic boundaries in their experiments, and the method handled them.

Fourth, and this is more an invitation than a caveat. Operators don't have to mean PDEs. An image is a function on a two-dimensional sheet — you can think of pixels as samples of an underlying continuous color field. A video is a function on a three-dimensional space-time volume. So this whole machinery — learning to map functions to functions, resolution-invariantly — might be a natural fit for computer vision tasks where the input could come at any resolution. That's left as future work.

The big picture. Up to this paper, neural networks were essentially limited to learning functions that map fixed-size numerical inputs to fixed-size numerical outputs. The shape of the input had to match the shape the network was trained on. What this work shows is that you can teach a network something one level more abstract. Not just one function. The rule that turns functions into other functions. The operator itself.

For physics, that's a big deal. Because the laws of physics are operators. They take an initial state and produce a future state. They take a boundary condition and produce an interior solution. If you can learn those operators directly, you're learning physics in a form that's actually usable — at any scale, any resolution, any starting condition, in a single fast forward pass.

That's the door this paper opens.
