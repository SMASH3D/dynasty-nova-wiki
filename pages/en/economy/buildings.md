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
updated: "2026-10-15T16:10:14.029Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Buildings list

> **In short**: a planet can hold up to 17 buildings. A moon takes 5: its 3 lunar buildings, plus the Automaton Factory and the Orbital Dock. Mines produce resources, power plants produce energy, storage keeps your stock, and facilities unlock research, ships, defenses and missiles. Every building level takes one field on the planet.
{.is-info}

> **Universe setting**: building speed may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

1. Buildings are built **level by level**. Each level costs more than the previous one.
2. **Each level takes one field** on the planet. Exceptions: the Planetary Base (one field, single level) and the Repair Station, which takes no field.
3. Buildings can **never be destroyed by an enemy**. Only their owner can demolish them (see [Demolishing a building](/en/economy/demolition)).
4. A building is **paid when its construction starts**, not when it is queued.
5. **Points**: each level is worth 1 point per 1,000 resources spent, counted as economy points.
6. Every building has a **maximum level**: going higher would unlock nothing.
7. The **Planetary Base** (Colonial Base on a colony) exists from the start, cannot be demolished, and provides base storage and a small fixed income.

## Worked example

Costs seen in game to raise the Mineral Excavator from level 13 to level 14:
- **11,677 metal and 2,919 crystal**, that is 14,596 resources, so **14.6 economy points**.
- Output rises from 1,346 to **1,594 metal/h**, and energy use from 448 to **531**.

## Detailed data

### Role, maximum level and requirements

| Building | Category | Role | Max level | Requirements |
|---|---|---|---|---|
| <img src="/images/illustrations/buildings/base-planetaire.jpg" width="48" alt="Planetary Base / Colonial Base"> Planetary Base / Colonial Base | base | Heart of the planet: base storage (10,000 of each resource), fixed income (20 metal and 10 crystal per hour) | 1 | none |
| <img src="/images/illustrations/buildings/excavateur-mineral.jpg" width="48" alt="Mineral Excavator"> Mineral Excavator | production | Produces metal | 50 | none |
| <img src="/images/illustrations/buildings/extracteur-cristallin.jpg" width="48" alt="Crystal Extractor"> Crystal Extractor | production | Produces crystal | 50 | none |
| <img src="/images/illustrations/buildings/condensateur-d-hydrogene.jpg" width="48" alt="Hydrogen Condenser"> Hydrogen Condenser | production | Produces hydrogen, more on a cold planet | 50 | none |
| <img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="48" alt="Photovoltaic Sensors"> Photovoltaic Sensors | energy | Produces energy, more on a hot planet | 50 | none |
| <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="48" alt="Thermonuclear Reactor"> Thermonuclear Reactor | energy | Produces energy by burning hydrogen | 50 | Hydrogen Condenser 5, Energy Science 3 |
| <img src="/images/illustrations/buildings/depot-alliages.jpg" width="48" alt="Alloy Depot"> Alloy Depot | storage | Raises metal storage | 20 | none |
| <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="48" alt="Crystal Chamber"> Crystal Chamber | storage | Raises crystal storage | 20 | none |
| <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="48" alt="Hydrogen Tank"> Hydrogen Tank | storage | Raises hydrogen storage | 20 | none |
| <img src="/images/illustrations/facilities/centre-d-innovation.jpg" width="48" alt="Innovation Center"> Innovation Center | research | Enables research and speeds it up | 12 | none |
| <img src="/images/illustrations/facilities/fabrique-d-automates.jpg" width="48" alt="Automaton Factory"> Automaton Factory | facility | Speeds up building construction | 10 | none |
| <img src="/images/illustrations/facilities/dock-orbital.jpg" width="48" alt="Orbital Dock"> Orbital Dock | facility | Builds ships and defenses | 12 | Automaton Factory 2 |
| <img src="/images/illustrations/facilities/assembleur-moleculaire.jpg" width="48" alt="Molecular Assembler"> Molecular Assembler | facility | Greatly speeds up construction | 10 | Automaton Factory 10, Quantum Computing 10 |
| <img src="/images/illustrations/facilities/station-de-reparation.jpg" width="48" alt="Repair Station"> Repair Station | shipyard | Recovers part of the ships destroyed in defense | 10 | Orbital Dock 2 |
| <img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="48" alt="Planetary Modulator"> Planetary Modulator | resource | Adds fields to the planet | 10 | Molecular Assembler 1, Energy Science 12 |
| <img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="48" alt="Ballistic Arsenal"> Ballistic Arsenal | resource | Stores missiles | 10 | Orbital Dock 1 |
| <img src="/images/illustrations/facilities/centre-logistique.jpg" width="48" alt="Logistics Center"> Logistics Center | resource | Enlarges storage by 10% per level | 10 | Quantum Computing 2 |

