journal_metadata:
  paper: 10.1109_cvpr52688.2022.01575
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: The authors are Berthy Feng, Alexander Ogren, Chiara Daraio, and Katie Bouman,
  at Caltech.
excerpt: |-
  Berthy T. Feng                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          Alexander C. Ogren        Chiara Daraio                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Katherine L. Bouman
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 California Institute of Technology
location:
  page_pdf: 1
  page_printed: 1
  section: Author block (front matter)
  surrounding_context: Front matter author affiliations on title page.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. All four author names appear verbatim on page 1, with the institutional
  line "California Institute of Technology" directly below. Katherine L. Bouman is
  the formal version of Katie Bouman. Confirms claim exactly.
---
index: 2
date: '2026-05-24'
status: matched
request: The method estimates Young's modulus and density throughout the 3D interior
  of an object from a single monocular video.
excerpt: |-
  We propose an approach that estimates heterogeneous
  material properties of an object from a monocular video
  of its surface vibrations. Specifically, we show how to es-
  timate Young's modulus and density throughout a 3D ob-
  ject with known geometry.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: See section Abstract on page 1.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim claim from the abstract. Confirms monocular video → 3D
  Young's modulus + density.
---
index: 3
date: '2026-05-24'
status: matched
request: The sub-pixel motion extraction method can detect motion on the order of
  0.001 pixel.
excerpt: |-
  we use the phase-based approach of Wadwha et al. [44],
  which computes local phase shifts in a complex steerable
  pyramid [32, 36, 37]. This method has the advantage over
  other tracking methods (e.g., optical flow) of being robust
  to tiny motion, down to 0.001 pixel [11].
location:
  page_pdf: 3
  page_printed: 3
  section: 4.1 Extracting Image-Space Modes from Video
  surrounding_context: See section 4.1 Extracting Image-Space Modes from Video on
    page 3.
  before: null
  after: null
  bbox: null
comments: 'SUPPORTS. Verbatim: ''0.001 pixel''. Confirms the ''one thousandth of a
  pixel'' claim in the narrative.'
---
index: 4
date: '2026-05-24'
status: matched
request: Motion extraction uses a phase-based approach over a complex steerable pyramid.
excerpt: |-
  we use the phase-based approach of Wadwha et al. [44],
  which computes local phase shifts in a complex steerable
  pyramid [32, 36, 37].
location:
  page_pdf: 3
  page_printed: 3
  section: 4.1 Extracting Image-Space Modes from Video
  surrounding_context: See section 4.1 Extracting Image-Space Modes from Video on
    page 3.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Phase-based + steerable pyramid confirmed verbatim. Narrative's
  'splitting into frequency layers' analogy maps to this technique.
---
index: 5
date: '2026-05-24'
status: matched
request: Only modes at frequencies below half the frame rate (Nyquist limit) are observable.
excerpt: |-
  we can only capture modes at frequencies below the
  Nyquist sampling rate of the camera, which is FPS/2.
location:
  page_pdf: 3
  page_printed: 3
  section: 3.2 Challenge of Monocular Material Estimation
  surrounding_context: See section 3.2 Challenge of Monocular Material Estimation
    on page 3.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Narrative correctly says 'fast modes are invisible'
  and 'slower than half your frame rate'.
---
index: 6
date: '2026-05-24'
status: matched
request: The optimization adds spatial smoothness regularization (total squared variation)
  to the material maps.
excerpt: |-
  we
  choose to minimize total squared variation (TSV) of w and
  v, which encourages spatial smoothness.
location:
  page_pdf: 4
  page_printed: 4
  section: 4.2.1 Optimization Formulation (Regularization)
  surrounding_context: See section 4.2.1 Optimization Formulation (Regularization)
    on page 4.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Narrative's 'smoothness preference' corresponds to TSV.
  Confirms claim.
---
index: 7
date: '2026-05-24'
status: matched
request: They tested the approach on the Stanford Bunny model.
excerpt: |-
  To demonstrate the approach on a
  more complex geometry, Fig. 5 shows a volumetric reconstruction of material properties for the Stanford Bunny [41].
location:
  page_pdf: 5
  page_printed: 5
  section: 5.3 Results (Complex geometry)
  surrounding_context: See section 5.3 Results (Complex geometry) on page 5.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Stanford Bunny used to demonstrate non-cubic geometry.
  Confirms claim.
---
index: 8
date: '2026-05-24'
status: matched
request: 'Real drums were constructed with defects from two materials: nail hardening
  gel and acrylic plastic.'
excerpt: |-
  The de-
  fects were created from two materials: nail hardening gel
  (painted beneath the surface) or acrylic plastic circles (glued
  onto the bottom of the surface).
location:
  page_pdf: 7
  page_printed: 7
  section: 6.1 Real Drums
  surrounding_context: See section 6.1 Real Drums on page 7.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms gel + acrylic defects, painted vs. glued. Narrative
  claim is accurate.
---
index: 9
date: '2026-05-24'
status: matched
request: A loudspeaker was used to excite drum vibrations during the experiment.
excerpt: |-
  The excitation source was a
  PreSonus Sceptre S8 loudspeaker, which sat on a platform
  separate from the optical table and was pointed at the drum.
  For each video, we recorded the drum head's vibration in
  response to a 3.5-second linear frequency sweep (50–1000
  Hz) played by the speaker.
