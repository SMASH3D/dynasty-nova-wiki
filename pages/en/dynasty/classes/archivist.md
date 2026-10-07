---
wiki_id: 167
locale: "en"
path: "dynasty/classes/archivist"
url: "https://wiki.dynastynova.com/en/dynasty/classes/archivist"
title: "The Archivist"
description: "The Archivist's class tree: Memory, Wreck, Registry."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:11.381Z"
updated: "2026-10-06T10:30:12.908Z"
---

# The Archivist

> **In short**: "Nothing is lost". The Archivist recovers what others leave behind: knowledge others have already found (**Memory**), the wrecks of other people's battles (**Wreck**), and its own fleet when it falls (**Registry**). A class exclusive to [The Heritage](/en/dynasty/dynasties).
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Archivist is **exclusive to The Heritage**: only players of that dynasty can take it.
2. Its tree has **3 branches of 9 rows** (15 points per branch). Points, gates and ultimates follow the rules of every class tree: see [Talent system](/en/dynasty/talents).
3. **Known level**: a research level already held by **25%** of the universe's active players. The whole Memory branch only applies to these levels.
4. **Debris harvests**: the Archivist's bonus is paid when the Salvagers come home. It takes no hold space and takes nothing more from the debris field.
5. **Loss registry**: the registry keeps the list of ships lost in combat for **7 days**. Everything on it is rebuilt on better terms, up to the quantities lost. It covers ships only, not defenses.
6. The registry's rebuild speed **adds up** with the ships' build speed (the common tree's Workshops, the alliance). A duration is divided by (1 + sum of the bonuses).
7. The class's only **accent** is the speed of recycling missions (Wreck Race), see [Talent system](/en/dynasty/talents).
8. The dock, recycling during combat and hydrogen from debris belong to the Admiral; defenses to the Veteran.

## Worked example

**Memory**: Weapon Systems 10 (409,600 metal, 102,400 crystal), universe research speed ×1, Innovation Center 10: **46 h 32 min** without talents. The level is known.
- Known Levels (+10%): **42 h 18 min**.
- With Archive Holdings at rank 3 (+25% in total): **37 h 14 min**.
- Rediscovery at rank 3 (−12%): **360,448** metal and **90,112** crystal.
- Momentum: Weapon Systems 11 (93 h 05 min at the same Center), if known, starts with 10% of its time done, **9 h 18 min**; with Headway at rank 3 (25%), **23 h 16 min**.

**Wreck**: a debris field of 400,000 resources.
- Scrapper (+10%): **440,000** brought home.
- With Metal Sorting at rank 3 (+25% in total): **500,000**. The field still loses 400,000 resources, no more.

**Registry**: 200 Corvettes lost, i.e. 4,000,000 metal, 1,400,000 crystal and 400,000 hydrogen (5,800,000 resources).
- Indemnity: 5% of their value, **290,000** resources paid at once; **464,000** with War Chest at rank 3 (8%).
- Kept Blueprints at rank 3 (−12%): 4,000,000 → **3,520,000** metal; with War Discount (−20% in total), **3,200,000**.
- A rebuild that takes 10 h without talents: **8 h 41 min** with Loss Registry (+15%), **7 h 41 min** with Relief Lines at rank 3 (+30%), **6 h 40 min** with Back to the Front (+50%). With Swift Relief as well, during the 24 h after the loss (+70%): **5 h 53 min**.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["REGISTRY<br/>Getting up faster than you fall."]:::head
        B3R1{{"Loss Registry<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Kept Blueprints<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Swift Relief<br/>1 pt"]:::option
        B3R3B["② Long Memory<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Relief Lines<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Indemnity<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Back to the Front<br/>1 pt"]:::option
        B3R6B["② War Discount<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("War Chest<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Lessons of Defeat<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Relief Yard<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["WRECK<br/>First to reach what drifts."]:::head
        B2R1{{"Scrapper<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Wreck Radar<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Scavenger<br/>1 pt"]:::option
        B2R3B["② Wreck Race<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Metal Sorting<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Wreck Alert<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Salvage Garrison<br/>1 pt"]:::option
        B2R6B["② Fresh Wrecks<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("On-Call Crew<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Sweep-All<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Seals<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["MEMORY<br/>What others have already found."]:::head
        B1R1{{"Known Levels<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Rediscovery<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Alliance Library<br/>1 pt"]:::option
        B1R3B["② Public Library<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Archive Holdings<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Momentum<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Catching Up<br/>1 pt"]:::option
        B1R6B["② Neck and Neck<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Headway<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Working Memory<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Universal Library<br/>ultimate"]]:::ultimate
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

Row types: *key* (1 point), *3 ranks*, *choice* (one point, option A or B), *ultimate*.

### Memory: "What others have already found."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Known Levels** | A research level already held by 25% of the universe's active players is known: you study it faster, and the Innovation Center flags it. | +10% |
| 2 | 3 ranks | **Rediscovery** | Your known levels cost less. | −4% per rank (−12%) |
| 3 | choice | **A: Alliance Library** | A level a member of your alliance holds counts as known. | unlock |
| | | **B: Public Library** | A level is known as soon as 10% of the active players hold it. | 10% |
| 4 | 3 ranks | **Archive Holdings** | Your known levels are studied faster still. | +5% per rank (+25% in total) |
| 5 | key | **Momentum** | When you complete a known level, the next level of the same research, if known, starts with part of its time already done. | 10% |
| 6 | choice | **A: Catching Up** | On a research where you are 5 levels or more behind the most common level, Archive Holdings counts double: 10 + 15 × 2 = +40% on a known level. | ×2 |
| | | **B: Neck and Neck** | Any level the player ranked just above you holds counts as known. | unlock |
| 7 | 3 ranks | **Headway** | Momentum gives the next level more head start. | +5% per rank (25%) |
| 8 | key | **Working Memory** | A known level starts without the Innovation Center level it requires: the other requirements are enough. | unlock |
| 9 | ultimate | **Universal Library** | A level counts as known as soon as a single player of the universe holds it. Only the first to reach it gains nothing on that research. | unlock |

### Wreck: "First to reach what drifts."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Scrapper** | Your debris harvests yield more. The bonus is paid on the way home, takes no hold space and empties the field no further. | +10% |
| 2 | 3 ranks | **Wreck Radar** | Debris fields show on your map around your planets, even on positions never explored. | 5 systems per rank (15) |
| 3 | choice | **A: Scavenger** | You recycle a field without having scouted its position: you leave as soon as you see it. | unlock |
| | | **B: Wreck Race** | Your recycling missions fly faster (accent). | +10% |
| 4 | 3 ranks | **Metal Sorting** | Your debris harvests yield more still. | +5% per rank (+25% in total) |
| 5 | key | **Wreck Alert** | You are warned as soon as a field of more than 50,000 resources appears within your radar's range. | 50,000 |
| 6 | choice | **A: Salvage Garrison** | When one of your planets is attacked, its docked Salvagers harvest the field as soon as the battle ends, before the attacker's. | unlock |
| | | **B: Fresh Wrecks** | On a field that appeared less than 1 h ago, your harvests yield 20 points more, on top of Scrapper and Metal Sorting. Like them, the bonus is created on the way home: it does not empty the field further (25% → 45% with the full branch). | +20 points |
| 7 | 3 ranks | **On-Call Crew** | When the alert rings, your Salvagers leave on their own from the nearest planet, even while you sleep. | 1 departure a day per rank (3) |
| 8 | key | **Sweep-All** | In the same flight, your Salvagers also harvest the fields of the neighbouring positions (±1 in the same system), as far as their holds allow. | ±1 position |
| 9 | ultimate | **Seals** | Once every 24 h, you seal a field you can see: for 1 h, other players no longer see it nor send Salvagers to it. Those already flying arrive as usual. | 1 h |

### Registry: "Getting up faster than you fall."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Loss Registry** | The registry keeps the ships you lose in combat for 7 days: they are rebuilt faster, up to the quantities lost. | +15% |
| 2 | 3 ranks | **Kept Blueprints** | Registry ships cost less. | −4% per rank (−12%) |
| 3 | choice | **A: Swift Relief** | For 24 h after a loss, the registry rebuilds faster still. | +20% |
| | | **B: Long Memory** | The registry keeps your losses for 21 days instead of 7. | 21 days |
| 4 | 3 ranks | **Relief Lines** | Registry ships are rebuilt faster still. | +5% per rank (+30% in total) |
| 5 | key | **Indemnity** | After a battle in which you lose ships, part of their cost is paid at once to the planet they left from, resource by resource. | 5% |
| 6 | choice | **A: Back to the Front** | Registry ships are rebuilt faster still. | +20% (+50% in total) |
| | | **B: War Discount** | Registry ships cost less still. | −8% (−20% in total) |
| 7 | 3 ranks | **War Chest** | Indemnity pays more of the value lost. | +1 point per rank (8%) |
| 8 | key | **Lessons of Defeat** | After a battle in which you lose more than you destroy, your Weapon Systems, Shielding Technology and Armor Technology research runs faster for 24 h. | +20% |
| 9 | ultimate | **Relief Yard** | The registry rebuilds on a second Orbital Dock line, alongside your normal one. | 2nd line |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| The catch-up | Memory 15 · Registry 10 | Universal Library; known levels +25% faster and −12%; 25% head start on each chained level; registry +30% and Indemnity 5%. |
| The scavenger | Wreck 15 · Memory 10 | Seals, alert, automatic departures, neighbouring fields; harvests +25%; known levels +25%. |
| The unbreakable | Registry 15 · Wreck 10 | Relief Yard, Indemnity 8%, Lessons of Defeat; harvests +25%, radar at 15 systems, Salvage Garrison. |

## Common pitfalls

- **A known level is judged on the universe's active players**, not on every account.
- **The first on a research gets nothing from Memory** on that research: nobody is ahead of them.
- **The harvest bonus does not empty the field any further**: other players can still harvest what is left.
- **The registry only covers ships lost in combat**, up to the quantities lost and for 7 days (21 with Long Memory). Defenses are not on it.
- **Swift Relief only lasts 24 h** after each loss.

## Related pages

- [Dynasties](/en/dynasty/dynasties)
- [Classes](/en/dynasty/classes)
- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Debris fields](/en/combat/debris)
- [Technology list](/en/research/technologies)
