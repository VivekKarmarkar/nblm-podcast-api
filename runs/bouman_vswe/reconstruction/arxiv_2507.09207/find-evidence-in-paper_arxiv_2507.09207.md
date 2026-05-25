journal_metadata:
  paper: arxiv_2507.09207
  skill: find-evidence-in-paper
  created: '2026-05-24'
  format: YAML documents separated by --- markers. First doc = metadata, subsequent
    docs = indexed entries. Machine-friendly format consumed by Cat-2 highlighting
    skills.
---
index: 1
date: '2026-05-24'
status: matched
request: The authors are Alexander Ogren, Berthy Feng, Jihoon Ahn, Katie Bouman, and
  Chiara Daraio at Caltech.
excerpt: |-
  Alexander C. Ogren∗            Berthy T. Feng∗ Jihoon Ahn Katherine L. Bouman                               Chiara Daraio
                                                                                    California Institute of Technology
location:
  page_pdf: 1
  page_printed: 1
  section: Author block (front matter)
  surrounding_context: Front matter author affiliations on title page.
comments: SUPPORTS. All five author names appear verbatim on page 1, with the institutional
  line "California Institute of Technology" directly below. Katherine L. Bouman =
  Katie Bouman. Confirms the claim exactly.
---
index: 2
date: '2026-05-24'
status: matched
request: VSWE infers thickness and stiffness of a structure from just a video of waves
  on its surface.
excerpt: We propose a method for inferring the thickness and stiffness of a structure
  from just a video of waves on its surface. Our method works by extracting a dispersion
  relation from the video and then solving a physics-based optimization problem to
  find the best-fitting thickness and stiffness parameters.
location:
  page_pdf: 1
  page_printed: 1
  section: Abstract
  surrounding_context: Abstract on page 1.
comments: 'SUPPORTS. Verbatim from abstract. Confirms the core method description:
  video of surface waves -> dispersion relation -> physics-based optimization -> thickness
  + stiffness.'
---
index: 3
date: '2026-05-24'
status: matched
request: A massage gun applied to your calf produces ripples that convey information
  about underlying layers of fat, muscle, and bone.
excerpt: Imagine applying a massage gun to your calf. The ripples on your skin convey
  information about the underlying layers of fat, muscle, and bone. In fact there
  is a well-defined relationship linking the thickness and stiffness of each layer
  to the wave propagation behavior.
location:
  page_pdf: 1
  page_printed: 1
  section: 1. Introduction
  surrounding_context: First paragraph of introduction on page 1.
comments: SUPPORTS. The massage gun image is verbatim from the introduction. The paper
  explicitly uses this motivating analogy, which is the same one used in the narrative
  hook.
---
index: 4
date: '2026-05-24'
status: matched
request: Tissue thickness or stiffness changes are linked to tumors, musculoskeletal
  degeneration, and liver disease.
excerpt: We are primarily motivated by the task of biological tissue characterization,
  which has broad applications including at-home health monitoring. For example, tumors
  [25, 29], musculoskeletal degeneration [30, 41, 42], and liver disease [22, 39]
  often lead to changes in tissue thickness or stiffness.
location:
  page_pdf: 1
  page_printed: 1
  section: 1. Introduction
  surrounding_context: Second paragraph of introduction on page 1.
comments: SUPPORTS. Verbatim. The narrative's "tumors, muscle disease, liver disease"
  matches exactly to the paper's clinical motivation citations.
---
index: 5
date: '2026-05-24'
status: matched
request: Current elastography techniques require specialized expensive equipment and
  trained medical specialists, making regular screening infeasible.
excerpt: However, such methods often require not only high-end, expensive equipment,
  but also trained medical specialists [6, 11], making regular screening infeasible.
  In contrast, our work leverages surface waves, which are generally less expensive
  to observe than their bulk counterparts.
location:
  page_pdf: 2
  page_printed: 2
  section: 2.2 Wave-based material characterization
  surrounding_context: Related work, near end of section 2.2 on page 2.
