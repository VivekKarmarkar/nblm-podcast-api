journal_metadata:
  paper: arxiv_2010.08895
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: The paper is from a Caltech and Purdue group, with lead author Zongyi Li,
  in the Anima Anandkumar group.
excerpt: |-
  Zongyi Li                           Nikola Kovachki                         Kamyar Azizzadenesheli
  zongyili@caltech.edu                nkovachki@caltech.edu                   kamyar@purdue.edu

  Burigede Liu          Kaushik Bhattacharya            Andrew Stuart           Anima Anandkumar
  bgl@caltech.edu       bhatta@caltech.edu              astuart@caltech.edu     anima@caltech.edu
location:
  page_pdf: 1
  page_printed: 1
  section: Author block (front matter)
  surrounding_context: Author affiliations on title page.
comments: SUPPORTS. Lead author Zongyi Li, Caltech and Purdue affiliations evident
  from email domains (@caltech.edu, @purdue.edu). Anima Anandkumar (last author) is
  the group head, confirmed by domain.
---
index: 2
date: '2026-05-24'
status: matched
request: The paper was published at the International Conference on Learning Representations
  (ICLR) in 2021.
excerpt: Published as a conference paper at ICLR 2021
location:
  page_pdf: 1
  page_printed: 1
  section: Header banner
  surrounding_context: Banner repeated on every page of the paper.
comments: SUPPORTS. ICLR 2021 venue confirmed verbatim by the page header that appears
  on every page.
---
index: 3
date: '2026-05-24'
status: matched
request: Classical neural networks learn mappings between finite-dimensional Euclidean
  spaces, whereas neural operators learn mappings between function spaces.
excerpt: |-
  The classical development of neural networks has primarily focused on learning
  mappings between finite-dimensional Euclidean spaces. Recently, this has been
  generalized to neural operators that learn mappings between function spaces.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: First two sentences of the abstract.
comments: SUPPORTS. The load-bearing distinction in the narrative — "regular networks
  learn functions, this learns rules that turn functions into functions" — is confirmed
  verbatim in the abstract.
---
index: 4
date: '2026-05-24'
status: matched
request: The Fourier neural operator is up to three orders of magnitude (~1000x) faster
  than traditional PDE solvers.
excerpt: |-
  It is up to
  three orders of magnitude faster compared to traditional PDE solvers.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Concluding sentences of the abstract.
comments: SUPPORTS. "Three orders of magnitude faster" = 1000x faster. Confirms the
  "thousand times faster" headline used throughout the narrative.
---
index: 5
date: '2026-05-24'
status: matched
request: FNO is the first ML-based method to successfully model turbulent flows with
  zero-shot super-resolution.
excerpt: |-
  The Fourier neural operator is the first ML-based method
  to successfully model turbulent flows with zero-shot super-resolution.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Abstract paragraph.
comments: SUPPORTS. "First ML-based method" claim verbatim from abstract. Confirms
  narrative's "nobody had ever cracked the turbulent regime with machine learning
  before. This was the first method that could."
---
index: 6
date: '2026-05-24'
status: matched
request: Designing materials such as airfoils requires solving an inverse problem
  with thousands of evaluations of the forward model.
excerpt: |-
  For example, when designing materials such as airfoils, one
  needs to solve the associated inverse problem where thousands of evaluations of the forward model
  are needed. A fast method can make such problems feasible.
location:
  page_pdf: 1
  page_printed: 1
  section: 1 Introduction
  surrounding_context: First paragraph of the introduction.
comments: SUPPORTS. The narrative's airfoil-design motivation ("ten thousand slightly
  different wing shapes") is verbatim supported by the paper's example.
---
index: 7
date: '2026-05-24'
status: matched
request: 'Traditional FEM and FDM solvers impose a trade-off on resolution: coarse
  grids are fast but inaccurate, fine grids are accurate but slow.'
excerpt: |-
  Traditional solvers such as finite element meth-
  ods (FEM) and finite difference methods (FDM) solve the equation by discretizing the space. There-
  fore, they impose a trade-off on the resolution: coarse grids are fast but less accurate; fine grids are
  accurate but slow.
