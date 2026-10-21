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
updated: "2026-10-21T16:00:26.928Z"
---

# The Theorist

> **In short**: "Understand first". The Theorist always has a study running and a level ahead. Method keeps the research queue from ever stopping, Network pools the Innovation Centers of its colonies, Prototypes lets it enjoy a research level before anyone else.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Theorist is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Method, Network and Prototypes.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic research speed and the second parallel study (Second Innovation Center) are in the [common tree](/en/dynasty/common-tree). The Theorist's tree only holds mechanics of its own. Its two **accents** are the Innovation Centers' build speed (Flat-Pack Benches) and the cost of research levels from the 11th on (Patents).
5. **Head starts.** A study may start with part of its time already elapsed. Unbroken Thread or Flying Start, plus Night Watch and Shared Results, never exceed **10%** of the study all together. Symposium, Kept Draft and the Archivist's momentum add on top. No head start ever completes a study.
6. **Research network.** With no talent, [Stellar Collaboration](/en/research/stellar-collaboration) level N pools the N best Innovation Centers of your other planets, if they are at least as advanced as the studying one. The network shortens the study, never its cost.
7. **Prototype.** A prototype makes a research count some levels higher for a while, wherever the game reads its level (fleet slots, number of planets, network Centers, combat...), never past its maximum level. It only applies to a research studied at least once. The three **combat technologies** (Weapon Systems, Shielding Technology, Armor Technology) only get a study prototype with Combat Prototype.
8. Prototype, Specialty and Revolution **do not add up** on the same research: it takes the largest of the three bonuses.
9. Research cost reductions (Protocols, Patents, Reverse Engineering) add up, then each resource is rounded up. They do not shorten the study, whose duration is computed on the normal price.

## Worked example

Reference study: **Weapon Systems 10** (409,600 metal, 102,400 crystal), universe research speed ×1, Innovation Center 10 on the studying planet: 512,000 / (1,000 × 11) h = **46 h 32 min 44 s**.

**Method**
- Unbroken Thread: the study, started after the previous one in the queue, begins with 10% of its time elapsed: **41 h 53 min 28 s** remain.
- Started by hand after 10 h of empty queue, with Flying Start at rank 3 and Night Watch: 9% (4 h 11 min 20 s) plus 2 h banked make 6 h 11 min 20 s, brought down to the 10% ceiling: **4 h 39 min 16 s**. Night Watch only added 27 min 56 s.
- Flash of Genius: one click moves the study ahead by 10% of its total time, **4 h 39 min 16 s**. With Stroke of Genius at rank 3 (19%), that would be 8 h 50 min, brought down to the **6 h** maximum.
- Protocols at rank 3 (−18%): 409,600 → **335,872** metal, 102,400 → **83,968** crystal.

**Network**: studying Center 10, three colonies with Centers 10, 9 and 8, Stellar Collaboration 3.
- With no talent, only the colony's Center 10 joins: effective level 10 + 10 = 20, **24 h 22 min 51 s**.
- Uplink: Centers 9 and 8 join too, effective level 37, **13 h 28 min 25 s**.
- Field Labs at rank 3: each of the three colony Centers counts 3 levels higher, effective level 46, **10 h 53 min 37 s**. With Mother Lab on top, 49: **10 h 14 min 24 s**.
- Study Grants at rank 3: the completed study gives back 9% of what it cost, that is **36,864** metal and **9,216** crystal on a 512,000 price.
- Symposium (4 Centers or more): 20% more at the start. A chained study then starts with 10% + 20% = **13 h 57 min 48 s** already done.

**Twin Innovation Center**: a second 10 h study takes **12 h 30 min** with Second Innovation Center and the ultimate (80%), 20 h with Second Innovation Center alone (50%), **25 h** with the ultimate alone (40%).

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
        B2H["NETWORK<br/>Every colony is an innovation center."]:::head
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
        B1R9[["✦ Twin Innovation Center<br/>ultimate"]]:::ultimate
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

### Method

