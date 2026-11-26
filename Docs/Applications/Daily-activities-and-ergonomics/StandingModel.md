---
gallery_title: "Standing Model"
gallery_image: "/Applications/images/StandingModel.webp"
anylink: Application/Examples/StandingModel/StandingModel.Main.any
---

(sphx_glr_auto_examples_ADLs_and_ergonomics_plot_StandingModel.py)=
(example_standingmodel)=
# Standing Model

:::{anylink-gallery}
:margin:
:::

A full-body model that uses center of mass (CoM) drivers to keep balance and ground reaction force (GRF) prediction for contact with the ground.

The model has the following features which makes it a good starting point for creating new models:

- Uses soft default mannequin constraints.
- The ankle drivers have lower weights, so the ankle angles are adjusted primarily to balance the CoM over the feet.
- Uses ground reaction force prediction for contact with the ground.
- Hard constraints between both feet and the ground, e.g. feet don't move.
- Foot constraints can be removed with `EXCLUDE_FOOT_CONSTRAINTS` to customize the model.
- The CoM balance driver can be removed with `EXCLUDE_COM_BALANCE_DRIVERS`.
- The foot and CoM positions can be specified in the main file.

The model is identical to the standing model created with the template generator in the AnyBody Modeling System.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::

