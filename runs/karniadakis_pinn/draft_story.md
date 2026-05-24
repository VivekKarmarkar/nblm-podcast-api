# Draft story — Physics Informed Deep Learning Part I

## The thesis behind the whole paper

Deep learning has been crushing it in image recognition, language, genomics — places where you have a giant pile of data. But step into physics, biology, or engineering, and the data well runs dry. Experiments are expensive. Measurements are noisy. You often have a handful of points to work with, not millions. Standard deep networks fall apart in that small-data regime.

But here's the thing the authors notice: in physics, you almost never start from nothing. You start with hundreds of years of accumulated PRIOR KNOWLEDGE. Newton's laws. Conservation of mass, momentum, energy. The actual differential equations that describe how the system is supposed to evolve. That prior knowledge is currently sitting unused in most machine-learning pipelines. So what if you BAKE IT IN?

That's the whole paper. Build a neural network whose training objective doesn't just say "match the data" but also says "satisfy the physics." Use the equations themselves as a regularization mechanism. The network is no longer free to produce any function that fits the data — it has to produce a function that also obeys the laws.

This is what the paper calls a physics informed neural network. PINN.

## How the mechanics work

The setup is so simple it almost feels like cheating. You have a partial differential equation. The general form they work with is:

> u_t + N[u] = 0

Here u(t, x) is the unknown solution and N is whatever nonlinear operator describes your physics — could be Burgers, could be Schrödinger, could be anything.

You approximate u by a deep neural network. So far so standard. But now you define a SECOND function f:

> f := u_t + N[u]

If u were exactly right, f would be zero everywhere. If u is wrong, f tells you how wrong, point by point.

Here's where automatic differentiation matters. Neural networks are differentiable end-to-end. You can compute u_t, u_x, u_xx directly from the network's weights, cheaply and exactly. Which means f is ALSO a neural network — sharing all of u's parameters, plus the differential structure of the PDE.

Now you train both networks at once. The loss has two terms. First term: match the observed data. Second term: drive f to zero at a set of scattered "collocation points" throughout the spatio-temporal domain. The first term says "fit my measurements." The second term says "wherever you don't have a measurement, you'd BETTER satisfy the equation."

That second term is the entire trick. The physics fills in the gaps where the data doesn't reach.

## The first demonstration — Burgers' equation

Burgers' equation is a classic test case from fluid mechanics. It's famous for being NASTY: at low viscosity it develops sharp internal layers, near-discontinuities that traditional numerical methods can only resolve by using extremely fine meshes.

The authors throw a PINN at it. The setup: 100 data points around the boundaries and the initial condition. Ten thousand collocation points scattered randomly through the (t, x) domain to enforce the equation. A nine-layer neural network with twenty neurons per layer.

What they get: the entire spatio-temporal solution, including that nasty sharp internal layer, with a relative error of 6.7 × 10⁻⁴. Two orders of magnitude better than their previous attempt using Gaussian processes. Training took about 60 seconds on a single GPU.

Critically: there's no mesh. The network represents u as a continuous function of t and x — you can query it anywhere. And the implementation is comically short. The paper inlines an 8-line TensorFlow snippet to make the point that this is a paradigm shift requiring almost no infrastructure.

## The Schrödinger stress test

The Burgers result is impressive but, you might think, special. So the authors deliberately pick a harder test: the nonlinear Schrödinger equation. Periodic boundaries (not Dirichlet). Complex-valued solutions (not real). A different shape of nonlinearity in the PDE itself.

They handle the complex part by splitting h(t, x) into real and imaginary components and using a multi-output network. Loss function now has three terms: initial-data match, periodic-boundary enforcement, and the physics residual at collocation points.

The setup: 50 initial-condition points, 50 boundary collocation points, 20,000 interior collocation points (sampled with Latin Hypercube Sampling). 5-layer network, 100 neurons per layer.

Result: relative L2 error of 1.97 × 10⁻³ across the whole spatio-temporal solution. From a handful of initial-data points, the network recovers the intricate nonlinear evolution of the wave function.

But this section also reveals a problem that motivates everything that comes next. Twenty thousand collocation points for a 1D problem on a small time window is a LOT. Scale up to 3D, or higher, and the number of collocation points needed to enforce the PDE everywhere grows exponentially with dimension. The curse of dimensionality, in PINN form.

