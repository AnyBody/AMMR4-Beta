---
gallery_title: "Pedal Demo (conditional)"
gallery_image: "/Applications/images/PedalDemoConditional.webp"
anylink: Application/Examples/PedalDemoConditional/PedalDemoConditional.Main.any
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-pedaldemoconditional-py)=

# Pedal Demo (conditional)

:::{anylink-gallery}
:margin:
:::

This model is a variant of the <a href="PedalDemo.html" target="_blank" rel="noopener">simple pedal demo</a> for designing a pedal for a seated operator. Its foot-pedal contact is conditional: contact becomes active only when the foot and pedal are sufficiently close to each other.

The model uses the same pedal environment, spring, seat position, and seated posture as the simple pedal demo, while adding a proximity-based contact condition through `ConditionalContactClass`.


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `
:::
