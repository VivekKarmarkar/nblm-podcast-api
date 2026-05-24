journal_metadata:
  paper: 10.1007_bf01231541
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: Authors are Gen Nakamura (University of Tokyo) and Gunther Uhlmann (University
  of Washington), 1994, published in Inventiones Mathematicae 118.
excerpt: |-
  Invent. math. 118, 457 474 (1994)
  Inventiones mathematicae
  Springer-Verlag 1994

  Global uniqueness for an inverse boundary problem arising in elasticity
  Gen Nakamura, Gunther Uhlmann
  Department of Mathematic Science, University of Tokyo, Tokyo, 162, Japan
  Department of Mathematics, University of Washington, Seattle, WA 98195, USA
location:
  page_pdf: 1
  page_printed: 457
  section: Title page / front matter
  surrounding_context: Title page header with journal citation, paper title, authors,
    affiliations.
comments: SUPPORTS. Confirms both author names, both affiliations, the journal (Inventiones
  Mathematicae), volume (118), pages (457-474), and year (1994). Verbatim from page
  1 of the PDF.
---
index: 2
date: '2026-05-24'
status: matched
request: The paper proves uniqueness/determination of Lame parameters of an elastic,
  isotropic, inhomogeneous medium from boundary measurements in dimensions n >= 3.
excerpt: Summary. We prove that we can determine the Lame parameters of an elastic,
  isotropic, inhomogeneous medium in dimensions n > 3, by making measurements of the
  displacements and corresponding stresses at the boundary of the medium.
location:
  page_pdf: 1
  page_printed: 457
  section: Summary
  surrounding_context: Abstract / Summary at top of paper.
comments: 'SUPPORTS. Verbatim summary. Note: OCR rendered ''>='' as ''>''; the formal
  Theorem 0.7 on page 2 makes it explicit that n >= 3. Confirms (a) elastic, isotropic,
  inhomogeneous medium, (b) determination from boundary displacement-stress measurements,
  (c) the dimension restriction.'
---
index: 3
date: '2026-05-24'
status: matched
request: The boundary measurement operator that takes surface displacement to surface
  stress is called the Dirichlet-to-Neumann (DN) map.
excerpt: |-
  The Dirichlet to Neumann map (DN) is defined by
  ...
  where v = (v_1, ..., v_n) is the outer unit normal vector field of partial Omega and u is the solution to (0.2). Physically the DN map sends the displacement at the boundary to the corresponding normal component of the stress at the boundary.
location:
  page_pdf: 2
  page_printed: 458
  section: 0. Introduction and statement of the results
  surrounding_context: Definition of the Dirichlet-to-Neumann map after the elasticity
    boundary value problem is stated.
comments: SUPPORTS. Verbatim definition of DN map as 'sends the displacement at the
  boundary to the corresponding normal component of the stress at the boundary.' Confirms
  the boundary-measurement framing in the narrative.
---
index: 4
date: '2026-05-24'
status: matched
request: 'Main theorem (Theorem 0.7): if two pairs of Lame parameters produce the
  same Dirichlet-to-Neumann map, they must be equal everywhere in Omega; this requires
  dimension n >= 3.'
excerpt: |-
  In this paper we prove the following identifiability result: The DN map determines lambda, mu in dimensions n >= 3.
  (0.7) Theorem. Let n >= 3 and (lambda_i, mu_i) ... satisfying the strong convexity condition (0.1). Assume A_1 = A_2 with A_i = Lambda_(lambda_i,mu_i) (i=1,2). Then (lambda_1, mu_1) = (lambda_2, mu_2) in Omega.
location:
  page_pdf: 2
  page_printed: 458
  section: Theorem 0.7
  surrounding_context: The main result, stated formally.
comments: SUPPORTS. The formal main theorem. Same DN map (A_1 = A_2) implies same
  Lame parameter pair throughout Omega. Confirms 'global uniqueness' framing and 'n
  >= 3' dimension requirement.
---
index: 5
date: '2026-05-24'
status: matched
request: Boundary determination (Theorem 0.8) was proved by the same authors in an
  earlier paper [N-U-I] and shows that the DN map determines Lame parameters AND all
  their derivatives on the boundary.
