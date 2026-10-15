---
wiki_id: 38
locale: "fr"
path: "fleet/jump-gate"
url: "https://wiki.dynastynova.com/fr/fleet/jump-gate"
title: "Porte de saut"
description: "Déplacer une flotte instantanément entre deux lunes."
tags: ["fleet", "lune"]
published: true
created: "2026-10-02T13:08:58.343Z"
updated: "2026-10-15T18:54:29.635Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Porte de saut

> **En bref** : la Porte de saut se construit sur une lune. Elle envoie instantanément des vaisseaux vers une autre de vos lunes équipée d'une Porte, sans temps de vol ni hydrogène. Elle ne transporte aucune ressource, et les deux portes doivent ensuite se recharger.
{.is-info}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Porte de saut">

## Règles

1. La Porte de saut se construit **uniquement sur une lune**. Prérequis : **Base lunaire 1** et **Pliage Spatial 7**. Elle n'a pas de niveau maximum ; son coût double à chaque niveau.
2. Un saut relie **deux lunes différentes qui vous appartiennent**, dans le même univers, chacune équipée d'une Porte de saut prête. Impossible de sauter vers la lune d'un autre joueur, même allié.
3. Le saut est **instantané** et ne consomme **aucun hydrogène**. Il n'occupe aucun emplacement de flotte.
4. **Coques seulement** : aucune ressource ne passe.
5. Après un saut, **les deux portes**, départ et arrivée, se rechargent, chacune selon son propre niveau (table plus bas). La recharge ne dépend pas des vitesses de l'univers.
6. Les deux lunes sont vérifiées avant tout mouvement : un saut refusé (porte en recharge, lune sans Porte) ne déplace rien et ne déclenche aucune recharge.
7. Des talents du Navigateur raccourcissent la recharge (jusqu'à 30 %) ou permettent deux sauts avant recharge (voir [Navigateur](/fr/dynasty/classes/navigator)).

## Exemple chiffré

Vous avez une Porte de saut niveau 3 sur la lune A et niveau 1 sur la lune B. Vous faites sauter votre flotte de A vers B.
- La flotte arrive aussitôt sur B, sans dépenser d'hydrogène.
- La porte de A se recharge en **47 minutes** (niveau 3), celle de B en **60 minutes** (niveau 1).
- Un nouveau saut depuis B, ou vers A, ne sera possible qu'une fois la porte concernée rechargée.

Avec une recharge raccourcie de 30 % par les talents, une porte niveau 5 passe de 36 à **25 minutes**.

## Données détaillées

### Recharge selon le niveau

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 et plus |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recharge (minutes) | 60 | 53 | 47 | 41 | 36 | 31 | 27 | 23 | 19 | 17 | 14 | 13 | 11 | 10 |

### Coût

| Niveau | Métal | Cristal | Hydrogène |
|---|---|---|---|
| 1 | 2 000 000 | 4 000 000 | 2 000 000 |
| 2 | 4 000 000 | 8 000 000 | 4 000 000 |
| 3 | 8 000 000 | 16 000 000 | 8 000 000 |
| 4 | 16 000 000 | 32 000 000 | 16 000 000 |
| 5 | 32 000 000 | 64 000 000 | 32 000 000 |

Le coût continue de doubler aux niveaux suivants.

## Pièges fréquents

- **La recharge frappe les deux bouts** : améliorer seulement la porte de départ ne suffit pas à enchaîner les sauts.
- **Pas de ressources** : une flotte chargée doit d'abord décharger sa cargaison.
- **Il faut deux lunes à vous** : une seule Porte ne sert à rien, et celle d'un allié non plus.
- **Au-delà du niveau 14, la recharge ne baisse plus** : elle reste à 10 minutes.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Déplacements](/fr/fleet/movement)
- [Liste des bâtiments](/fr/economy/buildings)
