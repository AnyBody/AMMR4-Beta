---
gallery_title: "Standing Lift"
gallery_image: "/Applications/images/StandingLift.webp"
anylink: Application/Examples/StandingLift/StandingLift.main.any
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingLift.py)=
(example_standinglift)=
# Standing Lift

:::{anylink-gallery}
:margin:
:::

This example extends the <a href="StandingModel.html" target="_blank" rel="noopener">Standing Model</a> with a box to demonstrate lifting from a standing posture. Non-sticking contact between the feet and the floor, and between the hands and the box, is represented with artificial reaction muscles.

The body posture and box trajectory are defined in
`Model/JointsAndDrivers.any`, which can be adapted when developing related
full-body applications.

:::{note}
This model can also output computed forces to be used by FEA. For more details, see the <a href="https://anyscript.org/tutorials/Finite_element_analysis/index.html" target="_blank" rel="noopener">Finite Element Analysis Interfacing</a> tutorial.
:::

:::{admonition} In Model Repository:
:class: seealso
`Application/Examples/StandingLift`

* {anylink-file}`StandingLift.main.any <Application/Examples/StandingLift/StandingLift.main.any>`
* {anylink-file}`StandingLiftFEA.main.any <Application/Examples/StandingLift/StandingLiftFEA.main.any>`

:::
