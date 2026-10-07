---
wiki_id: 166
locale: "en"
path: "dynasty/classes/admiral"
url: "https://wiki.dynastynova.com/en/dynasty/classes/admiral"
title: "The Admiral"
description: "The head-on combat class: Firing Line, Campaign and Spoils of War."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:08.859Z"
updated: "2026-10-06T10:30:10.470Z"
---

# The Admiral

> **In short**: the Admiral is the head-on combat class. It does not change the ships you build, but what they are worth once they face the enemy. All of the combat sits in the Firing Line branch; Campaign leaves fast, chains attacks and comes home sooner; Spoils of War brings more back from every battle.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Admiral is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Firing Line, Campaign and Spoils of War.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6. Points, gates and choices are explained on [Talents](/en/dynasty/talents).
4. Generic fleet speed, hydrogen and cargo come from the [common tree](/en/dynasty/common-tree). The Admiral only adds narrow accents: attack, espionage and moon destruction missions, combat ships' hydrogen and build speed, and one fleet kept for attacks.
5. **Combat ships** are every non-civil ship except the Solar Collector: Interceptor, Assailant, Corvette, Battleship, Orbital Striker, Predator, Annihilator and Stellar Colossus.

## Worked example

**Tuned Guns at rank 3**
- A Corvette has 400 base attack. With +9%: 400 × 1.09 = **436**, before research bonuses.

**Towing, Repair Station level 4 on Redline**
- The Station recovers 35% in defense. In attack, Towing applies 20% of it: 35% × 20% = **7%**.
- 30 Corvettes lost: 30 × 7% = 2.1, so **2 Corvettes**, with a 10% chance of a third.
- With Tugs at rank 3 (50%): 35% × 50% = 17.5%, i.e. 5.25: **5 Corvettes**, with a 25% chance of a sixth.

