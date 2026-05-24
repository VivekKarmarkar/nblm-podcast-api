journal_metadata:
  paper: arxiv_1711.10561
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: The paper was written by Maziar Raissi, Paris Perdikaris, and George Karniadakis,
  published in 2017 on arXiv.
excerpt: Maziar Raissi1 , Paris Perdikaris2 , and George Em Karniadakis1
location:
  page_pdf: 1
  page_printed: 1
  section: Title block (front matter)
  surrounding_context: 'Title page byline with affiliations: Brown University (Raissi,
    Karniadakis) and University of Pennsylvania (Perdikaris). arXiv preprint dated
    28 Nov 2017.'
comments: SUPPORTS. All three authors named verbatim. Year confirmed by arxiv tag
  "arXiv:1711.10561v1 [cs.AI] 28 Nov 2017" on same page.
---
index: 2
date: '2026-05-24'
status: matched
request: The authors coined the term "physics informed neural networks" (PINN) for
  networks that respect physical laws described by partial differential equations.
excerpt: |-
  We introduce physics informed neural networks – neural networks that
  are trained to solve supervised learning tasks while respecting any given law
  of physics described by general nonlinear partial differential equations.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Opening sentences of the paper's abstract, defining the new
    class of networks the rest of the paper develops.
comments: SUPPORTS. Verbatim introduction of "physics informed neural networks" in
  the abstract. Confirms both the term as authors' coinage and the conceptual scope
  (respecting PDEs).
---
index: 3
date: '2026-05-24'
status: matched
request: The PINN is constrained to respect symmetry, invariance, and conservation
  principles from the governing physical laws.
excerpt: |-
  Such neural networks are constrained to respect any symmetry,
  invariance, or conservation principles originating from the physical laws that
  govern the observed data, as modeled by general time-dependent and non-
  linear partial differential equations.
location:
  page_pdf: 3
  page_printed: 3
  section: 1.1 Problem setup and summary of contributions
  surrounding_context: Authors' framing of why physics-informed constraints matter
    — they constrain the space of admissible network outputs.
comments: SUPPORTS. Verbatim language about respecting conservation principles. Grounds
  the narrative's "network respects the equation" claim.
---
index: 4
date: '2026-05-24'
status: matched
request: The method uses automatic differentiation to differentiate the network with
  respect to its inputs, enabling evaluation of the PDE residual.
excerpt: |-
  We exploit recent developments in automatic differen-
  tiation [13] – one of the most useful but perhaps underused techniques in
  scientific computing – to differentiate neural networks with respect to their
  input coordinates and model parameters to obtain physics informed neural
  networks.
location:
  page_pdf: 3
  page_printed: 3
  section: 1.1 Problem setup and summary of contributions
  surrounding_context: Authors' description of automatic differentiation as the engineering
    tool that powers the PINN construction.
comments: SUPPORTS. Verbatim — auto-diff is the mechanism for differentiating the
  network, plus the paper explicitly calls it "underused" — which the narrative's
  metaphor leans on.
---
index: 5
date: '2026-05-24'
status: matched
request: Prior knowledge of physics acts as a regularization agent that constrains
  the space of admissible solutions.
excerpt: |-
  this prior information can act as
  a regularization agent that constrains the space of admissible solutions to a
  manageable size (for e.g., in incompressible fluid dynamics problems by dis-
  carding any non realistic flow solutions that violate the conservation of mass
  principle).
location:
  page_pdf: 2
  page_printed: 2
  section: 1 Introduction
  surrounding_context: Motivation paragraph explaining why physics priors are powerful
    in small-data regimes.
comments: SUPPORTS. The "regularization" framing of the physics-in-loss-function trick
  is verbatim. The narrative's "anywhere you don't have a thermometer you'd better
  satisfy Fourier's equation" is the pedagogical version of this.
---
index: 6
date: '2026-05-24'
status: matched
request: Burgers' equation arises in fluid mechanics, nonlinear acoustics, gas dynamics,
  and traffic flow.
excerpt: |-
  As an example, let us consider the Burgers’ equation. This equation arises
  in various areas of applied mathematics, including fluid mechanics, nonlinear
  acoustics, gas dynamics, and traffic flow [14].
