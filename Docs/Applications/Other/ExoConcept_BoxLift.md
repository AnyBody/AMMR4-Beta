---
gallery_title: "Exoskeleton Concepts"
gallery_image: "/Applications/images/ExoConcept_BoxLift.webp"
anylink: Application/Examples/ExoskeletonConcept/ExoConcept_BoxLift.main.any
---

(sphx_glr_auto_examples_Other_plot_ExoConcept_BoxLift.py)=
(example_exo_concept_boxlift)=
# Exoskeleton Concepts

:::{anylink-gallery}
:margin:
:::

This example shows how to study different exoskeleton concepts during a box-lifting activity. The model is
based on the [webcast](https://www.anybodytech.com/webcasts/simulation-driven-conceptual-design-of-exoskeletons/){target="_blank"}
presented by [Prof. John Rasmussen](https://vbn.aau.dk/da/persons/jr/){target="_blank"}
from Aalborg University on March 28, 2022.

The model points to the existing <a href="../Mocap/BVH_BoxLift.html" target="_blank" rel="noopener">BVH Box Lift model</a>
in the AMMR and implements the different steps described in the webcast. The `EXO_CONCEPT` macro selects the
configuration to study either:

- Rotational springs at the knees or
- Extensible rods crossing the knees, hips and lumbar spine.

For each concept, you can apply idealized forces through `AnyReacForce`. The idealized
forces are like hypothetical actuators that will provide as much force as is needed by the system. This approach can be used to investigate the required assistive force and its relationship with kinematic variables, such as joint angles. Subsequently, the required assistive forces can be used to design spring-based assistance, with the spring characteristics determined from the idealized forces required at the respective joints.

Thus, four configurations are considered in this model:
 1. Idealized forces applied at the knees
 2. Spring forces applied at the knees
 3. Idealized extensible rods crossing the knees, hips and lumbar spine
 4. Spring force-based extensible rods crossing the knees, hips and lumbar spine.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
