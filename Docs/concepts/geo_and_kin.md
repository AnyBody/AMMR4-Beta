
# Geometrical and kinematical concepts


<!-- ================================================================== -->
## Key reference frames

<!-- ------------------------------------------------------------------ -->
### Data and Segmental Frames

We use the term *Data Frame* to refer to the reference frame in which a particular set of geometrical data is defined. 
Different body parts, or even individual segments, may have distinct Data Frames, as these models are often based on different datasets. 
It is important to distinguish between the Data Frames of different datasets.
It is also important to acknowlegde that Data Frame is only a concept related to the original data, i.e., before model scaling.  

However, the *Segmental Frame* is the reference frame of a segment in the model (i.e. the frame of an `AnySeg` object).
The Segmental Frame is typically the same as the Data Frame, if no transformation due to model scaling has been applied.

In AMMR, the bodyparts use either of the following two concepts

- **Shared Data Frame for body part**: .... TODO ....
- **Local Data/Segmental Frames**: .... TODO ....

  MAYBE MENTION THAT THIS IS OLDER CONCEPT ?????


:::note **About AMMR Implementation**

The Trunk Model, The GM Foot and the Hand Model (new in AMMR 4.0) are cases using the Shared Data Frame concept,
while The TLEM Leg Model and The Shoulder-Arm Model uses Local Data/Segmental Frames
:::


A Data/Segmental Frame can have certain assumptions attached, 
for instance about the location of the data with respect certain features like neutral position, scanned position, etc.
Such assumptions may be exploited for building the model and a therefore they are important to acknowledge.

:::note **About AMMR Implementation**

- The Trunk Model's Data Frame is assumed to represent a neutral standing posture.
  This has been used to define Anatomical and Postural Data Frames, see further explanation later

- The Foot Model's Data Frame ... FILL HERE
- The Hand Model's Data Frame ... FILL HERE
- The TLEM Leg Model's Segmental Frames ... FILL HERE
- The Shoulder-Arm Model's Segmental Frames ... FILL HERE
:::


<!-- ------------------------------------------------------------------ -->
### Anatomical Frames 

An Anatomical Frame is a frame defined by the key bone(s) of a segment.
In principle, it uses bony landmarks to define the frame, but often we also 
use other bony features such as approximated joint centers.  

It should align roughly with global frame of the Body Model in a neutral standing position
so that Y is longitudinal(vetical) axis, while X is in the sagital plane and Z in the frontal plane 
in the so-called neutral standing posture.
In other postures, bones and segments are moved and the anatomical frames doe of course not align at all.
This rough alignment is merely eliminate large offsets (90, 180 deg. or larger) of angles 
measured between such Anatomical Frames.

Anatomical Frames are particular useful for:
- definition of key geometrical angles of the body, 
  hereunder kinematical degrees of freedom. 
- definition of markers and other environment connections related to segments/bones


:::note **About AMMR Implementation**
TODO:

- In upper and lower extremity models we define Y of the long-bones between the joint centers,
  while X points into the plane of the primary approximated joints axis, i.e.,
  - Thigh has X along the bony landmark defined knee axis
  - Shank has X along the bony landmark defined ankle axis
  - Upper arm has X along the bony landmark defined elbow axis
  - Lower arm has X along the bony landmark defined wrist axis

- TRUNK IN AMMR3 Anatomical Frame = Data Frame

:::


<!-- ------------------------------------------------------------------ -->
### Postural Frames

Postural Frames are somewhat like Anatomical Frames or closely related the Anatomical Frames.
However, the Postural Frames of the segments define the neutral position of the body.
This implies that you can measure angles between the Postural Frames of two related segments  
and these angles are zero in the neutral position.
Or you can drive such angles to zero and obtain the neutral position as defined the Body Model.

To define such Postural Frames on multiple segments of a body-part model,
we must define the neutral position of the body part and in this posture attach parallel 
Postural Frames on the segments.
TODO: IF NEEDED, EXPLAIN BETTER OR MAYBE LINK TO THE NOTE BELOW

:::note **About AMMR Implementation**
Postural Frames is a concept introduced in AMMR 4.0
TODO: IS IT FULLY IMPLEMENTED ?????????????

:::

<!-- ------------------------------------------------------------------ -->
### Joint Frames



<!-- ------------------------------------------------------------------ -->
### Scaling Frames
  <!-- ---- > maybe move this to  ## Scaling functions ??????????????? -->
- Scaling frame: Preferably this is the anatomical frame of the segments, 
  but this is not always a good idea

  - Align roughly with neutral global frame, so scaling functions applies same axes in all parts of the body
    Long bones of extremities Y is longitudinal axis, while X is in the sagital plane and Z in the frontal plane in neutral


:::note **About AMMR Implementation**

'ScalingNode'
:::



<!-- ================================================================== -->
## Body Model Symmetry and Mirrored Body Parts

The human body exhibit bilateral symmetry to a large extend, such as the left and right arms or legs, 
but the symmetry is not perfect for a given person and the are even statitically  . 

In AMMR, the Body Model is implmented to strive for perfect symmetry of the unscaled data and thereby in the generic Body Model.
The idea is that subject-specific (or even statistical) assymmetry should be implemented in the scaling of the Body Model.
It is simpler to control specific assymmetric feastures accurately, if the initial data are known to be symmetric. 
And leveraging symmetry in the generic model streamlines model development 
and helps to ensure that both sides of the body behave consistently in simulations.


:::note **About AMMR Implementation**

- **All body-part models of extremities** are developped for one side with 
  a specific mirroring parameter allowing to implement left and right side with sign-change and full reuse of code.
  These models are placed in Left and Right folders of the Body Model.
- **Central body-parts** (i.e. primarily The Trunk Model) are done the same way, 
  i.e., having Left and Right folders and  full code reuse. 

- **Geometrical mirroring** is carried out by using the mirror-sign parameters to switch 
  one of the coordinates
  EXPLAIN HOW THIS RELATES TO SCALING FUNCTIONS. IS IT DOEN BEFORE SCALING?

- **Kinematic Definitions**: Joint axes and degrees of freedom are mirrored appropriately 
  to maintain anatomical meaningfulness and consistent movement patterns.
  Special care is taken to correctly mirror reference frames while maintaining right-handedness. 
  A frame cannot be mirrored as geometry, which would lead to unuseful left-hand coordinate systems.
  In stead frames a mirror in view of other kinematical definitions, e.g. joint angles, 
  that arise from the axes of the mirrored frames. 

- **Naming Conventions**: Apart from the 'Left' and 'Right' folders at a high level in the Body Model and related folder structures, 
  there may be a few distinqt places where prefixing is used locally (e.g., prefixing with `L` or `R`).
:::




<!-- ================================================================== -->
## Degrees of freedom and neutral positions



<!-- ================================================================== -->
##  Movement rhythms
Movement rhythms, or shorter just "rhythms", are movement constraints in the model
that link basic degrees of freedom together in a natural pattern.

The purpose of such rhythms ....


To exemplify the concept, notice the two important rhythms built into AMMR's human model 
can be mentioned:

- **The Spine Rhythm(s)**: ?????????? 

- **The shoulder Rhythm**: ??????????







