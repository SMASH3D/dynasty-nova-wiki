---
wiki_id: 90
locale: "en"
path: "economy/storage"
url: "https://wiki.dynastynova.com/en/economy/storage"
title: "Storage"
description: "Storage capacity and overflow."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:40.543Z"
updated: "2026-10-15T16:10:20.353Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Storage

> **In short**: each planet stores its own resources, within the limit of its storage buildings. Production fills storage up to its capacity, never beyond, then stops until you spend some. Whatever is already above capacity stays usable.
{.is-info}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Alloy Depot"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Crystal Chamber"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Hydrogen Tank">

## Rules

1. Each planet has a **capacity per resource**: metal, crystal, hydrogen.
2. The **Planetary Base** provides **10,000** capacity for each resource. A **moon**, which has neither a Planetary Base nor storage buildings, also holds 10,000 of each resource.
3. Each storage building adds its capacity to one resource: **Alloy Depot** (metal), **Crystal Chamber** (crystal), **Hydrogen Tank** (hydrogen). At level N it holds 5,000 × integer part(2.5 × e^(20 × N / 33)), up to level 20.
4. Production fills storage **up to its capacity, never beyond**. When the stock **reaches** capacity, **production of that resource stops**; it resumes as soon as the stock drops below it.
5. A stock **above** capacity stays fully usable: construction, research, shipyard, transport.
6. The **Logistics Center** enlarges capacity by **10% per level**, up to +100% at level 10 (see [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)).
7. The **Federated warehouses** alliance talent adds **10%** capacity per level (2 levels), and some dynasty talents add more.
8. These bonuses **add up**: they do not multiply each other. They apply to the planet's whole capacity, **the Planetary Base's 10,000 included**.

## Worked example

Alloy Depot level 2: 40,000, plus 10,000 from the Planetary Base, so **50,000 metal**. With an output of 1,366 metal per hour, an empty stock is full in 50,000 / 1,366 = **36.6 hours**.

Add a level 3 Logistics Center (+30%) and Federated warehouses level 2 (+20%):
- Total bonus: 30% + 20% = **+50%** (not 1.3 × 1.2).
- Metal capacity: 50,000 × 1.5 = **75,000**.

## Detailed data

Capacity of one storage building at level N, without the Planetary Base or bonuses, and cost to reach that level (metal / crystal):

| Level | Capacity | Alloy Depot (metal) | Crystal Chamber | Hydrogen Tank |
|---|---|---|---|---|
| 1 | 20,000 | 1,000 | 1,000 / 500 | 1,000 / 1,000 |
| 2 | 40,000 | 2,000 | 2,000 / 1,000 | 2,000 / 2,000 |
| 3 | 75,000 | 4,000 | 4,000 / 2,000 | 4,000 / 4,000 |
| 4 | 140,000 | 8,000 | 8,000 / 4,000 | 8,000 / 8,000 |
| 5 | 255,000 | 16,000 | 16,000 / 8,000 | 16,000 / 16,000 |
| 6 | 470,000 | 32,000 | 32,000 / 16,000 | 32,000 / 32,000 |
| 7 | 865,000 | 64,000 | 64,000 / 32,000 | 64,000 / 64,000 |
| 8 | 1,590,000 | 128,000 | 128,000 / 64,000 | 128,000 / 128,000 |
| 9 | 2,920,000 | 256,000 | 256,000 / 128,000 | 256,000 / 256,000 |
| 10 | 5,355,000 | 512,000 | 512,000 / 256,000 | 512,000 / 512,000 |
| 11 | 9,820,000 | 1,024,000 | 1,024,000 / 512,000 | 1,024,000 / 1,024,000 |
| 12 | 18,005,000 | 2,048,000 | 2,048,000 / 1,024,000 | 2,048,000 / 2,048,000 |
| 13 | 33,005,000 | 4,096,000 | 4,096,000 / 2,048,000 | 4,096,000 / 4,096,000 |
| 14 | 60,510,000 | 8,192,000 | 8,192,000 / 4,096,000 | 8,192,000 / 8,192,000 |
| 15 | 110,925,000 | 16,384,000 | 16,384,000 / 8,192,000 | 16,384,000 / 16,384,000 |
| 16 | 203,350,000 | 32,768,000 | 32,768,000 / 16,384,000 | 32,768,000 / 32,768,000 |
| 17 | 372,785,000 | 65,536,000 | 65,536,000 / 32,768,000 | 65,536,000 / 65,536,000 |
| 18 | 683,385,000 | 131,072,000 | 131,072,000 / 65,536,000 | 131,072,000 / 131,072,000 |
| 19 | 1,252,785,000 | 262,144,000 | 262,144,000 / 131,072,000 | 262,144,000 / 262,144,000 |
| 20 | 2,296,600,000 | 524,288,000 | 524,288,000 / 262,144,000 | 524,288,000 / 524,288,000 |

## Common pitfalls

- **Full storage is lost production**: watch the resource bar, especially before going away.
- **A large stock draws raiders**: see [Plunder](/en/combat/plunder).
- **Each planet counts on its own**: a colony's storage only serves that colony.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Economy formulas](/en/economy/formulas)
- [Plunder](/en/combat/plunder)
