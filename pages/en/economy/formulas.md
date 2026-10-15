---
wiki_id: 92
locale: "en"
path: "economy/formulas"
url: "https://wiki.dynastynova.com/en/economy/formulas"
title: "Economy formulas"
description: "Costs, durations, production and points."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:44.388Z"
updated: "2026-10-15T19:28:24.872Z"
---

# Economy formulas

> **In short**: every economy formula, as the game computes it: cost and points of a level, time for buildings, ships, defenses and research, production, energy and storage. Every speed bonus divides a time, every production bonus adds to the mines' gross output.
{.is-info}

> **Universe setting**: the economy, construction, research and shipyard speeds may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

### Cost and points
1. Cost of level $N$ of a building or a research, for each resource:
$$C_N = \left\lfloor C_1 \times f^{N-1} \right\rfloor$$
   - $C_1$: level 1 cost; $f$: the building's or research's factor (see [Buildings list](/en/economy/buildings)).
   - Required energy follows the same formula; only the Repair Station has a different energy factor (2.5 instead of 5).
2. A ship or a defense always costs the same per unit.
3. **Points**: $P = (M + C + H) / 1{,}000$, where $M$, $C$ and $H$ are the metal, crystal and hydrogen spent. Required energy does not count.

### Times
4. **Building**, in hours:
$$t = \frac{M + C + H}{2{,}500 \times (1 + F) \times 2^{A}} \div v_c \div \left(1 + \frac{b}{100}\right)$$
   - $M + C + H$: the level's cost; $F$: Automaton Factory level; $A$: Molecular Assembler level; $v_c$: the universe's construction speed; $b$: speed bonuses in %, added up (Associated builders alliance talent, dynasty talents).
   - The result is rounded to the second. A demolition takes half the construction time of the level removed, without speed bonuses.
5. **Ship or defense**, in seconds per unit, never under one second:
$$t = \frac{T}{(1 + D) \times 2^{A}} \div v_{sh}$$
   - $T$: the unit's base time (for instance 5,400 s for a Cargo Shuttle, 2,880 s for a Solar Collector); $D$: Orbital Dock level; $A$: Molecular Assembler level; $v_{sh}$: the universe's shipyard speed. Shipyard speed bonuses (talents) then divide the time as for buildings.
6. **Research**, in hours:
$$t = \frac{M + C}{1{,}000 \times (1 + L)} \div v_r$$
   - $M + C$: the level's metal and crystal, without hydrogen; $L$: effective Innovation Center level, laboratory network included (see [Research](/en/research)); $v_r$: the universe's research speed. Speed bonuses (Networked innovation centers, talents) divide the time as for buildings.

### Production and energy (per hour, at level $N$)
7. Mineral Excavator: $30 \times N \times 1.1^N$ metal; Crystal Extractor: $20 \times N \times 1.1^N$ crystal; Hydrogen Condenser: $10 \times N \times 1.1^N \times k_H$ hydrogen, with $k_H = 1.44 - 0.004 \times T_{max}$ (never negative). All multiplied by the economy speed.
8. Energy use of each mine: $10 \times N \times 1.1^N$, without the economy speed.
9. Photovoltaic Sensors: $20 \times N \times 1.1^N \times (1 + T / 100)$, with $T$ the current temperature, counted as 0 when negative.
10. Thermonuclear Reactor: $30 \times N \times (1.05 + 0.01 \times S)^N$ energy, $S$ being the Energy Science level; it burns $10 \times N \times 1.1^N$ hydrogen, multiplied by the economy speed.
11. Solar Collector: $\lfloor T_{max} / 4 + 20 \rfloor$ energy per unit, never negative.
12. Production bonuses: Plasma Technology (+1% metal, +0.66% crystal, +0.33% hydrogen per level), Coordinated extraction (+5% per level), the colonies' position bonus, dynasty and talents. Each is computed on the mines' gross output and rounded down, and they add up.
13. Energy deficit: the mines' output, bonuses included, is multiplied by $\min(1, \text{production} / \text{consumption})$. Then come the Planetary Base's 20 metal and 10 crystal, multiplied by the economy speed.

### Storage
14. Capacity of a storage building at level $N$: $5{,}000 \times \lfloor 2.5 \times e^{20N/33} \rfloor$. Planetary Base: 10,000 per resource. Bonuses (Logistics Center +10% per level, Federated warehouses +10% per level, talents) added up and applied to the whole capacity.

$T_{max}$: the planet's maximum temperature, in °C.

## Worked example

Raising the Orbital Dock from level 6 to level 7 with an Automaton Factory level 6, a Molecular Assembler level 1, the Associated builders talent at level 2 (+20%), speed ×1:
- Level 7 cost: 400 × 2^6 = 25,600 metal, 12,800 crystal, 6,400 hydrogen, so 44,800 resources and 44.8 points.
- Base time: 44,800 / (2,500 × 7 × 2) hours = **4,608 seconds**.
- With +20% speed: 4,608 / 1.2 = **3,840 seconds** (1 h 04 min).

A Cargo Shuttle then built at Orbital Dock 7 with Assembler 1: 5,400 / (8 × 2) = **338 seconds** per unit.

## Detailed data

### What each universe speed changes

| Speed | Effect |
|---|---|
| Economy | Multiplies the output of the mines, of the Planetary Base and the Reactor's hydrogen use; changes neither energy nor energy use |
| Construction | Divides building and demolition times |
| Research | Divides research times |
| Shipyard | Divides ship and defense times, speeds up the Repair Station |
| Fleet | See [Movement](/en/fleet/movement) |

## Common pitfalls

- **Hydrogen counts in a building's time**: a building that costs hydrogen takes longer than a mine with the same metal and crystal total. In research, it does not count.
- **Speed bonuses do not cut by their percentage**: +20% speed divides the time by 1.2, so about 17% less.
- **The Molecular Assembler halves at every level**: buildings, ships and defenses.

## Related pages

- [Resources](/en/economy/resources)
- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Buildings list](/en/economy/buildings)
- [Build queues](/en/economy/build-queue)
