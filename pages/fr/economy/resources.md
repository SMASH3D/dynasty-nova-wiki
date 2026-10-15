---
wiki_id: 18
locale: "fr"
path: "economy/resources"
url: "https://wiki.dynastynova.com/fr/economy/resources"
title: "Les ressources"
description: "Métal, cristal, hydrogène et énergie."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:20.081Z"
updated: "2026-10-15T16:10:29.402Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Les ressources

> **En bref** : trois ressources se stockent, le métal, le cristal et l'hydrogène. Vos mines les produisent en continu, même quand vous n'êtes pas connecté, et chaque planète a son propre stock. L'énergie, quatrième ressource, ne se stocke pas : elle fait tourner les mines.
{.is-info}

> **Paramètre d'univers** : la vitesse d'économie multiplie la production des mines et de la Base planetaire.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Métal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Cristal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogène"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Énergie">

## Règles

1. **Métal** : produit par l'Excavateur minéral, 30 × N × 1,1^N par heure au niveau N.
2. **Cristal** : produit par l'Extracteur cristallin, 20 × N × 1,1^N par heure.
3. **Hydrogène** : produit par le Condensateur d'hydrogène, 10 × N × 1,1^N par heure, multiplié par un **facteur de température** qui vaut 1,44 − 0,004 × la température maximale de la planète. Une planète froide produit davantage ; au-delà de 360 °C, plus rien.
4. **Énergie** : produite par les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires, consommée par les trois mines. Elle ne se stocke pas (voir [L'énergie](/fr/economy/energy)).
5. La **Base planetaire** (Base Coloniale sur une colonie) ajoute **20 métal et 10 cristal par heure**, multipliés par la vitesse d'économie.
6. La production est **continue**, calculée à l'heure et arrondie à l'inférieur. Chaque planète a **son propre stock**, limité par ses entrepôts (voir [Le stockage](/fr/economy/storage)).
7. **Bonus** : ils s'appliquent à la production brute des trois mines et **s'additionnent**, sans se multiplier entre eux :
   - **Maîtrise du Plasma** : +1 % de métal, +0,66 % de cristal et +0,33 % d'hydrogène par niveau ;
   - talent d'alliance **Extraction coordonnée** : +5 % des trois ressources par niveau ;
   - **bonus de position**, sur les colonies seulement : jusqu'à +40 % de cristal en positions 1 à 3, jusqu'à +35 % de métal en positions 6 à 10 (voir [Planètes](/fr/universe/planets)) ;
   - les traits de dynastie et les talents (voir [Dynastie et talents](/fr/dynasty)).
8. Si l'énergie manque, la production des mines, bonus compris, baisse dans la proportion du déficit. Le revenu de la Base planetaire n'est pas touché.
9. **Taux de fonctionnement** : chaque mine se règle par pas de 10 %, de 0 à 100 %. Sa production et sa consommation d'énergie baissent dans la même proportion.
10. La production s'arrête quand le stock d'une ressource atteint sa capacité, pendant le [mode vacances](/fr/players/vacation-mode), sur une planète abandonnée, et quand un univers privé est gelé ou terminé.

## Exemple chiffré

Une colonie en position 8, avec Excavateur minéral 13, Extracteur cristallin 13, Maîtrise du Plasma 2, Extraction coordonnée 2 (+10 %) et assez d'énergie :
- Métal : 1 346 (Excavateur) + 26 (Plasma : 2 %) + 134 (alliance : 10 %) + 471 (position 8 : 35 %) + 20 (Base) = **1 997 par heure**.
- Cristal : 897 (Extracteur) + 11 (Plasma : 1,32 %) + 89 (alliance) + 10 (Base) = **1 007 par heure**. La position 8 n'a pas de bonus de cristal.
- Chaque bonus est calculé sur la production brute de la mine et arrondi à l'inférieur.

## Données détaillées

### Production des mines par niveau (par heure, vitesse ×1, sans bonus)

L'hydrogène est donné pour un facteur de température de 1 ; multipliez-le par le facteur de votre planète.

| Niveau | Excavateur minéral (métal) | Extracteur cristallin (cristal) | Condensateur d'hydrogène (hydrogène, facteur 1) |
|---|---|---|---|
| 1 | 33 | 22 | 11 |
| 2 | 72 | 48 | 24 |
| 3 | 119 | 79 | 39 |
| 4 | 175 | 117 | 58 |
| 5 | 241 | 161 | 80 |
| 6 | 318 | 212 | 106 |
| 7 | 409 | 272 | 136 |
| 8 | 514 | 342 | 171 |
| 9 | 636 | 424 | 212 |
| 10 | 778 | 518 | 259 |
| 11 | 941 | 627 | 313 |
| 12 | 1 129 | 753 | 376 |
| 13 | 1 346 | 897 | 448 |
| 14 | 1 594 | 1 063 | 531 |
| 15 | 1 879 | 1 253 | 626 |
| 16 | 2 205 | 1 470 | 735 |
| 17 | 2 577 | 1 718 | 859 |
| 18 | 3 002 | 2 001 | 1 000 |
| 19 | 3 486 | 2 324 | 1 162 |
| 20 | 4 036 | 2 690 | 1 345 |
| 21 | 4 662 | 3 108 | 1 554 |
| 22 | 5 372 | 3 581 | 1 790 |
| 23 | 6 178 | 4 118 | 2 059 |
| 24 | 7 091 | 4 727 | 2 363 |
| 25 | 8 126 | 5 417 | 2 708 |
| 26 | 9 296 | 6 197 | 3 098 |
| 27 | 10 619 | 7 079 | 3 539 |
| 28 | 12 113 | 8 075 | 4 037 |
| 29 | 13 800 | 9 200 | 4 600 |
| 30 | 15 704 | 10 469 | 5 234 |

### Facteur de température du Condensateur d'hydrogène

| Température maximale | Facteur |
|---|---|
| -120 °C | 1,92 |
| -100 °C | 1,84 |
| -80 °C | 1,76 |
| -60 °C | 1,68 |
| -40 °C | 1,60 |
| -20 °C | 1,52 |
| 0 °C | 1,44 |
| 20 °C | 1,36 |
| 40 °C | 1,28 |
| 60 °C | 1,20 |
| 80 °C | 1,12 |
| 100 °C | 1,04 |
| 120 °C | 0,96 |
| 140 °C | 0,88 |
| 160 °C | 0,80 |

## Pièges fréquents

- **L'hydrogène part en fumée** : chaque vol en consomme, aller et retour payés au départ pour la plupart des missions.
- **Un stock plein ne produit plus** : dépensez ou agrandissez vos entrepôts.
- **Le stock est local** : les ressources d'une colonie ne servent pas sur la planète mère, il faut les transporter.
- **La planète mère n'a pas de bonus de position** : pensez-y en choisissant l'emplacement de vos colonies.

## Pages liées

- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Formules de l'économie](/fr/economy/formulas)
- [Planètes : taille, température, type](/fr/universe/planets)
