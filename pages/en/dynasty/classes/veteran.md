---
wiki_id: 175
locale: "en"
path: "dynasty/classes/veteran"
url: "https://wiki.dynastynova.com/en/dynasty/classes/veteran"
title: "The Veteran"
description: "The Heritage's defensive class: Rampart, Relief and Silo."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:29.753Z"
updated: "2026-10-06T10:30:31.218Z"
---

# The Veteran

> **In short**: the Veteran does not win battles, it makes every attack against them costly for the attacker and nearly free for themselves. All of the combat sits in Rampart; Relief brings fallen defenses back; Silo answers with missiles. Exclusive to The Heritage.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Veteran is **exclusive to [The Heritage](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Rampart, Relief and Silo.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6. Points, gates and choices are explained on [Talents](/en/dynasty/talents).
4. A Veteran starts with a **75%** chance of free repair for their defenses instead of 70%, thanks to The Heritage's Nothing Is Lost trait. Relief talents raise this rate up to its ceiling of **85%**.
5. Generic defense build speed comes from the [common tree](/en/dynasty/common-tree). The Veteran only adds narrow accents: defense and missile build speed (15% at most for both), and protection against plunder (15 points at most, common tree included).

## Worked example

**An attack destroys 100 Ballistic Projectors**
- Without talents, a Veteran has a 75% chance to keep each one: **75** come back on average, 25 are lost (50,000 metal).
- With Stretcher-Bearers and Field Workshops at rank 3 (85%): **85** come back on average, 15 are lost, i.e. 30,000 metal.
- With Rebuilding Fund, Salvaged Gear and War Chest (50%): **15,000 metal** is given back. The real loss drops to 15,000 metal.

**Gun Layers at rank 3**
- A Ballistic Projector has 80 base attack. With +9%: 80 × 1.09 = **87.2**, before research bonuses.

**Underground Shelter**
- Plunder suffered drops from 50% to **40%**. With the common tree's Buried Vaults: **35%**, the lowest a Veteran can reach (15 points of protection at most). With 2,000,000 metal in stock, the attacker takes 700,000 instead of 1,000,000.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["SILO<br/>What answers back."]:::head
        B3R1{{"Deep Pits<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Shaped Charge<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Casemates<br/>1 pt"]:::option
        B3R3B["② Long Reach<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Recovered Interceptors<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Counter-Salvo<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Automatic Riposte<br/>1 pt"]:::option
        B3R6B["② Mass Production<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Impulse Reach<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Lunar Silo<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Steel Rain<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["RELIEF<br/>What comes back."]:::head
        B2R1{{"Stretcher-Bearers<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Rebuilding Fund<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Under Fire<br/>1 pt"]:::option
        B2R3B["② Quick Stretchers<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Field Workshops<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Salvaged Gear<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Express Rebuild<br/>1 pt"]:::option
        B2R6B["② Reservists Recalled<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("War Chest<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Domes First<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Line Reformed<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["RAMPART<br/>What stays standing."]:::head
        B1R1{{"Reinforced Concrete<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Gun Layers<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Heavy Pieces<br/>1 pt"]:::option
        B1R3B["② Light Curtain<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Counter-Battery<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Battle Stations<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Underground Shelter<br/>1 pt"]:::option
        B1R6B["② War Prize<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Front Rank<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"The Moon Holds<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Last Salvo<br/>ultimate"]]:::ultimate
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

### Rampart

*What stays standing.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Reinforced Concrete** | Your defenses' shields are stronger. | 1 rank | +5% |
| 2 | **Gun Layers** | Your defenses deal more damage. | 3 × 3% | +9% |
| 3 | **A · Heavy Pieces** or **B · Light Curtain** | A: your Magnetic Accelerators, Ion Batteries and Plasma Ejectors gain 10% hull. <br> B: your Ballistic Projectors and Photonic Cannons destroyed in battle are always repaired. | 1 rank | A: +10% <br> B: unlock |
| 4 | **Counter-Battery** | Your defenses deal more damage to ships that have rapid fire against them. | 3 × 2% | +6% |
| 5 | **Battle Stations** | While an attack is on its way to one of your planets, its defenses build faster: the attacker's spy report ages during the flight. | 1 rank | ×2 |
| 6 | **A · Underground Shelter** or **B · War Prize** | A: the loot rate you suffer drops by 10 points (accent). <br> B: after a won defense, 20% of the enemy fleet's debris drops straight into your depots. | 1 rank | A: −10 pts <br> B: 20% |
| 7 | **Front Rank** | In the first round, while the enemy fleet is still whole, your defenses deal more damage. | 3 × 3% | +9% |
| 8 | **The Moon Holds** | The chance of destroying your moons is multiplied by 0.75 (27% → 20%). | 1 rank | −25% |
| 9 | **Last Salvo** *(ultimate)* | If a battle ends in a draw, your defenses fire one more salvo on their own before the attacker leaves. | 1 rank | 1 salvo |

### Relief

*What comes back.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Stretcher-Bearers** | The free repair of your defenses gains points. | 1 rank | +4 pts (79%) |
| 2 | **Rebuilding Fund** | A defense lost for good gives back a share of what it cost, on its planet. | 3 × 5% | 15% |
| 3 | **A · Under Fire** or **B · Quick Stretchers** | A: 20% of the defenses destroyed by a Long-Range Warheads strike are rebuilt for free. <br> B: your defenses build 15% faster (accent). | 1 rank | A: 20% <br> B: +15% |
| 4 | **Field Workshops** | The free repair of your defenses gains more points, up to its ceiling of 85%. | 3 × 2 pts | +6 pts (85%) |
| 5 | **Salvaged Gear** | A defense lost for good gives back another share of what it cost. | 1 rank | +20% (35%) |
| 6 | **A · Express Rebuild** or **B · Reservists Recalled** | A: for 24 h after a battle, the defenses lost for good rebuild 50% faster. <br> B: each attack suffered moves the planet's defense queue 1 h forward at once. | 1 rank | A: +50% <br> B: 1 h |
| 7 | **War Chest** | Your defenses lost for good give back a further share of what they cost. | 3 × 5% | +15% (50%) |
| 8 | **Domes First** | Your Defensive Barrier and Protective Dome destroyed in battle are always repaired. | 1 rank | unlock |
| 9 | **Line Reformed** *(ultimate)* | For 6 h after an attack suffered on a planet, any defense a new attack destroys there is repaired: the second wave hits an intact line. | 1 rank | 6 h |

### Silo

*What answers back.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Deep Pits** | Your Ballistic Arsenal holds more missiles. | 1 rank | +5% |
| 2 | **Shaped Charge** | Your Long-Range Warheads deal more damage. | 3 × 3% | +9% |
| 3 | **A · Casemates** or **B · Long Reach** | A: your Ballistic Arsenal holds a further 10% more missiles. <br> B: your missiles reach 2 more systems. | 1 rank | A: +10% <br> B: +2 systems |
| 4 | **Recovered Interceptors** | An Interception Missile that downs a warhead has a chance to stay in the Arsenal. | 3 × 5% | 15% |
| 5 | **Counter-Salvo** | For 24 h, the base that struck one of your planets is within range of your missiles, even in another galaxy. | 1 rank | 24 h |
| 6 | **A · Automatic Riposte** or **B · Mass Production** | A: when a strike hits one of your planets, it fires back at once at the base of origin as many warheads as it received, up to 10, taken only from those you mark as the riposte reserve. <br> B: your missiles build 15% faster (accent). | 1 rank | A: 10 warheads <br> B: +15% |
| 7 | **Impulse Reach** | Your missiles reach further. | 3 × 1 system | +3 systems |
| 8 | **Lunar Silo** | You can build a Ballistic Arsenal on your moons and launch your missiles from them. | 1 rank | unlock |
| 9 | **Steel Rain** *(ultimate)* | A salvo of at least 20 warheads cannot be intercepted. Once per rolling 24 h: the next one is possible 24 h after the previous one. | 1 rank | 1 / 24 h |

Class caps: Arsenal capacity +15%, missile range +5 systems, warhead damage +9%.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Fortress | Rampart 15 · Relief 10 | Last Salvo, Battle Stations, defenses +9% damage and +5% shields, Front Rank; repair at 85%, 35% back on losses |
| Unbreakable | Relief 15 · Silo 10 | Line Reformed against the second wave, Domes First, 50% back on losses; Arsenal +15%, Recovered Interceptors, Counter-Salvo |
| Artillerist | Silo 15 · Rampart 10 | Steel Rain, Lunar Silo, Automatic Riposte or Mass Production, range +3 to +5 systems; Gun Layers and Battle Stations |

## Common pitfalls

- **Repair is still a roll**: 85% is a chance per defense, not a guaranteed share of the batch (see [Defense rebuild](/en/combat/defense-rebuild)).
- **Long-Range Warheads strikes** always destroy for good. Only Under Fire gives 20% back.
- An Admiral's **Scorched Earth** takes 15 points off your repair against them: at 85%, you keep 70%.
- **Automatic Riposte never empties your Arsenal**: only the warheads marked as the riposte reserve fire. With no reserve, nothing fires.
- **Plunder never goes below 30%**, whatever the protection sources.

## Related pages

- [Talents](/en/dynasty/talents)
- [Classes](/en/dynasty/classes)
- [Common tree](/en/dynasty/common-tree)
- [Dynasties](/en/dynasty/dynasties)
- [Defenses list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Defense rebuild](/en/combat/defense-rebuild)
- [Plunder](/en/combat/plunder)
- [Moon destruction](/en/combat/moon-destruction)
