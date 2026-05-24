# Section 2 — Continuous Time Models + Burgers' Equation (pages 4-9)

## The core construction
The setup is disarmingly simple. You have a PDE of the form:
> u_t + N[u] = 0

Define a second function f as:
> f := u_t + N[u]

If u were the true solution, f would be exactly zero everywhere. If u is wrong, f measures how wrong — point by point.

Now approximate u(t, x) with a deep neural network. Because neural networks are differentiable end-to-end (thanks to automatic differentiation), you can compute u_t and u_x and u_xx directly from the network's weights. That means f(t, x) is ALSO a neural network — sharing all of u's parameters, plus the differential structure of the PDE.

You now have two networks: u and f. They share weights. Train both at once.

## The loss function — the entire trick
The paper trains by minimizing:
> MSE = MSE_u + MSE_f

Two terms. The first, MSE_u, is just the standard supervised loss: predicted u vs. observed u on initial and boundary data points. The second, MSE_f, is the PHYSICS term: it pushes f toward zero at a set of collocation points — randomly sampled points (t_i, x_i) scattered through the spatio-temporal domain where the PDE is supposed to hold.

That second term is the entire trick. It tells the neural network: "wherever you don't have data, you'd BETTER satisfy the equation." It acts as a regularization mechanism that penalizes any network output that violates the physics. The paper explicitly calls this out as the key property that lets PINNs train on tiny datasets.

## The Burgers' equation example
Burgers' equation is a one-dimensional PDE that shows up in fluid mechanics, nonlinear acoustics, gas dynamics, and traffic flow. The specific instance they solve:
> u_t + u·u_x − (0.01/π)·u_xx = 0, x ∈ [−1, 1], t ∈ [0, 1]

with Dirichlet boundary conditions (u = 0 at the walls) and a sine-wave initial condition.

This equation is famous for being NASTY: for small viscosity, it forms shocks — near-discontinuities — that classical numerical methods struggle to resolve without elaborate spatial meshing.

## What they show in code
A small load-bearing detail: the paper inlines an 8-line TensorFlow snippet for the physics-informed network f(t, x). It's almost trivially short — a few calls to tf.gradients to compute partial derivatives of u with respect to t and x. The implementation simplicity is part of the message: this is a paradigm shift requiring almost no infrastructure beyond a standard deep-learning library.

## The result
With Nu = 100 initial-and-boundary training points and Nf = 10,000 collocation points, a 9-layer network with 20 neurons per layer reproduces the entire spatio-temporal solution of Burgers with a relative L2 error of 6.7 × 10⁻⁴. That's two orders of magnitude better than the authors' previous Gaussian-process approach.

Critically: this is achieved WITHOUT any discretization of the spatio-temporal domain. There's no mesh. The network represents u as a continuous function of (t, x), and you can query it anywhere. Training the whole thing took about 60 seconds on a single NVIDIA Titan X GPU.

## The sharp internal layer
The paper specifically highlights that Burgers' solution develops a sharp internal layer around t = 0.4 — the shock-like feature that classical methods need fine meshes to resolve. The PINN captures it accurately from a handful of training points. That's the headline-grabbing demonstration.

## Sensitivity studies (Tables 1, 2)
They run two systematic sweeps:
- Vary Nu (initial-and-boundary data) and Nf (collocation points) with fixed 9-layer architecture: Table 1 shows error generally decreasing as both increase.
- Vary network depth and width with fixed Nu = 100, Nf = 10,000: Table 2 shows error decreasing with capacity.

Important footnote: the case Nf = 0 corresponds to a standard neural network that doesn't know about the PDE at all. That's the control. The physics term clearly carries weight.

## The load-bearing claim
> "A key property of physics informed neural networks is that they can be effectively trained using small data sets; a setting often encountered in the study of physical systems for which the cost of data acquisition may be prohibitive."

This is the whole motivation paying off in practice. You can train with very few examples because the physics constrains the network for you.
