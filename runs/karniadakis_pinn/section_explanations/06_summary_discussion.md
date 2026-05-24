# Section 4 — Summary and Discussion (pages 18-20)

## The recap
The paper closes by restating the central contribution: PINNs are a new class of universal function approximators that can encode physical laws (specifically PDEs) directly into their training objective. The authors design two algorithm families — continuous-time and discrete-time — for inferring solutions to general nonlinear PDEs, and construct what they call "computationally efficient physics-informed surrogate models."

The pitch: this opens the door to endowing deep learning with the modeling power of mathematical physics, with applications including data-driven forecasting, model predictive control, and multi-physics/multi-scale simulation.

## The honesty paragraph
Crucially, the authors include a paragraph explicitly disclaiming overreach. The verbatim sentence:

> "We must note however that the proposed methods should not be viewed as replacements of classical numerical methods for solving partial differential equations (e.g., finite elements, spectral methods, etc.). Such methods have matured over the last 50 years and, in many cases, meet the robustness and computational efficiency standards required in practice."

This is unusually gracious for a flagship methods paper — most authors would oversell. The pitch here is COEXISTENCE, not replacement: the section-3 message that "classical methods such as the Runge-Kutta time-stepping schemes can coexist in harmony with deep neural networks" is reiterated as the actual stance. PINNs add to the toolkit; they don't subtract from it.

The argument for PINNs is then framed around implementation simplicity (small TensorFlow snippet), rapid prototyping, and a new class of problems that classical methods don't address well — particularly the inverse problems they preview as Part II.

## Future work — the load-bearing limitation
One pressing limitation called out: UNCERTAINTY QUANTIFICATION. Verbatim:

> "Finally, in terms of future work, one pressing question involves addressing the problem of quantifying the uncertainty associated with the neural network predictions. Although this important element was naturally addressed in previous work employing Gaussian processes [9], it not captured by the proposed methodology in its present form and requires further investigation."

Translation: when the network spits out a predicted solution u(t, x), there's no built-in way to ask "how confident should I be in this value at this point?" Gaussian processes natively produce uncertainty estimates; PINNs don't. This is flagged as an open research problem.

## Pointer to Part II
The paper is Part I of a two-part treatise. Part II is data-driven DISCOVERY of PDEs — given measurement data, infer the parameters λ (or even the structure of N) that best explain the observations. The closing paragraph promises that the implementation simplicity of PINNs will be especially valuable for that inverse-problem flavor.

## What the paper does NOT claim
A useful negative list, gathered across the discussion:
- Does NOT replace classical numerical methods.
- Does NOT provide uncertainty estimates.
- Does NOT guarantee global optimization convergence (acknowledged in section 2.1 footnote).
- Does NOT come with theoretical convergence proofs for the PINN training procedure itself.
- Does NOT address strong-nonlinearity-and-high-dimension regimes that would defeat the continuous-time approach (the discrete-time approach partially mitigates this, but no claim is made about, say, 10D PDEs).

## Acknowledgements / Code
- DARPA EQUiPS grant N66001-15-2-4055
- MURI/ARO grant W911NF-15-1-0562
- AFOSR grant FA9550-17-1-0013
- All code and data publicly available at https://github.com/maziarraissi/PINNs
