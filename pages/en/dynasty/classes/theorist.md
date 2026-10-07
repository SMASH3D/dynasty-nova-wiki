---
wiki_id: 174
locale: "en"
path: "dynasty/classes/theorist"
url: "https://wiki.dynastynova.com/en/dynasty/classes/theorist"
title: "The Theorist"
description: "The Theorist's class tree: Method, Network, Prototypes."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:27.452Z"
updated: "2026-10-06T10:30:28.918Z"
---

# The Theorist

> **In short**: "Understand first". The Theorist always has a study running and a level ahead. **Method** keeps the research queue from ever stopping, **Network** pools the Innovation Centers of the colonies, **Prototypes** lets you enjoy a research level before anyone else. A class open to every dynasty.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Theorist is a **common** class: every dynasty can take it.
2. Its tree has **3 branches of 9 rows** (15 points per branch). Points, gates and ultimates follow the rules of every class tree: see [Talent system](/en/dynasty/talents).
3. Generic research speed, the Space Pioneer's cost and young colonies are in the [common tree](/en/dynasty/common-tree) (Exploration). The Theorist's tree only holds mechanics of its own.
4. **Head starts**: Unbroken Thread and Flying Start make a study start with part of its time already elapsed. Together, these head starts never exceed **10%** of the study. Flash of Genius, Kept Draft and Symposium sit outside this ceiling.
5. **Study network**: without talents, [Stellar Collaboration](/en/research/stellar-collaboration) only networks Innovation Centers at least as advanced as the one of the studying base. Uplink and Distant Antenna accept lower Centers.
6. **Prototype**: after a civil or drive research level completes (a civil research is one that raises neither military power nor ship speed), the player enjoys the next level's effect for a while. The prototype only applies to the three combat technologies with Combat Prototype (or Test Bench, Specialty, Revolution).
7. Two of the class's bonuses are **accents** (with a ceiling of their own, see [Talent system](/en/dynasty/talents)): the build speed of Innovation Centers (Flat-Pack Benches) and the cost of research levels past level 10 (Patents).

## Worked example

Reference study: **Weapon Systems 10** (409,600 metal, 102,400 crystal), universe research speed ×1, Innovation Center 10 on the studying planet: **46 h 32 min** without a network.

**Method**
- Unbroken Thread: started right after the previous study in the queue, the study starts with 10% of its time elapsed: **41 h 53 min** left.
- Flash of Genius: one click moves the study ahead by 10% of its total time, **4 h 39 min** at once. With Stroke of Genius at rank 3 (19%): **8 h 50 min**.
- Protocols at rank 3 (−6%): 409,600 → **385,024** metal, 102,400 → **96,256** crystal.

**Network**: three colonies with Innovation Centers 10, 9 and 8, Stellar Collaboration 3.
- Without talents, only the Center 10 joins the network: effective level 20, **24 h 22 min**.
- Uplink (2-level tolerance): Centers 9 and 8 join, effective level 37, **13 h 28 min**.
- Field Labs at rank 3: each networked Center counts 3 levels higher, effective level 46, **10 h 53 min**.
- Study Grants at rank 3: the completed study gives back 9% of its cost, **46,080** resources.

