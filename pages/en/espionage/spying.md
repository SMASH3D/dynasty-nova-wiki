---
wiki_id: 122
locale: "en"
path: "espionage/spying"
url: "https://wiki.dynastynova.com/en/espionage/spying"
title: "Spying"
description: "Sending Scouts: detail level, shared vision, risks and alerts."
tags: ["espionage"]
published: true
created: "2026-10-02T13:11:44.334Z"
updated: "2026-10-15T18:53:01.030Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Spying

> **In short**: send Scouts to a planet or a moon to get a report on its resources, fleet, defenses, buildings and research. What you see depends on your Espionage Technology gap with the target and on how many Scouts you send. If the target has ships in orbit, your probes can be shot down.
{.is-info}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Scout">

## Rules

### Sending probes

1. Spying is done on an **Espionage** mission, with **Scouts only**: no other ship may go along. The quick spy button of the [galaxy view](/en/universe/galaxy-view) launches the same mission.
2. You can spy on any **planet or moon** that is not yours: a protected player, a member of your alliance, an uninhabited or abandoned planet. Deep space cannot be spied on.
3. Espionage **does not count** towards the attack limit and does not end your protection.
4. The hydrogen charged for a spy mission drops by **5%** per **Espionage Technology** level, down to **half** at level 10 (rounded down). The flight's actual consumption does not change.
5. During **maintenance**, espionage is suspended. If **you** are on vacation, you cannot send any mission.

### Discovered cells

6. A cell of the galaxy view stays unreadable until someone has spied on it for you. From your first spy run on, its planet and owner are shown, **with no time limit**.
7. **Shared alliance vision**: every cell a member spies on is discovered for **the whole alliance**. When you join an alliance, you bring it the cells you had already discovered. A cell known through the alliance reads "Discovered by an alliance member", without a date: only the discovery is shared, never the report.
8. The shared vision applies as soon as you join the alliance and is gone when you leave it. Your own discoveries stay yours.
9. Colonizing a planet or recycling a debris field requires the cell to have been spied on, by you **or by your alliance**. Your own planets and deep space are exempt.

### Detail level

10. The **effective level** of your espionage is:

$$N = \max\left(0,\ R_a - R_d + \min\left(5,\ \left\lfloor \frac{E}{2} \right\rfloor\right)\right)$$

- $N$: effective espionage level;
- $R_a$: your Espionage Technology level, plus your alliance's Informant network levels;
- $R_d$: the target's Espionage Technology level, plus its alliance's Federated counterintelligence levels;
- $E$: number of Scouts sent; $\lfloor\ \rfloor$: integer part.

11. Depending on that level, the report reveals: **resources** from 1, **fleet** from 3, **defenses and missiles** from 5, **buildings** from 7, **research** from 9. The planet's type, size and temperatures are always shown.
12. Each pair of Scouts adds 1 level, up to **+5 with 10 Scouts**. Beyond that the bonus stops growing: buildings and research need a real lead in Espionage Technology.
13. **Alliance talents**: **Informant network** adds 1 level to your Espionage Technology when you spy, **Federated counterintelligence** 1 level to that of your spied planets, per talent level (3 levels each, Intelligence branch). These levels count as research: they change the detail **and** the risk. They apply after **24 hours** in the alliance (see [Alliance missions and station](/en/players/alliance-missions)).
14. Some **dynasty talents** of the [Shadow](/en/dynasty/classes/shadow) read deeper or open the fleet and resources earlier. Those do not change the risk.

### Risk to the probes

15. The **chance of being shot down** is computed as follows, then kept between **5% and 25%**:

$$C = (2 \times R_d - R_a) \times V \times 0.05$$

- $C$: chance, in percent, that the wave is shot down;
- $R_d$ and $R_a$: the levels of rule 10;
- $V$: number of ships stationed on the spied planet or moon.

16. The risk is **zero** if your level reaches **twice** the target's, if there is **no ship** in orbit (defenses do not count), or if the target is uninhabited, abandoned or on vacation.
17. **A single roll for the whole wave**: either every probe is shot down, or none. The number of Scouts does not change the risk. There is no combat. Exceptions: some [Shadow](/en/dynasty/classes/shadow) talents bring part of a caught wave home.
18. A wave that is shot down **still** brings back its report, which shows how many probes were lost. Lost probes are destroyed for good.

### What the target sees

19. The target gets an **intrusion alert**: "Probe spotted", with no name, if the wave got through untouched.
20. If the wave was shot down, the alert **identifies** the spy (their username), and may also **trace its origin** (username and coordinates of the departure planet).
21. No alert on an abandoned planet, for a player on vacation, or for a player who switched intrusion alerts off in their report preferences.

## Worked example

You have Espionage Technology 6, the target level 4.
- With **6 Scouts**: (6 − 4) + min(5, 3) = **5**: resources, fleet, defenses and missiles. Not the buildings (that takes 7).
- With **10 Scouts**: (6 − 4) + 5 = **7**: the buildings show up. Research (9) stays out of reach, even with more probes.

Risk, if the target has 30 ships in orbit: (2 × 4 − 6) × 30 × 0.05 = 3, raised to the **5%** floor. With 100 ships: 10, so **10%**.

If your alliance holds Informant network level 2, your level counts as 6 + 2 = 8, twice 4: the risk drops to **0%**, and 6 Scouts now read at level **7** (buildings included).

## Detailed data

| Effective level | The report also reveals |
|---|---|
| 0 | nothing beyond the planet (type, size, temperatures) |
| 1 to 2 | resources |
| 3 to 4 | resources, fleet |
| 5 to 6 | resources, fleet, defenses and missiles |
| 7 to 8 | resources, fleet, defenses and missiles, buildings |
| 9 or more | resources, fleet, defenses and missiles, buildings, research |

| Scouts sent | 1 | 2 to 3 | 4 to 5 | 6 to 7 | 8 to 9 | 10 or more |
|---|---|---|---|---|---|---|
| Bonus | 0 | +1 | +2 | +3 | +4 | +5 |

Hydrogen charged for a spy mission, by Espionage Technology level (share of the normal cost):

| Level | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Charged | 100% | 95% | 90% | 85% | 80% | 75% |

| Level | 6 | 7 | 8 | 9 | 10 | 11 to 15 |
|---|---|---|---|---|---|---|
| Charged | 70% | 65% | 60% | 55% | 50% | 50% |

## Common pitfalls

- **No point sending more than 10 probes**: the bonus caps at +5, and the risk does not depend on the number.
- **All or nothing**: if the roll goes wrong, you lose the whole wave.
- **An empty orbit shoots nothing down**: with no ship stationed, the risk is zero, even behind many defenses.
- **The target's alliance talent counts too**: Federated counterintelligence raises both its protection and the risk to your probes.
- **Spying on an ally is allowed**: they get the alert like anyone else.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [The galaxy view](/en/universe/galaxy-view)
- [Technologies list](/en/research/technologies)
- [Alliance missions and station](/en/players/alliance-missions)
