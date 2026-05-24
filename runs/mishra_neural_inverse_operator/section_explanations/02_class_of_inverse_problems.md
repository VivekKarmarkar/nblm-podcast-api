# Section 2 — the class of inverse problems they're attacking

This section is the authors saying: let's be precise about what we mean. They lay out one mathematical framework and then show how four very different real-world problems all fit inside it. The point is to convince you that the architecture they'll propose later isn't a one-trick pony — it generalizes to a whole family of problems that look very different on the surface but share an underlying mathematical skeleton.

The skeleton is this. You have a partial differential equation governing what happens inside some region. Sitting inside that equation is an unknown coefficient — call it the material parameter. You can't see it. What you CAN see is a relationship: if you set the boundary of the region one way, the boundary will respond a certain way. Push the voltage up, the current does something. Send in a wave at one angle, the reflection comes out at another. That input-to-output relationship at the boundary IS an operator. The authors call it the boundary observation operator. The whole game is to invert that operator and recover the hidden interior coefficient. They write it formally as a map from operators to functions — that's the load-bearing piece.

The four concrete examples:

**Calderón problem (EIT).** Electrical impedance tomography. Stick electrodes on a patient. Apply voltages, measure currents. The interior is the electrical conductivity of the tissue. The boundary operator is the voltage-to-current map — engineers call it the Dirichlet-to-Neumann map. From that map, infer the conductivity. The math is governed by an elliptic equation.

**Inverse wave scattering.** Send a wave at a fixed frequency into a region. Measure how it interacts with the boundary. The interior is the material's effective wave-speed coefficient — its squared slowness. The boundary operator is again Dirichlet-to-Neumann, this time for the Helmholtz wave equation. From that, infer where the scatterers are hiding.

**Optical tomography.** Shine light into a cloudy medium. Measure how much light leaks out the other faces. The interior is described by two coefficients — how much the medium absorbs and how much it scatters. The boundary operator is called the Albedo operator: it maps incoming light at the inflow boundary to outgoing light at the outflow boundary. Governed by the radiative transport equation.

**Seismic imaging.** Generate acoustic waves at sources on the top of a region, listen for the response at receivers on the boundary as the waves propagate, reflect, and refract through the sub-surface. The interior is the local wave-velocity coefficient — what kinds of rock are where. The boundary operator is a source-to-receiver map. Governed by the acoustic wave equation. In oil and gas, this is called Full Waveform Inversion.

Four problems, four different equations, four different physical setups. But the mathematical SHAPE is identical. You're given a boundary operator. You want to recover the interior coefficient. That's the only sentence you need.

A side note the authors care about: the existence and uniqueness of these inverse problems isn't obvious. Decades of pure math went into proving that, for example, the Calderón problem really does have a unique solution given the full Dirichlet-to-Neumann map. That theory matters because it tells you the problem is well-posed in principle — which means a sufficiently good algorithm should be able to recover the inside. It just hasn't been clear how to design that algorithm without spending hours of computer time per scan.

That's what sets up the rest of the paper.
