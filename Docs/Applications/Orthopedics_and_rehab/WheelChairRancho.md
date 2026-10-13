---
gallery_title: "Wheelchair"
gallery_image: "/Applications/images/WheelChairRancho.webp"
anylink: Application/Examples/WheelChairRancho/WheelChairRancho.Main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_WheelChairRancho.py)=

# Wheelchair


:::{anylink-gallery}
:margin:
:::

This example models a person propelling a wheelchair. The model is driven by motion capture
data provided by <a href="https://www.linkedin.com/in/philip-requejo-phd-557b5826/?isSelfProfile=false" target="_blank" rel="noopener">Philip S. Requejo Ph.D.</a> (Pathokinesiology Laboratory, Rancho Los Amigos National Rehabilitation Center). The modeled body includes the trunk
and right arm; the left arm and both legs are disabled.

The marker trajectories are loaded from a C3D file, which also contains the force data between the right hand and the wheel rim along three directions:
- anterior/posterior (`WHLCHRFX`)
- medial/lateral (`WHLCHRFY`)
- vertical (`WHLCHRFZ`)

The C3D file also contains the EMG data of five muscles (anterior deltoid, infraspinatus, medial deltoid, rhomboid, supraspinatus) recorded during the trials. 

Further information regarding the model can be found in the PowerPoint presentation "WC_FBD.ppt" in `Input/Rancho_WC_data`.

:::{note}
The chair dimensions can be modified in `Model/InputParameters.any`. However, these changes only affect the model's visual appearance.
:::

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
