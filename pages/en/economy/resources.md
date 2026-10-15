---
wiki_id: 88
locale: "en"
path: "economy/resources"
url: "https://wiki.dynastynova.com/en/economy/resources"
title: "Resources"
description: "Metal, crystal, hydrogen and energy."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:36.697Z"
updated: "2026-10-02T17:40:47.420Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Resources

> **In short**: three resources are stored: metal, crystal and hydrogen. Your mines produce them continuously, even while you are offline, and each planet has its own stock. Energy, the fourth resource, is not stored: it runs the mines.
{.is-info}

> **Universe setting**: the economy speed multiplies the output of the mines and of the Planetary Base.
> Default: **×1** · Redline: **×1**
{.is-info}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Metal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Crystal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogen"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Energy">

## Rules

1. **Metal**: produced by the Mineral Excavator, 30 × N × 1.1^N per hour at level N.
2. **Crystal**: produced by the Crystal Extractor, 20 × N × 1.1^N per hour.
3. **Hydrogen**: produced by the Hydrogen Condenser, 10 × N × 1.1^N per hour, multiplied by a **temperature factor** of 1.44 − 0.004 × the planet's maximum temperature. A cold planet produces more; above 360°C, nothing at all.
4. **Energy**: produced by the Photovoltaic Sensors, the Thermonuclear Reactor and Solar Collectors, used by the three mines. It is not stored (see [Energy](/en/economy/energy)).
5. The **Planetary Base** (Colonial Base on a colony) adds **20 metal and 10 crystal per hour**, multiplied by the economy speed.
6. Production is **continuous**, computed per hour and rounded down. Each planet has **its own stock**, limited by its storage (see [Storage](/en/economy/storage)).
7. **Bonuses**: they apply to the gross output of the three mines and **add up**, without multiplying each other:
   - **Plasma Technology**: +1% metal, +0.66% crystal and +0.33% hydrogen per level;
   - **Coordinated extraction** alliance talent: +5% of all three resources per level;
   - **position bonus**, on colonies only: up to +40% crystal at positions 1 to 3, up to +35% metal at positions 6 to 10 (see [Planets](/en/universe/planets));
   - dynasty traits and talents (see [Dynasty and talents](/en/dynasty)).
8. When energy runs short, the mines' output, bonuses included, drops in proportion to the deficit. The Planetary Base's income is not affected.
9. **Operating rate**: each mine is set in steps of 10%, from 0 to 100%. Its output and its energy use drop in the same proportion.
10. Production stops when a resource's stock reaches its capacity, during [vacation mode](/en/players/vacation-mode), on an abandoned planet, and while a private universe is frozen or finished.

## Worked example

A colony at position 8, with Mineral Excavator 13, Crystal Extractor 13, Plasma Technology 2, Coordinated extraction 2 (+10%) and enough energy:
- Metal: 1,346 (Excavator) + 26 (Plasma: 2%) + 134 (alliance: 10%) + 471 (position 8: 35%) + 20 (Base) = **1,997 per hour**.
- Crystal: 897 (Extractor) + 11 (Plasma: 1.32%) + 89 (alliance) + 10 (Base) = **1,007 per hour**. Position 8 has no crystal bonus.
- Each bonus is computed on the mine's gross output and rounded down.

## Detailed data

### Mine output per level (per hour, speed ×1, no bonus)

Hydrogen is given for a temperature factor of 1; multiply it by your planet's factor.

| Level | Mineral Excavator (metal) | Crystal Extractor (crystal) | Hydrogen Condenser (hydrogen, factor 1) |
|---|---|---|---|
| 1 | 33 | 22 | 11 |
| 2 | 72 | 48 | 24 |
| 3 | 119 | 79 | 39 |
| 4 | 175 | 117 | 58 |
| 5 | 241 | 161 | 80 |
| 6 | 318 | 212 | 106 |
| 7 | 409 | 272 | 136 |
| 8 | 514 | 342 | 171 |
| 9 | 636 | 424 | 212 |
| 10 | 778 | 518 | 259 |
| 11 | 941 | 627 | 313 |
| 12 | 1,129 | 753 | 376 |
| 13 | 1,346 | 897 | 448 |
| 14 | 1,594 | 1,063 | 531 |
| 15 | 1,879 | 1,253 | 626 |
| 16 | 2,205 | 1,470 | 735 |
| 17 | 2,577 | 1,718 | 859 |
| 18 | 3,002 | 2,001 | 1,000 |
| 19 | 3,486 | 2,324 | 1,162 |
| 20 | 4,036 | 2,690 | 1,345 |
| 21 | 4,662 | 3,108 | 1,554 |
| 22 | 5,372 | 3,581 | 1,790 |
| 23 | 6,178 | 4,118 | 2,059 |
| 24 | 7,091 | 4,727 | 2,363 |
| 25 | 8,126 | 5,417 | 2,708 |
| 26 | 9,296 | 6,197 | 3,098 |
| 27 | 10,619 | 7,079 | 3,539 |
| 28 | 12,113 | 8,075 | 4,037 |
| 29 | 13,800 | 9,200 | 4,600 |
| 30 | 15,704 | 10,469 | 5,234 |

### Hydrogen Condenser temperature factor

| Maximum temperature | Factor |
|---|---|
| -120°C | 1.92 |
| -100°C | 1.84 |
| -80°C | 1.76 |
| -60°C | 1.68 |
| -40°C | 1.60 |
| -20°C | 1.52 |
| 0°C | 1.44 |
| 20°C | 1.36 |
| 40°C | 1.28 |
| 60°C | 1.20 |
| 80°C | 1.12 |
| 100°C | 1.04 |
| 120°C | 0.96 |
| 140°C | 0.88 |
| 160°C | 0.80 |

## Common pitfalls

- **Hydrogen goes up in smoke**: every flight burns some, with the return trip paid at departure for most missions.
- **A full stock stops producing**: spend it or enlarge your storage.
- **Stock is local**: a colony's resources cannot be used on the home planet; they have to be transported.
- **The home planet has no position bonus**: keep it in mind when picking where to settle your colonies.

## Related pages

- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Economy formulas](/en/economy/formulas)
- [Planets: size, temperature, type](/en/universe/planets)
