# 11 — Discussion: Practical Considerations

## Factors affecting VSWE
1. The types of waves supported by the tissue (some don't reach the surface clearly)
2. Quality of observation (camera resolution, frame rate, noise)
3. Quality of the physics model used in the FEM

## FEM mesh resolution
Element size in FEM determines smallest modeled wavelength. Smaller mesh → estimated parameters approach true values. There's an ablation figure showing this.

## Spatial extent of observation
The spatial length L of the observation window determines:
- Largest wavelength observable
- Number of wavelengths captured

Smaller L → degraded FFT dispersion → harder inference. Figure 11 shows that as L shrinks, the observed dispersion relation degrades and the optimization landscape becomes fuzzy.

## Conversational implication
This is the "what can go wrong" section. The method has knobs. The window size matters. The FEM mesh matters. The frame rate matters. Camera resolution matters.

This is relevant for the limitations discussion in the podcast — the method isn't magic, it has well-defined sensitivities. But the LIMITS are known, which means they're addressable through engineering (better cameras, better physics simulators, etc.) rather than through new theory.
