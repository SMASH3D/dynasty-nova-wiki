---
wiki_id: 114
locale: "en"
path: "combat/how-combat-works"
url: "https://wiki.dynastynova.com/en/combat/how-combat-works"
title: "How combat works"
description: "Rounds, shots, shields, explosions and outcome."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:27.663Z"
updated: "2026-10-02T16:38:19.380Z"
---

# How combat works

> **In short**: a battle lasts at most 6 rounds. Each round, shields recharge, the attacker fires, then the defender. Each shot targets a random enemy unit and always hits. A shot that is too weak bounces off shields; hull damage, however, carries over from one round to the next and can make the unit hit explode.
{.is-info}

## Rules

### Combat stats
1. Each unit fights with three values: **attack**, **shield** and **hull**. They start from the catalogue stats ([ships](/en/fleet/ships), [defenses](/en/defense/defenses)) and grow with three research technologies, by **10% per level**: Weapon Systems for attack, Shielding Technology for shield, Armor Technology for hull.
2. The **combat hull** is one tenth of the structure.
3. The **Weapons doctrine** and **Protection doctrine** alliance talents each add **5%**: the first to attack, the second to shield and hull. They apply after research, once the member's settling-in period is over.
4. [Dynasty and class talents](/en/dynasty/talents) can add their own percentages. They add up with the doctrine and the total is applied once.

$$A = \mathrm{round}\left(A_0 (1 + 0.1\,W)\right) \times \left(1 + \frac{b_A}{100}\right) \qquad B = \mathrm{round}\left(B_0 (1 + 0.1\,S)\right) \times \left(1 + \frac{b_P}{100}\right) \qquad C = \frac{\mathrm{round}\left(T (1 + 0.1\,M)\right)}{10} \times \left(1 + \frac{b_P}{100}\right)$$

- $A$, $B$, $C$: attack, shield and combat hull; $A_0$, $B_0$: catalogue attack and shield; $T$: catalogue structure.
- $W$, $S$, $M$: Weapon Systems, Shielding Technology and Armor Technology levels.
- $b_A$: Weapons doctrine plus attack talents, in %; $b_P$: Protection doctrine plus shield or hull talents, in %.
- $\mathrm{round}$: rounded to the nearest integer. The hull is rounded to an integer; the last product is rounded down.

### How a round unfolds
5. A battle has **at most 6 rounds**. It stops as soon as one side has no units left.
6. At the start of each round, **all shields recharge** fully. The **hull is not repaired**: damage taken in earlier rounds stays.
7. **The attacker fires, then the defender.** Every unit alive at the start of the round fires, even if it is destroyed during the round: in practice, fire is simultaneous.
8. Each unit fires **one shot per round**, at an **enemy unit picked at random** among the units still alive, all kinds together. **Every shot hits.**

### Rapid fire
9. After each shot, if the shooter has [rapid fire](/en/fleet/rapid-fire) with factor $f$ against the unit it just targeted, it fires again with a chance of $(f - 1) / f$, at a **new randomly picked target**. It keeps going as long as the roll succeeds.
10. Rapid fire therefore gives extra shots; it does not steer shots towards the units it counters. Against targets all of the same type, a factor $f$ gives $f$ shots on average.
11. In the catalogue, only ships have rapid fire. Defenses fire once per round.

### Damage
12. **1% rule**: a shot dealing less than **1% of the target's maximum shield** **bounces** with no effect at all.
13. Otherwise, the **shield absorbs** damage as long as it lasts, and the rest goes entirely to the **hull**. At zero hull, the unit is destroyed.
14. **Explosion**: after every shot that did not bounce, if the target's hull is **below 70%** of its combat hull, it explodes with a chance of **1 − share of hull left**. A shot absorbed by the shield also opens this roll, since the hull was already damaged; a bounced shot never does.

### Outcome
15. **Attacker wins** if the defender has no units left; **defender wins** if the attacker has no units left; otherwise it is a **draw**: both sides still standing after 6 rounds, or both wiped out.
16. A unit that survives the battle **leaves intact**: hull damage only lasts for the battle.
17. Silo missiles do not fight: they are ammunition, fired by another mission.
18. Then come [plunder](/en/combat/plunder) (victory only), the [debris field](/en/combat/debris) and the moon chance, the [defense rebuild](/en/combat/defense-rebuild) and the [Repair Station](/en/economy/repair-station).

