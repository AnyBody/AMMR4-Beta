---
gallery_title: "Total Hip Arthroplasty"
gallery_image: "/Applications/images/THA-KneeBendDemo.webp"
anylink: Application/Examples/THA-KneeBendDemo/THA-KneeBendDemo.Main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_THA-KneeBendDemo.py)=

# Total Hip Arthroplasty (THA) Model


:::{anylink-gallery}
:margin:
:::

This is a demo model for the simulation of knee bending in case of a body model
with total hip arthroplasty (THA) using:

- either an ideal spherical joint with joint reaction forces
- or force dependent kinematics and a contact model.

In the body model, the right hip joint is excluded from the AnyBodyStudy and a new
force dependent hip joint is included. Therefore, an acetabular cup and a femoral
component (provided by [Edmundo Fuentes](https://www.edmundofuentes.com/about/){target="_blank"} via [https://grabcad.com/](https://grabcad.com/){target="_blank"}) are included into the model and a contact force between these
implants is defined. For stabiliy reasons, an artifical spring is implemented to
avoid the joint to disconnect.

:::{warning}
Please notice that this simulation is only a demo example. The placement of the
implant is not based on any anatomical data. Further, the implant includes an
artificial spring (in `Model/ContactForces.any`) element to make the simulation
more robust. For each simulation, the force produced by this artifical spring
should be checked to be aware of the influence of this spring on the results.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::

