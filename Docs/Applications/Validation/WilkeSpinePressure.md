---
gallery_title: "Spine Disc Pressure"
gallery_image: "/Applications/images/SpinePressureStanding.webp"
anylink: Application/Validation/WilkeSpinalDiscPressure/SpinePressureSeatingRelaxed/SpinePressureSeatingRelaxed.main.any
---

(sphx_glr_auto_examples_Validation_plot_WilkeSpinePressure.py)=
(example_wilkespinepressure)=
# Spine Disc Pressure

:::{anylink-gallery}
:margin:
:::


This validation application compares intradiscal pressure at the L4–L5 disc across eight postures with in vivo measurements from the same trial.[^wilke1999] [^wilke2001]

The models use a uniformly scaled human model with the TLEM leg model. Each main file defines a posture-specific environment and runs muscle calibration followed by inverse dynamics. The study exposes reaction-force magnitudes at the L5–sacrum and L4–L5 joints for comparison with the measured data.

## Posture variants

The variants cover standing, sitting, lying, and lifting conditions. The images below show the corresponding model configurations; use the repository entry point to open the individual `.any` files.

::::{grid} 1 2 3 4
:gutter: 3

:::{grid-item-card} **Relaxed standing**
![Relaxed standing](/Applications/images/SpinePressureStanding.webp)
:::

:::{grid-item-card} **Lying on the back**
![Lying on the back](/Applications/images/SpinePressureLyingOnBack.webp)
:::

:::{grid-item-card} **Relaxed sitting**
![Relaxed sitting](/Applications/images/SpinePressureSeatingRelaxed.webp)
:::

:::{grid-item-card} **Erect sitting without back support**
![Erect sitting without back support](/Applications/images/SpinePressureSeatingStraitNoSupport.webp)
:::

:::{grid-item-card} **Standing, flexed forward**
![Standing, flexed forward](/Applications/images/SpinePressureStandingFlexed.webp)
:::

:::{grid-item-card} **Standing while holding a load close**
![Standing while holding a load close](/Applications/images/SpinePressureStandingLiftClose.webp)
:::

:::{grid-item-card} **Lifting with a flexed back**
![Lifting with a flexed back](/Applications/images/SpinePressureStandingLiftFlexed.webp)
:::

:::{grid-item-card} **Lifting with the arms extended**
![Lifting with the arms extended](/Applications/images/SpinePressureStandingLiftStretchedArms.webp)
:::

::::

The comparison is normalized to the reaction forces from `SpinePressureStanding.Main.any` in the relaxed-standing condition to show trends across postures.

```{figure} /Applications/Validation/wilke.svg
:alt: Comparison of measured and modelled intradiscal pressure across the Wilke postures
:width: 100%

Comparison of the Wilke intradiscal-pressure measurements and model results across the posture variants.
```


:::{admonition} In Model Repository:
:class: seealso
`Application/Validation/WilkeSpinalDiscPressure`

* {anylink-file}`SpinePressureSeatingRelaxed.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureSeatingRelaxed/SpinePressureSeatingRelaxed.main.any>`

* {anylink-file}`SpinePressureLyingOnBack.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureLyingOnBack/SpinePressureLyingOnBack.main.any>`

* {anylink-file}`SpinePressureSeatingStraitNoSupport.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureSeatingStraitNoSupport/SpinePressureSeatingStraitNoSupport.main.any>`

* {anylink-file}`SpinePressureStanding.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureStanding/SpinePressureStanding.Main.any>`

* {anylink-file}`SpinePressureStandingFlexed.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureStandingFlexed/SpinePressureStandingFlexed.Main.any>`

* {anylink-file}`SpinePressureStandingLiftClose.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureStandingLiftClose/SpinePressureStandingLiftClose.main.any>`

* {anylink-file}`SpinePressureStandingLiftFlexed.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureStandingLiftFlexed/SpinePressureStandingLiftFlexed.main.any>`

* {anylink-file}`SpinePressureStandingLiftStretchedArms.main.any <Application/Validation/WilkeSpinalDiscPressure/SpinePressureStandingLiftStretchedArms/SpinePressureStandingLiftStretchedArms.main.any>`

:::

## Bibliography

[^wilke1999]: Wilke, H.-J., et al. (1999). New in vivo measurements of pressures in the intervertebral disc in daily life. *Spine*, *24*, 755–762. <a href="https://doi.org/10.1097/00007632-199904150-00005" target="_blank" rel="noopener">https://doi.org/10.1097/00007632-199904150-00005</a>
[^wilke2001]: Wilke, H.-J., et al. (2001). Intradiscal pressure together with anthropometric data: A data set for the validation of models. *Clinical Biomechanics*, *16*(Suppl. 1), S111–S126. <a href="https://doi.org/10.1016/S0268-0033(00)00103-0" target="_blank" rel="noopener">https://doi.org/10.1016/S0268-0033(00)00103-0</a>



