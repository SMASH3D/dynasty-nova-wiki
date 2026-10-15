---
wiki_id: 107
locale: "en"
path: "fleet/expeditions"
url: "https://wiki.dynastynova.com/en/fleet/expeditions"
title: "Expeditions"
description: "Exploring deep space: conditions, outcomes and size of finds."
tags: ["fleet"]
published: true
created: "2026-10-02T13:11:13.809Z"
updated: "2026-10-02T17:41:05.921Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Expeditions

> **In short**: past the last position of every system lies deep space. A fleet holding position there sometimes comes back loaded with resources or abandoned ships, sometimes late, or runs into pirates, aliens, even a black hole. You need Astrophysics to go.
{.is-info}

> **Universe setting**: expeditions can be open or closed depending on the universe.
> Default: **open** · Redline: **open**
{.is-info}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Astrophysics">

## Rules

### Setting off
1. You need **Astrophysics level 1** at least.
2. The target is the system's **deep space**: the position after the last one (16 on Redline). Only Expedition and Recycling can go there.
3. The fleet cannot be **Scouts only**; a Scout may join any other hull. The Solar Collector never flies.
4. You pick the **hold duration**, in whole hours: from 1 h up to as many hours as your Astrophysics level.
5. **Simultaneous expeditions** = the integer part of the square root of your Astrophysics level. They count all your expeditions in the universe, flying out, holding or coming back. Each one **also** takes a fleet slot.
6. **Hydrogen**: the way out, the way back and the hold are paid at departure. The hold costs $\lceil h \times C / 10 \rceil$, where $h$ is the number of hours and $C$ the sum of the base consumption of the ships sent (consumption × count). No fuel-saving talent applies to the hold. All the trip's hydrogen must fit in the holds alongside the cargo.

### In deep space
7. The **hold duration does not change the odds** of finding something. It only lengthens the trip and the fuel bill, and any delay (rule 12).
8. **Recall**: a fleet recalled during its hold flies the whole way out again to get home and brings back **nothing**, neither outcome nor report.
9. An over-visited area **runs dry**: from **10 expeditions** resolved in the same system's deep space within 24 hours, all players combined, the area is "exploited" and the odds of a find drop; from **25**, it is "depleted" and they drop further. The lost share goes to the "nothing" outcome. If the fleet carries at least one **Scout**, the report gives the area's state.

### Outcomes
10. **Resources**: a single resource type per find, metal, crystal or hydrogen. The amount is proportional to the fleet's expedition points (rule 15), in metal equivalent: divided by 2 for crystal and by 3 for hydrogen. The find is capped by **free cargo space**: the excess is lost, and the report says so.
11. **Ships**: abandoned ships join your fleet, worth half a resource find. They take no cargo space. You can find up to the rank right above your best ship aboard (table below). Never a Stellar Colossus, Space Pioneer, Salvager or Solar Collector, which do not count for the rank either. Found ships bring their military points.
12. **Delay**: the way back is lengthened by 2, 3 or 5 times the chosen hold duration, depending on the size of the event. **Early return**: the way back is divided by 2, 3 or 5.
13. **Pirates** and **aliens**: a real battle against a fleet modelled on yours, stronger when the event is bigger, with an escort on top. Aliens are stronger than pirates. Pirates fight with your combat research minus 3 levels, aliens with 3 levels more. You get a battle report; survivors keep their cargo, no plunder. Debris (10% of the ships destroyed, both sides) stays in deep space.
14. **Black hole**: the whole fleet and its cargo are lost. **Nothing**: the fleet comes back as it left.

### Size of finds
15. **Expedition points** = max(200, total fleet structure / 200, rounded down), capped by the points of the universe's **top human player** (table below). The bigger the fleet, the more it brings back, up to the cap.

## Worked example

50 Stellar Freighters and 1 Scout fly from [2:40:8] to deep space [2:40:16], with Combustion Drive 6, at 100%, for a 3-hour hold. The universe's top player has 500,000 points.
- Distance: 1,000 + 5 × 8 = **1,040**. Fleet speed: the Freighter's, 7,500 × 1.6 = 12,000. Trip: **3,268 s** (54 min 28 s) each way.
- Hydrogen: 297 per leg, so 594 for the round trip, plus the hold $\lceil 3 \times 2{,}501 / 10 \rceil$ = 751: **1,345** paid at departure. It travels in the 1,250,005 of cargo space.
- Total structure: 50 × 12,000 + 1,000 = 601,000. Expedition points: 601,000 / 200 = **3,005**, under the cap of **6,000** (top player under 1,000,000 points).
- With Astrophysics 5: up to 5 hours of hold and **2** simultaneous expeditions.

## Detailed data

### Hold and simultaneous expeditions

| Astrophysics | Longest hold | Simultaneous expeditions |
|---|---|---|
| 1 | 1 h | 1 |
| 2 | 2 h | 1 |
| 3 | 3 h | 1 |
| 4 | 4 h | 2 |
| 6 | 6 h | 2 |
| 9 | 9 h | 3 |
| 12 | 12 h | 3 |
| 16 | 16 h | 4 |

### Expedition points cap

| Top player's points | Cap |
|---|---|
| under 10,000 | 200 |
| under 100,000 | 2,500 |
| under 1,000,000 | 6,000 |
| under 5,000,000 | 9,000 |
| under 25,000,000 | 12,000 |
| under 50,000,000 | 15,000 |
| under 75,000,000 | 18,000 |
| under 100,000,000 | 21,000 |
| 100,000,000 or more | 25,000 |

### Rank of found ships

| Rank | Ship |
|---|---|
| 1 | *Scout* |
| 2 | *Cargo Shuttle* |
| 3 | *Interceptor* |
| 4 | *Stellar Freighter* |
| 5 | *Assailant* |
| 6 | *Corvette* |
| 7 | *Battleship* |
| 8 | *Predator* |
| 9 | *Orbital Striker* |
| 10 | *Annihilator* |

Example: a fleet whose best ship is a Battleship (rank 7) can find up to a Predator (rank 8). A fleet with no ship from this table counts as rank 1.

## Common pitfalls

- **Staying longer does not help** the odds: pick the duration to suit your schedule. It also lengthens any delay.
- **Keep cargo space free**: a resource find that does not fit is lost, and the trip's hydrogen already takes part of the holds.
- **Switch systems**: a busy deep space runs dry, whoever visited it.
- **A recall cancels everything**: the fleet comes home empty-handed, after a way back as long as the way out.
- **Black holes exist**: do not send your main fleet.

## Related pages

- [Missions](/en/fleet/missions)
- [Fleet movement](/en/fleet/movement)
- [Ships list](/en/fleet/ships)
- [Technologies](/en/research/technologies)
- [Coordinates](/en/universe/coordinates)
- [Debris fields](/en/combat/debris)
