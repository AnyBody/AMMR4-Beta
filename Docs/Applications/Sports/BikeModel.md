---
gallery_title: "Bicycle"
gallery_image: "/Applications/images/BikeModel-FullBody.png"
anylink: Application/Examples/BikeModel/BikeModel-FullBody.main.any
---

(sphx_glr_auto_examples_Sports_plot_BikeModel.py)=
(example_bikemodel)=
# Bicycle

:::{anylink-gallery}
:margin:
:::

Bicycle rider model that runs either as
a FullBody or LowerExtremity version.

The model illustrates several important topics in model
construction:

- Block building techniques
- Include files
- Structuring of models using directories
- Modeling of an environment as a mechanism, in this case the bicycle

The human model is included as a block from the Body (BodyRepository) directory.

The model of the bike including bike frame, crank, wheels, definition of
crank moment, etc. can be found in the include file `BikeFrameAndWheels.any`.

The connections between the human model and the bicycle are defined in
`BikeLegConnection.any`.

Bike geometry and riding inputs are defined in `BikeParameters.any`.
The adjustable parameters include pedal arm length and width, saddle height and
horizontal position, cadence, average mechanical output, crank moment at top dead
center and crank-moment phase.

The model can run in two configurations: FullBodyModel and LowerExtremityModel. This
can be changed in the `Config.any` file.

:::{admonition} In Model Repository:
:class: seealso
`Application/Examples/BikeModel`
* Full body model: {anylink-file}`BikeModel-FullBody.main.any <Application/Examples/BikeModel/BikeModel-FullBody.main.any>`
* Lower extremity model: {anylink-file}`BikeModel-LowerBody.main.any <Application/Examples/BikeModel/BikeModel-LowerBody.main.any>`

:::