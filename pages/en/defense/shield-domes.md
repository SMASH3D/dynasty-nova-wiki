---
wiki_id: 111
locale: "en"
path: "defense/shield-domes"
url: "https://wiki.dynastynova.com/en/defense/shield-domes"
title: "Defensive Barrier and Protective Dome"
description: "The two planetary shields."
tags: ["defense"]
published: true
created: "2026-10-02T13:11:21.637Z"
updated: "2026-10-15T18:52:40.730Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Defensive Barrier and Protective Dome

> **In short**: the Defensive Barrier and the Protective Dome are defenses with a very large shield, limited to one of each per planet. They soak up shots for themselves only: they do not protect other units.
{.is-info}

<img src="/images/illustrations/defense/barriere-defensive.jpg" width="180" alt="Defensive Barrier"> <img src="/images/illustrations/defense/dome-protecteur.jpg" width="180" alt="Protective Dome">

## Rules

1. **Only one of each** per planet. An order can only be for one unit, and it is refused if there is already one on the planet or in the queue.
2. In battle they are **ordinary targets** with a large individual shield. They **do not create a global shield** around the planet.
3. They barely fire (attack 1): their job is to absorb shots.
4. A shot below 1% of their shield bounces off with no effect (see [How combat works](/en/combat/how-combat-works)).
5. Like any defense, they can be rebuilt for free after a battle (see [Defense rebuild](/en/combat/defense-rebuild)). If they are lost, you may build another one.
6. Against missiles, they count shield + hull like every other defense. Without a designated target, Warheads hit the toughest defense first: often the Dome. Destroyed by Warheads, they are lost (see [Missiles](/en/defense/missiles)).

## Worked example

**A Protective Dome with no research** (shield 10,000, hull 10,000)
- 1% threshold: 100. An Interceptor (ship, attack 50) falls below it: **every one of its shots bounces**, the Dome loses nothing.
- A Battleship (attack 1,000) clears the threshold: 10 shots empty the shield, the next ones hit the hull.

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).

**The same Dome against Long-Range Warheads**
- Toughness: 10,000 + 10,000 = **20,000**. A Warhead deals 12,000 damage with no research: it takes **2** that get past the Interception Missiles.
- With Shielding Technology 6 and Armor Technology 6 on the defender's side, toughness rises to 32,000: a shooter with no research needs **3** Warheads, but one at Weapon Systems 4 (16,800 per Warhead) needs **2**.

## Detailed data

|  | Defensive Barrier | Protective Dome |
|---|---|---|
| Cost (metal / crystal) | 10,000 / 10,000 | 50,000 / 50,000 |
| Points | 20 | 100 |
| Structure | 20,000 | 100,000 |
| Combat hull | 2,000 | 10,000 |
| Shield | 2,000 | 10,000 |
| Attack | 1 | 1 |
| Base time | 8 h | 1 d 16 h |
| Requirements | Orbital Dock 1, Shielding Technology 2 | Orbital Dock 6, Shielding Technology 6 |
| Copies | 1 | 1 |
| Toughness against Warheads (no research) | 4,000 | 20,000 |

The base time is divided by (1 + Orbital Dock level) and by 2 for each Molecular Assembler level (see [Defenses list](/en/defense/defenses)).

## Common pitfalls

- **No protective bubble**: your other defenses and ships remain exposed.
- **The Dome draws Warheads**: it is often the toughest defense, hence the first one hit by a salvo with no designated target.
- **No second order in the queue**: while a Dome is in the queue, a second one is refused.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
- [How combat works](/en/combat/how-combat-works)
- [Defense rebuild](/en/combat/defense-rebuild)
