---
wiki_id: 98
locale: "en"
path: "research/technologies"
url: "https://wiki.dynastynova.com/en/research/technologies"
title: "Technologies list"
description: "All technologies: effects, maximum levels, requirements."
tags: ["research"]
published: true
created: "2026-10-02T13:10:56.114Z"
updated: "2026-10-02T17:40:14.225Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Technologies list

> **In short**: the 17 technologies are researched in an Innovation Center. A level you gain applies to all your planets in the universe. They unlock buildings, ships and defenses, and give permanent bonuses: output, energy, speed, cargo, combat, espionage, colonies, fleet slots. Only one study runs at a time across the whole empire.
{.is-info}

> **Universe setting**: the research speed divides research times.
> Default: **×1** · Redline: **×1**
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

## Rules

1. Research is started from a planet with an **Innovation Center**. Its building requirements (most often the Innovation Center level) are read on **that planet**, its research requirements across the whole empire.
2. A level you gain applies to **all your planets** in the universe.
3. **Cost** of level N = level 1 cost × factor^(N − 1), rounded down for each resource. Research is **paid when it starts**.
4. **Duration** (formula below): it only depends on the level's metal and crystal, the **effective level** of the Innovation Center and the universe's research speed. Hydrogen does not change it.
5. **Effective level** = Innovation Center of the planet starting the research, plus the Centers networked by [Stellar Collaboration](/en/research/stellar-collaboration). It is set when the study starts.
6. **Speed bonuses** (alliance, talents): the duration is divided by (1 + bonus). Research speed talents are capped at 25%, alliance and talents together at 45%; a few class talents come on top of that (see [The Theorist](/en/dynasty/classes/theorist) and the other classes). A cost cut from a talent does not shorten the duration: it is worked out on the catalogue cost.
7. **Only one study at a time across the whole empire.** Each planet has its own research queue (same size as the [build queues](/en/economy/build-queue)); queued studies from all planets take their turn in the order they were placed. A queued study is only paid when its turn comes; if its planet lacks the resources then, it is dropped at no cost.
8. **Second Innovation Center** (ultimate talent of the common tree): a second study can run alongside the first, at 50% of the normal speed. It must be on another technology, and only starts in parallel when no study is waiting in a queue (see [The common tree](/en/dynasty/common-tree)).
9. **Points**: 1 research point per 1,000 resources spent (metal, crystal and hydrogen).
10. **Graviton Technology** is paid in **energy**: the energy output of the planet starting the research must reach the required threshold; nothing is used up. It takes no time and earns no points.
11. **Cancelling**: as for a building, 80% of the cost × share of the time left (see [Build queues](/en/economy/build-queue)).
12. While a planet's Innovation Center is **being upgraded**, the game neither starts nor queues any research there.
13. Every technology has a **maximum level**.

### Duration formula

$$t = \frac{M + C}{1{,}000 \times (1 + L)} \times \frac{3{,}600}{v}$$

- $t$: duration in seconds, rounded to the second;
- $M$, $C$: metal and crystal of the level studied (catalogue cost);
- $L$: effective Innovation Center level (rule 5);
- $v$: the universe's research speed.

With a speed bonus $b$ in percent (rule 6):

$$t' = \left\lceil \frac{100 \times t}{100 + b} \right\rceil$$

- $t'$: final duration in seconds, rounded up and never under 1 second;
- $b$: sum of the research speed bonuses (alliance and talents), capped as rule 6 says.

### Thermonuclear Reactor output

$$E = 30 \times N \times (1.05 + 0.01 \times S)^N$$

- $E$: energy produced, rounded down;
- $N$: Thermonuclear Reactor level;
- $S$: Energy Science level.

## Worked example

Espionage Technology level 4, started from a planet whose Innovation Center is level 4, without Stellar Collaboration:
- Cost: 200 × 2^3 = **1,600 metal**, **8,000 crystal** and **1,600 hydrogen**.
- Duration: (1,600 + 8,000) / (1,000 × (1 + 4)) = 1.92 h, that is **1 h 55 min 12 s**.
- With 15% research speed (talents): 6,912 × 100 / 115, rounded up, that is **1 h 40 min 11 s**.
- Research points gained: (1,600 + 8,000 + 1,600) / 1,000 = **11.2**.

Graviton Technology: level 1 needs an energy output of **300,000**, level 2 **900,000**, level 3 **2,700,000** (factor 3).

Plasma Technology level 1, on a planet with Mineral Excavator and Crystal Extractor at level 13 (speed ×1): the mines make 1,346 metal and 897 crystal per hour; Plasma adds **13 metal** (1%) and **5 crystal** (0.66%) per hour.

## Detailed data

### Effects