**Twin Laboratory**: a second 10 h study runs at 80% of the normal speed and takes **12 h 30 min** (20 h with the common tree's Second Laboratory alone). Without Second Laboratory, it runs at 40% and takes **25 h**.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["PROTOTYPES<br/>One level ahead of everyone."]:::head
        B3R1{{"Prototype<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Extended Trials<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Combat Prototype<br/>1 pt"]:::option
        B3R3B["② Green Light<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Reverse Engineering<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Double Prototype<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Patents<br/>1 pt"]:::option
        B3R6B["② Test Bench<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Spin-offs<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Specialty<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Revolution<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["NETWORK<br/>Every colony is a laboratory."]:::head
        B2R1{{"Uplink<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Field Labs<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Distant Antenna<br/>1 pt"]:::option
        B2R3B["② Mother Lab<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Flat-Pack Benches<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"One More Lab<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Living Network<br/>1 pt"]:::option
        B2R6B["② Shared Results<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Study Grants<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"University Exchange<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Symposium<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["METHOD<br/>A study never waits."]:::head
        B1R1{{"Unbroken Thread<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Flying Start<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Night Watch<br/>1 pt"]:::option
        B1R3B["② Kept Draft<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Protocols<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Flash of Genius<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Quick Wit<br/>1 pt"]:::option
        B1R6B["② Reflex<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Stroke of Genius<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Inspiration<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Twin Laboratory<br/>ultimate"]]:::ultimate
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

### Method: "A study never waits."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Unbroken Thread** | A study that starts on its own, right after the previous one in the queue, starts with part of its time already elapsed. | 10% |
| 2 | 3 ranks | **Flying Start** | A study you launch by hand on an empty research queue starts with part of its time already elapsed, never past the 10% ceiling on head starts. | 3% per rank (9%) |
| 3 | choice | **A: Night Watch** | With an empty research queue, the Innovation Center sets aside 25% of the time passing (1 min every 4 min), up to 2 h of head start paid to the next study. | 2 h |
| | | **B: Kept Draft** | A cancelled study keeps its progress: started again later at the same level, it resumes where it stopped. | unlock |
| 4 | 3 ranks | **Protocols** | Your researches cost less. | −2% per rank (−6%) |
| 5 | key | **Flash of Genius** | Once every 24 h, at the press of a button, the running study jumps ahead by part of its total time, never to its end. | 10% |
| 6 | choice | **A: Quick Wit** | Flash of Genius recharges in 16 h instead of 24 h. | 16 h |
| | | **B: Reflex** | Flash of Genius fires on its own as soon as it is ready and a study runs, even while you are away. | unlock |
| 7 | 3 ranks | **Stroke of Genius** | Flash of Genius advances the study further. | +3% per rank (19%) |
| 8 | key | **Inspiration** | Each completed study brings Flash of Genius back sooner, by part of the study's duration. | 20% |
| 9 | ultimate | **Twin Laboratory** | Your second study (Second Laboratory) runs at 80% of the normal speed. Without Second Laboratory, you still run a second one, at 40%. | 80% / 40% |

### Network: "Every colony is a laboratory."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Uplink** | The study network accepts Innovation Centers up to 2 levels below the studying one. | 2 levels |
| 2 | 3 ranks | **Field Labs** | Each networked Innovation Center counts higher. | +1 level per rank (+3) |
| 3 | choice | **A: Distant Antenna** | The network accepts Centers up to 5 levels below the studying one: for an empire of young colonies. | 5 levels |
| | | **B: Mother Lab** | The studying Center counts 3 levels higher: for a compact empire. | +3 levels |
| 4 | 3 ranks | **Flat-Pack Benches** | Your Innovation Centers are built faster (accent). | 3% per rank (9%) |
| 5 | key | **One More Lab** | The network pools 1 more Center than Stellar Collaboration allows. | +1 Center |
| 6 | choice | **A: Living Network** | When a networked Center levels up during a study, its remaining time is recomputed, never slower. | unlock |
| | | **B: Shared Results** | A completed study gives part of its time as a head start to the next study of the same family, even one launched by hand. | 10% |
| 7 | 3 ranks | **Study Grants** | A study completed with at least 2 networked Centers gives part of its cost back to the studying planet. | 3% per rank (9%) |
| 8 | key | **University Exchange** | The network accepts 1 allied Center: the best one of a member of your alliance, within the network's tolerance. The ally loses nothing. | +1 allied Center |
| 9 | ultimate | **Symposium** | A study launched with at least 4 networked Centers starts with part of its time already elapsed, past the head start ceiling. | 20% |

### Prototypes: "One level ahead of everyone."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Prototype** | After a civil or drive research level completes, you already enjoy the next level's effect. | 12 h |
| 2 | 3 ranks | **Extended Trials** | Your prototypes last longer. | +12 h per rank (48 h) |
| 3 | choice | **A: Combat Prototype** | The prototype also covers Weapon Systems, Shielding Technology and Armor Technology. | unlock |
| | | **B: Green Light** | During a prototype, you can already start what asks for that research's next level. | unlock |
| 4 | 3 ranks | **Reverse Engineering** | After a battle against a player further on than you in a combat technology, your next level of it costs less, once per level. | −5% per rank (−15%) |
| 5 | key | **Double Prototype** | For the 6 h after a study completes, its prototype is worth 2 levels instead of one. Not on combat technologies. | 2 levels, 6 h |
| 6 | choice | **A: Patents** | Research levels past level 10 cost less (accent). | −3% |
| | | **B: Test Bench** | Once every 24 h, start a 6 h prototype by hand on a research already studied, for instance right before an attack. | 6 h |
| 7 | 3 ranks | **Spin-offs** | When a prototype expires, the planet that ran the study gets part of its cost. | 2% per rank (6%) |
| 8 | key | **Specialty** | Choose a research: its prototype never ends. You can change it once a week. Quantum Computing and Astrophysics are excluded. | permanent |
| 9 | ultimate | **Revolution** | Once a week, at the press of a button: for 12 h, all your researches count 1 level higher. | 12 h |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Pure researcher | Method 15 · Network 10 | A queue that never stops, Flash of Genius at 19%, Twin Laboratory; a network opened by Uplink, colony Centers +3 levels, one more Center. |
| Grand network | Network 15 · Method 10 | Symposium and an allied Center; Unbroken Thread, Flash of Genius, Quick Wit or Reflex. |
| War scholar | Prototypes 15 · Method 10 | Revolution, combat prototypes or Green Light, Specialty; Flash of Genius to catch up on levels. |

## Common pitfalls

- **Head starts do not add up without limit**: Unbroken Thread and Flying Start stay under 10% of the study, whatever the rank. Only Flash of Genius, Kept Draft and Symposium go beyond.
- **Uplink does not create a Center**: it lets lower Centers into the network, but their number is still set by Stellar Collaboration (plus 1 with One More Lab).
- **Double Prototype does not touch combat**: combat technologies never get two prototype levels.
- **Twin Laboratory** reads 80% only with the common tree's Second Laboratory; without it, the second study runs at 40%.
- **Patents** only applies to levels past level 10.

## Related pages

- [Classes](/en/dynasty/classes)
- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Technology list](/en/research/technologies)
