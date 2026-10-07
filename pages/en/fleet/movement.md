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
updated: "2026-10-06T10:30:53.371Z"
---

# Fleet movement

> **In short**: a flight's duration depends on distance, the speed of the slowest ship and the speed percentage you choose. Its hydrogen cost depends on distance, the ships sent and speed. Flying slower costs much less.
{.is-info}

> **Universe setting**: fleet speed may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

### Fleet slots
1. The number of fleets in flight at the same time is limited: **fleet slots = 1 + Quantum Computing level**. An expedition also takes a slot.

### Speed
2. A ship's speed = base speed × (1 + bonus × level of its drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive.
3. A fleet flies at the speed of its **slowest ship**. Speed bonuses (personal talents and the Coordinated propulsion alliance talent) **divide the flight time**: +50% = a flight 1.5 times shorter, +60% at most in total. See [Talents](/en/dynasty/talents).
4. You choose a **speed percentage** from 10 to 100%, in steps of 10. In the formulas it becomes the factor $S$, from 1 to 10: $S = 1$ for 10%, $S = 10$ for 100%.

### Distance

5. Summary of distance calculation

| Trip | Distance |
|---|---|
| To another galaxy | 20,000 × galaxy gap |
| Same galaxy, other system | 2,700 + 95 × system gap |
| Same system | 1,000 + 5 × position gap |
| Between a planet and its moon | 5 |

### Duration

6. Calculation

$$
   T =
   \frac{
   10 + \frac{35000}{S}\sqrt{\frac{10 \times D}{V}}
   }{
   A
   }
   $$

- $T$ is the flight time of the fleet in seconds.
- $D$ is the flight distance as calculated above (See [Coordinates](/en/universe/coordinates) for more details).
- $V$ is the speed of the slowest ship in the fleet.
- $S$ is the chosen speed factor, from 1 (10%) to 10 (100%), in steps of 1.
- $A$ is the Universe's Fleet Speed Acceleration factor.

### Hydrogen use
7. **Fuel consumption per trip**

Fuel consumption per trip is calculated as the sum, for each ship type, of:

$$
U =
\sum_i
\left(
\frac{
F_i \times N_i \times D
}{
35\,000
}
\left(
\frac{S}{10}\sqrt{\frac{V}{V_i}} + 1
\right)^2
\right)
$$

- $U$ is the fuel consumption of the trip.
- $F_i$ is the fuel consumption of ship type $i$.
- $N_i$ is the number of ships of type $i$ in the fleet.
- $D$ is the flight distance.
- $S$ is the chosen speed factor, from 1 (10%) to 10 (100%).
- $V$ is the speed of the slowest ship in the fleet.
- $V_i$ is the speed of ship type $i$.


8. A ship faster than the rest of its fleet uses less.
9. **The return trip is paid at departure** (outbound and return charged together) for every mission except **Colonization** and **Stationing**.
10. The Optimised supply alliance talent removes 5% per level. No research lowers a ship's fuel use.

### Recall
11. A fleet can be **recalled at any time before the end of its outbound trip**. Recalling charges nothing more and **refunds no** hydrogen.

## Worked example

10 Interceptors (speed 20,000 with Combustion Drive 6, fuel use 20 each) attack from [2:40:8] to [2:50:3]. Distance: 2,700 + 95 × 10 = **3,650**.

| Speed | $S$ | One-way duration | One-way hydrogen | Charged at departure (round trip) |
|---|---|---|---|---|
| 100% | 10 | 10 + 35,000 / 10 × √(10 × 3,650 / 20,000) ≈ **4,738 s** (1 h 18 min 58 s) | 20 × 10 × 3,650 / 35,000 × (10 / 10 + 1)² ≈ **83** | **166** |
| 50% | 5 | 10 + 35,000 / 5 × √1.825 ≈ **9,466 s** (2 h 37 min 46 s) | 20 × 10 × 3,650 / 35,000 × (5 / 10 + 1)² ≈ **46** | **92** |

At half speed, the flight takes twice as long but uses **45% less hydrogen**.

## Detailed data

### Drives

| Drive | Bonus per level | Ships |
|---|---|---|
| Combustion Drive | +10% | Cargo Shuttle, Stellar Freighter, Salvager, Scout, Interceptor |
| Impulse Drive | +20% | Space Pioneer, Assailant, Corvette, Orbital Striker |
| Hyperspace Drive | +30% | Battleship, Predator, Annihilator, Stellar Colossus |

Base speeds and fuel use are on the [Ships list](/en/fleet/ships) page.

## Common pitfalls

- **The slowest sets the pace**: a single Salvager (speed 2,000) slows a whole fleet of Interceptors.
- **The return is paid at departure**: plan hydrogen for the round trip before attacking.
- **Recalling refunds nothing**: the hydrogen spent is lost.
- **Quantum Computing caps your fleets**: at level 2, only 3 fleets in flight, expeditions included.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Missions](/en/fleet/missions)
- [Ships list](/en/fleet/ships)
- [Expeditions](/en/fleet/expeditions)
- [Alliance missions and station](/en/players/alliance-missions)
