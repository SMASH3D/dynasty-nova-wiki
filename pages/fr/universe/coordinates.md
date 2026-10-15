---
wiki_id: 11
locale: "fr"
path: "universe/coordinates"
url: "https://wiki.dynastynova.com/fr/universe/coordinates"
title: "Coordonnées"
description: "Galaxie, système, position et distances."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:06.755Z"
updated: "2026-10-15T18:55:04.314Z"
---

# Coordonnées

> **En bref** : chaque planète a une adresse à trois nombres, [galaxie:système:position], par exemple [2:83:6]. Le nombre de galaxies, de systèmes par galaxie et de positions par système dépend de l'univers. La carte **boucle** : la dernière galaxie est voisine de la première, et le dernier système d'une galaxie voisin du premier. La distance entre deux coordonnées fixe la durée et le coût en hydrogène d'un vol.
{.is-info}

> **Paramètre d'univers** : le nombre de galaxies, de systèmes par galaxie et de positions par système (de 9 à 20) est fixé à la création de l'univers.
> Par défaut : **aucun, chaque univers a le sien** · Redline : **9 galaxies, 99 systèmes, 15 positions**
{.is-info}

## Règles

1. Une coordonnée s'écrit **[galaxie:système:position]**.
2. Chaque galaxie compte le même nombre de **systèmes** : 99 sur Redline, numérotés de 1 à 99.
3. Chaque système compte le même nombre de **positions** : 15 sur Redline. Chaque position accueille au plus une planète, et éventuellement sa lune.
4. Après la dernière position, chaque système a deux cases de plus, sans planète :
   - l'**espace lointain** (position 16 sur Redline), pour les expéditions et le recyclage ;
   - la **Station stellaire** (position 17 sur Redline), où se trouvent la Banque stellaire et la trésorerie d'alliance.
5. **La carte boucle sur les galaxies et sur les systèmes** : de la galaxie 9 à la galaxie 1, l'écart est de 1, comme de la galaxie 1 à la galaxie 2. De même, le système 99 est voisin du système 1 dans la même galaxie. Le jeu prend toujours le plus court des deux sens.
6. Les **positions ne bouclent pas** : de la position 1 à la position 15, l'écart est de 14.
7. La **distance** entre deux points ne dépend que de l'écart le plus important (tableau ci-dessous) : un écart de galaxie l'emporte sur tout le reste, puis un écart de système, puis un écart de position.

## Formules

Avec $\Delta G$, $\Delta S$ et $\Delta P$ les écarts de galaxie, de système et de position :

$$
D = \begin{cases}
20\,000 \times \Delta G & \text{si } \Delta G > 0 \\
2\,700 + 95 \times \Delta S & \text{sinon, si } \Delta S > 0 \\
1\,000 + 5 \times \Delta P & \text{sinon, si } \Delta P > 0 \\
5 & \text{entre une planète et sa lune}
\end{cases}
$$

- $\Delta G = \min(|G_1 - G_2|,\ n_G - |G_1 - G_2|)$, avec $n_G$ le nombre de galaxies de l'univers ;
- $\Delta S = \min(|S_1 - S_2|,\ n_S - |S_1 - S_2|)$, avec $n_S$ le nombre de systèmes par galaxie ;
- $\Delta P = |P_1 - P_2|$ ;
- $D$ : distance du vol, qui entre dans sa durée et sa consommation (voir [Déplacements](/fr/fleet/movement)).

## Exemples chiffrés

Sur Redline (9 galaxies, 99 systèmes) :

| Trajet | Écart retenu | Distance |
|---|---|---|
| [3:40:8] vers [5:40:8] | 2 galaxies | 20 000 × 2 = **40 000** |
| [1:40:8] vers [9:40:8] | 1 galaxie (la carte boucle) | 20 000 × 1 = **20 000** |
| [2:45:8] vers [2:50:8] | 5 systèmes | 2 700 + 95 × 5 = **3 175** |
| [2:97:8] vers [2:3:8] | 5 systèmes (la galaxie boucle) | 2 700 + 95 × 5 = **3 175** |
| [2:45:3] vers [2:45:6] | 3 positions | 1 000 + 5 × 3 = **1 015** |
| [2:45:3] vers sa lune | même case | **5** |

## Pièges fréquents

- **Changer de galaxie coûte cher** : une seule galaxie d'écart (20 000) vaut plus que le trajet le plus long à l'intérieur d'une galaxie de Redline, 49 systèmes d'écart au plus grâce à la boucle (2 700 + 95 × 49 = 7 355).
- **Pensez à la boucle** : une cible dans la galaxie 9 est à une seule galaxie de vous si vous êtes dans la galaxie 1.
- **Planète et lune ne sont pas au même endroit** : un trajet de 5 reste un vrai vol, très court.

## Pages liées

- [La vue galaxie](/fr/universe/galaxy-view)
- [Déplacements](/fr/fleet/movement)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Expéditions](/fr/fleet/expeditions)
