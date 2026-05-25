# 06 — Methods: Estimating Thickness and Stiffness

## The inverse problem
Given Dobs (the observed wave fingerprint from the video), find (T*, E*) such that the THEORETICAL dispersion relation D(T*, E*) most closely matches Dobs.

## How they compute D(T, E)
For any candidate (T, E), they use FEM (finite element method) — a standard numerical physics technique — to simulate what dispersion relation that material would actually produce. They wrote specialized FEM code for efficiency. The output of FEM is a set of CURVES on the (γ, ω) plot, one curve per "branch" of the eigenvalue solutions.

## How they compare images
- Dobs is an IMAGE (from the 2D FFT).
- D(T, E) is a set of CURVES.

To compare, convert D(T, E) into an image form Dhyp(T, E) by smearing a Gaussian kernel along each curve. Now both are images.

After testing several similarity measures, they found SSIM (structural similarity index measure) — a well-known image-similarity metric — works best. Better than MSE, PSNR, or a curve-integration objective.

## The optimization
Maximize SSIM(Dhyp(T, E), Dobs) over (T, E). They use a grid search over candidate values. Not gradient descent. Just brute-force search across a grid.

## Sensitivity claim
They show the method is sensitive to 5% changes in the true parameters. Important — this is the resolution of the method.

## Conversational hook
The "guess and check" framing works here. The computer guesses a thickness and stiffness. It simulates what wave fingerprint that material would produce. Compares to the video's fingerprint. Scores the match. Guesses again. Best match wins.

The clever bit is making the comparison an IMAGE-similarity problem. SSIM is the metric you'd use to grade how similar two photos look. They applied it to wave fingerprints. That's the unexpected move.

## Jargon to translate
- "FEM" → "a standard physics simulation that turns material properties into predicted wave behavior"
- "SSIM" → "an image-similarity score normally used to grade photo quality"
- "objective function" → ban / paraphrase
- "optimization problem" → "find the values that score the highest match"
