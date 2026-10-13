---
gallery_title: "Seated Human"
gallery_image: "/Applications/images/SeatedHuman.webp"
anylink: Application/Examples/SeatedHuman/SeatedHuman.main.any
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-seatedhuman-py)=
(example_seatedhuman)=
# Seated Human

:::{anylink-gallery}
:margin:
:::

A model of a seated human consisting of the full body model, a chair, and an
interface between the two.



The Seated Human is a family of models resulting from a
research project involving the furniture industry. This
model is a human sitting in a generic chair where the seat,
backrest, arm rests, foot rest and head rest can be adjusted
and their influence on the forces in the human body can be
investigated.

:::{note}
The contact conditions are conditional with
respect to the distance between the body and the surface
in question so that they are only active when the contact
pair is close to each other.
:::

The contact between the human body and the chair is by means
of contact elements that can only provide compression and
friction but no tension. The available friction is proportional
to the normal force and the user can supply a friction
coefficient for each surface such that the effect of different
surface fabrics can be investigated.

The contact elements expose separate normal and friction force
measures for each support surface. The study also provides the
resultant reaction force at the L5-sacrum joint through
`Study.L5SacrumReac`. These outputs can be compared while changing
the chair configuration or support settings; the model does not
calculate a separate comfort score.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
