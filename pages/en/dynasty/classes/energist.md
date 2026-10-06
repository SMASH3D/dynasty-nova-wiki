---
locale: "en"
path: "dynasty/classes/energist"
url: "https://wiki.dynastynova.com/en/dynasty/classes/energist"
title: "The Energetician"
description: "The Energetician's class tree: Overdrive, Plants, Continuity."
tags: ["dynasty"]
published: false
---

# The Energetician

> **In short**: for the Energetician, energy is never wasted. Its surplus becomes ore, its shortfall no longer blocks anything, and its plants cost less than anyone else's. Common to every dynasty. Its three branches: **Overdrive**, **Plants** and **Continuity**.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

*"The pulse."* The master of energy: one lever that drives all three of your mines at once.

## Rules

1. The Energetician's tree follows the rules of every [class tree](/en/dynasty/talents): 3 branches of 9 rows, 15 points per branch, 25 points at most.
2. The generic energy bonus (+8% on every plant and Solar Collector) comes from the [common tree](/en/dynasty/common-tree), Prosperity branch. The Energetician only has **mechanics**, and a single accent: the construction speed of the Photovoltaic Sensors and the Thermonuclear Reactor (10%).
3. It has **no combat bonus**. It is the only class that plays on energy shortfall, the Thermonuclear Reactor and Solar Collectors.
4. **Overdrive**: a mine can run above its full rate, drawing more energy. The yield stops at **125%** (Peak and Overheat included), and at **140%** on a single mine with Star Core.
5. **Electrolysis** only converts energy that nothing uses: overdrive takes its share first, electrolysis takes the rest. It always takes at least 3 energy for 1 hydrogen.

## Worked example

A level 20 Mineral Excavator produces **4,036 metal per hour** and draws **1,345 energy** (see [Energy](/en/economy/energy)).

- **Overdrive** (110%, +25% energy): 4,036 × 1.1 = **4,440 metal per hour**, for 1,345 × 0.25 = **336 more energy**.
- With **Fine Tuning** at rank 3 (extra draw down to 13%): the same mine only needs **175 more energy**.
- With **Peak** and **Overheat** at rank 3 (125%): 4,036 × 1.25 = **5,045 metal per hour**.
- **Electrolysis**: 1,000 unused energy gives **250 hydrogen per hour** (333 with Deep Electrolysis).
- **Load Shedding** at rank 3: at 80% energy, 20 points are missing; your mines ignore 30% of them, 6 points, and run at **86%**. The Excavator produces 3,471 metal per hour instead of 3,229.
- **Cold Fusion** on a level 10 Thermonuclear Reactor (Energy Science 3): **259 hydrogen per hour** saved, 6,216 per day.

## Detailed data

### Overdrive: "Every spare watt becomes ore."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Overdrive** | On each base, one mine can run above its full rate, for more energy drawn. | 110%, +25% energy, 1 mine |
| 2 | 3 ranks | **Fine Tuning** | Overdrive's extra energy draw drops. | −4 points per rank (+13%) |
| 3 | choice | **A: Peak** / **B: Wide Overdrive** | A: overdrive gains yield, with no extra energy. <br> B: up to 3 mines in overdrive on each base. | +6 points / 3 mines |
| 4 | 3 ranks | **Overheat** | Overdrive gains further yield, with no extra energy. | +3 points per rank (119%, 125% with Peak) |
| 5 | key | **Electrolysis** | Energy nothing uses turns into hydrogen. Overdrive takes its share first. | 4 energy for 1 hydrogen |
| 6 | choice | **A: Deep Electrolysis** / **B: Exchanger** | A: less energy is needed for a unit of hydrogen. <br> B: on each base, electrolysis can yield metal or crystal instead. | 3 energy for 1 / 3 metal or 2 crystal per hydrogen |
| 7 | 3 ranks | **Superconducting Cables** | Your mines draw less energy. | −3% per rank (−9%) |
| 8 | key | **Circuit Breaker** | When energy runs short, overdrive backs off on its own before the base falls into deficit, then comes back as soon as it can. | unlock |
| 9 | ultimate | **Star Core** | On each base, the mine of your choice can go past overdrive. Each step of 5 points beyond draws more energy. | up to 140%, +20% energy per step |