*A study never waits.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Unbroken Thread** | key | A study that starts on its own, right after the previous one in the queue, starts with 10% of its time already elapsed. |  |
| 2 | **Flying Start** | 3 ranks | A study you launch by hand on an empty research queue starts with 9% of its time already elapsed, never past the 10% ceiling on head starts. | 3 × 3% |
| 3 | **A · Night Watch** | choice | When your research queue is empty, the lab sets aside 25% of the time passing, up to 2 h of head start paid to the next study. | |
|  | **B · Kept Draft** |  | A cancelled study keeps its progress: started again later at the same level, it resumes where it stopped. | |
| 4 | **Protocols** | 3 ranks | Your researches cost 18% less. | 3 × 6% |
| 5 | **Flash of Genius** | key | Once a day, at the press of a button, the running study jumps ahead by 10% of its total time, 6 h at most, never to its end. |  |
| 6 | **A · Quick Wit** | choice | Flash of Genius recharges in 16 h. | |
|  | **B · Reflex** |  | Flash of Genius fires on its own as soon as it is ready and a study runs, even while you are away. | |
| 7 | **Stroke of Genius** | 3 ranks | Flash of Genius advances the study by 9% more. | 3 × 3% |
| 8 | **Inspiration** | key | Each completed study brings Flash of Genius back sooner, by 20% of its duration. |  |
| 9 | **Twin Innovation Center** | ultimate | Your second study (Second Innovation Center) runs at 80% of the normal speed. Without Second Innovation Center, you still run a second one, at 40%. |  |

- **Unbroken Thread** only works for a study that starts on its own after the previous one; **Flying Start** only for a study started by hand on an empty queue. Neither works in the second Innovation Center.
- **Night Watch** counts the time since the last study ended (completed or cancelled), and only serves a study started by hand. Since Flying Start already takes 9% of the 10%, it adds at most 1% of the study.
- **Kept Draft**: only a running study can be cancelled with its progress. It gets it back when you start the same level of the same research again, past the 10% ceiling. One draft per research, the latest.
- **Flash of Genius**: 6 h at most, even with Stroke of Genius, which therefore adds nothing past 31 h 35 min of study. The recharge counts from use, for the whole empire. If the advance would complete the study, the button is refused and stays available; Reflex also waits for a long enough study.
- **Inspiration** shortens the recharge by 20% of each completed study's duration, only while the burst is recharging.
- **Twin Innovation Center**: the second study must be another research, and nothing may wait in the queue. It gets neither Unbroken Thread, Flying Start, Night Watch nor Shared Results.

### Network

*Every colony is an innovation center.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Uplink** | key | The study network accepts labs up to 2 levels below the studying one. |  |
| 2 | **Field Labs** | 3 ranks | Each of your networked labs counts 3 levels higher. | 3 × 1 |
| 3 | **A · Distant Antenna** | choice | The study network accepts labs up to 5 levels below the studying one: for an empire of young colonies. | |
|  | **B · Mother Lab** |  | The studying lab counts 3 levels higher: for a compact empire. | |
| 4 | **Flat-Pack Benches** | 3 ranks | Your research labs are built 9% faster. | 3 × 3% |
| 5 | **One More Lab** | key | The study network pools 1 more lab than Stellar Collaboration allows. |  |
| 6 | **A · Living Network** | choice | When a lab of the network levels up during a study, its remaining time is recomputed, never slower. | |
|  | **B · Shared Results** |  | A completed study gives 10% of its time as a head start to the next study of the same family, even one launched by hand. | |
| 7 | **Study Grants** | 3 ranks | A study completed with at least 2 networked labs gives 9% of its cost back to the studying planet. | 3 × 3% |
| 8 | **University Exchange** | key | Your study network accepts 1 allied lab: the best one of a member of your alliance, within the network's tolerance. The ally loses nothing. |  |
| 9 | **Symposium** | ultimate | A study launched with at least 4 networked labs starts with 20% of its time already elapsed, past the head start ceiling. |  |

- **Uplink** and **Distant Antenna** do not add up: the tolerance is 5 levels with both. A level 0 Center never joins.
- **Field Labs** only applies to the pooled Centers of your other planets, not to the studying one nor to the allied Center.
- **Living Network**: when one of your Innovation Centers finishes a level, the network is recomputed as it stands and the remaining time drops in the same proportion.
- **Shared Results** passes 10% of the completed study's duration to the next one of the same category, but under the 10% ceiling: with Unbroken Thread, it adds nothing to a chained study.
- **Study Grants**: 2 Centers in the network, the studying one included. The share is taken on the price paid, resource by resource, and paid to the studying planet.
- **University Exchange**: the allied Center comes on top of Stellar Collaboration's limit, if it is within the tolerance. It counts for Study Grants and Symposium.
- **Symposium**: 4 Centers in the network, the studying one and the ally included. Also works in the second Innovation Center.

### Prototypes

