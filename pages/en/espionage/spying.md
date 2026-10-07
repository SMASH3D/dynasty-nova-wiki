---
wiki_id: 122
locale: "en"
path: "espionage/spying"
url: "https://wiki.dynastynova.com/en/espionage/spying"
title: "Spying"
description: "Sending Scouts: detail level, risks and counter-espionage."
tags: ["espionage"]
published: true
created: "2026-10-02T13:11:44.334Z"
updated: "2026-10-06T10:30:49.903Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Spying

> **In short**: send Scouts to a planet to get a report on its resources, fleet, defenses, buildings and research. What you see depends on your Espionage Technology gap with the target and on the number of Scouts. The defender is always warned, and your probes can be shot down.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Scout">

## Rules

### Sending probes
1. Espionage is done with **Scouts**, on an Espionage mission, or in one click with the quick spy button of the [galaxy view](/en/universe/galaxy-view). Spying on a cell also **reveals** its planet and owner in the galaxy view, hidden until then behind an unreadable script.
2. You can spy on a **protected** player. Espionage **does not count** towards the attack limit and does not end your new player protection.
3. Each **Espionage Technology** level cuts the hydrogen charged for a spy mission by 5%, down to −50%.
4. Spying on a player **on vacation** is possible: the position is mapped for you and your alliance, but the report reveals nothing (resources, fleet, defenses, buildings, research). Probes are never shot down and the absent player gets no alert.
5. During **maintenance**, espionage is suspended.

### Detail level
6. **Effective level** = (your Espionage Technology − the target's) + min(5, whole part of (number of Scouts / 2)), at least 0.
7. Depending on that level, the report reveals: **resources** from 1, **fleet** from 3, **defenses and missiles** from 5, **buildings** from 7, **research** from 9.
8. The Scout bonus **caps at +5** (reached with 10 probes).
9. The Informant network (offense) and Federated counterintelligence (defense) alliance talents each add 1 level per talent level.
10. At Espionage Technology **level 10**, a spied cell stays **discovered** for good.

### Risk to probes
11. **Destruction chance (in %)** = (2 × target's Espionage − yours) × number of ships stationed there × 0.05, capped between **5% and 25%**.
12. The risk drops to **0** if your level is at least **double** the target's, if there is **no ship** in orbit (defenses do not count), or if the target is uninhabited, abandoned or on vacation.
13. **A single roll for the whole wave**: all probes are destroyed, or none. The number of probes does not change the risk. There is no battle. Exception: the [Shadow](/en/dynasty/classes/shadow)'s Dropped Probes and Silent Hulls talents let part of a caught wave survive.
14. If your probes go down, a second roll decides whether you are **traced** (username and coordinates) or only **identified** (username).
15. The defender **always** receives an intrusion alert.

## Worked example

You have Espionage Technology 6, the target has level 4, and you send **6 Scouts**.
- Effective level: (6 − 4) + min(5, 3) = **5**: resources, fleet, defenses and missiles. Not buildings (that needs 7).
- With 10 Scouts: (6 − 4) + 5 = **7**: buildings appear.

Risk, if the target has 30 ships in orbit: (2 × 4 − 6) × 30 × 0.05 = 3%, raised to the **5%** minimum. With Espionage Technology 8 (double of 4), the risk drops to **0**.

## Detailed data

| Effective level | What the report reveals |
|---|---|
| 0 | Planet type, size and temperatures only |
| 1 to 2 | + resources |
| 3 to 4 | + fleet |
| 5 to 6 | + defenses and missiles |
| 7 to 8 | + buildings |
| 9 and above | + research |

| Scouts sent | 1 | 2 to 3 | 4 to 5 | 6 to 7 | 8 to 9 | 10 or more |
|---|---|---|---|---|---|---|
| Bonus | 0 | +1 | +2 | +3 | +4 | +5 |

## Common pitfalls

- **No point sending more than 10 probes**: the bonus caps at +5, and the risk does not depend on the number.
- **All or nothing**: if the roll fails, you lose every probe you sent.
- **The target knows**: they get an alert every time, and can identify you if your probes go down.
- **An empty orbit shoots no probe down**: with no ship stationed, the risk is zero, even with many defenses.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [Technologies list](/en/research/technologies)
- [The galaxy view](/en/universe/galaxy-view)
- [Alliance missions and station](/en/players/alliance-missions)
