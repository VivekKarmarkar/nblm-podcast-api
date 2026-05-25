# 10 — Results: Objective Function Ablation

## What they tested
Compared 4 candidate similarity measures for the optimization:
1. Curve-based (integrate Dobs along the FEM curves)
2. Negative MSE between images
3. PSNR between images
4. SSIM between images

## Outcome
SSIM wins decisively. It produces the SHARPEST optimization landscape (a clear peak at the true parameters). The other three either:
- Pick wrong optimal parameters (especially for the 3D leg)
- Produce blurrier landscapes (harder to locate the optimum)

SSIM was the choice that made the 3D leg results work. The narrative point: image-similarity reasoning, applied to wave fingerprints, beat the "obvious" curve-based and pixel-difference choices.

## Conversational worth
This is a methods detail but it's also a STORY about how empirically-driven optimization choices matter. They tried the obvious metric (curve integration), it didn't work. They tried pixel-difference (MSE, PSNR), didn't work. They tried image structural similarity (SSIM, originally designed for evaluating photo compression quality), and that worked.

There's a small "this is what research really looks like" detail buried here — the right metric isn't always the mathematically obvious one. Sometimes you have to test four options to find the one that's robust.

Whether to include in the podcast: probably ONLY as a passing aside, since it's a methods choice rather than a conceptual leap. The narrative space is better spent on the gelatin results and the human leg simulation.
