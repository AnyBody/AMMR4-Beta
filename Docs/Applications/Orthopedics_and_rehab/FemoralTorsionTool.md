---
gallery_title: "Femoral Torsion Tool"
gallery_image: "/Applications/images/FemoralTorsion.webp"
anylink: Application/Examples/FemoralTorsion/StandingModel.Main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_FemoralTorsionTool.py)=
(example_femoral_torsion)=
# Femoral Torsion Tool

:::{anylink-gallery}
:margin:
:::


This is an example of modifying the femoral torsion of the default
<a href="../../body/leg_tlem2_model.html" target="_blank" rel="noopener">TLEM 2.0</a> leg geometry using a model utility included in the model
repository. The example is based on the simple standing model, with the
femoral torsion set to 20°. It also demonstrates how a similar morphing
approach can be used to personalize other body segments.

The tool was developed by <a href="https://www.linkedin.com/in/enrico-de-pieri-13096a7a" target="_blank" rel="noopener">Enrico De Pieri</a>, from the University of Basel
Children’s Hospital (UKBB), and <a href="https://www.linkedin.com/in/biomedical" target="_blank" rel="noopener">Morten E. Lund</a>, from AnyBody Technology A/S.

This tool generates personalized models that account for subject-specific
values of femoral torsion and supports investigation of the effect of
torsional alignment on hip loading. This work is published in *Frontiers in
Bioengineering and Biotechnology* [^cite_dflm21]. Please cite the article when using this tool.



:::
:::{figure} /Applications/Orthopedics_and_rehab/femoral-torsion.png
:align: center
:width: 80%

The tool works by adding 8 control points around the hip center and knee
center, which control a RBF scale function. The control points are scaled
with the default model scaling, while the femoral torsion is added on top.
:::

:::{figure} /Applications/Orthopedics_and_rehab/femoral-torsion_2.png
:align: center
:width: 80%

The origin and insertion points of the muscles follow the morphed femoral
geometry.
:::

The model tool is a simple include file located in the model repository. It can
be included in any model using the following code:

```AnyScriptDoc
// The femoral torsion tool expects the following variables to be defined
Main.HumanModel.Anthropometrics = {
   AnyVar FemoralTorsionRight = 20;
   AnyVar FemoralTorsionLeft = 20;
};

// This line must be included before the "HumanModel".
#include "<ANYBODY_PATH_MODELUTILS>/FemoralTorsion/Include.any""
```

:::{note}
This tool takes as input the nominal value of femoral torsion that is
to be expected in the final morphed model. It automatically subtracts the
torsional value of the original model’s femoral geometry and introduces a twist
in the transversal plane according to the difference between the two values. The
femoral torsion in the geometry of the unscaled (TLEM 2.0 cadaver) model is
approximately 3.5°, so setting the femoral torsion to 3.5° will
not modify the model. In the original publication, a slightly different
definition of joint axes for the calculation of torsion in the unscaled model
was used, leading to a value of 5.5°. The adjusted value does not alter
the functionality of this tool nor the conclusions of the afore-mentioned
publication.
:::

The Femoral torsion tool uses a functionality override scaling for thigh segments. In this case
the include file sets `#define CUSTOM_SCALING_Right_Thigh` and `#define CUSTOM_SCALING_Left_Thigh` to override the default scaling for the right/left
thigh.

:::{seealso} See the <a href="https://anyscript.org/tutorials/Scaling/lesson2.html" target="_blank" rel="noopener">scaling tutorial</a> for more information on how to use the custom scaling functionality in the general case.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

## Bibliography

[^cite_dflm21]: De Pieri, E., et al. (2021). Subject-specific modeling of femoral torsion influences the prediction of hip loading during gait in asymptomatic adults. *Frontiers in Bioengineering and Biotechnology*, *9*, 679360. <a href="https://doi.org/10.3389/fbioe.2021.679360" target="_blank" rel="noopener">https://doi.org/10.3389/fbioe.2021.679360</a>