*One level ahead of everyone.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Prototype** | key | For 12 h after a civil or drive research level completes, you already enjoy the next level's effect. |  |
| 2 | **Extended Trials** | 3 ranks | Your prototypes last 36 h longer. | 3 × 12 h |
| 3 | **A · Combat Prototype** | choice | The prototype also covers Weapon Systems, Shielding Technology and Armor Technology. | |
|  | **B · Green Light** |  | During a prototype, you can already start what asks for that research's next level. | |
| 4 | **Reverse Engineering** | 3 ranks | After a battle against a player further on than you in a combat technology, your next level of it costs 15% less, once per level. | 3 × 5% |
| 5 | **Double Prototype** | key | For the 6 h after a study completes, its prototype is worth 2 levels instead of one. Not on combat technologies. |  |
| 6 | **A · Patents** | choice | Research levels past level 10 cost 3% less. | |
|  | **B · Test Bench** |  | Once a day, start a 6 h prototype by hand on a research already studied, for instance right before an attack. | |
| 7 | **Spin-offs** | 3 ranks | When a prototype expires, the planet that ran the study gets 6% of its cost. | 3 × 2% |
| 8 | **Specialty** | key | Choose a research: its prototype never ends. You can change it once a week. Quantum Computing and Astrophysics are excluded. |  |
| 9 | **Revolution** | ultimate | Once a week, at the press of a button: for 12 h, all your researches count 1 level higher. Keep it for the big offensive or the night of defense. |  |

- **Prototype**: every research except Weapon Systems, Shielding Technology and Armor Technology. A new prototype of the same research ends the previous one.
- **Green Light**: research requirements are read at the level reached with a prototype, Specialty or Revolution. Building requirements do not change.
- **Reverse Engineering** triggers on a planet attack, whether you attack or defend, for each combat technology where the opponent was higher than you. The discount targets your next level, once.
- **Double Prototype**: never on combat technologies.
- **Test Bench** also works on combat technologies, without Combat Prototype. It ends the running study prototype of that research and gives no Spin-offs.
- **Spin-offs**: the share is taken on what the study paid, and paid when its prototype ends, even cut short by a new one, if the planet is still yours.
- **Specialty**: a research already studied, +1 level for good. A combat technology only with Combat Prototype. The change delay counts from the last change.
- **Revolution**: all your researches already studied, combat technologies included.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| −18% research cost | 18% |
| The study network accepts innovation centers up to 5 levels below the one doing the study | 5 (capped) |
| Each of your networked labs counts +3 levels | 3 |
| The innovation center counts as +3 levels for research times | 3 |
| +9% innovation center construction speed | 9% |
| The study network pools +1 innovation center beyond what its level allows | 1 |
| −3% cost on high research levels | 3% |

The network tolerance keeps the largest value held (Uplink or Distant Antenna): 5 levels at most.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Pure researcher | Method 15 · Network 10 | Twin Innovation Center, Unbroken Thread, Kept Draft, Protocols −18%, Flash of Genius at 19% (6 h at most) every 16 h or automatic, Inspiration; Uplink, colony Centers +3 levels, One More Lab, Living Network |
| Great network | Network 15 · Method 10 | Symposium, University Exchange, Study Grants 9%, 5-level tolerance or Mother Lab; Unbroken Thread, Protocols −18%, Flash of Genius at 10%, Quick Wit or Reflex |
| War scholar | Prototypes 15 · Method 10 | Revolution, 48 h prototypes, Combat Prototype or Green Light, Reverse Engineering −15%, Specialty; Flash of Genius to catch up on levels |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **The 10% ceiling is shared**: Unbroken Thread fills it alone on a chained study, and Night Watch adds at most 1% to a study started by hand. Kept Draft is almost always the better row 3 choice.
- **Flash of Genius is capped at 6 h**: on a long study, Stroke of Genius changes nothing.
- **Uplink does not create a Center**: the number stays set by Stellar Collaboration, plus 1 with One More Lab and 1 ally with University Exchange.
- **Double Prototype does not touch combat**: combat technologies never get two prototype levels.
- **Level bonuses do not stack**: a Revolution adds nothing to a research that already has a prototype or the Specialty.
- **Twin Innovation Center** reaches 80% only with Second Innovation Center; without it, the second study runs at 40%.
- **Patents** only applies from a research's level 11.

## Related pages

- [Classes](/en/dynasty/classes)
- [Talents](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Technology list](/en/research/technologies)