### Chance
19. The chance in a battle (targets, rapid fire, explosions) is set when the fleet arrives: replayed, the same battle gives exactly the same result, shot for shot. The rolls that follow (defense rebuild, moon) are set by that battle too.

## Worked example

**A Battleship with no research**: attack 1,000, shield 200, combat hull 60,000 / 10 = **6,000**.

**The same Battleship with Weapon Systems, Shielding Technology and Armor Technology at level 10, and both doctrines**:
- Attack: 1,000 × 2 = 2,000, then × 1.05 = **2,100**.
- Shield: 200 × 2 = 400, then × 1.05 = **420**.
- Hull: 60,000 × 2 / 10 = 12,000, then × 1.05 = **12,600**.

**This Battleship with no research fires at an Interceptor with no research** (shield 10, hull 400): the shield absorbs 10, the hull takes 990. The Interceptor is **destroyed**.

**4 Interceptors fire at this Battleship** (attack 50):
- 1% threshold: 2. The shots go through.
- The 4 shots (200 in total) empty the shield (200), **without touching the hull**. Next round, the shield is full again.

**An Interceptor fires at a Protective Dome** (shield 10,000): the 1% threshold is 100, the 50 shot **bounces**. Interceptors can do nothing against the Dome, however many there are.

**A unit whose hull has dropped to 60%**: on every shot that does not bounce, it explodes with a chance of 1 − 0.60 = **40%**.

**A Stellar Colossus against a fleet of Interceptors**: its rapid fire of 200 gives it 200 shots per round on average.

## Detailed data

Combat stats with no research and no bonus. Each research level adds 10% of the base value. Ship names are provisional translations: the game still shows the French names.

| Unit | Attack | Shield | Combat hull | Shots bounce below |
|---|---|---|---|---|
| Cargo Shuttle | 5 | 10 | 400 | 0.1 |
| Stellar Freighter | 5 | 25 | 1,200 | 0.25 |
| Space Pioneer | 50 | 100 | 3,000 | 1 |
| Salvager | 1 | 10 | 1,600 | 0.1 |
| Scout | 0 | 0 | 100 | 0 |
| Solar Collector | 1 | 1 | 200 | 0.01 |
| Interceptor | 50 | 10 | 400 | 0.1 |
| Assailant | 150 | 25 | 1,000 | 0.25 |
| Corvette | 400 | 50 | 2,700 | 0.5 |
| Battleship | 1,000 | 200 | 6,000 | 2 |
| Orbital Striker | 1,000 | 500 | 7,500 | 5 |
| Predator | 700 | 400 | 7,000 | 4 |
| Annihilator | 2,000 | 500 | 11,000 | 5 |
| Stellar Colossus | 200,000 | 50,000 | 900,000 | 500 |
| Ballistic Projector | 80 | 20 | 200 | 0.2 |
| Photonic Cannon | 100 | 25 | 200 | 0.25 |
| High-Energy Emitter | 250 | 100 | 800 | 1 |
| Ion Battery | 150 | 500 | 800 | 5 |
| Magnetic Accelerator | 1,100 | 200 | 3,500 | 2 |
| Plasma Ejector | 3,000 | 300 | 10,000 | 3 |
| Defensive Barrier | 1 | 2,000 | 2,000 | 20 |
| Protective Dome | 1 | 10,000 | 10,000 | 100 |

## Common pitfalls

- **Small shots crash on shields**: weak units, even in numbers, may never scratch a big target, since its shield recharges every round.
- **Targets are random**: you do not choose what your ships aim at. Numerous, cheap units soak up many shots.
- **6 rounds, no more**: if nobody is wiped out, it is a draw and the attacker plunders nothing.
- **Wounds matter**: a damaged unit explodes more easily in later rounds. A burst of small shots can finish off a target that is already hit.

## Related pages

- [Rapid fire](/en/fleet/rapid-fire)
- [Ship list](/en/fleet/ships)
- [Defense list](/en/defense/defenses)
- [Plunder](/en/combat/plunder)
- [Reading a battle report](/en/combat/battle-report)
- [Battle simulator](/en/combat/simulator)