location:
  page_pdf: 1
  page_printed: 1
  section: 1 Introduction (Conventional solvers vs. Data-driven methods)
  surrounding_context: Second paragraph of the introduction.
comments: SUPPORTS. The narrative's "The finer you chop the boxes, the more accurate
  your answer. Also the slower. Always a trade-off" is a direct paraphrase of this
  passage.
---
index: 8
date: '2026-05-24'
status: matched
request: Classical neural networks map between finite-dimensional spaces and can therefore
  only learn solutions tied to a specific discretization.
excerpt: |-
  However, classical neural networks map between
  finite-dimensional spaces and can therefore only learn solutions tied to a specific discretization.
  This is often a limitation for practical applications and therefore the development of mesh-invariant
  neural networks is required.
location:
  page_pdf: 1
  page_printed: 1
  section: 1 Introduction
  surrounding_context: Second paragraph of introduction.
comments: SUPPORTS. The narrative's "bolted to one specific grid resolution... like
  teaching someone to read using only one font and watching them get baffled by Helvetica"
  is a vivid paraphrase of this limitation.
---
index: 9
date: '2026-05-24'
status: matched
request: Neural-FEM approaches parameterize the solution as a neural network for one
  specific instance of the PDE, and require training a new network for every new instance.
excerpt: |-
  Neural-FEM. The second approach directly parameterizes the solution function as a neural net-
  work (E & Yu, 2018; Raissi et al., 2019; Bar & Sochen, 2019; Smith et al., 2020; Pan & Duraisamy,
  2020). This approach is designed to model one specific instance of the PDE, not the solution oper-
  ator. It is mesh-independent and accurate, but for any given new instance of the functional parame-
  ter/coefficient, it requires training a new neural network.
location:
  page_pdf: 2
  page_printed: 2
  section: 1 Introduction (Neural-FEM)
  surrounding_context: Paragraph describing prior approaches.
comments: SUPPORTS. Narrative's description of the second camp — "use a small neural
  network to represent the answer itself... if you change the wing, you have to retrain
  from scratch. Days of GPU time for one design" — is a faithful paraphrase.
---
index: 10
date: '2026-05-24'
status: matched
request: The Fourier neural operator is the first work to learn a resolution-invariant
  solution operator for Navier-Stokes in the turbulent regime, where graph-based neural
  operators do not converge.
excerpt: |-
  • The Fourier neural operator is the first work that learns the resolution-invariant solution operator
    for the family of Navier-Stokes equation in the turbulent regime, where previous graph-based
    neural operators do not converge.
location:
  page_pdf: 3
  page_printed: 3
  section: 1 Introduction (Our Contributions)
  surrounding_context: First bullet of the Our Contributions list.
comments: SUPPORTS. Confirms verbatim. Also clarifies what the narrative referred
  to as "earlier groups had tried... nobody had cracked turbulence" — those were specifically
  graph-based neural operators that did not converge.
---
index: 11
date: '2026-05-24'
status: matched
request: 'Zero-shot super-resolution: the method can be trained on a lower resolution
  and directly evaluated on a higher resolution.'
excerpt: |-
  • By construction, the method shares the same learned network parameters irrespective of the dis-
    cretization used on the input and output spaces. It can do zero-shot super-resolution: trained on a
    lower resolution directly evaluated on a higher resolution, as shown in Figure 1.
location:
  page_pdf: 3
  page_printed: 3
  section: 1 Introduction (Our Contributions)
  surrounding_context: Second bullet of the Our Contributions list.
comments: SUPPORTS. Verbatim confirmation of the zero-shot super-resolution claim
  that anchors the central narrative arc.
---
index: 12
date: '2026-05-24'
status: matched
request: At fixed 64x64 resolution, FNO achieves 30% lower error on Burgers, 60% lower
  on Darcy, and 30% lower on Navier-Stokes (turbulent regime).
excerpt: |-
  • The proposed method consistently outperforms all existing deep learning methods even when
    fixing the resolution to be 64×64. It achieves error rates that are 30% lower on Burgers’ Equation,
    60% lower on Darcy Flow, and 30% lower on Navier Stokes (turbulent regime with viscosity
    ν = 1e−4).
