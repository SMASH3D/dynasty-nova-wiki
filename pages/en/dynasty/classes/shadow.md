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
updated: "2026-10-06T10:30:24.072Z"
---

# The Shadow

> **In short**: the Shadow plays intelligence both ways: reading other empires without getting caught, and making their own territory unreadable. Their talents are rules, not generic percentages, and they have no accent. A class open to every dynasty.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

*Motto: "Know without being seen".*

## Rules

1. The class tree follows the rules shared by every class: 3 branches of 9 rows, 15 points per branch, 25 points at most. See [Talent system](/en/dynasty/talents).
2. The Shadow's talents build on the rules of [espionage](/en/espionage/spying): effective level, report tiers (resources from 1, fleet from 3, defenses from 5, buildings from 7, research from 9), destruction chance bounded between 5% and 25%.
3. The Shadow's **caps**:
   - depth: **+1 effective level** at most (The Threshold), never counted by the detection roll; the Scout bonus stays capped at +5;
   - tiers: **1 tier earlier** at most per category from talents, only for resources and fleet; the Listening Far dynasty trait adds to it;
   - detection: **8 points** at most of destruction chance taken off (attacking) or added (defending), the 5% to 25% band still applied afterwards;
   - survival of a caught wave's Scouts: **50%** at most;
   - tracing: **+15 points** at most of chance to be traced.

## Worked example

**Economical Probes: reading buildings with 4 Scouts**
- Your Espionage Technology is 2 levels above the target's. Buildings need effective level 7: you need +5 from Scouts, so **10 Scouts**.
- At rank 3 of Economical Probes, your wave counts for 6 more Scouts: **4 Scouts** count as 10, i.e. +5. Effective level: 2 + 5 = **7**.

**The Threshold**
- Same 2-level edge, with 8 Scouts: 2 + 4 + 1 = **7**: buildings show.
- 3-level edge, with 10 Scouts: 3 + 5 + 1 = **9**: research shows.

## Detailed data

### Tree at a glance

The three branches of the class tree, from row 1 to the ultimate. Each talent is detailed in the tables.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["BACKLIGHT<br/>Your territory cannot be read"]:::head
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
        B2H["STEALTH<br/>Get in, read, get out"]:::head
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
        B1H["INFILTRATION<br/>What the report says"]:::head
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

### Infiltration: "What the report says"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Stock on Arrival** | every report works out what the planet will hold when your raid lands, production included and within its storage (180,000 metal at 12,000/h, 1 h raid: 192,000 on arrival, 96,000 plunderable) | unlock |
| 2 | 3 ranks | **Economical Probes** | your wave counts for 2 more Scouts per rank in the effective level, never past the +5 the Scouts give (buildings at a +2 edge with 4 Scouts instead of 10) | 3 × 2 probes |
| 3 | choice | **A · Reading the Holds** / **B · Reading the Hangars** | A: resources read 1 tier earlier, so always, even with a negative edge and a single Scout <br> B: the fleet reads 1 tier earlier (from effective level 2: at an even edge, 4 Scouts instead of 6) | 1 tier |
| 4 | 3 ranks | **Living Dossier** | every new report carries over, dated, the sections your reports read over the last 8 hours per rank: 24 h at rank 3. One full wave in the morning, then light passes keep buildings and defenses | 3 × 8 h |
| 5 | key | **Orbital Glance** | a wave also reads the other body of the cell (a planet's moon, a moon's planet), 2 levels lower, in a second report: that is where sheltered fleets hide | −2 levels |
| 6 | choice | **A · System Survey** / **B · Combat Reading** | A: the wave also lists the other planets of the system, "active" or "inactive", with a stock bracket <br> B: the target's weapons, shields and armor read from the fleet tier (3) instead of the research tier (9): you simulate without a full wave | unlock |
| 7 | 3 ranks | **Activity Report** | the report tells when the target last played. Rank 1: within the hour, the day or earlier. Rank 2: to within 15 min. Rank 3: and on which planet | 3 degrees |
| 8 | key | **The Threshold** | +1 effective level, for the report's depth only, never counted by the detection roll | +1 level |
| 9 | ultimate | **Bug** | an undetected wave may leave a Scout in orbit for 6 h. It sends a resources and fleet report each time the fleet on the ground changes (departure, return, sheltering). Each report rolls the detection again at half the chance; caught, it is destroyed | 6 h |

