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

> **In short**: each planet stores its own resources, within the limit of its storage buildings. When a resource's stock reaches its capacity, its production stops until you spend some. The surplus itself stays usable.
{.is-info}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Alloy Depot"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Crystal Chamber"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Hydrogen Tank">

## Rules

1. Each planet has a **capacity per resource**: metal, crystal, hydrogen.
2. The **Planetary Base** provides **10,000** capacity for each resource.
3. Storage buildings raise capacity: **Alloy Depot** (metal), **Crystal Chamber** (crystal), **Hydrogen Tank** (hydrogen), up to level 20.
4. Production fills storage **up to its capacity, never beyond**. When the stock **reaches** capacity, **production of that resource stops**; it resumes as soon as the stock drops below it.
5. The **surplus stays usable**: construction, research, shipyard, transport.
6. The **Logistics Center** enlarges storage by **10% per level**, up to +100% at level 10 (see [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)).
7. The **Federated warehouses** alliance talent adds 10% capacity per level.
8. These bonuses, and those of dynasty talents, **add up**: they do not multiply each other. They apply to the planet's whole capacity, **the Planetary Base's 10,000 included**.

## Worked example

Capacities seen in game:
- Alloy Depot level 2: 40,000, plus 10,000 from the Planetary Base, so **50,000 metal**.
- Crystal Chamber level 1: 20,000 + 10,000 = **30,000 crystal**.

With 50,000 capacity and an output of 1,366 metal/h, an empty stock is full in **just under 37 hours**.

Add a level 3 Logistics Center (+30%) and the Federated warehouses talent at level 2 (+20%):
- Total bonus: 30% + 20% = **+50%** (not 1.3 × 1.2).
- Metal capacity: 50,000 × 1.5 = **75,000**.

## Detailed data

| Storage | Level 1 | Level 2 | Recorded cost |
|---|---|---|---|
| Alloy Depot | 20,000 | 40,000 | level 3: 4,000 metal |
| Crystal Chamber | 20,000 | 40,000 | level 2: 2,000 metal, 1,000 crystal |
| Hydrogen Tank | 20,000 | 40,000 | level 2: 2,000 metal, 2,000 crystal |

The Planetary Base's 10,000 is added to these capacities. Full tables will be added to each storage building's page.

## Common pitfalls

- **Full storage means lost production**: watch the resource bar, especially before going away.
- **A large stock attracts raiders**: the attacker takes 50% of each resource.
- **Each planet counts separately**: a colony's storage only serves that colony.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Plunder](/en/combat/plunder)