excerpt: |-
  We have already proven in ([N-U-I]) the boundary determination of the Lame parameters from the DN map.
  (0.8) Theorem. Let n >= 2 and (lambda_i, mu_i) in C-infinity x C-infinity satisfying the strong convexity condition (0.1). Assume A_1 = A_2. Then [partial^alpha lambda_1 = partial^alpha lambda_2 and partial^alpha mu_1 = partial^alpha mu_2 on partial Omega] for any alpha in (N union {0})^n = Z_+^n.
location:
  page_pdf: 2
  page_printed: 458
  section: Theorem 0.8
  surrounding_context: Quoted prior result giving boundary determination including
    all derivatives.
comments: SUPPORTS. The narrative's claim that boundary determination (lambda and
  mu and all their derivatives agreeing at the boundary) was already known is explicitly
  attributed to [N-U-I] here. The 'for any alpha' quantifier gives derivatives of
  all orders.
---
index: 6
date: '2026-05-24'
status: matched
request: An integral identity (Proposition 0.9) connects equality of DN maps to a
  vanishing integral over Omega involving (lambda_1 - lambda_2), (mu_1 - mu_2), and
  the divergences/strains of solutions u^(1), u^(2).
excerpt: |-
  (0.9) Proposition. ([N-UII]) Let (lambda_i, mu_i) (i=1,2) be as in Theorem 0.7. Then
  E(u_1, u_2) = integral_Omega { (lambda_1 - lambda_2) div u^(1) . div u^(2) + 2(mu_1 - mu_2)(epsilon(u^(1)) . epsilon(u^(2))) } dx = 0
  (0.10)
  where L_j u^(j) = 0 in Omega (j=1,2) with L_j = L(lambda_j, mu_j) as in (0.2) and the dots are real inner products...
location:
  page_pdf: 3
  page_printed: 459
  section: Proposition 0.9
  surrounding_context: Integral identity stated as a quoted prior result, plays the
    role of the bilinear-form that links DN-map equality to interior information.
comments: SUPPORTS. Confirms the existence and form of the integral identity (eq 0.10)
  involving (lambda_1 - lambda_2), (mu_1 - mu_2), divergence of solutions, and strain
  inner products. Identity attributed to prior work [N-UII], consistent with narrative's
  'identity that's been around since the authors' earlier work.'
---
index: 7
date: '2026-05-24'
status: matched
request: The elasticity operator does NOT reduce to a Schrodinger operator (Laplacian
  + matrix potential) by a simple change of variables, unlike the conductivity equation.
  This is the obstruction that requires the new diagonalization technique.
excerpt: The main problem is then to find "enough" solutions of (0.2) to give information
  on the Lame parameters by substituting them to (0.10). The difficulty in doing this
  is that the second order elasticity operator cannot be reduced to a Schrodinger
  type operator (Delta + "matrix potential") as is in the case of the conductivity
  equation by a simple change of the dependent variables ([S-U]). In this paper we
  fully diagonalize the elasticity operator as we explain below.
location:
  page_pdf: 3
  page_printed: 459
  section: 0. Introduction and statement of the results
  surrounding_context: Authors' explanation of why the conductivity-style approach
    fails and what they do instead.
comments: SUPPORTS. Verbatim. Confirms the narrative's claim that the elasticity case
  is harder than the conductivity case because the Schrodinger reduction doesn't apply,
  and that full diagonalization is the substitute.
---
index: 8
date: '2026-05-24'
status: matched
request: 'The new technical ingredient is a complete diagonalization of a first-order
  pseudodifferential system N_zeta derived from the elasticity operator: there exist
  operators A_zeta, B_zeta in L^0 with N_zeta A_zeta = B_zeta mod L^{-N}.'
excerpt: |-
  The main point is that one can completely diagonalize N_zeta, namely there exist A_zeta, B_zeta in L^0 such that
  N_zeta A_zeta = B_zeta mod L^{-N}(R^n, Z)
  (0.19)
  with N large enough. This is the new ingredient in our approach. Moreover A_zeta and B_zeta converge as |zeta| -> infty, in an appropriate topology, to a matrix multiplication operator G_zeta which can be computed explicitly...
location:
  page_pdf: 4
  page_printed: 460
  section: 0. Introduction and statement of the results
  surrounding_context: 'End of the proof sketch: announces the diagonalization-modulo-smoothing
    as the new contribution.'
comments: SUPPORTS. Verbatim 'This is the new ingredient in our approach.' Confirms
  the narrative's claim that complete diagonalization (modulo smoothing) of the first-order
  system is the technical headline.
