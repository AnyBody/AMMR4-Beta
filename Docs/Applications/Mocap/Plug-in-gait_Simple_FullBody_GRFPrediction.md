---
gallery_title: "GRF Prediction"
gallery_image: "/Applications/images/GRFPrediction-Plug-in-gait.jpg"
anylink: Application/MocapExamples/Plug-in-gait_Simple/FullBody_GRFPrediction.main.any
---

(sphx_glr_auto_examples_Mocap_plot_Plug-in-gait_Simple_FullBody_GRFPrediction.py)=
(example_mocap_grf_prediction)=

# GRF Prediction

:::{anylink-gallery}
:margin:
:::


Example of a full-body MoCap model using the Plug-in-Gait marker protocol and
walking data without force plates. The external forces are predicted using the
GRF algorithms.


Motion capture data is often recorded without force plates. In traditional
inverse dynamics, this would make it impossible to perform a dynamic analysis.
However, AnyBody has the possibility to predict ground reaction forces (GRF), so
you can make inverse dynamics models based on recorded motion without GRF force
measurement (Fluit et al., 2014 [^fluit2014]; Jung et al., 2014 [^jung2014]).

More information is available in the <a href="../../grf_prediction/grf-prediction.html" target="_blank" rel="noopener">documentation for the GRF prediction</a>.

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::

## Bibliography

[^fluit2014]: Fluit, R., Andersen, M. S., Kolk, S., Verdonschot, N., & Koopman, H. (2014). Prediction of ground reaction forces and moments during various activities of daily living. *Journal of Biomechanics*, *47*(10), 2321–2329. <a href="https://doi.org/10.1016/j.jbiomech.2014.04.030" target="_blank" rel="noopener">https://doi.org/10.1016/j.jbiomech.2014.04.030</a>
[^jung2014]: Jung, M., Lee, Y., Koo, S., & Lee, K. (2014). Ground reaction force estimation using an insole-type pressure mat and joint kinematics during walking. *Journal of Biomechanics*, *47*(11), 2693–2699. <a href="https://doi.org/10.1016/j.jbiomech.2014.05.007" target="_blank" rel="noopener">https://doi.org/10.1016/j.jbiomech.2014.05.007</a>
