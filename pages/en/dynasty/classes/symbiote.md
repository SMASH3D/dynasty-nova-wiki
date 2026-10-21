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
updated: "2026-10-21T16:00:25.330Z"
---

# The Symbiote

> **In short**: the Symbiote plays what others endure: the planet's temperature, its place in the system, its size, its moon and its neighbours. Thermal turns temperature into an asset, Growth makes the most of position and fields, Host makes fallow planets and planets with neighbours produce.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Symbiote is a class **exclusive to [The Accord](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Thermal, Growth and Host.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic mine production, young colonies and generic fields come from the [common tree](/en/dynasty/common-tree). Fusion, the Solar Collectors' own output and energy shortage belong to the [Energetician](/en/dynasty/classes/energist). The Symbiote has a single **accent**: 2 more fields per planet (Ground Gained), 4 at most with Surveyors (common tree).
5. The Host's mine bonuses are mechanics of their own: they add to each other and to the other bonuses, all computed on the **gross output** of the three mines (Mineral Excavator, Crystal Extractor, Hydrogen Condenser), and they stay **outside** the talents' production cap. Never on a moon.
6. Temperature talents only widen a factor's **bonus share**, never its sign. Hydrogen Condenser: factor 1.44 − 0.004 × maximum temperature, widened only above 1. Photovoltaic Sensors: factor 1 + the day's temperature / 100, widened only above 0 °C. Solar Collector: maximum temperature / 4 + 20 energy, only the temperature share is widened, rounded down. Temperatures are detailed on [Planets: size, temperature, type](/en/universe/planets).
7. The position bonus **depends on the number of positions in the system**, a universe setting (15 on Redline). In a 15-position system, the Crystal Extractor gains +40, +30 and +20% in positions 1 to 3, the Mineral Excavator +17, +23, +35, +23 and +17% in positions 6 to 10. Elsewhere, the position is brought onto a 15-position scale and the bonus is computed between the two neighbouring positions: in a 9-position system, position 2 gives +22.5% crystal. The Hydrogen Condenser never gets a position bonus.
8. A planet is **fallow** while its built fields are strictly under 50% of its total fields (Planetary Modulator and bonus fields included). This only exists for a Symbiote holding Young Shoot or Rising Sap, and never applies to a moon. It has nothing to do with the common tree's young colony.

## Worked example

**Hydrogen Condenser in position 15 of a 15-position system** (−85 to −45 °C)
- No talent: 1.44 − 0.004 × (−45) = **1.62**. The bonus share is 0.62.
- With Cold Blood (+10%): 1 + 0.62 × 1.10 = **1.68**.
- Adding Reading the Climate at rank 3 (+40% in all): 1 + 0.62 × 1.40 = **1.87**.
- Adding Cold Pole (+65% in all): 1 + 0.62 × 1.65 = **2.02**.
- Full branch, with The Two Seasons and Planetary Climate Control set toward the cold: the Condenser reads −85 − 30 = −115 °C, factor 1.44 + 0.46 = 1.90, then 1 + 0.90 × 1.65 = **2.485**.
- At level 20, economy speed ×1 (Redline): 10 × 20 × 1.1²⁰ = 1,345.5 hydrogen per hour before the factor, that is **2,179** with no talent and **3,343** with the full branch (+53%).

**The Two Seasons on a colony in position 8 of a 15-position system** (20 to 60 °C)
- No talent, the Condenser reads the maximum temperature: 1.44 − 0.004 × 60 = **1.20**.
- With the ultimate, it reads the minimum: 1.44 − 0.004 × 20 = **1.36**, that is 13% more hydrogen.

**Mineral Excavator position bonus in position 8 of a 15-position system** (+35% with no talent)
- Roots changes nothing here: its 15% floor is under the position's 35%. The same planet's Crystal Extractor, with no position bonus, goes up to **+15%** instead.
- Layering: 35 × 1.9 = **+66.5%**.
- Adding Metal Lode: 35 × 1.65 = **+57.75%**.
- A homeworld at the same spot, with Layering and Native Soil at rank 3: 35 × 1.9 × 1.05 = **+69.825%**. Without Native Soil, it would only get the floor: +15% with Roots, +30% with Hollowed Moons at rank 3.

**Position floor at position 13 of a 15-position system** (no bonus without talents)
- Roots and Hollowed Moons at rank 3: the Mineral Excavator and the Crystal Extractor each get **+30%**. Layering adds nothing there: it widens the position's bonus, not the floor.