comments: SUPPORTS. The narrative's claim that "current tools need expensive machines
  and a trained operator" is verbatim supported. Phrase "making regular screening
  infeasible" maps directly to the narrative's "regular screening basically doesn't
  happen."
---
index: 6
date: '2026-05-24'
status: matched
request: Visual Vibration Tomography (VVT) infers subsurface material properties of
  a 3D object by analyzing its global vibrational modes - it requires the whole object.
excerpt: In contrast, Visual Vibration Tomography [17] infers subsurface material
  properties. Specifically, it recovers the spatially-varying stiffness and density
  throughout a 3D object with known geometry by analyzing its global vibrational modes.
location:
  page_pdf: 2
  page_printed: 2
  section: 2.1 Video-based material characterization
  surrounding_context: Related work, page 2.
comments: SUPPORTS. The VVT-vs-VSWE contrast in the narrative ("Jello cube paper required
  modeling the WHOLE object, this requires only a patch") is grounded in this paragraph.
  VVT analyzes "global vibrational modes" with "known geometry" - which is exactly
  the limitation VSWE relaxes by using surface waves.
---
index: 7
date: '2026-05-24'
status: matched
request: VSWE targets local regions with simpler geometry, avoiding the need to model
  complex global geometry.
excerpt: Surface waves have been under-utilized for video-based material characterization,
  even though they can also be observed in video and contain useful information about
  underlying material properties. Our work leverages surface waves, which prevents
  the need to model a complex geometry and solve for its global modes by targeting
  local regions where we can analyze wave modes of a simpler geometry.
location:
  page_pdf: 2
  page_printed: 2
  section: 2.1 Video-based material characterization (end)
  surrounding_context: Final paragraph of section 2.1 on page 2.
comments: SUPPORTS. This is the linchpin sentence for the narrative's "you can analyze
  a SECTION instead of the whole object" framing. Paper explicitly says VSWE targets
  "local regions" with "simpler geometry" - which is the structural advance over VVT.
---
index: 8
date: '2026-05-24'
status: matched
request: Wave propagation is characterized by a dispersion relation, and under their
  assumptions thickness T and stiffness E fully determine it.
excerpt: Under some common biomechanical assumptions in our layer model (discussed
  further in Sec. 3.1), the thickness and stiffness of the soft layer fully determine
  the dispersion relation. The main idea of our method is to find the thickness and
  stiffness values that lead to a dispersion relation that matches the dispersion
  relation extracted from surface waves observed in the video.
location:
  page_pdf: 2
  page_printed: 2
  section: 1. Introduction (end)
  surrounding_context: Bottom of page 1 transitioning to page 2.
comments: SUPPORTS. The narrative's "the wave fingerprint identifies the material"
  framing maps to this verbatim claim. "Fully determine" is verbatim. Confirms the
  inverse-problem framing.
---
index: 9
date: '2026-05-24'
status: matched
request: Motion extraction uses phase-based motion processing for sub-pixel displacement
  detection.
excerpt: The first step is to quantify the image-space displacements in the video.
  Since surface wave motion tends to be small, we use phase-based motion processing
  [43], which is sensitive to sub-pixel displacements. Specifically, we compute local
  phase shifts in a complex steerable pyramid [38] and then convert these to pixel
  displacements [19].
location:
  page_pdf: 3
  page_printed: 3
  section: 4.1.1 Motion extraction
  surrounding_context: First paragraph of motion extraction subsection on page 3.
comments: SUPPORTS. Verbatim. The narrative's claim that the motion-extraction trick
  uses "phase-based motion processing" with "complex steerable pyramid" matches this
  passage exactly. This is the same trick used in VVT (reference [43] Wadhwa et al.
  2013 is the same paper cited in the VVT narrative).
---
index: 10
date: '2026-05-24'
status: matched
request: The 2D FFT decomposes the surface motion into spatial (wavenumber) and temporal
  (frequency) components to produce the observed dispersion relation.
excerpt: We process the image-space surface displacements into a dispersion relation
  via the fast Fourier transform (FFT). We assume that the waves are traveling in
  the horizontal direction in image-space. For each row of pixels in the ũ(x̃, ỹ,
  t) video, we take a 2D FFT, transforming the space dimension x̃ to the wavenumber
  dimension γ and the time dimension t to the frequency dimension ω.
location:
  page_pdf: 3
  page_printed: 3
  section: 4.1.2 Estimating the dispersion relation
  surrounding_context: Page 3, after motion extraction subsection.
comments: SUPPORTS. Verbatim. Confirms the narrative's "decomposes the motion field
  into spatial and temporal frequencies, both at once" claim. The paper does this
  via 2D FFT - which the narrative paraphrases conversationally without naming "Fourier"
  directly (per jargon discipline).
---
index: 11
date: '2026-05-24'
status: matched
request: They use SSIM (structural similarity index measure) as the objective function
  for comparing dispersion relations, treating them as images.
excerpt: After testing various objective functions, we found that treating dispersion
  relations as images and using the structural similarity index measure (SSIM) [45]
  to work best. That is, we aim to maximize the SSIM between the images of the observed
  and proposed dispersion relations.
location:
  page_pdf: 4
  page_printed: 4
  section: 4.2 Estimating the thickness and stiffness
  surrounding_context: Page 4, optimization subsection.
comments: SUPPORTS. Verbatim. The narrative's claim that the team tried multiple metrics
  and SSIM (a photo-quality metric) won is grounded here. "Treating dispersion relations
  as images" matches the narrative's "the fingerprints are kind of like images, after
  all."
---
index: 12
date: '2026-05-24'
status: matched
request: The optimization is solved via grid search over candidate thickness and stiffness
  values.
excerpt: We solve Eq. (5) with a grid search over possible thickness and stiffness
  values, although more efficient approaches can be taken for computationally demanding
  settings.
location:
  page_pdf: 4
  page_printed: 4
  section: 4.2 Estimating the thickness and stiffness
  surrounding_context: Page 4, just after Eq. (5).
comments: SUPPORTS. The narrative's "the computer tries thousands of candidate combinations"
  matches the verbatim grid-search claim. Confirms the "guess and check, sped up enormously"
  framing is accurate to the actual method.
---
index: 13
date: '2026-05-24'
status: matched
request: VSWE is sensitive to 5% changes in the true parameters in plane-strain simulations.
excerpt: VSWE has some margin of error due to the discrepancy between the observed
  and true dispersion relations, although we show in our experiments in Sec. 5.1 it
  is sensitive to 5% changes in the true parameters.
location:
  page_pdf: 4
  page_printed: 4
  section: 4.1.2 Estimating the dispersion relation
  surrounding_context: Page 4, end of section 4.1.2.
comments: SUPPORTS. Verbatim "5% changes in the true parameters." The narrative's
  "good to about five percent under best-case conditions" matches this exactly.
---
index: 14
date: '2026-05-24'
status: matched
request: They created gelatin phantoms by pouring varying amounts (1000, 1100, 1500
  mL) of gelatin into the same-sized container to create three different thicknesses.
excerpt: To test our method on real data, we created gelatin-based phantoms (i.e.,
  samples mimicking biological tissue) of varying thicknesses. We poured varying amounts
  of gelatin (1000, 1100, and 1500 mL) into the same-sized container, leading to three
  different thicknesses. We set the samples in the refrigerator for about 24 hours.
location:
  page_pdf: 5
  page_printed: 5
  section: 5.2 Real videos of gelatin-based phantoms
  surrounding_context: Page 5, start of gelatin section.
comments: SUPPORTS. Verbatim volumes (1000, 1100, 1500 mL). Confirms the narrative's
  exact recipe for the three phantoms.
---
index: 15
date: '2026-05-24'
status: matched
request: They sprinkled garlic powder onto the gelatin samples to create texture for
  motion extraction.
excerpt: Once they were set, we sprinkled garlic powder onto the samples to create
  texture for motion extraction.
location:
  page_pdf: 5
  page_printed: 5
  section: 5.2 Real videos of gelatin-based phantoms
  surrounding_context: Page 5, gelatin section.
comments: SUPPORTS. Verbatim "garlic powder." The narrative's "Garlic powder. On Jello."
  callout is grounded in this exact methodological detail.
---
index: 16
date: '2026-05-24'
status: matched
request: They excited waves with a shaker, recorded with a high-speed camera at 600
  FPS for about four seconds per video.
excerpt: To obtain videos, we applied a shaker at one end of the sample to excite
  waves with a chirp signal and recorded the surface of the sample with a high-speed
  camera at 600 FPS (each video was about four seconds long).
location:
  page_pdf: 5
  page_printed: 5
  section: 5.2 Real videos of gelatin-based phantoms
  surrounding_context: Page 5, gelatin section.
comments: SUPPORTS. Verbatim "600 FPS" and "four seconds long." The narrative's "shaker
  on one side... six hundred frames per second" matches exactly.
---
index: 17
date: '2026-05-24'
status: matched
request: VSWE estimates stiffness within 1.2% error of the rheometry range on the
  gelatin phantoms.
excerpt: Regardless, in each case, VSWE estimates the stiffness extremely well, within
  1.2% error of the rheometry range.
location:
  page_pdf: 6
  page_printed: 6
  section: Figure 7 caption (continued from page 5)
  surrounding_context: Caption text on page 6 for Fig. 7.
comments: SUPPORTS. Verbatim "1.2% error of the rheometry range." The narrative's
  headline "one point two percent" matches exactly.
---
index: 18
date: '2026-05-24'
status: matched
request: Thickness was measured with calipers and stiffness with rheometry as the
  ground truth for the gelatin phantoms.
excerpt: For each set sample, we measured the thickness with calipers, and we used
  rheometry to obtain ground-truth stiffness values.
location:
  page_pdf: 5
  page_printed: 5
  section: 5.2 Real videos of gelatin-based phantoms
  surrounding_context: Page 5, gelatin methodology.
comments: SUPPORTS. The narrative's "checked recovered thickness against caliper measurements...
  recovered stiffness against a rheometer" matches verbatim. Confirms the lab-standard
  ground truth.
---
index: 19
date: '2026-05-24'
status: matched
request: As gelatin samples warmed up out of the refrigerator, their stiffness decreased
  and VSWE tracked the change.
excerpt: As a sample spends more time out of the refrigerator, its temperature increases
  and its stiffness decreases. Fig. 7(b) shows that the estimated stiffness decreases
  accordingly with temperature.
location:
  page_pdf: 6
  page_printed: 6
  section: 5.2 Real videos of gelatin-based phantoms (end)
  surrounding_context: Page 6, main text continuation.
comments: SUPPORTS. The narrative's "as the gelatin softened, the video-based estimate
  softened with it" is verbatim supported. Confirms the moving-ground-truth experiment.
---
index: 20
date: '2026-05-24'
status: matched
request: The 3D leg geometry came from the Visible Human Project dataset and they
  ran a full 3D physics simulation.
excerpt: The anatomical geometry of the leg was obtained as an STL file from the dataset
  of Andreassen et al. [3], who created 3D models from the National Library of Medicine's
  Visible Human Project [2]. We simulated the leg's response to a chirp excitation
  applied on the leg in COMSOL, running a full 3D physics simulation without any assumptions
  besides linear elasticity.
location:
  page_pdf: 6
  page_printed: 6
  section: 5.3 3D human leg with spatially-varying thickness
  surrounding_context: Page 6, leg section.
comments: SUPPORTS. Verbatim "Visible Human Project" and "full 3D physics simulation."
  The narrative correctly clarifies they did NOT film a real leg - this was a simulation,
  which is verbatim supported.
---
index: 21
date: '2026-05-24'
status: matched
request: They used a sliding observation window across the upper calf, with VSWE-estimated
  thickness tracking the changing leg thickness.
excerpt: We applied a sweeping window across the upper calf region, estimating the
  thickness and modulus at each window location. Fig. 8 shows how, as the window sweeps
  around the leg, the inferred thickness changes. We computed the true thickness by
  taking the distance from the point on the skin to the nearest point on the bone.
location:
  page_pdf: 7
  page_printed: 7
  section: 5.3 3D human leg with spatially-varying thickness
  surrounding_context: Page 7, leg subsection.
comments: SUPPORTS. Verbatim "sweeping window" - the narrative's "sliding observation
  window" describes exactly this. The "true thickness... distance from the point on
  the skin to the nearest point on the bone" matches the narrative's "actual changing
  thickness of the underlying soft tissue."
---
index: 22
date: '2026-05-24'
status: matched
request: Three distinct windows in the lower calf near the ankle recovered the very
  different thicknesses correctly.
excerpt: We also applied VSWE to three different windows in the lower calf region.
  Rather than perform a sweep in this region, we chose to focus on three distinct
  windows since there are three subregions in the lower calf area that have notably
  different thicknesses, due to the tissue structure changing a lot near the ankle.
  As Fig. 8 shows, the inferred thickness agrees with the true thickness distribution
  for each subregion.
location:
  page_pdf: 7
  page_printed: 7
  section: 5.3 3D human leg with spatially-varying thickness
  surrounding_context: Page 7, leg subsection.
comments: SUPPORTS. Verbatim "three different windows in the lower calf region" and
  "three subregions... notably different thicknesses, due to the tissue structure
  changing a lot near the ankle." Narrative claim is grounded.
---
index: 23
date: '2026-05-24'
status: matched
request: They assume isotropic linear-elastic materials.
excerpt: Assuming an isotropic linear-elastic material, the harmonic elastic wave
  equation can be written as
location:
  page_pdf: 2
  page_printed: 2
  section: 3.1 Dispersion relations
  surrounding_context: Page 2-3 transition, just before the wave equation.
comments: SUPPORTS. Verbatim "isotropic linear-elastic material." The narrative's
  "isotropic and linear elastic" disclaimer matches the paper's foundational assumption
  exactly.
---
index: 24
date: '2026-05-24'
status: matched
request: The model assumes the bone layer is much stiffer than soft tissue and can
  be modeled as motionless.
excerpt: 3. The bone is much stiffer than the soft tissue. This means neither the
  thickness nor the exact stiffness of the bone layer matters, and we can model it
  as motionless.
location:
  page_pdf: 3
  page_printed: 3
  section: 3.2 Assumptions for tissue characterization
  surrounding_context: Page 3, list of assumptions.
comments: 'SUPPORTS. Verbatim. The narrative''s "soft layer on top of a hard layer
  modeled as motionless" maps directly to assumption #3.'
---
index: 25
date: '2026-05-24'
status: matched
request: Characteristic numbers allow VSWE to be applied to scenarios with parameters
  very different from those originally tested.
excerpt: Understanding these characteristic numbers is important for extending the
  use of VSWE to scenarios and applications with vastly different parameter ranges
  than those studied in this paper, whether the objects are much larger or smaller,
  stiffer or softer, denser or lighter, or exhibit dynamics at much higher or lower
  wavenumbers or frequencies. In general, by preserving the values of these characteristic
  numbers (e.g., by increasing FPS in coordination with ω), we can preserve the performance
  of VSWE.
location:
  page_pdf: 8
  page_printed: 8
  section: 6.2 Characteristic numbers
  surrounding_context: Page 8, discussion section.
comments: SUPPORTS. Verbatim claim about extending VSWE across vastly different parameter
  ranges by preserving the characteristic numbers. The narrative's "if you adjust
  your camera, your frame rate, your window size in coordinated ways, you can apply
  this to objects ten times bigger or smaller" is grounded here. Also supported by
  Fig. 12 caption mentioning "parameters 10× different than the primary ranges studied
  in this paper."
---
index: 26
date: '2026-05-24'
status: matched
request: SSIM was decisively better than alternative objective functions (curve-based,
  MSE, PSNR) for the optimization landscape.
excerpt: 'As mentioned in Sec. 4.2, we find that SSIM performs best for the optimization
  objective function. This choice was crucial for obtaining acceptable results with
  the 3D leg. Fig. 9 shows the optimization landscape for different choices of the
  objective function, demonstrated on both the upper calf simulation and a real video
  of gelatin. We compare SSIM to the following objective functions: a curve-based
  objective function, the negative mean squared error (MSE) between the images, and
  the peak signal-to-noise ratio (PSNR) between the images.'
location:
  page_pdf: 6
  page_printed: 6
  section: 5.3.1 Objective function ablation
  surrounding_context: Page 6, ablation subsection.
comments: SUPPORTS. Verbatim. The narrative's "the team tried four different similarity
  scores. The winner was something called SSIM" matches exactly - four candidates
  (curve-based, MSE, PSNR, SSIM), SSIM wins.
---
index: 27
date: '2026-05-24'
status: matched
request: Visual Vibration Tomography (the predecessor paper) was published by Berthy
  T. Feng, Alexander C. Ogren, Chiara Daraio, and Katherine L. Bouman at CVPR 2022.
excerpt: 'Berthy T Feng, Alexander C Ogren, Chiara Daraio, and Katherine L Bouman.
  Visual vibration tomography: Estimating interior material properties from monocular
  video. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
  Recognition, pages 16231–16240, 2022.'
location:
  page_pdf: 9
  page_printed: 9
  section: References (entry [17])
  surrounding_context: Page 9, bibliography.
comments: SUPPORTS. Verbatim VVT paper citation [17]. Same authors as the current
  paper (Berthy Feng + Bouman group at Caltech) - confirms the narrative's "same Caltech
  group" lineage claim. Confirms the VVT-to-VSWE evolution arc is grounded in same-team
  continuation, not a stretched analogy.
---
index: 28
date: '2026-05-24'
status: matched
request: The closing line of the paper says "everyday visual data" can reveal critical
  information beneath the skin.
excerpt: We validated our method on both simulated and real data, showing that our
  method is sensitive to small changes in the properties of tissue-like media. We
  demonstrated the promise of applying VSWE in the real world by testing it on real
  videos of gelatin-based phantoms and on a simulated realistic 3D human leg. Our
  work shows the potential of everyday visual data to reveal critical information
  deep beneath the skin.
location:
  page_pdf: 8
  page_printed: 8
  section: 7. Conclusion
  surrounding_context: Page 8, final paragraph.
comments: SUPPORTS. Verbatim "everyday visual data to reveal critical information
  deep beneath the skin." The narrative's closing arc (cameras becoming instruments
  for what only specialists could touch) is grounded in this exact authorial statement.
  Not author intent inference - this is verbatim from the paper.
