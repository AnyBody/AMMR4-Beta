# The RHUM 2 Hand Model

:::{admonition} **Beta Model:**
:class: warning
This model is in testing and will be released into AMMR4. Access to the development version can be given on request.
:::

The existing AMMR hand models have no muscles on fingers and model structure is not consistent with the remaining body parts.
The existing beta version of the {doc}`regensburg_ulm_hand_model` is much more sophisticated but model bone geometries and model structure is also not in line with the remaning body model in AMMR. For both models, scaling can be difficult to control.

The new hand model is systematically implemented (high amount of code sharing between fingers) and structured in a similar manner to other AMMR bodyparts with separated model definition and model parameters.

The new hand model has 23 degrees of freedom (DOF) with 5 in the thumb (`CMCAbd`, `CMCFlex`, `MCPFlex`, `MCPAbd`, `DipFlex`), 4 in each finger (`MCPFlex`, `MCPAbd`, `PIPFlex`, `DIPFlex`) and additionally `CMC4Flex` and `CMC5Flex` allows control of the distal transverse arch.

:::{figure} _static/hand_rhum2.png
:align: center
:width: 50%
:::

## Scaling

Neutral position is well defined (flat) and one scaling function covers all bones.

## Muscles

Muscles stop at metacarpals, but additional lengths are accounted for. There are torques actuators on all finger joints and `CMC4` + `CMC5`. Development is ongoing to implement the muscle definitions from the {doc}`regensburg_ulm_hand_model`

:::{figure} _static/hand_rhum2_mus.png
:align: center
:width: 40%
:::

## Flexible and Rigid configurations

The new hand model has two configurations, flexible and rigid, each sharing the exact same DOF. The configuration is controlled by the new _BM_ statement `BM_ARM_HAND_MODEL`

### The Flexible Hand

Enabled by:
`#define BM_ARM_HAND_MODEL _HAND_MODEL_FLEXIBLE_`

- Has all finger joints (with the carpal bones being rigid)
- Allows for tracking of detailed hand motions
- Allows calculation of finger torques

#### Use case examples

- Finger torques needed to unscrew a lid
- Finger torques needed to open packaging

### The Rigid Hand

Enabled by:

`#define BM_ARM_HAND_MODEL _HAND_MODEL_RIGID_`

- Mechanically rigid (one segment) but still shapeable
- Identical model structure to the flexible hand
- Allows the hand to take the same shapes as the flexible hand, using the same DOF’s (this allows more realistic contact on rigid hands and makes it easier to get good boundary conditions for an arm model)
- Improves visuals on models with rigid hands

:::{figure} _static/hand_rhum2_rigid.png
:align: center
:width: 100%
:::

## References

This is a list of references used in the creation of this model:

- Barry, A., Murray, W., Kemper, D. (2018). Development of a dynamic index finger and thumb model to study impairment. Journal of Biomechanics ([link](https://doi.org/10.1016/j.jbiomech.2018.06.017))
