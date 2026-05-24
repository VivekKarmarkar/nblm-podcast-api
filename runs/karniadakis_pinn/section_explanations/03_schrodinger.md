# Section 2.2 — Schrödinger Equation (pages 9-12)

## Why this example exists
The Burgers example proved the method works on a single real-valued PDE with simple boundary conditions. The Schrödinger example is included to stress three additional capabilities:
1. **Periodic boundary conditions** (instead of Dirichlet)
2. **Complex-valued solutions** (instead of real-valued)
3. **A different type of nonlinearity** in the PDE itself

## The physics
The one-dimensional nonlinear Schrödinger equation is a classical field equation used to study quantum mechanical systems — nonlinear wave propagation in optical fibers and waveguides, Bose-Einstein condensates, plasma waves. In optics, the nonlinear term comes from the intensity-dependent index of refraction. In Bose-Einstein condensates, it comes from the mean-field interactions of an interacting N-body system. So it's a workhorse equation in physics.

The instance solved:
> i·h_t + 0.5·h_xx + |h|²·h = 0, x ∈ [−5, 5], t ∈ [0, π/2]

with periodic boundaries and h(0, x) = 2·sech(x) as the initial condition. Here h is complex-valued.

## How they handle "complex"
Trick: split h into real part u and imaginary part v. Then place a multi-output neural network on [u(t, x), v(t, x)]. The physics-informed network f then becomes complex-valued too, but mechanically it's just two real networks sharing structure.

## The loss has THREE terms now
With periodic boundaries, the loss splits into:
> MSE = MSE_0 + MSE_b + MSE_f

- **MSE_0**: error on initial data
- **MSE_b**: enforces periodic boundary conditions — h(t, −5) must equal h(t, 5), and h_x(t, −5) must equal h_x(t, 5)
- **MSE_f**: enforces the Schrödinger PDE at collocation points

## Setup specifics
- N0 = 50 initial data points (parsed randomly from a high-resolution reference solution generated with the Chebfun package)
- Nb = 50 collocation points on the boundary
- Nf = 20,000 collocation points inside the domain, sampled with Latin Hypercube Sampling
- 5-layer network, 100 neurons per layer, hyperbolic tangent activation

## Result
Relative L2 error of 1.97 × 10⁻³ across the full spatio-temporal solution. The bottom panel of Figure 2 shows comparisons at t = 0.59, 0.79, 0.98 — exact and predicted curves track each other extremely well.

> "Using only a handful of initial data, the physics informed neural network can accurately capture the intricate nonlinear behavior of the Schrödinger equation."

That's the headline.

## The crucial bottleneck this section reveals
The closing paragraph of section 2.2 is one of the most important paragraphs in the paper, because it sets up the existence of section 3. The authors observe:

> "One potential limitation of the continuous time neural network models considered so far, stems from the need to use a large number of collocation points Nf in order to enforce physics informed constraints in the entire spatio-temporal domain."

Twenty thousand collocation points for a 1D problem on a small time window is already a lot. Now imagine 3D, or higher. The number of collocation points needed to globally enforce the PDE grows exponentially with dimension. That's the curse of dimensionality, in PINN form.

This sets up the motivation for Discrete Time Models: a different parameterization that "circumvents the need for collocation points" by using Runge-Kutta time-stepping as the structural backbone.
