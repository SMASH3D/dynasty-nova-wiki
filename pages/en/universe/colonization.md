---
wiki_id: 84
locale: "en"
path: "universe/colonization"
url: "https://wiki.dynastynova.com/en/universe/colonization"
title: "Colonization"
description: "Founding colonies with the Space Pioneer."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:28.978Z"
updated: "2026-10-02T17:40:35.384Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Colonization

> **In short**: to found a colony, first spy the target position, then send a Space Pioneer there on a Colonization mission. How many planets you can own depends on your Astrophysics level: 2 planets at level 1, then one more every two levels. The colony starts empty, with the resources and ships you sent.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

> **Universe setting**: how long the former owner of an abandoned planet must wait before recolonizing it may differ from one universe to another.
> Default: **30 days** · Redline: **30 days**
{.is-info}

<img src="/images/illustrations/ships/pionnier-spatial.jpg" width="180" alt="Space Pioneer">

## Rules

### Before leaving
1. You need a **Space Pioneer** (Orbital Dock 4, Impulse Drive 3, Astrophysics 1) and a **free colony slot**.
2. **Number of planets** (mother planet included) = 1 + whole part of ((Astrophysics level + 1) / 2). Only planets count: a moon does not take a colony slot.
3. The target must have been **spied**, by you or by a member of your alliance. A position never spied cannot be colonized.
4. The target can be:
   - a **free position** in a system;
   - a planet **abandoned** by another player. Its former owner has to wait 30 days.
5. Deep space, the Stellar Station and moons cannot be colonized.
6. The **Colonization** mission is one way: hydrogen for a return trip is not charged.

### On arrival
7. The game checks the colony slot again. If you no longer have one, or if the position was taken in the meantime, the fleet turns back and a report tells you why.
8. **Only one Space Pioneer is used up**: it becomes the colony. The fleet's other ships, other Pioneers included, **stay on the new colony** as its first fleet.
9. The whole fleet's cargo is unloaded on the colony: these are its **starting resources**.
10. On a free position, the colony starts **with no building at all**. First build the **Colonial Base** (free, 10 seconds): no other building can be started before it. Meanwhile, the colony already stores 10,000 of each resource.
11. Its size and temperature depend on its position, and it gets the **position bonus** (see [Planets](/en/universe/planets)).
12. On an **abandoned** planet, you take over **everything left**: buildings, resources, ships, defenses, and its moon with whatever stands on it. The decay stops and output resumes for you (see [Abandoning a colony](/en/universe/abandoning-a-planet)).

## Worked example

You have Astrophysics level 3:
- Possible planets: 1 + whole part of ((3 + 1) / 2) = **3**, that is your mother planet and 2 colonies.
- Going to level 4 changes nothing (3 planets). You need level 5 for a 4th planet.

You send 2 fully loaded Space Pioneers to a free position already spied:
- They carry 7,500 × 2 = **15,000 resources**.
- On arrival, one Pioneer becomes the colony, the other stays in the colony's orbit, and the 15,000 resources are unloaded there.

## Detailed data

### Planets by Astrophysics level

| Level | 0 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Total planets | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

Even levels add no planet (level 2 gives as many as level 1).

### The Space Pioneer

| Cost | Structure | Cargo | Base speed | Drive | Fuel use |
|---|---|---|---|---|---|
| 10,000 metal, 20,000 crystal, 10,000 hydrogen | 30,000 | 7,500 | 2,500 | Impulse Drive | 1,000 |

## Common pitfalls

- **Spy before you leave**: without the position being spied, by you or your alliance, the mission is refused.
- **Load the fleet**: the colony has no resources other than those you bring.
- **Escorts do not come back**: every ship sent with the Pioneer stays on the colony.
- **One more colony every two levels**: check that you have a free slot before sending the Pioneer, and that you still have it on arrival.
- **Choose the position**: close to the star, a small hot planet and a crystal bonus; in the middle of the system, a metal bonus; far out, a large cold planet, better for hydrogen.

## Related pages

- [Planets: size, temperature, type](/en/universe/planets)
- [Abandoning a colony](/en/universe/abandoning-a-planet)
- [List of technologies](/en/research/technologies)
- [Missions](/en/fleet/missions)
- [Spying](/en/espionage/spying)
