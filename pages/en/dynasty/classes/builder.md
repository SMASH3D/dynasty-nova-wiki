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
updated: "2026-10-06T10:30:15.017Z"
---

# The Builder

> **In short**: the Builder is the class whose mines pay more than their level, whose yard works while they sleep, and who pays less for each level, above all when catching up on colonies. Common to every dynasty. Its three branches: **Lode**, **Yard** and **Foundry**.
{.is-info}

*"What stands."* Mine and yard: produce more, build faster, waste less.

## Rules

1. The Builder's tree follows the rules of every [class tree](/en/dynasty/talents): 3 branches of 9 rows, 15 points per branch, 25 points at most.
2. The generic bonuses (mine production, construction speed, storage, Plasma Technology) come from the [common tree](/en/dynasty/common-tree), Prosperity branch. The Builder only has **mechanics**, and a single accent bonus: **cost**, either of buildings or of ships and defenses (5%).
3. **Catch-up** is its construction speed accent: it only applies on a colony, to a building still below the level reached on your home planet (15% at most).
4. A mine gains at most **1 extra production level** from Mother lode, and at most 1 more from Master shaft or Twin mines.
5. The whole tree serves only you, except **Down payment**: the one talent another player meets, when they loot the planet.

## Worked example

A planet with a Mineral Excavator at level 20 (4,036 metal per hour; 4,662 at level 21, at full energy).

- **First pour + Great pours** (9 h): the Excavator reaches level 21 and pays out 9 × 4,662 = **41,958 metal** at once.
- **Mother lode** (from level 20): the level 20 Excavator produces as a level 21, so **4,662 instead of 4,036** per hour (+15%).
- **Prospecting** at rank 3 (+30%) on the level 21 Excavator: 4,662 × 1.3 = **6,061 per hour** for 24 h, about 33,600 more metal over the day.
- **Core sampling** (triple production for 4 h) on the same Excavator: 2 × 4,662 × 4 = **37,296 more metal**.
- **Known plans + Yard archives** (−25%): raising a colony's Excavator from level 13 to 14 when the home planet already reached 14 costs about **8,758 metal and 2,189 crystal** instead of 11,677 and 2,919.

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

### Lode: "Mines that pay more than their level."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **First pour** | When a mine gains a level, it pays out part of its new production at once. | 3 h |
| 2 | 3 ranks | **Great pours** | A mine that gains a level pays out more of its new production. | +2 h per rank (9 h in total) |
| 3 | choice | **A: Master shaft** / **B: Twin mines** | A: your home planet's mines produce as if they were 1 level higher. <br> B: your colonies' mines produce as if they were 1 level higher. | +1 level |
| 4 | 3 ranks | **Prospecting** | Every day, a mine drawn at random produces more for 24 h. | +10% per rank (30%) |
| 5 | key | **Mother lode** | From level 20, each mine produces as if it were 1 level higher, on top of Master shaft or Twin mines. | +1 level from level 20 |
| 6 | choice | **A: Chosen lode** / **B: Double lode** | A: you pick the Prospecting mine every day. <br> B: two mines are drawn every day instead of one. | choice / 2 mines |
| 7 | 3 ranks | **Galleries** | Mother lode applies earlier. | −3 levels per rank (from level 11) |
| 8 | key | **Nothing spills** | When a storage is full, the overflowing production is converted, unit for unit, into the resource of your choice. | 50% |
| 9 | ultimate | **Core sampling** | Once a day, the mine of your choice produces three times as much for 4 h. You pick the mine and the moment. | ×3 for 4 h |

### Yard: "The yard that works while you sleep."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **The yard never sleeps** | When a planet's building queue is empty, the yard sets aside a head start equal to part of the time passed; the next order takes that much less. | 50% of the time, up to 1 h |
| 2 | 3 ranks | **Night shifts** | The yard can set aside more head start. | +1 h per rank (4 h) |
| 3 | choice | **A: Continuous pour** / **B: Poured foundations** | A: an order that starts on its own after the previous one begins with part of its time already done. <br> B: an order started by hand begins with 30 min already done, at most half of its duration. | 10% / 30 min |
| 4 | 3 ranks | **Catch-up** | On a colony, a building still below your home planet's level builds faster (accent). | +5% per rank (15%) |
| 5 | key | **Night shipyard** | An idle Orbital Dock sets head start aside too, and it shortens your ships and defenses. | unlock |
| 6 | choice | **A: Hour bank** / **B: Automatic relay** | A: head start is no longer paid on its own; you keep it and pay it into the order of your choice. <br> B: head start is still paid on its own, and its cap rises. | up to 8 h / +1 h (5 h) |
| 7 | 3 ranks | **Head start plans** | The yard sets aside a larger share of its idle time. | +10% per rank (80%) |
| 8 | key | **Shared head start** | A planet's head start can be paid into an order on any other of your planets. | at most 50% of the order |
| 9 | ultimate | **All-out push** | Once a day, the yard of the planet of your choice works twice as fast for 4 h. | ×2 for 4 h |

### Foundry: "Pay less, keep what you set aside."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Known plans** | A building level already reached on another of your planets costs less. | −10% |
| 2 | 3 ranks | **Master stroke** | Each finished building has a chance to reach the next level too, for free. | 2% per rank (6%) |
| 3 | choice | **A: Tight quote** / **B: Bulk buying** | A: your buildings cost less. <br> B: your ships and defenses cost less. | −5% (accent) |
| 4 | 3 ranks | **Yard archives** | Known levels cost even less. | −5% per rank (−25% with Known plans) |
| 5 | key | **Down payment** | The resources set aside for the order at the head of the building queue are safe from looting, up to part of its cost. | 30% |
| 6 | choice | **A: Yard credit** / **B: Metal payment** | A: an order starts even when part of its resources is missing; the rest is taken from your production. <br> B: missing crystal or hydrogen is paid in metal. | 10% / 2 metal per unit |
| 7 | 3 ranks | **Yard vault** | Down payment shelters a larger share of the cost. | +10% per rank (60%) |
| 8 | key | **Alliance plans** | A level a member of your alliance already reached counts as known for Known plans. | unlock |
| 9 | ultimate | **State order** | Once a week, the upgrade of your choice costs half price. | −50%, once a week |

### What 25 points give

| Build | Split | What it gets |
|---|---|---|
| Miner | Lode 15 · Foundry 10 | Core sampling, Mother lode from level 11, a mine at +30% every day, 9 h of production at each level; colonies caught up at −25%, Master stroke, Down payment |
| Absent foreman | Yard 15 · Lode 10 | the yard catches up 5 to 8 h a night per planet, shared head start, All-out push; Mother lode, Prospecting, 9 h of production at each level |
| Colonizer | Foundry 15 · Yard 10 | State order every week, Alliance plans, −25% costs on every catch-up; yard head start and Catch-up on colonies |

## Common pitfalls

- **The Yard rewards empty queues**: a player who keeps their queues full gets little from it. Continuous pour and All-out push are there for them.
- **Known plans only covers a level already reached** on another of your planets (or by an ally with Alliance plans): your most advanced planet pays full price.
- **Down payment only covers the order at the head of the queue**, and 60% of its cost at most: a raider still takes the rest of the stock.
- **Cost reductions do not change points**: points and experience are computed on the catalogue cost, before any reduction.

## Related pages

- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Resources](/en/economy/resources)
- [Build queues](/en/economy/build-queue)