location:
  page_pdf: 3
  page_printed: 3
  section: 1 Introduction (Our Contributions)
  surrounding_context: Third bullet of the Our Contributions list.
comments: 'SUPPORTS. Confirms the narrative''s "beats every prior approach. Lowest
  error by a clear margin" (Burgers) and "beats every competitor by close to a factor
  of ten" (Darcy: 60% lower is roughly an order of magnitude in relative terms). The
  narrative''s "factor of ten" / "almost an order of magnitude" claim for Darcy is
  somewhat strong — the 60% relative error reduction is closer to a factor of 2.5
  reduction. NOTE: this is slightly stronger than the paper supports for Darcy and
  will be softened in narrative_final.md.'
---
index: 13
date: '2026-05-24'
status: matched
request: On Darcy Flow, FNO obtains nearly one order of magnitude lower relative error
  compared to all benchmarks.
excerpt: |-
  The pro-
  posed Fourier neural operator obtains nearly one order of magnitude lower relative error compared
  to any benchmarks. We again observe the invariance of the error with respect to the resolution.
location:
  page_pdf: 8
  page_printed: 8
  section: 5.2 Darcy Flow
  surrounding_context: Results paragraph at end of Darcy Flow subsection.
comments: SUPPORTS. The narrative's "beats every competitor by close to a factor of
  ten. Almost an order of magnitude" is verbatim aligned with the paper's "nearly
  one order of magnitude lower relative error." Entry 12's earlier caveat is therefore
  RETRACTED — the strong claim is paper-supported.
---
index: 14
date: '2026-05-24'
status: matched
request: On a 256x256 grid, FNO has an inference time of 0.005s vs. 2.2s for the pseudo-spectral
  solver for Navier-Stokes.
excerpt: |-
  • On a 256 × 256 grid, the Fourier neural operator has an inference time of only 0.005s compared
    to the 2.2s of the pseudo-spectral method used to solve Navier-Stokes.
location:
  page_pdf: 3
  page_printed: 3
  section: 1 Introduction (Our Contributions)
  surrounding_context: Fourth bullet of the Our Contributions list.
comments: SUPPORTS. The narrative's "single forward pass of the new method takes five
  thousandths of a second. The traditional solver takes two point two seconds. Three
  orders of magnitude" is verbatim — 0.005s vs 2.2s is a 440x ratio, which the paper
  itself rounds up as "three orders of magnitude."
---
index: 15
date: '2026-05-24'
status: matched
request: The Fourier neural operator works in Fourier space, where convolution becomes
  multiplication, by parameterizing the integral kernel directly in Fourier space.
excerpt: |-
  In this work, we formulate a new neural operator by parameterizing
  the integral kernel directly in Fourier space, allowing for an expressive and effi-
  cient architecture.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Abstract paragraph.
comments: SUPPORTS. The narrative's central trick — "the expensive blending step turns
  out to be wildly cheaper in the wave picture. You just multiply each wave by its
  own learned weight, one at a time" — is a faithful conversational paraphrase of
  "parameterizing the integral kernel directly in Fourier space."
---
index: 16
date: '2026-05-24'
status: matched
request: Choosing kmax_j = 12 modes per direction was sufficient for all tasks considered.
excerpt: |-
  In practice, we have found that choosing kmax,j = 12 which
  yields kmax = 12d parameters per channel to be sufficient for all the tasks that we consider.
location:
  page_pdf: 6
  page_printed: 6
  section: 4 Fourier Neural Operator
  surrounding_context: Implementation paragraph describing parameter choices.
comments: SUPPORTS. The narrative's "you keep only the first dozen or so — they found
  that twelve modes per direction was enough for everything they tried" is a verbatim
  match.
---
index: 17
date: '2026-05-24'
status: matched
request: The Fourier layers are discretization-invariant because they can learn from
  and evaluate functions discretized in arbitrary ways, since parameters are learned
  directly in Fourier space.
excerpt: |-
  The Fourier layers are discretization-invariant because they can
  learn from and evaluate functions which are discretized in an arbitrary way. Since parameters are
  learned directly in Fourier space, resolving the functions in physical space simply amounts to pro-
  jecting on the basis e2πihx,ki which are well-defined everywhere on Rd .
