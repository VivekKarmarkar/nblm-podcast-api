journal_metadata:
  paper: arxiv_2301.11167
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: The authors of the paper are Roberto Molinaro, Yunan Yang, Bjorn Engquist,
  and Siddhartha Mishra.
excerpt: Roberto Molinaro 1 Yunan Yang 2 Björn Engquist 3 Siddhartha Mishra 1 4
location:
  page_pdf: 1
  page_printed: 1
  section: Author block (front matter)
  surrounding_context: Front-matter author line on the title page.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. All four authors named verbatim on page 1.
---
index: 2
date: '2026-05-24'
status: matched
request: Molinaro and Mishra are at ETH Zurich; Yang is at the Institute for Theoretical
  Studies at ETH Zurich; Engquist is at the University of Texas at Austin.
excerpt: |-
  Seminar for Applied Mathematics (SAM), ETH, Zürich.
  Institute for Theoretical Studies (ITS), ETH Zürich. 3 Department
  of Mathematics and the Oden Institute, The University of Texas at
  Austin, USA. 4 ETH AI Center, ETH, Zürich.
location:
  page_pdf: 1
  page_printed: 1
  section: Affiliations (front-matter footnote)
  surrounding_context: Affiliations footer beneath the author block on the title page.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. ETH Zurich for Molinaro/Mishra (SAM), Yang at ITS / ETH Zurich,
  Engquist at UT Austin. Confirms institutional claim.
---
index: 3
date: '2026-05-24'
status: matched
request: The class of PDE inverse problems considered is only well-defined as a mapping
  from operators to functions ("operator in, function out" shape).
excerpt: |-
  A large class of inverse problems for PDEs are
  only well-defined as mappings from operators to
  functions.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: First sentence of the abstract on page 1.
  before: null
  after: null
  bbox: null
comments: SUPPORTS verbatim. The "operator in, function out" framing is exactly what
  the paper opens with.
---
index: 4
date: '2026-05-24'
status: matched
request: The authors propose a novel architecture called Neural Inverse Operators
  (NIO) based on a suitable composition of DeepONets and FNOs.
excerpt: |-
  We propose
  a novel architecture termed Neural Inverse Opera-
  tors (NIOs) to solve these PDE inverse problems.
  Motivated by the underlying mathematical struc-
  ture, NIO is based on a suitable composition of
  DeepONets and FNOs to approximate mappings
  from operators to functions.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Mid-abstract proposal sentence on page 1.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The NIO acronym and the DeepONet+FNO composition are both stated
  verbatim. Confirms the architecture claim.
---
index: 5
date: '2026-05-24'
status: matched
request: The proposed NIO architecture stacks DeepONets and FNOs in that specific
  order to handle the operator-to-function inverse map.
excerpt: |-
  These heuristic considerations are generalized to the abstract
  formalism of the inverse problem (4) and motivate us to
  propose the composition (stacking) of DeepONets and FNO
  to result in the following map
location:
  page_pdf: 6
  page_printed: 6
  section: 3.3 A Motivating (Formal) Calculation, transitioning into 3.4 The Architecture
  surrounding_context: Mid-page 6 derivation that produces the DeepONet-then-FNO stack.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The "composition (stacking)" wording confirms the order is DeepONet
  first, FNO second, and that the architecture is motivated by the derivation that
  precedes it.
---
index: 6
date: '2026-05-24'
status: matched
request: A DeepONet alone cannot represent the nonlinear mode-mixing operator (because
  it is linear in its trunk-net basis functions), which is why an FNO is needed as
  the next stage.
excerpt: |-
  a DeepONet (17) is linear in its trunk-net basis functions
  and thus cannot represent the nonlinear mode mixing opera-
  tor M. Instead, one can do so by passing the outputs of the
  DeepONet to the nonlinear layers of an FNO (20), which
  also performs the final inversion operator I.
