# Section 2 — Proof of Theorem 0.7

## What this section does

Closes the loop. Section 1 built the exponentially growing solutions (CGOs). Section 2 takes those solutions, plugs them into the integral identity from Proposition 0.9, takes the high-frequency limit, extracts a pair of strictly hyperbolic PDEs in the differences (lambda_1 - lambda_2) and (mu_1 - mu_2), and finishes the theorem using Cauchy uniqueness for hyperbolic operators starting from the boundary.

## The set-up: a clever complex frequency

The proof works wavevector-by-wavevector. Fix a real wavevector k in R^n (this is the spatial frequency the proof is going to extract information about). Pick two real unit vectors gamma_1 and gamma_2 in R^n that are mutually orthogonal AND both orthogonal to k. (You need n >= 3 to find such gamma_1, gamma_2 — this is where the dimension hypothesis enters.)

Now build a complex direction
`theta = gamma_1 + i gamma_2`
which automatically satisfies theta dot theta = 0, and let zeta(r, k) be a complex frequency that grows in r, picks up the wavevector k, and twists with theta:
`zeta(r, k) = r theta + g(r, k) i k` for a specific choice of g(r, k).

The two CGO solutions u^(1) and u^(2) the authors plug in are built from this zeta in a paired way (equations 2.1, 2.2): zeta^(1) puts +ik/2 on the imaginary side, zeta^(2) puts -ik/2. The sum zeta^(1) + zeta^(2) equals ik. This pairing is what makes the wavevector k come out cleanly in the resulting integral.

## The two cases

The amplitudes carried by the CGOs are matrix-valued, and the matrix has block structure. The authors split into two cases depending on which block they pull the amplitude from:

**Case 1.** Amplitudes drawn from the first block. After substituting the CGOs into the integral identity and taking the limit r -> infinity, formula (2.13) emerges:

`integral over Omega of exp(i x . k) { J(x, x^(0), theta, theta . del)(lambda_1 - lambda_2) + K'(x, x^(0), theta)(mu_1 - mu_2) } dx = 0`

