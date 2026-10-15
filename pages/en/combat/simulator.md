---
wiki_id: 119
locale: "en"
path: "combat/simulator"
url: "https://wiki.dynastynova.com/en/combat/simulator"
title: "Battle simulator"
description: "Planning an attack with the simulator."
tags: ["combat"]
published: true
created: "2026-10-02T13:11:38.050Z"
updated: "2026-10-15T18:52:34.412Z"
---

# Battle simulator

> **In short**: the simulator replays a battle with the game's real engine before you commit to it. No fleet is sent, no resource is spent. You start from a spy report or type in the defender by hand; the simulator gives victory rates, average losses and the debris field of an average battle.
{.is-info}

## Rules

### The defender
1. Two modes: **From a spy report** or **Manual entry**. A report shared with your alliance can be used too.
2. From a report, each part of the defender counts as **seen** only if the espionage reached its tier. The simulator says what it assumed and how old the report is.
3. A report that **did not see the fleet** is refused: there is nothing to simulate.
4. **Unseen defenses** are assumed to be **absent**: the victory rate shown is then an optimistic floor. Enter an estimate if you have one.
5. **Unseen research** is assumed to be **equal to yours**, without your talents.
6. Changing an imported value switches the simulation to **manual entry**: the report is no longer used.
7. The defender fights **without talents or dynasty bonuses**: they are never revealed.
8. Silo missiles never fight: they do not appear in the simulator.

### Your side
9. Your fleet fights with your research, dynasty and talents, as in a real battle.
10. You can enter more ships than you own: the simulator also helps decide what to build.
11. To simulate other Weapon Systems, Shielding Technology or Armor Technology levels, fill in **all three** research fields.

### The result
12. Each simulation replays the battle **50 times** and gives the attacker's and defender's **victory rates** and the draw rate, the average number of rounds, and the average **losses** and **survivors**, rounded to whole units.
13. The **round-by-round log** is that of one of the 50 battles, as an example: it does not describe the series.
14. The **debris field** is that of an average battle, both sides' wreckage, at your universe's debris rate.
15. Some talents add an **Expected loot** (the most a victory would bring, based on the stock the report read and the survivors' holds) or a **Hunt balance**.

### Limits
16. A simulation is refused beyond **5,000,000 units per side**, **50 battles**, or **10,000,000 deployments** (both sides' units × number of battles).

## Worked example

**Incomplete report**: your report saw the fleet, but neither defenses nor research. The simulator assumes zero defenses and technologies equal to yours. If the target actually has 20 Ion Batteries, your real chance of victory will be **lower** than shown.

**Size limit**: with 50 battles per simulation, the 10,000,000 deployment limit allows 200,000 units in all, for example 100,000 on each side. With 150,000 units on each side, (150,000 + 150,000) × 50 = 15,000,000: the simulation is refused.

## Common pitfalls

- **An incomplete report makes the simulator optimistic**: fill in the missing categories before trusting the result.
- **An old report lies**: a planet changes fast, spy again before you commit.
- **The defender may be stronger than expected**: its talents are not simulated.
- **Technologies matter**: if you know the target's, enter them.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [How combat works](/en/combat/how-combat-works)
- [Debris fields](/en/combat/debris)
- [Plunder](/en/combat/plunder)