**Solar Collector in position 8 of a 15-position system** (maximum temperature 60 °C)
- No talent: 60 / 4 + 20 = **35** energy per Collector.
- Skin of Light at rank 3: 15 × 1.45 + 20 = 41.75, rounded down to **41**.
- High-Altitude Satellites: the planet is read at 100 °C, 100 / 4 + 20 = **45**.
- Skin of Light at rank 3, Hot Pole, High-Altitude Satellites and Planetary Climate Control set toward the heat: (60 + 30 + 40) / 4 = 32.5, × 1.70 (45 + 25% amplitude) = 55.25, + 20 = **75**.

**Host on a 210-field colony with 100 fields built, Mineral Excavator level 20** (4,036 metal per hour gross, speed ×1)
- Fallow (100 / 210 = 47.6%) with Rising Sap at rank 3: +24%. Giants (over 200 fields): +8%. Three planets of other players in the system with Crowd: 3 × 2 = +6%. Another of your planets in the system with Tides at rank 3: +9%.
- Total **+47%**: 4,036 × 0.47 = **1,896** more metal per hour.
- For 6 h after a raid that took resources, Regrowth adds 20%: +67%, that is **2,704**.

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

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Cold Blood** | key | Your planets' temperature bonuses, cold for hydrogen and heat for solar, are 10% stronger. |  |
| 2 | **Planetary Climate Control** | 3 ranks | On each planet, shift the temperature by 30° toward the cold or the heat, adjustable once a week. | 3 × 10° |
| 3 | **A · Cold Pole** | choice | Your hydrogen synthesizer's cold bonus is 25% stronger still. | |
|  | **B · Hot Pole** |  | The heat bonus of your solar plants and satellites is 25% stronger still. | |
| 4 | **Skin of Light** | 3 ranks | The share of your solar satellites' energy that comes from temperature is 45% stronger. | 3 × 15% |
| 5 | **The Long Season** | key | Your solar plants always produce as at the month's hottest, instead of following the cycle. |  |
| 6 | **A · Deep Roots** | choice | On a planet too hot for it, your hydrogen synthesizer's yield never drops below ×1. | |
|  | **B · Winter Sun** |  | On a cold planet, your solar plants' yield never drops below ×1.25. | |
| 7 | **Reading the Climate** | 3 ranks | Your planets' temperature bonuses are 30% stronger still. | 3 × 10% |
| 8 | **High-Altitude Satellites** | key | Your solar satellites produce as if the planet were 40° hotter. |  |
| 9 | **The Two Seasons** | ultimate | Your hydrogen synthesizer reads the planet's coldest temperature, not its hottest. |  |

- **Cold Blood** and **Reading the Climate** add up (40% at most) and work on the Hydrogen Condenser and the Photovoltaic Sensors, not on Solar Collectors.
- **Planetary Climate Control**: never on a moon. The first setting is immediate; after that each planet waits 7 days between two settings, going back to "no shift" included. The shift applies to the Condenser, the Sensors and the Collectors at once, in the same direction: toward the cold, more hydrogen and less solar energy.
- **Cold Pole** only targets the Condenser (65% amplitude at most with the two nodes above). **Hot Pole** targets the Sensors **and** the Collectors' temperature share.
- **Skin of Light** only touches a Collector's temperature share (maximum temperature / 4), never its 20 base energy.
- **The Long Season**: a planet's temperature follows the month, from its minimum on the 1st to its maximum mid-month. With this node, the Sensors always read the maximum.
- **Deep Roots** raises the Condenser to ×1 wherever it falls under 1 (maximum temperature read above 110 °C). **Winter Sun** raises the Sensors to ×1.25 wherever their factor is lower.
- **High-Altitude Satellites** adds to the Climate Control's shift.
- **The Two Seasons** reads the minimum temperature, 40 °C under the maximum, shift included.

### Growth

