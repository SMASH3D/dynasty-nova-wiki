---
wiki_id: 105
locale: "en"
path: "fleet/movement"
url: "https://wiki.dynastynova.com/en/fleet/movement"
title: "Fleet movement"
description: "Speed, flight time, hydrogen use and fleet slots."
tags: ["fleet"]
published: true
created: "2026-10-02T13:11:09.961Z"
updated: "2026-10-15T18:53:08.419Z"
---

# Fleet movement

> **In short**: a flight's duration depends on the distance, the speed of the slowest ship and the speed you choose, from 1 to 100%. Its hydrogen use depends on the distance, the ships sent and the speed. Flying slower costs much less. The trip's hydrogen travels in the holds, with the cargo.
{.is-info}

> **Universe setting**: the fleet speed divides flight durations. It does not change consumption.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

### Fleet slots
1. The number of fleets flying at once is capped: **fleet slots = 1 + Quantum Computing level**, plus up to 3 talent slots (one of them for attacks only, for the Admiral). See [Talents](/en/dynasty/talents).
2. A fleet takes its slot from departure to return. Expeditions, including during their hold, and Stellar Station deposits take one. Missiles and [Jump gate](/en/fleet/jump-gate) jumps do not. The Navigator also gets shuttles, outside the slots, for transports and stationing between their own bases.

