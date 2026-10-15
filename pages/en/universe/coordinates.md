---
wiki_id: 81
locale: "en"
path: "universe/coordinates"
url: "https://wiki.dynastynova.com/en/universe/coordinates"
title: "Coordinates"
description: "Galaxy, system, position and distances."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:23.069Z"
updated: "2026-10-15T18:53:40.368Z"
---

# Coordinates

> **In short**: every planet has a three-number address, [galaxy:system:position], for example [2:83:6]. The number of galaxies, systems per galaxy and positions per system depends on the universe. The map **wraps around**: the last galaxy is next to the first one, and the last system of a galaxy is next to its first one. The distance between two coordinates sets a flight's duration and hydrogen cost.
{.is-info}

> **Universe setting**: the number of galaxies, systems per galaxy and positions per system (9 to 20) is set when the universe is created.
> Default: **none, each universe has its own** · Redline: **9 galaxies, 99 systems, 15 positions**
{.is-info}

## Rules

1. A coordinate is written **[galaxy:system:position]**.
2. Every galaxy has the same number of **systems**: 99 on Redline, numbered 1 to 99.
3. Every system has the same number of **positions**: 15 on Redline. Each position holds at most one planet, and possibly its moon.
4. After the last position, each system has two more cells, with no planet:
   - **deep space** (position 16 on Redline), for expeditions and recycling;
   - the **Stellar Station** (position 17 on Redline), home of the Stellar Bank and the alliance treasury.
5. **The map wraps around on galaxies and on systems**: from galaxy 9 to galaxy 1 the gap is 1, as from galaxy 1 to galaxy 2. Likewise, system 99 is next to system 1 in the same galaxy. The game always takes the shorter way.
6. **Positions do not wrap**: from position 1 to position 15, the gap is 14.
7. The **distance** between two points depends only on the largest gap (table below): a galaxy gap outweighs everything else, then a system gap, then a position gap.

## Formulas

With $\Delta G$, $\Delta S$ and $\Delta P$ the galaxy, system and position gaps:

$$
D = \begin{cases}
20{,}000 \times \Delta G & \text{if } \Delta G > 0 \\
2{,}700 + 95 \times \Delta S & \text{else, if } \Delta S > 0 \\
1{,}000 + 5 \times \Delta P & \text{else, if } \Delta P > 0 \\
5 & \text{between a planet and its moon}
\end{cases}
$$

- $\Delta G = \min(|G_1 - G_2|,\ n_G - |G_1 - G_2|)$, with $n_G$ the universe's number of galaxies;
- $\Delta S = \min(|S_1 - S_2|,\ n_S - |S_1 - S_2|)$, with $n_S$ the number of systems per galaxy;
- $\Delta P = |P_1 - P_2|$;
- $D$: the flight distance, which feeds its duration and consumption (see [Movement](/en/fleet/movement)).

## Worked examples

On Redline (9 galaxies, 99 systems):

| Trip | Gap used | Distance |
|---|---|---|
| [3:40:8] to [5:40:8] | 2 galaxies | 20,000 × 2 = **40,000** |
| [1:40:8] to [9:40:8] | 1 galaxy (the map wraps) | 20,000 × 1 = **20,000** |
| [2:45:8] to [2:50:8] | 5 systems | 2,700 + 95 × 5 = **3,175** |
| [2:97:8] to [2:3:8] | 5 systems (the galaxy wraps) | 2,700 + 95 × 5 = **3,175** |
| [2:45:3] to [2:45:6] | 3 positions | 1,000 + 5 × 3 = **1,015** |
| [2:45:3] to its moon | same cell | **5** |

## Common pitfalls

- **Changing galaxy is expensive**: a single galaxy gap (20,000) is worth more than the longest trip inside a Redline galaxy, 49 systems apart at most thanks to the wrap (2,700 + 95 × 49 = 7,355).
- **Remember the wrap**: a target in galaxy 9 is only one galaxy away if you are in galaxy 1.
- **A planet and its moon are not in the same place**: a trip of 5 is still a real, very short flight.

## Related pages

- [The galaxy view](/en/universe/galaxy-view)
- [Movement](/en/fleet/movement)
- [Planets: size, temperature, type](/en/universe/planets)
- [Expeditions](/en/fleet/expeditions)
