---
gallery_title: "Leg Press Machine"
gallery_image: "/Applications/images/LegPressMachine.webp"
anylink: Application/Examples/LegPressMachine/LegPressMachine.main.any
---

(sphx_glr_auto_examples_Sports_plot_LegPressMachine.py)=
(example_legpressmachinemodel)=
# Leg Press Machine

:::{anylink-gallery}
:margin:
:::

A model illustrating a leg press exercise and demonstrating the use of the
SolidModeling Class Template in the AMMR ToolBox. The machine is assembled from
parameterized solid parts and connected to the body through support conditions
at the seat, backrest, and footrest.

The right knee follows an interpolated flexion trajectory, and both feet are
constrained to the footrest.

The main settings are grouped in the model's parameter files:

- Machine dimensions, orientations, and part densities are defined in
	`Model/DesignParameters.any`.
- Contact friction coefficients and support-actuator strengths for the seat,
	backrest, and footrest are defined in `Model/SupportParameters.any`. The
	strengths set the force capacity available to these contact actuators.
- The knee-flexion trajectory and initial body posture are defined in
	`Model/TrialSpecificData.any`.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
