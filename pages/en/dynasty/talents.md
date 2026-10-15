---
wiki_id: 165
locale: "en"
path: "dynasty/talents"
url: "https://wiki.dynastynova.com/en/dynasty/talents"
title: "Talents"
description: "The two trees, points, gates, the draft, resets and caps."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:06.594Z"
updated: "2026-10-06T10:30:07.976Z"
---

# Talents

> **In short**: you have two trees. The **common tree** gets 1 point per level, 50 at most, and carries the generic bonuses. The **class tree** gets 1 point per 2 mastery levels, 25 at most, and carries your class's mechanics. You prepare your choices as a draft, then you confirm. A confirmed point only comes back through a reset.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

### Two trees, two pools
1. The **common tree**: 3 branches of 10 rows, 28 points per branch. It gets **1 point per level** of your character, **50 at most**.
2. The **class tree**: 3 branches of 9 rows, 15 points per branch. It gets **1 point per 2 mastery levels** of your class, rounded up, **25 at most**. See [Class mastery](/en/dynasty/classes#class-mastery).
3. The two pools are **separate**: a common point never goes into the class tree, and the other way round.

### Nodes and rows
4. Each row of a branch holds one node. Four kinds of nodes:
   - **ranked**: each point adds a rank (3 ranks in the class tree, 3 or 5 in the common tree);
   - **choice**: a single point, two options **A** and **B**, only one at a time;
   - **key**: a single point, a mechanic;
   - **ultimate**: the last row of each branch, a single point.
5. A node only opens once the **node above it is full** (for a choice: an option taken). A branch therefore fills from top to bottom.
6. Each tree has three ultimates, and your budget only allows **one**.

### Gates
7. A row opens when the rows **above it** hold enough points, **every branch together**.

| Tree | Gates (points placed above the row, every branch together) | Ultimate |
|---|---|---|
| Common | rows 1 to 3: open; rows 4 to 6: 8 points; rows 7 and 8: 20 points; rows 9 and 10: 32 points | level 40 and full branch above |
| Class | rows 1 to 3: open; rows 4 to 6: 5 points; rows 7 to 9: 12 points | full branch above, no level requirement |

8. An **ultimate** also requires **every node above it in its branch** to be full. In the common tree, it also requires **level 40**. In the class tree there is no level requirement: a full branch is enough, that is 15 class points, reached at mastery 29.

### Draft and confirmation
9. You place and remove your points freely as a **draft**. Nothing applies until you click **Confirm**.
10. A confirmed point is **final**: it only comes back through a reset. A confirmed choice option cannot be changed either.

### Reset
11. Each tree is reset **separately** and gives back all its points at once.
12. The **first** reset of each tree is **free**. The next ones cost **20 Stellar Points** and require **24 hours** since the previous reset of the same tree.
13. It is impossible while an **enemy fleet** is heading for one of your planets, and while one of your **attack fleets** is on its way to its target (the way back blocks nothing). An empty tree has nothing to reset: nothing is charged.
14. A [class change](/en/dynasty/classes#changing-class) empties the class tree and makes its next reset free. The common tree does not move.

### Caps
15. Each bonus has a **talent cap** (both trees together) and a **total cap**, alliance talents included. A point that would go past a cap adds nothing.
16. Your dynasty's trait adds **past** the talent cap, then the alliance; the total cap stays the same for everyone.
17. A class may strengthen a common bonus, but only on a **narrow scope** (a family of missions, ships or buildings). This is an **accent**, with its own cap.
18. Fleet speed bonuses (talents and alliance) **divide the flight duration**: +50% speed = a flight 1.5 times shorter. See [Movement](/en/fleet/movement).

## Worked example

**At level 20, with a class played from the start**
- Common tree: **20 points**. Rows 7 and 8 open as soon as 20 points are placed above them.
- Class tree: mastery 20, that is **10 points**. Rows 4 to 6 are open, rows 7 to 9 wait for 12 points placed above.

**A full common branch**
- It costs 28 points. Its rows 1 to 8 hold 22, but row 9 requires 32 points above it: you must have placed **10 elsewhere** before finishing it.
- At level 50, 22 points remain for a second branch, enough to reach its row 8, without its ultimate.
- In the class tree, rows 1 to 8 of a branch hold 14 points: the 12-point gate opens without placing anything elsewhere. With 25 points, 10 remain for a second branch, down to its row 6 (10 points).

**A reset**
- First reset of the common tree: free.
- Second one, the next day: 20 Stellar Points, possible 24 hours after the first.

## Detailed data

### Points per level

Experience comes from quests and from your points record: **10 experience points per [ranking](/en/players/rankings) point** gained above your best total. Losing points takes no experience away.

> **Universe setting**: the experience per ranking point is divided by the universe's economy speed.
> Default: **×1, 10 per point** · Redline: **×1, 10 per point**
{.is-info}

| Level | Total experience | Common points | Class points (equal mastery) | What opens |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | common and class, rows 1 to 3 |
| 8 | 500 | 8 | 4 | common, rows 4 to 6 |
| 9 | 782 | 9 | 5 | class, rows 4 to 6 |
| 20 | 43,939 | 20 | 10 | common, rows 7 and 8 |
| 23 | 82,453 | 23 | 12 | class, rows 7 to 9 |
| 29 | 255,374 | 29 | 15 | class ultimate (full branch) |
| 32 | 437,052 | 32 | 16 | common, rows 9 and 10 |
| 40 | 1,773,675 | 40 | 20 | common ultimate (with the full branch) |
| 50 | 10,000,000 | 50 | 25 | the whole budget |

Past level 50, experience keeps counting, each level costing as much as level 50, but no longer gives any point.

### Caps of the shared bonuses

| Bonus | Common tree | Class accent | Talent cap | Total cap (with the alliance) |
|---|---|---|---|---|
| Fleet speed | 40% | +10% on a mission family: attacks, espionage and moon destruction (Admiral), peaceful missions or missions to an abandoned target (Navigator), recycling (Admiral, Archivist), prepared strike (Oracle, 9%) | 50% | 60% |
| Hydrogen burned | −20% | −10% on combat ships (Admiral) | −30% | −45% |
| Cargo capacity | 25% |  | 25% | 25% (no alliance share) |
| Fleets in flight | +2 | +1 reserved for attacks (Admiral) | +3 | +3 |
| Research speed | 15% (25% on two studies with Astrometry, within the same cap) |  | 25% | 45% |
| Mine production | 25% |  | 25% (+2% from The Halden Rotation on top) | 45% |
| Colony production (home planet and moons excluded) | 10% |  | 10% | outside the cap, on top of the 45% |
| Young colony: mines, buildings | 25%, 20% |  | 25%, 20% | outside the cap |
| Effect of the Plasma research | +50% |  | +50% |  |
| Energy from power plants and satellites | +8% |  | +15% |  |
| Expeditions: gains, exploration time | +20%, −25% |  | +20%, −25% |  |
| Storage capacity | 20% |  | 20% | 40% |
| Building speed | 25% | +15% at most on a family: colony catch-up (Builder), power plants (Energetician, 10%), innovation centers (Theorist, 9%), fallow planet (Symbiote, 10%) | 25% (40% on the family) | 45% (50% on the family) |
| Ship and defence build speed | 10% | +15% on a family: combat ships (Admiral), defences and missiles (Veteran), civil ships (Navigator) | 10% (25% on the family) | no alliance share |
| Building, ship and defence costs |  | −5% (Builder) | −5% |  |
| Planet fields | +2 | +2 (Symbiote) | +4 |  |
| Plunder of abandoned targets | +20 points |  | +20 points |  |
| Resources sheltered from plunder | 5 points | Veteran (Underground Shelter), Oracle (The Cache) | 15 points for the Veteran, 10 points for the Oracle, 5 points for the others, common tree included | plunder rate never below 30% |

The bonuses that only serve you, on your way home or between your own planets (Tailwind, Inner Lanes, Victorious Return, Flash Retreat), are **outside** the speed cap: they multiply the speed separately. The Ark, however, stays under the 60% total cap.

## Common pitfalls

- **Confirming too fast**: a confirmed point does not come back without a reset, and only the first one is free.
- **Aiming for two ultimates**: two full branches require 56 common points or 30 class points. The budget only allows one.
- **Waiting for level 40 for a class ultimate**: it only requires its full branch.
- **Resetting during a raid**: an incoming enemy fleet, or one of your attacks on its way, blocks the reset until impact.
- **Stacking a bonus past its cap**: extra points give nothing. Check the cap before adding an alliance talent on the same bonus.
- **Reading +50% speed as a flight twice as short**: speed divides the duration. +50% turns a 1 h flight into 40 min.

## Related pages

- [The classes](/en/dynasty/classes)
- [The common tree](/en/dynasty/common-tree)
- [Alliance missions and station](/en/players/alliance-missions)
- [Rankings and points](/en/players/rankings)
- [Movement](/en/fleet/movement)
