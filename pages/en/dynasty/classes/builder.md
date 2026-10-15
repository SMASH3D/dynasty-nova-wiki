---
wiki_id: 168
locale: "en"
path: "dynasty/classes/builder"
url: "https://wiki.dynastynova.com/en/dynasty/classes/builder"
title: "The Builder"
description: "The Builder's class tree: Lode, Yard, Foundry."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:13.759Z"
updated: "2026-10-07T22:08:03.388Z"
---

# The Builder

> **In short**: the Builder is the class of the construction economy. Its mines pay more than their level, its yard moves forward while its queues are empty, and every level it already knows costs it less. Lode makes the mines produce; Yard banks lost time; Foundry cuts prices and protects what waits in the queue.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Builder is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Lode, Yard and Foundry.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic bonuses (mine production, construction speed, storage, Plasma Technology) come from the [common tree](/en/dynasty/common-tree). The Builder only has **mechanics**, a 5% cost accent (Tight quote or Bulk buying) and a construction speed accent, Catch-up, limited to colonies catching up with the home planet.
5. The extra levels of Master shaft, Twin mines and Mother lode only apply to the three mines (Mineral Excavator, Crystal Extractor, Hydrogen Condenser) and only to their production: the mine still draws the energy of its real level. A mine gains at most 2 production levels: 1 from Master shaft or Twin mines, 1 from Mother lode.
6. First pour, Prospecting and Core sampling are computed on the **mine's own production**: at its production level (extra levels included), its operating rate and the universe speed, without Plasma Technology or any other percentage bonus. Prospecting and Core sampling add to the planet's production and, like it, suffer from an energy shortfall; the First pour payout does not.
7. "Once a day" means 24 h after the last use, for your whole empire (Core sampling, All-out push). State order comes back 7 days after the designated order is paid.

## Worked example

Universe at speed 1. A Mineral Excavator produces 30 × N × 1.1^N metal per hour and draws 10 × N × 1.1^N energy: 4,036 metal and 1,345 energy at level 20, 4,662 metal and 1,554 energy at level 21.

**Full Lode on the home planet (Master shaft and Mother lode)**
- The Excavator reaches level 21. It produces as a level 23 (21 + 1 + 1): 30 × 23 × 1.1^23 = **6,178 metal per hour**, for the energy of a level 21 (1,554).
- First pour and Great pours (9 h): 9 × 6,178 = **55,602 metal** paid when the level ends.
- Prospecting at rank 3 on this mine: 6,178 × 30% = 1,853 (rounded down) more per hour, that is **44,472 metal** over the 24 h, at full energy.
- Core sampling: 2 × 6,178 × 4 = **49,424 more metal** in 4 h, at full energy.

**Galleries and Twin mines, on a colony**
- With Galleries at rank 3, Mother lode applies from level 11. A level 11 Excavator produces as a level 13: **1,346 metal per hour** instead of 941, for the energy of a level 11 (313).

**Foundry: an already known level**
- Level 25 Excavator on a colony, a level the home planet already reached: 1,010,046 metal and 252,511 crystal at catalogue price.
- Known plans and Yard archives (25%) plus Tight quote (5%): 30% less, rounded up, that is **707,033 metal** and **176,758 crystal**.
- Designated for State order: half of this already reduced price, **353,517 metal** and **88,379 crystal**, 35% of the catalogue price. Points are still counted on the catalogue price.

**Yard: an 8 h night, empty building queue**
- With Head start plans at rank 3 (80%) and Automatic relay (5 h): 8 h × 80% = 6 h 24 min, brought down to the ceiling, that is **5 h** paid automatically to the order started in the morning.
- With Hour bank (8 h): **6 h 24 min** kept, to pay onto the running order of your choice.

