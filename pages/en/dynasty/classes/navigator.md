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
updated: "2026-10-06T10:30:19.530Z"
---

# The Navigator

> **In short**: the Navigator is the master of routes. They decide when their fleets arrive, where they leave from and what they bring back. Generic speed, hydrogen, cargo and fleet slots come from the [common tree](/en/dynasty/common-tree) (Logistics); the Navigator keeps mechanics and two narrow accents. A class open to every dynasty.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

*Motto: "Arrive".*

## Rules

1. The class tree follows the rules shared by every class: 3 branches of 9 rows, 15 points per branch, 25 points at most. See [Talent system](/en/dynasty/talents).
2. The Navigator's **accents**:
   - speed: **+10%** on peaceful missions (Trade Route) or on abandoned targets (Hunting Route), within the talents' speed cap (50%, 60% with the alliance);
   - construction: **+15%** on Cargo Shuttles, Stellar Freighters and Salvagers (Civil Hulls).
3. What only serves your trips between your own planets (Airlift, Stowage) sits **outside the caps** of the common tree.
4. A speed bonus **divides the trip's duration**: +10% = a trip 1.1 times shorter. See [Fleet movement](/en/fleet/movement).

## Worked example

**Afterburner on a 1 h trip home**
- Base rank: the fleet cuts 25% of its remaining time: **1 h → 45 min**.
- With Full Afterburner at rank 3 (40%): **1 h → 36 min**.
- With Reserve Tanks at rank 3, Afterburner comes back every **12 h** instead of 24 h.

**Fuel Hold: 100 Corvettes to another galaxy**
- Distance: 20,000. Corvette consumption: 300. At 100% speed, one way costs 300 × 100 × 20,000 / 35,000 × 4 = **68,571 H**, so **137,143 H** for the round trip.
- Cargo of the 100 Corvettes, without bonuses: 100 × 800 = **80,000**. The fuel does not fit.
- At rank 3 of Fuel Hold, it only takes up 55% of its volume: 137,143 × 0.55 = **75,429**: the fleet can leave.

## Detailed data

### Thrust: "Arrive when you decided to"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Afterburner** | once every 24 h, one of your fleets in flight cuts 25% of its remaining time, never below 5 min (1 h trip home → 45 min) | 25% |
| 2 | 3 ranks | **Reserve Tanks** | Afterburner recharges 4 h sooner per rank: every 12 h at rank 3, twice a day | 3 × 4 h |
| 3 | choice | **A · Trade Route** / **B · Hunting Route** | A: transports, deployments (Stationing) and colonisations 10% faster (accent) <br> B: espionage runs and attacks on abandoned targets 10% faster (accent); a 1 h trip → 54 min 33 s | 10% / 10% |
| 4 | 3 ranks | **Full Afterburner** | +5% of the remaining time cut per rank: 40% at rank 3 (1 h trip home → 36 min) | 3 × 5% |
| 5 | key | **Tight Formation** | in a mixed fleet, slow ships fly 15% faster, never faster than the fastest (Stellar Freighter 7,500 → 8,625 alongside Interceptors at 12,500) | 15% |
| 6 | choice | **A · Relaunch** / **B · Holding Pattern** | A: a fleet sent at reduced speed can go back to 100% in flight, the extra hydrogen paid when it does (a fleet sheltered at 10% for 8 h, relaunched halfway: the remaining 4 h become about 24 min) <br> B: a fleet flying home or on a peaceful mission can slow down in flight to as low as 10%, the hydrogen saved is returned (30 min left become about 5 h) | unlock / unlock |
| 7 | 3 ranks | **Slipstream** | Tight Formation +5% per rank: 30% at rank 3 (Stellar Freighter 7,500 → 9,750) | 3 × 5% |
| 8 | key | **Emergency Takeoff** | once every 24 h, when an attack weighing at least 5% of your docked fleet's power comes at one of your planets (a Scout does not count), the fleet takes off on its own 3 min before impact, to your nearest planet. It comes back at a random time 1 h to 3 h after its takeoff (adjustable window). Attack at 4:12: takeoff at 4:09, back between 5:09 and 7:09 | unlock |
| 9 | ultimate | **Return Jump** | 2 charges per rolling 24 h: a fleet flying home from its mission lands there at once, unloaded like any return | 2 charges |

Afterburner on an outbound attack: the defender's alert is updated with the new arrival time. Relaunch and Holding Pattern never apply to an outbound Attack, Espionage or Moon destruction: a strike never lands at a time the defender cannot see.

