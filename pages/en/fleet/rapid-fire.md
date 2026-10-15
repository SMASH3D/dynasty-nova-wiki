---
wiki_id: 103
locale: "en"
path: "fleet/rapid-fire"
url: "https://wiki.dynastynova.com/en/fleet/rapid-fire"
title: "Rapid fire"
description: "Which units fire several times at which targets."
tags: ["fleet", "combat"]
published: true
created: "2026-10-02T13:11:06.074Z"
updated: "2026-10-15T18:53:11.575Z"
---

# Rapid fire

> **In short**: some ships have **rapid fire** against some units. After each shot at one of them, they have a chance to fire again in the same round, at a new randomly drawn target. The factor shown is the average number of chained shots against that unit type. Defenses have no rapid fire.
{.is-info}

> Ships are not translated in the game yet: it shows their French name in every language. The English names used here are provisional (see [Ships list](/en/fleet/ships)).
{.is-warning}

## Rules

1. Each round, every unit fires at least once (once per base shot) at an enemy unit **drawn at random** among those still alive. Rapid fire never steers a shot towards the units it counters.
2. After each shot, hit or miss, if the shooter has rapid fire of factor $f$ against the unit it just aimed at, it fires again with probability $(f - 1) / f$, at a **new randomly drawn target**.
3. The chain goes on as long as the roll succeeds **and** the last target is one of its rapid-fire targets. As soon as it lands on a unit that is not, it stops after that shot.
4. Against a fleet made only of that target, the shooter therefore fires $f$ times per round on average.
5. A chained shot follows the rules of a normal shot: a shot below 1% of the target's shield bounces off.
6. Some talents strengthen rapid fire (see [Talents](/en/dynasty/talents)): the table below gives the base factors.

## Worked example

A Corvette has rapid fire **6** against the Interceptor.
- After a shot at an Interceptor, it fires again with probability 5 / 6 = **83.3%**.
- Against a fleet made only of Interceptors, it fires **6 times on average** per round, instead of once.
- Against a fleet that is half Interceptors, half Battleships, the chain stops as soon as it lands on a Battleship: it fires much less.

## Detailed data

### Who rapid-fires at whom

| Shooter | Targets (factor) |
|---|---|
| *Cargo Shuttle* | *Scout* 5, *Solar Collector* 5 |
| *Stellar Freighter* | *Scout* 5, *Solar Collector* 5 |
| *Space Pioneer* | *Scout* 5, *Solar Collector* 5 |
| *Salvager* | *Scout* 5, *Solar Collector* 5 |
| *Interceptor* | *Scout* 5, *Solar Collector* 5 |
| *Assailant* | *Scout* 5, *Solar Collector* 5, *Cargo Shuttle* 3 |
| *Corvette* | Ballistic Projector 10, *Interceptor* 6, *Scout* 5, *Solar Collector* 5 |
| *Battleship* | *Scout* 5, *Solar Collector* 5 |
| *Orbital Striker* | Ballistic Projector 20, Photonic Cannon 20, High-Energy Emitter 10, Ion Battery 10, Magnetic Accelerator 5, Plasma Ejector 5, *Scout* 5, *Solar Collector* 5 |
| *Predator* | *Battleship* 7, *Scout* 5, *Solar Collector* 5, *Corvette* 4, *Assailant* 4, *Stellar Freighter* 3, *Cargo Shuttle* 3 |
| *Annihilator* | Photonic Cannon 10, *Scout* 5, *Solar Collector* 5, *Predator* 2 |
| *Stellar Colossus* | *Solar Collector* 1,250, *Scout* 1,250, *Cargo Shuttle* 250, *Space Pioneer* 250, *Stellar Freighter* 250, *Salvager* 250, Ballistic Projector 200, *Interceptor* 200, Photonic Cannon 200, *Assailant* 100, High-Energy Emitter 100, Ion Battery 100, Magnetic Accelerator 50, *Corvette* 33, *Battleship* 30, *Orbital Striker* 25, *Predator* 15, *Annihilator* 5 |
| *Scout*, *Solar Collector* | none |
| All defenses | none |

### Who is targeted by what

| Target | Ships with rapid fire against it |
|---|---|
| *Cargo Shuttle* | *Stellar Colossus* 250, *Assailant* 3, *Predator* 3 |
| *Stellar Freighter* | *Stellar Colossus* 250, *Predator* 3 |
| *Space Pioneer* | *Stellar Colossus* 250 |
| *Salvager* | *Stellar Colossus* 250 |
| *Scout* | *Stellar Colossus* 1,250, *Battleship* 5, *Orbital Striker* 5, *Space Pioneer* 5, *Corvette* 5, *Annihilator* 5, *Assailant* 5, *Stellar Freighter* 5, *Interceptor* 5, *Predator* 5, *Salvager* 5, *Cargo Shuttle* 5 |
| *Solar Collector* | *Stellar Colossus* 1,250, *Battleship* 5, *Orbital Striker* 5, *Space Pioneer* 5, *Corvette* 5, *Annihilator* 5, *Assailant* 5, *Stellar Freighter* 5, *Interceptor* 5, *Predator* 5, *Salvager* 5, *Cargo Shuttle* 5 |
| *Interceptor* | *Stellar Colossus* 200, *Corvette* 6 |
| *Assailant* | *Stellar Colossus* 100, *Predator* 4 |
| *Corvette* | *Stellar Colossus* 33, *Predator* 4 |
| *Battleship* | *Stellar Colossus* 30, *Predator* 7 |
| *Orbital Striker* | *Stellar Colossus* 25 |
| *Predator* | *Stellar Colossus* 15, *Annihilator* 2 |
| *Annihilator* | *Stellar Colossus* 5 |
| *Stellar Colossus* | nobody |
| Ballistic Projector | *Stellar Colossus* 200, *Orbital Striker* 20, *Corvette* 10 |
| Photonic Cannon | *Stellar Colossus* 200, *Orbital Striker* 20, *Annihilator* 10 |
| High-Energy Emitter | *Stellar Colossus* 100, *Orbital Striker* 10 |
| Magnetic Accelerator | *Stellar Colossus* 50, *Orbital Striker* 5 |
| Ion Battery | *Stellar Colossus* 100, *Orbital Striker* 10 |
| Plasma Ejector | *Orbital Striker* 5 |
| Defensive Barrier | nobody |
| Protective Dome | nobody |

## Common pitfalls

- **Scouts and Solar Collectors feed enemy chains**: almost every ship has rapid fire 5 against them. Leaving many of them in orbit during an attack hands the attacker extra shots.
- **Rapid fire guarantees nothing**: the next target is random. In a mixed fleet, chains are shorter than the factor shown.
- **No rapid fire targets the Stellar Colossus**: it can only be brought down by normal shots.
- **Rapid fire does not bypass the 1% rule**: a shot too weak for a big shield bounces off, even inside a chain.

## Related pages

- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [How combat works](/en/combat/how-combat-works)
- [Combat simulator](/en/combat/simulator)