location:
  page_pdf: 4
  page_printed: 4
  section: 2.1 Example (Burgers' Equation)
  surrounding_context: First sentence introducing Burgers' equation as the benchmark
    used for the continuous-time PINN demonstration.
comments: SUPPORTS. Verbatim list — fluid mechanics, nonlinear acoustics, gas dynamics,
  traffic flow. Confirms the narrative's "shock waves, traffic flow, fluid mechanics"
  framing.
---
index: 7
date: '2026-05-24'
status: matched
request: Low-viscosity Burgers' equation develops sharp internal layers that are notoriously
  hard to resolve with classical numerical methods.
excerpt: |-
  the viscosity parameters, Burgers’ equation can lead to shock formation that
  is notoriously hard to resolve by classical numerical methods.
location:
  page_pdf: 5
  page_printed: 5
  section: 2.1 Example (Burgers' Equation)
  surrounding_context: Sentence describing the difficulty of resolving low-viscosity
    Burgers solutions with classical numerics — motivates why PINNs are tested on
    this problem.
comments: SUPPORTS. Verbatim "notoriously hard to resolve" + "shock formation". Confirms
  the narrative's "sharp internal cliffs" + "tedious" framing.
---
index: 8
date: '2026-05-24'
status: matched
request: The Burgers PINN used a 9-layer network with 20 neurons per hidden layer,
  Nu=100 initial-and-boundary data points, and 10,000 collocation points.
excerpt: |-
  Specifically, given a set of Nu = 100 randomly distributed
  initial and boundary data, we learn the latent solution u(t, x) by training all
  3021 parameters of a 9-layer deep neural network using the mean squared
  error loss of (4). Each hidden layer contained 20 neurons and a hyperbolic
  tangent activation function.
location:
  page_pdf: 6
  page_printed: 6
  section: 2.1 Example (Burgers' Equation)
  surrounding_context: Description of the network architecture and training data setup
    for the headline Burgers experiment. The 10,000 collocation points are confirmed
    in Figure 1 caption on page 8.
comments: 'SUPPORTS. Verbatim — 9 layers, 20 neurons, Nu = 100. The 10,000 collocation
  count appears in the Figure 1 caption (page 8): "In addition we are using 10,000
  collocation points generated using a Latin Hypercube Sampling strategy."'
---
index: 9
date: '2026-05-24'
status: matched
request: The continuous-time Burgers PINN achieved a relative L2 error of 6.7e-4,
  two orders of magnitude better than the authors' previous Gaussian-process method,
  with training taking about 60 seconds on a single NVIDIA Titan X GPU.
excerpt: |-
  The relative L2 error for this case is 6.7 · 10−4 . Model training took
  approximately 60 seconds on a single NVIDIA Titan X GPU card.
location:
  page_pdf: 8
  page_printed: 8
  section: Figure 1 caption
  surrounding_context: Figure 1 caption summarizing the Burgers result, accuracy,
    and training cost. The "two orders of magnitude" comparison to Gaussian processes
    appears in the body text on page 7.
comments: SUPPORTS. Verbatim — 6.7e-4 error + 60 seconds + Titan X GPU. The "two orders
  of magnitude lower than the one reported in our previous work on data-driven solution
  of partial differential equation using Gaussian processes" claim is on page 7.
---
index: 10
date: '2026-05-24'
status: matched
request: The PINN prediction is obtained without any discretization of the spatio-temporal
  domain — it represents the solution as a continuous function.
excerpt: |-
  We must underline that, unlike any classical numerical method for solv-
  ing partial differential equations, this prediction is obtained without any
  sort of discretization of the spatio-temporal domain.
location:
  page_pdf: 7
  page_printed: 7
  section: 2.1 Example (Burgers' Equation)
  surrounding_context: Authors stress that the network represents the solution as
    a continuous function — no mesh, no grid.
comments: SUPPORTS. Verbatim — "without any sort of discretization of the spatio-temporal
  domain." Grounds the narrative's "no mesh, no fine grid, just a function" claim.
---
index: 11
date: '2026-05-24'
status: matched
request: A short TensorFlow code snippet is shown to highlight the implementation
  simplicity of the method.
excerpt: |-
  To highlight the simplicity in implementing this idea we have included a Python code
  snippet using Tensorflow [16]; currently one of the most popular and well
  documented open source libraries for machine learning computations.
location:
  page_pdf: 5
  page_printed: 5
  section: 2.1 Example (Burgers' Equation)
  surrounding_context: 'Lead-in to the inlined TensorFlow `def u(t, x): ...` and `def
    f(t, x): ...` code snippets on page 5.'
comments: PARTIALLY_SUPPORTS. The paper confirms a code snippet was shown and emphasizes
  implementation simplicity, but the narrative's "eight-line" character count is approximate
  — the snippet on page 5 is two functions whose combined body is roughly 8-10 lines
  of actual code. Not a quantitative claim of the paper itself; safe to leave as a
  colloquial approximation.
---
index: 12
date: '2026-05-24'
status: matched
request: The Schrödinger equation studied is the nonlinear Schrödinger equation used
  to study quantum mechanical systems, including nonlinear wave propagation in optical
  fibers and Bose-Einstein condensates.
excerpt: |-
  The
  one-dimensional nonlinear Schrödinger equation is a classical field equation
  that is used to study quantum mechanical systems, including nonlinear wave
  propagation in optical fibers and/or waveguides, Bose-Einstein condensates,
  and plasma waves.
location:
  page_pdf: 9
  page_printed: 9
  section: 2.2 Example (Schrödinger Equation)
  surrounding_context: Authors introduce the Schrödinger equation and list its physical
    applications.
comments: SUPPORTS. Verbatim — quantum mechanical systems, optical fibers, Bose-Einstein
  condensates. Narrative simplifies to "quantum mechanical wave functions, plus laser
  optics inside fiber-optic cables" which is faithful.
---
index: 13
date: '2026-05-24'
status: matched
request: The Schrödinger PINN was trained with 20,000 collocation points to enforce
  the equation inside the domain.
excerpt: |-
  In addition we are using 20,000 collocation points generated using
  a Latin Hypercube Sampling strategy.
location:
  page_pdf: 12
  page_printed: 12
  section: Figure 2 caption (Schrödinger)
  surrounding_context: Figure 2 caption gives the experimental setup for the Schrödinger
    PINN. Body text on page 11 also confirms "Nf = 20,000 randomly sampled collocation
    points used to enforce equation (5) inside the solution domain."
comments: SUPPORTS. Verbatim "20,000 collocation points" in both Figure 2 caption
  (page 12) and body text on page 11.
---
index: 14
date: '2026-05-24'
status: matched
request: The Schrödinger PINN achieved a relative L2 error of 1.97e-3.
excerpt: |-
  The resulting prediction error is validated against
  the test data for this problem, and is measured at 1.97 · 10−3 in the rela-
  tive L2 -norm.
location:
  page_pdf: 11
  page_printed: 11
  section: 2.2 Example (Schrödinger Equation)
  surrounding_context: Authors report the Schrödinger PINN's overall prediction error
    against the spectral-method reference solution.
comments: SUPPORTS. Verbatim 1.97e-3 relative L2 error. Confirms "the error stays
  small" claim in narrative.
---
index: 15
date: '2026-05-24'
status: matched
request: In higher dimensions, the number of collocation points needed to enforce
  the PDE grows exponentially — the curse of dimensionality.
excerpt: |-
  One potential limitation of the continuous time neural network models
  considered so far, stems from the need to use a large number of collocation
  points Nf in order to enforce physics informed constraints in the entire spatio-
  temporal domain. Although this poses no significant issues for problems
  in one or two spatial dimensions, it may introduce a severe bottleneck in
  higher dimensional problems, as the total number of collocation points needed
  to globally enforce a physics informed constrain (i.e., in our case a partial
  differential equation) will increase exponentially.
location:
  page_pdf: 11
  page_printed: 11
  section: End of 2.2 Schrödinger / lead-in to Section 3
  surrounding_context: Closing paragraph of the continuous-time section that motivates
    moving to the discrete-time Runge-Kutta approach in Section 3.
comments: SUPPORTS. Verbatim "will increase exponentially" with respect to collocation-point
  growth in higher dimensions. Narrative's "the number of points to peppershot through
  the domain grows exponentially with the dimension" maps exactly.
---
index: 16
date: '2026-05-24'
status: matched
request: The discrete-time PINN used an implicit Runge-Kutta scheme with 500 stages,
  the first time such a high-order scheme had ever been used.
excerpt: |-
  For illustration purposes, we start with a set of Nn = 250 initial
  data at t = 0.1, and employ a physics informed neural network induced by an
  implicit Runge-Kutta scheme with 500 stages to predict the solution at time
  t = 0.9 in a single step.
location:
  page_pdf: 14
  page_printed: 14
  section: 3.1 Example (Burgers' Equation) — discrete-time
  surrounding_context: Description of the discrete-time PINN's record-breaking 500-stage
    Runge-Kutta architecture. The "first time" claim is in the next paragraph on the
    same page.
comments: SUPPORTS. Verbatim "500 stages" + later "To our knowledge, this is the first
  time that an implicit Runge-Kutta scheme of that high-order has ever been used."
  Confirms the narrative's emphatic five-hundred-stage claim and the "nobody had ever
  used a scheme like that before" framing.
---
index: 17
date: '2026-05-24'
status: matched
request: The theoretical time-stepping error for the 500-stage Runge-Kutta + Δt=0.8
  case is approximately 10⁻⁹⁷, well below machine precision.
excerpt: |-
  The theoretical error estimates for this scheme predict
  a temporal error accumulation of O(∆t2q ) [24], which in our case translates
  into an error way below machine precision, i.e., ∆t2q = 0.81000 ≈ 10−97 .
location:
  page_pdf: 14
  page_printed: 14
  section: 3.1 Example (Burgers' Equation) — discrete-time
  surrounding_context: Authors compute the theoretical local truncation error for
    500 RK stages with Δt = 0.8, showing the time-stepping error is negligible — leaving
    only network approximation error.
comments: SUPPORTS. Verbatim 10⁻⁹⁷ figure. Narrative's "one followed by ninety-seven
  zeros below the decimal point" is the colloquial rendering of 10⁻⁹⁷.
---
index: 18
date: '2026-05-24'
status: matched
request: The discrete-time PINN predicted the Burgers solution at t=0.9 from data
  at t=0.1 in a single time step with relative L2 error 8.2e-4.
excerpt: |-
  Remarkably, starting from smooth
  initial data at t = 0.1 we can predict the nearly discontinuous solution at
  t = 0.9 in a single time-step with a relative L2 error of 8.2·10−4 .
location:
  page_pdf: 15
  page_printed: 15
  section: 3.1 Example (Burgers' Equation) — discrete-time
  surrounding_context: Authors report the single-time-step Burgers result with the
    discrete-time PINN.
comments: SUPPORTS. Verbatim 8.2e-4 error + single-time-step jump from t=0.1 to t=0.9.
  Confirms the narrative's "error is around eight ten-thousandths" + "one single time
  step" + "from time zero point one to time zero point nine" claims.
---
index: 19
date: '2026-05-24'
status: matched
request: The Allen-Cahn equation describes phase separation in multi-component alloy
  systems.
excerpt: |-
  The Allen-Cahn equation is a well-known equation from the area of reaction-
  diffusion systems. It describes the process of phase separation in multi-
  component alloy systems, including order-disorder transitions.
location:
  page_pdf: 17
  page_printed: 17
  section: 3.1.1 Example (Allen-Cahn Equation)
  surrounding_context: Authors introduce Allen-Cahn as a benchmark for the discrete-time
    PINN, with physical background on its origin in reaction-diffusion / alloy phase
    separation.
comments: SUPPORTS. Verbatim "phase separation in multi-component alloy systems".
  The narrative's "how a uniform mixture of two metals spontaneously separates into
  distinct domains" is the colloquial version of "phase separation in multi-component
  alloy systems."
---
index: 20
date: '2026-05-24'
status: matched
request: The Allen-Cahn PINN predicted the solution at t=0.9 from 200 sparse measurements
  at t=0.1, capturing sharp internal layers in a single time step.
excerpt: |-
  Evidently, despite the complex dynamics
  leading to a solution with two sharp internal layers, we are able to obtain an
  accurate prediction of the solution at t = 0.9 using only a small number of
  scattered measurements at t = 0.1.
location:
  page_pdf: 18
  page_printed: 18
  section: 3.1.1 Example (Allen-Cahn Equation)
  surrounding_context: Authors summarize the Allen-Cahn discrete-time PINN result.
    Setup details (Nn = 200 initial data points, single time step Δt = 0.8, network
    with 4 hidden layers × 200 neurons) appear in the preceding paragraphs.
comments: SUPPORTS. Verbatim — sharp internal layers + small number of scattered measurements
  + single time step. Confirms the narrative's "Sharp internal layers between the
  two phases, captured from two hundred sparse data points, in a single time step."
---
index: 21
date: '2026-05-24'
status: matched
request: The authors explicitly state PINNs are not replacements for classical numerical
  methods; the pitch is coexistence.
excerpt: |-
  We must note however that the proposed methods should not be viewed
  as replacements of classical numerical methods for solving partial differen-
  tial equations (e.g., finite elements, spectral methods, etc.). Such methods
  have matured over the last 50 years and, in many cases, meet the robustness
  and computational efficiency standards required in practice. Our message
  here, as advocated in Section 3, is that classical methods such as the Runge-
  Kutta time-stepping schemes can coexist in harmony with deep neural net-
  works
location:
  page_pdf: 20
  page_printed: 20
  section: 4 Summary and Discussion
  surrounding_context: Authors' explicit disclaimer that PINNs do not replace classical
    numerical methods, articulating a coexistence philosophy instead.
comments: SUPPORTS. Verbatim "should not be viewed as replacements" + "coexist in
  harmony". Confirms the narrative's "the pitch is coexistence, not overthrow" + "fifty
  years old and battle-tested and they're not going anywhere" claims.
---
index: 22
date: '2026-05-24'
status: matched
request: PINNs as proposed do not provide uncertainty estimates; quantifying prediction
  uncertainty is flagged as future work, in contrast to Gaussian processes which natively
  provide it.
excerpt: |-
  Finally, in terms of future work, one pressing question involves addressing
  the problem of quantifying the uncertainty associated with the neural net-
  work predictions. Although this important element was naturally addressed
  in previous work employing Gaussian processes [9], it not captured by the
  proposed methodology in its present form and requires further investigation.
location:
  page_pdf: 20
  page_printed: 20
  section: 4 Summary and Discussion
  surrounding_context: Authors call out lack of uncertainty quantification as a key
    open question for future work.
comments: SUPPORTS. Verbatim — uncertainty quantification flagged as pressing future
  work + naturally addressed by Gaussian processes but not by PINNs. Confirms the
  narrative's "no estimate of how confident it is" + "Gaussian processes natively
  produce uncertainty estimates" + "the authors call this out as a pressing open question"
  claims.
---
index: 23
date: '2026-05-24'
status: matched
request: The Schrödinger equation studied has complex-valued solutions with periodic
  boundary conditions.
excerpt: |-
  This example aims to highlight the ability of our method to handle pe-
  riodic boundary conditions, complex-valued solutions, as well as different
  types of nonlinearities in the governing partial differential equations.
location:
  page_pdf: 9
  page_printed: 9
  section: 2.2 Example (Schrödinger Equation)
  surrounding_context: 'Authors explicitly state the three properties Schrödinger
    is chosen to stress-test: periodic boundaries, complex-valued solutions, different
    nonlinearity.'
comments: SUPPORTS. Verbatim — periodic boundary conditions + complex-valued solutions.
  Confirms the narrative's "The solutions are complex-valued, and the boundaries are
  periodic — what flows out one side comes back in the other."
---
index: 24
date: '2026-05-24'
status: matched
request: Standard machine learning methods lack robustness in the small-data regime
  that often arises in physical and engineering systems.
excerpt: |-
  However, more often than not, in the course of analyzing complex physical,
  biological or engineering systems, the cost of data acquisition is prohibitive,
  and we are inevitably faced with the challenge of drawing conclusions and
  making decisions under partial information. In this small data regime, the
  vast majority of state-of-the art machine learning techniques (e.g., deep/-
  convolutional/recurrent neural networks) are lacking robustness and fail to
  provide any guarantees of convergence.
location:
  page_pdf: 2
  page_printed: 2
  section: 1 Introduction
  surrounding_context: Authors set up the small-data problem that motivates building
    physics into the network — vanilla neural networks fail when data is scarce.
comments: SUPPORTS. Verbatim — "small data regime" + "lacking robustness" + "cost
  of data acquisition is prohibitive". Confirms the narrative's "Vanilla neural networks
  fall apart with that little to chew on. They're data gluttons. Starve them and they
  hallucinate."
