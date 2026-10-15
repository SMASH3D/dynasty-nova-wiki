---
wiki_id: 91
locale: "en"
path: "economy/buildings"
url: "https://wiki.dynastynova.com/en/economy/buildings"
title: "Buildings list"
description: "All buildings: role, maximum level, requirements."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:42.469Z"
updated: "2026-10-15T18:52:44.907Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Buildings list

> **In short**: a planet can hold up to 17 buildings. A moon takes 5: its 3 lunar buildings, plus the Automaton Factory and the Orbital Dock. Mines produce resources, power plants produce energy, storage keeps your stock, and facilities open research, ships, defenses and missiles. Every building level takes one field.
{.is-info}

> **Universe setting**: the construction speed divides building times.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

1. A building goes up **level by level**. Level N costs the level 1 cost × factor^(N − 1), rounded down for each resource (see [Economy formulas](/en/economy/formulas)).
2. **Each level takes one field** on the planet. Exceptions: the Planetary Base (one field, single level) and the Repair Station, which takes none.
3. An enemy can **never destroy your buildings**. Only their owner can demolish them (see [Demolishing a building](/en/economy/demolition)); only the destruction of a moon takes that moon's buildings with it.
4. A building is **paid when its construction starts**, not when it is queued.
5. **Points**: each level earns 1 point per 1,000 resources spent (metal, crystal and hydrogen), counted in economy points.
6. Each building has a **maximum level**, except the lunar buildings, limited by the room on the moon.
7. The **Planetary Base** (Colonial Base on a colony) is there from founding and cannot be demolished.
8. Some buildings need a **required energy**: the planet's energy production must reach that threshold when construction starts; nothing is used up.
9. **On a moon**: the Lunar base, the Sensor phalanx and the Jump gate, plus the Automaton Factory and the Orbital Dock, at the same costs and with the same requirements as on a planet. A moon starts with 1 field; each Lunar base level opens 3 and takes 1, never beyond what the moon's diameter allows.

## Worked example

Raising the Mineral Excavator from level 13 to level 14:
- Cost: 60 × 1.5^13 = **11,677 metal** and 15 × 1.5^13 = **2,919 crystal**, so 14,596 resources and **14.6 economy points**.
- Output goes from 1,346 to **1,594 metal per hour**, energy use from 448 to **531**.
- Time with an Automaton Factory level 4: 14,596 / (2,500 × 5) hours, so **4,204 seconds** (1 h 10 min).

## Detailed data