location:
  page_pdf: 6
  page_printed: 6
  section: 4 Fourier Neural Operator (Invariance to discretization)
  surrounding_context: Subsection on discretization invariance.
comments: SUPPORTS. The narrative's "the dozen waves you care about look the same
  whether you sampled them on a coarse grid or a fine grid. They're features of the
  underlying continuous function, not of the grid you measured it on" is exactly this
  idea, paraphrased.
---
index: 18
date: '2026-05-24'
status: matched
request: FNO trained on 64x64x20 resolution was successfully evaluated on 256x256x80
  resolution for zero-shot super-resolution.
excerpt: |-
  Figure 1
  shows an example where we train the FNO-3D model on 64 × 64 × 20 resolution data in the setting
  above with (ν = 1e−4, N = 10000) and transfer to 256 × 256 × 80 resolution, demonstrating
  super-resolution in space-time.
location:
  page_pdf: 9
  page_printed: 9
  section: 5.4 Zero-shot super-resolution
  surrounding_context: First paragraph of the super-resolution subsection.
comments: SUPPORTS. The narrative's "Trained the network on a sixty-four-by-sixty-four
  spatial grid with twenty time steps. Then asked it to predict on a two hundred fifty-six
  by two hundred fifty-six grid with eighty time steps. Sixteen times finer in space,
  four times finer in time" is verbatim — 64*4=256 (spatial), 20*4=80 (temporal).
  Spatial ratio = 4 per dimension = 16 total, temporal = 4. Confirmed.
---
index: 19
date: '2026-05-24'
status: matched
request: For the Bayesian inverse problem, FNO takes 0.005s per evaluation vs. 2.2s
  for the traditional solver; 25,000 MCMC samples take 2.5 minutes with FNO vs. over
  18 hours with the solver.
excerpt: |-
  In sharp contrast, FNO takes 0.005s to evaluate a single instance while the traditional solver, after
  being optimized to use the largest possible internal time-step which does not lead to blow-up, takes
  2.2s. This amounts to 2.5 minutes for the MCMC using FNO and over 18 hours for the traditional
  solver.
location:
  page_pdf: 9
  page_printed: 9
  section: 5.5 Bayesian Inverse Problem
  surrounding_context: Results paragraph of the MCMC experiment.
comments: SUPPORTS. The narrative's "With the traditional solver, that takes eighteen
  hours. With the new method as the forward engine, two and a half minutes" is verbatim
  from this passage.
---
index: 20
date: '2026-05-24'
status: matched
request: The Bayesian inverse problem generated 25,000 samples from the posterior
  with a 5,000 sample burn-in, requiring 30,000 evaluations of the forward operator.
excerpt: |-
  We generate 25,000 samples from the posterior (with a 5,000 sample burn-in period), requiring
  30,000 evaluations of the forward operator.
location:
  page_pdf: 9
  page_printed: 9
  section: 5.5 Bayesian Inverse Problem
  surrounding_context: Setup paragraph of the MCMC experiment.
comments: SUPPORTS. The narrative's "you have to run the forward physics tens of thousands
  of times — twenty-five thousand times in this case" is verbatim from this passage.
---
index: 21
date: '2026-05-24'
status: matched
request: To learn the Navier-Stokes equation with viscosity 1e-4, the team needed
  N=10000 training pairs generated by a numerical solver.
excerpt: |-
  To learn
  Navier-Stokes equation with viscosity ν = 1e−4, we need to generate N = 10000 training pairs
  {aj , uj } with the numerical solver. However, for more challenging PDEs, generating a few training
  samples can be already very expensive. A future direction is to combine neural operators with
  numerical solvers to levitate the requirements on data.
location:
  page_pdf: 9
  page_printed: 9
  section: 6 Discussion and Conclusion (Requirements on Data)
  surrounding_context: First paragraph of conclusion.
comments: SUPPORTS. The narrative's caveat "To learn the hardest turbulent regime,
  they needed ten thousand training pairs, each generated by a slow traditional solver.
  There's a real upfront cost" is verbatim from this passage.
---
index: 22
date: '2026-05-24'
status: matched
request: The base FNO requires a uniform discretization in order to use the Fast Fourier
  Transform.