location:
  page_pdf: 6
  page_printed: 6
  section: 3.3 / 3.4 (architectural rationale)
  surrounding_context: Page 6, paragraph explaining why FNO must follow the DeepONet.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Confirms the design rationale stated in the narrative — DeepONet
  handles the basis / PDE-solve steps but cannot do the nonlinear mode mixing or the
  final inversion, which is the FNO's job.
---
index: 7
date: '2026-05-24'
status: matched
request: The motivating derivation that justifies the NIO architecture was done specifically
  for the inverse wave scattering problem (Helmholtz equation).
excerpt: |-
  We start by providing a heuristic motivation for our proposed
  architecture to learn the inverse map (4). To this end and
  for definiteness, we consider the inverse wave scattering
  problem for the Helmholtz equation (9), presented in section
  2.3.
location:
  page_pdf: 5
  page_printed: 5
  section: 3.3 A Motivating (Formal) Calculation
  surrounding_context: Opening sentences of section 3.3 on page 5.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's claim that the formal derivation is done for one
  of the four target problems (inverse wave scattering / Helmholtz) is exactly what
  the paper says.
---
index: 8
date: '2026-05-24'
status: matched
request: Randomized batching is the name of the training trick used so that the model
  is invariant to the number of input samples used to discretize the boundary observation
  operator.
excerpt: |-
  inspired by the well-known bagging algorithm widely used in
  machine learning, we propose an efficient and novel method
  to tackle this point which we term randomized batching.
  In this approach, given the sequence {Ψℓ}L
  ℓ=1, during each
  training iteration, an integer number Lb is randomly drawn
  from the set {2, . . . , L}. Then, Lb samples are randomly
  picked from {Ψℓ}L
  ℓ=1 and the new sequence {Ψk}L
  k=1 are
  fed into the model at each iteration during training.
location:
  page_pdf: 7
  page_printed: 7
  section: Page 7, paragraph at top
  surrounding_context: Definition of randomized batching, beginning at top of page
    7.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The randomized-batching mechanism is described exactly as the
  narrative summarizes it — each training iteration draws a random number of samples
  to feed the model.
---
index: 9
date: '2026-05-24'
status: matched
request: 'NIO is tested on four PDE inverse problems: the Calderon problem in EIT,
  inverse wave scattering with the Helmholtz equation, optical imaging via the radiative
  transport equation, and seismic imaging with the acoustic wave equation.'
excerpt: |-
  We tested the NIO on
  a variety of benchmark inverse problems. These include the
  Calderón Problem in electrical impedance tomography, in-
  verse wave scattering modelled with the Helmholtz equation,
  optical imaging using the radiative transport equation, and
  seismic imaging with the acoustic wave equation.
location:
  page_pdf: 9
  page_printed: 9
  section: 6. Discussion
  surrounding_context: Discussion section, on page 9, restating the suite of benchmarks.
  before: null
  after: null
  bbox: null
comments: SUPPORTS verbatim. The four problems and their governing equations are listed
  exactly as in the narrative.
---
index: 10
date: '2026-05-24'
status: matched
request: The two baselines used in the experiments are a DeepONet variant with a CNN
  branch net and a fully convolutional image-to-image neural network.
excerpt: |-
  As baselines in the following experiments, we choose two
  models. First, we consider a DeepONet with a CNN as
  the branch net in (17), which performs mixing of the input
  function within the branch itself
  ...
  Second, we consider a fully convolutional image-to-image
  neural network architecture (details in SM D.1). A variant
  of this architecture was already used in seismic imaging
  (full waveform inversion) in (Deng et al., 2021).
location:
  page_pdf: 7
  page_printed: 7
  section: 4. Empirical Results (preamble)
  surrounding_context: Page 7, baseline description preceding the per-problem experimental
    subsections.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The two baselines are (1) DeepONet with CNN branch and (2) fully
  convolutional image-to-image network — matching the narrative's description of "two
  baselines, one the natural DeepONet extension and one the FCNN from prior seismic
  work."
