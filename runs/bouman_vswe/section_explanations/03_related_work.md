# 03 — Related Work

## Video-based material characterization
Videos encode rich info about objects and environments. Prior work has used surface vibrations or sound from video to recover unknown properties. For material characterization:
- Specific object classes (fabrics, rods, trees) where dynamics are fully visible
- Visual Vibration Tomography (VVT, Feng et al. 2022) → infers subsurface stiffness and density across a 3D object with KNOWN geometry, by analyzing the object's GLOBAL VIBRATIONAL MODES

VVT is a clear sibling. The key contrast: VVT looks at MODES (whole-object vibrations). VSWE looks at SURFACE WAVES (traveling waves along a local patch of surface). Why this matters: surface waves don't require modeling the WHOLE object's complex geometry. You can target a local region with simpler geometry and analyze the waves traveling through it.

## Wave-based material characterization
Wave-based imaging uses physical understanding of how properties affect waves:
- MRI uses radio-frequency wave absorption
- Ultrasound uses high-frequency mechanical BULK waves (waves through the interior)
- Shear-wave elastography, MR elastography, transient elastography — all use bulk waves to estimate elasticity

These need expensive equipment AND trained specialists. VSWE uses SURFACE waves instead — generally less expensive to observe.

Inspiration: geophysics and seismic imaging have used surface waves to infer subsurface features for decades. The authors borrow that idea and bring it to consumer-video scale.

Prior work (Białas & Guzina 2011) suggested surface-wave sensing using SENSORS placed sparsely on the skin. VSWE uses DENSE VISUAL DATA from a video instead.

## Conversational takeaway
The intellectual lineage: VVT pulled material info from MODES; geophysicists have long pulled material info from SURFACE WAVES (think how seismologists infer Earth's crust structure from wave timing). VSWE marries those traditions — surface waves from seismology, but observed by camera instead of sensor array.
