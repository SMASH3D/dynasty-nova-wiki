---
locale: "en"
path: "dynasty/experience"
url: "https://wiki.dynastynova.com/en/dynasty/experience"
title: "Experience and level"
description: "Where experience comes from, and how it raises your level and your class mastery."
tags: ["dynasty"]
published: true
---

# Experience and level

> **In short**: experience (XP) has **two sources**, and only two: the **quests** you claim, and your **points record** in the [rankings](/en/players/rankings), worth **10 XP per point**. Building, researching and producing ships or defenses raises your points, hence your XP. Combat, plunder and recycling give none directly. The same XP raises your **level** and your **class mastery**.
{.is-info}

> **Universe setting**: the XP earned per ranking point is divided by the universe's economy speed. Quest XP does not change.
> Default: **×1, 10 XP per point** · Redline: **×1, 10 XP per point**
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

### The two sources of XP

1. **Quests**: each claimed quest pays its XP, and each completed grade pays an XP bonus. The amounts are fixed, whatever the universe. See [The tutorial (quests)](/en/getting-started/tutorial-quests).
2. **Your points record**: whenever your points total goes past your best total, the difference earns you **10 XP per point**.
3. Your total XP is the sum of both.

$$\text{XP} = \text{XP}_{\text{quests}} + \left\lfloor \frac{10 \times R}{v} \right\rfloor$$

- $\text{XP}_{\text{quests}}$: the XP of the claimed quests and grades.
- $R$: your points record, that is the best points total you have reached in this universe.
- $v$: the universe's economy speed (1 on Redline).
- $\lfloor \cdot \rfloor$: rounded down.

### What raises your points, hence your XP

Reminder: an item is worth **1 point per 1,000 resources** of its catalogue cost (metal, crystal and hydrogen), even if a talent made you pay less. See [Rankings and points](/en/players/rankings).

4. Every finished **building level**, including a level granted by a talent.
5. Every finished **research level**.
6. Every **ship** and **defense** delivered by the shipyard, as the deliveries come in.
7. **Ships found on an expedition**: they count as if they had been built, as soon as they join your fleet.
8. **Taking over an abandoned planet**: whatever still stands there (buildings, ships, defenses) is added to your points.

### What earns no XP

9. **Combat**: winning a battle gives no XP. Plundered or recycled resources only give XP once you spend them on building.
10. **Resources** produced, plundered, recycled or found on an expedition: as long as they sit in your storage, they earn nothing.
11. **Alliance missions**: they raise the **alliance's** experience, a counter separate from yours.

### Losses and rebuilding

12. **XP is never lost.** Losing ships, firing missiles or demolishing a building lowers your points, not your XP.
13. **Rebuilding earns nothing until you pass your record.** Only the points earned beyond your best total count.

### Level

