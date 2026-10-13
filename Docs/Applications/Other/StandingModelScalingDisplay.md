---
gallery_title: "Scaling Laws"
gallery_image: "/Applications/images/StandingModelScalingDisplay.webp"
anylink: Application/Examples/StandingModelScalingDisplay/StandingModelScalingDisplay.Main.any
---

(sphx_glr_auto_examples_Other_plot_StandingModelScalingDisplay.py)=

# Scaling Laws


:::{anylink-gallery}
:margin:
:::

This application shows all the scaling laws available.

The selected law is set with `BM_SCALING`; if it is not defined, the model uses standard scaling, corresponding to the 50th-percentile European male.

The available choices are:

* No scaling (`_SCALING_NONE_`).
* Uniform, length-mass, or length-mass-fat scaling (`_SCALING_UNIFORM_`, `_SCALING_LENGTHMASS_`, or `_SCALING_LENGTHMASSFAT_`), based on joint-to-joint measurements.
* XYZ scaling (`_SCALING_XYZ_`), using scale factors along the X, Y, and Z axes.

For further details, see <a href="../../Scaling/intro.html" target="_blank" rel="noopener">the tutorial about scaling</a>.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
