---
gallery_title: "Cross Trainer"
gallery_image: "/Applications/images/CrossTrainer.webp"
anylink: Application/Examples/CrossTrainer/CrossTrainer.main.any
---

(sphx_glr_auto_examples_Sports_plot_CrossTrainer.py)=
(example_crosstrainer)=
# Cross Trainer

:::{anylink-gallery}
:margin:
:::

This example combines a human body model with a cross trainer assembled from a
SolidWorks CAD model. The crank drives the pedals while conditional foot-plate
contacts represent the interaction between the feet and pedals.

The machine motion and resistance are configured in `Model/MachineOperation.any`:

* `T_period` sets the crank cycle period, and `phase_offset` sets its initial
	position.
* The resistance torque varies sinusoidally with crank angle. Its amplitude and offset are set by `coeff_term` and `const_term`

The model is also demonstrated in the AnyBody tutorial
<a href="https://anyscript.org/tutorials/AnyExp4SOLIDWORKS/index.html" target="_blank" rel="noopener">“Making Models using SolidWorks”</a>.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
