---
wiki_id: 169
locale: "en"
path: "dynasty/classes/energist"
url: "https://wiki.dynastynova.com/en/dynasty/classes/energist"
title: "The Energetician"
description: "The Energetician's class tree: Overdrive, Plants, Continuity."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:15.907Z"
updated: "2026-10-07T22:08:05.012Z"
---

# The Energetician

> **In short**: for the Energetician, energy is never wasted. Overdrive pushes mines past their full rate and turns the surplus into hydrogen; Plants makes the Photovoltaic Sensors, the Thermonuclear Reactor and the Solar Collectors stronger and cheaper to run; Continuity keeps an energy shortfall from slowing the mines.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Energetician is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Overdrive, Plants and Continuity.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. The generic energy bonus, +8% on the Photovoltaic Sensors, the Thermonuclear Reactor and the Solar Collectors (Optimised Grid), comes from the [common tree](/en/dynasty/common-tree). The Energetician only has **mechanics**, and a single accent: the construction speed of the Photovoltaic Sensors and the Thermonuclear Reactor (Quick Ignition, 10%).
5. The extra output of an overdriven mine is computed on its **own production**, beside Plasma Technology and the production bonuses, without being multiplied by them and outside the mines' production cap. The energy shortfall then slows the base's whole production; electrolysis finally converts the energy left unused.
6. **Overdrive**: a mine set to 100% runs at 110%. Peak and Overheat raise that rate to **131%** on one mine per base; Wide Overdrive allows three mines per base, at 119% at most. Star Core takes one designated mine per base to 140%.
7. **Load shedding**: in deficit, each mine wins back a share of the output points it lacks, **15 points at most** (30 with Transformers).

## Worked example

Universe at speed 1. A level 20 Mineral Excavator produces **4,036 metal per hour** and draws **1,345 energy** (see [Energy](/en/economy/energy)).

**Full overdrive**
- Superconducting Cables at rank 3: 1,345 × 0.91 = **1,223** energy (rounded down).
- Overdrive, Peak and Overheat at rank 3 (131%): 4,036 + 4,036 × 31% = 4,036 + 1,251 = **5,287 metal per hour**.
- With Fine Tuning at rank 3, the extra draw goes from 25% to 13%: 1,223 × 1.13 = **1,381** energy, only 36 more than the mine without any talent.
- Star Core on this mine (140%): 4,036 + 1,614 = **5,650 metal per hour**. The 9 points past 131% cost 4% each: extra draw 13 + 36 = 49%, that is 1,223 × 1.49 = **1,822** energy.

**Load shedding, base at 50% energy**
- With Load Shedding at rank 3 and Emergency Shedding (40%), 50 points are missing; 40% of 50 = 20, brought down to 15: the mines run at **65%**. With Transformers at rank 3 (30 points at most): **70%**.
- The level 20 Excavator then produces 2,623, then **2,825 metal per hour**, instead of 2,018.

**Level 10 Thermonuclear Reactor, Energy Science 3**
- Output: 30 × 10 × 1.08^10 = 647 energy. With Breeder Reactor (Energy Science counted at level 4): 30 × 10 × 1.09^10 = **710**, then **766** with Optimised Grid (+8%).
- It burns 10 × 10 × 1.1^10 = **259 hydrogen per hour**, 207 with Cold Core, **0** on the Cold Fusion base: 6,216 hydrogen saved per day.

**Solar Collectors, planet with a 60 °C maximum temperature**
- 100 Collectors: 100 × (60 / 4 + 20) = 3,500 energy. Sails at rank 3 and Optimised Grid (+23%): **4,305**. While Flare runs: 4,305 × 1.5 = **6,457**.
- A defense destroys 100 of them, without a Repair Station: **49** stay on the base with The Night Is Short, **70** with Orbital Workshops at rank 3.

