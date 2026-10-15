---
wiki_id: 16
locale: "fr"
path: "universe/moons"
url: "https://wiki.dynastynova.com/fr/universe/moons"
title: "Les lunes"
description: "Formation des lunes, Base lunaire et cases."
tags: ["universe"]
published: false
created: "2026-10-02T13:08:16.183Z"
updated: "2026-10-02T14:14:44.988Z"
---

# Les lunes

> **En bref** : une lune peut naître des débris d'un combat livré au-dessus d'une planète. Elle revient toujours au propriétaire de la planète, quel que soit le vainqueur. Elle commence avec une seule case : la Base lunaire en ouvre d'autres, dans la limite fixée par son diamètre. Une lune accueille la Phalange de capteur et la Porte de saut, et ne peut pas être scannée par une phalange.
{.is-info}

> **Paramètre d'univers** : la chance maximale de former une lune et la quantité de débris qui l'atteint peuvent être différentes selon l'univers.
> Par défaut : **20 % au plus, pour 2 000 000 de débris** · Redline : **20 % au plus, pour 2 000 000 de débris**
{.is-info}

## Règles

### Formation
1. À la fin d'un combat au-dessus d'une planète, une lune peut se former. La chance dépend **des débris de ce combat** (métal et cristal) : le champ de ruines déjà en orbite, laissé par des combats précédents, ne compte pas.
2. **Chance** = débris du combat × chance maximale / débris pour la chance maximale, plafonnée à la chance maximale (formule ci-dessous). En dessous d'un point de chance (100 000 débris par défaut), aucune lune ne peut se former.
3. La lune revient **au propriétaire de la planète**, que le combat soit gagné ou perdu. Un attaquant ne gagne jamais de lune en orbite d'une planète qui n'est pas la sienne.
4. Former une lune ne consomme pas les débris : les recycleurs récupèrent tout le champ de ruines.
5. Une position porte **au plus une lune**. Tant que la planète a sa lune, aucun combat n'en forme une autre.
6. Plus la chance était élevée, plus la lune est **grande** : son diamètre fixe le nombre maximal de cases qu'elle offrira (tableau ci-dessous). La notification du combat donne son diamètre.
7. Dans un univers où les **impacts géants** sont activés (événements cosmiques, fermés par défaut), une lune peut aussi naître d'un impact.

### Développement
8. Une lune naît **vide** : ni ressources, ni bâtiments, **une seule case**, et le nom de sa planète (elle peut être renommée).
9. La **Base lunaire** se construit en premier : aucun autre bâtiment ne peut être lancé sur la lune avant elle. Elle ne se démolit pas.
10. Chaque niveau de Base lunaire **ouvre 3 cases et en occupe une**, soit 2 cases nettes par niveau.
11. Les cases d'une lune ne dépassent jamais son **plafond** : partie entière((diamètre / 1 000)²). Au-delà, monter la Base lunaire n'ouvre plus rien. Certains talents de dynastie ajoutent des cases par niveau ou lèvent ce plafond.
12. Bâtiments possibles sur une lune : Base lunaire, Phalange de capteur, Porte de saut, Fabrique d'automates, Dock orbital (tableau ci-dessous).
13. Une lune **ne produit rien** et stocke 10 000 de chaque ressource (voir [Le stockage](/fr/economy/storage)).

### Vivre avec une lune
14. Le vol entre une planète et sa lune a une distance de **5** : un trajet très court, mais un vrai vol.
15. Une lune peut être espionnée, attaquée, détruite par des Colossus stellaires (voir [Destruction de lune](/fr/combat/moon-destruction)), et recevoir des transports. Elle ne se colonise pas, et elle n'occupe pas de place de colonie.
16. Une **Phalange de capteur** ne peut jamais scanner une lune : une flotte qui y stationne reste invisible.
17. Abandonner une planète abandonne aussi sa lune et tout ce qu'elle porte ; recoloniser cette planète la rend avec sa lune.

## Formules

$$ C = \min\left(D \times \frac{C_{max}}{D_{max}},\ C_{max}\right) \quad \text{si } D \geq \frac{D_{max}}{C_{max}},\ \text{sinon } 0 $$

- $C$ : chance de former une lune, en % ;
- $D$ : débris de métal et de cristal laissés par ce combat ;
- $C_{max}$ : chance maximale de l'univers (20 % par défaut) ;
- $D_{max}$ : débris qui donnent la chance maximale (2 000 000 par défaut).

$$ K = \left\lfloor \left( \frac{d}{1\,000} \right)^2 \right\rfloor $$

- $K$ : plafond de cases de la lune ;
- $d$ : son diamètre, en kilomètres.

## Exemple chiffré

