---
wiki_id: 89
locale: "en"
path: "economy/energy"
url: "https://wiki.dynastynova.com/en/economy/energy"
title: "Energy"
description: "Producing and using energy, shortage and operating rate."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:38.606Z"
updated: "2026-10-15T18:52:47.615Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Energy

> **In short**: your mines use energy, your power plants produce it. As long as production covers consumption, everything runs at full speed. As soon as it falls short, **all three mines** slow down in the same proportion. Energy is not stored.
{.is-info}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Photovoltaic Sensors"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Thermonuclear Reactor"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Solar Collector">

## Rules

1. **Photovoltaic Sensors**: 20 × N × 1.1^N energy at level N, multiplied by 1 + current temperature / 100 when the planet's current temperature is positive. The current temperature follows the calendar month (see [Planets](/en/universe/planets)).
2. **Thermonuclear Reactor**: 30 × N × (1.05 + 0.01 × Energy Science)^N energy, **burning hydrogen**: 10 × N × 1.1^N per hour, multiplied by the universe's economy speed.
3. **Solar Collector**: a ship that stays in orbit and produces, each, maximum temperature / 4 + 20 energy, rounded down and never negative. It can be destroyed in combat.
4. **Consumption**: the Mineral Excavator, the Crystal Extractor and the Hydrogen Condenser each use 10 × N × 1.1^N energy. The economy speed does not change consumption.
5. **Deficit**: when consumption exceeds production, the three mines' output, bonuses included, is multiplied by production / consumption. The production breakdown shows an "Energy deficit" line. The Planetary Base's income is not affected.
6. **Operating rate**: each mine is set in steps of 10%; output and consumption drop together. The Reactor always runs at full power, unless a talent allows otherwise.
7. Energy is **never stored**: it is computed at every moment.
8. Some buildings and research need a **required energy** to be started (Repair Station, Planetary Modulator, Graviton Technology): it is a production threshold, not a cost.

## Worked example

Photovoltaic Sensors 13 on a 10°C day, Mineral Excavator 13, Crystal Extractor 13, Hydrogen Condenser 10:
- Production: 20 × 13 × 1.1^13 × 1.1 = **987** energy.
- Consumption: 448 + 448 + 259 = **1,155**.
- Coverage: 987 / 1,155 = **85.5%**. The Excavator, which should produce 1,346 metal per hour, only produces **1,150**.
- Raising a mine one level would deepen the deficit: better raise the Sensors.

**Solar Collectors**: on a planet with a maximum temperature of 60°C, each produces 60 / 4 + 20 = **35** energy; 10 Collectors produce **350**.

## Detailed data

### Mine consumption and Sensors output

Sensors are given at 0°C or below; at a positive current temperature T, multiply by 1 + T / 100.

| Level | Consumption of each mine | Photovoltaic Sensors (0°C) |
|---|---|---|
| 1 | 11 | 22 |
| 2 | 24 | 48 |
| 3 | 39 | 79 |
| 4 | 58 | 117 |
| 5 | 80 | 161 |
| 6 | 106 | 212 |
| 7 | 136 | 272 |
| 8 | 171 | 342 |
| 9 | 212 | 424 |
| 10 | 259 | 518 |
| 11 | 313 | 627 |
| 12 | 376 | 753 |
| 13 | 448 | 897 |
| 14 | 531 | 1,063 |
| 15 | 626 | 1,253 |
| 16 | 735 | 1,470 |
| 17 | 859 | 1,718 |
| 18 | 1,000 | 2,001 |
| 19 | 1,162 | 2,324 |
| 20 | 1,345 | 2,690 |
| 21 | 1,554 | 3,108 |
| 22 | 1,790 | 3,581 |
| 23 | 2,059 | 4,118 |
| 24 | 2,363 | 4,727 |
| 25 | 2,708 | 5,417 |
| 26 | 3,098 | 6,197 |
| 27 | 3,539 | 7,079 |
| 28 | 4,037 | 8,075 |
| 29 | 4,600 | 9,200 |
| 30 | 5,234 | 10,469 |

### Thermonuclear Reactor

| Level | Energy (Energy Science 3) | Energy (6) | Energy (9) | Energy (12) | Hydrogen burned per hour (speed ×1) |
|---|---|---|---|---|---|
| 1 | 32 | 33 | 34 | 35 | 11 |
| 2 | 69 | 73 | 77 | 82 | 24 |
| 3 | 113 | 123 | 133 | 144 | 39 |
| 4 | 163 | 182 | 202 | 224 | 58 |
| 5 | 220 | 252 | 288 | 328 | 80 |
| 6 | 285 | 336 | 395 | 461 | 106 |
| 7 | 359 | 435 | 525 | 630 | 136 |
| 8 | 444 | 553 | 684 | 842 | 171 |
| 9 | 539 | 690 | 878 | 1,109 | 212 |
| 10 | 647 | 851 | 1,112 | 1,442 | 259 |
| 11 | 769 | 1,040 | 1,394 | 1,855 | 313 |
| 12 | 906 | 1,259 | 1,734 | 2,368 | 376 |
| 13 | 1,060 | 1,514 | 2,142 | 3,002 | 448 |
| 14 | 1,233 | 1,810 | 2,629 | 3,783 | 531 |
| 15 | 1,427 | 2,153 | 3,212 | 4,742 | 626 |
| 16 | 1,644 | 2,549 | 3,905 | 5,918 | 735 |
| 17 | 1,887 | 3,006 | 4,730 | 7,357 | 859 |
| 18 | 2,157 | 3,533 | 5,710 | 9,114 | 1,000 |
| 19 | 2,459 | 4,140 | 6,871 | 11,256 | 1,162 |
| 20 | 2,796 | 4,837 | 8,246 | 13,863 | 1,345 |

### Solar Collector

| Maximum temperature | Energy per Collector |
|---|---|
| -120°C | 0 |
| -100°C | 0 |
| -80°C | 0 |
| -60°C | 5 |
| -40°C | 10 |
| -20°C | 15 |
| 0°C | 20 |
| 20°C | 25 |
| 40°C | 30 |
| 60°C | 35 |
| 80°C | 40 |
| 100°C | 45 |
| 120°C | 50 |
| 140°C | 55 |
| 160°C | 60 |

## Common pitfalls

- **One more mine level can lower total output**: without a matching power plant, the deficit slows all three mines.
- **Solar output moves during the month**: the current temperature varies, and the Sensors with it. Keep a margin.
- **Solar Collectors are vulnerable**: they can be destroyed in combat.
- **The Reactor costs hydrogen**: what it burns is taken off your hydrogen output.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Economy formulas](/en/economy/formulas)
- [Planets: size, temperature, type](/en/universe/planets)
- [Ships list](/en/fleet/ships)
