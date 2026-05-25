# 08 — Results: Real Gelatin-Based Phantoms

## What they built
Gelatin "phantoms" (samples mimicking biological tissue). They poured three different volumes (1000, 1100, 1500 mL) of gelatin into the same container, yielding three different thicknesses. Set in the fridge ~24 hours. SPRINKLED GARLIC POWDER on top to create texture for motion extraction (smooth gel would be hard to track).

## Ground truth
- Thickness measured with calipers
- Stiffness measured with rheometry (a standard mechanical test for material stiffness)

## Experimental setup
A SHAKER applied at one end of the sample, exciting waves via a chirp signal. A HIGH-SPEED CAMERA at 600 FPS recorded the surface (~4 seconds per video). They took ~60 videos per sample over an hour after removing the gel from the fridge. As the gelatin warmed up, its stiffness changed, giving a natural range of ground-truth stiffness values.

## Results
- Thickness: VSWE consistently identifies the three different thicknesses correctly. Within the caliper confidence interval (0.2 to 0.8 quantiles of multiple measurements).
- Stiffness: As temperature increased, stiffness decreased (gel softens when warm). VSWE tracks this. Within ~1.2% of the rheometry range.

There's a caveat: rheometry was only measured between 10-100 Hz due to instrument limits, while excitation was 40-200 Hz. For colder/stiffer samples, higher-frequency wave dynamics dominate, which the rheometer wasn't measuring. Some of the discrepancy traces to this mismatch.

## Conversational hook
"They put garlic powder on Jello." This sentence will land. It's the kind of homemade-experiment detail that signals these are real people doing real things with kitchen ingredients to test a fancy idea.

The headline number — VSWE within 1.2% of professional rheometry on stiffness — is incredible for a video-based method. This is the strongest real-data validation in the paper.
