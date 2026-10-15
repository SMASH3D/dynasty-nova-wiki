---
wiki_id: 110
locale: "en"
path: "defense/defenses"
url: "https://wiki.dynastynova.com/en/defense/defenses"
title: "Defenses list"
description: "Defenses: costs, stats, requirements."
tags: ["defense"]
published: true
created: "2026-10-02T13:11:19.721Z"
updated: "2026-10-15T18:52:37.806Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Defenses list

> **In short**: defenses protect your planet around the clock. They never move, cannot be plundered and take part in every battle fought on their planet. The game has 8 of them, two of which are unique (Defensive Barrier and Protective Dome). Missiles are built at the same place but never fight: see [Missiles](/en/defense/missiles).
{.is-info}

> **Universe setting**: the share of destroyed defenses that turns into a debris field may differ from one universe to another.
> Default: **0%** · Redline: **0%**
{.is-info}

> **Universe setting**: the shipyard speed divides the build time of defenses.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

### Building
1. Defenses are built at the **Orbital Dock**, on a planet or on a moon that has one.
2. While the Orbital Dock is being upgraded, **no defense order** is accepted.
3. Defenses have **their own queue**, separate from the ships' queue: both run at the same time. The queue holds **2 orders** (**5** with Premium), the running one included (see [Build queues](/en/economy/build-queue)).
4. When you order, the planet must hold the resources for **the whole quantity**. Each unit is then paid when it enters production; if the next unit can no longer be paid, the order stops there.
5. Ordering a defense that is already waiting in the queue adds to that order, without taking another queue slot.
6. **Time per unit**, in seconds, never less than one second:
$$t = \frac{T}{(1 + D) \times 2^{A}} \div v$$
   - $T$: the defense's base time (table below); $D$: Orbital Dock level; $A$: Molecular Assembler level; $v$: the universe's shipyard speed.
   - Shipyard speed bonuses (dynasty talents, alliance) then divide this time.

### In battle
7. Each defense fires **once per round** and only fights where it is built (planet or moon).
8. Attack, shield and structure grow by **10% per level** of Weapon Systems, Shielding Technology and Armor Technology. In battle, the **hull** is the structure divided by 10.
9. Defenses have **no rapid fire**. Some ships have rapid fire against them (table below).
10. After a battle, part of the destroyed defenses is rebuilt for free: see [Defense rebuild](/en/combat/defense-rebuild). A defense destroyed by a missile is lost (see [Missiles](/en/defense/missiles)).
11. Destroyed defenses leave **no debris field**, unless the universe says otherwise.

### Uniqueness and points
12. **Defensive Barrier and Protective Dome**: one of each per planet. You cannot order more than one at a time, nor order one while there is one on the planet or in the queue.
13. **Points**: each defense earns 1 point per 1,000 resources of its cost (metal, crystal and hydrogen), counted in military points.

## Worked example

**Ordering 20 Ballistic Projectors with an Orbital Dock at level 4** (Molecular Assembler 0, speed ×1)
- Cost: 20 × 2,000 = **40,000 metal**, to be on the planet when you order; **40 military points** once built.
- One unit: 2,880 / (1 + 4) = **576 seconds**.
- The whole order: 20 × 576 = 11,520 seconds, that is **3 h 12 min**.

**An Ion Battery in battle** with Weapon Systems 5, Shielding Technology 4 and Armor Technology 6
- Attack: 150 × 1.5 = **225**.
- Shield: 500 × 1.4 = **700**.
- Hull: 8,000 × 1.6 / 10 = **1,280**.

## Detailed data

### Costs and base stats (no research)

| Defense | Metal | Crystal | Hydrogen | Points | Structure | Combat hull | Shield | Attack | Base time |
|---|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/projecteur-balistique.jpg" width="48" alt="Ballistic Projector"> Ballistic Projector | 2,000 | 0 | 0 | 2 | 2,000 | 200 | 20 | 80 | 48 min |
| <img src="/images/illustrations/defense/canon-photonique.jpg" width="48" alt="Photonic Cannon"> Photonic Cannon | 1,500 | 500 | 0 | 2 | 2,000 | 200 | 25 | 100 | 48 min |
| <img src="/images/illustrations/defense/emetteur-a-haute-energie.jpg" width="48" alt="High-Energy Emitter"> High-Energy Emitter | 6,000 | 2,000 | 0 | 8 | 8,000 | 800 | 100 | 250 | 3 h 12 min |
| <img src="/images/illustrations/defense/batterie-ionique.jpg" width="48" alt="Ion Battery"> Ion Battery | 2,000 | 6,000 | 0 | 8 | 8,000 | 800 | 500 | 150 | 3 h 12 min |
| <img src="/images/illustrations/defense/accelerateur-magnetique.jpg" width="48" alt="Magnetic Accelerator"> Magnetic Accelerator | 20,000 | 15,000 | 2,000 | 37 | 35,000 | 3,500 | 200 | 1,100 | 14 h |
| <img src="/images/illustrations/defense/ejecteur-a-plasma.jpg" width="48" alt="Plasma Ejector"> Plasma Ejector | 50,000 | 50,000 | 30,000 | 130 | 100,000 | 10,000 | 300 | 3,000 | 1 d 4 h |
| <img src="/images/illustrations/defense/barriere-defensive.jpg" width="48" alt="Defensive Barrier"> Defensive Barrier | 10,000 | 10,000 | 0 | 20 | 20,000 | 2,000 | 2,000 | 1 | 8 h |
| <img src="/images/illustrations/defense/dome-protecteur.jpg" width="48" alt="Protective Dome"> Protective Dome | 50,000 | 50,000 | 0 | 100 | 100,000 | 10,000 | 10,000 | 1 | 1 d 16 h |

