---
gallery_title: "ADL Gait (beta)"
gallery_image: "/Applications/images/ADL_Gait.webp"
anylink: Application/MocapExamples/ADL_Gait_[beta]/Subjects/2014001/2014001_C1_01/Main.any
---

(sphx_glr_auto_examples_MoCap_plot_ADL_Gait.py)=
(example_adlgait)=
# ADL Gait (beta)


:::{anylink-gallery}
:margin:
:::



Fullbody MoCap model with multiple subjects and trials based on the 
"Rehazenter Adult Walking Dataset" by Schreiber and Moissenet (2019). [^schreiber2019]



The model has 50 subjects and 1145 trials. Subjects walk at five different
speeds (conditions) C1: 0–0.4 m/s, C2: 0.4–0.8 m/s, C3: 0.8–1.2 m/s, C4: a 
self-selected spontaneous speed, C5, self-selected fast speed.

The dataset uses 53 reflective markers and measured ground reaction forces. A 
standing reference trial is used to identify a number parameters: 

* Segment lengths
* Tibial torsion angle
* Varus-valgus angle
* Unconstrained marker positions

These parameters are then loaded in the matching dynamic trials. 

:::{warning} The model is a starting point for analysing the 
Rehazenter adult walking dataset. 
The model has not been through *any* kind of validation or publication. It is likely that 
some results will not be correct without further adjustments.
:::
  
Choices of model parameters are in some cases arbitrary as this model is a work in progress. If you come up 
with improvements to the model please share them back. 

The model was created by <a href="https://www.linkedin.com/in/enrico-de-pieri-13096a7a" target="_blank" rel="noopener">Enrico De Pieri</a>,
<a href="https://vbn.aau.dk/en/persons/oliveira" target="_blank" rel="noopener">Anderson de Souza Castelo Oliveira</a>, and <a href="https://www.linkedin.com/in/biomedical" target="_blank" rel="noopener">Morten Enemark Lund</a> but has not yet been used for publication.

## Dataset

The full "Rehazenter adult walking dataset" is not distributed with the model. The dataset is
released under a Creative Commons license (CC BY 4.0). 

You must download the data sepearately from this model:

* <a href="https://figshare.com/articles/dataset/A_multimodal_dataset_of_human_gait_at_different_walking_speeds/7734767" target="_blank" rel="noopener">Rehazenter adult walking dataset</a>

After downloading extract the data into the `C3DFiles` sub folder. 


## Model structure

The model files are structured so each trial has its own folder with a main file
(`Main.any`) and a file with trial specific data (`TrialSpecificData.any`).
The C3D files are placed together in a separate folder.

The model is structured as outlined below:

```

   Application/MocapExamples/ADL_Gait_[beta]
    │   libdef.any
    │   C3DSettings.any
    │   BodyModelConfig.any
    │   ExtraDrivers.any
    │   ForcePlates.any
    │   MarkerProtocol.any
    │   LabSpecificData.any
    │
    ├───C3DFiles\
    |   │  
    |   ├───2014001\
    |   |      2014001_C1_01.c3d
    |   |      2014001_C1_02.c3d
    |   |      ..
    |   |      2014001_ST.c3d
    │   |
    |   └───2014002\
    │          ..
    │
    ├───Output\
    │
    └───Subjects\
        │
        ├───2014001\
        │   |   SubjectSpecificData.any
        |   |
        │   ├───2014001_C1_01\
        |   |      Main.any
        |   |      TrialSpecificData.any
        |   :   
        |   |   
        │   └───2014001_ST\
        |          Main.any
        |          TrialSpecificData.any
        │   
        └───2014002\
            |   SubjectSpecificData.any
            |
            ├───2014002_C1_01\
            |      Main.any
            |      TrialSpecificData.any
            : 
```

## Batch processing

The model also contains a batch processing Python script for running all models. The script 
`batchprocess.py` is located in the top-level folder. 

To use the script, install the <a href="https://www.anaconda.com/download" target="_blank" rel="noopener">Anaconda Python Distribution</a>.

The script uses the <a href="https://github.com/AnyBody-Research-Group/AnyPyTools" target="_blank" rel="noopener">AnyPyTools</a> library for working with the
AnyBody Model System (Lund et al., 2019 [^lund2019]).

Then run the following command in the model folder:

```bash
python batchprocess.py
```

:::{note} You may need to modify the script to output the variables you are interested in. It may also 
    be necessary to modify the number of parallel AnyBody instances to match the number of licenses you have. 
:::    

:::{admonition} In Model Repository:
:class: seealso

`Application/MocapExamples/ADL_Gait_[beta]`

* Dynamic trial: {anylink-file}`Subjects/2014001/2014001_C1_01/Main.any <Application/MocapExamples/ADL_Gait_[beta]/Subjects/2014001/2014001_C1_01/Main.any>`
* Standing reference: {anylink-file}`Subjects/2014001/2014001_ST/Main.any <Application/MocapExamples/ADL_Gait_[beta]/Subjects/2014001/2014001_ST/Main.any>`

:::

## Bibliography

[^schreiber2019]: Schreiber, C., & Moissenet, F. (2019). A multimodal dataset of human gait at different walking speeds established on injury-free adult participants. *Scientific Data*, *6*, 111. <a href="https://doi.org/10.1038/s41597-019-0124-4" target="_blank" rel="noopener">https://doi.org/10.1038/s41597-019-0124-4</a>

[^lund2019]: Lund, M. E., et al. (2019). AnyPyTools: A Python package for reproducible research in musculoskeletal biomechanics. *Journal of Open Source Software*, *4*(42), 1108. <a href="https://doi.org/10.21105/joss.01108" target="_blank" rel="noopener">https://doi.org/10.21105/joss.01108</a>