So the question becomes: can we replace this scatter-collocation-points-everywhere approach with something more structured?

## Discrete-time PINNs — Runge-Kutta in the network

The answer in section 3 is yes. Don't scatter collocation points through time. Instead, BUILD time-stepping into the architecture.

The trick comes from classical numerical analysis. Runge-Kutta methods are workhorse schemes that advance a PDE from time t_n to t_{n+1} via a small number of intermediate "stages." There's a general q-stage template — the constants determine which specific scheme. Classical textbooks tell you implicit Runge-Kutta with high q is wonderful in theory but computationally crippling in practice, because each step requires solving a giant nonlinear system.

The PINN twist: put a multi-output neural network on the q stage values plus the final state. The network takes only x as input — time is encoded structurally through the Runge-Kutta stages, not as a continuous variable. The loss enforces consistency between predicted stage values and the Runge-Kutta equations. No collocation points scattered through time.

The authors test this on Burgers' equation again. The architecture: an IMPLICIT Runge-Kutta scheme with FIVE HUNDRED stages. A 4-layer network with 50 neurons per layer, and an output layer that predicts 501 quantities — the 500 stages plus the final state.

They claim implicit Runge-Kutta with arbitrarily large q comes at essentially no extra cost in the PINN framework (a footnote clarifies: only the last layer's parameter count grows linearly with q).

For Δt = 0.8 and q = 500, the theoretical local error is O(Δt^{1000}) ≈ 10⁻⁹⁷. That's WAY below machine precision. So all the error in the final result is dominated by network approximation, not time-stepping.

The headline result: starting from smooth data at t = 0.1, the network predicts the near-discontinuous Burgers solution at t = 0.9 in a SINGLE TIME STEP, with a relative L2 error of 8.2 × 10⁻⁴. The paper claims this is the first time an implicit Runge-Kutta scheme of that high order has ever been used.

## The Allen-Cahn rerun

To show the discrete-time approach generalizes, the authors throw it at the Allen-Cahn equation. Allen-Cahn comes from reaction-diffusion systems and describes phase separation in alloys — domains of different composition that spontaneously emerge from a uniform mixture. It has a CUBIC nonlinearity, different from Burgers' quadratic one.

Setup: 200 initial data points at t = 0.1, predict the solution at t = 0.9 in a single time step of Δt = 0.8. Network: 4 layers, 200 neurons per layer, 100-stage Runge-Kutta scheme.

Result: relative L2 error of 6.99 × 10⁻³. Sharp internal layers between phases resolved from 200 sparse points, no spatial mesh, one giant time step. The recipe holds across different flavors of nonlinearity.

## The honest paragraph

The closing section is unusually gracious for a flagship methods paper. The authors explicitly disclaim overreach: PINNs are NOT replacements for classical numerical methods. Those methods have matured over 50 years and meet the robustness and efficiency standards required in practice. The pitch is COEXISTENCE — PINNs add to the toolkit, they don't subtract from it.

Where PINNs add value: implementation simplicity, rapid prototyping of new ideas, and (this is the Part II pitch) inverse problems where you want to discover the equation from data rather than solve a known one.

The most important limitation they call out: uncertainty quantification. When the network spits out a predicted solution u(t, x), there's no built-in way to ask "how confident should I be in this value here?" Gaussian processes natively produce uncertainty estimates. PINNs don't. The authors flag this as an open research question for future work.

## The bigger picture

What just happened is a kind of cultural fusion. Mathematical physics, which is several hundred years of structured prior knowledge about how the universe actually works, gets fused with deep learning, which is a couple of decades of statistical learning machinery. The fusion happens through automatic differentiation, the trick that lets a neural network compute the partial derivatives of its own output and therefore evaluate a PDE residual.

The implication, if you sit with it, is sweeping. Anywhere in science where you have an equation you trust but data that's too sparse for a vanilla neural network, this template applies. You don't need new physics. You don't need new machine learning infrastructure. You need a loss function with two terms — match the data, satisfy the equation — and an auto-diff library. Run gradient descent.

The original paper was published in 2017. In the years since, PINNs have spread through computational fluid dynamics, biomechanics, geophysics, climate modeling, electromagnetics, materials science. They're not perfect — there are still convergence issues, uncertainty issues, problems where the optimization landscape is too rough. But the seed planted in this paper turned out to be one of the most influential ideas in scientific machine learning.