### Plants: "The cheapest energy in the galaxy."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **The Night Is Short** | After a defense, part of your destroyed Solar Collectors is raised again for free, on the share that does not go to debris. With 30% debris, 70% of the destroyed Collectors remain, and 49% of those come back: 100 destroyed → 34 raised. | 49% |
| 2 | 3 ranks | **Sails** | Your Solar Collectors produce more energy. | +5% per rank (15%) |
| 3 | choice | **A: Full Sun** / **B: Cold Core** | A: your Photovoltaic Sensors produce more energy. <br> B: your Thermonuclear Reactor burns less hydrogen. | +10% / −20% |
| 4 | 3 ranks | **High Noon** | Your Photovoltaic Sensors read a temperature closer to the month's maximum. | 15% per rank (45%) |
| 5 | key | **Breeder Reactor** | Your Thermonuclear Reactor counts Energy Science as one level higher. | +1 level |
| 6 | choice | **A: Cold Standby** / **B: Swarm** | A: the Thermonuclear Reactor can be set like a mine, from off to full rate, and burns that much less hydrogen. <br> B: your Solar Collectors cost less. | setting / −20% |
| 7 | 3 ranks | **Orbital Workshops** | The Night Is Short raises more destroyed Collectors. | +7 points per rank (70%) |
| 8 | key | **Cluster Launch** | Your Solar Collectors are built on their own line, beside the Orbital Dock, which stays free for your ships. | unlock |
| 9 | ultimate | **Cold Fusion** | On the base of your choice, the Thermonuclear Reactor burns no hydrogen at all. | 1 base |

### Continuity: "Never out of power."

| Row | Type | Talent | Effect | Value |
|---|---|---|---|---|
| 1 | key | **Deferred Load** | A mine level just completed draws its new consumption only later: time to raise the plant that goes with it. | 4 h |
| 2 | 3 ranks | **Load Shedding** | Your mines ignore part of the energy shortfall. | 10% per rank (30%) |
| 3 | choice | **A: Emergency Shedding** / **B: Start-up** | A: your mines ignore more of the energy shortfall. <br> B: on a colony younger than 7 days, your mines ignore the whole energy shortfall. | +10% (40%) / colonies younger than 7 days |
| 4 | 3 ranks | **Spinning Reserve** | Deferred Load lasts longer. | +2 h per rank (10 h) |
| 5 | key | **Load Priority** | On each base, the mine of your choice is served first when energy runs short; the others share the rest. | unlock |
| 6 | choice | **A: Accumulators** / **B: Quick Ignition** | A: your spare energy is stored and covers a deficit on its own. <br> B: your Photovoltaic Sensors and Thermonuclear Reactors are built faster (accent). | up to 12 h of surplus / +10% |
| 7 | 3 ranks | **Transformers** | Load shedding can win back more points of energy, on top of the 15 it already does. | +5 points per rank (30 points) |
| 8 | key | **Flare** | Once a day, on the base of your choice, Photovoltaic Sensors and Solar Collectors produce more energy for 4 h. | ×1.5 for 4 h |
| 9 | ultimate | **Interplanetary Grid** | Your planets' surplus feeds those short of energy, up to part of their consumption. | 20% |

### What 25 points give

| Build | Split | What it gets |
|---|---|---|
| Surplus miner | Overdrive 15 · Plants 10 | three mines at 119% or one at 125%, one mine up to 140% with Star Core, electrolysis of the rest; stronger Sensors or a Reactor burning 20% less, and Breeder Reactor |
| Climber | Continuity 15 · Overdrive 10 | no more deficit: 10 h deferred load, load priority, Flare, then a grid between planets; overdrive and electrolysis so nothing is wasted |
| Lord of the Collectors | Plants 15 · Continuity 10 | Collectors raised at 70%, built on their own line and 20% cheaper, a base whose Reactor burns nothing; deferred load and load priority |

## Common pitfalls

- **Overdrive always costs energy**: without a surplus it throws the base into deficit and slows all three mines. Circuit Breaker avoids that trap.
- **Electrolysis creates nothing from energy already used**: overclock your mines first, then convert what is left.
- **No Continuity talent produces ore**: the branch removes the brake that stops you from raising a mine before its plant.
- **Row 3 of Plants decides your energy**: Photovoltaic Sensors cost nothing to run but depend on the planet's temperature; the Reactor burns hydrogen but grows with Energy Science.

## Related pages

- [Talent system](/en/dynasty/talents)
- [Common tree](/en/dynasty/common-tree)
- [Classes](/en/dynasty/classes)
- [Energy](/en/economy/energy)
- [Planets: size, temperature, type](/en/universe/planets)
