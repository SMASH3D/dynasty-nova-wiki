---
wiki_id: 93
locale: "en"
path: "economy/build-queue"
url: "https://wiki.dynastynova.com/en/economy/build-queue"
title: "Build queues"
description: "Queued orders, payment and cancellation."
tags: ["economy"]
published: true
created: "2026-10-02T13:10:46.440Z"
updated: "2026-10-15T16:10:12.425Z"
---

# Build queues

> **In short**: each planet has four queues: buildings, research, ships and defenses. Each queue takes 2 orders (5 with Premium), the running one included. Research runs one study at a time across your whole empire. A building or a research is paid only when it starts; if it cannot be paid then, it is dropped at no cost.
{.is-info}

> **Universe setting**: queue size may differ from one universe to another.
> Default and Redline: **2 orders**, **5 with Premium**
{.is-info}

## Rules

1. Four queues per planet: **buildings**, **research**, **ships**, **defenses**. Research studies run **one at a time across your whole empire**: each planet keeps its own queue, but a study placed on a colony waits until the one running on another planet is finished (the [Second Laboratory](/en/dynasty/common-tree) talent lets you run two).
2. Each queue takes **2 orders**, the running one included, or **5 with Premium**.
3. A **building** or a **research** is **paid when it starts**, not when queued. If the planet cannot afford it when it is due to start, the order is **dropped at no cost**.
4. Waiting orders show an **estimated duration**, recalculated when they start.
5. You cannot queue an upgrade and a demolition of the same building at the same time.
6. While the **Orbital Dock** is producing units, it can be neither upgraded nor demolished; while it is under work, no ship or defense can be ordered there. While a planet's **Innovation Center** is under work, no research can be started or queued from that planet; and while a research started from a planet is running, its Innovation Center cannot be upgraded.

### Cancellation
7. Cancelling an order **still waiting** costs nothing and refunds nothing: it has not been paid.
8. Cancelling a **running building or research** refunds **80% of the cost × (remaining time / total time)**, rounded down for each resource. The [Nothing Is Lost](/en/dynasty/dynasties) dynasty trait raises this rate to 85%.
9. Cancelling a **ship or defense order** refunds 80% of the units paid but not yet delivered, with no time proration. Units already delivered are kept.
10. **Required energy** is never refunded: it is not spent.

## Worked example

You cancel a building that cost 20,000 metal and 10,000 crystal, with 25% of its time elapsed.
- Time remaining: 75%.
- Refund: 80% × 75% = **60%**, so **12,000 metal and 6,000 crystal**.
- You lose 8,000 metal and 4,000 crystal: cancelling early already costs 20%.

## Common pitfalls

- **Cancelling is never free**: even right after the start, you lose at least 20%.
- **Keep resources for the next order**: an order that cannot be paid when its turn comes is dropped.
- **Premium lengthens all four queues**: buildings, research, ships and defenses all go to 5 orders.

## Related pages

- [Buildings list](/en/economy/buildings)
- [Demolishing a building](/en/economy/demolition)
- [Premium, shop and Stellar Points](/en/misc/premium)
