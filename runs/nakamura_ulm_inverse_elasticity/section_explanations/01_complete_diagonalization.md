# Section 1 — Complete diagonalization

## What this section does

This is the technical heart of the paper. The previous section explained WHY diagonalizing the elasticity operator matters; this section actually DOES it. The output of this section is a family of "exponentially growing solutions" (CGOs) to the elasticity system — solutions of a very particular shape that section 2 will substitute into the integral identity to crack the uniqueness theorem.

## The starting puzzle

The elasticity operator L, applied to a displacement vector u, is a second-order linear differential SYSTEM. (System because u has n components and so does Lu.) Written out it looks like the divergence of the stress tensor, with the stress tensor depending linearly on the strain tensor, which depends linearly on the gradient of u. The coefficients are built from the Lame parameters lambda and mu.

If L were a single scalar equation — say, the Laplacian Delta — there's a classical recipe for building exponentially growing solutions: try u(x) = exp(x dot zeta) for a complex vector zeta with zeta dot zeta = 0 (an "isotropic" complex direction in C^n). For Delta this works because Delta exp(x dot zeta) = (zeta dot zeta) exp(x dot zeta) = 0.

For L (a 2nd-order system with variable coefficients) the trick fails. The principal symbol of L is not a scalar — it's a matrix that mixes the components of u. You can't just write down an exponential and have it solve the system. Worse, the off-diagonal coupling persists into the lower-order terms.

The way out, due to the authors: trade the original elasticity operator for a higher-order pseudodifferential operator whose principal part IS diagonal.

## Step 1 — Pseudodifferential factorization

The authors construct a 2nd-order matrix differential operator P (diagonal in its principal part) such that

`M := (mu(lambda + 2 mu))^{-1} L P = Delta^2 + M^(1)(x,D) Delta + M^(2)(x,D)`

where M^(j) is a differential system of order j. The principal part is Delta^2 (a scalar fourth-order operator times the identity matrix). The factor of Delta in front of the order-1 term is crucial: it means the third-order part of M is already "factored through" the Laplacian, which makes the subsequent reduction clean.

Equation (0.11) in the paper records this factorization.

## Step 2 — Conjugation and the carrier operator

For any complex frequency zeta in C^n with zeta dot zeta = 0, the authors define conjugated operators

`M_zeta = exp(-x dot zeta) M exp(x dot zeta), A_zeta = exp(-x dot zeta) Delta exp(x dot zeta)`

and rescale these to absorb the powers of |zeta|:

`A-tilde_zeta = A_zeta / A_zeta^classical, M-tilde_zeta = M_zeta A_zeta^{-2}`

The point of all this conjugation is that the conjugated operator M-tilde_zeta turns out to be a pseudodifferential system in a class L^m(R^n, Z) (Shubin's class, where Z is a complex parameter), and its principal symbol becomes a tractable matrix.

After all the conjugation and rescaling, equation (0.15) gives

`M-tilde_zeta = A-tilde_zeta^{-2} + M-tilde_zeta^(1) A-tilde_zeta + M-tilde_zeta^(0)`

with M-tilde_zeta^(1) in L^1, M-tilde_zeta^(0) in L^0. So the operator is now "small" in the limit |zeta| -> infinity: leading term scales like |zeta|^{-2}, and the lower-order terms are bounded.

## Step 3 — Reduction to a first-order system

The 2nd-order pseudodifferential system M-tilde_zeta is further reduced to a first-order system N_zeta by introducing the augmented unknown

`W = transpose(V, A-tilde_zeta V)`

(equation 0.16) where V solves M-tilde_zeta V = 0. Then W satisfies N_zeta W = 0 where

`N_zeta = A-tilde_zeta I + N_zeta^(0)`

with N_zeta^(0) a system in L^0. This is now a first-order pseudodifferential system in W, of the same shape as the systems for which the diagonalization-modulo-smoothing technique has a chance.

## Step 4 — The key result: complete diagonalization

**Theorem 1.23 (the new technical theorem).** There exist pseudodifferential operators A_zeta, B_zeta in L^0(R^n, Z) such that

`N_zeta A_zeta = B_zeta + smoothing of order -N`

with N arbitrarily large. Moreover, as |zeta| -> infinity, both A_zeta and B_zeta converge (in the appropriate topology) to a matrix multiplication operator G_omega (where omega = zeta/|zeta|) that can be computed explicitly.

In words: by composing N_zeta with a carefully chosen A_zeta you transform it into B_zeta — and B_zeta is essentially diagonal (a multiplication operator) modulo terms that vanish in the high-frequency limit. This is the FULL diagonalization referred to in the section title.

Lemma 1.25 elaborates the technical properties of A_zeta and B_zeta — boundedness on Sobolev spaces, smoothness in the parameter zeta, the formulas for the limiting matrix G_omega.

## Step 5 — Exponentially growing solutions

With the diagonalization in hand, the authors can finally write down approximate solutions to the original elasticity system L u = 0 of the form

`u = exp(x dot zeta) P(x, D) (something)`

(equation 2.8 in the next section). The "something" comes from solving a much simpler equation involving the diagonalized operator. Because the construction is exponentially growing in |zeta|, taking |zeta| -> infinity allows the authors to probe arbitrarily high spatial frequencies of the difference (lambda_1 - lambda_2, mu_1 - mu_2) when they substitute into the integral identity.

## Why this matters in plain words

The whole section is one long ladder of substitutions, each one trading the current operator for a slightly cleaner one. At the top of the ladder the operator is the original elasticity system — coupled, second-order, ugly. At the bottom of the ladder you have a multiplication operator — diagonal, zeroth-order, trivial. The miracle is that the bottom of the ladder still contains enough information about the original to recover lambda and mu.

This is analogous to what happens in the Calderon conductivity problem (Sylvester-Uhlmann 1987), but the elasticity case is genuinely harder because the original operator is a SYSTEM. The trick of factoring through Delta and then diagonalizing modulo smoothing is, as the authors say, "the new ingredient in our approach."

## Load-bearing verbatim hooks

- "In this paper we fully diagonalize the elasticity operator as we explain below."
- "We first construct a differential system P of order 2 (diagonal in the principal part) so that M = (mu(lambda+2mu))^{-1} L P = Delta^2 + M^(1)(x,D) Delta + M^(2)(x,D). We note that the third order part is factored out by Delta. This is crucial in our arguments."
- "The main point is that one can completely diagonalize N_zeta, namely there exist A_zeta, B_zeta in L^0 such that N_zeta A_zeta = B_zeta mod L^{-N}... This is the new ingredient in our approach."
- "Since the work [S-U] the construction of growing exponential solutions for operators that can be reduced to first order differential or pseudodifferential perturbations of the Laplacian has played a crucial role in identifiability results... In this paper we construct these solutions for any differential operator or system that can be reduced to a first order differential or pseudodifferential perturbation of the Laplacian."

## Podcast hook for this section

This is the deep machinery, not the headline. For a general listener the message of this section is: the proof needs special solutions — solutions that grow exponentially in a controllable way — and to build them the authors have to take the elasticity equations apart and put them back together in a much simpler form. Think of it like learning to play a single piano chord by first taking the piano apart, tuning every string in isolation, then putting it back together. Tedious but necessary, because without it you can't hit the right note.
