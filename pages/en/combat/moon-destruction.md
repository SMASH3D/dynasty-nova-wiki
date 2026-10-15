---
wiki_id: 120
locale: "en"
path: "combat/moon-destruction"
url: "https://wiki.dynastynova.com/en/combat/moon-destruction"
title: "Moon destruction"
description: "Destroying a moon with Stellar Colossi."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:40.153Z"
updated: "2026-10-15T18:52:31.608Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Moon destruction

> **In short**: a fleet made only of Stellar Colossi can try to destroy another player's moon. It must first win the battle against whatever defends the moon. Then two independent rolls decide whether the moon is destroyed and whether the Colossi are lost.
{.is-info}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Stellar Colossus">

## Rules

### The mission
1. The **Moon destruction** mission requires a fleet made **only of Stellar Colossi**, and targets another player's **moon**. It is not offered on a planet.
2. It follows the same conditions as an attack: it is not offered against a protected player, a member of your alliance or a target whose [attack limit](/en/players/attack-limit) is reached.

### The battle
3. A **regular battle** takes place first, against the ships and defenses **of the moon**. See [How combat works](/en/combat/how-combat-works).
4. The moon's destroyed defenses follow the [defense rebuild](/en/combat/defense-rebuild).
5. This battle leaves **no plunder, no debris and no new moon**.

### The two rolls
6. The rolls only happen if the attacker **wins**. On a draw or a defeat, the moon is untouched and the survivors fly home.
7. With $S$ the moon's diameter and $N$ the number of **surviving** Colossi:

$$p_{moon} = \min\left(100,\ (100 - \sqrt{S}) \times \sqrt{N}\right) \qquad p_{fleet} = \frac{\sqrt{S}}{2}$$

- $p_{moon}$: chance of destroying the moon, in %; $p_{fleet}$: chance of losing the whole fleet, in %.
- $S$: moon diameter in km; $N$: Stellar Colossi still standing after the battle.

8. Both rolls are **independent** and both take place, whether or not the moon is destroyed. All four outcomes are possible, the worst being a fleet lost over an intact moon.
9. Losing the fleet is **one roll for the whole fleet** and **does not depend on the number of Colossi**: sending more Colossi only improves the chance of destroying the moon.
10. The **Moonbreaker** talent ([Admiral](/en/dynasty/classes/admiral)) multiplies the risk of losing the fleet by 0.75. The **The Moon Holds** talent ([Veteran](/en/dynasty/classes/veteran)) multiplies the chance of destroying the Veteran's moon by 0.75.

### Aftermath
11. If the moon is destroyed: everything on it disappears, and the matching points are removed from its owner. Fleets on their way to the moon, or due to return to it, are redirected to the planet.
12. Each side receives a **Moon destruction** report, which gives both chances even when the battle is lost. This report can be turned off in the report settings.
13. A moon whose owner is on vacation cannot be targeted.

## Worked example

A **8,944 km** moon (the largest possible size) and **100 Colossi** surviving:
- √8,944 ≈ 94.6.
- Chance of destroying the moon: (100 − 94.6) × √100 ≈ **54.3%**.
- Chance of losing the Colossi: 94.6 / 2 ≈ **47.3%**.
- With Moonbreaker, the risk drops to 47.3% × 0.75 ≈ **35.5%**. Against a Veteran holding The Moon Holds, the destruction chance drops to 54.3% × 0.75 ≈ **40.7%**.

## Detailed data

Chance of destroying the moon by its diameter and the number of surviving Colossi, and risk of losing the fleet (no talent). Moons are 3,605 to 8,944 km wide.

| Diameter | 1 Colossus | 4 Colossus | 25 Colossus | 100 Colossus | 400 Colossus | Fleet loss |
|---|---|---|---|---|---|---|
| 3,605 km | 40.0% | 79.9% | 100.0% | 100.0% | 100.0% | 30.0% |
| 6,324 km | 20.5% | 41.0% | 100.0% | 100.0% | 100.0% | 39.8% |
| 8,944 km | 5.4% | 10.9% | 27.1% | 54.3% | 100.0% | 47.3% |

## Common pitfalls

- **A big moon is harder and more dangerous**: the larger the diameter, the harder the destruction and the higher the risk of losing the fleet.
- **Numbers do not protect the fleet**: the risk of loss depends only on the diameter.
- **You must win the battle first**: without a victory, no roll. Colossi lost during the battle no longer count in $N$.
- **No loot, no debris**: a moon destruction brings no resources to either side.

## Related pages

- [Moons](/en/universe/moons)
- [Ship list](/en/fleet/ships)
- [Missions](/en/fleet/missions)
- [How combat works](/en/combat/how-combat-works)
- [Debris fields and moon formation](/en/combat/debris)