| Technology | Effect |
|---|---|
| <img src="/images/illustrations/research/science-energetique.jpg" width="48" alt="Energy Science"> Energy Science | Raises the energy output of the Thermonuclear Reactor (formula below): a level 10 Reactor gives 488 energy without Energy Science, 1,213 with Energy Science 10. No effect on Photovoltaic Sensors or Solar Collectors. |
| <img src="/images/illustrations/research/systemes-photoniques.jpg" width="48" alt="Laser Technology"> Laser Technology | No effect of its own: a requirement for technologies, ships and defenses. |
| <img src="/images/illustrations/research/manipulation-ionique.jpg" width="48" alt="Ion Technology"> Ion Technology | No effect of its own: a requirement for technologies, ships and defenses. |
| <img src="/images/illustrations/research/pliage-spatial.jpg" width="48" alt="Hyperspace Technology"> Hyperspace Technology | +5% cargo capacity per level (transport, plunder, recycling, expedition finds). Level 7 needed for the Jump gate. |
| <img src="/images/illustrations/research/maitrise-du-plasma.jpg" width="48" alt="Plasma Technology"> Plasma Technology | Per level: 1% metal, 0.66% crystal and 0.33% hydrogen on top, worked out on the gross output of each planet's mines (Planetary Base excluded). |
| <img src="/images/illustrations/research/propulseur-chimique.jpg" width="48" alt="Combustion Drive"> Combustion Drive | +10% speed per level for ships flying on the Combustion Drive. |
| <img src="/images/illustrations/research/moteur-magnetique.jpg" width="48" alt="Impulse Drive"> Impulse Drive | +20% speed per level for ships flying on the Impulse Drive. Long-Range Warheads range: 5 × level − 1 systems. At level 5, the Cargo Shuttle switches to this drive. |
| <img src="/images/illustrations/research/navigation-transdimensionnelle.jpg" width="48" alt="Hyperspace Drive"> Hyperspace Drive | +30% speed per level for ships flying on the Hyperspace Drive. The Orbital Striker switches to it at level 8, the Salvager at level 15. |
| <img src="/images/illustrations/research/systemes-offensifs.jpg" width="48" alt="Weapon Systems"> Weapon Systems | +10% attack per level for your ships and defenses, and +10% damage per level for your Long-Range Warheads. |
| <img src="/images/illustrations/research/champs-de-protection.jpg" width="48" alt="Shielding Technology"> Shielding Technology | +10% shield per level for your ships and defenses. |
| <img src="/images/illustrations/research/metallurgie-avancee.jpg" width="48" alt="Armor Technology"> Armor Technology | +10% structure per level for your ships and defenses. |
| <img src="/images/illustrations/research/renseignement-tactique.jpg" width="48" alt="Espionage Technology"> Espionage Technology | Depth of spy reports and counter-espionage (see [Spying](/en/espionage/spying)); −5% per level on the hydrogen of spy missions, down to −50%; at level 10, a spied position stays discovered for good. |
| <img src="/images/illustrations/research/calcul-quantique.jpg" width="48" alt="Quantum Computing"> Quantum Computing | Fleet slots = 1 + level. An expedition also takes a slot. |
| <img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="48" alt="Astrophysics"> Astrophysics | Number of planets, simultaneous expeditions and longest expedition hold (table below). Level 1 needed for expeditions. |
| <img src="/images/illustrations/research/collaboration-stellaire.jpg" width="48" alt="Stellar Collaboration"> Stellar Collaboration | Pools the Innovation Centers of your other planets to shorten research (see [Stellar Collaboration](/en/research/stellar-collaboration)). |
| <img src="/images/illustrations/research/manipulation-gravitationnelle.jpg" width="48" alt="Graviton Technology"> Graviton Technology | Requirement for the Stellar Colossus. Paid in energy produced, takes no time and earns no points. |
| <img src="/images/illustrations/research/diplomatie-stellaire.jpg" width="48" alt="Stellar Diplomacy"> Stellar Diplomacy | Level 1 needed to found an alliance. Sets the capacity of the alliance you found (table below). |

### Costs, maximum levels and requirements

