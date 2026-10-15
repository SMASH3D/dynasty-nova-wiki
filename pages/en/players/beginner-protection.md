---
wiki_id: 127
locale: "en"
path: "players/beginner-protection"
url: "https://wiki.dynastynova.com/en/players/beginner-protection"
title: "Beginner protection"
description: "Who can attack whom: newcomer protection and point tiers."
tags: ["players"]
published: true
created: "2026-10-02T13:11:54.297Z"
updated: "2026-10-15T18:53:20.884Z"
---

# Beginner protection

> **In short**: two protections keep players who are too unequal away from each other. **Newcomer protection** makes you unattackable for your first 7 days in a universe, as long as you attack nobody. **Point protection** forbids any attack between two players whose point gap is too wide, in either direction.
{.is-info}

> **Universe setting**: point tiers and the inactivity delay may differ from one universe to another.
> Default: **1:3** under 500 points, **1:5** under 5,000, **1:10** under 500,000, inactive after **14 days** · Redline: same tiers, inactive after **7 days**
{.is-info}

## Rules

### Newcomer protection
1. For **7 days** from your **first arrival** in a universe, nobody can attack you or fire missiles at you. This duration is the same in every universe.
2. The time left is shown at the top of the screen ("Newcomer protection"). Your planets and your card carry the "New player" badge, with the end date.
3. **Launching an attack or a missile salvo ends it, for good**, whatever the target (player, non-human player, abandoned planet). A warning is shown before you confirm. Recalling the fleet does not give the protection back.
4. Espionage, transport, stationing, recycling and colonization do not remove it, in either direction: a newcomer can be spied on and supplied.
5. It applies **per universe**. Leaving a universe and coming back does not renew it: the first arrival date stays the same.
6. Non-human (PvE) players never have it.

### Point protection
7. An attack is forbidden when the stronger of the two players has **at least N times** the points of the weaker one, N depending on the tier of the **weaker** player:
   - under 500 points: **1:3**;
   - from 500 to under 5,000 points: **1:5**;
   - from 5,000 to under 500,000 points: **1:10**;
   - 500,000 points or more: **no protection at all**, whatever the gap.
8. The rule works **both ways**: the small player is protected from the big one, and the small one cannot attack the big one either.
9. A boundary belongs to the upper tier: at exactly 500 points you are in 1:5. Exactly N times more points is enough to block.
10. The points used are the ranking **total**, rounded down (see [Rankings and points](/en/players/rankings)).
11. A player with **0 points** cannot be attacked by any player who has some; two players with 0 points may fight each other.
12. It applies to **attacks** and **missile salvos**. Espionage, transport and recycling stay free.
13. An **inactive** defender (see [Inactivity](/en/players/inactivity)) loses this protection: anyone may attack them, whatever the gap, including a much smaller player. Only the defender's inactivity matters.

### Both together
14. The two protections **stack**: an attack must clear both, then the [attack limit](/en/players/attack-limit). Newcomer protection does not depend on points; point protection does not depend on seniority.
15. In the [galaxy view](/en/universe/galaxy-view), attack, missiles and moon destruction are not offered against a player covered by either protection.

## Worked example

Active players, newcomer protection over, default tiers:

| Player A | Player B | Tier of the weaker | Gap | Attack possible? |
|---|---|---|---|---|
| 400 points | 1,000 points | 1:3 (< 500) | 2.5 | yes, both ways |
| 400 points | 1,200 points | 1:3 (< 500) | 3 | **no, either way** |
| 400 points | 1,500 points | 1:3 (< 500) | 3.75 | **no, either way** |
| 0 points | 50 points | 1:3 (< 500) |  | **no, either way** |
| 0 points | 0 points | 1:3 (< 500) |  | yes, both ways |
| 500 points | 2,400 points | 1:5 (< 5,000) | 4.8 | yes, both ways |
| 6,000 points | 50,000 points | 1:10 (< 500,000) | 8.33 | yes, both ways |
| 6,000 points | 80,000 points | 1:10 (< 500,000) | 13.33 | **no, either way** |
| 6,000 points | 80,000 points (inactive) | 1:10 (< 500,000) | 13.33 | A may attack B (inactive), not the reverse |
| 600,000 points | 5,000,000 points | none (≥ 500,000) | 8.33 | yes, both ways |

## Common pitfalls

- **The stronger player is protected too**: a small player cannot attack a much bigger one, unless that player is inactive.
- **Your first attack costs you the rest of your 7 days**, even against an abandoned planet.
- **Inactivity lifts point protection**: before a long absence, think of [vacation mode](/en/players/vacation-mode).
- **Points count everything**: economy, research and military. Building a lot can move you to another tier.

## Related pages

- [Rankings and points](/en/players/rankings)
- [Attack limit](/en/players/attack-limit)
- [Vacation mode](/en/players/vacation-mode)
- [Inactivity](/en/players/inactivity)
- [The galaxy view](/en/universe/galaxy-view)
