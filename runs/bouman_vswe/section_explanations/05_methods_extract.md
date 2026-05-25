# 05 — Methods: Extracting a Dispersion Relation from Video

## Two big steps overall
1. Extract dispersion relation from the video.
2. Solve an optimization problem to find (T, E) that best explain it.

## Step 1: Motion extraction (sub-pixel)
Surface wave motion is TINY — well below one pixel of camera motion. They use the SAME phase-based motion processing technique as VVT (Wadhwa et al. 2013) — compute local phase shifts in a complex steerable pyramid, convert to pixel displacements. Result: per-pixel, per-frame horizontal displacement (u-tilde) and vertical displacement (v-tilde). Image-space coordinates have a tilde to distinguish from world-space.

This is the same sub-pixel-motion trick as VVT. They piggyback on prior tools. Surface motion can be MUCH smaller than the pixel grid and still get recovered.

## Step 2: 2D FFT to get a dispersion relation
Assume the waves travel in the horizontal direction in image-space. For each ROW of pixels in the displacement video, take a 2D FFT:
- Time (t) → temporal frequency (ω)
- Space (x-tilde) → wavenumber (γ)

This produces a complex-valued (γ, ω) spectrum. The MAGNITUDE of this spectrum is the row's dispersion relation. Average across all rows AND both displacement directions (horizontal u and vertical v) → "observed dispersion relation" Dobs.

The result is the image-form dispersion relation. Bright spots on the (γ, ω) plot indicate combinations of wavenumber and frequency that are present in the surface motion.

## Things that mess it up (the "incompleteness" problem)
Dobs doesn't perfectly match the theoretical dispersion relation because:
- Some wave modes don't express on the surface or need too much energy → invisible in video
- Frequencies above Nyquist (FPS/2) can't be captured → missing high-frequency content
- Motion extraction is noisy (camera noise, ambient motion)

This is why the next step is an OPTIMIZATION — not a direct readout.

## Conversational hook
The 2D FFT step is the load-bearing magic. You record a video of ripples. You break the video into rows. For each row, you decompose what you see into "which wavelengths are present" (γ) and "which frequencies are present" (ω). Plot those together. The bright spots on the plot are the waves that actually got through the medium. THAT pattern is the fingerprint.
