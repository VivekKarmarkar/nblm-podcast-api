# 12 — Discussion: Characteristic Numbers

## The idea (dimensionless groups / pi-groups)
Characterize the system using DIMENSIONLESS combinations of parameters:
- π1 = γL (wavenumber × window length)
- π2 = PPM/γ (pixels per meter relative to wavenumber)
- π3 = ωτ (frequency × observation time)
- π4 = FPS/ω (frame rate relative to frequency)
- π5 = 1/(γ·e) (related to FEM element size)
- π6 = γT (wavenumber × tissue thickness — the "shallowness" of the wave)

Larger π1-π4 → better FFT dispersion quality. π5 → controls FEM accuracy. π6 controls the wave-physics regime:
- π6 too large → wave behaves as if medium were infinitely thick (can't pinpoint thickness)
- π6 too small → above some wavelength, waves can't exist (need to capture shorter wavelengths)

## Why this matters
These dimensionless numbers let you EXTEND VSWE to settings far outside the original parameter ranges. If you preserve the values of π1-π6 (e.g., scale FPS in coordination with ω), the method should work for objects much bigger/smaller, stiffer/softer, denser/lighter.

Figure 12 shows an example: they ran VSWE on a system with parameters 10× different from the tested ranges, by rescaling everything to preserve the pi-groups. The performance was preserved.

## Conversational hook
The story here is one of GENERALIZABILITY. The team didn't just show the method works on gelatin and on simulated legs. They showed there's a SCALING LAW — what dimensionless ratios you need to keep fixed to make VSWE work for vastly different objects.

This is the bridge to all those other application domains. Want to use VSWE on a giant geological structure? Scale your camera, frame rate, and observation window such that the pi-groups stay in range. Want to use it on a microscopic sample? Same principle.

In the podcast, this is probably distilled to: "the method scales." Skip the math. The implication — that VSWE can apply to wildly different scales by tuning the camera/observation parameters — is the takeaway.
