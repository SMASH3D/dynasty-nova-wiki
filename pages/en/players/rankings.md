---
wiki_id: 126
locale: "en"
path: "players/rankings"
url: "https://wiki.dynastynova.com/en/players/rankings"
title: "Rankings and points"
description: "The four player rankings, the two alliance rankings and how points are counted."
tags: ["players"]
published: true
created: "2026-10-02T13:11:52.215Z"
updated: "2026-10-15T18:53:26.805Z"
---

# Rankings and points

> **In short**: everything you build earns points, at **1 point per 1,000 resources** of its cost. Players are ranked on four boards: Points (the total), Economy, Research and Military. Alliances have two rankings of their own: Power and Progression.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

### How points are counted
1. An item is worth **(metal + crystal + hydrogen) / 1,000** points. Energy does not count.
2. The **catalogue cost** is what counts, not what you paid: a cost reduction (talent, bonus) does not change the points earned.
3. **Economy**: every building level standing on your planets and moons. Level N earns the cost of level N; a building at level 10 therefore counts the costs of levels 1 to 10.
4. **Research**: every technology level, the same way.
5. **Military**: **every ship**, civilian ships included (Cargo Shuttle, Stellar Freighter, Space Pioneer, Salvager, Scout, Solar Collector), every defense and every missile, docked or in flight.
6. **Points** (the general ranking) = Economy + Research + Military.
7. Points are earned when a building or research level **finishes**, and **at each delivery** from the shipyard for ships and defenses.

### What makes them go up or down
8. **Down**: ships and defenses destroyed, missiles fired, a demolished building level (it removes that level's points), an abandoned colony (its buildings, ships and defenses), a destroyed moon (its buildings and everything on it).
9. **Not down**: ships towed back by the Repair Station and defenses restored after a battle, since they are not lost. Abandoning a colony removes **no research points**: technologies belong to the empire.
10. **Also up**: ships found on an expedition, a building level granted for free (it counts as a built level), a recolonized abandoned planet (you receive the points of what is still standing on it).

### The ranking
11. The ranking is **computed live**. Points are shown rounded down; that rounded number is also what [beginner protection](/en/players/beginner-protection) uses.
12. The **progression** arrows compare your rank and points with the latest daily snapshot of the ranking.
13. The **Humans** filter hides non-human players (marked "AI player (PvE)") without changing ranks: everyone keeps their rank in the universe.
14. **Search** finds a player or an alliance by name or tag. Clicking a player opens their **card**: rank, badges ("AI player (PvE)", "On vacation", "New player") and a button to message them.
15. Two players tied on points are separated by an internal order, not by seniority.

### Alliance rankings
16. **Alliance Power**: the sum of all members' Points. The treasury and alliance talents do not count.
17. **Alliance Progression**: the alliance's level and experience; on a tie, the first to get there ranks higher. See [Alliances](/en/players/alliances).

## Worked example

- You raise the Mineral Excavator from level 13 to level 14 for 11,677 metal and 2,919 crystal: **+14.6 points** of economy (the ranking shows the integer part).
- You build a Battleship (45,000 metal, 15,000 crystal): **+60 points** of military.
- You build 10 Stellar Freighters (12,000 resources each): **+120 points** of military. Civilian ships count.
- You fire 10 Long-Range Warheads: **-250 points** of military, whether they hit or not.
- Your Battleship is destroyed in combat and the Repair Station does not recover it: **-60 points** of military.

## Detailed data

Points of each ship (catalogue cost):

| Ship | Metal | Crystal | Hydrogen | Points |
|---|---|---|---|---|
| Cargo Shuttle | 2,000 | 2,000 | 0 | 4 |
| Stellar Freighter | 6,000 | 6,000 | 0 | 12 |
| Space Pioneer | 10,000 | 20,000 | 10,000 | 40 |
| Salvager | 10,000 | 6,000 | 2,000 | 18 |
| Scout | 0 | 1,000 | 0 | 1 |
| Solar Collector | 0 | 2,000 | 500 | 2.5 |
| Interceptor | 3,000 | 1,000 | 0 | 4 |
| Assailant | 6,000 | 4,000 | 0 | 10 |
| Corvette | 20,000 | 7,000 | 2,000 | 29 |
| Battleship | 45,000 | 15,000 | 0 | 60 |
| Orbital Striker | 50,000 | 25,000 | 15,000 | 90 |
| Predator | 30,000 | 40,000 | 15,000 | 85 |
| Annihilator | 60,000 | 50,000 | 15,000 | 125 |
| Stellar Colossus | 5,000,000 | 4,000,000 | 1,000,000 | 10,000 |

Points of each defense and missile:

| Defense | Metal | Crystal | Hydrogen | Points |
|---|---|---|---|---|
| Ballistic Projector | 2,000 | 0 | 0 | 2 |
| Photonic Cannon | 1,500 | 500 | 0 | 2 |
| High-Energy Emitter | 6,000 | 2,000 | 0 | 8 |
| Ion Battery | 2,000 | 6,000 | 0 | 8 |
| Magnetic Accelerator | 20,000 | 15,000 | 2,000 | 37 |
| Plasma Ejector | 50,000 | 50,000 | 30,000 | 130 |
| Defensive Barrier | 10,000 | 10,000 | 0 | 20 |
| Protective Dome | 50,000 | 50,000 | 0 | 100 |
| Interception Missile | 8,000 | 2,000 | 0 | 10 |
| Long-Range Warheads | 12,500 | 2,500 | 10,000 | 25 |

| Ranking | What counts | What lowers it |
|---|---|---|
| Economy | Building levels, planets and moons | Demolition, abandoned colony, destroyed moon |
| Research | Technology levels | Nothing |
| Military | Every ship, defense and missile | Units destroyed, missiles fired, abandoned colony, destroyed moon |
| Points | Sum of the three | All of the above |

## Common pitfalls

- **A transport fleet counts**: 100 Stellar Freighters are worth 1,200 military points, and losing them takes those away.
- **Firing missiles costs points**, even when they are intercepted.
- **Climbing the ranking changes your protection**: crossing a tier changes who you may attack and who may attack you.
- **Abandoning a colony makes your points drop**, but not your research.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Alliances](/en/players/alliances)
- [Building list](/en/economy/buildings)
- [Technology list](/en/research/technologies)
- [Ship list](/en/fleet/ships)
- [Defense list](/en/defense/defenses)