The base time is that of one unit with an Orbital Dock at level 0; the Dock then divides it (rule 6).

### Requirements

| Defense | Requirements | Copies per planet |
|---|---|---|
| Ballistic Projector | Orbital Dock 1 | unlimited |
| Photonic Cannon | Orbital Dock 2, Laser Technology 3 | unlimited |
| High-Energy Emitter | Orbital Dock 4, Laser Technology 6, Energy Science 3 | unlimited |
| Ion Battery | Orbital Dock 4, Ion Technology 4 | unlimited |
| Magnetic Accelerator | Orbital Dock 6, Weapon Systems 3, Shielding Technology 1, Energy Science 6 | unlimited |
| Plasma Ejector | Orbital Dock 8, Plasma Technology 7 | unlimited |
| Defensive Barrier | Orbital Dock 1, Shielding Technology 2 | 1 |
| Protective Dome | Orbital Dock 6, Shielding Technology 6 | 1 |

### Time per unit by Orbital Dock level

Molecular Assembler 0, shipyard speed ×1, no bonus. "no": Dock level too low.

| Defense | Dock 2 | Dock 4 | Dock 6 | Dock 8 | Dock 10 | Dock 12 |
|---|---|---|---|---|---|---|
| Ballistic Projector | 16 min | 9 min 36 s | 6 min 51 s | 5 min 20 s | 4 min 22 s | 3 min 42 s |
| Photonic Cannon | 16 min | 9 min 36 s | 6 min 51 s | 5 min 20 s | 4 min 22 s | 3 min 42 s |
| High-Energy Emitter | no | 38 min 24 s | 27 min 26 s | 21 min 20 s | 17 min 27 s | 14 min 46 s |
| Ion Battery | no | 38 min 24 s | 27 min 26 s | 21 min 20 s | 17 min 27 s | 14 min 46 s |
| Magnetic Accelerator | no | no | 2 h | 1 h 33 min 20 s | 1 h 16 min 22 s | 1 h 4 min 37 s |
| Plasma Ejector | no | no | no | 3 h 6 min 40 s | 2 h 32 min 44 s | 2 h 9 min 14 s |
| Defensive Barrier | 2 h 40 min | 1 h 36 min | 1 h 8 min 34 s | 53 min 20 s | 43 min 38 s | 36 min 55 s |
| Protective Dome | no | no | 5 h 42 min 51 s | 4 h 26 min 40 s | 3 h 38 min 11 s | 3 h 4 min 37 s |

Each Molecular Assembler level halves these times again.

### Ships with rapid fire against defenses

| Defense | Rapid fire taken |
|---|---|
| Ballistic Projector | Orbital Striker 20, Corvette 10, Stellar Colossus 200 |
| Photonic Cannon | Orbital Striker 20, Annihilator 10, Stellar Colossus 200 |
| High-Energy Emitter | Orbital Striker 10, Stellar Colossus 100 |
| Ion Battery | Orbital Striker 10, Stellar Colossus 100 |
| Magnetic Accelerator | Orbital Striker 5, Stellar Colossus 50 |
| Plasma Ejector | Orbital Striker 5 |
| Defensive Barrier | none |
| Protective Dome | none |

Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).

## Common pitfalls

- **The Orbital Dock blocks orders while it is upgraded**: queue your defenses before upgrading it.
- **A large order can stop halfway**: each unit is paid in turn. If you spend the resources elsewhere meanwhile, the order stops at the last unit paid.
- **The Orbital Striker is the bane of defenses**: it has rapid fire against almost all of them. Against it, the Plasma Ejector and the two shields hold best.
- **Defenses give the attacker nothing**: by default they leave no debris field. A heavily defended planet is costly to attack and gives nothing back in debris.

## Related pages

- [Missiles](/en/defense/missiles)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Defense rebuild](/en/combat/defense-rebuild)
- [How combat works](/en/combat/how-combat-works)
- [Rapid fire](/en/fleet/rapid-fire)
- [Build queues](/en/economy/build-queue)
