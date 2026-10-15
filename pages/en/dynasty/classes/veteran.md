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
updated: "2026-10-07T22:08:14.085Z"
---

# The Veteran

> **In short**: the Veteran does not win battles, it makes every attack on it cost the attacker dearly and itself next to nothing. All the combat lies in Rampart; Relief brings fallen defences back and refunds the others; Silo answers with missiles. Class exclusive to The Heritage.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Veteran is a class **exclusive to [The Heritage](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Rampart, Relief and Silo.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. A Veteran starts with a **75%** chance of free repair for each destroyed defence instead of 70%, thanks to The Heritage's Nothing Is Lost trait. Stretcher-Bearers and Field Workshops raise this rate up to its ceiling of **85%**. The repair stays a roll per defence.
5. Generic defence build speed comes from the [common tree](/en/dynasty/common-tree). The Veteran only adds narrow **accents**: defence and missile build speed (Quick Stretchers, Mass Production), **15% at most for both together**, and protection against plunder (Underground Shelter), **15 points at most**, the common tree's Buried Vaults included.
6. Rampart's stat bonuses apply **after** research and multiply with it. Your defences' shield and hull also count against missile strikes: Reinforced Concrete and Heavy Pieces make them harder to destroy. Damage bonuses (Counter-Battery, Front Rank) only work for your defences, when you are attacked, and multiply with each other.

## Worked example

**An attack destroys 100 Ballistic Projectors** (2,000 metal each)
- Without talents, each has a 75% chance to come back: **75** come back on average, 25 are lost, that is 50,000 metal.
- With Stretcher-Bearers and Field Workshops at rank 3 (85%): **85** come back on average, 15 are lost, that is 30,000 metal.
- With Rebuilding Fund, Salvaged Gear and War Chest (50%): **15,000 metal** is given back. The real loss drops to 15,000 metal.
- With Light Curtain, all 100 come back.

**Gun Layers at rank 3**
- A Ballistic Projector has 80 weapons. Weapon Systems level 10: 80 × 2 = 160. With +9%: 160 × 1.09 = 174.4, rounded down to **174**.

**Deep Pits and Casemates, Ballistic Arsenal level 10**
- 10 slots per level: 100 slots, that is 50 Long-Range Warheads (2 slots each).
- With +35%: 100 × 1.35 = 135 slots, that is **67 warheads**.
- With Shaped Charge at rank 3 and Weapon Systems level 10, a warhead deals 12,000 × 2 × 1.09 = **26,160** damage.

**Underground Shelter**
- Plunder suffered drops from 50% to **40%**. With the common tree's Buried Vaults: **35%**, the lowest a Veteran can reach. With 2,000,000 metal in stock, the attacker takes 700,000 instead of 1,000,000.

**War Prize** (universe with 30% ship debris, like Redline)
- The attacker loses 100 Corvettes (20,000 metal and 7,000 crystal each) and you win. Debris: 600,000 metal and 210,000 crystal. **120,000 metal and 42,000 crystal** drop into your stores; the rest stays in the field.

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

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Reinforced Concrete** | key | Your defenses' shields are 5% stronger. |  |
| 2 | **Gun Layers** | 3 ranks | Your defenses deal 9% more damage. | 3 × 3% |
| 3 | **A · Heavy Pieces** | choice | Your magnetic accelerators, ion batteries and plasma ejectors gain 10% hull. | |
|  | **B · Light Curtain** |  | Your ballistic projectors and photonic cannons destroyed in battle are always repaired. | |
| 4 | **Counter-Battery** | 3 ranks | Your defenses deal 6% more damage to ships that have rapid fire against them. | 3 × 2% |
| 5 | **Battle Stations** | key | While an attack is on its way to one of your planets, its defenses build twice as fast: the attacker's spy report ages during the flight. |  |
| 6 | **A · Underground Shelter** | choice | The loot rate you suffer drops by 10 points. | |
|  | **B · War Prize** |  | After a won defense, 20% of the enemy fleet's debris drops straight into your stores. | |
| 7 | **Front Rank** | 3 ranks | In the first round, while the enemy fleet is still whole, your defenses deal 9% more damage. | 3 × 3% |
| 8 | **The Moon Holds** | key | The chance of destroying your moons drops by 25%. |  |
| 9 | **Last Salvo** | ultimate | If a battle ends in a draw, your defenses fire 1 more salvo on their own before the attacker leaves: an undecided raid turns costly. |  |

- **Heavy Pieces** only affects the Magnetic Accelerator, Ion Battery and Plasma Ejector.
- **Light Curtain** and **Domes First** always repair, even against Scorched Earth, but only after a battle: nothing against missiles.
- **Counter-Battery** works against every ship that has rapid fire against the firing defence.
- **Battle Stations** applies to attacks and moon destructions aimed at this base. A defence order never gains more than half of its remaining time.
- **War Prize**: only on a won defence; the resources go past your storage capacity and are taken out of the debris field.
- **Front Rank** works in the first round of every battle, against every target.
- **The Moon Holds** multiplies the chance of destroying the moon by 0.75: a 100% chance drops to 75%.
- **Last Salvo**: only your defences fire this salvo, not your ships. If it finishes the enemy fleet, the battle becomes a defence victory.

### Relief

*What comes back.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Stretcher-Bearers** | key | The free repair of your defenses after a battle gains 4 points. |  |
| 2 | **Rebuilding Fund** | 3 ranks | A defense lost for good gives back 15% of what it cost, on its planet. | 3 × 5% |
| 3 | **A · Under Fire** | choice | 20% of the defenses destroyed by a missile strike are rebuilt for free. | |
|  | **B · Quick Stretchers** |  | Your defenses build 15% faster. | |
| 4 | **Field Workshops** | 3 ranks | The free repair of your defenses gains another 6 points, up to its ceiling of 85%. | 3 × 2 pts |
| 5 | **Salvaged Gear** | key | A defense lost for good gives back another 20% of what it cost. |  |
| 6 | **A · Express Rebuild** | choice | For 24 h after a battle, the defenses lost for good rebuild 50% faster. | |
|  | **B · Reservists Recalled** |  | Each attack suffered moves the planet's defense queue 1 h forward at once. | |
| 7 | **War Chest** | 3 ranks | Your defenses lost for good give back a further 15% of what they cost. | 3 × 5% |
| 8 | **Domes First** | key | Your Defensive Barrier and Protective Dome destroyed in battle are always repaired. |  |
| 9 | **Line Reformed** | ultimate | For 6 h after an attack suffered on a planet, any defense a new attack destroys there is repaired: the second wave hits an intact line. |  |

- **Rebuilding Fund**, **Salvaged Gear** and **War Chest** add up (50% at most). They give back the price paid (metal, crystal and hydrogen), on the planet, even past its storage. Only for defences lost in battle: a defence destroyed by a missile is not refunded.
- **Under Fire** is a chance per destroyed defence, not a guaranteed share.
- **Express Rebuild**: defence orders started within 24 h build faster, for as many units of each type as you lost. A new loss adds its units and restarts the 24 h.
- **Reservists Recalled** only moves the running defence order forward, never past its end.
- **Line Reformed**: the window opens on every attack suffered outside a window. An attack landing inside it does not extend it. An Admiral's Scorched Earth still takes its 15 points off: 85% repair instead of 100%.

### Silo

*What answers back.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Deep Pits** | key | Your missile silo holds 5% more missiles. |  |
| 2 | **Shaped Charge** | 3 ranks | Your warheads deal 9% more damage. | 3 × 3% |
| 3 | **A · Casemates** | choice | Your missile silo holds a further 30% more missiles. | |
|  | **B · Long Reach** |  | Your missiles reach 2 more systems. | |
| 4 | **Recovered Interceptors** | 3 ranks | An interceptor that downs a warhead has a 15% chance to stay in the silo. | 3 × 5% |
| 5 | **Counter-Salvo** | key | For 24 h, the base that struck one of your planets is within range of your missiles, even in another galaxy. |  |
| 6 | **A · Automatic Riposte** | choice | When a strike hits one of your planets, it fires back at once at the base of origin as many warheads as it received, up to 10, taken only from those you mark as the riposte reserve: the rest of the silo is never emptied. | |
|  | **B · Mass Production** |  | Your missiles build 15% faster. | |
| 7 | **Impulse Reach** | 3 ranks | Your missiles reach a further 3 systems. | 3 × 1 |
| 8 | **Lunar Silo** | key | You can build a Ballistic Arsenal on your moons and launch your missiles from them. |  |
| 9 | **Steel Rain** | ultimate | Once a day, a salvo of at least 20 warheads cannot be intercepted. |  |

- **Deep Pits** and **Casemates** add up: +35% slots, rounded down. An Interception Missile takes 1 slot, a Long-Range Warhead 2.
- **Long Reach** and **Impulse Reach** add up (5 systems at most) on the base range, Impulse Drive level × 5 − 1. Never outside the galaxy, except against a base targeted by Counter-Salvo.
- **Recovered Interceptors** is a chance per Interception Missile that downs a warhead.
- **Counter-Salvo**: the base the salvo came from is within range of all your bases for 24 h.
- **Automatic Riposte**: the riposte reserve is marked base by base. A struck base with no marked warheads does not answer. A riposte never triggers a riposte in return.
- **Mass Production** shares Quick Stretchers's 15% cap: with both, your missiles build no faster.
- **Steel Rain** is declared at launch, for a salvo of at least 20 warheads, once per rolling 24 h for your whole empire. No level is required.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| +5% defense shield | 5% |
| +9% defense weapons | 9% |
| +10% hull on magnetic accelerators, ion batteries and plasma ejectors | 10% |
| +6% defense damage against ships with rapid fire against them | 6% |
| −15 pts on the loot rate you suffer | 10 pts |
| +9% defense damage in the first round | 9% |
| −25% chance of your moons being destroyed | 25% |
| +15 pts free defense repair after a battle | 10 pts |
| A defense lost for good in battle gives back 50% of what it cost | 50% |
| +15% defense construction speed | 15% |
| +35% silo capacity | 35% |
| +9% warhead yield | 9% |
| +5 systems of missile range | 5 |

Two caps are shared: the build speed of Quick Stretchers and Mass Production fits in a single 15% accent, and the protection of Underground Shelter in 15 points with Buried Vaults. Free repair stops at 85%: a 75% start and 10 talent points just reach it.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Fortress | Rampart 15 · Relief 10 | Last Salvo, Battle Stations, defences +9% damage and +5% shield, Counter-Battery, Front Rank, The Moon Holds; repair at 85%, 35% back on losses |
| Unbreakable | Relief 15 · Silo 10 | Line Reformed, Domes First, repair at 85%, 50% back on losses; Arsenal +35% with Casemates (or range +2 with Long Reach), warheads +9%, Recovered Interceptors, Counter-Salvo |
| Artillerist | Silo 15 · Rampart 10 | Steel Rain, Lunar Silo, Automatic Riposte or Mass Production, range +3 to +5 systems; Reinforced Concrete, Gun Layers, Counter-Battery, Battle Stations |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Repair is still a roll**: 85% is a chance per defence, not a guaranteed share of the batch (see [Defense rebuild](/en/combat/defense-rebuild)).
- **Missile strikes are neither repaired nor refunded**: only Under Fire gives each destroyed defence a chance to come back. Light Curtain, Domes First, Line Reformed and Relief's refunds only work after a battle.
- **Quick Stretchers and Mass Production do not stack** on missiles: a single 15% accent.
- **An Admiral's Scorched Earth** takes 15 points off your repair against them: at 85%, you are left with 70%.
- **Automatic Riposte never empties your Ballistic Arsenal**: only the warheads marked as "riposte reserve" on the struck base leave. Without a reserve, nothing leaves.
- **Reservists Recalled only moves the running order**: with no defence in production, it does nothing.
- **Plunder never goes below 30%**, but a Veteran does not go below 35%: its protection is capped at 15 points.

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
