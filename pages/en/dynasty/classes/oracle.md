---
wiki_id: 171
locale: "en"
path: "dynasty/classes/oracle"
url: "https://wiki.dynastynova.com/en/dynasty/classes/oracle"
title: "The Oracle"
description: "The foreknowledge class, exclusive to The Accord: Watch, Omen and Forewarning."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:20.508Z"
updated: "2026-10-07T22:08:07.934Z"
---

# The Oracle

> **In short**: the Oracle does not hit harder, it knows first. Each of its branches sells information, never a statistic: Watch sees fleets move from a moon, Omen prepares raids, Forewarning keeps you away when the blow lands.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Oracle is a class **exclusive to [The Accord](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Watch, Omen and Forewarning.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. Generic plunder protection and fleet return speed come from the [common tree](/en/dynasty/common-tree). The Oracle only adds two narrow **accents**: Prepared Strike (attack speed, within the class's 10% speed accent) and The Cache (plunder protection, 10 points at most with Buried Vaults). Tracking spies belongs to the [Shadow](/en/dynasty/classes/shadow).
5. With no talent, only an **Attack** mission is announced, **60 s** before impact, or as soon as it leaves if the flight is shorter. A fleet's lead is set **when it leaves**, from your talents at that moment; a fleet sped up in flight keeps the same lead on its new impact time. In the time gained before the 60 s, the alert only gives the targeted base and the arrival time to the minute; the exact time and the origin come at 60 s, except with Exact Hour. The alert never gives the fleet's composition.
6. The [Sensor phalanx](/en/espionage/sensor-phalanx) is built on a moon and never targets a moon. A sweep costs 5,000 hydrogen, except the one from Reflex Sweep, and is impossible in vacation mode. It only shows **movements** (fleets leaving or reaching the planet), never parked ships, nor espionage and recycling missions. By default, nobody is told of a sweep: only the Shadow, with Light at Your Back, learns of it.
7. Omen's readings start from **your** espionage reports. The plunderable share is computed at your plunder rate (50% on Redline, plus your talents against an abandoned target), **without** the defender's protection, which the report does not show: it is a maximum.

## Worked example

**Alert lead by Forewarning talents**

| Talents taken | Lead before impact |
|---|---|
| none | 1 min |
| Keen Ear | 2 min 30 |
| + Guard Tower at rank 3 | 3 min 30 |
| + Night Watchmen at rank 3 | 4 min 30 |
| + The Great Forewarning (full branch) | 6 min |

An attack whose flight lasts 75 s is announced when it leaves, 75 s before impact: Forewarned Guard, which needs 90 s, does not work.

**Sensor phalanx level 3 with Long Sight and Lenses at rank 3**
- Reach: the phalanx reaches like a level 4, that is 4² − 1 = **15 systems** on each side, instead of 8.
- Cost of a sweep: 5,000 × (1 − 0.24) = **3,800 hydrogen**.
- With Empire View, a player with 3 planets in reach is swept entirely for 3,800 hydrogen instead of 11,400.
- With Moon Relay and another moon in system 70, a level 4 phalanx in system 40 (reach of a level 5: 24 systems) sweeps the planets of systems 16 to 64 **and** 46 to 94 of the same galaxy.

**Weighing**: the report reads 1,200,000 metal, 800,000 crystal and 300,000 hydrogen. At 50%, the plunderable share is 600,000 + 400,000 + 150,000 = **1,150,000**.
- Without Hyperspace Technology: 1,150,000 / 25,000 = **46 Stellar Freighters**, or 1,150,000 / 5,000 = **230 Cargo Shuttles**.
- Hyperspace Technology level 5 (+25% hold): a Stellar Freighter carries 31,250, it takes 36.8, rounded up to **37**; a Cargo Shuttle carries 6,250, it takes **184**.
- Adding Wider Holds (+10%): 34,375 per Stellar Freighter, that is **34**.

**Headcount**: the alert rounds the fleet's value (its ships' cost in metal, crystal and hydrogen) to the nearest multiple of half its power of ten.
- 200 Battleships (60,000 each) and 50 Stellar Freighters (12,000 each): 12,600,000, shown as **15,000,000**.
- 1,200 Interceptors (4,000 each): 4,800,000, shown as **5,000,000**.

**The Cache**: 2,000,000 resources in stock. A winning raid takes 50% with no talent, that is 1,000,000; with The Cache, 45%, that is **900,000**; adding Buried Vaults, 40%, that is **800,000**.

**Prepared Strike**: a 60 min trip with no other speed bonus lasts 60 / 1.09, about **55 min 3 s**, if the attack leaves at most 30 min after your last report on the target.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FOREWARNING<br/>Not to be there when the blow lands."]:::head
        B3R1{{"Keen Ear<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Forewarned Guard<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Enemy Gauge<br/>1 pt"]:::option
        B3R3B["② Exact Hour<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Guard Tower<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"The Colossus Foretold<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Headcount<br/>1 pt"]:::option
        B3R6B["② Flash Retreat<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Night Watchmen<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"The Cache<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ The Great Forewarning<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["OMEN<br/>Know before you strike."]:::head
        B2R1{{"Weighing<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Farm Ledger<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Measuring the Gap<br/>1 pt"]:::option
        B2R3B["② Reading the Rankings<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Raid's Eye<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Foreseen Loot<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Farm Round<br/>1 pt"]:::option
        B2R6B["② Hunt Balance<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Prepared Strike<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"The Clash Foretold<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ The Raid Plan<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["WATCH<br/>See the fleets move."]:::head
        B1R1{{"Long Sight<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Lenses<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Shared Watch<br/>1 pt"]:::option
        B1R3B["② Moon and Planet<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Phalanx Memory<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"The Return Foretold<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Silent Sweep<br/>1 pt"]:::option
        B1R6B["② Moon Relay<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Lingering Gaze<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Empire View<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Reflex Sweep<br/>ultimate"]]:::ultimate
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

### Watch

*See the fleets move.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Long Sight** | key | Your phalanx reaches as if it had 1 more level: it covers more systems. |  |
| 2 | **Lenses** | 3 ranks | Your phalanx sweeps cost 24% less hydrogen. | 3 × 8% |
| 3 | **A · Shared Watch** | choice | Each of your phalanx sweeps is handed to your whole alliance. | |
|  | **B · Moon and Planet** |  | A sweep also shows the fleets leaving or reaching the planet's moon, where players park their fleet out of harm's way. | |
| 4 | **Phalanx Memory** | 3 ranks | The fleets a sweep saw stay tracked, with their arrival time, for 3 h after the sweep ends. | 3 × 1 h |
| 5 | **The Return Foretold** | key | An announced attack also tells you when the enemy fleet will be back home: you know how long its port stays empty. |  |
| 6 | **A · Silent Sweep** | choice | Your sweeps are never announced to the swept planet, whatever talents its owner holds. | |
|  | **B · Moon Relay** |  | A planet in reach of any of your moons can be swept from your phalanx moon. | |
| 7 | **Lingering Gaze** | 3 ranks | A sweep stays open for 30 min: fleets leaving or reaching the planet meanwhile are added to its reading. | 3 × 10 min |
| 8 | **Empire View** | key | A sweep also shows the fleets of every other planet of the same player in reach, for the price of one. |  |
| 9 | **Reflex Sweep** | ultimate | When an attack against you is announced, one of your moons in reach sweeps the planet it left from for free: you see what stays there and what comes back. |  |

- **Long Sight** only works on a phalanx already built: (level + 1)² − 1 systems.
- **Shared Watch**: the other members of your alliance get a notification with what the sweep saw. Nothing without an alliance.
- **Moon and Planet** applies to all your sweeps, those of Lingering Gaze, Empire View and Reflex Sweep included.
- **Phalanx Memory** follows the fleets live, return trip included, up to 3 h after the sweep ends (after it closes, for a sweep left open).
- **The Return Foretold** is alert information: it works without a moon. The time given assumes the fleet flies straight home; a faster return may bring it back sooner.
- **Silent Sweep** only matters against a player holding Light at Your Back: without it, no sweep is reported.
- **Moon Relay**: your phalanx's reach is also measured from each of your other moons, even without a phalanx.
- **Lingering Gaze** never opens on your own planet.
- **Empire View** adds the player's other **planets** in reach of the phalanx moon (or the relays); no effect on your own planets.
- **Reflex Sweep**: the sweep comes from your nearest moon whose phalanx reaches the departure planet, relays included. That moon needs a phalanx built. The reading shows that planet's movements at the moment you read the alert.

### Omen

*Know before you strike.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Weighing** | key | Every espionage report shows how many cargo ships it takes to carry off the plunderable share. |  |
| 2 | **Farm Ledger** | 3 ranks | You follow 15 targets. The game projects their stock from your last two reports and tells you when the plunderable share reaches the threshold you set. | 3 × 5 |
| 3 | **A · Measuring the Gap** | choice | The report says how many probes it takes to read the next tier: no more blind waves. | |
|  | **B · Reading the Rankings** |  | A report too short for the simulator gets a defence outlook (probably empty, unknown, dangerous) instead of a refusal. | |
| 4 | **Raid's Eye** | 3 ranks | Your attack battle reports read the target as a probe would, over 3 tiers: first the stock left after the plunder, then the buildings, then the research your probes could have read. | 3 × 1 |
| 5 | **Foreseen Loot** | key | The simulator also gives the expected loot, at most: the plunderable share capped by your surviving ships' holds. |  |
| 6 | **A · Farm Round** | choice | Pick up to 5 farms: the game shares your cargo ships between them by their plunderable share and prepares the sends. | |
|  | **B · Hunt Balance** |  | The simulator gives the expected debris field and the net gain over your losses. | |
| 7 | **Prepared Strike** | 3 ranks | An attack launched less than 30 min after your report on the target flies 9% faster. | 3 × 3% |
| 8 | **The Clash Foretold** | key | An attack against you gets a verdict, hold or fall, drawn from the public military rankings; simulated against the real fleet when your forewarning measures its power. |  |
| 9 | **The Raid Plan** | ultimate | From a report that read the fleet, the game suggests the smallest fleet, taken from the base of your choice, that wins at least 9 simulated fights out of 10 and carries off the whole plunderable share. |  |

- **Weighing** counts the holds of your Cargo Shuttles and Stellar Freighters with your Hyperspace Technology and your hold talents, rounded up.
- **Farm Ledger**: a target is a planet or a moon, with a threshold on the total plunderable share. The stock is carried forward at the pace measured between your last two reports, with no storage cap; a resource that went down counts as 0. One notification per report. The node also gives this projection on every report. After a reset that leaves fewer slots, only the first targets count.
- **Measuring the Gap** relies on what your previous waves on that body proved.
- **Reading the Rankings** shows on the report's reading; the simulator still refuses a report that did not read the fleet. "Dangerous": the owner has more public military points than you. "Probably empty": the stock read is under 10,000 and you have at least 1.2 times their military points. "Unknown" otherwise.
- **Raid's Eye**: research only shows at rank 3 if your Scouts could read it on that defender. Never the fleet or the defences.
- **Foreseen Loot** and **Hunt Balance** give averages over the simulated fights.
- **Farm Round** shares the Stellar Freighters and Cargo Shuttles of **one** chosen base; a farm whose report did not read the stock is left out. You launch the sends.
- **Prepared Strike**: Attack mission only, not a moon destruction; your most recent report on that very body (planet or moon) is the one that counts. Speed divides the duration.
- **The Clash Foretold**: three verdicts, hold, fall or unknown. Without Headcount, "fall" if the attacker has more public military points than you, "unknown" if a ranking is missing. With Headcount, 20 simulated fights against the real fleet and your current defence, Forewarned Guard included: "hold" if the attacker wins fewer than half. Only the verdict is shown.
- **The Raid Plan** looks for the smallest share, in twentieths, of the chosen base's whole combat fleet (every type kept), then adds that base's Stellar Freighters and Cargo Shuttles, within what is stationed there. Without research read in the report, the defender is assumed at your levels. If the whole combat fleet is not enough, no plan is offered.

### Forewarning

*Not to be there when the blow lands.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Keen Ear** | key | Attacks against you are announced 90 s earlier, on top of the 60 s of forewarning the game gives everyone. |  |
| 2 | **Forewarned Guard** | 3 ranks | If the forewarning came at least 90 s before impact, the planet's defences and ships gain 6% shield and 6% damage, against attacks only. | 3 × 2% |
| 3 | **A · Enemy Gauge** | choice | The forewarning gives the size of the enemy fleet (small, medium, large, overwhelming), to decide whether to hold or flee. | |
|  | **B · Exact Hour** |  | From its very first second, the forewarning gives the exact arrival time and the origin, to leave at the last second. | |
| 4 | **Guard Tower** | 3 ranks | Your attack forewarnings gain another 60 s. | 3 × 20 s |
| 5 | **The Colossus Foretold** | key | Moon destructions aimed at your moons are announced like attacks, with the same forewarning. |  |
| 6 | **A · Headcount** | choice | The forewarning gives the power of the enemy fleet within 25%, never its ships. | |
|  | **B · Flash Retreat** |  | A fleet leaving a planet targeted by an announced attack flies 20% faster and burns 50% less hydrogen. | |
| 7 | **Night Watchmen** | 3 ranks | Your attack forewarnings gain 60 s. | 3 × 20 s |
| 8 | **The Cache** | key | The plunder you suffer drops by 5 points: a share of every resource stays out of the raiders' reach. |  |
| 9 | **The Great Forewarning** | ultimate | Your attack forewarnings gain another 90 s: the alert comes well before impact. |  |

- **Forewarned Guard**: +2% shield and +2% damage per rank, for the parked ships and defences of the attacked base, if the alert for **that** attack really came 90 s before impact. The attacker does not see it in their simulator.
- **Enemy Gauge**: small under 100,000 of value (ships' cost in resources), medium under 1,000,000, large under 10,000,000, overwhelming beyond.
- **The Colossus Foretold**: without this node, a moon destruction is not announced at all.
- **Headcount**: the gap between the value shown and the real one never exceeds 20% of the real one. Taken with Enemy Gauge, the estimate is what shows.
- **Flash Retreat**: any fleet, whatever its mission, leaving the targeted body (planet or moon) while an attack **already announced** is flying at it. Its speed and reduction apply after every other bonus, outside the caps.
- **The Cache** applies to all your bases; the plunder rate never drops below 30%.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| The phalanx reaches as if it had +1 level | 1 |
| −24% hydrogen cost of a phalanx sweep | 24% |
| A phalanx sweep stays open for 30 min: fleets leaving or heading for the swept planet are added to it | 30 min |
| +9% speed for an attack launched soon after your report on the target | 9% |
| +300 s of forewarning before an attack lands | 300 s |
| +20% speed for a fleet leaving a world an announced attack is still flying at, whatever its mission | 20% |
| −50% hydrogen consumption for that fleet, over the whole trip | 50% |
| −10 pts on the loot rate you suffer | 5 pts |

The plunder row is completed by the common tree's Buried Vaults (5 points): 10 points in all, the rate you suffer drops from 50 to 40%. The alert lead adds to the 60 s the game gives everyone: 360 s, that is 6 min, at most.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Sentinel | Forewarning 15 · Watch 10 | alert 6 min before impact, The Cache, guard +6% shield and damage, Enemy Gauge or Exact Hour, The Colossus Foretold, Headcount or Flash Retreat; phalanx +1 level at 3,800 hydrogen, Shared Watch or Moon and Planet, 3 h memory, The Return Foretold, Silent Sweep or Moon Relay |
| Augur | Omen 15 · Forewarning 10 | The Raid Plan, The Clash Foretold, Prepared Strike, Foreseen Loot, 15-target ledger, Raid's Eye; alert 3 min 30 before impact, guard +6%, The Colossus Foretold, Headcount (which makes The Clash Foretold simulate) or Flash Retreat |
| Lookout | Watch 15 · Omen 10 | Reflex Sweep, Empire View, sweeps open 30 min, 3 h memory; Weighing, 15-target ledger, Raid's Eye, Foreseen Loot, Farm Round or Hunt Balance |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Forewarned Guard needs 90 seconds of alert**: the minute the game gives everyone is not enough, you need at least Keen Ear. An attack whose flight is shorter than 90 s never triggers it.
- **Alert talents count when the enemy fleet leaves**: taking Keen Ear while an attack is already flying does not announce it earlier.
- **The early alert is vague**: targeted base and time to the minute, no origin, until the last 60 seconds. To leave at the last second, Exact Hour matters more than the lead.
- **No moon, no phalanx**: the phalanx is built on a moon and never targets a moon; Moon and Planet only shows the fleets leaving or reaching the moon. The Return Foretold, however, needs no moon.
- **Silent Sweep only matters against the Shadow**: by default, nobody is told of a sweep.
- **Weighing, Foreseen Loot, Farm Ledger and The Raid Plan are maximums**: they ignore the defender's plunder protection and the size of their storage.
- **Prepared Strike** only applies to an attack launched at most 30 minutes after your espionage report on the same body. It counts in the class's speed accent (10% at most).
- **Enemy Gauge and Headcount measure a cost, not a strength**: 1,000 Cargo Shuttles (4,000,000) come out "large" like a combat fleet of the same price.
- **The Cache and Buried Vaults stack**: 10 points of protection in all, the plunder you suffer drops from 50 to 40%. That is the Oracle's cap.

## Related pages

- [Talents](/en/dynasty/talents)
- [Classes](/en/dynasty/classes)
- [Common tree](/en/dynasty/common-tree)
- [Dynasties](/en/dynasty/dynasties)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Reading a spy report](/en/espionage/spy-report)
- [Plunder](/en/combat/plunder)
- [Battle simulator](/en/combat/simulator)
- [The Shadow](/en/dynasty/classes/shadow)