**Electrolysis**
- 1,000 unused energy gives **250 hydrogen per hour** with Electrolysis, **333** with Deep Electrolysis, provided the base's Hydrogen Condenser produces at least 84 (or 111) hydrogen per hour: electrolysis never exceeds 3 times its output.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["CONTINUITY<br/>Never out of power."]:::head
        B3R1{{"Deferred Load<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Load Shedding<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Emergency Shedding<br/>1 pt"]:::option
        B3R3B["② Start-up<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Spinning Reserve<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Load Priority<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Accumulators<br/>1 pt"]:::option
        B3R6B["② Quick Ignition<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Transformers<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Flare<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Interplanetary Grid<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["PLANTS<br/>The cheapest energy in the galaxy."]:::head
        B2R1{{"The Night Is Short<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Sails<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Full Sun<br/>1 pt"]:::option
        B2R3B["② Cold Core<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("High Noon<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Breeder Reactor<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Cold Standby<br/>1 pt"]:::option
        B2R6B["② Swarm<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Orbital Workshops<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Cluster Launch<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Cold Fusion<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["OVERDRIVE<br/>Every spare watt becomes ore."]:::head
        B1R1{{"Overdrive<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Fine Tuning<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Peak<br/>1 pt"]:::option
        B1R3B["② Wide Overdrive<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Overheat<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Electrolysis<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Deep Electrolysis<br/>1 pt"]:::option
        B1R6B["② Exchanger<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Superconducting Cables<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Circuit Breaker<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Star Core<br/>ultimate"]]:::ultimate
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

### Overdrive

*Every spare watt becomes ore.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Overdrive** | key | Your mines can run at 110% of their full rate for 25% more energy drawn: 1 per base. |  |
| 2 | **Fine Tuning** | 3 ranks | Overdrive's extra energy draw drops by 12 points. | 3 × 4 pts |
| 3 | **A · Peak** | choice | Overdrive gains 12 points of yield, with no extra energy. | |
|  | **B · Wide Overdrive** |  | You can overclock up to 3 mines on each base. | |
| 4 | **Overheat** | 3 ranks | Overdrive gains a further 9 points of yield, with no extra energy. | 3 × 3 pts |
| 5 | **Electrolysis** | key | Energy nothing uses is no longer lost: it turns into hydrogen, 4 energy per unit, up to three times what the mine of that resource produces on the base. Overdrive takes its share first. |  |
| 6 | **A · Deep Electrolysis** | choice | Only 3 unused energy now makes a unit of hydrogen. | |
|  | **B · Exchanger** |  | On each base, electrolysis can yield metal or crystal instead: 3 metal or 2 crystal for what would have made 1 hydrogen, still capped by the base's metal or crystal mine. | |
| 7 | **Superconducting Cables** | 3 ranks | Your mines draw 9% less energy. | 3 × 3% |
| 8 | **Circuit Breaker** | key | When energy runs short, overdrive backs off on its own before the base falls into deficit, then comes back as soon as it can. |  |
| 9 | **Star Core** | ultimate | On each base, the mine of your choice can go past overdrive, up to 140% of its full rate. Each step of 5 points beyond draws 20% more energy. |  |

- **Overdrive**: only a mine set to 100% can be overdriven; lowering its rate stops it. The extra draw applies to the draw already reduced by Superconducting Cables.
- **Electrolysis**: the energy left unused once everything is served, overdrive included. Per hour, electrolysis never yields more than 3 times what the base's Hydrogen Condenser produces: no Condenser, no hydrogen. It stops while the Accumulators reserve is filling.
- **Exchanger** is chosen base by base; it excludes Deep Electrolysis, so it takes 4 energy for 3 metal or 2 crystal. The cap is then 3 times the output of the base's Mineral Excavator or Crystal Extractor.
- **Circuit Breaker**: if overdrive would throw the base into deficit, the base's whole overdrive (Star Core included) backs off by the same share, just enough to keep energy balanced; it comes back on its own when energy allows.
- **Star Core**: the designated mine must be overdriven. Each point past the overdrive rate costs 4% energy (20% per 5-point step), added to the overdrive's extra draw: 36% from 131%, 84% from 119%.

### Plants

*The cheapest energy in the galaxy.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **The Night Is Short** | key | After a defense, 49% of your destroyed solar satellites are raised again for free, on the share that does not go to debris. |  |
| 2 | **Sails** | 3 ranks | Your solar satellites produce 15% more energy. | 3 × 5% |
| 3 | **A · Full Sun** | choice | Your solar plants produce 10% more energy. | |
|  | **B · Cold Core** |  | Your fusion plant burns 20% less hydrogen. | |
| 4 | **High Noon** | 3 ranks | Your solar plant reads a temperature 45% closer to the month's maximum. | 3 × 15% |
| 5 | **Breeder Reactor** | key | Your fusion plant counts energy science as 1 level higher. |  |
| 6 | **A · Cold Standby** | choice | Your fusion plant can be set like a mine, from off to full rate, and burns that much less hydrogen. | |
|  | **B · Swarm** |  | Your solar satellites cost 20% less. | |
| 7 | **Orbital Workshops** | 3 ranks | The Night Is Short raises 21 more points of your destroyed satellites. | 3 × 7 pts |
| 8 | **Cluster Launch** | key | Your solar satellites are built on their own line, beside the shipyard: it stays free for your ships while a cluster goes up. |  |
| 9 | **Cold Fusion** | ultimate | On the base of your choice, the fusion plant burns no hydrogen at all. |  |

- **The Night Is Short**: after a battle where the base loses Solar Collectors, 49% of the destroyed Collectors (rounded down) stay on the base at once. Those the Repair Station already took in are counted off: you get back the larger of the two numbers. The debris field is computed on all losses.
- **Sails**, **Full Sun**: these percentages add to the 8% of Optimised Grid (23% for Collectors, 18% for Sensors).
- **High Noon**: the Sensors read the day's temperature plus 45% of the gap up to the month's maximum. The Sensors gain nothing below 0 °C: on a cold planet, the node changes nothing.
- **Cold Standby**: without this node, the Reactor always runs at 100%, whatever its setting. With it, its energy and hydrogen burn follow the chosen rate.
- **Swarm** applies on top of the 5% cap on cost reductions.
- **Cluster Launch**: Collectors built on their own lane do not draw on a Builder's Orbital Dock head start.
- **Cold Fusion**: you designate the base, and can change it.

### Continuity

*Never out of power.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Deferred Load** | key | A mine level just completed draws its new consumption only 4 h later: time to raise the plant that goes with it. |  |
| 2 | **Load Shedding** | 3 ranks | Your mines ignore 30% of the energy shortfall. | 3 × 10% |
| 3 | **A · Emergency Shedding** | choice | Your mines ignore a further 10% of the energy shortfall. | |
|  | **B · Start-up** |  | On a colony younger than 30 days, your mines ignore the whole energy shortfall: raise them before the first plant. | |
| 4 | **Spinning Reserve** | 3 ranks | Deferred Load lasts 6 h longer. | 3 × 2 h |
| 5 | **Load Priority** | key | On each base, the mine of your choice is served first when energy runs short; the others share the rest. |  |
| 6 | **A · Accumulators** | choice | Your spare energy is stored, up to 12 h of surplus, and covers a deficit on its own. | |
|  | **B · Quick Ignition** |  | Your solar and fusion plants are built 10% faster. | |
| 7 | **Transformers** | 3 ranks | Load shedding can win back 15 more points of energy, on top of the 15 it already does. | 3 × 5 pts |
| 8 | **Flare** | key | Once a day, on the base of your choice, solar plants and satellites produce one and a half times as much energy for 4 h. |  |
| 9 | **Interplanetary Grid** | ultimate | Your planets' surplus feeds those short of energy, up to 20% of their consumption. |  |

- **Deferred Load**: the completed level produces at once; only its draw waits, the previous level's draw staying in force during the delay.
- **Start-up**: on a colony founded by a Space Pioneer less than 30 days ago, not on the home planet.
- **Load Priority**: the designated mine runs full as long as energy production covers **its** draw; the others share the rest, with their load shedding.
- **Accumulators**: the base stores at most 12 hours of its current surplus. In deficit, the reserve covers the whole shortfall, the mines running full, until it runs out.
- **Flare**: on a base with Photovoltaic Sensors or Solar Collectors, 24 h after the previous one, for your whole empire.
- **Interplanetary Grid**: each planet in deficit receives at most the smaller of its shortfall and 20% of its draw, within the others' surplus, shared in proportion. Moons take no part. The sharing is redone regularly.
- **Flare** and **Interplanetary Grid** do not count toward the energy a research such as Graviton Technology requires.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| −12 pts on overdrive's extra energy draw | 12 pts |
| −9% energy drawn by the mines | 9% |
| +15% solar satellite energy | 15% |
| +10% solar plant energy | 10% |
| −20% fusion plant hydrogen consumption | 20% |
| The solar plant reads a temperature of the day that closes 45% of the gap to the month's maximum | 45% |
| The fusion plant reads energy science as if it had +1 level | 1 |
| −20% solar satellite cost | 20% |
| A mine level just completed draws its new energy consumption only 10 h later | 10 h |
| All three mines ignore a further 40% of the energy shortfall | 40% |
| +10% solar and fusion plant construction speed | 10% |
| Load shedding can win back 15 pts more energy | 15 pts |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Surplus Miner | Overdrive 15 · Plants 10 | one mine at 131% or three at 119% per base, 13% extra draw, electrolysis, mines −9% energy, Circuit Breaker, one mine up to 140% with Star Core; Collectors +15%, Full Sun or Cold Core, High Noon, Breeder Reactor |
| Climber | Continuity 15 · Overdrive 10 | 10 h delay, load shedding up to 30 points (40% of the shortfall), Load Priority, Flare, Interplanetary Grid; one mine at 131% or three at 119%, electrolysis |
| Lord of the Collectors | Plants 15 · Continuity 10 | Collectors raised at 70%, Cluster Launch, Swarm −20%, Cold Fusion on one base; 10 h delay, load shedding, Load Priority |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Overdrive always costs energy**: without a surplus it throws the base into deficit and slows all three mines. Circuit Breaker makes it back off in time.
- **An overdriven mine must stay at 100%**: lowering its rate stops the overdrive.
- **Electrolysis creates nothing from energy already used**, nor without a Hydrogen Condenser on the base, nor while the Accumulators reserve is filling.
- **Load shedding is bounded**: in a deep deficit, it only gives back 15 output points (30 with Transformers).
- **No Continuity talent produces ore**: the branch removes the brake that stops you from raising a mine before its plant.
- **Row 3 of Plants decides your energy**: Photovoltaic Sensors burn nothing but depend on temperature, and High Noon is useless on a cold planet; the Reactor burns hydrogen but grows with Energy Science.
- **Flare and Interplanetary Grid do not unlock Graviton Technology**: the energy it requires is read without them.

## Related pages

- [Talents](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Energy](/en/economy/energy)
- [Planets: size, temperature, type](/en/universe/planets)
- [Repair Station](/en/economy/repair-station)
