---
gallery_title: "Bicycle (2D)"
gallery_image: "/Applications/images/BikeModel2D.png"
anylink: Application/Examples/BikeModel2D/BikeModel2D.main.any
---

(sphx_glr_auto_examples_Sports_plot_BikeModel2D.py)=

# Bicycle (2D)

:::{anylink-gallery}
:margin:
:::


This example is a simplified, 2D version of the <a href="BikeModel.html" target="_blank" rel="noopener">bike model</a>. It combines a planar lower-extremity model with a bicycle frame, crank, and wheels to simulate pedaling. Its operation sequence runs an inverse
dynamics analysis with prescribed crank motion, pedal motion, and an applied
crank moment.

Bike geometry and riding inputs are defined in `Main.BikeParameters` in
`BikeModel2D.main.any`. These include pedal-arm dimensions, saddle position,
cadence, and average mechanical output. Changing these parameters allows the
effects of bicycle setup and riding conditions on the inverse dynamics analysis
to be examined.

:::{note}
The legs are modeled in the sagittal plane with a limited set of muscles. The
bicycle and model can be oriented in 3-D space, but this does not add 3-D
biomechanics to the planar leg model.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
