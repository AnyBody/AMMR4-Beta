---
gallery_title: "Knee Simulator"
gallery_image: "/Applications/images/KneeSimulator.webp"
anylink: Application/Examples/KneeSimulator/Main.any
---

(sphx_glr_auto_examples_Orthopedics_and_rehab_plot_KneeSimulator.py)=
(example_kneesimulator)=
# Knee Simulator


:::{anylink-gallery}
:margin:
:::

Model of a knee simulator using a knee implant model and force-dependent kinematics (FDK).
For an in-depth description of the mathematics and mechanics behind FDK please see [^cite_azdn17].

:::{note}
Please note that this simulation is only a demo example.
:::

This is a demo model of a knee simulator device resembling the principles of the Kansas Knee simulator [^cite_hcmt10].
The model is constructed as a stand-alone model and does not use any elements or body parts from the model repository (AMMR).
Data for the total knee replacement (TKR) implant comes from the [6th Grand Challenge Competition to Predict In Vivo Knee Loads](https://simtk.org/projects/kneeloads){target="_blank"}.

## Segments

The model is constructed of five main segments (femur, patella, tibia, ankle-fixture, and hip-fixture).
In practice, more segments are included. The mass of the femur/tibia is implemented as separate segments
for easier specification of the moments of inertia. Likewise, the trans-spherical mechanism between ankle
and ground segments is implmented using three segments connected with revolute and slider joints.

:::{figure} /Applications/images/KneeSimulator_Full.jpg
:align: center
:width: 60%

Overview of the knee simulator.
:::

## Ligaments

The ligaments are modeled using one-dimensional, nonlinear elastic spring elements. In order to prevent
ligaments from penetrating the bone/implant surfaces, they were wrapped around various geometrical shapes (cylinder, ellipsoid,...).
Ligament properties (stiffness and reference strains) were adopted from the literature [^cite_bkhg91] [^cite_mvfk15].

:::{figure} /Applications/images/KneeSimulator_Ligaments.jpg
:align: center
:width: 60%

Ligaments in the model, abbreviations adopted from [^cite_sbtp06] (Figure 1).
:::

## Contacts

Three STL-based rigid-rigid contact models were defined: between the patella and femoral component,  the femoral component and tibia insert (lateral side),
and the femoral component and tibia insert (medial side).

```{figure} /Applications/images/KneeSimulator_Contacts.jpg
:align: center
:width: 60%

Contact surfaces in the model.
```

## Settings

Model settings can be added and removed here: `UserDefinedSettings.Main.any`. To use FDK define:

```AnyScriptDoc
#define USE_FDK 1
```

Other adjustable settings include: ligament parameters, femur and tibia mass ratios, load applied to the hip fixture and desired knee flexion.

```AnyScriptDoc
#define DEF_KNEE_FLEXION_MIN 10
#define DEF_KNEE_FLEXION_MAX 60

#define DEF_HIP_AXIAL_LOAD_MIN 200
#define DEF_HIP_AXIAL_LOAD_MAX 200

#define FEMUR_MASS_RATIO 0.135
#define TIBIA_MASS_RATIO 0.0465

#include "Input/Ligament_Properties.any"
```

:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::

## Bibliography

[^cite_azdn17]: Andersen, M. S., de Zee, M., Damsgaard, M., Nolte, D., & Rasmussen, J. Introduction to Force-Dependent Kinematics: Theory and Application
    to Mandible Modeling. J Biomech Eng. 139(9), 091001 (2017). <a href="https://doi.org/10.1115/1.4037100" target="_blank" rel="noopener">https://doi.org/10.1115/1.4037100</a>

[^cite_hcmt10]: Halloran JP, Clary CW, Maletsky LP, Taylor M, Petrella AJ, Rullkoetter PJ. Verification
    of predicted knee replacement kinematics during simulated gait in the Kansas knee simulator. J
    Biomech Eng. 132(8), 081010 (2010). <a href="https://dx.doi.org/10.1115/1.4001678" target="_blank" rel="noopener">https://dx.doi.org/10.1115/1.4001678</a>

[^cite_bkhg91]: Blankevoort, L., Kuiper, J. H., Huiskes, R., and Grootenboer, H. J., “Articular Contact
    in a Three-Dimensional Model of the Knee,” J. Biomech., 24(11), pp. 1019–1031, (1991). <a href="https://doi.org/10.1016/0021-9290(91)90019-J" target="_blank" rel="noopener">https://doi.org/10.1016/0021-9290(91)90019-J</a>

[^cite_mvfk15]: Marra, M. A. et al. A subject-specific musculoskeletal modeling framework to predict in
    vivo mechanics of total knee arthroplasty. J. Biomech. Eng. 137, 020904 (2015). <a href="https://dx.doi.org/10.1115/1.4029258" target="_blank" rel="noopener">https://dx.doi.org/10.1115/1.4029258</a>

[^cite_sbtp06]: Shelburne, K. B., Torry, M. R. & Pandy, M. G. Contributions of muscles, ligaments, and the ground-reaction force to tibiofemoral joint loading
    during normal gait. J. Orthop. Res. 24, 1983–1990 (2006). <a href="https://dx.doi.org/10.1002/jor.20255" target="_blank" rel="noopener">https://dx.doi.org/10.1002/jor.20255</a>
