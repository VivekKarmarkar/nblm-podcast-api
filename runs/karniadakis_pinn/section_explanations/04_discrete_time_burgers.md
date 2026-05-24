# Section 3 — Discrete Time Models + Burgers' Revisited (pages 12-17)

## What changed
The continuous-time PINN minimized residual error over a CLOUD of collocation points scattered through the entire (t, x) domain. That works, but as dimension grows, you need exponentially more points. Section 3 proposes a different structural choice: don't scatter collocation points through time — instead, BUILD time-stepping right into the network architecture using classical Runge-Kutta methods.

## The Runge-Kutta backbone
Runge-Kutta methods are workhorse classical numerical schemes for advancing a PDE forward in time. Given the solution at time t_n, they advance to t_{n+1} via a small number of intermediate "stages." The paper writes down the general q-stage form:

> u_{n+ci} = u_n − Δt · Σ_j a_ij · N[u_{n+cj}],  for i = 1, ..., q
> u_{n+1} = u_n − Δt · Σ_j b_j · N[u_{n+cj}]

This is the standard Runge-Kutta template; the constants {a_ij, b_j, c_i} determine which specific scheme (implicit or explicit, what order).

The PINN twist: instead of evaluating each stage with classical numerics, the authors put a multi-output neural network on the q stage solutions [u_{n+c1}(x), ..., u_{n+cq}(x), u_{n+1}(x)] all at once. The network now takes ONLY x as input — time is encoded structurally through the Runge-Kutta stages, not as a continuous input. The loss enforces consistency between the predicted stage values and the Runge-Kutta equations.

## The training loss
Two terms again:
> SSE = SSE_n + SSE_b

- **SSE_n**: error of the stage predictions against observed data at time t_n
- **SSE_b**: error at the spatial boundaries x = −1, x = 1 for all stages

NO collocation points scattered through time. The Runge-Kutta structure replaces them.

## The Burgers' test, redone in discrete-time mode
Same Burgers PDE as section 2.1. But now: start with Nn = 250 data points at t = 0.1, take ONE giant time step of size Δt = 0.8, and predict the solution at t = 0.9.

The architecture: an implicit Runge-Kutta scheme with 500 stages (q = 500). A 4-layer neural network with 50 neurons per hidden layer, and an output layer that predicts 501 quantities — the 500 RK stages plus the final state.

## The mind-blowing claim
Classical numerical analysis textbooks tell you implicit Runge-Kutta schemes with high q are wonderful in theory but computationally crippling in practice — each step requires solving a giant nonlinear system. The paper claims that in the PINN framework, this cost goes away:

> "Here we can employ implicit Runge-Kutta schemes with an arbitrarily large number of stages at effectively no extra cost."

(Footnote clarifies "no extra cost" means only the LAST layer of the network grows linearly with q — the rest is fixed.)

The theoretical local truncation error for a q-stage scheme is O(Δt^{2q}). For Δt = 0.8 and q = 500, that's roughly 0.81000 ≈ 10⁻⁹⁷ — way below machine precision. So error is dominated by network approximation, not by time-stepping.

## The result
Starting from smooth data at t = 0.1, the network predicts the near-discontinuous solution at t = 0.9 in a SINGLE TIME STEP, with a relative L2 error of 8.2 × 10⁻⁴. Two orders of magnitude better than prior Gaussian-process work.

> "To our knowledge, this is the first time that an implicit Runge-Kutta scheme of that high-order has ever been used."

That's the engineering punchline. Classical methods can't go to q = 500. PINNs can.

## The sensitivity sweep (Tables 3, 4)
- Table 3: vary network depth × width. As capacity goes up, accuracy improves.
- Table 4: vary q × Δt. Low q + large Δt = bad accuracy. But push q to 32, 100, 500 and you can take Δt = 0.8 in one shot. Stability holds because implicit Runge-Kutta is A-stable regardless of order — ideal for stiff problems.

## Why this matters
The discrete-time model trades the curse-of-dimensionality issue of the continuous-time approach (too many collocation points in high dimensions) for a much more compact structural prior (Runge-Kutta time-stepping baked into the architecture). The two approaches are complementary — different tools for different shapes of problems.
