---
gallery_title: "Toe Flexion (BVH driven)"
gallery_image: "/Applications/images/BVH_ToeFlex_GM.webp"
anylink: Application/MocapExamples/SpecialFeatures/BVH_Xsens_ToeFlexion.main.any
---

(sphx_glr_auto_examples_Mocap_plot_BVH_toe_flexion.py)=
(example_mocap_bvh_toe_flexion)=
# Toe Flexion (BVH driven)

:::{anylink-gallery}
:margin:
:::

This model is a variant of the <a href="BVH.html" target="_blank" rel="noopener">Inertial MoCap (Xsens) example</a> and
demonstrates toe flexion.

In this example, the left and right foot are treated differently for the user to see the different
options for toe flexion. The left foot uses the measured motion data to drive the bending of
the toes, while the right foot uses the 
<a href="../../tools/class-templates/Utilities.Kinematic%20limits.RotationPenetrationCombiDriver_template.html" target="_blank" rel="noopener">RotationPenetrationCombiDriver</a>
class template to keep the toes in the neutral position normally and bend them to prevent the 
penetration between toes and ground.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