excerpt: |-
  Generally, we have found using FFTs to be very efficient. However a uniform
  discretization is required.
location:
  page_pdf: 6
  page_printed: 6
  section: 4 Fourier Neural Operator (Quasi-linear complexity)
  surrounding_context: Subsection on computational complexity.
comments: SUPPORTS. The narrative's caveat "The base version requires the grid to
  be uniform — irregular meshes around weird-shaped wings need adaptation that isn't
  in this paper" is verbatim from this passage.
---
index: 23
date: '2026-05-24'
status: matched
request: FNO handles non-periodic boundary conditions through the local linear transform
  W (the bias term), unlike traditional Fourier methods which require periodic boundaries.
excerpt: |-
  Non-periodic boundary condition. Traditional Fourier methods work only with periodic bound-
  ary conditions. However, the Fourier neural operator does not have this limitation. This is due to the
  linear transform W (the bias term) which keeps the track of non-periodic boundary. As an example,
  the Darcy Flow and the time domain of Navier-Stokes have non-periodic boundary conditions, and
  the Fourier neural operator still learns the solution operator with excellent accuracy.
location:
  page_pdf: 9
  page_printed: 9
  section: 5.5 Bayesian Inverse Problem (Non-periodic boundary condition subsection)
  surrounding_context: Discussion of architecture flexibility.
comments: SUPPORTS. The narrative's "with a small per-point tweak alongside each one
  to handle stuff the smooth wave picture misses, like sharp boundaries" is a conversational
  paraphrase of this local-linear-transform-W passage.
---
index: 24
date: '2026-05-24'
status: matched
request: When learning the mapping for the entire time series, FNO achieves less than
  1% error at viscosity 1e-3 and 8% error at viscosity 1e-4.
excerpt: |-
  When learning the mapping for the entire time series, the method achieves < 1%
  error with viscosity ν = 1e−3 and 8% error with viscosity ν = 1e−4.
location:
  page_pdf: 3
  page_printed: 3
  section: 1 Introduction (Our Contributions)
  surrounding_context: Third bullet of the Our Contributions list, continued.
comments: SUPPORTS. The narrative's "At the easiest level — gentle, barely turbulent
  — the method gets a hair under one percent error. At the chaos-on-the-edge level
  — full turbulence — it gets about eight percent error" is verbatim from this passage.
  (1e-3 is the easier/less-turbulent regime, 1e-4 is the harder/more-turbulent regime).
---
index: 25
date: '2026-05-24'
status: matched
request: FNO operates on Fourier (spectral) modes by truncating higher modes, which
  corresponds to filtering out high-frequency components and keeping only the lower
  modes.
excerpt: |-
  On top: apply
    the Fourier transform F; a linear transform R on the lower Fourier modes and filters out the higher modes;
         then apply the inverse Fourier transform F −1 .
location:
  page_pdf: 4
  page_printed: 4
  section: Figure 2 caption (Fourier layer architecture)
  surrounding_context: Caption of Figure 2 describing the Fourier layer.
comments: SUPPORTS. The narrative's "throw away the highest-frequency waves entirely.
  You keep only the first dozen or so" matches the paper's "linear transform R on
  the lower Fourier modes and filters out the higher modes" verbatim in spirit.
---
index: 26
date: '2026-05-24'
status: matched
request: FNO is the only model among the benchmarks (FNO-2D, U-Net, TF-Net, ResNet)
  that can do zero-shot super-resolution, and it works in both spatial and temporal
  domains.
excerpt: |-
  Fourier neural operator is the only model among the benchmarks
  (FNO-2D, U-Net, TF-Net, and ResNet) that can do zero-shot super-resolution. And surprisingly, it
  can do super-resolution not only in the spatial domain but also in the temporal domain.
location:
  page_pdf: 9
  page_printed: 9
  section: 5.4 Zero-shot super-resolution
  surrounding_context: Second paragraph of the super-resolution subsection.
comments: SUPPORTS. The narrative's "None of the other methods can do this at all
  — they're nailed to whatever grid they were trained on. This one is grid-agnostic
  by design" is verbatim aligned with this passage.
