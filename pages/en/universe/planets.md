---
wiki_id: 83
locale: "en"
path: "universe/planets"
url: "https://wiki.dynastynova.com/en/universe/planets"
title: "Planets: size, temperature, type"
description: "Fields, temperature and the effect of position."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:27.007Z"
updated: "2026-10-06T10:31:00.620Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Planets: size, temperature, type

> **In short**: a planet's position in its system sets its average size and its temperature. Planets close to the sun are smaller and hotter, ideal for solar energy; distant planets are larger and colder, ideal for hydrogen. The planet type (desert, jungle, ice…) only changes its look. Colonies also get an output bonus depending on their position.
{.is-info}

> **Universe setting**: the number of positions per system (9 to 20) depends on the universe. In a universe without 15 positions, the position is first scaled to a 15-position range: the profiles below still apply, from closest to farthest from the sun.
> Redline: **15 positions**
{.is-info}

![A system in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*A system in orbit layout: each planet looks like its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

1. **Size**: a planet's total number of fields equals the average size of its position, plus or minus 15, rolled when the planet is created and then fixed.
2. The **mother planet** always starts with **163 fields**, whatever its position.
3. Each building level takes **one field**. The [Planetary Modulator](/en/economy/terraformer-and-logistics) adds fields.
4. **Temperature**: each position has a minimum and a maximum temperature (table below). The **current** temperature follows the calendar month: at its minimum on the 1st, it rises each day to its maximum in the middle of the month (the 15th, the 14th in February), then falls back to its minimum on the last day of the month.
5. Temperature affects three outputs:
   - **Hydrogen Condenser**: output × (1.44 − 0.004 × maximum temperature). The colder, the more it produces.
   - **Solar Collector**: output = maximum temperature / 4, plus a base amount of energy.
   - **Photovoltaic Sensors**: output × (1 + current temperature / 100), when the current temperature is positive.
6. **Type, biome and look**: each planet has a type (desert, dry, normal, jungle, water, ice, gas) and a **biome**, a visual variant rolled when it is created. Together they give each planet its own look, in the galaxy view as in 3D. They only change the generated name and the pictures, not output. A **planet skin**, from the shop or the Premium monthly set, replaces your planet's look.
7. Beyond the last position lies **deep space**: no planet, only debris fields and fleets on expedition.
8. **Position bonus** (colonies only): the Crystal Extractor at positions 1 to 3 and the Mineral Excavator at positions 6 to 10 produce more (table below). The mother planet never gets it, so that nobody starts at an advantage. The bonus has its own line in the production breakdown.

## Worked example

**Hydrogen: position 3 versus position 12**
- Position 3 (max temperature 135 °C): factor 1.44 − 0.004 × 135 = **0.90**.
- Position 12 (max temperature 0 °C): factor 1.44 − 0.004 × 0 = **1.44**.
- At the same level, the position 12 Condenser produces 1.44 / 0.90 = **60% more**.

**Solar energy on a planet at position 8** (20 to 60 °C)
- On a day when the current temperature is 23 °C, Photovoltaic Sensors produce **23% more** (× 1.23).
- Each Solar Collector there produces 35 energy (value seen in game).

## Detailed data

### By position (15-position universes)

| Position | Average size (fields) | Possible types | Min / max temperature (°C) |
|---|---|---|---|
| 1 | 145 | desert, dry | 125 / 165 |
| 2 | 150 | desert, dry | 110 / 150 |
| 3 | 155 | desert, dry, normal | 95 / 135 |
| 4 | 160 | dry, normal | 80 / 120 |
| 5 | 163 | normal, water | 65 / 105 |
| 6 | 185 | normal, water, jungle | 50 / 90 |
| 7 | 190 | normal, water, jungle | 35 / 75 |
| 8 | 195 | water, jungle | 20 / 60 |
| 9 | 200 | water, jungle, normal | 5 / 45 |
| 10 | 205 | jungle, normal | −10 / 30 |
| 11 | 225 | ice, normal | −25 / 15 |
| 12 | 230 | ice, gas | −40 / 0 |
| 13 | 235 | ice, gas | −55 / −15 |
| 14 | 242 | ice, gas | −70 / −30 |
| 15 | 245 | ice, gas | −85 / −45 |

A colony's actual size varies by 15 fields around the average: a colony at position 15 has between 230 and 260 fields.

### Hydrogen output factor

| Position | 1 | 3 | 5 | 8 | 10 | 12 | 15 |
|---|---|---|---|---|---|---|---|
| Max temperature (°C) | 165 | 135 | 105 | 60 | 30 | 0 | −45 |
| Condenser factor | 0.78 | 0.90 | 1.02 | 1.20 | 1.32 | 1.44 | 1.62 |

### Position bonus (colonies only)

| Position | 1 | 2 | 3 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| Crystal Extractor (crystal) | +40% | +30% | +20% | | | | | |
| Mineral Excavator (metal) | | | | +17% | +23% | +35% | +23% | +17% |

Positions 4, 5 and 11 to 15 have no bonus. The mother planet never has one, whatever its position.

## Common pitfalls

- **The mother planet ignores the table**: it always has 163 fields, and has no position bonus.
- **For a colony, position matters twice**: crystal at positions 1 to 3, metal at positions 6 to 10 (+35% at position 8).
- **The solar bonus changes during the month**: it depends on the current temperature, which goes up and down. A cold planet almost never benefits from it.
- **Type does not matter**: an "ice" planet and a "gas" planet at the same position produce the same.
- **Fields are the real long-term limit**: a small planet close to the sun fills up fast.

## Related pages

- [Colonization](/en/universe/colonization)
- [Buildings list](/en/economy/buildings)
- [Energy](/en/economy/energy)
- [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)
- [Coordinates](/en/universe/coordinates)
