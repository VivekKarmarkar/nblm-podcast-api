# Section 1 — Introduction (pages 1-3)

## The setup the paper opens with
Deep learning has been a giant success in image recognition, natural language processing, cognitive science, genomics — all the places where you have mountains of data. But the authors are interested in a different regime: physical, biological, and engineering systems, where collecting data can be expensive, slow, or just impossible. In that small-data world, the same neural networks that crush ImageNet stop working. They lose robustness. They stop converging.

## The load-bearing pivot
Here's the trick they propose. In physics, you almost never start from "nothing." You start from a giant pile of prior knowledge — Newton's laws, conservation of mass, conservation of momentum, the actual differential equations that govern how the system evolves. This prior knowledge is currently sitting unused in most machine-learning pipelines. The authors' idea: BAKE IT IN. Use the equations of physics as a regularization agent that constrains the neural network's space of possible solutions.

The metaphor the paper uses: in incompressible fluid dynamics, conservation of mass means any candidate flow that doesn't conserve mass is automatically nonsense. If the learning algorithm knows that, it can throw those out of consideration before it even starts. The data it does have gets amplified — the physics tells the network where in solution space to look.

## Why neural networks (not Gaussian processes)
They mention prior work using Gaussian processes for this kind of physics-informed inference. Gaussian processes have elegance and uncertainty estimates, but they hit two walls when you go nonlinear: (a) the authors had to locally linearize the nonlinear terms, which restricted them to discrete-time domains, and (b) the Bayesian prior assumptions become brittle in strongly nonlinear regimes.

So this paper switches to deep neural networks, leveraging their well-known capacity as universal function approximators. With networks, you can tackle nonlinear problems directly — no linearization, no time-stepping tricks needed up front.

## The mathematical seed
The whole paper is anchored to one general equation:
> u_t + N[u; λ] = 0

where u(t, x) is the latent (hidden) solution and N is a nonlinear operator parametrized by λ. This single template covers a huge class of physics — conservation laws, diffusion processes, advection-diffusion-reaction systems, kinetic equations. Burgers' equation, for example, is the special case where N[u; λ] = λ₁·u·u_x − λ₂·u_xx.

## Two problem classes
The authors split everything into two flavors:
1. **Data-driven SOLUTIONS** — given known λ, infer u(t, x). (This paper, Part I.)
2. **Data-driven DISCOVERY** — given measurements, infer the λ that best explains them. (Part II, separate paper.)

And cross-cutting both, they introduce two families of algorithms:
- **Continuous-time models** (sections 2)
- **Discrete-time models** (section 3)

## Verbatim load-bearing excerpt
> "Such neural networks are constrained to respect any symmetry, invariance, or conservation principles originating from the physical laws that govern the observed data, as modeled by general time-dependent and nonlinear partial differential equations."

That sentence captures the whole proposal — make the neural network respect physics by construction.

## The "automatic differentiation" hook
A small but absolutely load-bearing remark: they exploit AUTOMATIC DIFFERENTIATION to differentiate the neural network with respect to its inputs. Auto-diff is described by the paper as "one of the most useful but perhaps underused techniques in scientific computing." It's what lets them compute u_t, u_x, u_xx from the network output cheaply and exactly — which is the mechanical core of the whole method. Without auto-diff, this would be a much harder paper to implement.