### Moon buildings

| Building | Role |
|---|---|
| <img src="/images/illustrations/facilities/base-lunaire.jpg" width="48" alt="Lunar base"> Lunar base | Makes a moon's surface buildable: each level opens 3 fields and takes 1 |
| <img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="48" alt="Sensor phalanx"> Sensor phalanx | Spots fleets around a planet (see [Sensor phalanx](/en/espionage/sensor-phalanx)) |
| <img src="/images/illustrations/facilities/porte-de-saut.jpg" width="48" alt="Jump gate"> Jump gate | Instant jump between two moons (see [Jump gate](/en/fleet/jump-gate)) |

On a moon you can also build the **Automaton Factory** and the **Orbital Dock**, at the same costs and with the same requirements as on a planet. The other planet buildings cannot be built there.

### Costs seen in game

Cost of one given level, recorded on a planet in the Redline universe. Full level-by-level tables will be added to each building's own page.

| Building | Level | Metal | Crystal | Hydrogen | Energy required |
|---|---|---|---|---|---|
| Mineral Excavator | 14 | 11,677 | 2,919 | 0 | |
| Crystal Extractor | 14 | 21,617 | 10,808 | 0 | |
| Hydrogen Condenser | 10 | 8,649 | 2,883 | 0 | |
| Photovoltaic Sensors | 14 | 14,596 | 5,838 | 0 | |
| Thermonuclear Reactor | 2 | 1,620 | 648 | 324 | |
| Alloy Depot | 3 | 4,000 | 0 | 0 | |
| Crystal Chamber | 2 | 2,000 | 1,000 | 0 | |
| Hydrogen Tank | 2 | 2,000 | 2,000 | 0 | |
| Innovation Center | 5 | 3,200 | 6,400 | 3,200 | |
| Automaton Factory | 5 | 6,400 | 1,920 | 3,200 | |
| Orbital Dock | 5 | 6,400 | 3,200 | 1,600 | |
| Molecular Assembler | 1 | 1,000,000 | 500,000 | 100,000 | |
| Repair Station | 1 | 200 | 0 | 50 | 50 |
| Planetary Modulator | 1 | 0 | 50,000 | 100,000 | 1,000 |
| Ballistic Arsenal | 1 | 20,000 | 20,000 | 1,000 | |
| Logistics Center | 1 | 20,000 | 40,000 | 0 | |

**Energy required** is not consumed: the planet's energy output only has to reach that threshold when construction starts.

## Common pitfalls

- **Mines and energy go together**: every mine level uses more energy. Without enough power, all output slows down (see [Energy](/en/economy/energy)).
- **Fields are limited**: each level takes one. Think of the Planetary Modulator before your planet fills up.
- **A queued order is not paid yet**: it is paid when it starts. If the planet cannot afford it at that moment, the order is dropped at no cost.
- **Maximum levels**: there is no point trying to push the Innovation Center or the Orbital Dock beyond level 12, or the Automaton Factory beyond level 10.

## Related pages

- [Resources](/en/economy/resources)
- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Build queues](/en/economy/build-queue)
- [Demolishing a building](/en/economy/demolition)
- [Tech tree](/en/research/tech-tree)