| Building | Category | Role | Level 1 cost (metal / crystal / hydrogen) | Factor | Max level | Requirements | Where |
|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/buildings/base-planetaire.jpg" width="48" alt="Planetary Base / Colonial Base"> Planetary Base / Colonial Base | base | Heart of the planet: 10,000 storage per resource, 20 metal and 10 crystal per hour | given at founding |  | 1 | none | planet |
| <img src="/images/illustrations/buildings/excavateur-mineral.jpg" width="48" alt="Mineral Excavator"> Mineral Excavator | production | Produces metal | 60 / 15 / 0 | 1.5 | 50 | none | planet |
| <img src="/images/illustrations/buildings/extracteur-cristallin.jpg" width="48" alt="Crystal Extractor"> Crystal Extractor | production | Produces crystal | 48 / 24 / 0 | 1.6 | 50 | none | planet |
| <img src="/images/illustrations/buildings/condensateur-d-hydrogene.jpg" width="48" alt="Hydrogen Condenser"> Hydrogen Condenser | production | Produces hydrogen, more on a cold planet | 225 / 75 / 0 | 1.5 | 50 | none | planet |
| <img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="48" alt="Photovoltaic Sensors"> Photovoltaic Sensors | energy | Produces energy, more in hot weather | 75 / 30 / 0 | 1.5 | 50 | none | planet |
| <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="48" alt="Thermonuclear Reactor"> Thermonuclear Reactor | energy | Produces energy by burning hydrogen | 900 / 360 / 180 | 1.8 | 50 | Hydrogen Condenser 5, Energy Science 3 | planet |
| <img src="/images/illustrations/buildings/depot-alliages.jpg" width="48" alt="Alloy Depot"> Alloy Depot | storage | Stores metal | 1,000 / 0 / 0 | 2 | 20 | none | planet |
| <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="48" alt="Crystal Chamber"> Crystal Chamber | storage | Stores crystal | 1,000 / 500 / 0 | 2 | 20 | none | planet |
| <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="48" alt="Hydrogen Tank"> Hydrogen Tank | storage | Stores hydrogen | 1,000 / 1,000 / 0 | 2 | 20 | none | planet |
| <img src="/images/illustrations/facilities/centre-d-innovation.jpg" width="48" alt="Innovation Center"> Innovation Center | research | Enables research and speeds it up | 200 / 400 / 200 | 2 | 12 | none | planet |
| <img src="/images/illustrations/facilities/fabrique-d-automates.jpg" width="48" alt="Automaton Factory"> Automaton Factory | facility | Speeds up building construction | 400 / 120 / 200 | 2 | 10 | none | planet and moon |
| <img src="/images/illustrations/facilities/dock-orbital.jpg" width="48" alt="Orbital Dock"> Orbital Dock | facility | Builds ships and defenses, faster at each level | 400 / 200 / 100 | 2 | 12 | Automaton Factory 2 | planet and moon |
| <img src="/images/illustrations/facilities/assembleur-moleculaire.jpg" width="48" alt="Molecular Assembler"> Molecular Assembler | facility | Halves, at each level, the time of buildings, ships and defenses | 1,000,000 / 500,000 / 100,000 | 2 | 10 | Automaton Factory 10, Quantum Computing 10 | planet |
| <img src="/images/illustrations/facilities/station-de-reparation.jpg" width="48" alt="Repair Station"> Repair Station | shipyard | Recovers a share of the ships lost in defense | 200 / 0 / 50 · 50 required energy | 5 (required energy: 2.5) | 10 | Orbital Dock 2 | planet |
| <img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="48" alt="Planetary Modulator"> Planetary Modulator | resource | Adds fields to the planet | 0 / 50,000 / 100,000 · 1,000 required energy | 2 | 10 | Molecular Assembler 1, Energy Science 12 | planet |
| <img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="48" alt="Ballistic Arsenal"> Ballistic Arsenal | resource | Stores missiles | 20,000 / 20,000 / 1,000 | 2 | 10 | Orbital Dock 1 | planet |
| <img src="/images/illustrations/facilities/centre-logistique.jpg" width="48" alt="Logistics Center"> Logistics Center | resource | Enlarges storage by 10% per level | 20,000 / 40,000 / 0 | 2 | 10 | Quantum Computing 2 | planet |
| <img src="/images/illustrations/facilities/base-lunaire.jpg" width="48" alt="Lunar base"> Lunar base | facility | Makes the moon's surface buildable: each level opens 3 fields and takes 1 | 20,000 / 40,000 / 20,000 | 2 | none | none | moon |
| <img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="48" alt="Sensor phalanx"> Sensor phalanx | facility | Spots fleets around a planet | 20,000 / 40,000 / 20,000 | 2 | none | Lunar base 1 | moon |
| <img src="/images/illustrations/facilities/porte-de-saut.jpg" width="48" alt="Jump gate"> Jump gate | facility | Instant jump between two moons | 2,000,000 / 4,000,000 / 2,000,000 | 2 | none | Lunar base 1, Hyperspace Technology 7 | moon |

Level N cost follows from the factor: for instance, Orbital Dock level 5 costs 400 × 2^4 = 6,400 metal, 3,200 crystal and 1,600 hydrogen. The cost, energy and output of every level are in the [appendix: buildings level by level](/en/economy/building-levels).

## Common pitfalls

- **Mines and energy go together**: each mine level uses more energy. Without enough power, all production slows down (see [Energy](/en/economy/energy)).
- **Fields are limited**: each level takes one. Think of the Planetary Modulator before your planet fills up.
- **A queued order is not paid**: it is paid when it starts. If the planet no longer has the resources then, the order is dropped at no cost.
- **Factors are not all equal**: the Crystal Extractor (1.6) and the Reactor (1.8) get pricier faster than the other mines.

## Related pages

- [Resources](/en/economy/resources)
- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Economy formulas](/en/economy/formulas)
- [Build queues](/en/economy/build-queue)
- [Demolishing a building](/en/economy/demolition)
- [Tech tree](/en/research/tech-tree)
- [Appendix: buildings level by level](/en/economy/building-levels)
