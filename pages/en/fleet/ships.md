---
wiki_id: 102
locale: "en"
path: "fleet/ships"
url: "https://wiki.dynastynova.com/en/fleet/ships"
title: "Ships list"
description: "The 14 ships: costs, stats, requirements."
tags: ["fleet", "ships"]
published: true
created: "2026-10-02T13:11:03.964Z"
updated: "2026-10-02T17:40:04.626Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Ships list

> **In short**: Dynasty Nova has 14 ships, built at the Orbital Dock. The game sorts them into three families: civil (carry, colonize, recycle, spy), combat and special. This page gives each ship's cost, build time, requirements, stats and drive.
{.is-info}

> Ships are not translated in the game yet: it shows their French name (in brackets below) in every language. The English names used here are provisional.
{.is-warning}

> **Universe setting**: the shipyard speed divides ship build times.
> Default: **×1** · Redline: **×1**
{.is-info}

## Rules

1. Ships are built at the **Orbital Dock**, on a planet or a moon. An order is only accepted if the base can pay for all of it; each unit is then paid when it enters production (see [Orbital Dock](/en/fleet/orbital-dock)).
2. A ship **always costs the same**, however many you already built.
3. The game sorts them into three families: **Civil Ships**, **Combat Ships** and **Special Ships**.
4. Every ship has a **built-in drive**. The Cargo Shuttle, the Salvager and the Orbital Striker **switch to a better drive on their own** once that drive's research reaches a given level: their base speed and consumption change with it (table below). If several goals are met, the most advanced drive wins.
5. **Speed** = the drive's base speed × (1 + bonus × level of that drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive. A fleet flies at the speed of its slowest ship (see [Fleet movement](/en/fleet/movement)).
6. **Consumption**: no research lowers it. A better drive burns more.
7. **Cargo**: +5% per level of Hyperspace Technology, rounded to the unit.
8. **Combat**: attack, shield and structure rise by 10% per level of Weapon Systems, Shielding Technology and Armor Technology. The **combat hull** equals structure divided by 10.
9. **Points**: each ship is worth 1 point per 1,000 resources of its cost (metal, crystal and hydrogen). **Every ship**, civil ones included, counts towards military points: they are credited on delivery and removed when the ship is lost.
10. The **Solar Collector** never flies: it stays in orbit and produces floor(Tmax / 4 + 20) energy, never below 0, where Tmax is the planet's maximum temperature in °C (see [Energy](/en/economy/energy)).
11. A destroyed ship is lost. After a battle where your base defends, the [Repair Station](/en/economy/repair-station) recovers part of them.

## Worked example

**A Cargo Shuttle before and after its drive switch**, with Combustion Drive 6:
- Impulse Drive 4: it keeps the Combustion Drive, speed 5,000 × (1 + 0.1 × 6) = **8,000**, consumption **10**.
- Impulse Drive 5: it switches to the Impulse Drive, speed 10,000 × (1 + 0.2 × 5) = **20,000**, consumption **20**.

**10 Stellar Freighters with Hyperspace Technology 3**: one Freighter carries 25,000 × (1 + 0.05 × 3) = 28,750, so **287,500 resources** for the fleet.

**An Interceptor** with Combustion Drive 6, Weapon Systems 2, Shielding Technology 0, Armor Technology 3: speed 12,500 × 1.6 = **20,000**; attack 50 × 1.2 = **60**; shield **10**; combat hull 4,000 × 1.3 / 10 = **520**.

## Detailed data

### Costs, build times and roles

The base time is divided by (1 + Orbital Dock level) × 2^(Molecular Assembler level) and by the shipyard speed (see [Orbital Dock](/en/fleet/orbital-dock)).

