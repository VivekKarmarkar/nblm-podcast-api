# 04 — Background: Dispersion Relations + Assumptions

## What is a dispersion relation?
Just as sound waves decompose into simple harmonic modes, any wave can be expressed as a combination of wave modes at different spatial frequencies (γ, "wavenumber" = waves per unit length) and temporal frequencies (ω, "angular frequency"). A dispersion relation is the set of ALL the (γ, ω) pairs the medium supports — the "menu" of waves the medium can carry.

For each spatial frequency γ, the math gives you a set of allowed temporal frequencies ω. Plot all the allowed (γ, ω) pairs together → curves on a γ-ω plot. THAT plot is the dispersion relation.

## The math (high level)
- Elastic wave equation: −ω² M(u) = K(u). M = mass operator (depends on density). K = stiffness operator (depends on elastic modulus E and Poisson's ratio).
- Boundary conditions: assume the medium is a finite section but waves continue past the boundary. They apply Bloch-Floquet periodic boundary conditions.
- For each wavenumber γ in [0, π/a], solve a generalized eigenvalue problem to get (ω, u). The set of all ω solutions for every γ = the dispersion relation.

## Assumptions for tissue characterization
The paper models the medium as a soft tissue layer of uniform thickness T on top of bone. Several simplifications:
1. The soft layer has uniform stiffness E (a single number, not a spatial map).
2. Density and Poisson's ratio are KNOWN constants (ρ = 1 g/cm³, ν = 0.45).
3. Bone is much stiffer than soft tissue → modeled as motionless (doesn't matter how thick or stiff exactly).

Under these assumptions, T and E FULLY DETERMINE the dispersion relation. Two numbers in → a whole dispersion curve out. Inverse problem: given a measured dispersion relation from a video, recover T and E.

## Conversational hook
The dispersion relation is the wave equivalent of a fingerprint. Every (thickness, stiffness) pair has its own dispersion fingerprint. Different combinations of (T, E) produce different fingerprints. If you can read the fingerprint off a video, you can identify what made it.

Critically: the paper's assumption that ONLY thickness and stiffness vary (everything else is fixed at known values) is what makes the inverse problem tractable. Two unknowns, not a million.
