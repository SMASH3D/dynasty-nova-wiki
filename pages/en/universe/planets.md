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
updated: "2026-10-15T18:53:45.173Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Planets: size, temperature, type

> **In short**: a planet's position in its system sets its average size and its temperature. Planets close to the star are smaller and hotter, ideal for solar energy; distant planets are larger and colder, ideal for hydrogen. The planet type (desert, jungle, ice…) only changes its look. Colonies also get a metal or crystal output bonus depending on their position; the mother planet gets none.
{.is-info}

> **Universe setting**: the number of positions per system (9 to 20) depends on the universe. In a universe without 15 positions, each position is read on a 15-position scale (rules 2 and 11).
> Default: **none, each universe has its own** · Redline: **15 positions**
{.is-info}

![A system in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*A system in orbit layout: each planet looks like its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

### Size
1. A planet's number of fields is the **average size of its position, plus or minus 15**. It is fixed once and for all when the universe is created, cell by cell.
2. In a system without 15 positions, the position is first **scaled to 15 and rounded** (list in the detailed data): size, types and temperature are those of that scaled position.
3. The **mother planet** always has **163 fields**, whatever its position.
4. Each building level takes **one field**, except the Repair Station. The [Planetary Modulator](/en/economy/terraformer-and-logistics) adds fields, and so do some dynasty talents.

### Temperature
5. Each position has a **minimum** and a **maximum** temperature, 40 °C apart: $T_{max} = 180 - 15 \times p$ and $T_{min} = T_{max} - 40$, with $p$ the position scaled to 15.
6. The **current** temperature follows the calendar month: at its minimum on the 1st, it rises each day to its maximum on the middle day of the month (the 15th, the 14th in February), then falls back to its minimum on the last day. It is rounded to the degree.
7. Temperature affects three outputs (details in [Energy](/en/economy/energy)):
   - **Hydrogen Condenser**: output × (1.44 − 0.004 × $T_{max}$), never below 0. The colder, the more it produces.
   - **Solar Collector**: $T_{max}$ / 4 + 20 energy each, rounded down.
   - **Photovoltaic Sensors**: output × (1 + current temperature / 100), when the current temperature is positive.

### Type and look
8. Each planet has a **type** (desert, dry, normal, jungle, water, ice, gas), drawn among those of its position, and a **biome**, a visual variant. They only change the generated name and the pictures, not output. A **planet skin**, from the shop or the Premium monthly set, replaces your planet's look.

### Position bonus
9. **Position bonus**: the Crystal Extractor produces more close to the star, the Mineral Excavator in the middle of the system (table below). The bonus has its own line in the production breakdown. It does not affect hydrogen, which depends on temperature.
10. The **mother planet has no position bonus**: its slot is drawn at random, and the bonus would hand everyone a different head start by luck. Only a dynasty talent can grant it a share.
11. In a system without 15 positions, the position is read on the 15-position scale **without rounding**, and the bonus is **interpolated** between the two positions around it. The peak (+40% crystal, +35% metal) stays the same, and no position is doubled or skipped.
12. The bonus applies to the mine's output, rounded down.

## Worked example

**Hydrogen: position 3 versus position 12**
- Position 3 (max temperature 135 °C): factor 1.44 − 0.004 × 135 = **0.90**.
- Position 12 (max temperature 0 °C): factor **1.44**.
- At the same level, the position 12 Condenser produces 1.44 / 0.90 = **60% more**.

**A colony's position bonus**
- Colony at position 8 of a 15-position system, Mineral Excavator producing 1,000 metal per hour: bonus 35%, so **+350 metal per hour**.
- Same mine on a colony at position 4 of a 9-position system: the position is read as 6.25 on the 15 scale, between 6 (+17%) and 7 (+23%), so a bonus of **18.5%**: **+185 metal per hour**.
- The same mine on your mother planet: **no bonus**.

**The month's temperature at position 8** (20 to 60 °C, 31-day month) and the Photovoltaic Sensors bonus:

| Day | Current temperature (°C) | Sensors bonus |
|---|---|---|
| 1 | 20 | 20% |
| 5 | 31 | 31% |
| 10 | 46 | 46% |
| 15 | 60 | 60% |
| 16 | 58 | 58% |
| 20 | 48 | 48% |
| 25 | 35 | 35% |
| 31 | 20 | 20% |

## Detailed data

### By position (out of 15)

| Position | Average size | Possible size | Possible types | Min / max temp. (°C) | Condenser factor | Energy per Collector |
|---|---|---|---|---|---|---|
| 1 | 145 | 130 to 160 | desert, dry | 125 / 165 | 0.78 | 61 |
| 2 | 150 | 135 to 165 | desert, dry | 110 / 150 | 0.84 | 57 |
| 3 | 155 | 140 to 170 | desert, dry, normal | 95 / 135 | 0.90 | 53 |
| 4 | 160 | 145 to 175 | dry, normal | 80 / 120 | 0.96 | 50 |
| 5 | 163 | 148 to 178 | normal, water | 65 / 105 | 1.02 | 46 |
| 6 | 185 | 170 to 200 | normal, water, jungle | 50 / 90 | 1.08 | 42 |
| 7 | 190 | 175 to 205 | normal, water, jungle | 35 / 75 | 1.14 | 38 |
| 8 | 195 | 180 to 210 | water, jungle | 20 / 60 | 1.20 | 35 |
| 9 | 200 | 185 to 215 | water, jungle, normal | 5 / 45 | 1.26 | 31 |
| 10 | 205 | 190 to 220 | jungle, normal | −10 / 30 | 1.32 | 27 |
| 11 | 225 | 210 to 240 | ice, normal | −25 / 15 | 1.38 | 23 |
| 12 | 230 | 215 to 245 | ice, gas | −40 / 0 | 1.44 | 20 |
| 13 | 235 | 220 to 250 | ice, gas | −55 / −15 | 1.50 | 16 |
| 14 | 242 | 227 to 257 | ice, gas | −70 / −30 | 1.56 | 12 |
| 15 | 245 | 230 to 260 | ice, gas | −85 / −45 | 1.62 | 8 |

### Positions scaled to 15 (size, types, temperature)

Scaled position of each position of the system, from the 1st to the last:

- 9 positions: 1, 3, 5, 6, 8, 10, 12, 13, 15
- 10 positions: 1, 3, 4, 6, 7, 9, 10, 12, 13, 15
- 11 positions: 1, 2, 4, 5, 7, 8, 9, 11, 12, 14, 15
- 12 positions: 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15
- 13 positions: 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15
- 14 positions: 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15
- 15 positions: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- 16 positions: 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15
- 17 positions: 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15
- 18 positions: 1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 13, 14, 15
- 19 positions: 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13, 13, 14, 15
- 20 positions: 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15

### Position bonus (colonies only)

15-position system (Redline); positions not listed have no bonus:

| Position | Read on 15 | Metal | Crystal |
|---|---|---|---|
| 1 | 1 |  | 40% |
| 2 | 2 |  | 30% |
| 3 | 3 |  | 20% |
| 6 | 6 | 17% |  |
| 7 | 7 | 23% |  |
| 8 | 8 | 35% |  |
| 9 | 9 | 23% |  |
| 10 | 10 | 17% |  |

9-position system:

| Position | Read on 15 | Metal | Crystal |
|---|---|---|---|
| 1 | 1 |  | 40% |
| 2 | 2.75 |  | 22.5% |
| 4 | 6.25 | 18.5% |  |
| 5 | 8 | 35% |  |
| 6 | 9.75 | 18.5% |  |

20-position system:

| Position | Read on 15 | Metal | Crystal |
|---|---|---|---|
| 1 | 1 |  | 40% |
| 2 | 1.74 |  | 32.63% |
| 3 | 2.47 |  | 25.26% |
| 4 | 3.21 |  | 15.79% |
| 5 | 3.95 |  | 1.05% |
| 7 | 5.42 | 7.16% |  |
| 8 | 6.16 | 17.95% |  |
| 9 | 6.89 | 22.37% |  |
| 10 | 7.63 | 30.58% |  |
| 11 | 8.37 | 30.58% |  |
| 12 | 9.11 | 22.37% |  |
| 13 | 9.84 | 17.95% |  |
| 14 | 10.58 | 7.16% |  |

The position read on 15 is $1 + (p - 1) \times 14 / (n - 1)$, with $p$ the position and $n$ the system's number of positions.

## Common pitfalls

- **The mother planet does not follow the table**: it always has 163 fields and no position bonus.
- **For a colony, position counts twice**: crystal close to the star, metal in the middle of the system (+35% at position 8 out of 15).
- **Size and bonus are not read the same way** in a universe without 15 positions: size and temperature follow the rounded position, the bonus the exact one.
- **The solar bonus varies over the month**: a cold planet hardly ever benefits.
- **Type does not matter**: an "ice" planet and a "gas" planet at the same position produce the same.

## Related pages

- [Colonization](/en/universe/colonization)
- [List of buildings](/en/economy/buildings)
- [Energy](/en/economy/energy)
- [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)
- [Coordinates](/en/universe/coordinates)
