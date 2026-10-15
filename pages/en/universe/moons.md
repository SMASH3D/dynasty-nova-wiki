---
wiki_id: 86
locale: "en"
path: "universe/moons"
url: "https://wiki.dynastynova.com/en/universe/moons"
title: "Moons"
description: "Moon formation, Lunar base and fields."
tags: ["universe"]
published: false
created: "2026-10-02T13:10:32.724Z"
updated: "2026-10-02T14:16:09.824Z"
---

# Moons

> **In short**: a moon may be born from the debris of a battle fought above a planet. It always goes to the planet's owner, whoever won. It starts with a single field: the Lunar base opens more, within the limit set by its diameter. A moon hosts the Sensor phalanx and the Jump gate, and cannot be scanned by a phalanx.
{.is-info}

> **Universe setting**: the maximum chance of forming a moon and the amount of debris that reaches it may differ from one universe to another.
> Default: **20% at most, at 2,000,000 debris** · Redline: **20% at most, at 2,000,000 debris**
{.is-info}

## Rules

### Formation
1. At the end of a battle above a planet, a moon may form. The chance depends on **that battle's debris** (metal and crystal): a debris field already in orbit, left by earlier battles, does not count.
2. **Chance** = battle debris × maximum chance / debris for the maximum chance, capped at the maximum chance (formula below). Below one point of chance (100,000 debris by default), no moon can form.
3. The moon goes **to the planet's owner**, whether the battle was won or lost. An attacker never gains a moon in orbit of a planet that is not theirs.
4. Forming a moon does not use up the debris: recyclers collect the whole debris field.
5. A position holds **at most one moon**. As long as the planet has its moon, no battle forms another one.
6. The higher the chance was, the **bigger** the moon: its diameter sets the maximum number of fields it will offer (table below). The battle notification gives its diameter.
7. In a universe where **giant impacts** are switched on (cosmic events, closed by default), a moon can also be born from an impact.

### Development
8. A moon is born **empty**: no resources, no buildings, **a single field**, and its planet's name (it can be renamed).
9. The **Lunar base** is built first: no other building can be started on the moon before it. It cannot be demolished.
10. Each Lunar base level **opens 3 fields and takes one**, a net 2 fields per level.
11. A moon's fields never go past its **cap**: whole part of ((diameter / 1,000)²). Beyond it, raising the Lunar base opens nothing more. Some dynasty talents add fields per level or lift that cap.
12. Buildings possible on a moon: Lunar base, Sensor phalanx, Jump gate, Automaton Factory, Orbital Dock (table below).
13. A moon **produces nothing** and stores 10,000 of each resource (see [Storage](/en/economy/storage)).

### Living with a moon
14. The flight between a planet and its moon has a distance of **5**: a very short trip, but a real flight.
15. A moon can be spied on, attacked, destroyed by Stellar Colossi (see [Moon destruction](/en/combat/moon-destruction)), and receive transports. It cannot be colonized, and it does not take a colony slot.
16. A **Sensor phalanx** can never scan a moon: a fleet stationed there stays invisible.
17. Abandoning a planet also abandons its moon and everything on it; recolonizing that planet hands it back with its moon.

## Formulas

$$ C = \min\left(D \times \frac{C_{max}}{D_{max}},\ C_{max}\right) \quad \text{if } D \geq \frac{D_{max}}{C_{max}},\ \text{otherwise } 0 $$

- $C$: chance of forming a moon, in %;
- $D$: metal and crystal debris left by that battle;
- $C_{max}$: the universe's maximum chance (20% by default);
- $D_{max}$: debris that gives the maximum chance (2,000,000 by default).

$$ K = \left\lfloor \left( \frac{d}{1{,}000} \right)^2 \right\rfloor $$

- $K$: the moon's field cap;
- $d$: its diameter, in kilometers.

## Worked example

A battle leaves **1,000,000** debris above your planet, in a universe with default settings:
- Moon chance: 1,000,000 × 20 / 2,000,000 = **10%**.
- If the moon forms, its diameter is between **6,324 and 7,071 km**, a cap of **39 to 49 fields**.
- With a cap of 39 fields, the Lunar base reaches that cap at level **13** (1 + 3 × 13 = 40 fields opened, brought down to 39).
- The debris field stays whole for your recyclers.

