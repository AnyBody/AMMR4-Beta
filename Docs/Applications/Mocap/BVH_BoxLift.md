---
gallery_title: "BVH-Driven Box Lift"
gallery_image: "/Applications/images/BVH_BoxLift.webp"
anylink: Application/MocapExamples/BVH_BoxLift/Subjects/S01/S01_T01/Main.any
---

(sphx_glr_auto_examples_Mocap_plot_BVH_BoxLift.py)=
(example_bvh_boxlift)=
# BVH-Driven Box Lift


:::{anylink-gallery}
:margin:
:::


This example extends the <a href="BVH.html" target="_blank" rel="noopener">inertial MoCap model</a> with a box-lifting
task driven by data from an inertial measurement unit (IMU) based suit. The model uses a
BVH file with data from an Xsens suit, and the ground reaction forces are predicted using
the GRF prediction algorithm.


The model works using virtual markers placed on the BVH rig (i.e. the stick-figure model
specified by the BVH file). The virtual markers are used to make the Musculoskeletal model
moved similar to marker based MoCap models.

AnyBody automatically calculates the virtual markers positions, and the model is scaled
directly from the size of the BVH stick figure. Hence the model contains no *Parameter
identification* step to find the parameters. The remaining parts of the model are equivalent to other
{ref}`MoCap model <anymocap>`  based on C3D files.

The box is represented by a separate segment whose handles are connected to the palm
joints of both hands. Its position and orientation are calculated from the hand
positions, while a soft constraint keeps the box level with the ground. The box
kinematics are saved after marker tracking and loaded again to drive the box during the
inverse-dynamics study. This allows interaction with an environment object to be
investigated even when no kinematic data for that object is available.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
