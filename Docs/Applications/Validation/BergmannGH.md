---
gallery_title: "Shoulder Model (Bergmann)"
gallery_image: "/Applications/images/BergmannGH.webp"
anylink: Application/Validation/BergmannGH/BergmannGH.Main.any
---

(sphx_glr_auto_examples_Validation_plot_BergmannGH.py)=

# Shoulder Model (Bergmann)

:::{anylink-gallery}
:margin:
:::

This example models right-arm abduction with a 2 kg dumbbell. The model is used to assess the fidelity of the shoulder model by comparing the computed glenohumeral (GH) joint reactions with in vivo measurements reported by Bergmann et al. in the *Journal of Biomechanics*. [^bergmann-2007]

The pelvis is fixed to the ground while the arm follows an abduction movement
based on the experimental protocol. A hand constraint keeps the movement in the
frontal plane. The `GHReactionInHumerus` output reports the resultant
glenohumeral joint reaction in humeral coordinates, matching the reference
frame used for the experimental force measurements.

:::{warning}
A documented comparison between the predicted joint reactions and the study measurements is not provided. Therefore, the example demonstrates a comparison setup rather than validated agreement with the experimental measurements.
:::


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}`Application/Validation/BergmannGH/BergmannGH.Main.any`

:::

## Bibliography

[^bergmann-2007]: Bergmann, G., et al. (2007). In vivo glenohumeral contact forces—Measurements in the first patient 7 months postoperatively. *Journal of Biomechanics*, *40*(10), 2139–2149. <a href="https://doi.org/10.1016/j.jbiomech.2006.10.037" target="_blank" rel="noopener">https://doi.org/10.1016/j.jbiomech.2006.10.037</a>