### Lines: "All your planets, one single base"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Shuttles** | 2 transports or stationings between your planets no longer take a fleet slot | 2 |
| 2 | 3 ranks | **Fuel Hold** | the trip's fuel takes up 15% less of the hold per rank: 55% of its volume at rank 3 (see the worked example) | 3 × 15% |
| 3 | choice | **A · Fuel on Arrival** / **B · Fuel Returned** | A: the fuel of a transport or stationing between your planets can be paid by the arrival planet; a planet drained of hydrogen can still evacuate its fleet <br> B: a recalled fleet brings back half of the fuel it did not burn (20,000 H paid for the round trip, recalled halfway out: 10,000 H unburnt, 5,000 H returned) | unlock / 50% |
| 4 | 3 ranks | **Hot Gates** | your [Jump gates](/en/fleet/jump-gate) recharge 10% faster per rank: 30% at rank 3 (level 5: 36 min → 25 min 12 s; level 14: 10 min → 7 min) | 3 × 10% |
| 5 | key | **Change of Course** | once every 12 h, a transport, a stationing or a fleet flying home can be redirected to another of your planets or moons in the same system, its arrival time unchanged | 12 h |
| 6 | choice | **A · Double Gate** / **B · Airlift** | A: a Jump gate makes 2 jumps before it recharges <br> B: transports and stationings between your planets burn half the hydrogen (200 Cargo Shuttles to a colony in another galaxy: 9,143 → 4,571 H round trip) | 2 jumps / 50% |
| 7 | 3 ranks | **More Shuttles** | +1 trip between your planets outside the slots per rank: 5 at rank 3 | 3 × 1 |
| 8 | key | **Orbital Lift** | a transport or stationing between a planet and its moon takes 1 min | 1 min |
| 9 | ultimate | **Home Port** | any round trip can come home to another of your planets, chosen at departure; the way back and its fuel follow the real route | unlock |

### Freight: "Bring it all back, lose nothing"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Return Freight** | a transport to one of your planets flies back loaded with a cargo chosen at departure: 20 Stellar Freighters deliver 500,000 metal and bring back 500,000 crystal, one trip instead of two | unlock |
| 2 | 3 ranks | **Stowage** | your transports and stationings between your planets carry 10% more than their holds per rank: +30% at rank 3 (20 Stellar Freighters: 500,000 → 650,000) | 3 × 10% |
| 3 | choice | **A · Grouped Delivery** / **B · Bottomless Holds** | A: a transport can deliver two of your planets in one flight, the second on its way home (50% each, or the split chosen at departure) <br> B: your [expeditions](/en/fleet/expeditions) bring back everything they find, even beyond their holds | unlock / unlock |
| 4 | 3 ranks | **Civil Hulls** | Cargo Shuttles, Stellar Freighters and Salvagers built 5% faster per rank: +15% at rank 3 (accent; 10 h → 8 h 42) | 3 × 5% |
| 5 | key | **False Bottom** | once every 24 h, a fleet leaves with twice its cargo capacity for its whole sortie, there and back (40 Stellar Freighters: 1,000,000 → 2,000,000) | ×2 |
| 6 | choice | **A · False Bottom in Flight** / **B · Shared False Bottom** | A: False Bottom can also be triggered on a fleet already in flight, before it arrives: you see the target before deciding <br> B: False Bottom applies to 2 fleets leaving within 1 min of each other | unlock / 2 fleets |
| 7 | 3 ranks | **Prepared Holds** | False Bottom recharges 4 h sooner per rank: every 12 h at rank 3 | 3 × 4 h |
| 8 | key | **Insured Freight** | if one of your transport fleets is destroyed, half of its cargo goes back to its departure planet; the attacker gains nothing more from it (30 Stellar Freighters carrying 750,000: 375,000 saved) | 50% |
| 9 | ultimate | **Razzia** | once every 24 h, an attack won on an abandoned target carries off everything that can be plundered instead of the usual share (3,000,000 in stock: 1,500,000 at the 50% rate → 3,000,000, within the cargo limit) | 100% |

Razzia only hits abandoned targets (inactive players, ruined worlds, game-controlled opponents), never an active player.

### What 25 points give

| Build | Split | How it feels |
|---|---|---|
| **Runner** | Thrust 15 · Lines 10 | Return Jump, Afterburner twice a day at 40%, Tight Formation at 30%, Emergency Takeoff; 2 shuttles outside the slots, lighter fuel, Change of Course |
| **Empire logistician** | Lines 15 · Freight 10 | Home Port, 5 shuttles outside the slots, Orbital Lift, Airlift or Double Gate; Return Freight, +30% cargo between your planets, Grouped Delivery, False Bottom |
| **Farm raider** | Freight 15 · Thrust 10 | Razzia, False Bottom every 12 h (in flight or on two fleets), Insured Freight; Afterburner, Hunting Route, Tight Formation at 15% |

## Common pitfalls

- **Fuel takes up cargo space**: without Fuel Hold, a distant combat fleet may be unable to leave for lack of cargo.
- **Tight Formation levels speeds out**: every ship except the fastest flies 15% faster, never past the fastest. The fleet still flies at its slowest ship's speed. A fleet of a single type gains nothing.
- **Hunting Route only targets abandoned targets**: an attack on an active player keeps its normal speed.
- **Relaunch and Holding Pattern** do not work on an outbound attack.
- **Shuttles**: only transports and stationings between your own planets are outside the slots.

## Related pages

- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Fleet movement](/en/fleet/movement)
- [Jump gate](/en/fleet/jump-gate)
- [Expeditions](/en/fleet/expeditions)
- [Plunder](/en/combat/plunder)
