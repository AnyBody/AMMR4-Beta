---
gallery_title: "Hand Crank"
gallery_image: "/Applications/images/WheelTurn.webp"
anylink: Application/Examples/WheelTurn/WheelTurn.Main.any
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_WheelTurn.py)=

# Hand Crank

:::{anylink-gallery}
:margin:
:::


This model demonstrates a person turning a horizontal wheel by means of a handle. It is intended for shoulder validation during a constrained hand-cranking task.

The model uses the configured human body model and connects the hand to the wheel handle through the model environment. The study simulates one complete wheel revolution and provides operations for previewing and generating a video of the movement.

The main parameters are defined in `Model/InputParameters.any`:

- `WheelParameters.Hub`: wheel-center position.
- `WheelParameters.Rad`: wheel radius.
- `WheelParameters.Omega`: wheel angular velocity.
- `WheelParameters.M`: applied wheel moment and design variable.
- `ChairParameters.HandRest`: position of the hand rest.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