### Speed
3. A ship's speed = its drive's base speed × (1 + bonus × level of that drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive. Some ships switch drives with research (see [Ships list](/en/fleet/ships)).
4. A fleet flies at the speed of its **slowest ship**.
5. You choose a **speed from 1 to 100%**, in steps of 1%. In the formulas it becomes the fraction $s$: $s = 1$ at 100%, $s = 0.5$ at 50%.

### Distance
6. The distance depends on what differs between departure and arrival:

| Trip | Distance |
|---|---|
| To another galaxy | 20,000 × galaxy gap |
| Same galaxy, other system | 2,700 + 95 × system gap |
| Same system, other position | 1,000 + 5 × position gap |
| Between a planet and its moon | 5 |

7. **The map wraps around** for galaxies and for systems: the gap is counted the shortest way, across the edge if need be. On Redline, galaxy 9 neighbours galaxy 1, and system 99 neighbours system 1. Positions do not wrap.

### Duration
8. One-way duration, in seconds, rounded, at least 1:

$$
T = \frac{10 + \frac{3{,}500}{s}\sqrt{\frac{10 \times D}{V}}}{A \times B}
$$

- $T$: trip duration, in seconds;
- $s$: chosen speed, as a fraction (from 0.01 for 1% to 1 for 100%);
- $D$: trip distance (rule 6);
- $V$: speed of the slowest ship in the fleet;
- $A$: the universe's fleet speed;
- $B$: speed bonus, 1 without a bonus (rule 13).

### Hydrogen consumption
9. One-way consumption, rounded down, at least 1 as soon as a ship burns fuel:

$$
U = \sum_i \frac{F_i \times N_i \times D}{35{,}000} \left( s \sqrt{\frac{V}{V_i}} + 1 \right)^2
$$

- $U$: hydrogen for the trip;
- $F_i$: consumption of one ship of type $i$, that of its current drive;
- $N_i$: number of ships of type $i$;
- $D$: trip distance;
- $s$: chosen speed, as a fraction;
- $V$: speed of the slowest ship in the fleet;
- $V_i$: speed of ship type $i$.

10. A ship faster than the rest of its fleet burns less. No research lowers consumption; a better drive raises it.
11. **The way back is paid at departure**: each leg is counted on its own, out then back, for every mission except **Colonization** and **Stationing**, which are one-way. Stellar Station deposits burn nothing.
12. **The trip's hydrogen travels in the holds**: cargo + trip hydrogen must not exceed the fleet's cargo capacity. A Navigator talent lightens that fuel.

### Bonuses
13. Speed bonuses (personal talents and the alliance talent Coordinated propulsion, +5% per level) **divide the duration**: +50% = a trip 1.5 times shorter. Together they cap at **+60%**; a few trip talents add on top of the cap (return, trips between your bases, recall).
14. Consumption cuts (personal talents and the alliance talent Optimised supply, 5% per level) cap together at **45%**, never below 1 per leg.

### Recall and return
15. A fleet can be **recalled** while it is flying out or holding on an expedition, not on its way back. Stellar Station deposits cannot be recalled.
16. A recalled fleet flies home in as much time as it already spent flying out; an expedition recalled during its hold flies the whole way. A recall **does not refund** hydrogen (except with a Navigator talent). A recalled attack no longer counts towards the [attack limit](/en/players/attack-limit).
17. On return, the fleet lands at its home base with its cargo, even beyond storage capacity. **That base must still be yours and have an Orbital Dock**: otherwise the fleet is lost.

## Worked example

10 Interceptors (speed 12,500 × 1.6 = 20,000 with Combustion Drive 6, consumption 20 each) attack from [2:40:8] to [2:50:3]. Distance: 2,700 + 95 × 10 = **3,650**.

| Speed | One-way time | One-way hydrogen | Paid at departure (round trip) |
|---|---|---|---|
| 100% | 4,738 s (1 h 18 min 58 s) | 83 | 166 |
| 50% | 9,466 s (2 h 37 min 46 s) | 46 | 92 |
| 10% | 47,292 s (13 h 8 min 12 s) | 25 | 50 |

For instance at 100%: 10 + 3,500 / 1 × √(10 × 3,650 / 20,000) ≈ 4,738 s, and 20 × 10 × 3,650 / 35,000 × (1 + 1)² ≈ 83 hydrogen. At half speed the flight takes twice as long but costs **45% less hydrogen**.

**Wrapping map**: from galaxy 1 to galaxy 9 on Redline, the gap is 1 galaxy, so a distance of 20,000, not 8 × 20,000. From system 3 to system 97 of the same galaxy, the gap is 5 systems: distance 3,175.

## Detailed data

### Drives

| Drive | Bonus per level | Ships (built-in drive) |
|---|---|---|
| Combustion Drive | +10% | *Cargo Shuttle*, *Stellar Freighter*, *Salvager*, *Scout*, *Interceptor* |
| Impulse Drive | +20% | *Space Pioneer*, *Assailant*, *Corvette*, *Orbital Striker* |
| Hyperspace Drive | +30% | *Battleship*, *Predator*, *Annihilator*, *Stellar Colossus* |

Speeds, consumption and drive switches are on the [Ships list](/en/fleet/ships) page.

### Talent flight orders

Talents add flight orders: changing speed in flight (Relaunch at 100%, Holding pattern down to 10%), Home port, Return freight, Grouped delivery, Loading order, Afterburner, Redirection, Return jump. They are described in [Talents](/en/dynasty/talents) and the [Navigator](/en/dynasty/classes/navigator) tree.

## Common pitfalls

- **The slowest ship sets the pace**: a single Salvager (speed 2,000) slows a whole fleet of Interceptors.
- **The way back is paid at departure**: plan the round-trip hydrogen before attacking, and the hold space to carry it.
- **A recall refunds nothing**: the hydrogen spent is gone.
- **Do not remove the Orbital Dock of a base expecting a fleet**: with no Dock on arrival, the returning fleet is lost.
- **Mind the edge of the map**: the nearest galaxy is not always the one you think.
- **Quantum Computing caps your fleets**: at level 2, only 3 fleets in flight, expeditions and deposits included.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Missions](/en/fleet/missions)
- [Ships list](/en/fleet/ships)
- [Expeditions](/en/fleet/expeditions)
- [Jump gate](/en/fleet/jump-gate)
- [Alliance missions and station](/en/players/alliance-missions)
