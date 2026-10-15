---
wiki_id: 179
locale: "en"
path: "economy/stellar-bank"
url: "https://wiki.dynastynova.com/en/economy/stellar-bank"
title: "Stellar Bank"
description: "Trading your resources for Credits, and your Credits for resources."
tags: ["economy"]
published: true
created: "2026-10-15T16:27:27.035Z"
updated: "2026-10-15T16:29:41.185Z"
---

# Stellar Bank

> **In short**: at the Stellar Station of your system, you sell metal, crystal or hydrogen for **Credits**, then use those Credits to buy the resource you lack. The bank is the only counterpart: every trade moves the rate, and the more a resource flows in, the less it is worth. Credits cannot be bought with real money.
{.is-info}

## Rules

### Access
1. The bank sits at the **Stellar Station**, the last row of every system in the [galaxy view](/en/universe/galaxy-view) ("Open the station" button). The station has two desks: the Stellar Bank and the [alliance treasury](/en/players/alliance-missions).
2. The bank **opens on the universe's 7th day**. Before that, the page says it has not opened yet.
3. **Credits** are the bank's currency. They belong to each universe, have no cap, do not erode and nobody can steal them. They cannot be bought with real money and have nothing to do with Stellar Points.
4. Selling and buying are impossible in [vacation mode](/en/players/vacation-mode).

### Selling
5. Selling means **sending cargo ships** to your system's station, from a planet or moon with an **Orbital Dock**. Only **Cargo Shuttles and Stellar Freighters** can go; one shipment carries 1 to 3 resources.
6. The trip takes **1 hour out and 1 hour back**, whatever the distance, **with no hydrogen** and **no recall**. It takes a fleet slot.
7. The **price is set at departure**, at the rate of the moment. The Credits are paid when the cargo ships reach the station, and they come home empty.
8. The bank takes a **10% tax** on every sale.
9. A planet with an announced attack on it can no longer sell.

### Buying
10. You buy 1 to 3 resources with your Credits, debited at once, at the rate of the moment. **No tax** on a purchase: the price already climbs with every unit taken.
11. Delivery arrives **one hour later** on the chosen planet, in one go. It is not a fleet: it cannot be intercepted, and it is **not limited by the planet's storage**.
12. If the planet is no longer yours on arrival, the delivery goes to your home planet.
13. If your balance does not cover the whole purchase, nothing is bought. A line the bank cannot serve (reserve too low, amount too small) is simply skipped.

### The rate
14. Each resource has its **reserve** in the bank: a stock of that resource facing a stock of Credits. Selling adds units to the reserve and takes Credits out: the rate goes down. Buying does the opposite: the rate goes up.
15. You cannot swap one resource directly for another: you sell the first, then buy the second. The cross rates shown are indicative.
16. A **quote** shows before every trade: Credits received or spent, tax, realised rate, rate before and after.
17. The page shows rates over 24 hours, 7 days or 30 days, the day's and week's trends, and the history of your trades.

## Formulas

For a resource whose reserve holds $R$ units facing $M$ Credits:

$$\text{rate} = \frac{M}{R} \times 1{,}000$$

$$\text{selling } \Delta \text{ units}: \quad \text{gross} = \frac{M \times \Delta}{R + \Delta}, \quad \text{received} = \text{gross} - 10\% \times \text{gross}$$

$$\text{buying } q \text{ units}: \quad \text{cost} = \frac{M \times q}{R - q}$$

- $R$: units of the resource in the bank's reserve.
- $M$: Credits in the reserve.
- $\Delta$: units sold; $q$: units bought (always fewer than $R$).
- rate: Credits per 1,000 units.

Credits count to the hundredth, and every rounding goes the bank's way. The tax stays in the reserve.

## Worked example

A metal reserve of 1,000,000 units facing 1,000 Credits (rate: 1.00 Credit per 1,000 metal), a crystal reserve of 666,666 units facing 1,000 Credits (rate: 1.50).

**Selling 100,000 metal**
- Gross: 1,000 × 100,000 / 1,100,000 = **90.90 Credits**.
- Tax: 10% = **9.09**. Received when the cargo ships arrive: **81.81 Credits**.
- Realised rate: 0.82 Credit per 1,000 metal, against 1.00 at the shown rate. The metal rate then drops to about 0.83.

**Buying crystal with those 81.81 Credits**
- At most **50,415 crystal**: 1,000 × 50,415 / 616,251 = 81.81.
- Realised rate: about 1.62 Credits per 1,000 crystal, against 1.50 at the shown rate.

Outcome: 100,000 metal buy 50,415 crystal. The tax and the rate slipping on a big trade cost a lot: 10,000 metal alone fetch 8.91 Credits, so 0.89 per 1,000.

## Common pitfalls

- **Big volumes slip**: the more you sell at once, the less each unit fetches. Several small, spaced sales give the rate time to recover with other players' trades.
- **No turning back**: a sale leaves with no recall, at a price set at departure.
- **Two kinds of "credits"**: bank Credits are earned by selling resources; they have nothing to do with the shop's packs.
- **Private universe**: a player excluded from a private universe loses their Credits in that universe and any delivery under way.

## Related pages

- [Resources](/en/economy/resources)
- [Alliance missions and station](/en/players/alliance-missions)
- [The galaxy view](/en/universe/galaxy-view)
- [Private universes](/en/misc/private-universes)
