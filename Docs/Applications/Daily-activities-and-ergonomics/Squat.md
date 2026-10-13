---
gallery_title: "Squat"
gallery_image: "/Applications/images/Squat.webp"
anylink: Application/Examples/Squat/Squat.main.any
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_Squat.py)=
(example_squat)=
# Squat

:::{anylink-gallery}
:margin:
:::


This model demonstrates a parameterized squatting motion using the default human model with the TLEM leg model. The posture is prescribed by the mannequin drivers, while conditional foot contacts predict the ground reaction forces during the movement.


The following parameters can be changed in `Input/Parameters.any`:

* Time period of a squat cycle
* FPS (frames per second) for simulation
* Minimum and maximum knee flexion angle of a squat cycle (in degrees)
* Distance between the two medial contact nodes of both feet (in meters)
* Rotation angle of both feet (in degrees)

The ground reaction force (GRF) prediction is implemented in `Model/Supports.any` using conditional foot contact. The parametric posture and movement drivers are defined in `Model/JointsAndDrivers.any`.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
