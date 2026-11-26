---
gallery_title: "Facet Joint"
gallery_image: "/Applications/images/FacetJointModel.webp"
anylink: Application/Examples/FacetJointModel/FacetJointModel.main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_FacetJointModel.py)=

# Facet Joint

:::{anylink-gallery}
:margin:
:::

This model presents a methodology for implementation of facet joints in the
lumbar spine model developed by De Zee et al. [^de-zee-2007]. It enables the
facet joint forces to become part of a redundant system of equilibrium
equations for the entire system including the muscles. This redundant system is
subsequently solved uniquely thereby making it possible to analyze the effect of
whole body movements and loads on facet joint loading for the whole lumbar spine
together with its muscles.

More details can also be found in the webcast
<a href="https://www.anybodytech.com/download/implementation-of-facet-joints-in-a-lumbar-spine-model/" target="_blank" rel="noopener">Implementation of facet joints in a lumbar spine model - AnyBody Technology</a>.

:::{note}
For dynamic analyses, this model should be used with care because the facet joint
forces may add energy to the mechanical system.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::

## Bibliography

[^de-zee-2007]: De Zee, M., Dalstra, M., Cattaneo, P. M., Rasmussen, J., Svensson, P., & Melsen, B. (2007). A generic detailed rigid-body lumbar spine model. *Journal of Biomechanics*, *40*(6), 1219–1227. <a href="https://doi.org/10.1016/j.jbiomech.2006.05.030" target="_blank" rel="noopener">https://doi.org/10.1016/j.jbiomech.2006.05.030</a>
