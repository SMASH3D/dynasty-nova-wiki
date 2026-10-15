---
wiki_id: 112
locale: "en"
path: "defense/missiles"
url: "https://wiki.dynastynova.com/en/defense/missiles"
title: "Missiles"
description: "Ballistic Arsenal, Interception Missiles and Long-Range Warheads."
tags: ["defense", "missiles"]
published: true
created: "2026-10-02T13:11:23.628Z"
updated: "2026-10-02T17:40:29.534Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Missiles

> **In short**: missiles are stored in the Ballistic Arsenal. **Long-Range Warheads** destroy the defenses of an enemy planet in the same galaxy without sending a fleet; their range depends on the Impulse Drive. **Interception Missiles** automatically shoot down, one for one, the Warheads aimed at your planet. Missiles never take part in fleet battles.
{.is-info}

> **Universe setting**: the attack limit, which also counts missile salvos, may differ from one universe to another.
> Default: **6 attacks per 24 h** · Redline: **6 attacks per 24 h**
{.is-info}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Ballistic Arsenal"> <img src="/images/illustrations/defense/intercepteurs.jpg" width="180" alt="Interception Missile"> <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="180" alt="Long-Range Warheads">

## Rules

### The Ballistic Arsenal
1. Missiles are stored in the **Ballistic Arsenal**, which offers **10 slots per level** (level 10 at most). It can only be built on a planet.
2. An **Interception Missile** takes **1 slot**, a **Long-Range Warhead** takes **2**.
3. Missiles in the queue or under construction already count: an order that would not fit in the free slots is refused before anything is spent.
4. Missiles take no planet fields. Only the Arsenal itself takes one field per level.
5. Demolishing an Arsenal level while it is full destroys no missile; you just cannot order more.
6. Missiles never fire during a battle, do not count towards the planet's defensive power and cannot be destroyed by a salvo.
7. **Points**: like defenses, 1 point per 1,000 resources, in military points, while they sit in the silo. A missile fired, or an Interception Missile spent, leaves your points.

### Range and flight
8. **Range**: with the Impulse Drive at level $N$, a Warhead reaches any planet at most $5 \times N - 1$ systems away, **in the same galaxy** only.
   - $N$: your Impulse Drive level. Another galaxy is always out of range, whatever the level.
9. The systems of a galaxy form a ring: system 99 is next to system 1. The distance is counted the short way round. The position within the system does not matter.
10. **Flight time**: 30 seconds per system of distance, and 30 seconds at least (same system). The target gets **no warning** before impact.
11. A salvo **cannot be recalled**. Warheads leave the silo at launch and never come back, even if the target planet is abandoned in the meantime.

### Targets and restrictions
12. A salvo leaves from a planet and targets a **planet**: never a moon, an empty slot or one of your own planets.
13. Forbidden against a member of your alliance, a player **in vacation mode** and a protected player ([Beginner protection](/en/players/beginner-protection)). You cannot fire during your own vacation.
14. A salvo **counts as an attack** in the [attack limit](/en/players/attack-limit) on the targeted player. Since it cannot be recalled, the slot is spent.
15. Firing **ends your own new-player protection**, for good.
16. An abandoned planet can be targeted: nobody defends it, and the attack limit does not apply.
17. During **maintenance**, no launch is accepted; a salvo already in flight lands normally.

### On impact
18. **Interception**: each Interception Missile on the target planet shoots down **one Warhead**, automatically, before any damage. It is spent.
19. **Damage**: each Warhead that gets through brings $12{,}000 \times (1 + 0.1 \times S)$ damage, pooled for the whole salvo (rounded down).
   - $S$: the shooter's Weapon Systems level.
20. **Toughness** of a defense: its shield + its combat hull, with the defender's research and bonuses (see [Defenses list](/en/defense/defenses), rule 8).
21. **Target order**: the designated target first (if the planet has any), then defenses by decreasing toughness. Without a designated target, the toughest first.
22. A defense is only destroyed **whole**. On each line, the salvo destroys as many units as its remaining damage pays for; if it cannot pay for a single one, it moves on to the next, less tough line. Whatever is left at the end is lost.
23. A salvo **only destroys defenses**: never buildings, the fleet in orbit, resources or the missiles in the silo.
24. Defenses destroyed by a Warhead are **lost for good**: no free rebuild. Their points are removed.
25. Both the shooter and the defender get a report: Warheads fired, intercepted, landed, defenses hit and planet of origin.
26. Some dynasty talents change the range, the Arsenal capacity, the damage and the interception (see [Dynasty and talents](/en/dynasty)).

## Worked example

**Filling a level 3 Ballistic Arsenal**
- Capacity: 3 × 10 = **30 slots**.
- 10 Interception Missiles (10 slots) + 10 Long-Range Warheads (20 slots) = 30: the Arsenal is full.
- Cost of the 10 Warheads: 125,000 metal, 25,000 crystal, 100,000 hydrogen, that is 250 military points, removed when they leave.

**Range and flight** (Impulse Drive 4)
- Range: 5 × 4 − 1 = **19 systems**.
- From [3:40:8] to [3:55:4]: 15 systems, in range. Flight: 15 × 30 = 450 seconds, that is **7 min 30 s**.
- From [5:97:6] to [5:3:10]: the ring goes through 98, 99, 1, 2, 3, that is **5 systems**, in range from Impulse Drive 2; flight of 2 min 30 s.
- To [4:40:8]: another galaxy, **out of range**.

