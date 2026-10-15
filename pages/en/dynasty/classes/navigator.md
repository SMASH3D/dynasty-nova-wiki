---
wiki_id: 170
locale: "en"
path: "dynasty/classes/navigator"
url: "https://wiki.dynastynova.com/en/dynasty/classes/navigator"
title: "The Navigator"
description: "The Navigator's class tree: Thrust, Lines and Freight."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:18.119Z"
updated: "2026-10-07T22:08:06.524Z"
---

# The Navigator

> **In short**: the Navigator is the master of routes. It decides when its fleets arrive, where they leave from and what they bring back. Generic speed, hydrogen, holds and fleet slots come from the common tree; the Navigator keeps mechanics and two narrow accents.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Navigator is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Thrust, Lines and Freight.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic fleet speed, hydrogen, holds and slots come from the [common tree](/en/dynasty/common-tree). The Navigator only adds two **accents**: +10% speed on Transports, Stationings and Colonizations (Trade Route) or on Attacks and Espionage aimed at an abandoned target (Hunting Route), within the talents' speed cap (50%, 60% with the alliance); +15% build speed for Cargo Shuttles, Stellar Freighters and Salvagers (Civil Hulls).
5. An **abandoned target** is a base with no owner, a base of a game-controlled opponent, or that of a player inactive for the duration set by the universe.
6. Trips **between your own bases** (planets and moons) are the class's own scope: Transport and Stationing for Shuttles, Airlift, Stowage and Orbital Lift. Stowage and Airlift are **outside the common tree's** cargo and hydrogen caps.
7. A flight speed bonus **divides** the trip's duration: +10% makes a trip 1.1 times shorter. Recharge nodes, on the other hand, **take** hours or a percentage off the delay. See [Movement](/en/fleet/movement).
8. In-flight orders (Afterburner, Relaunch, Holding Pattern, Change of Course, Return Jump, False Bottom in Flight) are given from the fleet's details. Cycles count for the whole empire, from the last use.

## Worked example

**Afterburner on a round trip**
- A round-trip Transport, 2 h out. After 1 h of flight, Afterburner cuts 25% of the remaining time: 3,600 s × 0.75 = 2,700 s. The fleet arrives 1 h 45 after leaving.
- The way back lasts as long as the actual way out: 1 h 45. Total **3 h 30** instead of 4 h: cutting 15 min on the way out saves 30.
- With Full Afterburner at rank 3 (40%): 3,600 s × 0.6 = 2,160 s, out 1 h 36, back 1 h 36, total **3 h 12**.

**Fuel Hold: 100 Corvettes to another galaxy**
- Distance: 20,000. A Corvette burns 300. One leg at 100% costs 300 × 100 × 20,000 / 35,000 × 4 = 68,571 H (rounded down), so **137,142 H** for the round trip.
- Hold of the 100 Corvettes, without Hyperspace Technology: 100 × 800 = **80,000**. The fuel does not fit.
- Rank 1 (85% of its volume): 116,571. Rank 2 (70%): 96,000. Rank 3 (55%): 137,142 × 0.55 = **75,429**: the fleet can leave.

**Emergency Takeoff: the 5% threshold**
- Docked: 100 Corvettes costing 29,000 each (20,000 + 7,000 + 2,000), that is 2,900,000. Threshold: 5% = **145,000**.
- 37 Interceptors (4,000 each) = 148,000: the fleet takes off. 36 Interceptors (144,000): it stays.
- The refuge planet is 40 min away; the return is drawn at 1 h. The fleet never comes back faster than it left: it lands 40 min + 40 min = **1 h 20** after taking off.