---
index: 9
date: '2026-05-24'
status: matched
request: The conductivity-equation inverse problem (Calderon problem) was solved by
  Sylvester and Uhlmann ([S-U]) using exponentially growing solutions (CGOs).
excerpt: Since the work [S-U] the construction of growing exponential solutions for
  operators that can be reduced to first order differential or pseudodifferential
  perturbations of the Laplacian has played a crucial role in identifiability results
  ([C-P], [I], [Is], [O-P-S], [Su], [Su-U]). In this paper we construct these solutions
  for any differential operator or system that can be reduced to a first order differential
  or pseudodifferential perturbation of the Laplacian.
location:
  page_pdf: 4
  page_printed: 460
  section: 0. Introduction and statement of the results
  surrounding_context: Acknowledgment of the [S-U] (Sylvester-Uhlmann) lineage of
    growing exponential solutions and the paper's extension of that technique.
comments: SUPPORTS. Confirms (a) the Sylvester-Uhlmann CGO lineage from the conductivity
  problem, (b) that growing exponential solutions are the load-bearing technique in
  this whole family of identifiability results, (c) the paper extends them to operators
  reducible to first-order perturbations of the Laplacian (which now includes elasticity,
  after the diagonalization).
---
index: 10
date: '2026-05-24'
status: matched
request: The last step of the proof reduces the problem to two strictly hyperbolic
  equations (0.20) and (0.21) in (mu_1 - mu_2) and (lambda_1 - lambda_2) respectively,
  with time variable x_j.
excerpt: |-
  In section 2 we show that there exists R > 0 such that for any x^(0) in Omega, lambda_1 - lambda_2, mu_1 - mu_2 satisfy the following strictly hyperbolic equations with respect to the time variable x_j in Omega(R) = {x in Omega; |x - x^(0)| < R}
  {(n - 1) partial_x_j^2 - (Delta - partial_x_j^2)}(mu_1 - mu_2) + c_{ij}(x) R_{j,2}^h(x, partial)(mu_1 - mu_2) + R_{j,1}(x, partial)(mu_1 - mu_2) = 0,
  (0.20)
  {(n - 1) partial_x_j^2 - (Delta - partial_x_j^2)}(lambda_1 - lambda_2) + c_{2j}(x) S_{j,2}^h(x, partial)(lambda_1 - lambda_2) + S_{j,1}(x, partial)(lambda_1 - lambda_2) = 0
  (0.21)
location:
  page_pdf: 4
  page_printed: 460
  section: 0. Introduction and statement of the results
  surrounding_context: Outlined final step of the proof.
comments: SUPPORTS. Verbatim statement of the pair of strictly hyperbolic PDEs (0.20)-(0.21)
  in the differences. Confirms the narrative's 'wave equation' / 'strictly hyperbolic
  equation' framing.
---
index: 11
date: '2026-05-24'
status: matched
request: Cauchy uniqueness for strictly hyperbolic operators, plus boundary flatness
  of (lambda_1 - lambda_2) and (mu_1 - mu_2), forces them to vanish throughout Omega.
excerpt: Moreover c_{ij} in C-infinity(Omega(R)) with c_{ij}(x^(0)) = 0. Recalling
  that lambda_1 - lambda_2, mu_1 - mu_2 are flat on partial Omega we can apply uniqueness
  of the Cauchy problem for strictly hyperbolic operators repeatedly starting from
  a neighborhood of partial Omega to conclude that mu_1 - mu_2 = lambda_1 - lambda_2
  = 0 in Omega.
location:
  page_pdf: 4
  page_printed: 460
  section: 0. Introduction and statement of the results
  surrounding_context: Final closing argument of the introduction's proof sketch.
comments: SUPPORTS. Verbatim. Confirms (a) the differences are flat on the boundary
  (boundary determination), (b) Cauchy uniqueness for strictly hyperbolic operators
  is applied repeatedly starting from neighborhood of the boundary, (c) the conclusion
  is that the differences vanish in all of Omega. Exactly the narrative's 'wave equation
  propagates silence inward' picture.
---
index: 12
date: '2026-05-24'
status: matched
request: The freedom to choose the complex frequency zeta in the CGOs is what allows
  the proof to access information about a Fourier-type transform of the differences
  lambda_1-lambda_2 and mu_1-mu_2.