**Breakthrough**
- A draw plunders at 10% of the normal rate: 50% × 10% = **5%** of the stock. With 2,000,000 metal in stock, you take **100,000** (within your cargo space).

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["SPOILS OF WAR<br/>What you bring back from a battle."]:::head
        B3R1{{"Towing<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Tugs<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Nobody in Orbit<br/>1 pt"]:::option
        B3R3B["② Breakthrough<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Dry Dock<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Combat Recycling<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Emergency Repair<br/>1 pt"]:::option
        B3R6B["② Fast Recyclers<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Refining<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Breaking Yard<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Raptors<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["CAMPAIGN<br/>Leave fast, strike, come home."]:::head
        B2R1{{"Forced March<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Refuel on the Enemy<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Fast Escort<br/>1 pt"]:::option
        B2R3B["② War Economy<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Victorious Return<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Assault Squadron<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Orderly Recall<br/>1 pt"]:::option
        B2R6B["② Supply Line<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("War Yard<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Scorched Earth<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Second Wave<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["FIRING LINE<br/>What your fleet is worth on contact."]:::head
        B1R1{{"Plating<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Tuned Guns<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Fire Doctrine<br/>1 pt"]:::option
        B1R3B["② Hull Doctrine<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Volleys<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Master of Cadence<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Siege Volley<br/>1 pt"]:::option
        B1R6B["② Countermeasures<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Read the Hull<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Moonbreaker<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Focused Fire<br/>ultimate"]]:::ultimate
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

### Firing Line

*What your fleet is worth on contact.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Plating** | Your ships' shields are stronger. | 1 rank | +3% |
| 2 | **Tuned Guns** | Your ships deal more damage. | 3 × 3% | +9% |
| 3 | **A · Fire Doctrine** or **B · Hull Doctrine** | A: your defenses get half of your ships' weapons bonus. <br> B: your ships' bonus moves from their weapons to their hull, and their hull gains another 2%. | 1 rank | A: 50% <br> B: +2% |
| 4 | **Volleys** | Your rapid fires against the ships you counter chain more shots. | 3 × 3% | +9% |
| 5 | **Master of Cadence** | Designate a ship type: its rapid fires of 10 or more go up by 1. | 1 rank | +1 |
| 6 | **A · Siege Volley** or **B · Countermeasures** | A: your rapid fires against defenses chain 10% more shots. <br> B: you take 10% less damage from the units that counter you. | 1 rank | 10% |
| 7 | **Read the Hull** | Your shots deal more damage to the units you counter. | 3 × 3.5% | +10.5% |
| 8 | **Moonbreaker** | When you destroy a moon, the risk of losing your ships is multiplied by 0.75. | 1 rank | −25% |
| 9 | **Focused Fire** *(ultimate)* | Before an attack, designate an enemy unit type: every shot you fire at it deals more damage. | 1 rank | +7.5% |

Class caps: ship weapons 9%, hull 11%, shields 3%.

### Campaign

*Leave fast, strike, come home.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Forced March** | Your attacks, espionage runs and moon destructions go faster (speed accent). | 1 rank | +10% |
| 2 | **Refuel on the Enemy** | A won attack gives you back a share of the hydrogen burnt on the way out. | 3 × 10% | 30% |
| 3 | **A · Fast Escort** or **B · War Economy** | A: in an attack fleet, your transporters fly 25% faster, never past the fastest ship. <br> B: your combat ships burn 5% less hydrogen (accent). | 1 rank | A: +25% <br> B: −5% |
| 4 | **Victorious Return** | After a won attack, your fleet comes home faster. Outside the speed budget. | 3 × 10% | +30% |
| 5 | **Assault Squadron** | One more fleet in flight, kept for attacks. | 1 rank | +1 |
| 6 | **A · Orderly Recall** or **B · Supply Line** | A: a recalled fleet comes home 20% faster. <br> B: a lost or drawn attack gives you back 15% of the hydrogen burnt on the way out. | 1 rank | A: +20% <br> B: 15% |
| 7 | **War Yard** | Your combat ships are built faster (accent). | 3 × 5% | +15% |
| 8 | **Scorched Earth** | The defenses you destroy have 15 points less chance of a free repair (70% usually). | 1 rank | −15 pts |
| 9 | **Second Wave** *(ultimate)* | A fleet that has just won an attack flies on once to another target, 1 system away at most, without coming home. | 1 rank | 1 rebound |

### Spoils of War

*What you bring back from a battle.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Towing** | The Repair Station of the departure planet recovers the ships lost in attack, at a share of its efficiency. | 1 rank | 20% |
| 2 | **Tugs** | Towing gains efficiency. | 3 × 10% | 50% with Towing |
| 3 | **A · Nobody in Orbit** or **B · Breakthrough** | A: towing works even when your whole fleet is destroyed. <br> B: an attack that ends in a draw still plunders, at 10% of the normal loot rate. | 1 rank | A: unlock <br> B: 10% |
| 4 | **Dry Dock** | Your Repair Station repairs your ships faster. | 3 × 8% | +24% |
| 5 | **Combat Recycling** | The Salvagers sent with an attack pick up the debris field as soon as the fight ends. | 1 rank | unlock |
| 6 | **A · Emergency Repair** or **B · Fast Recyclers** | A: the Repair Station's shortest repair takes 15 min less (30 min usually). <br> B: your recycling missions go 10% faster (accent). | 1 rank | A: −15 min <br> B: +10% |
| 7 | **Refining** | Every debris harvest also brings you a share of its tonnage in hydrogen. | 3 × 4% | 12% |
| 8 | **Breaking Yard** | Your Repair Station recovers your ships lost in defense with more efficiency: its share is multiplied by 1.2. | 1 rank | ×1.2 |
| 9 | **Raptors** *(ultimate)* | After a won attack, your combat ships load a share of the debris into their free holds, after the loot. | 1 rank | 30% |

Towing uses **probabilistic rounding**: the decimal part becomes a chance of one more ship, so a small raid brings ships back too.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Fleet hunter | Firing Line 15 · Campaign 10 | Focused Fire, weapons +9%, volleys, Read the Hull; Forced March, hydrogen back on won attacks, victorious return, one more attack fleet |
| Raider | Campaign 15 · Spoils of War 10 | Second Wave, 30% of the hydrogen back per won attack, War Yard; towing up to 50%, faster repairs, combat recycling |
| Battlefield looter | Spoils of War 15 · Firing Line 10 | Raptors, towing, refining, Breaking Yard; weapons +9% and volleys |

## Common pitfalls

- **Focused Fire is set before departure**: the target unit type is chosen in the send form. Spy first.
- **Second Wave does not go far**: the second target must be 1 system away at most from the first.
- **No Repair Station, no towing**: the Station of the departure planet does the towing. Without Nobody in Orbit, a fleet wiped out brings nothing back.
- **Victorious Return does not count toward the speed cap**, but Forced March does: it uses the class's 10% speed accent.
- **Scorched Earth** also hits a Veteran: their defense repair loses 15 points against you.

## Related pages

- [Talents](/en/dynasty/talents)
- [Classes](/en/dynasty/classes)
- [Common tree](/en/dynasty/common-tree)
- [Dynasties](/en/dynasty/dynasties)
- [Rapid fire](/en/fleet/rapid-fire)
- [Plunder](/en/combat/plunder)
- [Debris fields](/en/combat/debris)
- [Repair Station](/en/economy/repair-station)
- [Defense rebuild](/en/combat/defense-rebuild)
- [Moon destruction](/en/combat/moon-destruction)
