---
gallery_title: "Pedal Demo (simple)"
gallery_image: "/Applications/images/PedalDemo.webp"
anylink: Application/Examples/PedalDemo/PedalDemo.Main.any
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-pedaldemo-py)=

# Pedal Demo (simple)

:::{anylink-gallery}
:margin:
:::

This model is for design of a pedal that is comfortable to use
for a seated operator depending on the stiffness of the embedded
spring and the distance of the seat from the pedal.

The environment contains a rigid pedal connected to the ground by a
hinge and supported by a torsional spring. The right foot is connected to
the pedal, while the left foot rests on a separate support. The seated
posture is defined by the mannequin, and the body model configuration
uses the lower-limb and trunk components needed for this example.

The main design variables are the spring stiffness `SpringStiff` and
the seat position `Hpoint`, both defined in `Model.MyPedal`. Change
these variables and run `Study` to examine how the resulting pedal
motion and musculoskeletal forces change. The example does not calculate
a separate comfort score or represent a validated comfort assessment;
comfort must be evaluated from appropriate analysis results and design
criteria for the intended application.



:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
