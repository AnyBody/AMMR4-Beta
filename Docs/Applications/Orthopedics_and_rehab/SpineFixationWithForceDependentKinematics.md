---
gallery_title: "Spine Fixation Using FDK"
gallery_image: "/Applications/images/SpineFixationWithForceDependentKinematics.webp"
anylink: Application/Examples/SpineFixationWithForceDepKinematics/SpineFixationWithForceDependentKinematics.main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_SpineFixationWithForceDependentKinematics.py)=

# Spine Fixation Using FDK


:::{anylink-gallery}
:margin:
:::

This example applies the force-dependent kinematics (FDK) solver to a lumbar
spine with muscles, ligaments, facet-joint contact, and a fixation device
between the L4 and L5 vertebrae. Rather than using the default lumbar spine rhythm, the model
leaves lumbar joint rotations force-dependent so the solver determines them
from the modeled forces while the thorax-pelvis posture is driven through
flexion-extension, lateral bending, and axial rotation.

The starting and ending thorax-pelvis angles and the implant stiffness
coefficient can be changed in `Model/InputParameters.any`.

The position of the spine fixation device can also be changed in `Model/SpineFixation.any`. In this file, it is also possible to change the rotational stiffness of the fixation device. The default value is based on a FE bending analysis of a circular, elastic titanium rod which was fixed on both sides by clamps.

By default, the study exports lumbar joint angles for flexion-extension, axial torsion, and lateral bending
to separate text files, together with the combined thorax-pelvis motion.

:::{note}
The fixation device is intended only as a demonstration of potential developments. It operates only during flexion/extension activities, as its behavior depends on the flexion/extension angle.
:::

:::{admonition} In Model Repository:
:class: seealso

`Application/Examples/SpineFixationWithForceDepKinematics`

{anylink-file}`SpineFixationWithForceDependentKinematics.main.any <Application/Examples/SpineFixationWithForceDepKinematics/SpineFixationWithForceDependentKinematics.main.any>`

:::