excerpt: Roughly speaking we use the freedom to choose the complex frequencies of
  the exponentially growing solutions constructed in section 1 to get information
  about the Fourier transform of a differential operator applied to lambda_1 - lambda_2
  and mu_1 - mu_2.
location:
  page_pdf: 5
  page_printed: 461
  section: 0. Introduction and statement of the results
  surrounding_context: Authors' English-prose summary of the role of varying the complex
    frequency.
comments: 'SUPPORTS. Verbatim. Confirms the narrative''s account: varying the complex
  frequency probes different spatial scales of the difference between the two materials.'
---
index: 13
date: '2026-05-24'
status: matched
request: The fourth-order operator M produced by the substitution has principal part
  Delta^2 with the third-order part factored out by Delta, and this factoring is crucial.
excerpt: |-
  We first construct a differential system P of order 2 (diagonal in the principal part) so that
  M = (mu(lambda + 2 mu))^{-1} L P = Delta^2 + M^(1)(x, D) Delta + M^(2)(x, D)
  (0.11)
  where M^(j)(x, D) is a differential system of order j (j = 1, 2). We note that the third order part is factored out by Delta. This is crucial in our arguments.
location:
  page_pdf: 3
  page_printed: 459
  section: 0. Introduction and statement of the results
  surrounding_context: Construction of the operator P and the resulting M, which set
    up the rest of the diagonalization machinery.
comments: SUPPORTS. Verbatim. Confirms the structural setup that the narrative compresses
  into the metaphor of 'taking the elasticity system apart and putting it back together
  in a much simpler form.'
---
index: 14
date: '2026-05-24'
status: matched
request: The CGO ansatz involves an exponential of x dot zeta, where zeta is a nonzero
  complex vector with zeta dot zeta = 0.
excerpt: |-
  Let 0 != zeta in C^n with zeta . zeta = 0. We shall look for solutions of M u = 0 of the form
  u = e^{x . zeta} v
  (0.12)
  For this it is natural to consider the conjugation of all the operators involved with e^{x . zeta} ...
location:
  page_pdf: 3
  page_printed: 459
  section: 0. Introduction and statement of the results
  surrounding_context: Introduction of the exponentially growing solution ansatz.
comments: SUPPORTS. Verbatim. Confirms the form of the CGO solutions used in the proof
  (exponential of x . zeta with zeta dot zeta = 0 in C^n). Matches the narrative's
  'special solution that grows exponentially as you move through space in a chosen
  complex direction.'
---
index: 15
date: '2026-05-24'
status: matched
request: The dimension restriction n >= 3 enters because the proof requires choosing
  two unit vectors gamma_1, gamma_2 that are mutually orthogonal AND both orthogonal
  to a chosen real wavevector k.
excerpt: |-
  For given k in R^n let gamma_1, gamma_2 in R^n be unit vectors such that k, gamma_1, gamma_2 are orthogonal. We set
  theta = gamma_1 + i gamma_2, ...
location:
  page_pdf: 13
  page_printed: 469
  section: 2. Proof of Theorem 0.7
  surrounding_context: 'Opening of Section 2: choice of the complex direction theta
    = gamma_1 + i gamma_2 used in the CGO construction.'
comments: SUPPORTS. Verbatim. Confirms the narrative's claim that the proof requires
  picking two perpendicular real directions BOTH perpendicular to the wavevector —
  and that this needs the ambient space to be at least 3D (you can fit k, gamma_1,
  gamma_2 mutually orthogonal only if n >= 3).
---
index: 16
date: '2026-05-24'
status: matched
request: An integral-geometry lemma (Helgason) is used to pass from 'the integrals
  over hyperplanes vanish for every direction' to 'the integrand itself vanishes.'
excerpt: |-
  Now let us recall the following result in integral geometry.
  (2.18) Lemma. ([H] Chapter I, Lemma 2.11) Let omega^(0) in R^n be a fixed unit vector and N is a neighborhood of omega^(0) in S^{n-1} subset R^n. Let phi(x) in C-infinity(R^n) satisfy
  integral phi(x) dH_s = 0 (omega in N, s > s_0)
  [over the hyperplane x . omega = s]
  then phi(x) = 0 in the half-space x . omega^(0) > s_0.
location:
  page_pdf: 16
  page_printed: 472
  section: 2. Proof of Theorem 0.7
  surrounding_context: Quoted lemma from Helgason that converts the vanishing-over-hyperplanes
    condition into pointwise vanishing.
