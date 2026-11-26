---
gallery_title: "AnyMoCap Features"
gallery_image: "/Applications/images/force_plate_offset.webp"
anylink: Application/MocapExamples/SpecialFeatures/ForcePlateSurfaceOffset.main.any
---

(sphx_glr_auto_examples_MoCap_plot_AnyMoCapFeatures.py)=

# AnyMoCap Features

:::{anylink-gallery}
:margin:
:::

A collection of small models that demonstrate selected features of the
*AnyMoCap* framework. The examples in `Application/MocapExamples/SpecialFeatures`
show how to adjust common MoCap workflows without creating a full custom model.

The folder includes examples for:

* driving toe flexion in a BVH-based model using either a marker or a soft-contact driver (`BVH_Xsens_ToeFlexion.main.any`)
* offsetting the effective surface of a force plate to represent stepped or elevated floor geometry (`ForcePlateSurfaceOffset.main.any`)
* assigning individual marker cutoff frequencies and filter orders (`IndividualMarkerCutoffFrequency.main.any`)
* normalizing output data to gait-cycle events using `Normalized_Abscissa` (`GaitCycleNormalization.main.any`)
* assigning time-varying or custom marker weights to handle dropout or trial-specific reliability (`MarkerWeightsExample.main.any`)
* estimating the initial posture from marker positions (`InitialPosExample.any`)
* customizing external design variables during parameter identification (`ExternalDesVars.main.any`)

These examples are meant to be read as compact starting points for adapting a standard
MoCap workflow to a specific movement, dataset, or analysis requirement.

:::{admonition} In Model Repository:
:class: seealso
`Application/MocapExamples/SpecialFeatures`

* {anylink-file}`BVH_Xsens_ToeFlexion.main.any <Application/MocapExamples/SpecialFeatures/BVH_Xsens_ToeFlexion.main.any>` 
* {anylink-file}`ExternalDesVars.main.any <Application/MocapExamples/SpecialFeatures/ExternalDesVars.main.any>` 
* {anylink-file}`ForcePlateSurfaceOffset.main.any <Application/MocapExamples/SpecialFeatures/ForcePlateSurfaceOffset.main.any>`
* {anylink-file}`GaitCycleNormalization.main.any <Application/MocapExamples/SpecialFeatures/GaitCycleNormalization.main.any>`
* {anylink-file}`IndividualMarkerCutoffFrequency.main.any <Application/MocapExamples/SpecialFeatures/IndividualMarkerCutoffFrequency.main.any>`
* {anylink-file}`InitialPosExample.any <Application/MocapExamples/SpecialFeatures/InitialPosExample.any>`
* {anylink-file}`MarkerWeightsExample.main.any <Application/MocapExamples/SpecialFeatures/MarkerWeightsExample.main.any>`

:::
