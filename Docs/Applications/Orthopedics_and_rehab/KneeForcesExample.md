---
gallery_title: "Estimation of Knee Forces"
gallery_image: "/Applications/images/KneeForceExample.webp"
anylink: Application/Examples/KneeForcesExample/Knee_force_example.main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_KneeForcesExample.py)=
(example_knee_forces_estimate)=
# Estimation of Knee Forces

:::{anylink-gallery}
:margin:
:::


Example of calculating the medial/lateral knee force from the total force and moment.

Most musculoskeletal models represent the knee joint as a simplified revolute joint. However, the medial and lateral femoral condyle contact forces acting on the tibial plateau can still be estimated.

:::{caution}
The medial and lateral knee forces calculated here are only crude
estimates of the actual knee condyle contact force.
:::

This example demonstrates how to determine the knee reaction forces and moments and resolve them into two equivalent forces representing the medial and lateral knee force components acting from the femur onto the tibial tray.

:::
:::{figure} /Applications/Orthopedics_and_rehab/knee_forces.svg
:align: center
:width: 50%
The vertical knee force with regards to the shank and the knee moment in the shank frontal plane is decomposed into a lateral and medial force component.
:::

The vertical knee force with regards to the shank and the knee moment in the
shank frontal plane is decomposed into a lateral and medial force component.
These forces can be thought of as a representation of the knee condyle forces on
the tibial plateau.

The figure above shows the concept. The relationship between the forces and moment can be expressed as:

$$
F_{total} = F_{med} + F_{lat}

M_{total}= F_{med}\cdot  l_{med} - F_{lat}\cdot l_{lat}
$$

From the above equations we can find the medial and lateral knee forces:

$$
F_{lat} = \left( F_{total}\cdot l_{med} - M_{total} \right) / \left( l_{lat} + l_{med} \right)

F_{med} = F_{total} - F_{lat}
$$

The model shows how this can be added to any model and walks through the AnyScript code.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::