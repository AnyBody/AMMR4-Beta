---
gallery_title: "Free Posture"
gallery_image: "/Applications/images/FreePostureFullBodyShoulderRhythmStatic.webp"
anylink: Application/Examples/FreePosture/FreePostureFullBodyMove.Main.any
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-freeposture.py)=
(example_freeposture)=
# Free Posture


:::{anylink-gallery}
:margin:
:::

A basic static full-body model standing on a floor.

This model uses the full-body model; most of the body parts are available in the AAUHuman part of the Body directory. The model is grounded at the pelvis, and the posture of the model is controlled through a `mannequin.any` file by means of joint angles.

:::{note}
This application is a starting point for new applications involving the entire body. The model does not contain muscles and is only intended for running kinematic analysis.
:::

The model has several configurations that can be changed in the file `Config.any`.

- `BodyModelSelection` can be set to:
  - "FullBodyModel" for a full-body model.
  - "FullBodySRHand" for a full-body model with a detailed hand and shoulder rhythm.
- `CONFIGURATION2` can be set to:
  - "FreePostureStatic" for a static model in which the joint angles are controlled in the `mannequin.any` file.
  - "FreePostureMove" for a dynamic model controlled through angles that can be set in the `MannequinInterpolation.any` file.

:::{admonition} In Model Repository:
:class: seealso
Models are located in: `Application/Examples/FreePosture/`

* {anylink-file}`FreePostureFullBodyMove.Main.any <Application/Examples/FreePosture/FreePostureFullBodyMove.Main.any>`
* {anylink-file}`FreePostureFullBodyShoulderRhythmMove.Main.any <Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmMove.Main.any>`
* {anylink-file}`FreePostureFullBodyShoulderRhythmStatic.Main.any <Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmStatic.Main.any>`
* {anylink-file}`FreePostureFullBodyShoulderRhythmStatic.Main.any <Application/Examples/FreePosture/FreePostureFullBodyShoulderRhythmStatic.Main.any>`
:::