---
index: 11
date: '2026-05-24'
status: matched
request: NIO outperformed the baselines significantly on all four benchmark problems.
excerpt: |-
  For all
  these problems, NIO outperformed baselines significantly
  and provided accurate and, more importantly, robust ap-
  proximations to the unknown coefficients with small errors
location:
  page_pdf: 9
  page_printed: 9
  section: 6. Discussion
  surrounding_context: Discussion summary stating that NIO outperformed baselines
    on every problem.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's "NIO is the best or tied for the best on every
  benchmark" claim is supported verbatim — paper says "NIO outperformed baselines
  significantly" across all four problems.
---
index: 12
date: '2026-05-24'
status: matched
request: On the heart-and-lungs EIT phantom, the D-bar method has a much larger error
  (8.75%) than NIO.
excerpt: |-
  In contrast, a traditional direct method such as the D-bar
  method (Muller & Siltanen, 2012) has a larger error of
  8.75% for this numerical inversion test (see SM Section E.8
  for details).
location:
  page_pdf: 7
  page_printed: 7
  section: 4.1 Calderon Problem for EIT (heart-and-lungs sub-experiment)
  surrounding_context: Page 7, end of EIT subsection discussing the heart-and-lungs
    phantom comparison.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The 8.75% D-bar error on the heart-and-lungs phantom is verbatim.
  The narrative claim that NIO is below 1% while D-bar is around 8.75% is consistent
  with this and with SM page 33 ("L1-test error for the D-bar method is an unacceptably
  high 8.75%, compared to the almost 0.15% test error with NIO").
---
index: 13
date: '2026-05-24'
status: matched
request: NIO is robust to noise added to the boundary inputs at test time, to changes
  in grid resolution, and to randomly chosen sensor locations.
excerpt: |-
  we start with adding
  noise to the inputs of each of the benchmarks at test time
  and present the resulting test errors in SM Table 8 to ob-
  serve that NIO (as well as the baselines) are not sensitive
  to this noise. Next, in SM Table 9, we plot the test errors
  for the models when the underlying grid resolution is varied
  at test time to observe that NIO is not sensitive to the input
  grid resolution. Finally, in SM Table 10, we present errors
  when the locations of input sensors are chosen randomly at
  test time, in contrast to sensors located on a uniform grid
  at training, to see that NIO is also robust to this variation.
location:
  page_pdf: 8
  page_printed: 8
  section: 4.5 Robustness and Computational Efficiency of NIO
  surrounding_context: Page 8, robustness summary block in section 4.5.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The three robustness tests in the narrative (noise, grid resolution,
  random sensor locations) are stated verbatim in the same order, all reporting NIO
  robust.
---
index: 14
date: '2026-05-24'
status: matched
request: When the number of input samples is changed at test time, NIO degrades gracefully
  (because of randomized batching), while baselines collapse.
excerpt: |-
  We clearly see that NIO is very robust to this fluctuation,
  completely contrasting to the baselines whose performance
  ...
  deteriorates, and the test errors increase by almost an or-
  der of magnitude. This demonstrates that NIO genuinely
  learns the underlying inverse map rather than just a discrete
  representation of it.
location:
  page_pdf: 8
  page_printed: 8
  section: 4.5 Robustness and Computational Efficiency of NIO
  surrounding_context: Page 8 bottom and into top of page 9, sample-count robustness
    test on inverse wave scattering.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's claim that NIO degrades gracefully under sample-count
  change while baselines collapse is supported verbatim. The paper also frames the
  result as evidence that "NIO genuinely learns the underlying inverse map" — matching
  the narrative's interpretive line.
---
index: 15
date: '2026-05-24'
status: matched
request: On the inverse wave scattering benchmark (out-of-distribution test), NIO
  has 2.3% L1 error and PDE-constrained optimization has 11.1% L1 error.
excerpt: |-
  The L1 -test errors are 2.3% for
  NIO and 11.1% for PDE-constrained optimization.
location:
  page_pdf: 9
  page_printed: 9
  section: 4.5 Robustness and Computational Efficiency of NIO (NIO vs PDE-constrained
    optimization comparison)
  surrounding_context: Page 9, NIO vs PDE-constrained optimization on out-of-distribution
    inverse wave scattering test.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The specific error numbers (2.3% vs 11.1%) and the comparison
  are verbatim. The ~5x accuracy advantage in the narrative is the ratio 11.1/2.3
  ≈ 4.83.
---
index: 16
date: '2026-05-24'
status: matched
request: NIO inference takes less than 1 second on a CPU; PDE-constrained optimization
  takes 8.5 hours on a GPU. NIO is 5 times more accurate while being 4 orders of magnitude
  faster.
excerpt: |-
  Moreover, it took less than 1 sec of inference time for NIO (on a
  CPU) compared to a single GPU training time of 8.5 hours
  for the PDE-constrained optimization problem. Thus, this
  experiment demonstrates the real efficiency of NIO as it is
  5 times more accurate while being 4 orders of magnitude
  faster than the PDE-constrained optimization algorithm.
location:
  page_pdf: 9
  page_printed: 9
  section: 4.5 Robustness and Computational Efficiency of NIO
  surrounding_context: Page 9, headline comparison of NIO inference time vs PDE-constrained
    optimization training time.
  before: null
  after: null
  bbox: null
comments: SUPPORTS verbatim. "Less than 1 sec on CPU", "8.5 hours on GPU", "5 times
  more accurate while being 4 orders of magnitude faster" — every numerical claim
  in the narrative on this point is directly grounded.
---
index: 17
date: '2026-05-24'
status: matched
request: Existing operator learning frameworks (DeepONets and FNOs) only map functions
  to functions, so they need to be adapted to handle the operator-to-function inverse
  map.
excerpt: |-
  Both operator learning frameworks (DeepONet and FNO)
  and their variants map functions to functions. Hence, they
  cannot directly be used to learn the inverse map F−1 (4),
  which maps operators to functions. Therefore, we need to
  modify and adapt these architectures to learn the inverse
  map.
location:
  page_pdf: 5
  page_printed: 5
  section: 3.2 Existing Operator Learning Architectures
  surrounding_context: Page 5, paragraph immediately before section 3.3 Motivating
    Calculation.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's central gap framing — "existing operator-learning
  architectures take function in / function out, but the inverse problem is operator
  in / function out" — is stated verbatim by the paper, and the verb "modify and adapt"
  is what motivates NIO.
---
index: 18
date: '2026-05-24'
status: matched
request: The Calderon problem for EIT is governed by an elliptic PDE on the domain.
excerpt: |-
  Let the coefficient 0 < a ∈ C 2(D) represent the conduc-
  tivity of the underlying medium (domain D ⊂ Rd) and the
  associated PDE (1) is the following elliptic equation,
  −∇ · a(z)∇u = 0, z ∈ D,
location:
  page_pdf: 3
  page_printed: 3
  section: 2.2 Calderon Problem (EIT)
  surrounding_context: Page 3, opening of section 2.2 defining the elliptic equation
    for EIT.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative says "The math here is governed by an elliptic equation"
  for the EIT problem — exactly what the paper states verbatim.
---
index: 19
date: '2026-05-24'
status: matched
request: The "first paper" claim — this is the first end-to-end machine-learning framework
  specifically built for learning maps between operators and functions for PDE inverse
  problems.
excerpt: |-
  As this is the first paper
  where an end-to-end machine learning framework is pro-
  posed for learning maps between operators and functions,
  various extensions are possible.
location:
  page_pdf: 9
  page_printed: 9
  section: 6. Discussion
  surrounding_context: Page 9, discussion section claim about novelty.
  before: null
  after: null
  bbox: null
comments: SUPPORTS verbatim. The narrative says "this is the first end-to-end machine-learning
  framework specifically built for inverse problems with the operator-in/function-out
  shape" — matches the authors' explicit claim word for word.
---
index: 20
date: '2026-05-24'
status: matched
request: The classical alternative for solving these PDE inverse problems is iterative
  gradient-based PDE-constrained optimization, which is expensive because it repeatedly
  applies forward and adjoint PDE solvers.
excerpt: |-
  iterative numerical algorithms
  based on the PDE-constrained optimization are commonly
  used to approximate the solution (Chavent, 2010). These
  algorithms repeatedly apply the forward and adjoint PDE
  solvers to converge to the unknown coefficient. However, a
  large number of iterations might be necessary, which leads
  to prohibitively high computational costs as numerous calls
  to PDE solvers are very expensive, particularly in two and
  three space dimensions.
location:
  page_pdf: 1
  page_printed: 1
  section: 1. Introduction
  surrounding_context: Page 1, right column, introduction's discussion of the classical
    alternative.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's "guess-and-check loop, expensive because each
  iteration solves the full physics equation, takes hours in 3D" claim is supported
  almost verbatim.
---
index: 21
date: '2026-05-24'
status: matched
request: Future work flagged by the authors includes other operator-learning architectures
  (LOCA, VIDON, graph-based), higher-dimensional (3D) problems particularly in seismic,
  and theoretical approximation/universality bounds.
excerpt: |-
  For instance, other archi-
  tectures, such as recently proposed LOCA (Kissas et al.,
  2022), VIDON (Prasthofer et al., 2022), or graph-based ap-
  proaches (Boussif et al., 2022; Brandstetter et al., 2022), can
  be adapted in this context. Problems in higher-dimensional
  (particularly with seismic) imaging need to be considered
  to explore how NIOs scale with increasing problem size. Fi-
  nally, approximation bounds and universality results, in the
  spirit of (Lanthaler et al., 2022; Kovachki et al., 2021a) need
  to be derived in order to place NIOs on a solid theoretical
  footing.
location:
  page_pdf: 9
  page_printed: 9
  section: 6. Discussion
  surrounding_context: Page 9, future-work paragraph at the end of the discussion
    section.
  before: null
  after: null
  bbox: null
comments: SUPPORTS verbatim. The narrative's three open directions (other architectures,
  3D scaling, theoretical guarantees) are stated almost word-for-word by the paper.
