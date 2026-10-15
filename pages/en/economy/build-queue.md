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
updated: "2026-10-15T18:52:43.411Z"
---

# Build queues

> **In short**: each planet has four queues: buildings, research, ships and defenses. Each queue takes 2 orders (5 with Premium), the running one included. Research only moves one study at a time across your whole empire. A building or a research is paid only when it starts; if it cannot be paid then, it is dropped at no cost.
{.is-info}

> **Universe setting**: queue size may differ from one universe to another.
> Default: **2 orders**, **5 with Premium** · Redline: **2 orders**, **5 with Premium**
{.is-info}

## Rules

1. Four queues per planet: **buildings**, **research**, **ships**, **defenses**. Each takes **2 orders**, the running one included, or **5 with Premium**.
2. **Research**: studies run **one at a time across your whole empire**. Each planet keeps its own queue, but a study placed on a colony waits until the one running on another planet is finished, in the order you placed them. The [Second Laboratory](/en/dynasty/common-tree) talent lets you run two.
3. A **building** or a **research** is **paid when it starts**, not when queued. If the planet cannot afford it when it is due to start, the order is **dropped at no cost**. Requirements, though, are checked when you queue, at the levels your buildings and research will have once the orders ahead are done.
4. A **ship** or **defense** order is only accepted if the planet can pay for all of it when you place it. Units are then paid **one at a time**, as each one goes into production; if the planet can no longer pay for the next unit, the order stops there and the units already built are kept.
5. Ordering the same ship or defense as the last waiting order adds to that order, without taking a queue slot.
6. Waiting orders show an **estimated duration**, recalculated when they start.
7. An upgrade cannot wait behind a demolition of the same building, nor a demolition behind its upgrade.
8. While the **Orbital Dock** is producing units, it can be neither upgraded nor demolished; while it is under work, no ship or defense can be ordered there. While a planet's **Innovation Center** is under work, no research can be started or queued from that planet; and while a research started from a planet is running, its Innovation Center cannot be upgraded.

### Cancelling
9. Cancelling an order **still waiting** costs nothing and refunds nothing: it has not been paid.
10. Cancelling a **running building or research** refunds **80% of the cost × (remaining time / total time)**, rounded down for each resource. The [Nothing Is Lost](/en/dynasty/dynasties) dynasty trait raises this rate to 85%.
11. Cancelling a **ship or defense order** refunds 80% of the unit paid but not yet delivered, with no time proration. Units already delivered are kept.
12. Cancelling a **demolition** refunds nothing: it cost nothing.
13. **Required energy** is never refunded: it is not spent.

## Worked example

You cancel a building that cost 20,000 metal and 10,000 crystal, with 25% of its time elapsed.
- Remaining time: 75%.
- Refund: 80% × 75% = **60%**, so **12,000 metal and 6,000 crystal**.
- You lose 8,000 metal and 4,000 crystal: cancelling early already costs 20%.

## Common pitfalls

- **Cancelling is never free**: even right after the start, you lose at least 20%.
- **Keep resources for the next order**: a building or research that cannot be paid on its turn is dropped, a unit order stops.
- **One research at a time for the whole empire**: a colony does not run a second study alongside.
- **Premium lengthens all four queues**: buildings, research, ships and defenses all go to 5 orders.

## Related pages

- [Buildings list](/en/economy/buildings)
- [Demolishing a building](/en/economy/demolition)
- [Economy formulas](/en/economy/formulas)
- [Premium, shop and Stellar Points](/en/misc/premium)