*The right place, the right size.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Roots** | key | Each of your planets, homeworld included, gets at least 15% position bonus on its metal and crystal mines, wherever it sits in the system. |  |
| 2 | **Native Soil** | 3 ranks | Your homeworld receives 105% of the bonus of its position in the system. | 3 × 35% |
| 3 | **A · Metal Lode** | choice | The position bonus of your metal mines, mid-system, is 20% stronger still. | |
|  | **B · Crystal Vein** |  | The position bonus of your crystal mines, near the star, is 20% stronger still. | |
| 4 | **Hollowed Moons** | 3 ranks | The position bonus Roots guarantees rises by 15% on the metal and crystal mines of each of your planets. | 3 × 5% |
| 5 | **Layering** | key | Your planets' position bonus is 90% stronger still. |  |
| 6 | **A · Ground Gained** | choice | Each of your planets gains 2 buildable fields. | |
|  | **B · Full Moon** |  | Your moons are no longer bounded by their diameter: each lunar base level gives them all its fields. | |
| 7 | **Living Soil** | 3 ranks | Your terraformer and lunar base cost 24% less. | 3 × 8% |
| 8 | **Living Terraformer** | key | Each terraformer level gives +1 field on top of its 5. |  |
| 9 | **Transplantation** | ultimate | Once a week, move a colony to a free position of its system, buildings and moon included, if no fleet is flying to or from it. |  |

- **Roots** and **Hollowed Moons** set a **floor**: the metal and crystal mines of each of your planets, homeworld included, get at least this position bonus (15%, then 30% at rank 3 of Hollowed Moons), wherever they sit. The floor replaces a weaker bonus, it does not add to it. Moons get none.
- **Layering** and **Metal Lode** or **Crystal Vein** add up, then multiply the position bonus: +110% at most on one mine. Nothing where the position gives nothing, floor aside.
- **Native Soil**: without this node, the homeworld only gets the floor. The share (105% at rank 3) applies to the bonus already widened by the nodes above; the floor is then compared to the result.
- **Ground Gained** only applies to planets, not moons.
- **Living Soil** only targets the Planetary Modulator and the Lunar base; the reduction adds to the other building price reductions, past their common cap.
- **Living Terraformer**: 6 fields per Modulator level instead of 5, and the extra field of even levels stays (Modulator 6: 33 → 39 fields).
- **Transplantation**: once every 7 days for **the whole empire**, never the homeworld. The target position must be free, moonless and outside deep space. Refused while another player's fleet is heading for the colony, while one of your fleets flies to or from it, or in vacation mode. The colony keeps its size and buildings, but takes the temperature and position bonus of its new spot.

### Host

*Make a world live on what it has.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Young Shoot** | key | On a fallow planet, with fewer than 50% of its fields built, your buildings are built 10% faster. |  |
| 2 | **Rising Sap** | 3 ranks | Your fallow planets produce 24% more in their mines. | 3 × 8% |
| 3 | **A · Small Worlds** | choice | On a planet of fewer than 150 fields, your buildings cost 15% less. | |
|  | **B · Giants** |  | On a planet of more than 200 fields, your mines produce 8% more. | |
| 4 | **Long Fallow** | 3 ranks | A planet stays fallow longer: its threshold rises by 30 pts above 50% of its fields built. | 3 × 10 pts |
| 5 | **Neighbourhood** | key | Each planet of another player in the system of one of your planets raises its mines by 1%, up to 8%. |  |
| 6 | **A · Crowd** | choice | Each planet of another player in the system raises your mines by 2%, up to 15%. | |
|  | **B · Solitude** |  | A planet alone in its system, with no other player, produces 10% more in its mines. | |
| 7 | **Tides** | 3 ranks | When several of your planets share a system, each one's mines produce 9% more. | 3 × 3% |
| 8 | **Regrowth** | key | A plundered planet produces 20% more in its mines for the next 6 h. |  |
| 9 | **Eternal Fallow** | ultimate | 1 planet of your choice, homeworld included, stays fallow for good, however many fields are built. Changing it takes 7 days. |  |

