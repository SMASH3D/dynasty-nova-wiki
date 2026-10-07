---
wiki_id: 13
locale: "fr"
path: "universe/planets"
url: "https://wiki.dynastynova.com/fr/universe/planets"
title: "Planètes : taille, température, type"
description: "Cases, température et effet de la position."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:10.469Z"
updated: "2026-10-06T10:31:13.668Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Planètes : taille, température, type

> **En bref** : la position d'une planète dans son système fixe sa taille moyenne et sa température. Les planètes proches du soleil sont plus petites et plus chaudes, idéales pour l'énergie solaire ; les planètes lointaines sont plus grandes et plus froides, idéales pour l'hydrogène. Le type de planète (désert, jungle, glace…) ne change que l'apparence. Les colonies ont en plus un bonus de production selon leur position.
{.is-info}

> **Paramètre d'univers** : le nombre de positions par système (de 9 à 20) dépend de l'univers. Dans un univers qui n'en a pas 15, la position est d'abord ramenée sur une échelle de 15 : les profils ci-dessous restent valables, du plus proche au plus lointain du soleil.
> Redline : **15 positions**
{.is-info}

![Un système en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*Un système en affichage orbites : chaque planète a l'aspect de son type et de son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

1. **Taille** : le nombre total de cases d'une planète vaut la taille moyenne de sa position, plus ou moins 15, tirée au hasard à sa création puis figée.
2. La **planète mère** démarre toujours à **163 cases**, quelle que soit sa position.
3. Chaque niveau de bâtiment occupe **une case**. Le [Modulateur planétaire](/fr/economy/terraformer-and-logistics) ajoute des cases.
4. **Température** : chaque position a une température minimale et maximale (table ci-dessous). La température **actuelle** suit le mois du calendrier : à sa minimale le 1er, elle monte chaque jour jusqu'à sa maximale au milieu du mois (le 15, le 14 en février), puis redescend jusqu'à sa minimale le dernier jour du mois.
5. La température agit sur trois productions :
   - **Condensateur d'hydrogène** : production × (1,44 − 0,004 × température maximale). Plus il fait froid, plus il produit.
   - **Collecteur solaire** : production = température maximale / 4, plus une énergie de base.
   - **Capteurs photovoltaïques** : production × (1 + température actuelle / 100), quand la température actuelle est positive.
6. **Type, biome et apparence** : chaque planète a un type (désert, aride, normal, jungle, eau, glace, gaz) et un **biome**, une variante visuelle tirée à sa création. Ensemble, ils donnent à chaque planète son aspect propre, dans la vue galaxie comme en 3D. Ils ne changent que le nom généré et les images, pas la production. Un **skin de planète**, obtenu en boutique ou dans le lot mensuel Premium, remplace l'apparence de votre planète.
7. Au-delà de la dernière position s'étend l'**espace lointain** : aucune planète, seulement des champs de ruines et les flottes en expédition.
8. **Bonus de position** (colonies uniquement) : l'Extracteur cristallin des positions 1 à 3 et l'Excavateur minéral des positions 6 à 10 produisent davantage (table ci-dessous). La planète mère n'en bénéficie jamais, pour ne pas créer d'inégalités au départ. Le bonus a sa propre ligne dans le détail de production.

## Exemple chiffré

**Hydrogène : position 3 contre position 12**
- Position 3 (température max 135 °C) : facteur 1,44 − 0,004 × 135 = **0,90**.
- Position 12 (température max 0 °C) : facteur 1,44 − 0,004 × 0 = **1,44**.
- À niveau égal, le Condensateur de la position 12 produit 1,44 / 0,90 = **60 % de plus**.

**Énergie solaire sur une planète en position 8** (20 à 60 °C)
- Un jour où la température actuelle est de 23 °C, les Capteurs photovoltaïques produisent **23 % de plus** (× 1,23).
- Chaque Collecteur solaire y produit 35 énergie (valeur relevée en jeu).

## Données détaillées

### Selon la position (univers à 15 positions)

| Position | Taille moyenne (cases) | Types possibles | Température min / max (°C) |
|---|---|---|---|
| 1 | 145 | désert, aride | 125 / 165 |
| 2 | 150 | désert, aride | 110 / 150 |
| 3 | 155 | désert, aride, normal | 95 / 135 |
| 4 | 160 | aride, normal | 80 / 120 |
| 5 | 163 | normal, eau | 65 / 105 |
| 6 | 185 | normal, eau, jungle | 50 / 90 |
| 7 | 190 | normal, eau, jungle | 35 / 75 |
| 8 | 195 | eau, jungle | 20 / 60 |
| 9 | 200 | eau, jungle, normal | 5 / 45 |
| 10 | 205 | jungle, normal | −10 / 30 |
| 11 | 225 | glace, normal | −25 / 15 |
| 12 | 230 | glace, gaz | −40 / 0 |
| 13 | 235 | glace, gaz | −55 / −15 |
| 14 | 242 | glace, gaz | −70 / −30 |
| 15 | 245 | glace, gaz | −85 / −45 |

La taille réelle d'une colonie varie de 15 cases autour de la moyenne : une colonie en position 15 compte entre 230 et 260 cases.

### Facteur de production d'hydrogène

| Position | 1 | 3 | 5 | 8 | 10 | 12 | 15 |
|---|---|---|---|---|---|---|---|
| Température max (°C) | 165 | 135 | 105 | 60 | 30 | 0 | −45 |
| Facteur du Condensateur | 0,78 | 0,90 | 1,02 | 1,20 | 1,32 | 1,44 | 1,62 |

### Bonus de position (colonies uniquement)

| Position | 1 | 2 | 3 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|
| Extracteur cristallin (cristal) | +40 % | +30 % | +20 % | | | | | |
| Excavateur minéral (métal) | | | | +17 % | +23 % | +35 % | +23 % | +17 % |

Les positions 4, 5 et 11 à 15 n'ont pas de bonus. La planète mère n'en a jamais, quelle que soit sa position.

## Pièges fréquents

- **La planète mère ne suit pas la table** : elle a toujours 163 cases, et n'a pas de bonus de position.
- **Pour une colonie, la position compte double** : cristal en positions 1 à 3, métal en positions 6 à 10 (+35 % en position 8).
- **Le bonus solaire varie dans le mois** : il dépend de la température actuelle, qui monte et descend. Une planète froide n'en profite presque jamais.
- **Le type ne compte pas** : une planète « glace » et une planète « gaz » à la même position produisent pareil.
- **Les cases sont la vraie limite à long terme** : une petite planète proche du soleil se remplit vite.

## Pages liées

- [Coloniser](/fr/universe/colonization)
- [Liste des bâtiments](/fr/economy/buildings)
- [L'énergie](/fr/economy/energy)
- [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)
- [Coordonnées](/fr/universe/coordinates)
