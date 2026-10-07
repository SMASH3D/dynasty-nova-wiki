---
wiki_id: 173
locale: "en"
path: "dynasty/classes/symbiote"
url: "https://wiki.dynastynova.com/en/dynasty/classes/symbiote"
title: "The Symbiote"
description: "The environment class, exclusive to The Accord: Thermal, Growth and Host."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:25.107Z"
updated: "2026-10-06T10:30:26.572Z"
---

# The Symbiote

> **In short**: the Symbiote plays what others endure: the planet's temperature, its place in the system, its size, its moon and its neighbours. Thermal turns temperature into an asset, Growth makes the most of position and fields, Host makes fallow planets and crowded systems produce.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Symbiote is a class **exclusive to [The Accord](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Thermal, Growth and Host.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6. Points, gates and choices are explained on [Talents](/en/dynasty/talents).
4. Mine production, young colonies and generic fields come from the [common tree](/en/dynasty/common-tree). Fusion, Solar Collectors and energy shortage belong to the [Energetician](/en/dynasty/classes/energist). The Symbiote has a single accent: 2 more fields per planet (*Ground Gained*), 4 at most with the common tree.
5. The temperature and position bonus rules these talents play on are described on [Planets: size, temperature, type](/en/universe/planets).

## Worked example

**Hydrogen Condenser on a colony in position 15** (−85 to −45 °C)
- Without talents, the factor is 1.44 − 0.004 × (−45) = **1.62**. The cold bonus is the part above 1: 0.62.
- With *Cold Blood* (+10%): 1 + 0.62 × 1.10 = **1.68**.
- With *Cold Blood* and *Reading the Climate* at rank 3 (+40%): 1 + 0.62 × 1.40 = **1.87**.
- With *Cold Pole* on top (+65% in all): 1 + 0.62 × 1.65 = **2.02**.

**The Two Seasons on a colony in position 8** (20 to 60 °C)
- Without talents, the Condenser reads the maximum temperature: 1.44 − 0.004 × 60 = **1.20**.
- With the ultimate, it reads the minimum: 1.44 − 0.004 × 20 = **1.36**, 13% more hydrogen.
- With the whole branch (+40%): 1.28 without the ultimate, **1.50** with it, 17.5% more.

**Mineral Excavator position bonus in position 8** (+35% without talents)
- *Roots*: 35 × 1.15 = **+40.25%**.
- *Roots* and *Layering*: 35 × 1.45 = **+50.75%**.
- With *Metal Lode* on top: 35 × 1.65 = **+57.75%**.
- A homeworld in position 8 with *Native Soil* at rank 3 and no other talent: 35 × ½ = **+17.5%**.