location:
  page_pdf: 13
  page_printed: 13
  section: D.0.2 Vibration-Capture Setup (Supplementary)
  surrounding_context: See section D.0.2 Vibration-Capture Setup (Supplementary) on
    page 13.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim from supplementary. Confirms loudspeaker excitation.
  Narrative claim is accurate.
---
index: 10
date: '2026-05-24'
status: matched
request: The Jello-cube reconstruction used six modes obtained from three videos of
  the cube under different initial deformation conditions.
excerpt: |-
  We recorded three videos
  of the cube under different initial deformation conditions
  (e.g., in one video, we lifted and then quickly released the
  top-front corner of the cube). Multiple videos allowed us to
  identify more unique modes and average duplicate ones.
location:
  page_pdf: 7
  page_printed: 7
  section: 6.2 Real Cubes
  surrounding_context: See section 6.2 Real Cubes on page 7.
  before: null
  after: null
  bbox: null
comments: PARTIALLY_SUPPORTS. PARTIALLY_SUPPORTS. Confirms three videos with different
  initial deformation conditions, and one example was top-front-corner pluck. Six
  modes is confirmed elsewhere on page 7 ('The reconstruction is obtained using six
  unique, motion-extracted image-space modes'). Narrative says 'plucking different
  corners' — paper gives ONE corner example and says 'different initial deformation
  conditions', so 'different corners' is a slight overgeneralization. NARRATIVE WILL
  BE SOFTENED to match the paper's 'different initial deformation conditions' phrasing.
---
index: 11
date: '2026-05-24'
status: matched
request: The real Jello cube reconstruction looks more similar to the simulated cube-with-defect
  than to the simulated homogeneous cube.
excerpt: |-
  (a) is more similar to
  (b) than to (c), indicating that with 6 modes, we can differentiate
  between a cube with a defect and a homogeneous one.
location:
  page_pdf: 8
  page_printed: 8
  section: Figure 11 caption (6.2 Real Cubes)
  surrounding_context: See section Figure 11 caption (6.2 Real Cubes) on page 8.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim from Fig. 11 caption. (a) is the real-data reconstruction,
  (b) is the defect-cube simulation, (c) is the homogeneous-cube simulation. Confirms
  narrative claim.
---
index: 12
date: '2026-05-24'
status: matched
request: The method assumes materials are isotropic and linear elastic.
excerpt: |-
  Our method assumes that materials are isotropic and lin-
  ear elastic. Linear elasticity is only satisfied if the object's
  motion is small.
location:
  page_pdf: 8
  page_printed: 8
  section: 7 Limitations
  surrounding_context: See section 7 Limitations on page 8.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms both assumptions stated in narrative.
---
index: 13
date: '2026-05-24'
status: matched
request: The method requires the object's geometry to be roughly known ahead of time.
excerpt: |-
  Further, we assume that the geometry is, at
  least roughly, known ahead of time (see Fig. 6).
location:
  page_pdf: 8
  page_printed: 8
  section: 7 Limitations
  surrounding_context: See section 7 Limitations on page 8.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms narrative's claim about roughly-known geometry.
---
index: 14
date: '2026-05-24'
status: matched
request: The method was validated with a high-speed camera, not yet with consumer-grade
  cameras.
excerpt: |-
  For now, we have validated our method with a high-
  speed camera. We have not yet demonstrated the approach
  with consumer-grade cameras that bring additional chal-
  lenges such as image compression and noise.
location:
  page_pdf: 8
  page_printed: 8
  section: 7 Limitations
  surrounding_context: See section 7 Limitations on page 8.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms the narrative's honest framing about high-speed
  vs phone.
---
index: 15
date: '2026-05-24'
status: matched
request: For gel defects, the density estimation shows a bright filled region; for
  acrylic defects, only the edges of the defect appear.
excerpt: |-
  For gel defects,
  there is a bright, filled region in the density map that corre-
  sponds to a higher mass from the defect. For acrylic defects,
  this change only appears on the edges of the defect. This is
  possibly because the acrylic circles are much stiffer than
  gel, which bends along with the rubber membrane.
location:
  page_pdf: 7
  page_printed: 7
  section: 6.1 Real Drums (Results)
  surrounding_context: See section 6.1 Real Drums (Results) on page 7.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms the gel-fills-versus-acrylic-edges-only claim
  and the reason (acrylic too stiff to bend along).
---
index: 16
date: '2026-05-24'
status: matched
request: The drums were made by stretching a thin rubber sheet over a 4-inch frame
  (a 4 x 4 PVC adaptor).
excerpt: |-
  The drums were constructed by fixing a thin rubber sheet
  over a 4"x4" PVC adaptor with a rubber band.
location:
  page_pdf: 13
  page_printed: 13
  section: D.0.1 Drum Construction (Supplementary)
  surrounding_context: See section D.0.1 Drum Construction (Supplementary) on page
    13.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms 4"x4" PVC adaptor as the drum frame. Narrative's
  'four-inch frame' is accurate.
---
index: 17
date: '2026-05-24'
status: matched
request: Prior NDT tools mostly estimate only homogenized material properties, not
  spatially-varying interior maps.
excerpt: |-
  Traditional non-
  destructive testing approaches, which often require expen-
  sive instruments, generally estimate only homogenized ma-
  terial properties or simply identify the presence of defects.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: See section Abstract on page 1.
  before: null
  after: null
  bbox: null
comments: SUPPORTS. Verbatim. Confirms the narrative's claim that traditional NDT
  mostly gives a single number, not an interior map.
