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
updated: "2026-10-07T22:08:00.206Z"
---

# The Admiral

> **In short**: the Admiral is the head-on combat class. It does not change the ships you build, but what they are worth once facing the enemy. All the combat lies in the Firing Line branch; Campaign leaves fast, chains raids and comes home sooner; Spoils of War brings more back from every battle.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Admiral is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Firing Line, Campaign and Spoils of War.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic fleet speed, hydrogen and holds come from the [common tree](/en/dynasty/common-tree). The Admiral only adds narrow **accents**: the speed of attacks, espionage and moon destruction (Forced March) and of recycling (Fast Recyclers), combat ships' hydrogen and build speed, and a fleet reserved for attacks.
5. **Combat ships** are the Interceptor, Assailant, Corvette, Battleship, Orbital Striker, Predator, Annihilator and Stellar Colossus. Civil ships (Cargo Shuttle, Stellar Freighter, Salvager, Scout, Space Pioneer) and the Solar Collector are not.
6. Stat bonuses apply **after** research and multiply with it. They work in attack as in defence. Damage bonuses on a pair (Read the Hull, Focused Fire) multiply with each other.

## Worked example

**Tuned Guns and Hull Doctrine, on a Corvette**
- Base weapons 400, Offensive Systems level 10: 400 × 2 = 800. With Tuned Guns at rank 3: 800 × 1.09 = **872**.
- With Hull Doctrine, the 9% moves to the hull and adds to the node's 4%: hull +13%, weapons 800 with no bonus.

**Towing and Tugs (50%), Repair Station level 10, 30% debris**
- Station share: 54% × (1 − 30%) = 37.8%. Towing: 37.8% × 50% = **18.9%**.
- 30 Corvettes lost in attack: 30 × 18.9% = 5.67, that is **5 Corvettes**, and a 67% chance of a sixth.
- The same 30 Corvettes lost in defence, with Breaking Yard: 54% × 1.2 × 70% = 45.36%, that is **13** Corvettes (11 without the node).

**Breakthrough**
- A draw plunders at 30% of a victory's rate: 50% × 30% = **15%** of the stock. On 2,000,000 metal, you take **300,000**, within your holds' limit.

**Moonbreaker**
- Against an 8,944 km moon, the risk of losing your fleet is √8,944 / 2 = 47.29%; with the node: 47.29% × 0.75 = **35.47%**. The chance of destroying the moon does not change.

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

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Plating** | key | Your ships' shields are 3% stronger. |  |
| 2 | **Tuned Guns** | 3 ranks | Your ships deal 9% more damage. | 3 × 3% |
| 3 | **A · Fire Doctrine** | choice | Your defenses get 50% of your ships' weapons bonus. | |
|  | **B · Hull Doctrine** |  | Your ships' bonus moves from their weapons to their hull, and their hull gains another 4%. | |
| 4 | **Volleys** | 3 ranks | Your rapid fires against the ships you counter chain 9% more shots. | 3 × 3% |
| 5 | **Master of Cadence** | key | Designate a ship type: its strongest rapid fires go up by 1. |  |
| 6 | **A · Siege Volley** | choice | Your rapid fires against defenses chain 10% more shots. | |
|  | **B · Countermeasures** |  | You take 10% less damage from the units that counter you. | |
| 7 | **Read the Hull** | 3 ranks | Your shots deal 10.5% more damage to the units you counter. | 3 × 3.5% |
| 8 | **Moonbreaker** | key | When you destroy a moon, the risk of losing your ships drops by 25%. |  |
| 9 | **Focused Fire** | ultimate | Before an attack, designate an enemy unit type: every shot you fire at it deals 7.5% more damage. |  |

