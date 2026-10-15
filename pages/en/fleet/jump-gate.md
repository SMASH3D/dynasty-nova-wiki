---
wiki_id: 108
locale: "en"
path: "fleet/jump-gate"
url: "https://wiki.dynastynova.com/en/fleet/jump-gate"
title: "Jump gate"
description: "Moving a fleet instantly between two moons."
tags: ["fleet", "moon"]
published: true
created: "2026-10-02T13:11:15.751Z"
updated: "2026-10-02T17:40:23.324Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Jump gate

> **In short**: the Jump gate is built on a moon. It sends ships instantly to another of your moons with a Gate, with no flight time and no hydrogen. It carries no resources, and both gates must then recharge.
{.is-info}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Jump gate">

## Rules

1. The Jump gate can **only be built on a moon**. Requirements: **Lunar base 1** and **Hyperspace Technology 7**. It has no maximum level; its cost doubles at each level.
2. A jump links **two different moons that you own**, in the same universe, each with a ready Jump gate. You cannot jump to another player's moon, not even an ally's.
3. The jump is **instant** and burns **no hydrogen**. It takes no fleet slot.
4. **Hulls only**: no resources go through.
5. After a jump, **both gates**, departure and arrival, recharge, each by its own level (table below). The recharge does not depend on universe speeds.
6. Both moons are checked before anything moves: a refused jump (gate recharging, moon without a Gate) moves nothing and starts no recharge.
7. Navigator talents shorten the recharge (by up to 30%) or allow two jumps before recharging (see [Navigator](/en/dynasty/classes/navigator)).

## Worked example

You have a level 3 Jump gate on moon A and a level 1 on moon B. You jump your fleet from A to B.
- The fleet lands on B at once, without spending hydrogen.
- Gate A recharges in **47 minutes** (level 3), gate B in **60 minutes** (level 1).
- A new jump from B, or to A, is only possible once the gate in question has recharged.

With a recharge cut by 30% through talents, a level 5 gate goes from 36 to **25 minutes**.

## Detailed data

### Recharge by level

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 and above |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recharge (minutes) | 60 | 53 | 47 | 41 | 36 | 31 | 27 | 23 | 19 | 17 | 14 | 13 | 11 | 10 |

### Cost

| Level | Metal | Crystal | Hydrogen |
|---|---|---|---|
| 1 | 2,000,000 | 4,000,000 | 2,000,000 |
| 2 | 4,000,000 | 8,000,000 | 4,000,000 |
| 3 | 8,000,000 | 16,000,000 | 8,000,000 |
| 4 | 16,000,000 | 32,000,000 | 16,000,000 |
| 5 | 32,000,000 | 64,000,000 | 32,000,000 |

The cost keeps doubling at higher levels.

## Common pitfalls

- **The recharge hits both ends**: upgrading only the departure gate is not enough to chain jumps.
- **No resources**: a loaded fleet must unload its cargo first.
- **You need two moons of your own**: a single Gate is useless, and so is an ally's.
- **Past level 14 the recharge stops dropping**: it stays at 10 minutes.

## Related pages

- [Moons](/en/universe/moons)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Fleet movement](/en/fleet/movement)
- [Buildings list](/en/economy/buildings)
