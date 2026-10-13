---
gallery_title: "Arm Curl"
gallery_image: "/Applications/images/ArmCurl.webp"
anylink: Application/Examples/ArmCurl/ArmCurl.Main.any
---

(sphx_glr_auto_examples_Sports_plot_ArmCurl.py)=

# Arm Curl

:::{anylink-gallery}
:margin:
:::


This example uses the full-body model to simulate an arm curl on a fitness
machine. It compares an adjusted cable-wheel eccentricity with a
zero-eccentricity configuration to show how wheel geometry can account for
changing arm-muscle moment arms during elbow flexion.

The default setup includes `Model/EnvironmentOptimized.any`. Replacing it with
`Model/Environment.any` selects the zero-eccentricity configuration.

:::{note}
The adjusted wheel geometry is preconfigured; the repository does not include
the optimization procedure used to obtain it. It is not possible to obtain a completely constant muscle effort with only the eccentricity as parameter. However, if more parameters were introduced into an actual design optimization, then it is likely that an almost completely uniform effort profile could be obtained.
:::


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
