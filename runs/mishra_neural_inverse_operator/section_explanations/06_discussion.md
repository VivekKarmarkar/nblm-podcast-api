# Section 6 — discussion and what's next

The discussion section is where the authors take stock. They re-state what NIO is, why it's structured the way it is, and what worked, then they're honest about what's still to do.

The re-statement is worth registering, because it crystallizes the contribution. NIO is a novel architecture, built by composing two existing pieces (DeepONets and FNOs) in a specific order dictated by the mathematical structure of the inverse map. It includes a randomized batching training procedure specifically designed so the model is invariant to the number of input samples used to discretize the boundary operator. It was tested on the Calderón problem in EIT, inverse wave scattering for the Helmholtz equation, optical imaging via the radiative transport equation, and seismic imaging via the acoustic wave equation. On every benchmark, it significantly outperformed the baselines. It was also robust to noise, varying sensor locations, varying grid resolutions, and out-of-distribution inputs.

Why does this matter beyond just winning on benchmarks? Because the authors believe this is the first end-to-end machine-learning framework specifically built for inverse problems that have the "operator in, function out" mathematical structure. That structure is shared across an enormous range of practical problems. EIT, optical tomography, seismic imaging, geophysical exploration, ground-penetrating radar, non-destructive testing of materials — all the same shape. If NIO genuinely generalizes the way the experimental results suggest, the same architecture can be redeployed across all of them with minimal changes.

The honest about-what's-next section flags three open directions.

**Other architectures.** NIO is built on DeepONet plus FNO, but other operator-learning architectures have appeared more recently — the authors mention LOCA (Kissas and colleagues, 2022), VIDON (Prasthofer and colleagues, 2022), and graph-based approaches (Boussif and colleagues, 2022; Brandstetter and colleagues, 2022). It would be interesting to see whether substituting these pieces in changes performance.

**Higher dimensions.** All the experiments in the paper are in 2D. Real seismic imaging is 3D. Real medical imaging is 3D. Scaling NIO to handle higher-dimensional problems is the obvious next direction, and the authors flag that it will require careful work.

**Theory.** The paper is empirical — there's no formal proof that NIO can approximate the inverse map to arbitrary accuracy. There's a body of theoretical results for the forward operators (Lanthaler and colleagues, 2022; Kovachki and colleagues, 2021) that establish universality guarantees for DeepONets and FNOs. The authors note that analogous theoretical results for NIO are needed to put the architecture on solid theoretical footing.

The closing tone is confident but not triumphant. They've opened a new direction. Plenty of work remains. The point of the paper is: there is now a recipe for learning the operator-to-function inverse map end-to-end, and that recipe gets you accurate, fast, robust solutions to inverse problems that traditionally took hours of compute per scan. That's the headline. Everything else is build-out.
