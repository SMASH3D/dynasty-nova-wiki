---
wiki_id: 19
locale: "fr"
path: "economy/energy"
url: "https://wiki.dynastynova.com/fr/economy/energy"
title: "L'énergie"
description: "Produire et consommer de l'énergie, déficit et taux de fonctionnement."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:22.054Z"
updated: "2026-10-02T17:40:48.927Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# L'énergie

> **En bref** : vos mines consomment de l'énergie, vos centrales en produisent. Tant que la production couvre la consommation, tout tourne à plein régime. Dès qu'elle ne suffit plus, **les trois mines** ralentissent dans la même proportion. L'énergie ne se stocke pas.
{.is-info}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Capteurs photovoltaïques"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Réacteur thermonucléaire"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Collecteur solaire">

## Règles

1. **Capteurs photovoltaïques** : 20 × N × 1,1^N énergie au niveau N, multipliés par 1 + température actuelle / 100 quand la température actuelle de la planète est positive. La température actuelle suit le mois du calendrier (voir [Planètes](/fr/universe/planets)).
2. **Réacteur thermonucléaire** : 30 × N × (1,05 + 0,01 × Science Énergétique)^N énergie, en **consommant de l'hydrogène** : 10 × N × 1,1^N par heure, multipliés par la vitesse d'économie de l'univers.
3. **Collecteur solaire** : vaisseau qui reste en orbite et produit, chacun, température maximale / 4 + 20 énergie, arrondi à l'inférieur et jamais négatif. Il peut être détruit en combat.
4. **Consommation** : l'Excavateur minéral, l'Extracteur cristallin et le Condensateur d'hydrogène consomment chacun 10 × N × 1,1^N énergie. La vitesse d'économie ne change pas la consommation.
5. **Déficit** : si la consommation dépasse la production, la production des trois mines, bonus compris, est multipliée par production / consommation. Le détail de production affiche une ligne « Déficit d'énergie ». Le revenu de la Base planetaire n'est pas touché.
6. **Taux de fonctionnement** : chaque mine se règle par pas de 10 % ; production et consommation baissent ensemble. Le Réacteur, lui, tourne toujours à plein, sauf talent qui le permet.
7. L'énergie **ne se stocke pas** : elle se calcule à chaque instant.
8. Certains bâtiments et recherches demandent une **énergie requise** pour être lancés (Station de réparation, Modulateur planétaire, Manipulation Gravitationnelle) : c'est un seuil de production, pas une dépense.

## Exemple chiffré

Capteurs photovoltaïques 13 un jour à 10 °C, Excavateur minéral 13, Extracteur cristallin 13, Condensateur d'hydrogène 10 :
- Production : 20 × 13 × 1,1^13 × 1,1 = **987** énergie.
- Consommation : 448 + 448 + 259 = **1 155**.
- Couverture : 987 / 1 155 = **85,5 %**. L'Excavateur, qui devrait produire 1 346 métal par heure, n'en produit plus que **1 150**.
- Monter une mine d'un niveau aggraverait le déficit : il vaut mieux monter les Capteurs.

**Collecteurs solaires** : sur une planète dont la température maximale est de 60 °C, chacun produit 60 / 4 + 20 = **35** énergie ; 10 Collecteurs en produisent **350**.

## Données détaillées

### Consommation des mines et production des Capteurs

Les Capteurs sont donnés à 0 °C ou moins ; à une température actuelle T positive, multipliez par 1 + T / 100.

| Niveau | Consommation de chaque mine | Capteurs photovoltaïques (0 °C) |
|---|---|---|
| 1 | 11 | 22 |
| 2 | 24 | 48 |
| 3 | 39 | 79 |
| 4 | 58 | 117 |
| 5 | 80 | 161 |
| 6 | 106 | 212 |
| 7 | 136 | 272 |
| 8 | 171 | 342 |
| 9 | 212 | 424 |
| 10 | 259 | 518 |
| 11 | 313 | 627 |
| 12 | 376 | 753 |
| 13 | 448 | 897 |
| 14 | 531 | 1 063 |
| 15 | 626 | 1 253 |
| 16 | 735 | 1 470 |
| 17 | 859 | 1 718 |
| 18 | 1 000 | 2 001 |
| 19 | 1 162 | 2 324 |
| 20 | 1 345 | 2 690 |
| 21 | 1 554 | 3 108 |
| 22 | 1 790 | 3 581 |
| 23 | 2 059 | 4 118 |
| 24 | 2 363 | 4 727 |
| 25 | 2 708 | 5 417 |
| 26 | 3 098 | 6 197 |
| 27 | 3 539 | 7 079 |
| 28 | 4 037 | 8 075 |
| 29 | 4 600 | 9 200 |
| 30 | 5 234 | 10 469 |

### Réacteur thermonucléaire

| Niveau | Énergie (Science Énergétique 3) | Énergie (6) | Énergie (9) | Énergie (12) | Hydrogène consommé par heure (vitesse ×1) |
|---|---|---|---|---|---|
| 1 | 32 | 33 | 34 | 35 | 11 |
| 2 | 69 | 73 | 77 | 82 | 24 |
| 3 | 113 | 123 | 133 | 144 | 39 |
| 4 | 163 | 182 | 202 | 224 | 58 |
| 5 | 220 | 252 | 288 | 328 | 80 |
| 6 | 285 | 336 | 395 | 461 | 106 |
| 7 | 359 | 435 | 525 | 630 | 136 |
| 8 | 444 | 553 | 684 | 842 | 171 |
| 9 | 539 | 690 | 878 | 1 109 | 212 |
| 10 | 647 | 851 | 1 112 | 1 442 | 259 |
| 11 | 769 | 1 040 | 1 394 | 1 855 | 313 |
| 12 | 906 | 1 259 | 1 734 | 2 368 | 376 |
| 13 | 1 060 | 1 514 | 2 142 | 3 002 | 448 |
| 14 | 1 233 | 1 810 | 2 629 | 3 783 | 531 |
| 15 | 1 427 | 2 153 | 3 212 | 4 742 | 626 |
| 16 | 1 644 | 2 549 | 3 905 | 5 918 | 735 |
| 17 | 1 887 | 3 006 | 4 730 | 7 357 | 859 |
| 18 | 2 157 | 3 533 | 5 710 | 9 114 | 1 000 |
| 19 | 2 459 | 4 140 | 6 871 | 11 256 | 1 162 |
| 20 | 2 796 | 4 837 | 8 246 | 13 863 | 1 345 |

### Collecteur solaire

| Température maximale | Énergie par Collecteur |
|---|---|
| -120 °C | 0 |
| -100 °C | 0 |
| -80 °C | 0 |
| -60 °C | 5 |
| -40 °C | 10 |
| -20 °C | 15 |
| 0 °C | 20 |
| 20 °C | 25 |
| 40 °C | 30 |
| 60 °C | 35 |
| 80 °C | 40 |
| 100 °C | 45 |
| 120 °C | 50 |
| 140 °C | 55 |
| 160 °C | 60 |

## Pièges fréquents

- **Une mine de plus peut faire baisser la production totale** : sans centrale correspondante, le déficit ralentit les trois mines.
- **La production solaire bouge dans le mois** : la température actuelle varie, et avec elle les Capteurs. Gardez une marge.
- **Les Collecteurs solaires sont vulnérables** : ils peuvent être détruits en combat.
- **Le Réacteur coûte de l'hydrogène** : sa consommation est retirée de votre production d'hydrogène.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Formules de l'économie](/fr/economy/formulas)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Liste des vaisseaux](/fr/fleet/ships)
