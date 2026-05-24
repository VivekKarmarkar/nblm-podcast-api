# Section 4 — does it actually work? Yes. On all four benchmarks.

This is the test-it section, and the structure is straightforward: take each of the four problem types laid out earlier, generate a synthetic dataset where the ground-truth interior is known, train NIO, compare against two reasonable baselines, report errors.

The two baselines are interesting and fair choices. One is a vanilla DeepONet with a convolutional neural network as the branch — basically the natural way you'd try to apply existing operator-learning machinery to the inverse problem. The other is a fully convolutional image-to-image network — the kind of thing that's been used very successfully for seismic imaging in earlier work. So one baseline is the obvious extension of the existing operator-learning literature, and the other is the strongest task-specific baseline from the seismic community. NIO has to beat both.

Quick tour of what each experiment looks like:

**EIT (Calderón problem).** They synthesize conductivity maps inside the unit square, solve the elliptic equation, generate the boundary voltage-to-current pairs. Two sub-experiments — one with smooth trigonometric conductivities, one with the discontinuous heart-and-lungs phantom that's a standard benchmark in the EIT community. NIO beats the next-best baseline by roughly halving the error. On the heart-and-lungs case, the headline comparison isn't just to the deep-learning baselines but to the traditional D-bar method that real EIT software uses — NIO's error is much lower.

**Inverse wave scattering.** They sample wave coefficients that look like a few square inclusions sprinkled randomly in a 2D domain — like trying to find buried objects with sonar. The data is voltage-to-current style for the Helmholtz equation. NIO wins again, comfortably.

**Optical tomography.** They use the radiative transport equation on a 1D position by 1D velocity domain, with the absorption coefficient being a step-shaped function — basically a slab of absorbing material with sharp edges. Even with this discontinuous interior, NIO recovers it cleanly and significantly outperforms both baselines.

**Seismic imaging.** This is where the baseline FCNN is at its strongest — it was originally designed for this task. They use two standard seismic datasets, Style-A and CurveVel-A, from earlier published work. NIO is either better than FCNN or matches it. Even on the baseline's home turf, NIO holds up.

A summary table in the paper shows the median errors on every benchmark for every model. NIO is either the best or tied for the best on every problem. The improvements aren't subtle — they're often factor-of-two reductions.

After the benchmark tour, there's a really important sub-section that gets to the heart of why operator-input matters. The authors stress-test NIO under several kinds of variation, all at test time only — so the model never saw these conditions during training.

They add noise to the boundary inputs. NIO is robust.

They change the grid resolution between training and testing. NIO is robust.

They scatter the input sensor locations randomly instead of putting them on a uniform grid. NIO is robust.

But the headline robustness test is the one about the number of input samples. Recall that the boundary operator is approximated by L samples at training time. What happens if at test time you give the model a different number — say, half as many, or twice as many? For a model that treats the inputs as a fixed-size vector, this would be a disaster — the input shape doesn't even match. NIO, because of its randomized batching training, can take ANY number of samples at test time. The accuracy degrades very gracefully. The baseline models, in contrast, fall apart completely when the sample count changes.

The authors interpret this as evidence that NIO has actually learned the inverse OPERATOR — the abstract underlying map — rather than just memorizing a fixed-size lookup table. If the model could only handle one specific discretization, you'd suspect it's overfitting to that discretization. But because it handles ANY discretization gracefully, it must be representing something more fundamental.

The final comparison in this section is to traditional PDE-constrained optimization. This is the gold-standard non-learning approach: iteratively solving the inverse problem by repeatedly running the forward PDE solver and adjusting the interior guess. On an out-of-distribution test case for inverse wave scattering, NIO comes out about five times more accurate than PDE-constrained optimization, while being roughly four orders of magnitude faster. Inference takes NIO less than a second on a CPU. The PDE-constrained optimization took 8.5 hours on a GPU.

That gap — five times more accurate AND four orders of magnitude faster, on a problem the network was never explicitly trained for — is the result that makes you sit up.
