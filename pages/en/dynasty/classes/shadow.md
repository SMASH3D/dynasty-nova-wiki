---
wiki_id: 172
locale: "en"
path: "dynasty/classes/shadow"
url: "https://wiki.dynastynova.com/en/dynasty/classes/shadow"
title: "The Shadow"
description: "The Shadow's class tree: Infiltration, Stealth and Backlight."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:30:22.733Z"
updated: "2026-10-07T22:08:09.480Z"
---

# The Shadow

> **In short**: the Shadow plays intelligence both ways: reading others without getting caught, and making its own territory unreadable. Its talents are rules, not generic percentages, and it has no accent.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. The Shadow is a **common** class: every dynasty can take it.
2. Its tree has **three branches**: Infiltration, Stealth and Backlight.
3. Each branch has 9 rows and costs 15 points. With 25 points at most, you complete one branch and its ultimate, plus a second branch down to row 6 (10 points). How points, gates and choices work is described on [Talents](/en/dynasty/talents).
4. The Shadow's talents build on the rules of [espionage](/en/espionage/spying): effective level = Espionage Technology gap + 1 per pair of Scouts (+5 at most); report tiers: resources from 1, fleet from 3, defences and missiles from 5, buildings from 7, research from 9; detection chance bounded between 5% and 25%, zero if your Espionage Technology is at least double the target's or if the orbit is empty.
5. Detection points (Low Signature for the spy, Sentinels for the target) apply **before** the 5% to 25% band: they never take the chance below 5% or above 25%, and never create a chance where it is zero.
6. **Depth** (Economical Probes, The Threshold, Jamming) never changes the detection chance.
7. A **caught** wave is identified (the defender learns your name); a second roll may **trace** it (they also learn the planet of origin). The defender gets an intrusion alert for every wave, even an undetected one.

## Worked example

**A wave's risk, from both sides**
- Target: Espionage Technology 8, 40 ships in orbit. Spy: Espionage Technology 8. Chance: (2 × 8 − 8) × 40 × 0.05 = **16%**.
- The spy has Low Signature at rank 3: 16 − 6 = **10%**. Their Caution (15%) does not turn them back.
- If the target has Sentinels at rank 3: 16 + 6 − 6 = **16%**: the wave turns back.
- Against an 8% target: 8 − 6 = 2, raised to the band: **5%**.

**Reading defences with 4 Scouts, at equal Espionage Technology**
- With no talent: 4 Scouts give +2; effective level 2: only resources are read.
- Economical Probes at rank 3: the wave counts as 4 + 6 = 10 Scouts, that is +5; level 5: resources, fleet, defences and missiles.
- If the target has Jamming: level 4, defences stay closed. With The Threshold as well: 5 again.

**A caught wave of 9 Scouts**
- Dropped Probes alone: 9 × 20% = 1.8, rounded down: **1** comes home, 8 are lost.
- With Silent Hulls at rank 3: 9 × 41% = 3.69: **3** come home.
- No Address and Silent Hulls at rank 3: 9 × 21% = 1.89: **1** comes home.