### Stealth: "Get in, read, get out"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Measured Risk** | the send screen and every report show the destruction chance the wave faces: you see the risk before you leave | unlock |
| 2 | 3 ranks | **Low Signature** | −2 points of chance to be detected per rank: −6 at rank 3 (16% → 10%). A well-guarded target's 25% bound applies afterwards | 3 × 2 pts |
| 3 | choice | **A · Dropped Probes** / **B · No Address** | A: 20% of a caught wave's Scouts survive and come back (10 caught → 2 come back) <br> B: a caught wave is identified but never traced: the defender learns who, never from where | 20% / unlock |
| 4 | 3 ranks | **Silent Hulls** | +7% survival per rank for a caught wave's Scouts: +21% at rank 3 (41% with Dropped Probes: 10 caught → 4 come back) | 3 × 7% |
| 5 | key | **Caution** | a wave facing 15% risk or more turns back before orbit: no report, no loss, no alert. It told you the target is guarded. The risk compared is the one displayed, 5% and 25% bounds included. Can be switched off at the send | 15% |
| 6 | choice | **A · Silhouette** / **B · Smoke Screen** | A: enemy [Sensor phalanxes](/en/espionage/sensor-phalanx) see your fleets, but not their composition or cargo <br> B: your attacks show at their target as an "unknown fleet", with no ship count, until 15 min before impact | unlock |
| 7 | 3 ranks | **False Trail** | a traced wave has a 30% chance per rank to give the defender a false origin (an inactive planet of your galaxy): 90% at rank 3 | 3 × 30% |
| 8 | key | **The Perfect Void** | a wave that ran no risk (a target half as advanced, or an empty orbit) leaves only a vague trace: "activity spotted in your system", no planet, no name, to the hour | unlock |
| 9 | ultimate | **Unseen, Unknown** | once every 24 h, a caught wave is not shot down: it slips past the defense and all its Scouts come home | 1 per 24 h |

Detection budget: −6 points here, under the cap of 8. Survival: 20 + 21 = 41%, under the 50% cap.

### Backlight: "Your territory cannot be read"

| Row | Type | Node | Effect (example) | Value |
|---|---|---|---|---|
| 1 | key | **Guarded Orbit** | counter-espionage plays even over an empty orbit, at the 5% floor: your colonies without a fleet are no longer an open book | 5% |
| 2 | 3 ranks | **Sentinels** | +2 points of chance to detect waves on your planets per rank: +6 at rank 3 (a spy at 10% goes up to 16%) | 3 × 2 pts |
| 3 | choice | **A · Shared Alert** / **B · Incident Report** | A: your intrusion alerts are copied to your whole alliance <br> B: an undetected intrusion still tells you how many Scouts, and from which galaxy | unlock |
| 4 | 3 ranks | **Hidden Vault** | enemy reports on your planets and moons show 10% less stock per rank: 30% at rank 3 (300,000 crystal read as 210,000). The stock can still be plundered: the attacker brings too little cargo | 3 × 10% |
| 5 | key | **Light at Your Back** | you are warned when a Sensor phalanx sweeps one of your planets, and by whom | unlock |
| 6 | choice | **A · Moon Sentinels** / **B · Veiled Fleet** | A: a planet's counter-espionage also counts its moon's ships, and the other way round <br> B: enemy reports give your fleet rounded to within 10% ("≈ 120 Corvettes") | unlock |
| 7 | 3 ranks | **Tailing** | +5 points of chance per rank to trace a detected wave: +15 at rank 3 | 3 × 5 pts |
| 8 | key | **Jamming** | enemy reports on your planets read 1 effective level lower, depth only: enough to cancel an enemy Shadow's Threshold | −1 level |
| 9 | ultimate | **Return to Sender** | a traced wave brings you, without probes and without the spy knowing, a report on its planet of origin, read at tier 3: resources and fleet | tier 3 |

Hidden Vault and Veiled Fleet mislead about quantities, never about what exists, and leave plunder untouched.

### What 25 points give

| Build | Split | How it feels |
|---|---|---|
| **Hunter** | Infiltration 15 · Stealth 10 | Bug on the target, Combat Reading, The Threshold, activity down to the planet; 10% risk instead of 16, Caution, blind phalanxes |
| **Ghost** | Stealth 15 · Infiltration 10 | Unseen, Unknown, The Perfect Void, false trails; stock on arrival, buildings read with 4 Scouts, 24 h living dossier, moons read on the way |
| **Warden** | Backlight 15 · Stealth 10 | Return to Sender, Jamming, stock shown at 70%, tailing +15; own waves at 10% risk with Caution |

## Common pitfalls

- **Listening Far and Reading the Hangars stack**: a Shadow of The Accord who takes Reading the Hangars reads the fleet **two tiers** earlier.
- **The Threshold does not lower the risk**: it adds depth, never stealth.
- **No more "all or nothing"**: with Dropped Probes and Silent Hulls, some Scouts of a caught wave come home; without these talents, the whole wave still goes down.
- **Hidden Vault protects nothing**: it skews the enemy report, the stock stays fully plunderable.
- **Jamming cancels The Threshold**: against a Shadow who took Backlight down to row 8, your extra effective level disappears.

## Related pages

- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Dynasties](/en/dynasty/dynasties)
- [Spying](/en/espionage/spying)
- [Reading a spy report](/en/espionage/spy-report)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
