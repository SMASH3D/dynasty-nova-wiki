---
wiki_id: 100
locale: "en"
path: "research/stellar-collaboration"
url: "https://wiki.dynastynova.com/en/research/stellar-collaboration"
title: "Stellar Collaboration"
description: "Networking your Innovation Centers."
tags: ["research"]
published: true
created: "2026-10-02T13:10:59.894Z"
updated: "2026-10-02T17:40:56.528Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Stellar Collaboration

> **In short**: Stellar Collaboration pools the Innovation Centers of your other planets to shorten your research. At level N, it adds to the Center studying the N best Centers of your other planets, as long as they are at least as advanced as it is. It never changes the cost.
{.is-info}

<img src="/images/illustrations/research/collaboration-stellaire.jpg" width="180" alt="Stellar Collaboration">

## Rules

1. Requirements: **Innovation Center 10, Quantum Computing 8, Hyperspace Technology 8**. Maximum level: 10.
2. At **level N**, a study pools up to **N Innovation Centers** from your **other** planets in the same universe.
3. A Center is only kept if its level is **at least equal** to that of the planet starting the research. Among those, the **most advanced** come first.
4. **Effective level** = Center of the planet starting the research + sum of the Centers kept. That is what goes into the duration formula (see [Technologies list](/en/research/technologies)).
5. The network is set **when the study starts**, or when a queued study takes its turn. Upgrading a Center afterwards does not change a study already running. A Center being upgraded counts at its current level.
6. Stellar Collaboration **does not change the cost** of research, and pooled Centers stay free: they are neither locked nor used up.
7. Only one study runs at a time in the empire: the network speeds up that study, it does not start others.

### Theorist talents

Some talents of the Theorist class change these rules (values on [The Theorist](/en/dynasty/classes/theorist)):

- **Uplink**: accepts Centers a few levels below the one studying.
- **Distant Antenna**: also accepts Centers below the one studying.
- **One More Lab**: pools one more Center than Stellar Collaboration allows.
- **Field Labs**: each of your pooled Centers counts extra levels.
- **Mother Lab**: the Center studying counts extra levels.
- **University Exchange**: adds the best Center of a member of your alliance, if it fits the tolerance.
- **Living Network**: recomputes a running study when a pooled Center gains a level, never slower.

## Worked example

You research **Hyperspace Technology level 8** (512,000 crystal, 256,000 hydrogen). Your planets have Innovation Centers at levels **10, 9, 8 and 6**. Stellar Collaboration level **2**.

Started from the planet with the level **8** Center:
- Centers kept: the 2 best among those at level 8 or more, so **10 and 9**. The level 6 Center is too weak.
- Effective level: 8 + 10 + 9 = **27**.
- Duration: 512,000 / (1,000 × (1 + 27)) h, that is **18 h 17 min 9 s**, instead of 2 d 8 h 53 min 20 s with the local Center alone.

Started from the planet with the level **10** Center:
- No other Center reaches level 10: the network adds nothing, effective level **10**.
- Duration: **1 d 22 h 32 min 44 s**. Starting from the level 8 Center is faster.

## Detailed data

### Speed gain

Effective level and speed compared with the local Center alone, when all Centers have the same level and Stellar Collaboration is at least the number of pooled Centers.

| Pooled Centers (all at the same level) | Centers at level 8 | Centers at level 10 | Centers at level 12 |
|---|---|---|---|
| 0 | 8 (×1) | 10 (×1) | 12 (×1) |
| 1 | 16 (×1.89) | 20 (×1.91) | 24 (×1.92) |
| 2 | 24 (×2.78) | 30 (×2.82) | 36 (×2.85) |
| 3 | 32 (×3.67) | 40 (×3.73) | 48 (×3.77) |
| 4 | 40 (×4.56) | 50 (×4.64) | 60 (×4.69) |
| 5 | 48 (×5.44) | 60 (×5.55) | 72 (×5.62) |
| 6 | 56 (×6.33) | 70 (×6.45) | 84 (×6.54) |
| 7 | 64 (×7.22) | 80 (×7.36) | 96 (×7.46) |
| 8 | 72 (×8.11) | 90 (×8.27) | 108 (×8.38) |
| 9 | 80 (×9) | 100 (×9.18) | 120 (×9.31) |
| 10 | 88 (×9.89) | 110 (×10.09) | 132 (×10.23) |

### Stellar Collaboration cost

| Level | Metal | Crystal | Hydrogen | Duration with a single Center 10 | Points |
|---|---|---|---|---|---|
| 1 | 240,000 | 400,000 | 160,000 | 2 d 10 h 10 min 55 s | 800 |
| 2 | 480,000 | 800,000 | 320,000 | 4 d 20 h 21 min 49 s | 1,600 |
| 3 | 960,000 | 1,600,000 | 640,000 | 9 d 16 h 43 min 38 s | 3,200 |
| 4 | 1,920,000 | 3,200,000 | 1,280,000 | 19 d 9 h 27 min 16 s | 6,400 |
| 5 | 3,840,000 | 6,400,000 | 2,560,000 | 38 d 18 h 54 min 33 s | 12,800 |
| 6 | 7,680,000 | 12,800,000 | 5,120,000 | 77 d 13 h 49 min 5 s | 25,600 |
| 7 | 15,360,000 | 25,600,000 | 10,240,000 | 155 d 3 h 38 min 11 s | 51,200 |
| 8 | 30,720,000 | 51,200,000 | 20,480,000 | 310 d 7 h 16 min 22 s | 102,400 |
| 9 | 61,440,000 | 102,400,000 | 40,960,000 | 620 d 14 h 32 min 44 s | 204,800 |
| 10 | 122,880,000 | 204,800,000 | 81,920,000 | 1,241 d 5 h 5 min 27 s | 409,600 |

## Common pitfalls

- **Start from the right Center**: too high a local Center rules out weaker ones; too low a local Center lowers the base. Compare before starting, as in the example.
- **One level per Center**: at level 1, only the best eligible Center counts; each level adds one.
- **You need several equipped planets**: without another Innovation Center of a high enough level, Collaboration does nothing.
- **No effect midway**: upgrade your Centers before starting a long study, not during it.
- **Moons do not count**: an Innovation Center can only be built on a planet.

## Related pages

- [Technologies list](/en/research/technologies)
- [Tech tree](/en/research/tech-tree)
- [The Theorist](/en/dynasty/classes/theorist)
- [Colonization](/en/universe/colonization)
