---
gallery_title: "Gait Model (Vaughan)"
gallery_image: "/Applications/images/GaitVaughan.webp"
anylink: Application/Validation/GaitVaughan/GaitVaughan.main.any
---

(sphx_glr_auto_examples_Validation_plot_GaitVaughan.py)=

# Gait Model (Vaughan)

:::{anylink-gallery}
:margin:
:::

This example demonstrates a potential validation approach for the gait model by comparing the calculated muscle activity with measured EMG data. The data set used in the example is obtained from the book *Dynamics of Human Gait*. [^dynamics-human-gait] The model uses the “man” data set, which is available from the <a href="https://www.isbweb.org/data/" target="_blank" rel="noopener">ISB Data Resources</a>.

Marker trajectories drive selected model coordinates, and measured force-plate loads are applied at the feet. The inverse-dynamics study calculates muscle activity, which is compared with measured EMG envelopes for the tibialis anterior, gluteus maximus, gluteus medius, rectus femoris, adductor longus, and hamstrings. The post-processing study normalizes each measured and calculated curve to its own peak for comparison.

:::{note}
The marker drivers and input files are configured for the included dataset. A different recording requires compatible marker trajectories, force-plate inputs, and marker-to-model drivers.
:::



:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

## Bibliography

[^dynamics-human-gait]: Vaughan C.L., Davis B.L., O’Connor J.C., *Dynamics of Human Gait*. Human Kinetics; 1992