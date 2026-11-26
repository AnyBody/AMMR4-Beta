---
gallery_title: "Trunk Exoskeleton Concept"
gallery_image: "/Applications/images/ExoConceptTrunk_BoxLift.webp"
anylink: Application/Examples/ExoskeletonTrunk/ExoConceptTrunk_BoxLift.main.any
---

(sphx_glr_auto_examples_Other_plot_ExoConceptTrunk_BoxLift.py)=
(example_exo_concept_trunk)=
# Trunk Exoskeleton Concept


:::{anylink-gallery}
:margin:
:::

This is an example of a passive trunk exoskeleton concept.

The model is structured to include the <a href="../Mocap/BVH_BoxLift.html" target="_blank" rel="noopener">BVH_BoxLift model</a> from the AMMR, with the code for the exoskeleton concept then applied to it. This approach avoids duplicating the box-lift model within the AMMR.

In this example of a passive trunk exoskeleton concept, an assistive torque
is applied at the `PelvisThoraxExtension` measure in the `Interface` folder of
the Body Model. The spring stiffness can be set in the `ExoskeletonParameters`
folder in `Main.ModelSetup`.

This simple example illustrates how the effects of an exoskeleton can be
investigated by applying the assistive torque directly at the human body with
a few lines.

:::{note}
To apply the exoskeleton concept to another model, the code from the `ExoConcept` section can simply be copied into the desired model.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
