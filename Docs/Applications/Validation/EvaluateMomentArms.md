---
gallery_title: "Evaluation of Moment Arms"
gallery_image: "/Applications/images/EvaluateMomentArms.webp"
anylink: Application/Validation/EvaluateMomentArms/EvaluateMomentArms.main.any
---

(sphx_glr_auto_examples_Validation_plot_EvaluateMomentArms.py)=
(example_evaluate_momentarms)=
# Evaluation of Moment Arms


:::{anylink-gallery}
:margin:
:::

This model shows how to enable the built-in moment arm evaluation studies.
The studies can be enabled by setting the switch: `#define EVALUATE_MOMENT_ARMS 1`.

The studies will appear in the `HumanModel.EvaluateMomentArms` folder.

:::{figure} /Applications/Validation/EvalMomentArms_plot.png
:align: center

The moment arms (in meters) of the Iliacus and GluteusMaximus (inferior) during hip flexion.
Agonist muscles (e.g. Iliacus) have positive moment arms, while anatagonist muscles (e.g. GluetusMaximus) have negative moment arms.
:::

:::{note}
Enabling moment arm evaluations will include a significant number of studies (one per DoF), which will affect performance when loading and switching between tabs/operations.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