- **Fire Doctrine**: your defences get half of your ships' weapons bonus, that is +4.5% with Tuned Guns at rank 3. It only helps when you are attacked.
- **Hull Doctrine**: Tuned Guns no longer gives weapons, its points go to the hull.
- **Volleys** and **Siege Volley** lengthen your ships' rapid fire chains (against ships, against defences).
- **Master of Cadence**: in the Abilities tab, you designate one type among the Corvette, Orbital Striker, Annihilator and Stellar Colossus. It **does not add** to Volleys or Siege Volley: each rapid fire takes the better of the two.
- **Countermeasures** protects your ships and defences, in attack as in defence. All sources together, this reduction never exceeds 15%.
- **Read the Hull** works on every pair where the shooter has rapid fire against its target. The Accord's Tuning Fork adds 5% past the cap.
- **Focused Fire** is set when sending an Attack mission (not a moon destruction). It does not work when you are attacked.

### Campaign

*Leave fast, strike, come home.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Forced March** | key | Your attacks, espionage runs and destructions go 10% faster. |  |
| 2 | **Refuel on the Enemy** | 3 ranks | A won attack gives you back 30% of the hydrogen burnt on the way out. | 3 × 10% |
| 3 | **A · Fast Escort** | choice | In an attack fleet, your transporters fly 25% faster, never past the fastest ship. | |
|  | **B · War Economy** |  | Your combat ships burn 10% less hydrogen. | |
| 4 | **Victorious Return** | 3 ranks | After a won attack, your fleet comes home 30% faster. | 3 × 10% |
| 5 | **Assault Squadron** | key | You can have 1 more fleet in flight, kept for attacks. |  |
| 6 | **A · Orderly Recall** | choice | A recalled fleet comes home 20% faster. | |
|  | **B · Supply Line** |  | A lost or drawn attack gives you back 15% of the hydrogen burnt on the way out. | |
| 7 | **War Yard** | 3 ranks | Your combat ships are built 15% faster. | 3 × 5% |
| 8 | **Scorched Earth** | key | The defenses you destroy have 15 pts less chance of a free repair (70% usually). |  |
| 9 | **Second Wave** | ultimate | A fleet that has just won an attack flies on 1 time to another target, 1 system away at most, without coming home. |  |

- **Refuel on the Enemy** gives back part of the outbound hydrogen on a won attack whose fleet survives. It is loaded outside capacity and delivered on return.
- **Fast Escort** speeds up the Cargo Shuttles and Stellar Freighters of an Attack mission, never past the fastest ship. **War Economy** cuts the share of hydrogen burned by your combat ships: a fleet where they burn half the fuel saves 5%.
- **Assault Squadron** only serves the Attack mission (neither espionage nor moon destruction).
- **Supply Line**: a defeat destroys the whole fleet, so there is nothing to give back; in practice, it only works on a draw.
- **Scorched Earth** applies to your attacks and your moon destructions.
- **Second Wave**: when sending, you name a second target, a planet of another player or an abandoned one, in the same galaxy, at most 1 system from the first. If the attack is won and the fleet survives, it leaves for it at once, once per flight, taking the jump's hydrogen from its holds. Truce, alliance, vacation mode, protections and the attack limit are checked at the time of the jump: if refused, the fleet goes home.

### Spoils of War

*What you bring back from a battle.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Towing** | key | Your dock recovers the ships lost in attack at 20% of its efficiency. |  |
| 2 | **Tugs** | 3 ranks | Towing your ships lost in attack gains 30% efficiency. | 3 × 10% |
| 3 | **A · Nobody in Orbit** | choice | Towing works even when your whole fleet is destroyed. | |
|  | **B · Breakthrough** |  | An attack that ends in a draw still plunders, at 30% of the normal loot rate. | |
| 4 | **Dry Dock** | 3 ranks | Your dock repairs your ships 24% faster. | 3 × 8% |
| 5 | **Combat Recycling** | key | The recyclers sent with an attack pick up the debris as soon as the fight ends. |  |
| 6 | **A · Emergency Repair** | choice | The dock's shortest repair takes 15 min less (30 min usually). | |
|  | **B · Fast Recyclers** |  | Your recycling missions go 10% faster. | |
| 7 | **Refining** | 3 ranks | Every debris harvest also brings you 12% of its tonnage in hydrogen. | 3 × 4% |
| 8 | **Breaking Yard** | key | Your dock recovers your ships lost in defense with 20% more efficiency. |  |
| 9 | **Raptors** | ultimate | After a won attack, your combat ships load 30% of the debris into their free holds, after the loot. |  |