**A salvo of 5 Warheads** fired with Weapon Systems 6, at a planet holding 3 Interception Missiles, 1 Protective Dome, 2 Plasma Ejectors and 40 Ballistic Projectors (defender at Shielding Technology 4 and Armor Technology 5)
- Interception: 3 Warheads shot down, **2 land**. The 3 Interception Missiles are spent.
- Damage: 2 × 12,000 × 1.6 = **38,400**.
- Toughness: Dome 29,000, Plasma Ejector 15,420, Ballistic Projector 328.
- No designated target: 1 Protective Dome (1 × 29,000): 38,400 → 9,400; 28 Ballistic Projectors (28 × 328): 9,400 → 216. The Ejectors (one would take 15,420) are skipped. Result: **1 Protective Dome, 28 Ballistic Projectors**, 216 damage lost.
- Designated target "Plasma Ejector": 2 Plasma Ejectors (2 × 15,420): 38,400 → 7,560; 23 Ballistic Projectors (23 × 328): 7,560 → 16. The Dome is skipped. Result: **2 Plasma Ejectors, 23 Ballistic Projectors**, 16 damage lost.

## Detailed data

### Missiles

| Missile | Metal | Crystal | Hydrogen | Points | Arsenal slots | Damage | Base time | Requirements |
|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/intercepteurs.jpg" width="48" alt="Interception Missile"> Interception Missile | 8,000 | 2,000 | 0 | 10 | 1 | none | 3 h 12 min | Orbital Dock 1, Ballistic Arsenal 2 |
| <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="48" alt="Long-Range Warheads"> Long-Range Warheads | 12,500 | 2,500 | 10,000 | 25 | 2 | 12,000 | 6 h | Orbital Dock 1, Ballistic Arsenal 4, Impulse Drive 1 |

Damage is that of one Warhead with no research (rule 19). An Interception Missile deals no damage: it only shoots down a Warhead. The Impulse Drive 1 required for Warheads already gives a range of 4 systems.

### Ballistic Arsenal

Requirement: Orbital Dock 1. The cost doubles at each level.

| Level | Metal | Crystal | Hydrogen | Slots | Warheads at most | Interception Missiles at most |
|---|---|---|---|---|---|---|
| 1 | 20,000 | 20,000 | 1,000 | 10 | 5 | 10 |
| 2 | 40,000 | 40,000 | 2,000 | 20 | 10 | 20 |
| 3 | 80,000 | 80,000 | 4,000 | 30 | 15 | 30 |
| 4 | 160,000 | 160,000 | 8,000 | 40 | 20 | 40 |
| 5 | 320,000 | 320,000 | 16,000 | 50 | 25 | 50 |
| 6 | 640,000 | 640,000 | 32,000 | 60 | 30 | 60 |
| 7 | 1,280,000 | 1,280,000 | 64,000 | 70 | 35 | 70 |
| 8 | 2,560,000 | 2,560,000 | 128,000 | 80 | 40 | 80 |
| 9 | 5,120,000 | 5,120,000 | 256,000 | 90 | 45 | 90 |
| 10 | 10,240,000 | 10,240,000 | 512,000 | 100 | 50 | 100 |

### Range by Impulse Drive level

| Impulse Drive | Range (systems) | Flight to the limit |
|---|---|---|
| 1 | 4 | 2 min |
| 2 | 9 | 4 min 30 s |
| 3 | 14 | 7 min |
| 4 | 19 | 9 min 30 s |
| 5 | 24 | 12 min |
| 6 | 29 | 14 min 30 s |
| 7 | 34 | 17 min |
| 8 | 39 | 19 min 30 s |
| 9 | 44 | 22 min |
| 10 | 49 | 24 min 30 s |

On Redline a galaxy has 99 systems: the short way round the ring, none is more than 49 systems away. Level 10 therefore covers your whole galaxy.

### Defense toughness against Warheads (no defender research)

| Defense | Toughness (shield + hull) | Warheads for one unit |
|---|---|---|
| Protective Dome | 20,000 | 2 |
| Plasma Ejector | 10,300 | 1 |
| Defensive Barrier | 4,000 | 1 |
| Magnetic Accelerator | 3,700 | 1 |
| Ion Battery | 1,300 | 1 |
| High-Energy Emitter | 900 | 1 |
| Photonic Cannon | 225 | 1 |
| Ballistic Projector | 220 | 1 |

"Warheads for one unit": Warheads landing, with no shooter research, needed to destroy a single unit.

## Common pitfalls

- **"Interception Missile" is not the "Interceptor"**: the missile and the combat ship have nothing in common. The game shows the missile as "Interceptors".
- **No missile across galaxies**: range only counts systems in your own galaxy.
- **The Dome goes first**: without a designated target, the toughest defense is hit first. Designate a target if you are after something else.
- **A salvo too weak goes past**: a single Warhead does not destroy a Dome with no research; its damage goes to the next defenses.
- **A salvo costs an attack slot**: it counts in the attack limit on the player, even if it destroys nothing.
- **End of new-player protection**: your first salvo ends it, just like a fleet attack.
- **Missiles do not defend against fleets**: only Interception Missiles help in defense, and only against Warheads.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Attack limit](/en/players/attack-limit)
- [Beginner protection](/en/players/beginner-protection)
- [Vacation mode](/en/players/vacation-mode)
- [Maintenance](/en/misc/maintenance)
