---
gallery_title: "Evaluation of Joint Strength"
gallery_image: "/Applications/images/EvaluateJointStrength.webp"
anylink: Application/Validation/EvaluateJointStrength/EvaluateJointStrength.main.any
---

(sphx_glr_auto_examples_Validation_plot_EvaluateJointStrength.py)=
(example_evaluate_joint_strength)=
# Evaluation of Joint Strength

:::{anylink-gallery}
:margin:
:::

This model shows how to enable the built-in studies to evaluate joint strength.
The studies can be enabled by setting the switch: `#define EVALUATE_JOINT_STRENGTH 1`.

The studies will appear in the `HumanModel.EvaluateJointStrength`
folder.

:::{figure} /Applications/Validation/EvalJointStrength_model_tree.png
:align: center
:::

:::{note}
Currently, joint strength studies are available only for the arm and leg models.
:::

:::{note}
Enabling joint strength evaluations will include a significant number of studies (two per DoF), which will affect performance when loading and switching between tabs/operations.
:::


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