- **Towing**: the Repair Station of the departure planet does the towing. A moon has no Station: a fleet leaving from a moon tows nothing. Towing uses **probabilistic rounding**: the decimal part becomes a chance of one more ship.
- **Breakthrough**: 30% of a victory's plunder rate, the defender's shelters deducted.
- **Dry Dock** speeds up every Station repair; a repair stays between 30 min (15 min with Emergency Repair) and 12 h.
- **Combat Recycling**: the attack fleet's Salvagers collect this battle's debris, after plunder.
- **Refining** only adds hydrogen in the space left in the holds.
- **Breaking Yard** only works in defence, not on towing.
- **Raptors**: after a won attack, your combat ships load 30% of the battle's debris into their free holds, after plunder and the Salvagers.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| +3% ship shield | 3% |
| +9% to ship weapons, or to their hull under the hull doctrine | 9% |
| Your defenses get 50% of your ships' arsenal bonus on their weapons | 50% |
| +13% ship hull, under the hull doctrine only | 4% |
| +9% rapid fire chain against ships | 9% |
| +1 to the strongest rapid fires of one designated ship type | 1 |
| +10% rapid fire chain against defenses | 10% |
| −10% damage taken from enemy shots that have a rapid fire against your units | 10% |
| +15% counter damage, on the units the shooter has a rapid fire against | 10.5% |
| −25% risk of losing your ships during a moon destruction | 25% |
| +10% speed on attacks, espionage and destructions | 10% |
| A won attack gives back 30% of the hydrogen burnt to reach the target | 30% |
| +25% speed for an attack fleet's transporters, never past the fastest ship | 25% |
| −10% hydrogen consumption of combat ships | 10% |
| +30% speed on the way home from a won attack | 30% |
| +1 fleet slot kept for attacks | 1 |
| +20% speed on a recalled fleet's way back | 20% |
| A lost or drawn attack gives back 15% of the hydrogen burnt to reach the target | 15% |
| +15% build speed of combat ships | 15% |
| −15 pts free repair of the defenses you destroy | 15 pts |
| Ships lost in attack are recovered at 50% of the home base's repair dock rate | 50% |
| A drawn attack plunders at 30% of a won attack's rate | 30% |
| +24% dock repair speed | 24% |
| −15 min off the dock's shortest repair time | 15 min |
| +10% fleet speed on recycling missions | 10% |
| A debris harvest also yields hydrogen worth 12% of the tonnage harvested | 12% |
| +20% dock recovery factor | 20% |
| After a won attack, your combat ships load 30% of the debris | 30% |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Fleet Hunter | Firing Line 15 · Campaign 10 | Focused Fire, weapons +9% (or hull +13%), shield +3%, Volleys, Read the Hull; Forced March, hydrogen back on victories, victorious return, one more attack fleet |
| Raider | Campaign 15 · Spoils of War 10 | Second Wave, War Yard, Scorched Earth; towing up to 50%, Nobody in Orbit or Breakthrough, faster repairs, combat recycling |
| Battle Looter | Spoils of War 15 · Firing Line 10 | Raptors, towing, Refining, Breaking Yard; weapons +9%, shield +3%, Volleys, Master of Cadence |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Focused Fire is set before leaving**: the targeted unit type is designated in the sending form. Spy first.
- **Hull Doctrine removes the weapons bonus**: with it, Tuned Guns no longer gives any damage.
- **Master of Cadence may add nothing**: with Volleys at rank 3 and Siege Volley, every rapid fire is already better served.
- **Second Wave does not go far**: the second target must be at most 1 system from the first, and the fleet pays the jump with the hydrogen in its holds.
- **No Repair Station, no towing**: a fleet leaving from a moon tows nothing. Without Nobody in Orbit, a fleet wiped out gives nothing back.
- **Victorious Return does not count toward the speed cap**, but Forced March does: it takes the class's 10% speed accent.
- **Scorched Earth also hits a Veteran**: their defence repair loses 15 points against you.

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