**Solar Collector in position 8** (maximum temperature 60 °C)
- Without talents: 60 / 4 + 20 = **35** energy per Collector.
- *Skin of Light* at rank 3: 15 × 1.45 + 20 = 41.75, rounded down to **41** energy.
- *High-Altitude Satellites*: the planet is read at 100 °C, 100 / 4 + 20 = **45** energy.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["HOST<br/>Make a world live on what it has."]:::head
        B3R1{{"Young Shoot<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Rising Sap<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Small Worlds<br/>1 pt"]:::option
        B3R3B["② Giants<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Long Fallow<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Neighbourhood<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Crowd<br/>1 pt"]:::option
        B3R6B["② Solitude<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Tides<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Regrowth<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Eternal Fallow<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["GROWTH<br/>The right place, the right size."]:::head
        B2R1{{"Roots<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Native Soil<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Metal Lode<br/>1 pt"]:::option
        B2R3B["② Crystal Vein<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Hollowed Moons<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Layering<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Ground Gained<br/>1 pt"]:::option
        B2R6B["② Full Moon<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Living Soil<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Living Terraformer<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Transplantation<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["THERMAL<br/>The planet decides, you listen."]:::head
        B1R1{{"Cold Blood<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Planetary Climate Control<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Cold Pole<br/>1 pt"]:::option
        B1R3B["② Hot Pole<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Skin of Light<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"The Long Season<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Deep Roots<br/>1 pt"]:::option
        B1R6B["② Winter Sun<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Reading the Climate<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"High-Altitude Satellites<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ The Two Seasons<br/>ultimate"]]:::ultimate
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

### Thermal

*The planet decides, you listen.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Cold Blood** | Your planets' temperature bonuses (cold for the Hydrogen Condenser, heat for the Photovoltaic Sensors) are stronger. | 1 rank | +10% |
| 2 | **Planetary Climate Control** | On each planet, you shift the temperature toward the cold or the heat. Adjustable once a week. | 3 × 10 °C | 30 °C |
| 3 | **A · Cold Pole** or **B · Hot Pole** | A: the Hydrogen Condenser's cold bonus is stronger still. <br> B: the heat bonus of the Photovoltaic Sensors and Solar Collectors is stronger still. | 1 rank | +25% |
| 4 | **Skin of Light** | The share of your Solar Collectors' energy that comes from temperature is stronger. | 3 × 15% | +45% |
| 5 | **The Long Season** | The Photovoltaic Sensors always produce as at the month's hottest, instead of following the cycle. | 1 rank | unlock |
| 6 | **A · Deep Roots** or **B · Winter Sun** | A: on a planet too hot for it, the Hydrogen Condenser's factor never drops below ×1. <br> B: on a cold planet, the Photovoltaic Sensors' factor never drops below ×1.25. | 1 rank | A: ×1 <br> B: ×1.25 |
| 7 | **Reading the Climate** | Temperature bonuses are stronger still. | 3 × 10% | +30% (+40% with Cold Blood) |
| 8 | **High-Altitude Satellites** | Your Solar Collectors produce as if the planet were hotter. | 1 rank | +40 °C |
| 9 | **The Two Seasons** *(ultimate)* | Your Hydrogen Condenser reads the planet's **minimum** temperature, not its maximum. | 1 rank | unlock |

Row 3 amplifies your strength, row 6 fixes your weakness: the player of cold planets and the player of hot planets do not make the same choices.

### Growth

*The right place, the right size.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Roots** | Your planets' position bonus is stronger. | 1 rank | +15% |
| 2 | **Native Soil** | Your homeworld, which never gets a position bonus, receives a share of it. | 3 × ⅙ | ½ |
| 3 | **A · Metal Lode** or **B · Crystal Vein** | A: the Mineral Excavator's position bonus (positions 6 to 10) is stronger still. <br> B: the Crystal Extractor's (positions 1 to 3) is stronger still. | 1 rank | +20% |
| 4 | **Hollowed Moons** | Each Lunar base level gives fields on top of its 3, within the moon's diameter. | 3 × 1 field | 6 fields per level |
| 5 | **Layering** | The position bonus is stronger still. | 1 rank | +30% (+45% with Roots) |
| 6 | **A · Ground Gained** or **B · Full Moon** | A: each of your planets gains 2 fields (accent). <br> B: your moons are no longer bounded by their diameter. | 1 rank | A: +2 fields <br> B: unlock |
| 7 | **Living Soil** | The Planetary Modulator and the Lunar base cost less. | 3 × 8% | −24% |
| 8 | **Living Terraformer** | Each Planetary Modulator level gives one more field, on top of the extra field at even levels (Modulator 6: 33 → 39 fields). | 1 rank | +1 field per level |
| 9 | **Transplantation** *(ultimate)* | Once a week, you move a colony to a free position of its system, buildings and moon included, if no fleet is flying to or from it. | 1 rank | 1 per week |

Every Growth point is worth something on the right positions and nothing elsewhere; the ultimate fixes a bad placement.

### Host

*Make a world live on what it has.*

A planet is **fallow** while fewer than half of its fields are built. This notion belongs to the Symbiote; do not mix it up with the common tree's young colony.

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Young Shoot** | On a fallow planet, your buildings are built faster. | 1 rank | +10% |
| 2 | **Rising Sap** | The mines of your fallow planets produce more. | 3 × 5% | +15% |
| 3 | **A · Small Worlds** or **B · Giants** | A: on a planet of fewer than 150 fields, your buildings cost 15% less. <br> B: on a planet of more than 200 fields, your mines produce 8% more. | 1 rank | A: −15% <br> B: +8% |
| 4 | **Long Fallow** | A planet stays fallow longer: the threshold rises above half of its fields built. | 3 × 10 pts | 80% of the fields |
| 5 | **Neighbourhood** | Each planet of another player in the system of one of your planets raises its mines. | 1 rank | +1% per neighbour, 8% at most |
| 6 | **A · Crowd** or **B · Solitude** | A: +2% per neighbour, up to 15%. <br> B: a planet alone in its system, with no other player, produces 10% more in its mines. | 1 rank | A: 15% at most <br> B: +10% |
| 7 | **Tides** | When several of your planets share a system, each one's mines produce more. | 3 × 3% | +9% |
| 8 | **Regrowth** | A plundered planet produces more in its mines for the next 6 hours. | 1 rank | +20% for 6 h |
| 9 | **Eternal Fallow** *(ultimate)* | One planet of your choice, homeworld included, stays fallow for good, however many fields are built. Changing it takes a week. | 1 rank | 1 planet |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Climatologist | Thermal 15 · Host 10 | The Two Seasons, temperature bonuses +40 to +65%, Photovoltaic Sensors at the month's hottest, 30 °C climate control; fallow planets +15%, small worlds or giants, fallow up to 80% of the fields, Neighbourhood |
| Settler | Growth 15 · Thermal 10 | Transplantation, position bonus +45 to +65%, homeworld at half its bonus, one more field per Modulator level; temperature bonuses +40%, one pole, long season |
| Gardener | Host 15 · Growth 10 | Eternal Fallow, fallow planets +15%, Neighbourhood, Tides, Regrowth; position bonus +45%, Native Soil, +2 fields or full moon |

## Common pitfalls

- **A temperature bonus never changes sign**: on a planet too hot for the Hydrogen Condenser (factor below 1), *Cold Blood* adds nothing. *Deep Roots* raises the floor instead.
- **The position bonus only concerns two mines**: the Crystal Extractor in positions 1 to 3, the Mineral Excavator in positions 6 to 10. Elsewhere, Roots and Layering bring nothing.
- **"Fallow" is not "young"**: a colony is young for its first 7 days (common tree); a planet is fallow while not enough of its fields are built.
- **Climate Control is set once a week** per planet, and never on a moon.
- **Transplantation** is refused while a fleet is flying to or from the colony.

## Related pages

- [Talents](/en/dynasty/talents)
- [Classes](/en/dynasty/classes)
- [Common tree](/en/dynasty/common-tree)
- [Dynasties](/en/dynasty/dynasties)
- [Planets: size, temperature, type](/en/universe/planets)
- [Energy](/en/economy/energy)
- [The Energetician](/en/dynasty/classes/energist)