| Ship | Family | Metal | Crystal | Hydrogen | Points | Base time | Role |
|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/ships/navette-de-fret.jpg" width="48" alt="Cargo Shuttle (Navette de fret)"> *Cargo Shuttle* (Navette de fret) | civil | 2,000 | 2,000 | 0 | 4 | 1 h 30 min | Small fast transport |
| <img src="/images/illustrations/ships/cargo-stellaire.jpg" width="48" alt="Stellar Freighter (Cargo stellaire)"> *Stellar Freighter* (Cargo stellaire) | civil | 6,000 | 6,000 | 0 | 12 | 4 h | Large transport |
| <img src="/images/illustrations/ships/pionnier-spatial.jpg" width="48" alt="Space Pioneer (Pionnier spatial)"> *Space Pioneer* (Pionnier spatial) | civil | 10,000 | 20,000 | 10,000 | 40 | 28 h | Founds a colony |
| <img src="/images/illustrations/ships/recuperateur.jpg" width="48" alt="Salvager (Récupérateur)"> *Salvager* (Récupérateur) | civil | 10,000 | 6,000 | 2,000 | 18 | 7 h | Recycles debris fields |
| <img src="/images/illustrations/ships/eclaireur.jpg" width="48" alt="Scout (Éclaireur)"> *Scout* (Éclaireur) | civil | 0 | 1,000 | 0 | 1 | 10 min | Espionage probe |
| <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="48" alt="Solar Collector (Collecteur solaire)"> *Solar Collector* (Collecteur solaire) | special | 0 | 2,000 | 500 | 2.5 | 48 min | Produces energy in orbit, never flies |
| <img src="/images/illustrations/ships/intercepteur.jpg" width="48" alt="Interceptor (Intercepteur)"> *Interceptor* (Intercepteur) | combat | 3,000 | 1,000 | 0 | 4 | 30 min | Basic fighter |
| <img src="/images/illustrations/ships/assaillant.jpg" width="48" alt="Assailant (Assaillant)"> *Assailant* (Assaillant) | combat | 6,000 | 4,000 | 0 | 10 | 1 h 30 min | Sturdier fighter |
| <img src="/images/illustrations/ships/corvette.jpg" width="48" alt="Corvette (Corvette)"> *Corvette* (Corvette) | combat | 20,000 | 7,000 | 2,000 | 29 | 8 h | Anti-Interceptor specialist |
| <img src="/images/illustrations/ships/cuirasse.jpg" width="48" alt="Battleship (Cuirassé)"> *Battleship* (Cuirassé) | combat | 45,000 | 15,000 | 0 | 60 | 18 h | Ship of the line |
| <img src="/images/illustrations/ships/frappe-orbital.jpg" width="48" alt="Orbital Striker (Frappe-orbital)"> *Orbital Striker* (Frappe-orbital) | special | 50,000 | 25,000 | 15,000 | 90 | 24 h | Anti-defense specialist |
| <img src="/images/illustrations/ships/predateur.jpg" width="48" alt="Predator (Prédateur)"> *Predator* (Prédateur) | special | 30,000 | 40,000 | 15,000 | 85 | 22 h | Fleet hunter |
| <img src="/images/illustrations/ships/annihilateur.jpg" width="48" alt="Annihilator (Annihilateur)"> *Annihilator* (Annihilateur) | special | 60,000 | 50,000 | 15,000 | 125 | 32 h | Strongest of the standard fleet |
| <img src="/images/illustrations/ships/colossus-stellaire.jpg" width="48" alt="Stellar Colossus (Colossus stellaire)"> *Stellar Colossus* (Colossus stellaire) | special | 5,000,000 | 4,000,000 | 1,000,000 | 10,000 | 3,600 h | Ultimate ship, destroys moons |

### Base stats (no research, built-in drive)

| Ship | Structure | Combat hull | Shield | Attack | Cargo | Speed | Drive | Consumption |
|---|---|---|---|---|---|---|---|---|
| *Cargo Shuttle* (Navette de fret) | 4,000 | 400 | 10 | 5 | 5,000 | 5,000 | Combustion Drive | 10 |
| *Stellar Freighter* (Cargo stellaire) | 12,000 | 1,200 | 25 | 5 | 25,000 | 7,500 | Combustion Drive | 50 |
| *Space Pioneer* (Pionnier spatial) | 30,000 | 3,000 | 100 | 50 | 7,500 | 2,500 | Impulse Drive | 1,000 |
| *Salvager* (Récupérateur) | 16,000 | 1,600 | 10 | 1 | 20,000 | 2,000 | Combustion Drive | 300 |
| *Scout* (Éclaireur) | 1,000 | 100 | 0 | 0 | 5 | 100,000,000 | Combustion Drive | 1 |
| *Solar Collector* (Collecteur solaire) | 2,000 | 200 | 1 | 1 | 0 | 0 | none | 0 |
| *Interceptor* (Intercepteur) | 4,000 | 400 | 10 | 50 | 50 | 12,500 | Combustion Drive | 20 |
| *Assailant* (Assaillant) | 10,000 | 1,000 | 25 | 150 | 100 | 10,000 | Impulse Drive | 75 |
| *Corvette* (Corvette) | 27,000 | 2,700 | 50 | 400 | 800 | 15,000 | Impulse Drive | 300 |
| *Battleship* (Cuirassé) | 60,000 | 6,000 | 200 | 1,000 | 1,500 | 10,000 | Hyperspace Drive | 500 |
| *Orbital Striker* (Frappe-orbital) | 75,000 | 7,500 | 500 | 1,000 | 500 | 4,000 | Impulse Drive | 700 |
| *Predator* (Prédateur) | 70,000 | 7,000 | 400 | 700 | 750 | 10,000 | Hyperspace Drive | 250 |
| *Annihilator* (Annihilateur) | 110,000 | 11,000 | 500 | 2,000 | 2,000 | 5,000 | Hyperspace Drive | 1,000 |
| *Stellar Colossus* (Colossus stellaire) | 9,000,000 | 900,000 | 50,000 | 200,000 | 1,000,000 | 100 | Hyperspace Drive | 1 |