| Technology | In-game section | Level 1 cost (metal / crystal / hydrogen) | Factor | Max level | Requirements |
|---|---|---|---|---|---|
| Energy Science | Fundamental Research | 0 / 800 / 400 | 2 | 25 | Innovation Center 1 |
| Laser Technology | Fundamental Research | 200 / 100 / 0 | 2 | 20 | Innovation Center 1, Energy Science 2 |
| Ion Technology | Fundamental Research | 1,000 / 300 / 100 | 2 | 15 | Innovation Center 4, Energy Science 4, Laser Technology 5 |
| Hyperspace Technology | Fundamental Research | 0 / 4,000 / 2,000 | 2 | 15 | Innovation Center 7, Energy Science 5, Laser Technology 7, Ion Technology 5 |
| Plasma Technology | Fundamental Research | 2,000 / 4,000 / 1,000 | 2 | 20 | Innovation Center 4, Energy Science 8, Laser Technology 10, Ion Technology 5 |
| Combustion Drive | Propulsion Research | 400 / 0 / 600 | 2 | 15 | Innovation Center 1, Energy Science 1 |
| Impulse Drive | Propulsion Research | 2,000 / 4,000 / 600 | 2 | 15 | Innovation Center 2, Energy Science 1, Combustion Drive 3 |
| Hyperspace Drive | Propulsion Research | 10,000 / 20,000 / 6,000 | 2 | 15 | Innovation Center 7, Energy Science 1, Hyperspace Technology 3 |
| Weapon Systems | Combat Research | 800 / 200 / 0 | 2 | 20 | Innovation Center 4 |
| Shielding Technology | Combat Research | 200 / 600 / 0 | 2 | 20 | Innovation Center 6, Energy Science 3 |
| Armor Technology | Combat Research | 1,000 / 0 / 0 | 2 | 20 | Innovation Center 2 |
| Espionage Technology | Strategic Research | 200 / 1,000 / 200 | 2 | 15 | Innovation Center 3 |
| Quantum Computing | Strategic Research | 0 / 400 / 600 | 2 | 20 | Innovation Center 1 |
| Astrophysics | Strategic Research | 4,000 / 8,000 / 4,000 | 1.75 | 20 | Innovation Center 3, Espionage Technology 4, Impulse Drive 3 |
| Stellar Collaboration | Strategic Research | 240,000 / 400,000 / 160,000 | 2 | 10 | Innovation Center 10, Quantum Computing 8, Hyperspace Technology 8 |
| Graviton Technology | Strategic Research | 300,000 required energy | 3 | 10 | Innovation Center 12, Energy Science 12, Laser Technology 12, Ion Technology 8 |
| Stellar Diplomacy | Strategic Research | 5,000 / 10,000 / 5,000 | 2 | 8 | Innovation Center 5, Quantum Computing 4 |

Level N cost follows from the factor: for instance, Weapon Systems level 5 costs 800 × 2^4 = 12,800 metal and 3,200 crystal. Full level-by-level tables are planned on separate pages.

### Astrophysics

| Level | Planets in total (home planet included) | Simultaneous expeditions | Longest expedition hold |
|---|---|---|---|
| 0 | 1 | 0 | none |
| 1 | 2 | 1 | 1 h |
| 2 | 2 | 1 | 2 h |
| 3 | 3 | 1 | 3 h |
| 4 | 3 | 2 | 4 h |
| 5 | 4 | 2 | 5 h |
| 6 | 4 | 2 | 6 h |
| 7 | 5 | 2 | 7 h |
| 8 | 5 | 2 | 8 h |
| 9 | 6 | 3 | 9 h |
| 10 | 6 | 3 | 10 h |
| 11 | 7 | 3 | 11 h |
| 12 | 7 | 3 | 12 h |
| 13 | 8 | 3 | 13 h |
| 14 | 8 | 3 | 14 h |
| 15 | 9 | 3 | 15 h |
| 16 | 9 | 4 | 16 h |
| 17 | 10 | 4 | 17 h |
| 18 | 10 | 4 | 18 h |
| 19 | 11 | 4 | 19 h |
| 20 | 11 | 4 | 20 h |

Planets in total = 1 + whole part of ((level + 1) / 2). Simultaneous expeditions = whole part of √level, taken from your fleet slots. Longest hold = level, in hours.

### Stellar Diplomacy

| Founder's level | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Alliance members | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 50 |

Only the alliance **founder's** level counts. Capacity goes up when they complete a level, and never goes down.

### Drive switch

Three ships switch drive when a propulsion technology reaches a given level. Their base speed and fuel consumption then become the new drive's, and that drive's technology speeds them up.

| Ship | Starting drive | Switches drive at | Base speed | Base consumption |
|---|---|---|---|---|
| Cargo Shuttle | Combustion Drive | Impulse Drive 5 | 5,000 → 10,000 | 10 → 20 |
| Orbital Striker | Impulse Drive | Hyperspace Drive 8 | 4,000 → 5,000 | 700 → 700 |
| Salvager | Combustion Drive | Hyperspace Drive 15 | 2,000 → 6,000 | 300 → 900 |

## Common pitfalls

- **The planet's Center matters**: duration and requirements are read on the planet starting the research. Start from your best Center; a colony with too weak a Center cannot start a technology that asks for more.
- **Hydrogen does not lengthen research**: only metal and crystal go into the duration. Hydrogen counts for points.
- **A queued study is not paid**: get the resources ready on the right planet before its turn.
- **Quantum Computing limits your fleets**: at level 2, you only have 3 fleets in flight, expeditions included.
- **One more colony every two levels**: Astrophysics 2 gives no more planets than level 1.
- **Energy Science only improves the Thermonuclear Reactor**, not Photovoltaic Sensors or Solar Collectors.
- **Graviton Technology does not use up energy**, but you must produce it when the study starts: the planet's Sensors, Reactor and Solar Collectors count.
- **Laser Technology and Ion Technology have no effect of their own**: you raise them for what they unlock.

## Related pages

- [Tech tree](/en/research/tech-tree)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Build queues](/en/economy/build-queue)
- [Buildings list](/en/economy/buildings)
- [Ships list](/en/fleet/ships)
- [Fleet movement](/en/fleet/movement)
- [Colonization](/en/universe/colonization)
- [Expeditions](/en/fleet/expeditions)
- [Alliances](/en/players/alliances)
- [The common tree](/en/dynasty/common-tree)