14. Your level depends only on your total XP (thresholds table in the [Detailed data](#detailed-data)).
15. Each level gives **1 point** in the common tree, **50 at most**. See [Talents](/en/dynasty/talents).
16. Past level 50, XP keeps counting and the level keeps rising, each level costing as much as the 50th (**1,585,249 XP**), but with no new talent point.
17. XP and level are **specific to each universe**.

### Class mastery

18. Mastery has **no source of its own**: it rises with the same XP as your level, along the same curve.
19. A class played since you joined the universe has its mastery **equal to your level**.
20. A class picked along the way starts from its own mastery (0 if you have never played it) and rises with the XP earned **since** you picked it.
21. Mastery **never goes above your level**, nor above 50.
22. Mastery gives the class tree points: **1 point per 2 mastery levels**, rounded up, **25 at most**. See [The classes](/en/dynasty/classes#class-mastery).

## Worked example

On Redline (speed ×1). You have claimed grade 1 of the tutorial (**100 XP**) and your record is **2,000 points**:
- Total XP: $100 + 10 \times 2{,}000 = 20{,}100$, that is **level 16**.

You build a Battleship (45,000 metal, 15,000 crystal, that is 60,000 resources):
- **+60 points**, record raised to 2,060: **+600 XP**, total 20,700.

It is destroyed in combat:
- **−60 points**, back to 2,000. Your XP stays at **20,700**.

You rebuild it:
- **+60 points**, back to 2,060: that is your record, not beyond. **+0 XP**.

You build a second one:
- **+60 points**, record raised to 2,120: **+600 XP**, total **21,300**. You reach **level 17** (threshold at 20,974).

The same Battleship, in a universe whose economy runs at ×2: **+300 XP**.

**Changing class.** At level 20 (43,939 XP), you switch to a class you have never played: mastery 0. You then earn 10,699 XP:
- your total reaches 54,638 XP: **level 21**;
- the new class has climbed 10,699 XP from the bottom of the curve: **mastery 14**, that is **7** class points.

## Detailed data

### Level thresholds

| Level | Total XP to reach it | XP to the next level | Common points | Class points (equal mastery) |
|---|---|---|---|---|
| 1 | 0 | 4 | 1 | 1 |
| 2 | 4 | 18 | 2 | 1 |
| 3 | 22 | 42 | 3 | 2 |
| 4 | 64 | 62 | 4 | 2 |
| 5 | 126 | 79 | 5 | 3 |
| 6 | 205 | 115 | 6 | 3 |
| 7 | 320 | 180 | 7 | 4 |
| 8 | 500 | 282 | 8 | 4 |
| 9 | 782 | 439 | 9 | 5 |
| 10 | 1,221 | 688 | 10 | 5 |
| 11 | 1,909 | 1,073 | 11 | 6 |
| 12 | 2,982 | 1,677 | 12 | 6 |
| 13 | 4,659 | 2,621 | 13 | 7 |
| 14 | 7,280 | 3,804 | 14 | 7 |
| 15 | 11,084 | 4,520 | 15 | 8 |
| 16 | 15,604 | 5,370 | 16 | 8 |
| 17 | 20,974 | 6,379 | 17 | 9 |
| 18 | 27,353 | 7,580 | 18 | 9 |
| 19 | 34,933 | 9,006 | 19 | 10 |
| 20 | 43,939 | 10,699 | 20 | 10 |
| 21 | 54,638 | 12,712 | 21 | 11 |
| 22 | 67,350 | 15,103 | 22 | 11 |
| 23 | 82,453 | 17,944 | 23 | 12 |
| 24 | 100,397 | 21,319 | 24 | 12 |
| 25 | 121,716 | 25,330 | 25 | 13 |
| 26 | 147,046 | 30,094 | 26 | 13 |
| 27 | 177,140 | 35,754 | 27 | 14 |
| 28 | 212,894 | 42,480 | 28 | 14 |
| 29 | 255,374 | 50,471 | 29 | 15 |
| 30 | 305,845 | 59,964 | 30 | 15 |
| 31 | 365,809 | 71,243 | 31 | 16 |
| 32 | 437,052 | 84,644 | 32 | 16 |
| 33 | 521,696 | 100,566 | 33 | 17 |
| 34 | 622,262 | 119,482 | 34 | 17 |
| 35 | 741,744 | 141,957 | 35 | 18 |
| 36 | 883,701 | 168,658 | 36 | 18 |
| 37 | 1,052,359 | 200,383 | 37 | 19 |
| 38 | 1,252,742 | 238,076 | 38 | 19 |
| 39 | 1,490,818 | 282,857 | 39 | 20 |
| 40 | 1,773,675 | 336,063 | 40 | 20 |
| 41 | 2,109,738 | 399,277 | 41 | 21 |
| 42 | 2,509,015 | 474,380 | 42 | 21 |
| 43 | 2,983,395 | 563,611 | 43 | 22 |
| 44 | 3,547,006 | 669,626 | 44 | 22 |
| 45 | 4,216,632 | 795,583 | 45 | 23 |
| 46 | 5,012,215 | 945,233 | 46 | 23 |
| 47 | 5,957,448 | 1,123,030 | 47 | 24 |
| 48 | 7,080,478 | 1,334,273 | 48 | 24 |
| 49 | 8,414,751 | 1,585,249 | 49 | 25 |
| 50 | 10,000,000 | 1,585,249 | 50 | 25 |

Past level 50: each level costs **1,585,249 XP** and no longer gives a point.

## Common pitfalls

- **Claim your quests**: a finished quest only pays its XP once claimed.
- **Hoarding does not level you up**: stockpiled, plundered or recycled resources only earn XP once invested.
- **Rebuilding after a defeat earns nothing**: you must first pass your former record. A lost fleet therefore delays your next "military" XP.
- **Demolishing takes no XP away**, but levels rebuilt afterwards earn nothing until you pass your record.
- **Switching class late**: the new class starts from its own mastery. Your common tree points do not move.
- **Each universe has its own XP**: playing in another universe does not raise your level here.

## Related pages

- [Talents](/en/dynasty/talents)
- [The classes](/en/dynasty/classes)
- [The tutorial (quests)](/en/getting-started/tutorial-quests)
- [Rankings and points](/en/players/rankings)
- [Expeditions](/en/fleet/expeditions)