**Tight Formation and Slipstream: Stellar Freighters and Corvettes to another galaxy** (universe fleet speed ×1, as on Redline; no drive research)
- Without the node, the fleet flies at the Stellar Freighter's speed, 7,500: 10 + 3,500 × √(10 × 20,000 / 7,500) = 18,084 s, that is **5 h 01 min 24 s**.
- Tight Formation (15%): 8,625, that is **4 h 41 min 04 s**. With Slipstream at rank 3 (30%): 9,750, that is **4 h 24 min 22 s**. Hydrogen does not change.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FREIGHT<br/>Bring it all back, lose nothing."]:::head
        B3R1{{"Return Freight<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Stowage<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Grouped Delivery<br/>1 pt"]:::option
        B3R3B["② Bottomless Holds<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Civil Hulls<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"False Bottom<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① False Bottom in Flight<br/>1 pt"]:::option
        B3R6B["② Shared False Bottom<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Prepared Holds<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Insured Freight<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Razzia<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["LINES<br/>All your planets, one single base."]:::head
        B2R1{{"Shuttles<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Fuel Hold<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Fuel on Arrival<br/>1 pt"]:::option
        B2R3B["② Fuel Returned<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Hot Gates<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Change of Course<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Double Gate<br/>1 pt"]:::option
        B2R6B["② Airlift<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("More Shuttles<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Orbital Lift<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Home Port<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["THRUST<br/>Arrive when you decided to."]:::head
        B1R1{{"Afterburner<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Reserve Tanks<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Trade Route<br/>1 pt"]:::option
        B1R3B["② Hunting Route<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Full Afterburner<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Tight Formation<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Relaunch<br/>1 pt"]:::option
        B1R6B["② Holding Pattern<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Slipstream<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Emergency Takeoff<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Return Jump<br/>ultimate"]]:::ultimate
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

### Thrust

*Arrive when you decided to.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Afterburner** | key | Once a day, one of your fleets in flight cuts 25% of its remaining trip, never below 5 min. |  |
| 2 | **Reserve Tanks** | 3 ranks | Afterburner recharges 12 h sooner. | 3 × 4 h |
| 3 | **A · Trade Route** | choice | Your transports, deployments and colonisations go 10% faster. | |
|  | **B · Hunting Route** |  | Your espionage runs and attacks on abandoned targets go 10% faster. | |
| 4 | **Full Afterburner** | 3 ranks | Afterburner cuts 15% more of the remaining trip. | 3 × 5% |
| 5 | **Tight Formation** | key | In a mixed fleet, your slow ships fly 15% faster, never faster than the fastest. |  |
| 6 | **A · Relaunch** | choice | A fleet sent at reduced speed can go back to full speed in flight; the extra hydrogen is paid when it does. | |
|  | **B · Holding Pattern** |  | A fleet flying home or on a peaceful mission can slow down in flight to as low as 10% of its speed; the hydrogen saved comes back to you. | |
| 7 | **Slipstream** | 3 ranks | Tight Formation gains 15% more. | 3 × 5% |
| 8 | **Emergency Takeoff** | key | Once a day, when an attack weighing at least 5% of your docked fleet comes at one of your planets, the fleet takes off on its own 3 min before impact, to your nearest planet. It comes back at random 1 h to 3 h later, a window you can set. |  |
| 9 | **Return Jump** | ultimate | 2 charges per rolling 24 h: a fleet flying home from its mission lands there at once, unloaded like any return. |  |

- **Afterburner**: on a fleet flying out or home, refused with 5 min or less left; the remaining time is rounded up to the second. On a round trip, the way back takes the shortened outbound duration (except with Home Port, Grouped Delivery or a speed changed in flight). On an Attack, the defender's alert follows the new impact time.
- **Reserve Tanks** takes 4 h per rank off the 24 h cycle: 12 h at rank 3.
- **Trade Route** and **Hunting Route** take the 10% speed accent; they add to at most 40% from the common tree.
- **Tight Formation**: the slowest ship counts 15% faster (30% with Slipstream), never past the fleet's fastest, drive research included. A single-type fleet gains nothing. Duration follows the square root of speed: +30% speed shortens the flight by about 12%.
- **Relaunch**: only up to 100%. The remaining time is multiplied by the old speed / 100 (on a round trip flying out, the way back too); the extra hydrogen is taken from the base.
- **Holding Pattern**: down to 10% at the lowest; the hydrogen saved goes back into the fleet's hold.
- Neither Relaunch nor Holding Pattern applies to an Attack, Espionage, Moon destruction or Expedition on its way out; both apply to any return.
- **Emergency Takeoff**: the threat is measured by the ships' total cost (metal, crystal, hydrogen), Solar Collectors excluded; a Scout counts like any other ship. The fleet leaves as a Transport at 100%, with no resources, for your nearest other planet (never a moon, nor the planet of the same cell), up to 3 min before impact. Nothing leaves if you have no other planet or if the base lacks the flight's hydrogen. The return window can be set between 15 min and 24 h; a return never flies faster than the way out, so it may land after the window when the refuge planet is far.
- **Return Jump**: any fleet flying home, whatever its mission. Each charge comes back 24 h after it was used.

### Lines

*All your planets, one single base.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Shuttles** | key | 2 transports or deployments between your planets no longer take a fleet slot. |  |
| 2 | **Fuel Hold** | 3 ranks | The trip's fuel takes up 45% less of its volume in your holds. | 3 × 15 pts |
| 3 | **A · Fuel on Arrival** | choice | The fuel of a transport or deployment between your planets can be paid by the arrival planet: a planet drained of hydrogen can still evacuate its fleet. | |
|  | **B · Fuel Returned** |  | A recalled fleet brings back 50% of the fuel it did not burn. | |
| 4 | **Hot Gates** | 3 ranks | Your jump gates recharge 30% faster. | 3 × 10% |
| 5 | **Change of Course** | key | Once every 12 h, a transport, a deployment or a fleet flying home can be redirected to another of your planets or moons in the same system, its arrival time unchanged. |  |
| 6 | **A · Double Gate** | choice | A jump gate makes 2 jumps before it recharges. | |
|  | **B · Airlift** |  | Transports and deployments between your planets burn 50% less hydrogen. | |
| 7 | **More Shuttles** | 3 ranks | +3 shuttles: trips between your planets that take no fleet slot. | 3 × 1 |
| 8 | **Orbital Lift** | key | A transport or deployment between a planet and its moon takes 1 min. |  |
| 9 | **Home Port** | ultimate | Any round trip can come home to another of your planets, chosen at departure; the way back and its fuel follow the real route. |  |

- **Shuttles** and **More Shuttles**: a Transport or Stationing to one of your bases leaves outside the slots while a shuttle is free. The shuttle stays taken until the fleet is back. 5 shuttles at most.
- **Fuel Hold**: the fuel's volume is rounded up.
- **Fuel on Arrival**: the arrival base pays all of the flight's hydrogen, round trip included; the departure base only pays the cargo.
- **Fuel Returned**: on recall, the way back already owed counts as burned. 20,000 H paid for the round trip, recalled halfway out: 10,000 H unburned, 5,000 H returned into the hold.
- **Hot Gates** **cuts** the recharge by 10% per rank (×0.7 at rank 3), it does not divide it: level 5, 36 min → 25 min 12 s; level 14, 10 min → 7 min.
- **Change of Course**: a Transport or Stationing flying out, or any fleet flying home, whose destination is yours. The new base must be in the same system and have an Orbital Dock if the fleet lands there (return or stationing).
- **Airlift** multiplies with the common tree's and the alliance's hydrogen reductions.
- **Orbital Lift**: a fixed 1 min, whatever the chosen speed or the universe's.
- **Home Port**: the home base (planet or moon) must have an Orbital Dock. The way back flies the real distance and pays its hydrogen, without the bonuses of trips between your bases.

### Freight

*Bring it all back, lose nothing.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Return Freight** | key | A transport to one of your planets flies back loaded with a cargo chosen at departure: one trip instead of two. |  |
| 2 | **Stowage** | 3 ranks | Your transports and deployments between your planets carry 30% more than their holds. | 3 × 10% |
| 3 | **A · Grouped Delivery** | choice | A transport can deliver two of your planets in one flight, the second on its way home: 50% each, or the split chosen at departure. | |
|  | **B · Bottomless Holds** |  | Your expeditions bring back everything they find, even beyond their holds. | |
| 4 | **Civil Hulls** | 3 ranks | Your transporters and recyclers are built 15% faster. | 3 × 5% |
| 5 | **False Bottom** | key | Once a day, a fleet leaves with twice its cargo capacity for its whole sortie, there and back. |  |
| 6 | **A · False Bottom in Flight** | choice | False Bottom can also be triggered on a fleet already in flight, before it arrives: you see the target before deciding. | |
|  | **B · Shared False Bottom** |  | False Bottom applies to 2 fleets leaving within 1 min of each other. | |
| 7 | **Prepared Holds** | 3 ranks | False Bottom recharges 12 h sooner. | 3 × 4 h |
| 8 | **Insured Freight** | key | If one of your transport fleets is destroyed, 50% of its cargo goes back to its departure planet; the attacker gains nothing more from it. |  |
| 9 | **Razzia** | ultimate | Once a day, an attack won on an abandoned target carries off 100% of what can be plundered, instead of the usual share. |  |

- **Return Freight**: Transport only (not Stationing). The requested cargo must fit in the hold when sending; it is loaded within the arrival base's stock.
- **Stowage** adds to the common tree's cargo bonus: up to +55% between your bases.
- **Grouped Delivery**: the first base gets 50% of the cargo, or the share chosen between 1 and 99%. The flight pays its three legs. It combines with neither Return Freight nor Home Port.
- **Bottomless Holds**: only concerns the resource finds of [expeditions](/en/fleet/expeditions).
- **Civil Hulls** adds to the common tree's unit build speed: a 10 h Stellar Freighter builds in 8 h 41 min 45 s (÷ 1.15).
- **False Bottom** is requested when sending: the doubled hold serves everything the fleet loads (plunder, debris, finds, freight). The cycle starts from the first fleet.
- **Shared False Bottom**: the second fleet must leave at most 1 min after the first.
- **Insured Freight**: works when one of your fleets is entirely destroyed in combat during its own Attack (Second Wave included) or a Moon destruction. Half of what it carried, rounded down resource by resource, goes back to its departure base.
- **Razzia**: the charge is spent on the **first** won attack against an abandoned target in the cycle, with no choice. The defender's shelters apply, then the holds' limit. 3,000,000 in stock: 1,500,000 at the usual 50% rate, 3,000,000 with Razzia, within the holds' limit.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| +10% speed on transports, deployments and colonisations | 10% |
| +10% speed on espionage runs and attacks on abandoned targets | 10% |
| +30% speed for a fleet's slowest ships, never past its fastest ship | 30% |
| 2 return jump charges: a fleet returning from its mission arrives home instantly | 2 |
| −45 pts on the share of its volume the trip's fuel takes up in the hold | 45 pts |
| A recalled fleet brings 50% of its unburnt fuel back to its base | 50% |
| +30% jump gate recharge speed | 30% |
| −50% hydrogen for transports and deployments between your planets | 50% |
| +30% load for transports and deployments between your planets | 30% |
| +15% transporter and recycler construction speed | 15% |
| Boosted cargo capacity: ×2 | ×2 |
| 50% of the cargo of a destroyed transport fleet goes back to its departure planet | 50% |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Runner | Thrust 15 · Lines 10 | Return Jump, Afterburner at 40% every 12 h, a route at +10%, Tight Formation at 30%, Relaunch or Holding Pattern, Emergency Takeoff; 2 shuttles, fuel at 55% of its volume, Fuel on Arrival or Fuel Returned, Hot Gates, Change of Course, Double Gate or Airlift |
| Empire Logistician | Lines 15 · Freight 10 | Home Port, 5 shuttles, Orbital Lift, Change of Course, Double Gate or Airlift; Return Freight, +30% load between your bases, Grouped Delivery or Bottomless Holds, Civil Hulls, False Bottom once per 24 h |
| Farm Raider | Freight 15 · Thrust 10 | Razzia, False Bottom every 12 h (False Bottom in Flight or Shared False Bottom), Insured Freight; Afterburner at 40% every 12 h, Hunting Route, Tight Formation at 15% |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Fuel takes up hold space**: without Fuel Hold, a distant combat fleet may be unable to leave for lack of hold.
- **Tight Formation only looks at the slowest ship**: the fleet flies at the slowest speed raised by 15% (30%), never past the fastest. A single-type fleet does not benefit.
- **Afterburner on the way out counts twice** on a round trip: the way back takes the shortened outbound duration.
- **Hunting Route only targets abandoned targets**: an attack on an active player keeps its normal speed.
- **Relaunch and Holding Pattern** do not work on an Attack, Espionage, Moon destruction or Expedition on its way out.
- **Emergency Takeoff only takes the ships**: resources stay on the planet. Without another planet or without the flight's hydrogen, the fleet does not leave.
- **Insured Freight does not protect a convoy**: it only works when your fleet is wiped out during its own attack or a Moon destruction.
- **Razzia fires on its own** on the first victory against an abandoned target, even a nearly empty one.
- **Shuttles**: only Transports and Stationings to your own bases are outside the slots.
- **Grouped Delivery, Return Freight and Home Port do not combine** on the same send.

## Related pages

- [Talents](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Movement](/en/fleet/movement)
- [Jump gate](/en/fleet/jump-gate)
- [Expeditions](/en/fleet/expeditions)
- [Plunder](/en/combat/plunder)
