---
wiki_id: 95
locale: "en"
path: "economy/repair-station"
url: "https://wiki.dynastynova.com/en/economy/repair-station"
title: "Repair Station"
description: "Recovering part of the ships destroyed while defending."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:50.356Z"
updated: "2026-10-15T18:52:50.833Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Repair Station

> **In short**: after a battle in which your planet lost ships in defense, the Repair Station recovers part of them and gives them back repaired, after 30 minutes to 12 hours. The recovered share grows with its level. It takes no field.
{.is-info}

> **Universe setting**: the recovered share depends on the universe's debris rate, and repair time on its shipyard speed.
> Default: debris **30%**, shipyard **×1** · Redline: debris **30%**, shipyard **×1**
{.is-info}

<img src="/images/illustrations/facilities/station-de-reparation.jpg" width="180" alt="Repair Station">

## Rules

1. The Station steps in after **any battle in which your planet defends and loses ships**, whether you win or lose the battle.
2. It recovers part of the destroyed ships: **share = level coefficient × (1 − debris rate)**. The coefficient goes from 45% at level 1 to 54% at level 10; some talents raise it.
3. The share applies **to each ship type separately**, rounded down: a few losses may recover nothing.
4. **There is no roll**: the share is fixed.
5. **Time**: the Station repairs **10 structure points per second per level**, multiplied by the universe's shipyard speed. The time is between **30 minutes and 12 hours**. All ships from one battle come back together.
6. During the repair, the ships are **off the planet**: they do not defend, cannot be destroyed or plundered, and count neither in your fleets nor in your points. They come back intact.
7. A repair **cannot be cancelled**.
8. Recovered ships appear in the battle report's **losses**, with a note.
9. The Station **takes no field** and uses no energy while running; energy is only a threshold to build it.
10. **Defenses** are not concerned: they have their own rebuild (see [Defense rebuild](/en/combat/defense-rebuild)).

## Worked example

You lose **100 Interceptors** in defense, with a Repair Station level 4, on Redline:
- Recovered share: 50% × (1 − 30%) = **35%**, so **35 Interceptors**.
- Structure to repair: 35 × 4,000 = 140,000. Speed: 10 × 4 = 40 per second, so 3,500 seconds: about **58 minutes**.
- Had you lost only 2 Interceptors: 35% of 2 = 0.7, rounded to **0**: nothing is recovered.

## Detailed data

| Level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Coefficient | 45% | 48% | 49% | 50% | 51% | 52% | 53% | 53% | 54% | 54% |
| Recovered share (debris 30%) | 31.5% | 33.6% | 34.3% | 35% | 35.7% | 36.4% | 37.1% | 37.1% | 37.8% | 37.8% |

Requirement: Orbital Dock 2. Level 1 cost: 200 metal, 50 hydrogen, 50 required energy; the cost is multiplied by 5 at each level, the required energy by 2.5.

## Common pitfalls

- **Small losses recover nothing**: rounding is done per ship type.
- **Ships under repair do not defend you**: a new attack meanwhile finds an emptier orbit.
- **The cost climbs very fast**: ×5 per level.

## Related pages

- [Ships list](/en/fleet/ships)
- [Reading a battle report](/en/combat/battle-report)
- [Debris fields](/en/combat/debris)
- [Defense rebuild](/en/combat/defense-rebuild)
