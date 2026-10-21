---
gallery_title: "Toe Flexion (C3D driven)"
gallery_image: "/Applications/images/Plug-in-gait_simple_lowerbody_ToeFlex_GM.webp"
anylink: Application/MocapExamples/Plug-in-gait_Simple/LowerExtremity_ToeFlexion.main.any
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_LowerExtremity_ToeFlexion)=

# Toe Flexion (C3D driven)

:::{anylink-gallery}
:margin:
:::

This is a variant of the <a href="Plug-in-gait_Simple_LowerExtremity.html" target="_blank" rel="noopener">Simple Lower Extremity Model</a>, showing toe flexion. The model shows how the <a href="../../tools/class-templates/Utilities.Kinematic%20limits.RotationPenetrationCombiDriver_template.html" target="_blank" rel="noopener">RotationPenetrationCombiDriver</a> class
template can be used to bend the toes even without measured data. This class template
ensures that toes bend to prevent penetration with the ground at toe-off, while they
stay in the neutral posture otherwise.

<!-- See https://sphinxcontrib-video.readthedocs.io/en/latest/quickstart.html -->
:::{video} ../../body/_static/FootGaitNormal_1_ToeFlex_GM.webm
:autoplay:
:loop:
:muted:
:width: 45%
:align: center
:nocontrols:
:controlslist: nofullscreen

:::

When motion for the toes has been measured, for example with a toe marker, the marker can instead be used to drive the bending of the toes. See the <a href="BVH_ToeFlex.html" target="_blank" rel="noopener">BVH driven model with Toe Flexion</a>.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
