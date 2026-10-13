---
gallery_title: "Evaluation of Max External Loading"
gallery_image: "/Applications/Validation/EvaluateMaxLoadPlot.png"
anylink: Application/Validation/EvaluateMaxExternalLoading/EvalMaxLoad.main.any
---

(example_evaluate_max_load)=
# Evaluation of Max External Loading

:::{anylink-gallery}
:margin:
:::

This model shows how to use the `EvaluateMaxLoad` class-template to estimate
the maximum loading where `MaxMuscleActivity` reaches 1.

The `EvaluateMaxLoad` class-template requires an argument specifying the study, as well as a pointer to the variable that controls the loading. This variable can be anything, as long as it controls some external force or moment of the model.

In this example, the hand crank model is imported and `EvaluateMaxLoad` is used to evaluate the maximum torque the model can provide at every timestep in the study. This is done by setting the pointer of `EvaluateMaxLoad` to the variable representing the hand wheel torque.

:::{Note}
The tool asumes a linear relationship betweeen the external load and the
maximum muscle activity. This is almost always the case, but it is woth considering if
this assumption holds.
See [this blog post](https://anyscript.org/tools/estimating-maximum-model-strength/){target="_blank"} for more details.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