---
index: 29
date: '2026-05-24'
status: matched
request: The phase-based motion technique used in VSWE can detect motion on the order
  of one-thousandth of a pixel (0.001 pixel).
excerpt: Since surface wave motion tends to be small, we use phase-based motion processing
  [43], which is sensitive to sub-pixel displacements. Specifically, we compute local
  phase shifts in a complex steerable pyramid [38] and then convert these to pixel
  displacements [19].
location:
  page_pdf: 3
  page_printed: 3
  section: 4.1.1 Motion extraction
  surrounding_context: Page 3, motion extraction subsection.
comments: PARTIALLY_SUPPORTS. VSWE only describes the technique as "sensitive to sub-pixel
  displacements" without quantifying the resolution. The "0.001 pixel" figure is a
  published property of the SAME phase-based technique (Wadhwa et al. 2013, reference
  [43] here; reference [44] in the VVT paper), and was quantified in the predecessor
  VVT paper (where the narrative previously cited it). The narrative frames it correctly
  as a property of the technique used (not a VSWE-specific claim) by saying "the same
  technique they used for the Jello cube... can detect motion on the order of one
  thousandth of a pixel." This is grounded in the technique's documented sensitivity.
  ACCEPTABLE in the narrative because the framing makes clear this is a property of
  the underlying technique, not a new claim made by THIS paper.