**Veiled Fleet**: 117 Corvettes read as 120; 1,234 Interceptors, 1,200; 19 Battleships, 19.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["BACKLIGHT<br/>Your territory cannot be read."]:::head
        B3R1{{"Guarded Orbit<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Sentinels<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Shared Alert<br/>1 pt"]:::option
        B3R3B["② Incident Report<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points in the tree"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Hidden Vault<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Light at Your Back<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Moon Sentinels<br/>1 pt"]:::option
        B3R6B["② Veiled Fleet<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points in the tree"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Tailing<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Jamming<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Return to Sender<br/>ultimate"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["STEALTH<br/>Get in, read, get out."]:::head
        B2R1{{"Measured Risk<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Low Signature<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Dropped Probes<br/>1 pt"]:::option
        B2R3B["② No Address<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points in the tree"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Silent Hulls<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Caution<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Silhouette<br/>1 pt"]:::option
        B2R6B["② Smoke Screen<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points in the tree"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("False Trail<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"The Perfect Void<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Unseen, Unknown<br/>ultimate"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["INFILTRATION<br/>What the report says."]:::head
        B1R1{{"Stock on Arrival<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Economical Probes<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Reading the Holds<br/>1 pt"]:::option
        B1R3B["② Reading the Hangars<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points in the tree"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Living Dossier<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Orbital Glance<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① System Survey<br/>1 pt"]:::option
        B1R6B["② Combat Reading<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points in the tree"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Activity Report<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"The Threshold<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Bug<br/>ultimate"]]:::ultimate
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

### Infiltration

*What the report says.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Stock on Arrival** | key | Every report works out what the planet will hold when your raid lands, production included and under its storage: you know what you will plunder. |  |
| 2 | **Economical Probes** | 3 ranks | Your wave counts for 6 more probes in the depth, never past the +5 levels probes give: buildings read with far fewer probes. | 3 × 2 |
| 3 | **A · Reading the Holds** | choice | Resources open 1 tier earlier: they always read, even with a negative edge and a single probe. | |
|  | **B · Reading the Hangars** |  | The fleet opens 1 tier earlier: at the same edge, fewer probes read it. | |
| 4 | **Living Dossier** | 3 ranks | Every new report carries over the sections your reports read over the last 24 h, dated: one full wave in the morning, then light passes keep buildings and defences. | 3 × 8 h |
| 5 | **Orbital Glance** | key | A wave also reads the other body of the cell (a planet's moon, a moon's planet), 2 levels lower, in a second report. That is where sheltered fleets hide. |  |
| 6 | **A · System Survey** | choice | The wave also lists the other planets of the system, "active" or "inactive", with a stock bracket: you find your farms in a single pass. | |
|  | **B · Combat Reading** |  | The target's weapons, shields and armour read from the fleet tier (3) instead of the research tier (9): you simulate without a full wave. | |
| 7 | **Activity Report** | 3 ranks | The report tells when the target last played, with 3 degrees of precision: within the hour, the day or earlier; then to within 15 min; then on which planet. Strike while it sleeps. | 3 × 1 |
| 8 | **The Threshold** | key | Your reports read 1 more effective level, depth only, never counted by the detection roll. |  |
| 9 | **Bug** | ultimate | An undetected wave may leave a probe in orbit for 6 h. It sends you a resources and fleet report each time the fleet on the ground changes (departure, return, sheltering). Each report rolls the detection again at 50% of the chance; caught, it is destroyed. |  |

- **Stock on Arrival**: when the resources section is read, the report also gives the target's hourly production and storage, to project the stock at your raid's arrival.
- **Economical Probes**: the wave needs at least 1 Scout; the bonus from Scouts stays capped at +5.
- **Reading the Holds**: resources are always read, even with a negative gap and a single Scout. **Reading the Hangars**: the fleet is read from effective level 2; with Listening Far from [The Accord](/en/dynasty/dynasties), from 1.
- **Living Dossier**: only sections of the same body (the planet or its moon) are carried over; the game keeps the last 10 reports per cell.
- **Orbital Glance**: the second report has the same detection result as the wave.
- **System Survey**: only planets are listed, with the player name, the status (active, inactive, abandoned, on vacation) and a bracket of the total stock: under 10,000, 10,000, 50,000, 100,000, 250,000, 500,000, 1,000,000, 2,500,000, 5,000,000 and more. No stock for a player on vacation.
- **Combat Reading** gives Weapon Systems, Shielding Technology and Armor Technology while the fleet is read but not the research; the fleet tier follows Reading the Hangars.
- **Activity Report**: present even in a report that reads nothing else (not on an abandoned base). At rank 2, the time is rounded down to the quarter hour; at rank 3, the base the player last selected.
- **Bug**: requested when sending. The Scout left in orbit is lost to your fleet. It reports at every fleet departure or arrival on the base. Caught, it is destroyed and the defender's alert names you, without giving your planet. Only one per targeted base: placing another restarts the 6 h.

### Stealth

*Get in, read, get out.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Measured Risk** | key | The send screen and every report show the detection chance the wave faces: you see the risk before you leave. |  |
| 2 | **Low Signature** | 3 ranks | Your waves have 6 pts less chance of being detected. A well-guarded target's ceiling applies after. | 3 × 2 pts |
| 3 | **A · Dropped Probes** | choice | 20% of a caught wave's probes survive and come back. | |
|  | **B · No Address** |  | A caught wave is identified but never traced: the defender learns who, never from where. | |
| 4 | **Silent Hulls** | 3 ranks | A caught wave's probes gain 21% survival: more of them come back. | 3 × 7% |
| 5 | **Caution** | key | A wave facing 15% risk or more turns back before orbit: no report, no loss, no alert. It told you the target is guarded. Can be switched off at the send. |  |
| 6 | **A · Silhouette** | choice | Enemy phalanxes see your fleets, but not their composition or cargo. | |
|  | **B · Smoke Screen** |  | Your attacks show at their target as an "unknown fleet", with no ship count, until 15 min before impact. | |
| 7 | **False Trail** | 3 ranks | A traced wave has a 90% chance to give the defender a false origin: an inactive planet of your galaxy. | 3 × 30% |
| 8 | **The Perfect Void** | key | A wave that ran no risk (a target half as advanced, or an empty orbit) leaves only a vague trace: "activity spotted in your system", no planet, no name, to the hour. |  |
| 9 | **Unseen, Unknown** | ultimate | Once a day, a caught wave is not shot down: it slips past the defense and all its probes come home. |  |

- **Measured Risk**: the sending screen computes the chance at sending time; the roll happens when the Scouts arrive.
- **Dropped Probes** and **Silent Hulls** add up; the number of Scouts saved is rounded down, a lone Scout never comes home. No Address being the other choice, survival is then 21% at most.
- **Caution**: compares the chance with the band applied. The wave has flown the round trip and paid its hydrogen. You get a notification.
- **Silhouette**: applies to every Sensor phalanx sweep, including those shared in an alliance.
- **Smoke Screen**: only Attacks on their way out, for every other player (target and phalanxes).
- **False Trail**: the false origin is a planet of an inactive player in your galaxy; if there is none, the real origin is given. Useless with No Address, since the wave is never traced.
- **The Perfect Void**: "no risk" means a 0% chance; a target with Guarded Orbit keeps its empty orbits at 5%. The defender gets "activity spotted" in their system, to the hour, instead of the alert.
- **Unseen, Unknown**: fires on its own on the **first** caught wave of the cycle. It is still caught: the defender gets their alert and may trace it.

### Backlight

*Your territory cannot be read.*

| Row | Node | Type | Effect (full node) | Per rank |
|---|---|---|---|---|
| 1 | **Guarded Orbit** | key | Counter-espionage plays even over an empty orbit, at its 5% floor: your colonies without a fleet are no longer an open book. |  |
| 2 | **Sentinels** | 3 ranks | Waves on your planets have 6 pts more chance of being detected. | 3 × 2 pts |
| 3 | **A · Shared Alert** | choice | Your intrusion alerts are copied to your whole alliance. | |
|  | **B · Incident Report** |  | An undetected intrusion still tells you how many probes, and from which galaxy. | |
| 4 | **Hidden Vault** | 3 ranks | Enemy reports on your planets and moons show 30% less stock. The stock can still be plundered: the attacker brings too little cargo. | 3 × 10% |
| 5 | **Light at Your Back** | key | You are warned when a phalanx sweeps one of your planets, and by whom. |  |
| 6 | **A · Moon Sentinels** | choice | A planet's counter-espionage also counts its moon's ships, and the other way round. | |
|  | **B · Veiled Fleet** |  | Enemy reports give your fleet rounded to within 10%: "≈" before every number. | |
| 7 | **Tailing** | 3 ranks | A detected wave has 15 pts more chance of being traced: the spy leaves an address. | 3 × 5 pts |
| 8 | **Jamming** | key | Enemy reports on your planets read 1 effective level lower, depth only: enough to cancel an enemy Shadow's Threshold. |  |
| 9 | **Return to Sender** | ultimate | A traced wave brings you, without probes and without the spy knowing, a report on its planet of origin, read at tier 3: resources and fleet. |  |

- **Guarded Orbit**: the Espionage Technology gap must still be in your favour. With Sentinels at rank 3, an empty orbit is guarded at 6%.
- **Shared Alert**: every intrusion alert you receive is copied as a notification to the other members of your alliance.
- **Hidden Vault**: each resource is read at 70% at rank 3 (rounded down), in any report by another player on your bases: wave, Bug, Return to Sender, System Survey.
- **Light at Your Back**: you learn the player's name and moon. Nothing against an Oracle with Silent Sweep.
- **Moon Sentinels**: only if you also own the other body of the cell.
- **Veiled Fleet**: each ship count is rounded by steps of 1, 10, 100… depending on its size; under 20 ships of a type, the count stays exact.
- **Jamming** does not affect a Bug, which always reads at tier 3.
- **Return to Sender**: only on a traced wave. The report reads the planet of origin, or the false origin if False Trail worked. The spy gets "activity spotted" in their system, to the hour.

### Class caps

The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.

| Class cap (talents of both trees) | What the class tree reaches |
|---|---|
| Resources show 1 tier earlier in your spy reports | 1 |
| The fleet shows 1 tier earlier in your spy reports | 1 |
| +1 level of depth for your spy reports, never for the detection roll | 1 |
| −6 pts chance of your spy waves being detected | 6 pts |
| +41% of a caught wave's probes survive and come back | 41% |
| +6 pts chance to detect waves on your planets | 6 pts |
| +15 pts chance to trace a detected wave back to its planet of origin | 15 pts |
| Enemy reports on your planets read 1 effective level lower, depth only | 1 |

### 25-point builds

| Build | Split | What it gets |
|---|---|---|
| Hunter | Infiltration 15 · Stealth 10 | Bug, Combat Reading or System Survey, The Threshold, activity down to the base, a 24 h Living Dossier; −6 detection points, Caution, 41% survival (or No Address), Silhouette (phalanxes without composition) or Smoke Screen |
| Ghost | Stealth 15 · Infiltration 10 | Unseen, Unknown, The Perfect Void, False Trail at 90%, 41% survival; Stock on Arrival, buildings read with 4 Scouts if your Espionage Technology is 2 levels ahead, a 24 h Living Dossier, Orbital Glance |
| Warden | Backlight 15 · Stealth 10 | Return to Sender, Jamming, stock read at 70%, Tailing +15 points, Guarded Orbit; its own waves at −6 points with Caution |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.

## Common pitfalls

- **Listening Far and Reading the Hangars stack**: an Accord Shadow taking Reading the Hangars reads the fleet **two tiers** earlier.
- **The Threshold does not lower the risk**: it adds depth, never stealth.
- **Low Signature hits the 5% floor**: against a lightly guarded target, part of the 6 points is wasted.
- **No more "all or nothing"**: with Dropped Probes and Silent Hulls, part of a caught wave's Scouts comes home. Without these talents, the whole wave falls; a lone Scout never comes home.
- **No Address and False Trail do not go together**: a wave that is never traced has no origin to fake.
- **Unseen, Unknown fires on its own** on the first caught wave of the cycle, even a single-Scout wave.
- **Bug costs a Scout** each time it is placed.
- **Hidden Vault protects nothing**: it skews the enemy report, the stock stays fully lootable.
- **Jamming cancels The Threshold**: against a Shadow that took Backlight down to row 8, your extra effective level disappears.
- **Return to Sender gets noticed**: the spy learns there was activity in their system.

## Related pages

- [Talents](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Dynasties](/en/dynasty/dynasties)
- [Spying](/en/espionage/spying)
- [Reading a spy report](/en/espionage/spy-report)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