Un combat laisse **1 000 000** de débris au-dessus de votre planète, dans un univers réglé par défaut :
- Chance de lune : 1 000 000 × 20 / 2 000 000 = **10 %**.
- Si la lune se forme, son diamètre est compris entre **6 324 et 7 071 km**, soit un plafond de **39 à 49 cases**.
- Avec un plafond de 39 cases, la Base lunaire atteint ce plafond au niveau **13** (1 + 3 × 13 = 40 cases ouvertes, ramenées à 39).
- Le champ de ruines reste entier pour vos recycleurs.

## Données détaillées

### Chance selon les débris du combat (réglages par défaut)

| Débris du combat | Chance de lune |
|---|---|
| 50 000 | 0 % |
| 100 000 | 1 % |
| 500 000 | 5 % |
| 1 000 000 | 10 % |
| 2 000 000 | 20 % |
| 5 000 000 | 20 % |

### Taille de la lune selon la chance (réglages par défaut)

| Chance du combat | Débris correspondants | Diamètre (km) | Plafond de cases |
|---|---|---|---|
| 1 % | 100 000 | 3 605 à 4 795 | 12 à 22 |
| 2 % | 200 000 | 4 000 à 5 099 | 16 à 25 |
| 5 % | 500 000 | 5 000 à 5 916 | 25 à 34 |
| 10 % | 1 000 000 | 6 324 à 7 071 | 39 à 49 |
| 15 % | 1 500 000 | 7 416 à 8 062 | 54 à 64 |
| 20 % | 2 000 000 | 8 366 à 8 944 | 69 à 79 |

### Base lunaire niveau par niveau

Coût du niveau N : coût du niveau 1 × 2^(N − 1). Les cases ouvertes sont plafonnées par le diamètre de la lune.

| Niveau | Métal | Cristal | Hydrogène | Cases ouvertes | Cases libres (Base lunaire seule) |
|---|---|---|---|---|---|
| 1 | 20 000 | 40 000 | 20 000 | 4 | 3 |
| 2 | 40 000 | 80 000 | 40 000 | 7 | 5 |
| 3 | 80 000 | 160 000 | 80 000 | 10 | 7 |
| 4 | 160 000 | 320 000 | 160 000 | 13 | 9 |
| 5 | 320 000 | 640 000 | 320 000 | 16 | 11 |
| 6 | 640 000 | 1 280 000 | 640 000 | 19 | 13 |
| 7 | 1 280 000 | 2 560 000 | 1 280 000 | 22 | 15 |
| 8 | 2 560 000 | 5 120 000 | 2 560 000 | 25 | 17 |
| 9 | 5 120 000 | 10 240 000 | 5 120 000 | 28 | 19 |
| 10 | 10 240 000 | 20 480 000 | 10 240 000 | 31 | 21 |
| 11 | 20 480 000 | 40 960 000 | 20 480 000 | 34 | 23 |
| 12 | 40 960 000 | 81 920 000 | 40 960 000 | 37 | 25 |
| 13 | 81 920 000 | 163 840 000 | 81 920 000 | 40 | 27 |
| 14 | 163 840 000 | 327 680 000 | 163 840 000 | 43 | 29 |
| 15 | 327 680 000 | 655 360 000 | 327 680 000 | 46 | 31 |

### Bâtiments d'une lune

| Bâtiment | Coût du niveau 1 (métal / cristal / hydrogène) | Facteur par niveau | Prérequis | Niveau max |
|---|---|---|---|---|
| Base lunaire | 20 000 / 40 000 / 20 000 | ×2 | aucun | aucun (le diamètre plafonne les cases) |
| Phalange de capteur | 20 000 / 40 000 / 20 000 | ×2 | Base lunaire 1 | aucun |
| Porte de saut | 2 000 000 / 4 000 000 / 2 000 000 | ×2 | Base lunaire 1, Pliage Spatial 7 | aucun |
| Fabrique d'automates | 400 / 120 / 200 | ×2 | Base lunaire 1 | 10 |
| Dock orbital | 400 / 200 / 100 | ×2 | Base lunaire 1, Fabrique d'automates 2 | 12 |

## Pièges fréquents

- **Un gros champ de ruines déjà en orbite ne sert à rien** : seuls les débris du combat qui vient d'avoir lieu comptent.
- **Les défenses ne laissent pas de débris** dans un univers réglé par défaut : seuls les vaisseaux détruits nourrissent la chance de lune.
- **Une petite lune reste petite** : son plafond est fixé à sa naissance, et la Base lunaire ne le dépasse pas.
- **Une lune n'est pas un abri contre tout** : invisible à la phalange, elle peut quand même être attaquée ou détruite.

## Pages liées

- [Champs de débris](/fr/combat/debris)
- [Destruction de lune](/fr/combat/moon-destruction)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Porte de saut](/fr/fleet/jump-gate)
- [Liste des bâtiments](/fr/economy/buildings)
