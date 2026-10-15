---
wiki_id: 57
locale: "fr"
path: "players/beginner-protection"
url: "https://wiki.dynastynova.com/fr/players/beginner-protection"
title: "Protection des débutants"
description: "Qui peut attaquer qui : protection nouvel arrivant et paliers de points."
tags: ["players"]
published: true
created: "2026-10-02T13:09:35.168Z"
updated: "2026-10-15T18:54:44.723Z"
---

# Protection des débutants

> **En bref** : deux protections tiennent les joueurs trop inégaux à l'écart l'un de l'autre. La **protection nouvel arrivant** vous rend inattaquable pendant vos 7 premiers jours dans un univers, tant que vous n'attaquez personne. La **protection par points** interdit toute attaque entre deux joueurs dont l'écart de points est trop grand, dans un sens comme dans l'autre.
{.is-info}

> **Paramètre d'univers** : les paliers de points et le délai d'inactivité peuvent être différents selon l'univers.
> Par défaut : **1:3** sous 500 points, **1:5** sous 5 000, **1:10** sous 500 000, inactif après **14 jours** · Redline : mêmes paliers, inactif après **7 jours**
{.is-info}

## Règles

### Protection nouvel arrivant
1. Pendant **7 jours** à compter de votre **première arrivée** dans un univers, personne ne peut vous attaquer ni vous tirer de missiles. Cette durée est la même dans tous les univers.
2. Le temps restant s'affiche en haut de l'écran (« Protection nouvel arrivant »). Vos planètes et votre fiche portent le badge « Nouveau joueur », avec la date de fin.
3. **Lancer une attaque ou une salve de missiles y met fin, définitivement**, quelle que soit la cible (joueur, joueur non humain, planète abandonnée). Un avertissement s'affiche avant de confirmer. Rappeler la flotte ne rend pas la protection.
4. L'espionnage, le transport, le stationnement, le recyclage et la colonisation ne la retirent pas, dans un sens comme dans l'autre : un nouvel arrivant peut être espionné et ravitaillé.
5. Elle vaut **par univers**. Quitter un univers puis y revenir ne la renouvelle pas : la date de première arrivée reste la même.
6. Les joueurs non humains (PvE) n'en ont jamais.

### Protection par points
7. Une attaque est interdite quand le plus fort des deux joueurs a **au moins N fois** les points du plus faible, N dépendant du palier du **plus faible** :
   - moins de 500 points : **1:3** ;
   - de 500 à moins de 5 000 points : **1:5** ;
   - de 5 000 à moins de 500 000 points : **1:10** ;
   - 500 000 points ou plus : **plus aucune protection**, quel que soit l'écart.
8. La règle joue **dans les deux sens** : le petit joueur est protégé du gros, et le petit ne peut pas attaquer le gros non plus.
9. Une borne appartient au palier du dessus : à exactement 500 points, on est en 1:5. Exactement N fois plus de points suffit à bloquer.
10. Les points comptés sont le **total** du classement, arrondi à l'entier inférieur (voir [Classements et points](/fr/players/rankings)).
11. Un joueur à **0 point** ne peut être attaqué par aucun joueur qui en a ; deux joueurs à 0 point peuvent s'affronter.
12. Elle s'applique aux **attaques** et aux **salves de missiles**. L'espionnage, le transport et le recyclage restent libres.
13. Un défenseur **inactif** (voir [Inactivité](/fr/players/inactivity)) perd cette protection : n'importe qui peut l'attaquer, quel que soit l'écart, y compris un joueur beaucoup plus petit que lui. Seule l'inactivité du défenseur compte.

### Les deux ensemble
14. Les deux protections **s'ajoutent** : une attaque doit passer l'une et l'autre, puis la [limite d'attaques](/fr/players/attack-limit). La protection nouvel arrivant ne dépend pas des points ; la protection par points ne dépend pas de l'ancienneté.
15. Dans la [vue galaxie](/fr/universe/galaxy-view), l'attaque, les missiles et la destruction de lune ne sont pas proposés contre un joueur que l'une des deux protections couvre.

## Exemple chiffré

Joueurs actifs, protection nouvel arrivant terminée, paliers par défaut :

| Joueur A | Joueur B | Palier du plus faible | Écart | Attaque possible ? |
|---|---|---|---|---|
| 400 points | 1 000 points | 1:3 (< 500) | 2,5 | oui, dans les deux sens |
| 400 points | 1 200 points | 1:3 (< 500) | 3 | **non, dans aucun sens** |
| 400 points | 1 500 points | 1:3 (< 500) | 3,75 | **non, dans aucun sens** |
| 0 point | 50 points | 1:3 (< 500) |  | **non, dans aucun sens** |
| 0 point | 0 point | 1:3 (< 500) |  | oui, dans les deux sens |
| 500 points | 2 400 points | 1:5 (< 5 000) | 4,8 | oui, dans les deux sens |
| 6 000 points | 50 000 points | 1:10 (< 500 000) | 8,33 | oui, dans les deux sens |
| 6 000 points | 80 000 points | 1:10 (< 500 000) | 13,33 | **non, dans aucun sens** |
| 6 000 points | 80 000 points (inactif) | 1:10 (< 500 000) | 13,33 | A peut attaquer B (inactif), pas l'inverse |
| 600 000 points | 5 000 000 points | aucun (≥ 500 000) | 8,33 | oui, dans les deux sens |

## Pièges fréquents

- **Le plus fort est protégé aussi** : un petit joueur ne peut pas attaquer un joueur bien plus gros que lui, sauf s'il est inactif.
- **Votre première attaque vous coûte le reste de vos 7 jours**, même contre une planète abandonnée.
- **L'inactivité lève la protection par points** : avant une longue absence, pensez au [mode vacances](/fr/players/vacation-mode).
- **Les points comptent tout** : économie, recherche et militaire. Construire beaucoup peut vous faire changer de palier.

## Pages liées

- [Classements et points](/fr/players/rankings)
- [Limite d'attaques](/fr/players/attack-limit)
- [Mode vacances](/fr/players/vacation-mode)
- [Inactivité](/fr/players/inactivity)
- [La vue galaxie](/fr/universe/galaxy-view)
