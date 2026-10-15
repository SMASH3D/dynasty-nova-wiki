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
updated: "2026-10-15T16:10:18.767Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Resources

> **In short**: three resources can be stored, metal, crystal and hydrogen, produced continuously by your mines, even while you are offline. Energy, the fourth resource, cannot be stored: it powers the mines. Each planet has its own stock.
{.is-info}

> **Universe setting**: economy speed (production) may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Metal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Crystal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogen"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Energy">

## Rules

1. **Metal**: the basis of every construction. Produced by the Mineral Excavator.
2. **Crystal**: needed for technologies and advanced parts. Produced by the Crystal Extractor.
3. **Hydrogen**: fleet fuel, also used by research and the Thermonuclear Reactor. Produced by the Hydrogen Condenser, more on a cold planet.
4. **Energy**: produced by Photovoltaic Sensors, the Thermonuclear Reactor and Solar Collectors, used by mines. It cannot be stored (see [Energy](/en/economy/energy)).
5. Production is **continuous**, computed per hour, and each planet has **its own stock**, capped by its storage.
6. The **Planetary Base** gives a small fixed income: **20 metal and 10 crystal per hour**.
7. Production stops when a resource's stock reaches its capacity (see [Storage](/en/economy/storage)), during [vacation mode](/en/players/vacation-mode), or while a private universe is frozen (see [Private universes](/en/misc/private-universes)).
8. Possible bonuses: Plasma Technology, the Coordinated extraction alliance talent (+5% per level), planet temperature for hydrogen, and the colonies' **position bonus** (up to +40% crystal at positions 1 to 3, up to +35% metal at positions 6 to 10; see [Planets](/en/universe/planets)).

## Worked example

Output seen in game on a planet with Mineral Excavator 13 and Crystal Extractor 13, with no energy shortage:
- Metal: 1,346 (Excavator) + 20 (Planetary Base) = **1,366 per hour**, about **32,800 per day**.
- Crystal: 897 (Extractor) + 10 (Planetary Base) = **907 per hour**.

## Detailed data

### Output seen in game (per hour, at full energy)

| Level | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Mineral Excavator (metal) | 1,346 | 1,594 | 1,879 | 2,205 | 2,577 | 3,002 | 3,486 | 4,036 | 4,662 | 5,372 |
| Crystal Extractor (crystal) | 897 | 1,063 | 1,253 | 1,470 | 1,718 | 2,001 | 2,324 | 2,690 | 3,108 | 3,581 |

| Level | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|
| Hydrogen Condenser (planet at 60 °C max) | 254 | 311 | 376 | 451 | 538 | 637 | 751 | 882 | 1,031 | 1,200 |

Hydrogen output varies with the planet's maximum temperature (see [Planets](/en/universe/planets)).

## Common pitfalls

- **Hydrogen burns fast**: every flight uses it, with outbound and return paid at departure for most missions.
- **A full stock stops producing**: empty your storage or expand it.
- **Stock is local**: a colony's resources cannot be used on the mother planet, they must be transported.

## Related pages

- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Buildings list](/en/economy/buildings)
- [Planets: size, temperature, type](/en/universe/planets)
