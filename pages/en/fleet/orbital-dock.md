---
wiki_id: 104
locale: "en"
path: "fleet/orbital-dock"
url: "https://wiki.dynastynova.com/en/fleet/orbital-dock"
title: "Orbital Dock (shipyard)"
description: "Building ships and defenses: queues, payment, delivery, build times."
tags: ["fleet"]
published: true
created: "2026-10-02T13:11:07.986Z"
updated: "2026-10-15T19:28:26.518Z"
---

# Orbital Dock (shipyard)

> **In short**: the Orbital Dock builds ships and defenses. Each level speeds production up, and the Molecular Assembler halves it at each level. An order is checked in full when you place it, then each unit is paid when it enters production and delivered as soon as it is done.
{.is-info}

> Ships are not translated in the game yet: it shows their French name in every language. The English names used here are provisional (see [Ships list](/en/fleet/ships)).
{.is-warning}

> **Universe setting**: the shipyard speed divides ship and defense build times.
> Default: **×1** · Redline: **×1**
{.is-info}

> **Universe setting**: the size of build queues may differ from one universe to another.
> Default: **2 orders**, **5 with Premium** · Redline: **2 orders**, **5 with Premium**
{.is-info}

<img src="/images/illustrations/facilities/dock-orbital.jpg" width="180" alt="Orbital Dock">

## Rules

### The building
1. The Orbital Dock is built on a planet **or a moon**. Requirement: Automaton Factory 2. Maximum level: **12**. You need at least level 1 to order a ship or a defense, on top of each unit's own requirements.
2. On a moon the Dock works without a Molecular Assembler, which can only be built on a planet.

### Queues
3. Each base has **a ship queue and a defense queue**, which run **side by side**. Each takes 2 orders (5 with Premium), the running one included (see [Build queues](/en/economy/build-queue)).
4. Ordering the same ship or defense as the **last waiting order** adds to that order, without taking a queue slot. The Defensive Barrier and the Protective Dome, which are unique, never merge.
5. An order holds at least 1 unit and at most **1,000,000**.

### Payment and delivery
6. An order is only accepted if the base can **pay for all of it** when you place it.
7. Each unit is then **paid when it enters production**, not before. If the first one cannot be paid at start, the order is dropped at no cost.
8. Units are **delivered one by one**, each as soon as it is done, and bring their military points at once.
9. After each delivery the next unit is paid. If the base can no longer pay for it, the order **stops there**: delivered units are kept, the others cost nothing.
10. **Time per unit**, in seconds, never under one second:

$$t = \frac{T}{(1 + D) \times 2^{A}} \div v$$

- $t$: build time of one unit, rounded to the second;
- $T$: the unit's base time (table below, and [Defenses list](/en/defense/defenses));
- $D$: the base's Orbital Dock level;
- $A$: the base's Molecular Assembler level;
- $v$: the universe's shipyard speed.

Talent speed bonuses then divide this time, as for buildings (see [Economy formulas](/en/economy/formulas)). The time per unit is set when the order starts; the order lasts that time × the number of units.

### Cancelling
11. Cancelling a **waiting** order costs nothing and refunds nothing.
12. Cancelling a **running** order refunds **80%** of the unit paid but not yet delivered; delivered units are kept, the next ones cost nothing. Talents raise this rate, up to 95%.
13. You can also ask to **stop after the current unit**: it finishes as usual, the rest of the order is dropped at no cost.

### While building
14. As long as the Dock has a ship or defense order, waiting or running, it can be **neither upgraded nor demolished**.
15. While the Dock is being upgraded, no ship or defense can be ordered there. Other buildings go up as usual.

## Worked example

**A Cargo Shuttle** (base time 5,400 s):
- Orbital Dock 4, no Assembler: 5,400 / 5 = **1,080 s** (18 min).
- Orbital Dock 7 and Molecular Assembler 1: 5,400 / (8 × 2) = 337.5, rounded to **338 s**. Ten Shuttles: 3,380 s (56 min 20 s).

**Cancelling**: you order 10 Cargo Shuttles and cancel after the 3rd delivery. The 4th is in production and paid: you get back 80% of its cost, so **1,600 metal and 1,600 crystal**. The 3 delivered Shuttles stay, the next 6 cost nothing.

## Detailed data

### Ship build time by Orbital Dock level (seconds, speed ×1, no talent)

| Ship | Base time (s) | Dock 4 | Dock 8 | Dock 12 | Dock 12 and Assembler 2 |
|---|---|---|---|---|---|
| *Cargo Shuttle* | 5,400 | 1,080 | 600 | 415 | 104 |
| *Stellar Freighter* | 14,400 | 2,880 | 1,600 | 1,108 | 277 |
| *Space Pioneer* | 100,800 | 20,160 | 11,200 | 7,754 | 1,938 |
| *Salvager* | 25,200 | 5,040 | 2,800 | 1,938 | 485 |
| *Scout* | 600 | 120 | 67 | 46 | 12 |
| *Solar Collector* | 2,880 | 576 | 320 | 222 | 55 |
| *Interceptor* | 1,800 | 360 | 200 | 138 | 35 |
| *Assailant* | 5,400 | 1,080 | 600 | 415 | 104 |
| *Corvette* | 28,800 | 5,760 | 3,200 | 2,215 | 554 |
| *Battleship* | 64,800 | 12,960 | 7,200 | 4,985 | 1,246 |
| *Orbital Striker* | 86,400 | 17,280 | 9,600 | 6,646 | 1,662 |
| *Predator* | 79,200 | 15,840 | 8,800 | 6,092 | 1,523 |
| *Annihilator* | 115,200 | 23,040 | 12,800 | 8,862 | 2,215 |
| *Stellar Colossus* | 12,960,000 | 2,592,000 | 1,440,000 | 996,923 | 249,231 |

The Orbital Dock itself: level 1 costs 400 metal, 200 crystal and 100 hydrogen, doubled at each level (see [Buildings list](/en/economy/buildings)).

## Common pitfalls

- **Keep resources for what comes next**: a long order stops as soon as a unit can no longer be paid.
- **Queues are not shared**: ships and defenses progress at the same time, but each queue is capped at 2 orders (5 with Premium).
- **Do not upgrade the Dock mid-production**: it is refused while an order waits or runs.
- **A moon builds slower**: there is no Molecular Assembler on a moon.

## Related pages

- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [Build queues](/en/economy/build-queue)
- [Economy formulas](/en/economy/formulas)
- [Repair Station](/en/economy/repair-station)
- [Buildings list](/en/economy/buildings)
