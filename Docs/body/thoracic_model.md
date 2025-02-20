(Ribcage and thoracic spine model)=

# Ribcage and thoracic spine model

The present generic thoracic model extends the state-of-the-art by introducing a kinematically determinate rigid-body model controlled by full spine DOFs, enabling the simulation of activities such as breathing and curved spine motions (e.g., scoliosis) with detailed ribcage kinematics. Designed for improved usability in clinical and motion capture applications, the model has a wide Range of Motion (ROM) and accommodates severe deformities without locking, thanks to nonlinear constraints and redundancy handling. The model supports direct and inverse kinematics, offering flexibility in input options.

The new model builds on a previously developed thoracic spine model [1]. This thoracic spine model consists of the thoracic vertebral column (12 vertebrae) and the ribcage, including individual ribs (24 ribs) and a two-part sternum. The multiple segments interconnected by joints replicate the physiological connections and load transfer mechanisms.

## Kinematics
The kinematic constraints of the thorax are summarized as follows:

- **Vertebra constraints:** The intervertebral joints of the spine, adopted from previous work, are modeled as spherical joints. These joint angles can be adjusted to set the model’s posture.
- **Rib constraints:** The costovertebral (CV) connections between the vertebrae and ribs are also defined as spherical joints. For each rib, three rotational Averaging measure (AvgM) constraints were established. Detailed information is provided in the published paper [2].
- **Sternum constraints:** A revolute joint was defined between the manubrium and the sternal body, allowing rotation around the mediolateral axis. This DOF enables ribcage movements independent of spinal posture, e.g., for breathing. Additionally, three linear and three rotational AvgM constraints were defined for the entire sternum, with further details provided in the published paper [2].

```{image} _static/Ribcage_Constraints.jpg 
    :width: 60%
    :align: center  
```

## Spine rhythms 
To drive the thoracic model, only the thoracic spine needs to be controlled, while the ribcage follows the spine as it is kinematically determinate due to the constraints. However, the thoracic spine consists of 12 vertebrae, each requiring three rotational drivers. To simplify usage, we introduced rhythms, which are constraints that link the rotational DOFs of the intervertebral joints. As a result, all vertebrae are linked with rhythm drivers, requiring input for only three spine rotational DOFs (flexion/extension, lateral bending, and axial rotation). Below is a video demonstrating how the rhythms work.

```{raw} html
<video width="100%" style="display:block; margin: 0 auto;" controls autoplay loop>
    <source src="../_static/rhythms.mp4" type="video/mp4">
Your browser does not support the video tag.
</video>
```


## Example of the model
Here are some examples of the thoracic model [2].

<div style="display: flex; justify-content: center; gap: 10px;">
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_AR.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_LB.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>

<div style="display: flex; justify-content: center; gap: 10px;">
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_FE.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <video width="45%" controls autoplay loop>
        <source src="../_static/Thoracic_Scoliosis_PA.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
</div>



## Muscles configurations
The majority of the muscle fascicles are defined for the thoracic column and ribcage region. 


<div style="display: flex; justify-content: center; gap: 10px;">
    <img src="../_static/Thoracic_muscle_front.png" width="30%" alt="Thoracic Muscle Front">
    <img src="../_static/Thoracic_muscle_back.png" width="30%" alt="Thoracic Muscle Back">
    <img src="../_static/Thoracic_muscle_iso.png" width="30%" alt="Thoracic Muscle Iso">
</div>




% .. image:: _static/thoracic.png

% :width: 100%

## Example Configuration

The detailed thoracic model can be controlled using the `BM_*` statements like the rest of the body models. 


```{code-block} AnyScriptDoc
:emphasize-lines: 2

#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_RIGID_
#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_FLEXIBLE_
#define BM_TRUNK_THORACIC_MODEL _THORACIC_MODEL_USERDEFINED_

model

```


```{rst-class} without-title
```





% .. rst-class:: float-right

% .. seealso::

% The :doc:`Trunk configuration parameters <../bm_config/trunk>` for a

% full list of Trunk parmaeters.

## References

- 1. [Shayestehpour, H., Rasmussen, J., Galibarov, P., Wong, C.: An articulated spine and ribcage kinematic model for simulation of scoliosis deformities. Multibody Syst. Dyn. 53, 115–134 (2021).](https://doi.org/10.1007/s11044-021-09787-9)
- 2. [Shayestehpour, H., Tørholm, S., Damsgaard, M., Lund, M., Wong, C., Rasmussen, J.: A generic detailed multibody thoracic spine and ribcage model](http://dx.doi.org/10.1007/s11044-024-10034-0)