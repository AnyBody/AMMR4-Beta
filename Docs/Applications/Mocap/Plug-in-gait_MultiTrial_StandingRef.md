---
gallery_title: "Multi-Trial MoCap"
gallery_image: "/Applications/images/Plug-in-gait_Squat_Flywheel.webp"
anylink: Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef/Subjects/S1/S1_FlywheelSquat/Main.any
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_MultiTrial_StandingRef.py)=
(example_mocap_multitrial)=

# Multi-Trial MoCap

:::{anylink-gallery}
:margin:
:::

Example of a MoCap model structured for analyzing data from multiple subjects
and trials. This special structure makes it much easier to work with large
datasets with multiple subjects and trials. Hence, this model is the best
starting point for analyzing bigger MoCap experiments.

This example shows the <a href="../../anymocap/index.html" target="_blank" rel="noopener">AnyMoCap framework</a> applied to a set of squatting trials. The subject-specific scaling and marker optimization is done on a standing reference recording, and the values are then applied to a squatting trial.

The files are structured so each trial has its own folder with a main file
(`Main.any`) and a file with trial-specific data (`TrialSpecificData.any`).
The C3D files are placed together in a separate folder.

The data was provided by Maria Jönsson from KTH (Royal Institute of Technology, School of Technology and Health) in Sweden.

## Model structure

The model is structured as outlined below:

```{code-block} none
:emphasize-lines: 8,21,24,25

Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef
 │   libdef.any
 │   C3DSettings.any
 │   BodyModelConfig.any
 │   ExtraDrivers.any
 │   ForcePlates.any
 │   MarkerProtocol.any
 │   LabSpecificData.any
 │
 ├───c3d_files\
 |      S1_FlywheelSquat.c3d
 |      S1_StandingRef.c3d
 |      S2_FlywheelSquat.c3d
 |      S2_StandingRef.c3d
 │
 ├───Output\
 │
 └───Subjects\
     │
     ├───S1\
     │   |   SubjectSpecificData.any
     |   |
     │   ├───S1_FlywheelSquat\
     |   |      Main.any
     |   |      TrialSpecificData.any
     |   |
     │   └───S1_StandingRef\
     |          Main.any
     |          TrialSpecificData.any
     │
     └───S2\
         |   SubjectSpecificData.any
         |
         ├───S2_FlywheelSquat\
         |      Main.any
         |      TrialSpecificData.any
         |
         └───S2_StandingRef\
                Main.any
                TrialSpecificData.any
```

:::{admonition} In Model Repository:
:class: seealso
`Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef`

* Standing reference: {anylink-file}`Subjects/S1/S1_StandingRef/Main.any <Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef/Subjects/S1/S1_StandingRef/Main.any>`
* Dynamic trial: {anylink-file}`Subjects/S1/S1_FlywheelSquat/Main.any <Application/MocapExamples/Plug-in-gait_MultiTrial_StandingRef/Subjects/S1/S1_FlywheelSquat/Main.any>`

:::