Each ship fires once per round, plus the extra shots of its [rapid fire](/en/fleet/rapid-fire).

### Drive switches

| Ship | Built-in drive · speed · consumption | Switches drive at | New drive · speed · consumption |
|---|---|---|---|
| *Cargo Shuttle* (Navette de fret) | Combustion Drive · 5,000 · 10 | Impulse Drive 5 | Impulse Drive · 10,000 · 20 |
| *Salvager* (Récupérateur) | Combustion Drive · 2,000 · 300 | Impulse Drive 17 | Impulse Drive · 4,000 · 600 |
| *Salvager* (Récupérateur) | Combustion Drive · 2,000 · 300 | Hyperspace Drive 15 | Hyperspace Drive · 6,000 · 900 |
| *Orbital Striker* (Frappe-orbital) | Impulse Drive · 4,000 · 700 | Hyperspace Drive 8 | Hyperspace Drive · 5,000 · 700 |

The Salvager switches to the Hyperspace Drive at level 15, even without Impulse Drive 17: each goal is enough on its own.

### Requirements

| Ship | Orbital Dock | Research |
|---|---|---|
| *Cargo Shuttle* (Navette de fret) | 2 | Combustion Drive 2 |
| *Stellar Freighter* (Cargo stellaire) | 4 | Combustion Drive 6 |
| *Space Pioneer* (Pionnier spatial) | 4 | Impulse Drive 3, Astrophysics 1 |
| *Salvager* (Récupérateur) | 4 | Combustion Drive 6, Shielding Technology 2 |
| *Scout* (Éclaireur) | 3 | Combustion Drive 3, Espionage Technology 2 |
| *Solar Collector* (Collecteur solaire) | 1 | none |
| *Interceptor* (Intercepteur) | 1 | none |
| *Assailant* (Assaillant) | 3 | Armor Technology 2 |
| *Corvette* (Corvette) | 5 | Impulse Drive 4, Ion Technology 2 |
| *Battleship* (Cuirassé) | 7 | Hyperspace Drive 4 |
| *Orbital Striker* (Frappe-orbital) | 8 | Impulse Drive 6, Plasma Technology 5 |
| *Predator* (Prédateur) | 8 | Hyperspace Drive 5, Laser Technology 12, Ion Technology 5 |
| *Annihilator* (Annihilateur) | 9 | Hyperspace Drive 6, Armor Technology 6 |
| *Stellar Colossus* (Colossus stellaire) | 12 | Hyperspace Drive 7, Hyperspace Technology 6, Graviton Technology 1 |

## Common pitfalls

- **New drive, new consumption**: a Cargo Shuttle on the Impulse Drive starts twice as fast but burns twice as much. A Salvager on the Hyperspace Drive burns three times what it does on the Combustion Drive.
- **A weak shot bounces off**: a shot below 1% of the target's shield does nothing (see [How combat works](/en/combat/how-combat-works)).
- **The Stellar Colossus is very slow**: base speed 100. A fleet with one in it flies at its pace.
- **The warp factor does nothing**: the game shows it, but no calculation uses it.
- **Cargo is not only for transport**: it also caps plunder, recycling, expedition finds and the trip's hydrogen, which travels in the holds.
- **Civil ships count too**: losing Freighters or Scouts lowers your military points.

## Related pages

- [Rapid fire](/en/fleet/rapid-fire)
- [Orbital Dock](/en/fleet/orbital-dock)
- [Fleet movement](/en/fleet/movement)
- [Missions](/en/fleet/missions)
- [How combat works](/en/combat/how-combat-works)
- [Repair Station](/en/economy/repair-station)
- [Glossary](/en/getting-started/glossary)
