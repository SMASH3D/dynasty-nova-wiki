---
wiki_id: 82
locale: "en"
path: "universe/galaxy-view"
url: "https://wiki.dynastynova.com/en/universe/galaxy-view"
title: "The galaxy view"
description: "Reading the galaxy view, system by system."
tags: ["universe"]
published: true
created: "2026-10-02T13:10:25.037Z"
updated: "2026-10-15T18:53:41.773Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# The galaxy view

> **In short**: the galaxy view shows one system at a time, position by position, then deep space and the Stellar Station. A cell that neither you nor your alliance has spied stays unreadable. For each discovered planet you see its owner, points, badges, moon and debris. It is also where you spy in one click, share a position with your alliance, bookmark it or launch a mission.
{.is-info}

> **Universe setting**: the number of attacks allowed against the same player, and its window, may differ from one universe to another.
> Default: **6 attacks per 24 h** · Redline: **6 attacks per 24 h**
{.is-info}

> **Universe setting**: the number of bookmarks may differ from one universe to another.
> Default: **10, 200 with Premium** · Redline: **10, 200 with Premium**
{.is-info}

![The galaxy view in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*The galaxy view in orbit layout: each planet has its own look, according to its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

![The galaxy view in list layout](/images/screenshots/english/galaxy-view.jpg)
*In list layout, positions not yet spied stay unreadable. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

### Getting around
1. The galaxy view shows **one system**: all its positions, then two more lines, **deep space** and the **Stellar Station**.
2. **Navigation**: ← / → arrow keys to change system, Ctrl + ← / → (⌘ on Mac) to change galaxy. The selector at the bottom also lets you type a galaxy and a system. After the last system you are back at the first one.
3. When opened, the view shows the system of your current planet.
4. Two layouts are offered on large screens: **Orbits** (the default) and **List**. Your choice is remembered.

### What you see
5. **Unexplored cells**: as long as neither you nor a member of your alliance has spied a position, everything there stays hidden. Alien script replaces the planet's and the owner's names, and the thumbnail stays grey. An unreadable cell may be free or taken: only spying tells. Spying is the only mission offered there.
6. **A spied cell stays revealed for good**: every spy mission that reaches its target reveals the position, for you and for your alliance. When you join an alliance, you bring it the cells you had already discovered.
7. On a discovered cell, a line shows the position, the thumbnail with its **badges** (table below), the planet's name (a crown tells mother planet from colony), the owner (green for an ally, red for an enemy), their **points** and military points, and the **"On vacation"** tag when relevant.
8. The owner may also read **"Abandoned"** (abandoned planet, see [Abandoning a colony](/en/universe/abandoning-a-planet)), **"Uninhabited"** (free position) or **"You"**.
9. On an unexplored cell, the name of a player who spied on or attacked you from that position may show, with what they did.
10. A **moon** is shown on a sub-line below its planet, with its diameter (and its fields if it is yours). It has its own card.
11. In Orbits layout, hovering a discovered planet shows its points, its **size** in fields, its **temperature**, its debris and its moon. In List layout, size and temperature are in the cell's card.
12. A banner announces a **comet shower** when the universe has one coming, with the galaxies hit and a countdown.

### Special lines
13. **Deep space** (position 16 on Redline): the line offers the **expedition**, if the universe allows them, and **recycling** of the debris found there. No planet ever stands there.
14. **Stellar Station** (position 17 on Redline): one per system. The **"Open the station"** button leads to the [Stellar Bank](/en/economy/stellar-bank) and, if you have an alliance, to its treasury.

### Acting from a cell
15. **Quick spy**: the button on the line sends **one Scout** at full speed from your current planet. You need a Scout available on that planet.
16. **Cell card**: a click opens the card, with the possible missions (spy, attack, colonize, transport, recycle, missile strike; on a moon: spy, attack, destroy, transport; deploy on your own planets and moons).
17. **Colonizing** and **recycling** require a cell already spied, by you or by your alliance.
18. **Share a position** with your alliance: each member opens it in their own galaxy view, with what they are allowed to see there. The message stays **30 days** in the channel.
19. A **star** adds the position (or the moon) to your **bookmarks**.
20. You can write to the owner of a discovered planet, except to an opponent controlled by the game.
21. While you are in vacation mode, no mission is offered.

## Worked example

On Redline you can attack the same player **6 times per 24 hours**. You have already attacked them twice: on their line, the badge reads **"Attacks remaining: 4 / 6"**. After 4 more attacks it will read 0 / 6, and any new attack will be refused until the first one leaves the 24-hour window.

## Detailed data

### Cell badges

Each corner of the thumbnail shows one badge at a time.

| Corner | Badge | Meaning |
|---|---|---|
| Top left | New player | Player in their first 7 days in the universe: no attacks, no missiles |
| Top left | Protected beginner / Too strong for you | Points gap between you too wide (see [Beginner protection](/en/players/beginner-protection)) |
| Top left | Attacks remaining: x / y | Attacks you have left against this player in the current window, shown from the first attack on |
| Top right | Debris field | Debris in orbit, to be recycled |
| Bottom right | Spied recently | You spied it less than 5 minutes ago |
| Bottom right | Discovered by an alliance member | Cell revealed by a member of your alliance spying it |
| Bottom left | Member of your alliance, Under a non-aggression pact, Under an alliance pact, Enemy | Relation between your alliance and theirs |
| Bottom left | AI player (PvE) | Planet of an opponent controlled by the game |

## Common pitfalls

- **An unreadable cell says nothing**: it may hide a player or be empty. Send a Scout before concluding.
- **No blind colonizing**: a position never spied cannot be colonized.
- **The attack counter is per player**: it counts all their planets together.
- **Quick spy leaves from the selected planet**: without a Scout on that planet, the button does not work.
- **Debris belongs to everyone**: a debris field you spot goes to whoever recycles it first.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Beginner protection](/en/players/beginner-protection)
- [Attack limit](/en/players/attack-limit)
- [Spying](/en/espionage/spying)
- [Empire view and bookmarks](/en/misc/empire-and-bookmarks)
- [Stellar Bank](/en/economy/stellar-bank)