comments: SUPPORTS. Verbatim. Confirms the narrative's account of the role of Helgason's
  integral-geometry lemma in the middle of Section 2.
---
index: 17
date: '2026-05-24'
status: matched
request: 'The final concluding argument: the hyperbolic equations (0.20) and (0.21)
  hold in a ball around any x^(0), and Cauchy uniqueness forces lambda_1 - lambda_2
  = mu_1 - mu_2 in Omega.'
excerpt: Finally we note that the continuity of solutions of ODE with respect to parameters
  and initial data imply that there exists a radius R > 0 such that the equations
  (0.20) and (0.21) are strictly hyperbolic with respect to the time variable x_j
  in Omega intersect {x; |x - x^(0)| <= R} for any x^(0) in Omega. Therefore the aforementioned
  argument in section 0 implies that lambda_1 - lambda_2 = mu_1 - mu_2 in Omega.
location:
  page_pdf: 16
  page_printed: 472
  section: 2. Proof of Theorem 0.7 (last paragraph)
  surrounding_context: The closing lines of Section 2 — final assembly of the uniqueness
    conclusion.
comments: 'SUPPORTS. Verbatim. Confirms the conclusion of the proof: lambda_1 - lambda_2
  = mu_1 - mu_2 = 0 in all of Omega, by applying the hyperbolic-uniqueness argument
  from Section 0. This is the formal closing the narrative''s ''difference is zero,
  materials are the same'' delivers as the punchline.'
---
index: 18
date: '2026-05-24'
status: matched
request: The strong convexity condition (0.1) requires mu > 0 and n*lambda + 2*mu
  > 0 in Omega.
excerpt: |-
  Let lambda, mu in C-infinity(Omega) satisfy the strong convexity condition
  mu > 0, n*lambda + 2*mu > 0 in Omega
  (0.1)
  The domain Omega is considered here as an elastic, isotropic, inhomogeneous medium with Lame parameters lambda, mu.
location:
  page_pdf: 1
  page_printed: 457
  section: 0. Introduction and statement of the results
  surrounding_context: Setup of the elastic medium and the basic positivity / convexity
    assumption on the Lame parameters.
comments: SUPPORTS. Verbatim setup. Confirms that the paper's framework is an elastic,
  isotropic, inhomogeneous medium with positive Lame parameters (per the strong convexity
  condition). Underlies the narrative's 'recipe for the material' framing.
---
index: 19
date: '2026-05-24'
status: matched
request: Pseudodifferential calculus / Shubin class L^m(R^n, Z) is the framework used
  to make sense of the operators depending on the complex parameter zeta.
excerpt: where A_zeta is the properly supported pseudodifferential operator with principal
  symbol |zeta/|zeta||^2 + |xi|^2. Here the dots represent functions to which the
  operators are applied. We note that A_zeta is a pseudodifferential operator depending
  on the complex parameter zeta in the Shubin class ([S, section 9]) with lambda replaced
  by zeta.
location:
  page_pdf: 3
  page_printed: 459
  section: 0. Introduction and statement of the results
  surrounding_context: Definition of the conjugated Laplacian operator A_zeta in the
    Shubin pseudodifferential class.
comments: SUPPORTS. Verbatim. Confirms the narrative's claim that the technical machinery
  is pseudodifferential calculus (Shubin class L^m). The 'fairly heavy machinery from
  a field called pseudodifferential calculus' phrase in the narrative is accurate.
---
index: 20
date: '2026-05-24'
status: matched
request: The CGO solutions for the original elasticity operator have the form u^(j)
  = P_j(x, D)(e^{x . zeta^(j)} w^(j)) approximating L_j u^(j) = 0 for large |zeta|.
excerpt: |-
  Then according to Theorem (1.23) and Lemma (1.25),
  u^(j) = P_j(x, D)(e^{x . zeta^(j)} w^(j))
  (2.8)
  with P_j(x, D) given by (1.2) approximate solutions of L_j u_j = 0 (j = 1, 2) for large |zeta^(j)|.
location:
  page_pdf: 13
  page_printed: 469
  section: 2. Proof of Theorem 0.7
  surrounding_context: The CGO solutions plugged into the proof in Section 2.
comments: SUPPORTS. Verbatim form of the CGO solutions used in the proof. Matches
  the narrative's picture of building special solutions and substituting them.