- **Young Shoot** counts in the buildings' speed accent. A speed divides the duration: +10% = duration ÷ 1.1.
- **Small Worlds** and **Giants** read the planet's **total** fields, which grow with the Planetary Modulator and bonus fields. The homeworld starts at 163 fields: neither small nor giant. Small Worlds adds to the other building price reductions.
- **Long Fallow** brings the fallow threshold to 60, 70 then 80% of fields built.
- **Neighbourhood** counts every planet of another player in the system, allies and bots included; moons do not count. The count is refreshed regularly, with a short delay.
- **Crowd** **replaces** the rate of Neighbourhood (2% per neighbour instead of 1%, 15% at most instead of 8%): they do not add up. **Solitude** applies when no other player has a planet in the system; your own planets do not prevent it.
- **Tides**: one other planet of yours in the system is enough. The bonus does not grow with their number, and it adds to Neighbourhood, Crowd or Solitude.
- **Regrowth** only triggers if the raid took resources. A new raid restarts the 6 h.
- **Eternal Fallow**: never a moon. The first planet named is fallow at once. Naming another removes the status from the old one at once, and the new one only gets it 7 days later.
- At most, the Host adds +56% to a planet's mines (24 + 8 + 15 + 9), and +20% more for 6 h after a raid.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| The temperature bonuses (cold for hydrogen, heat for solar) gain 40% amplitude | 40% |
| The hydrogen synthesizer's cold bonus gains 25% amplitude | 25% |
| The heat bonus of the solar plant and satellites gains 25% amplitude | 25% |
| The share of solar satellites' energy that comes from temperature gains 45% amplitude | 45% |
| Every planet gets at least 30% position bonus on its metal and crystal mines | 30% |
| The mother planet receives 105% of the position bonus of its place in the system | 105% |
| The metal mines' position bonus gains 20% amplitude | 20% |
| The crystal mines' position bonus gains 20% amplitude | 20% |
| The system position bonus gains 90% amplitude | 90% |
| +4 fields on every planet | 2 |
| −24% terraformer and lunar base cost | 24% |
| −15% building cost on a small world | 15% |

The fields row is completed by the common tree's Surveyors (+2): the class tree only gives 2 of the 4. The Host's bonuses, the Climate Control, the yield floors, the Modulator fields are mechanics bounded to what the tree gives: no point is lost there.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Climatologist | Thermal 15 · Host 10 | The Two Seasons, temperature bonus +40% on both factors and +25% more on one, 30 °C Climate Control, Skin of Light, The Long Season, High-Altitude Satellites; Young Shoot, fallow planets +24%, small worlds or giants, fallow up to 80% of fields, Neighbourhood, Crowd or Solitude |
| Settler | Growth 15 · Thermal 10 | Transplantation, position bonus +90% (+110% on one mine) and at least 30% everywhere, homeworld at 105% of its bonus, Living Soil, Living Terraformer; temperature bonus **+10%** only (+35% on one building with the pole), 30 °C Climate Control, Skin of Light, The Long Season |
| Gardener | Host 15 · Growth 10 | Eternal Fallow, fallow planets +24%, Neighbourhood, Tides, Regrowth; position bonus +90% (+110% on one mine) and at least 30% everywhere, Native Soil, +2 fields or Full Moon |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **A temperature bonus never changes sign**: on a planet too hot for the Hydrogen Condenser (factor under 1), Cold Blood adds nothing, Deep Roots is what raises the floor. Likewise, under 0 °C the Photovoltaic Sensors have no bonus to widen: only Winter Sun helps them.
- **Planetary Climate Control cuts both ways**: toward the cold, the planet gains hydrogen but loses solar energy; toward the heat, the reverse.
- **10 points in Thermal do not give the +40%**: Reading the Climate is in row 7. Without it, the general amplitude stays at 10%.
- **The position bonus only concerns two mines**, and its positions depend on the number of positions in the system: positions 1 to 3 and 6 to 10 in a 15-position system (Redline). On other positions, Layering and Metal Lode or Crystal Vein bring nothing: only the floor of Roots and Hollowed Moons works there.
- **"Fallow" is not "young"**: a colony is young for its first days (common tree); a planet is fallow while its fields are not built enough. Every level built brings it closer to the threshold.
- **Crowd replaces Neighbourhood**, it does not add to it.
- **The total of fields moves**: a Planetary Modulator level or Ground Gained can lose you Small Worlds (going from 149 to 151 fields) or win you Giants.
- **Regrowth needs real loot**: a won raid on an empty stock triggers nothing.
- **Transplantation only works once a week for the whole empire**, and the moved colony changes temperature: its Condenser and Sensors produce differently.
- **Eternal Fallow has no overlap**: when changing planet, the old one loses the status at once and the new one gets it 7 days later.

## Related pages

- [Talents](/en/dynasty/talents)
- [Classes](/en/dynasty/classes)
- [Common tree](/en/dynasty/common-tree)
- [Dynasties](/en/dynasty/dynasties)
- [Planets: size, temperature, type](/en/universe/planets)
- [Energy](/en/economy/energy)
- [The Energetician](/en/dynasty/classes/energist)
