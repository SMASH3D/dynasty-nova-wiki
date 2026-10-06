---
locale: "en"
path: "dynasty/classes/oracle"
url: "https://wiki.dynastynova.com/en/dynasty/classes/oracle"
title: "The Oracle"
description: "The foreknowledge class, exclusive to The Accord: Watch, Omen and Forewarning."
tags: ["dynasty"]
published: false
---

# The Oracle

> **In short**: the Oracle does not hit harder, it knows sooner. Each branch sells information, never a statistic: Watch sees fleets move from a moon, Omen prepares raids, Forewarning keeps you away when the blow lands.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Oracle is a class **exclusive to [The Accord](/en/dynasty/dynasties)**: only players of that dynasty can take it.
2. Its tree has **three branches**: Watch, Omen and Forewarning.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6. Points, gates and choices are explained on [Talents](/en/dynasty/talents).
4. Generic plunder protection and fleet return speed come from the [common tree](/en/dynasty/common-tree). The Oracle only adds two narrow accents: *Prepared Strike* (attack speed) and *The Cache* (plunder protection). Tracking spies belongs to the [Shadow](/en/dynasty/classes/shadow).
5. Without talents, an attack against you is announced **1 minute** before impact. Forewarning talents add to that lead.
6. Watch needs a moon: the [Sensor phalanx](/en/espionage/sensor-phalanx) is built there, and every sweep is paid for, except the ultimate's.

## Worked example

**Alert lead by Forewarning talents**

| Talents taken | Lead before impact |
|---|---|
| none | 1 min |
| Keen Ear | 2 min 30 |
| + Guard Tower at rank 3 | 3 min 30 |
| + Night Watchmen at rank 3 | 4 min 30 |
| + The Great Forewarning (level 40, full branch) | 6 min |

**Phalanx level 3 with Long Sight and Lenses at rank 3**
- Range: the Phalanx reaches as a level 4, i.e. 4² − 1 = **15 systems** on each side, instead of 8.
- Cost of a sweep: 5,000 × (1 − 0.24) = **3,800 hydrogen**.
- With *Empire View*, a player with 3 planets in reach is swept whole for 3,800 hydrogen instead of 11,400.

**Weighing**: the report reads 1,200,000 metal, 800,000 crystal and 300,000 hydrogen, i.e. 2,300,000 resources. With 50% plunder, the plunderable share is **1,150,000**. It takes 1,150,000 / 25,000 = **46 Stellar Freighters**, or 1,150,000 / 5,000 = **230 Cargo Shuttles**.

**The Cache**: 2,000,000 resources in stock. A winning raid takes 50% without talents, i.e. 1,000,000; with *The Cache*, 45%, i.e. **900,000**.

## Detailed data

### Watch

*See the fleets move.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Long Sight** | Your Phalanx reaches as if it had one more level. | 1 rank | +1 level |
| 2 | **Lenses** | Your sweeps cost less hydrogen. | 3 × 8% | −24% |
| 3 | **A · Shared Watch** or **B · Moon and Planet** | A: each of your sweeps is handed to your whole alliance. <br> B: a sweep also shows the fleets leaving or reaching the planet's moon. | 1 rank | unlock |
| 4 | **Phalanx Memory** | The fleets a sweep saw stay tracked, with their arrival time, after the sweep ends. | 3 × 1 h | 3 h |
| 5 | **The Return Foretold** | An announced attack also tells you when the enemy fleet will be back home. | 1 rank | unlock |
| 6 | **A · Silent Sweep** or **B · Moon Relay** | A: your sweeps are never reported to the swept planet, whatever talents its owner holds. <br> B: a planet in reach of any of your moons can be swept from your phalanx moon. | 1 rank | unlock |
| 7 | **Lingering Gaze** | A sweep stays open: fleets leaving or reaching the planet meanwhile are added to its reading. | 3 × 10 min | 30 min |
| 8 | **Empire View** | A sweep also shows the fleets of every other planet of the same player in reach, for the price of one. | 1 rank | unlock |
| 9 | **Reflex Sweep** *(ultimate)* | When an attack against you is announced, one of your moons in reach sweeps the planet it left from for free. | 1 rank | free |

### Omen

