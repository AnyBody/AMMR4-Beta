---
gallery_title: "Aalborg Mandible Model"
gallery_image: "/Applications/images/AalborgMandibleValidation.webp"
anylink: Application/Validation/AalborgMandibleValidation/Trials/ChewingClockwisePref0001/AnalysisFreeMovement.any
---

(sphx_glr_auto_examples_Validation_plot_AalborgMandible.py)=
(example_aalborgmandible)=
# Aalborg Mandible Model

:::{anylink-gallery}
:margin:
:::

This is a validation example of a mandible model based on the CT scan of a 40-year-old male.

The model was developed for two purposes:

1. Demonstration of how to apply force-dependent kinematics (FDK) for the modeling of
   the temporomandibular joint (TMJ)
2. Validation of the predicted mandible kinematics with the FDK TMJ model and
   comparison to a simpler point-on-plane (POP) model.

More information about the model and the validation can be found in [^cite_andersen].
The work was supported by the Sapere Aude program of the Danish Council for
Independent Research under grant number: DFF-4184-00018.

## How to run the model

Under the Trials folder, there are six folders with the recorded trials. One of
these is a static reference trial (Static0001), which is used to register the
brace to the CT scan. This model can be run by loading the
file `AnalysisFreeMovement.any` and runnig the operation "AnalysisMandible". The
results of this are saved in text files in the folder and used by the other
trials.

In the remaining trial folders, there are four AnyScript files:

- `TrialSpecificData.any`
- `AnalysisFreeMovement.any`
- `AnalysisPlanar.main.any`
- `AnalysisFDK.main.any`

The `TrialSpecificData.any` file contains information about the trial to analyse
including start and end times.

The three other files are all loadable and are used to run the model with
no TMJ model (`AnalysisFreeMovement.any`), with the POP joint model
(`AnalysisPlanar.main.any`) or with the FDK TMJ model (`AnalysisFDK.main.any`). To run each of
these, load the main file and run the operation "AnalysisMandible".

If you have any questions or comments, please do not hesitate to contact the [authors](mailto:msa@mp.aau.dk).

:::{admonition} In Model Repository:
:class: seealso
{file}`Application/Validation/AalborgMandibleValidation`

* {anylink-file}`ChewingClockwisePref0001/AnalysisFDK.main.any <Application/Validation/AalborgMandibleValidation/Trials/ChewingClockwisePref0001/AnalysisFDK.main.any>`
* {anylink-file}`ChewingClockwisePref0001/AnalysisFreeMovement.any <Application/Validation/AalborgMandibleValidation/Trials/ChewingClockwisePref0001/AnalysisFreeMovement.any>`
* {anylink-file}`ChewingClockwisePref0001/AnalysisPlanar.main.any <Application/Validation/AalborgMandibleValidation/Trials/ChewingClockwisePref0001/AnalysisPlanar.main.any>`

:::

## Bibliography

[^cite_andersen]: Andersen, M. S., De Zee, M., Damsgaard, M., Nolte, D., & Rasmussen, J. (2017). Introduction to Force-Dependent Kinematics: Theory and Application to mandible Modeling. *Journal of Biomechanical Engineering*, *139(9)*. <a href="https://doi.org/10.1115/1.4037100" target="_blank" rel="noopener">https://doi.org/10.1115/1.4037100</a>