**Nothing spills**
- The crystal storage is full and 10,000 crystal produced overflow. Metal is chosen and its storage has room: 10,000 × 1.5 × 50% = **7,500 metal**. Had crystal been the chosen resource, those 10,000 would be lost.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FOUNDRY<br/>Pay less, keep what you set aside."]:::head
        B3R1{{"Known plans<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Master stroke<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Tight quote<br/>1 pt"]:::option
        B3R3B["② Bulk buying<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Yard archives<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Down payment<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Yard credit<br/>1 pt"]:::option
        B3R6B["② Metal payment<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Yard vault<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Alliance plans<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ State order<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["YARD<br/>The yard that works while you sleep."]:::head
        B2R1{{"The yard never sleeps<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Night shifts<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Continuous pour<br/>1 pt"]:::option
        B2R3B["② Poured foundations<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Catch-up<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Night shipyard<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Hour bank<br/>1 pt"]:::option
        B2R6B["② Automatic relay<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Head start plans<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Shared head start<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ All-out push<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["LODE<br/>Mines that pay more than their level."]:::head
        B1R1{{"First pour<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Great pours<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Master shaft<br/>1 pt"]:::option
        B1R3B["② Twin mines<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Prospecting<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Mother lode<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Chosen lode<br/>1 pt"]:::option
        B1R6B["② Double lode<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Galleries<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Nothing spills<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Core sampling<br/>ultimate"]]:::ultimate
        B1R8 --- B1R9
    end
    classDef head fill:#111b2e,stroke:#2a3852,color:#e6ecf7,stroke-width:1px;
    classDef key fill:#1c1606,stroke:#f5c542,color:#fde9a8,stroke-width:2px;
    classDef rank fill:#0e1a30,stroke:#4f8cff,color:#e6ecf7,stroke-width:2px;
    classDef option fill:#101827,stroke:#46546e,color:#cfd8e6,stroke-width:1px;
    classDef gate fill:#241b06,stroke:#c99a2e,color:#f5c542,stroke-width:1px;
    classDef ultimate fill:#1a1630,stroke:#e2c068,color:#fff6d8,stroke-width:3px;
    linkStyle default stroke:#33415c,stroke-width:2px,fill:none;
    style B1 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
    style B2 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
    style B3 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
```

### Lode

*Mines that pay more than their level.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **First pour** | key | When one of your mines gains a level, it pays you 3 h of its new production at once. |  |
| 2 | **Great pours** | 3 ranks | A mine that gains a level pays you 6 h more of its new production. | 3 × 2 h |
| 3 | **A · Master shaft** | choice | Your home planet's mines produce as if they were 1 level higher. | |
|  | **B · Twin mines** |  | Your colonies' mines produce as if they were 1 level higher. | |
| 4 | **Prospecting** | 3 ranks | Every day, one of your mines drawn at random produces 30% more for 24 h. | 3 × 10% |
| 5 | **Mother lode** | key | From level 20, each of your mines produces as if it were 1 level higher, on top of Master shaft or Twin mines. |  |
| 6 | **A · Chosen lode** | choice | Every day, you pick the Prospecting mine instead of the draw. | |
|  | **B · Double lode** |  | Every day, 2 mines are drawn for Prospecting instead of one. | |
| 7 | **Galleries** | 3 ranks | Mother lode applies 9 levels earlier. | 3 × 3 |
| 8 | **Nothing spills** | key | When a storage is full, 50 pts of the value of the overflowing production is converted into the resource of your choice, at equal value: three metal are worth two crystal or one hydrogen. |  |
| 9 | **Core sampling** | ultimate | Once a day, the mine of your choice produces three times as much for 4 h. You pick the mine and the moment. |  |

- **First pour**: every completed level of a mine pays its hours of production, including the level granted by Master stroke. The payout goes straight into the planet's stock.
- **Master shaft** applies to the home planet, **Twin mines** to every colony, from the mine's level 1.
- **Prospecting**: the draw is made among all standing mines of all your planets (not moons), each with the same chance whatever its level. A new mine of the day is drawn shortly after the 24 h end.
- **Mother lode** triggers on the mine's real level (20, or 11 with Galleries at rank 3), not its production level.
- **Chosen lode**: your choice replaces the drawn mine and lasts 24 h; you choose again when those 24 h end. Without a choice, the draw goes on. **Double lode** draws two different mines.
- **Nothing spills**: only the overflow of the two other resources is converted, at equal value, rounded down, and only into the free space of the chosen resource's storage (metal as long as you have chosen nothing). The choice is made planet by planet. It only applies to production, and after Safety Stock (common tree).
- **Core sampling**: the Mineral Excavator, Crystal Extractor or Hydrogen Condenser, at the time you choose.

### Yard

*The yard that works while you sleep.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **The yard never sleeps** | key | When a planet's building queue is empty, the yard sets aside a head start of 50% of the time passed, up to 1 h: the next order takes that much less. |  |
| 2 | **Night shifts** | 3 ranks | Your yard can set aside 3 h more head start. | 3 × 1 h |
| 3 | **A · Continuous pour** | choice | An order that starts on its own after the previous one begins with 10% of its time already done. | |
|  | **B · Poured foundations** |  | An order you start by hand begins with 5% of its duration already done, 30 min at least, at most 50%. | |
| 4 | **Catch-up** | 3 ranks | On a colony, a building still below your home planet's level builds 15% faster. | 3 × 5% |
| 5 | **Night shipyard** | key | Your idle shipyard sets head start aside too, and it can shorten your ships and defenses. |  |
| 6 | **A · Hour bank** | choice | Head start is no longer paid on its own: you keep it, up to 8 h, and pay it into the order of your choice. | |
|  | **B · Automatic relay** |  | Head start is still paid into the next order, and you can set aside 1 h more. | |
| 7 | **Head start plans** | 3 ranks | Your yard sets aside 30% more of its idle time. | 3 × 10% |
| 8 | **Shared head start** | key | A planet's head start can be paid into an order on any other of your planets, at most 50% of that order. |  |
| 9 | **All-out push** | ultimate | Once a day, the yard of the planet of your choice works twice as fast for 4 h. |  |

- **The yard never sleeps**: the head start is banked planet by planet, while its building queue is empty. It is paid automatically to the next construction or demolition started on that empty queue, and the **whole** head start goes, even if the order is shorter than it.
- **Continuous pour** only applies to a queued order that starts on its own. **Poured foundations** only applies to an order started on an empty queue: 30 min, or 5% of its duration if that is more, never past half its duration.
- **Catch-up** also applies to the level equal to the home planet's. It adds to the common tree's construction speed; a duration is divided by (1 + speed).
- **Night shipyard**: the planet has a single bank, which fills while at least one of its two yards (buildings, Orbital Dock) is empty, at the same rate. A ship or defense order started on an empty Orbital Dock only takes its own duration from it.
- **Hour bank**: the ceiling becomes 8 h instead of 5 h (Night shifts no longer adds anything). You pay the head start onto a running order of the planet (ships and defenses with Night shipyard), at most what it has left.
- **Shared head start**: paying another planet is done by hand, also with Automatic relay; all contributions from other planets together never exceed 50% of the order's duration.
- **All-out push** only affects the building yard. The running order gains up to 4 h at once (at most half of what it has left); an order starting during the window gains the same way on what is left of the window.

### Foundry

*Pay less, keep what you set aside.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Known plans** | key | A building level you already reached on another of your planets costs 10% less. |  |
| 2 | **Master stroke** | 3 ranks | Each finished building has a 6% chance to reach the next level too, for free. | 3 × 2% |
| 3 | **A · Tight quote** | choice | Your buildings cost 5% less. | |
|  | **B · Bulk buying** |  | Your ships and defenses cost 5% less. | |
| 4 | **Yard archives** | 3 ranks | Levels you already know cost another 15% less. | 3 × 5% |
| 5 | **Down payment** | key | The resources set aside for the order at the head of your building queue are safe from looting, up to 30% of its cost. |  |
| 6 | **A · Yard credit** | choice | An order starts even when up to 10% of its resources are missing; the rest is taken from your production. | |
|  | **B · Metal payment** |  | The crystal or hydrogen an order lacks is paid in metal: 2 metal per missing unit. | |
| 7 | **Yard vault** | 3 ranks | Down payment shelters another 30% of the order's cost. | 3 × 10% |
| 8 | **Alliance plans** | key | A level a member of your alliance already reached counts as known for Known plans. |  |
| 9 | **State order** | ultimate | Once a week, the upgrade of your choice costs 50% less. |  |

- **Known plans**: the level must be reached on **another** of your planets or moons. Building reductions add up (Known plans, Yard archives, Tight quote: 30% at most); the price is rounded up.
- **Master stroke**: only after an upgrade (not a demolition), and if the next level is possible (maximum level, free field).
- **Down payment**: the protected order is the first order **waiting** in the planet's queue, not the running one (already paid), nor a demolition. The sheltered share, at most the stock, is removed from what can be plundered; the plunder rate then applies to the rest.
- **Yard credit**: you need at least 90% of **each** resource. The whole available stock goes, the shortfall becomes a debt taken from the stock as soon as it fills, before any other spending. No new credit while a debt runs. **Metal payment** pays missing crystal and hydrogen in metal, if there is enough metal. Both only apply to buildings.
- **State order**: you designate on a planet the next level of a building; the price drops as soon as it is designated, and you can change it until the order is paid. The discount applies to the price already reduced by the other talents.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| The home planet's mines produce as if they had +1 level | 1 |
| The colonies' mines produce as if they had +1 level | 1 |
| Every mine produces as if it had +1 level | 1 |
| Mother lode applies 9 levels earlier | 9 |
| +15% build speed on a colony level the home planet already has | 15% |
| −25% cost of a building level already reached on another of your planets | 25% |
| −5% building resource cost | 5% |
| −5% ship and defense cost | 5% |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Miner | Lode 15 · Foundry 10 | Core sampling, Mother lode from level 11, 9 h of production at every mine level, Prospecting at 30% on one chosen mine or two drawn, Nothing spills; known levels −25% (−30% with Tight quote), Master stroke 6%, Down payment 30% |
| Absent Foreman | Yard 15 · Lode 10 | bank of 80% of idle time, 5 h (Automatic relay) or 8 h (Hour bank) per planet, Orbital Dock included, Catch-up 15%, Shared head start, All-out push; 9 h of production at every mine level, Prospecting 30%, Mother lode from level 20 |
| Colonizer | Foundry 15 · Yard 10 | State order, Alliance plans, Down payment up to 60%, known levels −25%; bank of 50% of idle time up to 5 h or 8 h, Catch-up 15% on colonies, Night shipyard |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **The Yard rewards empty queues**: the head start is only paid automatically to an order started on an empty queue. A player who keeps their queue full mostly benefits from Continuous pour and All-out push.
- **A head start longer than the order is lost**: starting a 10 min building with 5 h banked uses up the 5 h. With Hour bank, pay it by hand onto a big order.
- **First pour, Prospecting and Core sampling ignore Plasma Technology**: they apply to the mine's own production. An energy shortfall also reduces Prospecting and Core sampling.
- **Extra production levels cost no energy**: the mine draws that of its real level.
- **Nothing spills does not save the chosen resource**: its own overflow is lost, and nothing is converted when its storage is full.
- **Known plans only covers a level already reached** on another of your planets (or by a member of your alliance with Alliance plans): your most advanced planet pays full price.
- **Down payment protects the waiting order**: keep an order queued behind the running one. At most 60% of its cost, never more than the stock; the raider takes their rate on the rest.
- **Cost reductions do not change points**: points and experience are computed on the catalogue price.

## Related pages

- [Talents](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Resources](/en/economy/resources)
- [Build queues](/en/economy/build-queue)
- [Plunder](/en/combat/plunder)
