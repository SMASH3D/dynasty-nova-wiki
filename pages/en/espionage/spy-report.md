---
wiki_id: 123
locale: "en"
path: "espionage/spy-report"
url: "https://wiki.dynastynova.com/en/espionage/spy-report"
title: "Reading a spy report"
description: "The report sections, what unlocks them, and the intrusion alert."
tags: ["espionage"]
published: true
created: "2026-10-02T13:11:46.231Z"
updated: "2026-10-02T16:38:32.118Z"
---

# Reading a spy report

> **In short**: a spy report always describes the targeted planet or moon, then opens one section per tier reached: resources, fleet, defenses and missiles, buildings, research. A section marked "Insufficient espionage level" was not read: it does not mean the target has nothing.
{.is-info}

## Rules

### The header

1. The report shows the **target** (planet or moon, coordinates, owner), your **departure base**, and what happened to your probes: "2 probes lost out of 10", or no loss.
2. An empty cell reads "Uninhabited planet". An abandoned planet shows no owner, but how many days it has been abandoned: its figures are today's, decay included.

### Characteristics, always shown

3. For a **planet**: its type, its size in fields, the fields still free and its minimum and maximum temperatures.
4. For a **moon**: its diameter, its fields, the free fields and the temperatures, which are its planet's.

### Sections, by effective level

5. Each section opens at its **effective level** tier (see [Spying](/en/espionage/spying)):
   - **Resources** from 1: metal, crystal and hydrogen on hand when the probes arrive, production up to that moment included (within storage limits);
   - **Fleet** from 3: the ships stationed on the spied body;
   - **Defenses** and **Missiles** from 5: missiles are listed apart, since they do not fight;
   - **Buildings** from 7: the level of each building;
   - **Research** from 9: the level of each of the player's research.
6. A section that was **not read** shows "Insufficient espionage level". A section that was read but is empty shows "Nothing detected": then the target really has nothing.
7. For a player **on vacation**, the report gives the planet and its owner, but **no section**, whatever your lead.
8. Some dynasty talents add lines to the report (target activity, neighbouring system, production) or blur it (rounded fleet, partly hidden stock): see the [Shadow](/en/dynasty/classes/shadow) and the [Oracle](/en/dynasty/classes/oracle).

### Your reports

9. The game keeps your **10 latest spy reports** on a given target; older ones are deleted.
10. A report can be **shared** with your alliance (see [Messages and reports](/en/players/messages-and-reports)) and **imported** into the [battle simulator](/en/combat/simulator).

### The intrusion alert (target side)

11. The spied player gets an **intrusion alert** on the targeted planet or moon. It carries one of three levels:
    - **Unknown intruder**: the wave got through, the alert only says "Probe spotted";
    - **Intruder identified**: the wave was shot down, the alert gives the spy's username;
    - **Origin traced**: in addition, the coordinates of the planet the probes left from.
12. The alert also shows how many probes your defense shot down.

## Worked example

You send **2 Scouts**. The report shows resources and fleet, but the defenses are marked "Insufficient espionage level".
- The report reached tier 3 with a +1 probe bonus: your lead on this target is at least 3 − 1 = **2**.
- To read the **defenses** (tier 5), you need a bonus of 5 − 2 = 3, so **6 Scouts**.
- For the **buildings** (tier 7), you need the maximum +5 bonus: **10 Scouts**.
- **Research** (tier 9) would take +7: beyond what probes can give. You need more Espionage Technology.

## Common pitfalls

- **"Insufficient espionage level" ≠ nothing**: never conclude that a planet is undefended because the section was not read.
- **Reports age**: the target produces, builds and moves its fleet. Spy right before attacking.
- **An empty report may mean vacation**: check the status in the galaxy view.
- **Planet and moon are two targets**: the fleet stationed on the moon does not show in the planet's report, and vice versa.

## Related pages

- [Spying](/en/espionage/spying)
- [Plunder](/en/combat/plunder)
- [Battle simulator](/en/combat/simulator)
- [Messages and reports](/en/players/messages-and-reports)
