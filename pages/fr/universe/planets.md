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

> **En bref** : la position d'une planète dans son système fixe sa taille moyenne et sa température. Les planètes proches de l'étoile sont plus petites et plus chaudes, idéales pour l'énergie solaire ; les planètes lointaines sont plus grandes et plus froides, idéales pour l'hydrogène. Le type de planète (désert, jungle, glace…) ne change que l'apparence. Les colonies ont en plus un bonus de production de métal ou de cristal selon leur position ; la planète mère n'en a pas.
{.is-info}

> **Paramètre d'univers** : le nombre de positions par système (de 9 à 20) dépend de l'univers. Dans un univers qui n'en a pas 15, chaque position est lue sur une échelle de 15 (règles 2 et 9).
> Par défaut : **aucun, chaque univers a le sien** · Redline : **15 positions**
{.is-info}

![Un système en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*Un système en affichage orbites : chaque planète a l'aspect de son type et de son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

### Taille
1. Le nombre de cases d'une planète vaut la **taille moyenne de sa position, plus ou moins 15**. Il est fixé une fois pour toutes à la création de l'univers, case par case.
2. Dans un système qui n'a pas 15 positions, la position est d'abord **ramenée sur 15 et arrondie** (liste dans les données détaillées) : la taille, les types et la température sont ceux de cette position ramenée.
3. La **planète mère** a toujours **163 cases**, quelle que soit sa position.
4. Chaque niveau de bâtiment occupe **une case**, sauf la Station de réparation. Le [Modulateur planétaire](/fr/economy/terraformer-and-logistics) ajoute des cases, et certains talents de dynastie aussi.

### Température
5. Chaque position a une température **minimale** et **maximale**, écartées de 40 °C : $T_{max} = 180 - 15 \times p$ et $T_{min} = T_{max} - 40$, avec $p$ la position ramenée sur 15.
6. La température **actuelle** suit le mois du calendrier : à sa minimale le 1er, elle monte chaque jour jusqu'à sa maximale le jour du milieu du mois (le 15, le 14 en février), puis redescend jusqu'à sa minimale le dernier jour. Elle est arrondie au degré.
7. La température agit sur trois productions (détail dans [L'énergie](/fr/economy/energy)) :
   - **Condensateur d'hydrogène** : production × (1,44 − 0,004 × $T_{max}$), jamais en dessous de 0. Plus il fait froid, plus il produit.
   - **Collecteur solaire** : $T_{max}$ / 4 + 20 énergie chacun, arrondi à l'inférieur.
   - **Capteurs photovoltaïques** : production × (1 + température actuelle / 100), quand la température actuelle est positive.

### Type et apparence
8. Chaque planète a un **type** (désert, aride, normal, jungle, eau, glace, gaz), tiré parmi ceux de sa position, et un **biome**, une variante visuelle. Ils ne changent que le nom généré et les images, pas la production. Un **skin de planète**, obtenu en boutique ou dans le lot mensuel Premium, remplace l'apparence de votre planète.

### Bonus de position
9. **Bonus de position** : l'Extracteur cristallin produit davantage près de l'étoile, l'Excavateur minéral au milieu du système (tableau ci-dessous). Le bonus a sa propre ligne dans le détail de production. Il ne touche pas l'hydrogène, qui dépend de la température.
10. La **planète mère n'a pas de bonus de position** : son emplacement est tiré au hasard, et le bonus donnerait à chacun une avance différente par chance. Seul un talent de dynastie peut lui en accorder une part.
11. Dans un système qui n'a pas 15 positions, la position est lue sur l'échelle de 15 **sans arrondi**, et le bonus est **interpolé** entre les deux positions qui l'encadrent. Le pic (+40 % de cristal, +35 % de métal) reste le même, aucune position n'est doublée ni sautée.
12. Le bonus s'applique à la production de la mine, arrondi à l'inférieur.

## Exemple chiffré

**Hydrogène : position 3 contre position 12**
- Position 3 (température max 135 °C) : facteur 1,44 − 0,004 × 135 = **0,90**.
- Position 12 (température max 0 °C) : facteur **1,44**.
- À niveau égal, le Condensateur de la position 12 produit 1,44 / 0,90 = **60 % de plus**.

**Bonus de position d'une colonie**
- Colonie en position 8 d'un système de 15, Excavateur minéral produisant 1 000 métal par heure : bonus 35 %, soit **+350 métal par heure**.
- Même mine sur une colonie en position 4 d'un système de 9 : la position est lue à 6,25 sur 15, entre 6 (+17 %) et 7 (+23 %), soit un bonus de **18,5 %** : **+185 métal par heure**.
- La même mine sur votre planète mère : **aucun bonus**.

**La température du mois en position 8** (20 à 60 °C, mois de 31 jours) et le bonus des Capteurs photovoltaïques :

| Jour | Température actuelle (°C) | Bonus des Capteurs |
|---|---|---|
| 1 | 20 | 20 % |
| 5 | 31 | 31 % |
| 10 | 46 | 46 % |
| 15 | 60 | 60 % |
| 16 | 58 | 58 % |
| 20 | 48 | 48 % |
| 25 | 35 | 35 % |
| 31 | 20 | 20 % |

## Données détaillées

### Selon la position (sur 15)

| Position | Taille moyenne | Taille possible | Types possibles | Temp. min / max (°C) | Facteur du Condensateur | Énergie par Collecteur |
|---|---|---|---|---|---|---|
| 1 | 145 | 130 à 160 | désert, aride | 125 / 165 | 0,78 | 61 |
| 2 | 150 | 135 à 165 | désert, aride | 110 / 150 | 0,84 | 57 |
| 3 | 155 | 140 à 170 | désert, aride, normal | 95 / 135 | 0,90 | 53 |
| 4 | 160 | 145 à 175 | aride, normal | 80 / 120 | 0,96 | 50 |
| 5 | 163 | 148 à 178 | normal, eau | 65 / 105 | 1,02 | 46 |
| 6 | 185 | 170 à 200 | normal, eau, jungle | 50 / 90 | 1,08 | 42 |
| 7 | 190 | 175 à 205 | normal, eau, jungle | 35 / 75 | 1,14 | 38 |
| 8 | 195 | 180 à 210 | eau, jungle | 20 / 60 | 1,20 | 35 |
| 9 | 200 | 185 à 215 | eau, jungle, normal | 5 / 45 | 1,26 | 31 |
| 10 | 205 | 190 à 220 | jungle, normal | −10 / 30 | 1,32 | 27 |
| 11 | 225 | 210 à 240 | glace, normal | −25 / 15 | 1,38 | 23 |
| 12 | 230 | 215 à 245 | glace, gaz | −40 / 0 | 1,44 | 20 |
| 13 | 235 | 220 à 250 | glace, gaz | −55 / −15 | 1,50 | 16 |
| 14 | 242 | 227 à 257 | glace, gaz | −70 / −30 | 1,56 | 12 |
| 15 | 245 | 230 à 260 | glace, gaz | −85 / −45 | 1,62 | 8 |

### Positions ramenées sur 15 (taille, types, température)

Position ramenée de chaque position du système, de la 1re à la dernière :

- 9 positions : 1, 3, 5, 6, 8, 10, 12, 13, 15
- 10 positions : 1, 3, 4, 6, 7, 9, 10, 12, 13, 15
- 11 positions : 1, 2, 4, 5, 7, 8, 9, 11, 12, 14, 15
- 12 positions : 1, 2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15
- 13 positions : 1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15
- 14 positions : 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15
- 15 positions : 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- 16 positions : 1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 14, 15
- 17 positions : 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13, 14, 15
- 18 positions : 1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11, 12, 13, 13, 14, 15
- 19 positions : 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10, 11, 12, 13, 13, 14, 15
- 20 positions : 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10, 11, 11, 12, 13, 14, 14, 15

### Bonus de position (colonies uniquement)

Système de 15 positions (Redline) ; les positions absentes n'ont pas de bonus :

| Position | Lue sur 15 | Métal | Cristal |
|---|---|---|---|
| 1 | 1 |  | 40 % |
| 2 | 2 |  | 30 % |
| 3 | 3 |  | 20 % |
| 6 | 6 | 17 % |  |
| 7 | 7 | 23 % |  |
| 8 | 8 | 35 % |  |
| 9 | 9 | 23 % |  |
| 10 | 10 | 17 % |  |

Système de 9 positions :

| Position | Lue sur 15 | Métal | Cristal |
|---|---|---|---|
| 1 | 1 |  | 40 % |
| 2 | 2,75 |  | 22,5 % |
| 4 | 6,25 | 18,5 % |  |
| 5 | 8 | 35 % |  |
| 6 | 9,75 | 18,5 % |  |

Système de 20 positions :

| Position | Lue sur 15 | Métal | Cristal |
|---|---|---|---|
| 1 | 1 |  | 40 % |
| 2 | 1,74 |  | 32,63 % |
| 3 | 2,47 |  | 25,26 % |
| 4 | 3,21 |  | 15,79 % |
| 5 | 3,95 |  | 1,05 % |
| 7 | 5,42 | 7,16 % |  |
| 8 | 6,16 | 17,95 % |  |
| 9 | 6,89 | 22,37 % |  |
| 10 | 7,63 | 30,58 % |  |
| 11 | 8,37 | 30,58 % |  |
| 12 | 9,11 | 22,37 % |  |
| 13 | 9,84 | 17,95 % |  |
| 14 | 10,58 | 7,16 % |  |

La position lue sur 15 vaut $1 + (p - 1) \times 14 / (n - 1)$, avec $p$ la position et $n$ le nombre de positions du système.

## Pièges fréquents

- **La planète mère ne suit pas la table** : elle a toujours 163 cases et n'a pas de bonus de position.
- **Pour une colonie, la position compte double** : cristal près de l'étoile, métal au milieu du système (+35 % en position 8 sur 15).
- **Taille et bonus ne se lisent pas pareil** dans un univers qui n'a pas 15 positions : la taille et la température suivent la position arrondie, le bonus la position exacte.
- **Le bonus solaire varie dans le mois** : une planète froide n'en profite presque jamais.
- **Le type ne compte pas** : une planète « glace » et une planète « gaz » à la même position produisent pareil.

## Pages liées

- [Coloniser](/fr/universe/colonization)
- [Liste des bâtiments](/fr/economy/buildings)
- [L'énergie](/fr/economy/energy)
- [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)
- [Coordonnées](/fr/universe/coordinates)