## Detailed data

### Chance by battle debris (default settings)

| Battle debris | Moon chance |
|---|---|
| 50,000 | 0% |
| 100,000 | 1% |
| 500,000 | 5% |
| 1,000,000 | 10% |
| 2,000,000 | 20% |
| 5,000,000 | 20% |

### Moon size by chance (default settings)

| Battle chance | Matching debris | Diameter (km) | Field cap |
|---|---|---|---|
| 1% | 100,000 | 3,605 to 4,795 | 12 to 22 |
| 2% | 200,000 | 4,000 to 5,099 | 16 to 25 |
| 5% | 500,000 | 5,000 to 5,916 | 25 to 34 |
| 10% | 1,000,000 | 6,324 to 7,071 | 39 to 49 |
| 15% | 1,500,000 | 7,416 to 8,062 | 54 to 64 |
| 20% | 2,000,000 | 8,366 to 8,944 | 69 to 79 |

### Lunar base level by level

Cost of level N: level 1 cost × 2^(N − 1). Fields opened are capped by the moon's diameter.

| Level | Metal | Crystal | Hydrogen | Fields opened | Free fields (Lunar base only) |
|---|---|---|---|---|---|
| 1 | 20,000 | 40,000 | 20,000 | 4 | 3 |
| 2 | 40,000 | 80,000 | 40,000 | 7 | 5 |
| 3 | 80,000 | 160,000 | 80,000 | 10 | 7 |
| 4 | 160,000 | 320,000 | 160,000 | 13 | 9 |
| 5 | 320,000 | 640,000 | 320,000 | 16 | 11 |
| 6 | 640,000 | 1,280,000 | 640,000 | 19 | 13 |
| 7 | 1,280,000 | 2,560,000 | 1,280,000 | 22 | 15 |
| 8 | 2,560,000 | 5,120,000 | 2,560,000 | 25 | 17 |
| 9 | 5,120,000 | 10,240,000 | 5,120,000 | 28 | 19 |
| 10 | 10,240,000 | 20,480,000 | 10,240,000 | 31 | 21 |
| 11 | 20,480,000 | 40,960,000 | 20,480,000 | 34 | 23 |
| 12 | 40,960,000 | 81,920,000 | 40,960,000 | 37 | 25 |
| 13 | 81,920,000 | 163,840,000 | 81,920,000 | 40 | 27 |
| 14 | 163,840,000 | 327,680,000 | 163,840,000 | 43 | 29 |
| 15 | 327,680,000 | 655,360,000 | 327,680,000 | 46 | 31 |

### Moon buildings

| Building | Level 1 cost (metal / crystal / hydrogen) | Factor per level | Requirements | Max level |
|---|---|---|---|---|
| Lunar base | 20,000 / 40,000 / 20,000 | ×2 | none | none (the diameter caps the fields) |
| Sensor phalanx | 20,000 / 40,000 / 20,000 | ×2 | Lunar base 1 | none |
| Jump gate | 2,000,000 / 4,000,000 / 2,000,000 | ×2 | Lunar base 1, Hyperspace Technology 7 | none |
| Automaton Factory | 400 / 120 / 200 | ×2 | Lunar base 1 | 10 |
| Orbital Dock | 400 / 200 / 100 | ×2 | Lunar base 1, Automaton Factory 2 | 12 |

## Common pitfalls

- **A large debris field already in orbit is no help**: only the debris of the battle that just took place counts.
- **Defenses leave no debris** in a universe with default settings: only destroyed ships feed the moon chance.
- **A small moon stays small**: its cap is set at birth, and the Lunar base never goes past it.
- **A moon is not a shelter from everything**: invisible to the phalanx, it can still be attacked or destroyed.

## Related pages

- [Debris fields](/en/combat/debris)
- [Moon destruction](/en/combat/moon-destruction)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Jump gate](/en/fleet/jump-gate)
- [List of buildings](/en/economy/buildings)