---
index: 22
date: '2026-05-24'
status: matched
request: NIO inference is several orders of magnitude faster than existing direct
  and PDE-constrained optimization methods.
excerpt: |-
  NIOs
  significantly outperform baselines and solve PDE
  inverse problems robustly, accurately and are sev-
  eral orders of magnitude faster than existing direct
  and PDE-constrained optimization methods.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Page 1, closing of the abstract.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. The narrative's headline "several orders of magnitude faster than
  the existing approaches" is a direct paraphrase of the abstract.
---
index: 23
date: '2026-05-24'
status: matched
request: The narrative says "Maxwell's equations for electrical tomography" as an
  example of a governing physics equation, alongside the wave equation for seismic
  and radiative transport for optics.
excerpt: |-
  Let the coefficient 0 < a ∈ C 2(D) represent the conduc-
  tivity of the underlying medium (domain D ⊂ Rd) and the
  associated PDE (1) is the following elliptic equation,
  −∇ · a(z)∇u = 0, z ∈ D,
  u(z) = g(z), z ∈ ∂D,
location:
  page_pdf: 3
  page_printed: 3
  section: 2.2 Calderon Problem (EIT)
  surrounding_context: Page 3, top of section 2.2, defining the governing PDE for
    EIT.
  before: null
  after: null
  bbox: null
comments: PARTIALLY_SUPPORTS. The paper actually presents EIT as governed by a static
  elliptic equation (Poisson-type with variable coefficient — −∇·(a∇u)=0), not by
  the full Maxwell's equations. The elliptic equation IS derivable from Maxwell's
  under the quasi-static approximation, so "Maxwell's equations for electrical tomography"
  is physicist's shorthand that is defensible but slightly overgeneralizes — the paper
  itself never names Maxwell's equations. CORRECTION applied in narrative_final.md,
  replacing "Maxwell's equations for electrical tomography" with "the elliptic equation
  for electrical tomography" to match the paper's framing precisely.