*Know before you strike.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Weighing** | Every spy report shows how many cargo ships it takes to carry off the plunderable share. | 1 rank | unlock |
| 2 | **Farm Ledger** | You follow targets: the game projects their stock from your last two reports and tells you when the plunderable share reaches the threshold you set. | 3 × 5 targets | 15 targets |
| 3 | **A · Measuring the Gap** or **B · Reading the Rankings** | A: the report says how many Scouts it takes to read the next tier. <br> B: a report too short for the simulator gets a defence outlook (probably empty, unknown, dangerous) instead of a refusal. | 1 rank | unlock |
| 4 | **Raid's Eye** | Your attack battle reports read the target as a spy report would: first the stock left after the plunder, then the buildings, then the research. | 3 × 1 tier | 3 tiers |
| 5 | **Foreseen Loot** | The simulator also gives the expected loot: the plunderable share, capped by your surviving ships' cargo space. | 1 rank | unlock |
| 6 | **A · Farm Round** or **B · Hunt Balance** | A: pick up to 5 farms; the game shares your cargo ships between them by their plunderable share and prepares the sends. <br> B: the simulator gives the expected debris field and the net gain over your losses. | 1 rank | A: 5 farms <br> B: unlock |
| 7 | **Prepared Strike** | An attack launched less than 30 minutes after your report on the target flies faster (speed accent). | 3 × 3% | +9% |
| 8 | **The Clash Foretold** | An attack against you gets a verdict, hold or fall, drawn from the public military rankings; simulated against the real fleet when your forewarning measures its power (*Headcount*). | 1 rank | unlock |
| 9 | **The Raid Plan** *(ultimate)* | From a report that read the fleet, the game suggests the smallest fleet, taken from the planet of your choice, that wins at least 9 simulated fights out of 10 and carries off the whole plunderable share. | 1 rank | 9 out of 10 |

Omen reveals nothing you have not already paid for: your reports, your battles and the public rankings.

### Forewarning

*Not to be there when the blow lands.*

| Row | Node | Effect | Per rank | Total |
|---|---|---|---|---|
| 1 | **Keen Ear** | Attacks against you are announced earlier. | 1 rank | +90 s |
| 2 | **Forewarned Guard** | If the alert came at least 90 seconds before impact, the planet's defenses and ships gain shield and damage, against attacks only. | 3 × 2% | +6% |
| 3 | **A · Enemy Gauge** or **B · Exact Hour** | A: the alert gives the size of the enemy fleet (small, medium, large, overwhelming). <br> B: from its very first second, the alert gives the exact arrival time and the origin. | 1 rank | unlock |
| 4 | **Guard Tower** | The alert comes earlier still. | 3 × 20 s | +60 s |
| 5 | **The Colossus Foretold** | Moon destructions aimed at your moons are announced like attacks, with the same lead. | 1 rank | unlock |
| 6 | **A · Headcount** or **B · Flash Retreat** | A: the alert gives the power of the enemy fleet within 25%, never its ships. <br> B: a fleet leaving a planet targeted by an announced attack flies 20% faster and burns 50% less hydrogen. | 1 rank | A: ±25% <br> B: +20%, −50% |
| 7 | **Night Watchmen** | The alert comes earlier still. | 3 × 20 s | +60 s |
| 8 | **The Cache** | The plunder you suffer drops by 5 points (accent). | 1 rank | −5 pts |
| 9 | **The Great Forewarning** *(ultimate)* | The alert comes earlier still. | 1 rank | +90 s |

The alert never gives the enemy fleet's composition: at most its size or its power.

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Sentinel | Forewarning 15 · Watch 10 | alert 6 min before impact, The Cache, guard +6%, moon destructions announced; Phalanx +1 level at 3,800 hydrogen, 3 h memory, The Return Foretold, silent sweep or moon relay |
| Augur | Omen 15 · Forewarning 10 | The Raid Plan, Foreseen Loot, 15-farm ledger, Raid's Eye; alert 3 min 30 before impact, Headcount or Flash Retreat |
| Lookout | Watch 15 · Omen 10 | Reflex Sweep, Empire View, sweeps open 30 min; Weighing, farm ledger, Raid's Eye, Foreseen Loot, round or balance |

## Common pitfalls

- **Forewarned Guard needs a 90-second alert**: the minute the game gives everyone is not enough. Take at least *Keen Ear*.
- **No moon, no Watch**: the Phalanx is built on a moon and never targets a moon; *Moon and Planet* only shows the fleets leaving or reaching the moon.
- **Prepared Strike** only applies to an attack launched less than 30 minutes after your spy report on the same target. It counts toward the class's speed accent (10% at most).
- **The Cache and Buried Vaults stack**: 10 points of protection in total, plunder suffered drops from 50 to 40%. That is the Oracle's cap.

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
