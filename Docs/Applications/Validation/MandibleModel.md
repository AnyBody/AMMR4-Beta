---
gallery_title: "Symmetric Mandible Example"
gallery_image: "/Applications/images/MandibleChewingAndClenching.jpg"
anylink: Application/Validation/MandibleChewingAndClenching/MandibleChewingAndClenching.main.any
---

(sphx_glr_auto_examples_Validation_plot_MandibleModel.py)=
(example_mandiblemodel)=
# Symmetric Mandible Example

:::{anylink-gallery}
:margin:
:::


This example demonstrates a symmetric human mandible model based on a computed tomography scan of a 30-year-old male. It simulates chewing with measured kinematic data and compares the resulting model behavior with experimental measurements from the validation study by de Zee et al.[^dezee2007]

The model uses a three-element Hill muscle model and includes calibration of the mandible muscles. The active configuration drives the incisor point with measured chewing coordinates and applies a simulated chewing force. The study writes the right and left temporomandibular-joint reaction forces to `TMJ_Forces.csv` and includes chart definitions for the model outputs. An alternate clenching configuration using measured kinematics and force is also present in the source file but is commented out in the active setup.

:::{warning}
The chewing force is simulated and may differ substantially from the force in the measured movement. The example is therefore intended as a demonstration rather than a direct reproduction of the chewing experiment. The mandibular fossa is represented by a planar constraint without curvature.
:::


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

## Bibliography

[^dezee2007]: de Zee, M., et al. (2007). Validation of a musculo-skeletal model of the mandible and its application to mandibular distraction osteogenesis. *Journal of Biomechanics*, *40*(6), 1192–1201. <a href="https://doi.org/10.1016/j.jbiomech.2006.06.024" target="_blank" rel="noopener">https://doi.org/10.1016/j.jbiomech.2006.06.024</a>