and a companion identity (2.13') with the roles slightly swapped. Here J, K' are polynomials in theta (degree 2) and in theta . del (degree 2). Crucially, J and K' satisfy

`limit as r -> infinity of r^{-2} J(x^(0), x^(0), theta, r) = -4 mu^2 |_{x=x^(0)}`

so as you scale up, the dependence on theta drops out and you get an honest equation in (lambda_1 - lambda_2) and (mu_1 - mu_2) alone (locally at x^(0)).

**Case 2.** Amplitudes drawn from the second block, producing equation (2.16):

`integral over Omega of exp(i x . k) { g(x, x^(0), theta)(lambda_1 - lambda_2) + h(x, x^(0), theta)(mu_1 - mu_2) } dx = 0`

with g(x^(0), x^(0), theta) = h(x^(0), x^(0), theta) = 2 mu_1 mu_2 |_{x=x^(0)}, independent of theta.

## Removing the complex direction

The integrands phi_1, phi_2, phi_3 of these identities depend on the complex direction theta = gamma_1 + i gamma_2. The next step uses an integral-geometry lemma (Lemma 2.18, from Helgason) to show that because these integrals vanish for all admissible theta, the integrands themselves must vanish:

`Delta phi_i (x, x^(0), theta) = 0   (i = 1, 2, 3)`

for all x in Omega and all admissible theta. This is equation (2.19).

The hypothesis of Helgason's lemma is satisfied because Theorem 0.8 (boundary determination, proved in the prior paper [N-U-I]) tells us that (lambda_1 - lambda_2) and (mu_1 - mu_2) are FLAT on the boundary — they vanish to all orders there — so the integrand phi_i has support in Omega. The integrals are then integrals over hyperplanes that intersect Omega, and the lemma applies.

## Extracting the hyperbolic PDEs

Specialize: fix a coordinate index j with 1 <= j <= n, and choose the pair (gamma_1, gamma_2) to be (e_l, e_l') (the l-th and l'-th standard basis vectors, with l, l' both different from j). For each such choice you get one equation; summing the REAL PARTS over admissible l yields

`{ (n - 1) partial^2 over partial x_j squared - (Delta - partial^2 over partial x_j squared) }(lambda_1 - lambda_2) + c_{2j}(x) S_{j,2}^h(x, partial)(lambda_1 - lambda_2) + S_{j,1}(x, partial)(mu_1 - mu_2) + l_j(x) (mu_1 - mu_2) = 0`

This is equation (2.22), which immediately implies equation (0.21) — one of the two strictly hyperbolic PDEs in the introduction. An analogous argument with Case 2 implies (0.20).

The key structural fact: the operator inside the curly braces, `(n - 1) partial^2/partial x_j^2 - (Delta - partial^2/partial x_j^2)`, is strictly hyperbolic with respect to the time variable x_j (when restricted to a small enough ball around any point x^(0)). That hyperbolicity is what makes the next step work.

## Closing the proof with Cauchy uniqueness

So now we have a pair of strictly hyperbolic PDEs (equations (0.20) and (0.21)) in the differences (lambda_1 - lambda_2) and (mu_1 - mu_2), with x_j as time, valid in a ball Omega(R) around any x^(0) in Omega.

Boundary determination (Theorem 0.8) says: (lambda_1 - lambda_2) and (mu_1 - mu_2) are flat on the boundary of Omega. So in any neighborhood of the boundary, all their derivatives vanish — they have zero Cauchy data.

Apply Cauchy uniqueness for strictly hyperbolic operators (a classical PDE theorem): zero Cauchy data plus a hyperbolic equation means the solution is identically zero in the domain of dependence. Start from a neighborhood of the boundary, where you know the differences are zero. The hyperbolic uniqueness propagates the zero inward, layer by layer. By covering Omega with such balls you get

`lambda_1 - lambda_2 = 0 and mu_1 - mu_2 = 0 everywhere in Omega.`

Which is exactly Theorem 0.7. The end.

## Why the logic works

Three things are doing the work, and the listener should track them separately:

1. **The CGOs (built in section 1)** are the "test functions" — special solutions of the elasticity equation that probe the system at any chosen spatial frequency k.
2. **The integral identity (Proposition 0.9, from the prior companion paper)** is the channel — it converts "two media have the same DN map" into a statement that an integral involving (lambda_1 - lambda_2, mu_1 - mu_2) and any pair of valid solutions vanishes.
3. **The hyperbolic Cauchy uniqueness** is the propagator — it carries information from the boundary (where you already know the differences vanish, by Theorem 0.8) inward to the interior.

The CGOs and the integral identity together extract a hyperbolic PDE for the unknown differences; the boundary determination gives the boundary condition; Cauchy uniqueness propagates the zero across the whole domain.

## Load-bearing verbatim hooks

- "Recalling that lambda_1 - lambda_2, mu_1 - mu_2 are flat on partial Omega we can apply uniqueness of the Cauchy problem for strictly hyperbolic operators repeatedly starting from a neighborhood of partial Omega to conclude that mu_1 - mu_2 = lambda_1 - lambda_2 = 0 in Omega."
- "The continuity of solutions of ODE with respect to parameters and initial data imply that there exists a radius R > 0 such that the equations (0.20) and (0.21) are strictly hyperbolic with respect to the time variable x_j in Omega intersect {x ; |x - x^(0)| <= R} for any x^(0) in Omega. Therefore the aforementioned argument in section 0 implies that lambda_1 - lambda_2 = mu_1 - mu_2 in Omega."

## Podcast hook for this section

This is where the abstract machinery cashes out. The listener doesn't need the case analysis or the explicit polynomials. What they need to hear is the rhythm of the closing argument: special solutions, plug them in, take a limit, get an equation in the unknown differences; that equation is hyperbolic (think wave equation), and you happen to know the differences are zero at the boundary, so the wave equation propagates "zero" inward and fills the entire object. Same DN map -> same interior. Quod erat demonstrandum.
