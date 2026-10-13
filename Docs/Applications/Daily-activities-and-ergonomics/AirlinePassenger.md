---
gallery_title: "Airline Passenger"
gallery_image: "/Applications/images/AirlinePassenger.webp"
anylink: "Application/Examples/AirlinePassenger/AirlinePassenger.main.any"
---

(sphx-glr-auto-examples-adls-and-ergonomics-plot-airlinepassenger-py)=

# Airline Passenger

:::{anylink-gallery}
:margin:
:::


This example models a person sitting in a coach-class airline passenger seat. The seat is characterized by the following:

- No arm rests (you always lose the battle for the armrest  to the person next to you)
- Horizontal seat pan
- Limited ability to recline the backrest due to the lack of clearance to the person behind


## Comfort assessment

The model assesses passenger comfort using the following measures:

- Maximum muscle activity, expressed as the percentage of maximum voluntary contraction required to maintain the posture. The activity search covers the right vastus muscle group.
- The total shear force between the seat pan and the buttocks. Shear forces can contribute to discomfort during static loading, such as when a passenger tries to sleep.

The seat-to-buttocks friction coefficient, `StaticFrictionSeat`, creates an important comfort trade-off. As friction decreases, the shear load on the buttocks can ease, but the passenger must recruit the right vastus muscle group more strongly to avoid sliding forward. The model makes this relationship visible by reporting both the seat shear force and the muscle activity required to maintain the posture.

## Model setup

The posture is controlled by the backrest angle. The main posture and support settings are defined in `Model/InputParameters.any`, including the backrest angle and velocity, seat and footrest positions, contact friction, and support strengths.

The inverse dynamic analysis reclines the backrest from an initial 10° forward inclination to a 30° backward inclination, near the upper limit of coach-class passenger seats.

:::{note}
The backrest provides pressure support for the back but no tension support. Forward-leaning postures are therefore created by inclining the seat forward, without support from the backrest.
:::


:::{admonition} In Model Repository:
:class: seealso

{anylink-file}` `

:::
