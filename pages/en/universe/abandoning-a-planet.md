---
wiki_id: 85
locale: "en"
path: "universe/abandoning-a-planet"
url: "https://wiki.dynastynova.com/en/universe/abandoning-a-planet"
title: "Abandoning a colony"
description: "Conditions and consequences of abandoning a colony."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:30.810Z"
updated: "2026-10-15T18:53:37.036Z"
---

# Abandoning a colony

> **In short**: you can give up a colony for good to get its slot back. The planet stays on the map with what it holds, but immediately loses part of its buildings, fleet and defenses, then decays until it disappears after 60 days. Any other player can raid or recolonize it in the meantime, and then gets what is left.
{.is-info}

> **Universe setting**: every decay value of an abandoned planet (immediate losses, pace of losses, lifetime, delay before the former owner can take it back) may differ from one universe to another.
> Default: **values in the table below** · Redline: **the same**
{.is-info}

## Rules

### Conditions
1. The **mother planet** cannot be abandoned. A moon is never abandoned on its own: it leaves with its planet.
2. Abandoning is impossible while something is under way **on this planet or its moon**: building, ship or defense construction, repair, research started from this planet, a fleet travelling from or to it, a missile strike still in flight. The game lists everything that blocks it. Your other planets may be busy.
3. To confirm, you must type the planet's name. **Abandoning cannot be undone.**

### Immediate consequences
4. You lose the planet **for good**. Nothing is refunded, and its points leave your score.
5. You get **a colony slot back at once**. If you were looking at that planet, the game takes you back to your mother planet.
6. Resources stay where they are, and never decay. Production stops.
7. The **first shock**, on the planet as on its moon: each building loses **1 level**, the fleet loses **30%** of each ship type and the defenses **35%** of each type (rounded down). Solar Collectors are **all lost**.
8. Ships destroyed by this shock leave a **debris field** in orbit, at the universe's ship debris rate (30% by default). Defenses and Solar Collectors leave none.
9. The planet's **moon**, and everything on it, is abandoned along with it.

### Afterwards
10. Buildings lose 1 level **every 2 days**. The remaining fleet loses 5% of what is left every 2 days, the defenses 5% every 3 days: at least one unit each time, as long as any are left.
11. Other players can **spy on, attack, raid or recolonize** it. Nobody can transport resources to it. The attack limit does not apply: the planet no longer has an owner.
12. Whoever recolonizes it takes over **everything left**, moon included, and the decay stops.
13. The planet **disappears** after **60 days**, or earlier once nothing is left on it or its moon (every building at 0, no ship or defense left). Resources go with it; the position becomes free again, under its original name. Debris fields in orbit stay.
14. The former owner cannot recolonize it for **30 days**.

## Worked example

You abandon a colony with a level 10 Mineral Excavator, 1,000 Interceptors, 200 defenses of one type and 50 Solar Collectors.
- At once: Excavator level **9**; 300 Interceptors destroyed, **700** left; **130** defenses left; no Solar Collector left.
- The 300 destroyed Interceptors leave 300 × 3,000 × 30% = **270,000 metal** and 300 × 1,000 × 30% = **90,000 crystal** of debris.
- The Excavator reaches 0 after 18 days. The planet still lasts 60 days, as long as ships or defenses are left.

What is left over the days:

| Day | Mineral Excavator | Interceptors | Defenses |
|---|---|---|---|
| 0 | 9 | 700 | 130 |
| 2 | 8 | 665 | 130 |
| 6 | 6 | 601 | 118 |
| 10 | 4 | 543 | 113 |
| 20 | 0 | 422 | 98 |
| 40 | 0 | 255 | 72 |
| 60 | 0 | 156 | 53 |

If a player recolonizes it after 6 days, they get the Excavator at level **6**, 601 Interceptors, 118 defenses and all the resources.

## Detailed data

| Item | Immediate loss | Loss afterwards |
|---|---|---|
| Buildings | −1 level | −1 level every 2 days |
| Ships | −30% | −5% of what is left every 2 days |
| Defenses | −35% | −5% of what is left every 3 days |
| Solar Collectors | −100% |  |
| Resources | no loss | no loss |
| Planet |  | disappears after 60 days, or earlier if nothing is left on it |
| Recolonization by the former owner |  | barred for 30 days |

## Common pitfalls

- **Empty the planet first**: bring fleet and resources home before abandoning, or they stay at the mercy of raiders and of whoever recolonizes it.
- **The moon is lost too**: a moon and its buildings leave with the planet.
- **No way back**: you cannot take it back for 30 days, and it will have kept decaying.
- **Everything must be idle, moon included**: a construction, a research or a fleet on its way blocks the abandonment.

## Related pages

- [Colonization](/en/universe/colonization)
- [Planets: size, temperature, type](/en/universe/planets)
- [Moons](/en/universe/moons)
- [Debris fields](/en/combat/debris)
