---
wiki_id: 128
locale: "en"
path: "players/attack-limit"
url: "https://wiki.dynastynova.com/en/players/attack-limit"
title: "Attack limit"
description: "6 attacks on the same player per 24-hour window."
tags: ["players"]
published: true
created: "2026-10-02T13:11:56.425Z"
updated: "2026-10-02T16:38:39.212Z"
---

# Attack limit

> **In short**: you may attack the same player at most **6 times per 24-hour window**, all their planets and moons together, missile salvos included. The window opens at your first attack on them and does not slide. The attack that would go over the limit is refused at sending.
{.is-info}

> **Universe setting**: the number of attacks and the window length may differ from one universe to another; a maximum of 0 turns the rule off.
> Default: **6 attacks per 24 h** · Redline: **6 attacks per 24 h**
{.is-info}

## Rules

1. The limit applies to **one attacker and one targeted player**: all the targeted player's planets and moons count together. Each player you attack has their own counter.
2. Counted: **fleet attacks** and **missile salvos** (a salvo counts as one attack, whatever the number of missiles).
3. Not counted: espionage, transport, stationing, recycling and moon destruction. Once your quota against a player is used up, the galaxy view no longer offers the attack, missiles or moon destruction against them.
4. The attack is counted **when it is sent**. The one that would go over the maximum is **refused at sending**.
5. The **window is fixed**: it opens at your first attack on that player and lasts 24 hours. Once it has elapsed the counter goes back to zero, and the next attack opens a new window.
6. **Recalling** an attack fleet before it arrives gives the slot back. A missile salvo cannot be recalled: its slot is used up.
7. **Abandoned planets** are not concerned: they no longer have an owner. Non-human (PvE) players are, like human players.
8. Alliance wars and pacts change nothing about the limit. Members of your own alliance cannot be attacked anyway.
9. The galaxy view shows how many attacks you have left against each player.

## Worked example

Universe set to 6 attacks per 24 h, attacks on the same player X:

| Time | Action against X | Attacks left |
|---|---|---|
| Monday 10:00 | Fleet attack (the window opens until Tuesday 10:00) | 5 |
| Monday 12:00 | Fleet attack | 4 |
| Monday 14:00 | Missile salvo | 3 |
| Monday 15:00 | Fleet attack, recalled one hour later: slot given back | 3 |
| Monday 18:00 | Fleet attack | 2 |
| Monday 19:00 | Fleet attack | 1 |
| Monday 20:00 | Fleet attack | 0 |
| Monday 23:00 | Fleet attack: **refused at sending** | 0 |
| Tuesday 10:00 | The window has elapsed | 6 |
| Tuesday 11:00 | Fleet attack (the window opens until Wednesday 11:00) | 5 |

## Common pitfalls

- **The window does not slide**: it starts at your first attack, not your last. But it only reopens with your next attack.
- **Missiles count**: a salvo is a full attack, and it cannot be recalled.
- **All their planets count together**: attacking two colonies of the same player uses two slots.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Missiles](/en/defense/missiles)
- [The galaxy view](/en/universe/galaxy-view)
- [Plunder](/en/combat/plunder)
