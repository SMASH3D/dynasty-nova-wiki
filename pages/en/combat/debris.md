---
wiki_id: 117
locale: "en"
path: "combat/debris"
url: "https://wiki.dynastynova.com/en/combat/debris"
title: "Debris fields"
description: "Debris created by battles, recycling and moon formation."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:34.089Z"
updated: "2026-10-15T18:52:26.677Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Debris fields

> **In short**: when ships are destroyed, a share of their metal and crystal forms a debris field in orbit, 30% by default. Defenses leave none, unless the universe says otherwise. Debris never disappears: it must be recycled with Salvagers. A big battle can also give birth to a moon.
{.is-info}

> **Universe setting**: the debris rate of ships and defenses, and the maximum moon chance and the debris that gives it, may differ from one universe to another.
> Default: ships **30%**, defenses **0%**, moon **20% at most, reached at 2,000,000 debris** · Redline: ships **30%**, defenses **0%**, moon **20% for 2,000,000**
{.is-info}

<img src="/images/illustrations/ships/recuperateur.jpg" width="180" alt="Salvager">

## Rules

### What turns into debris
1. Destroyed ships **on both sides**, civil ones included, leave the universe's **ship debris rate** (30% by default) of their cost in **metal and crystal**. Hydrogen leaves nothing.
2. Destroyed **defenses** leave the universe's **defense debris rate**: **0%** by default, so nothing. That rate counts every defense destroyed, even those later [rebuilt](/en/combat/defense-rebuild).
3. The total is rounded down, for metal as for crystal.
4. Battles against [expedition](/en/fleet/expeditions) pirates and aliens leave **10%** of the ships destroyed, whatever the universe.
5. A [Moon destruction](/en/combat/moon-destruction) mission leaves **no debris**, neither from the battle nor from the moon.
6. A battle's debris **adds up** with the field already on the cell.

### Collecting debris
7. Debris **never disappears**. Only recycling removes it. It stays even if the planet below is abandoned.
8. To collect it, send **Salvagers** on a **Recycle** mission. Only the Salvagers' holds count; whatever does not fit stays in orbit.
9. The field belongs to whoever recycles it, whoever won the battle.

### Moon formation
10. After an attack, the target planet may gain a **moon**. The chance is computed on **this battle's debris only** (metal plus crystal), not on the field already in orbit:

$$p = \min\left(D \times \frac{p_{max}}{D_{max}},\ p_{max}\right) \quad\text{and}\quad p = 0 \text{ if } D < \frac{D_{max}}{p_{max}}$$

- $p$: moon chance, in %; $D$: the battle's debris (metal + crystal).
- $p_{max}$: the universe's maximum chance (20% by default); $D_{max}$: debris that gives this maximum chance (2,000,000 by default).
- By default: **1% per 100,000 debris**, nothing below 100,000, 20% at most.

11. The moon goes **to the planet's owner**, even if they lost the battle. The attacker never gains a moon over someone else's planet.
12. No moon if the cell already has one, nor over an abandoned planet, nor when the battle takes place above the moon itself.
13. Formation **does not consume** the debris: Salvagers collect all of it either way.
14. **Moon size**: it is drawn among **11 equally likely sizes**, bigger as the chance was higher. With $X$ drawn between 0 and 10:

$$c = 10 + X + 60 \times \frac{p}{p_{max}} \qquad \text{diameter} = \left\lfloor 1{,}000 \sqrt{c} \right\rfloor \text{ km}$$

- The last term is at least 3. A moon is therefore **3,605 km** (1% chance) to **8,944 km** (maximum chance) wide.
- A moon starts with 1 field; at most it will have integer part((diameter / 1,000)²), opened by the Lunar base. See [Moons](/en/universe/moons).

## Worked example

You destroy 100 Interceptors (3,000 metal and 1,000 crystal each), in a universe with default settings:
- Debris: 30% × 300,000 metal = **90,000 metal**, and 30% × 100,000 crystal = **30,000 crystal**.
- Total haul: 120,000 resources. A Salvager carries 20,000: you need **6** (without Hyperspace Technology bonus).
- Moon chance: 120,000 × 20 / 2,000,000 = **1.2%**. If it forms, it is between **3,687 and 4,857 km** wide.

## Detailed data

Debris left by one destroyed ship, at a 30% rate (ship names are provisional translations: the game still shows the French names):

| Ship | Metal | Crystal |
|---|---|---|
| Cargo Shuttle | 600 | 600 |
| Stellar Freighter | 1,800 | 1,800 |
| Space Pioneer | 3,000 | 6,000 |
| Salvager | 3,000 | 1,800 |
| Scout | 0 | 300 |
| Solar Collector | 0 | 600 |
| Interceptor | 900 | 300 |
| Assailant | 1,800 | 1,200 |
| Corvette | 6,000 | 2,100 |
| Battleship | 13,500 | 4,500 |
| Orbital Striker | 15,000 | 7,500 |
| Predator | 9,000 | 12,000 |
| Annihilator | 18,000 | 15,000 |
| Stellar Colossus | 1,500,000 | 1,200,000 |

Moon chance and possible diameters by the battle's debris, default settings:

| Battle debris | Moon chance | Diameter (km) |
|---|---|---|
| 50,000 | 0% | no moon |
| 100,000 | 1% | 3,605 to 4,795 |
| 250,000 | 2.5% | 4,183 to 5,244 |
| 500,000 | 5% | 5,000 to 5,916 |
| 1,000,000 | 10% | 6,324 to 7,071 |
| 2,000,000 | 20% | 8,366 to 8,944 |
| 5,000,000 | 20% | 8,366 to 8,944 |

## Common pitfalls

- **Your own losses feed the field**: a battle lost while defending also leaves debris above your planet, which others can recycle.
- **The field does not help the next moon**: only the debris of the battle that just happened counts for the moon chance.
- **Hyperspace Technology raises cargo**: +5% per level, handy to recycle with fewer Salvagers.
- **First come, first served**: the field belongs to whoever recycles it.

## Related pages

- [Ship list](/en/fleet/ships)
- [Missions](/en/fleet/missions)
- [Moons](/en/universe/moons)
- [Repair Station](/en/economy/repair-station)
- [Defense rebuild](/en/combat/defense-rebuild)
