---
wiki_id: 124
locale: "en"
path: "espionage/sensor-phalanx"
url: "https://wiki.dynastynova.com/en/espionage/sensor-phalanx"
title: "Sensor phalanx"
description: "Watching fleets from a moon: range, cost, what is seen."
tags: ["espionage", "moon"]
published: true
created: "2026-10-02T13:11:48.294Z"
updated: "2026-10-02T17:40:26.409Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Sensor phalanx

> **In short**: the Sensor phalanx is built on a moon. It sweeps a planet of the same galaxy and shows every fleet under way leaving it or heading for it: composition, mission and times. Each sweep costs 5,000 hydrogen, taken from the moon.
{.is-info}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Sensor phalanx">

> **Universe setting**: the number of systems per galaxy may differ from one universe to another.
> Default: **set when the universe is created** · Redline: **99 systems**
{.is-info}

## Rules

### Building

1. The Phalanx can be built **only on a moon**, after **Lunar base level 1**.
2. Level N costs 20,000 metal, 40,000 crystal and 20,000 hydrogen, doubled at each level (× 2^(N − 1)). It has no maximum level: only the moon's fields limit it.

### Sweeping

3. The Phalanx sweeps a **planet** in the **same galaxy**, within range. It can **never target a moon**.
4. **Range** = level² − 1 systems on each side of the moon, at least 1.
5. The galaxy **wraps around** its systems: the last system is next to the first. A moon near one end therefore also sees the systems at the other end.
6. Each sweep costs **5,000 hydrogen**, taken from the moon, even if no fleet is found.
7. A refused sweep (out of range, other galaxy, moon targeted, not enough hydrogen) costs nothing.
8. You cannot sweep while you are on vacation.

### What the sweep shows

9. Every fleet **under way** whose **departure or destination** is the planet, outbound or returning, enemy fleets included: their **ships**, their **mission**, where they leave from and where they go, and their **departure and arrival times**.
10. The **cargo** stays hidden.
11. **Espionage** and **Recycling** missions do not show.
12. Fleets leaving the planet's **moon** or heading for it do not show either.
13. The swept player **is not warned**.
14. Some dynasty talents change the Phalanx (range, cost, extended sweep, memory) or fool it: see the [Oracle](/en/dynasty/classes/oracle) and the [Shadow](/en/dynasty/classes/shadow).

## Worked example

Your moon is at [3:50:8] with a level 4 Phalanx, in a galaxy of 99 systems.
- Range: 4² − 1 = **15 systems** on each side, i.e. systems **35 to 65** of galaxy 3.
- You can sweep a planet at [3:60:5] for 5,000 hydrogen.
- A planet at [3:70:5] is out of range. A planet at [4:50:5] is in another galaxy: impossible.
- Near the edge, the range carries on from the other end: from [3:5:8], the same Phalanx covers systems **1 to 20** and **89 to 99**.

## Detailed data

| Level | Range (systems on each side) | Metal | Crystal | Hydrogen |
|---|---|---|---|---|
| 1 | 1 | 20,000 | 40,000 | 20,000 |
| 2 | 3 | 40,000 | 80,000 | 40,000 |
| 3 | 8 | 80,000 | 160,000 | 80,000 |
| 4 | 15 | 160,000 | 320,000 | 160,000 |
| 5 | 24 | 320,000 | 640,000 | 320,000 |
| 6 | 35 | 640,000 | 1,280,000 | 640,000 |
| 7 | 48 | 1,280,000 | 2,560,000 | 1,280,000 |
| 8 | 63 | 2,560,000 | 5,120,000 | 2,560,000 |
| 9 | 80 | 5,120,000 | 10,240,000 | 5,120,000 |
| 10 | 99 | 10,240,000 | 20,480,000 | 10,240,000 |

## Common pitfalls

- **A fleet stationed on a moon escapes the Phalanx**: a moon cannot be swept, and the moon's traffic does not show on its planet's sweep.
- **The sweep is paid even when empty**: 5,000 hydrogen every time.
- **Keep hydrogen on the moon**: the cost is taken from the moon, which produces nothing. Bring hydrogen there by transport.
- **No sweeping another galaxy**, whatever the level.

## Related pages

- [Moons](/en/universe/moons)
- [Jump gate](/en/fleet/jump-gate)
- [Spying](/en/espionage/spying)
- [Coordinates](/en/universe/coordinates)
