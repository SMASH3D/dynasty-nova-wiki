---
wiki_id: 30
locale: "fr"
path: "research/stellar-collaboration"
url: "https://wiki.dynastynova.com/fr/research/stellar-collaboration"
title: "Collaboration Stellaire"
description: "Mettre ses Centres d'innovation en réseau."
tags: ["research"]
published: true
created: "2026-10-02T13:08:42.942Z"
updated: "2026-10-15T18:54:54.606Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Collaboration Stellaire

> **En bref** : la Collaboration Stellaire met en réseau les Centres d'innovation de vos autres planètes pour raccourcir vos recherches. Au niveau N, elle ajoute au Centre qui étudie les N meilleurs Centres de vos autres planètes, à condition qu'ils soient au moins aussi avancés que lui. Elle ne change jamais le coût.
{.is-info}

<img src="/images/illustrations/research/collaboration-stellaire.jpg" width="180" alt="Collaboration Stellaire">

## Règles

1. Prérequis : **Centre d'innovation 10, Calcul Quantique 8, Pliage Spatial 8**. Niveau maximum : 10.
2. Au **niveau N**, une recherche met en réseau jusqu'à **N Centres d'innovation** de vos **autres** planètes du même univers.
3. Un Centre n'est retenu que si son niveau est **au moins égal** à celui de la planète qui lance la recherche. Parmi ceux-là, les **plus avancés** passent en premier.
4. **Niveau effectif** = Centre de la planète qui lance la recherche + somme des Centres retenus. C'est lui qui entre dans la formule de durée (voir [Liste des technologies](/fr/research/technologies)).
5. Le réseau est fixé **au lancement** de l'étude, ou quand une étude en file prend son tour. Améliorer un Centre ensuite ne change pas une étude déjà lancée. Un Centre en travaux compte à son niveau actuel.
6. La Collaboration Stellaire **ne change pas le coût** des recherches, et les Centres mis en réseau restent libres : ils ne sont ni bloqués ni consommés.
7. Une seule étude avance à la fois dans l'empire : le réseau accélère cette étude, il n'en lance pas d'autres.

### Talents du Théoricien

Certains talents de la classe Théoricien changent ces règles (valeurs sur [Le Théoricien](/fr/dynasty/classes/theorist)) :

- **Liaison montante** : accepte des Centres jusqu'à quelques niveaux sous celui qui étudie.
- **Antenne lointaine** : accepte, elle aussi, des Centres plus bas que celui qui étudie.
- **Un labo de plus** : met en commun un Centre de plus que la Collaboration Stellaire ne l'autorise.
- **Labos de campagne** : chaque Centre de vos planètes mis en réseau compte des niveaux de plus.
- **Labo-mère** : le Centre qui étudie compte des niveaux de plus.
- **Échange universitaire** : ajoute le meilleur Centre d'un membre de votre alliance, s'il entre dans la tolérance.
- **Réseau vivant** : recalcule une étude en cours quand un Centre du réseau monte de niveau, jamais plus lentement.

## Exemple chiffré

Vous recherchez **Pliage Spatial niveau 8** (512 000 cristal, 256 000 hydrogène). Vos planètes ont des Centres d'innovation aux niveaux **10, 9, 8 et 6**. Collaboration Stellaire niveau **2**.

Lancée depuis la planète au Centre **8** :
- Centres retenus : les 2 meilleurs parmi ceux de niveau 8 ou plus, soit **10 et 9**. Le Centre de niveau 6 est trop faible.
- Niveau effectif : 8 + 10 + 9 = **27**.
- Durée : 512 000 / (1 000 × (1 + 27)) h, soit **18 h 17 min 9 s**, au lieu de 2 j 8 h 53 min 20 s avec le seul Centre local.

Lancée depuis la planète au Centre **10** :
- Aucun autre Centre n'atteint le niveau 10 : le réseau n'apporte rien, niveau effectif **10**.
- Durée : **1 j 22 h 32 min 44 s**. Lancer depuis le Centre 8 est donc plus rapide.

## Données détaillées

### Gain de vitesse

Niveau effectif et vitesse par rapport au Centre local seul, quand tous les Centres ont le même niveau et que la Collaboration Stellaire est au moins égale au nombre de Centres en réseau.

| Centres en réseau (tous au même niveau) | Centres au niveau 8 | Centres au niveau 10 | Centres au niveau 12 |
|---|---|---|---|
| 0 | 8 (×1) | 10 (×1) | 12 (×1) |
| 1 | 16 (×1,89) | 20 (×1,91) | 24 (×1,92) |
| 2 | 24 (×2,78) | 30 (×2,82) | 36 (×2,85) |
| 3 | 32 (×3,67) | 40 (×3,73) | 48 (×3,77) |
| 4 | 40 (×4,56) | 50 (×4,64) | 60 (×4,69) |
| 5 | 48 (×5,44) | 60 (×5,55) | 72 (×5,62) |
| 6 | 56 (×6,33) | 70 (×6,45) | 84 (×6,54) |
| 7 | 64 (×7,22) | 80 (×7,36) | 96 (×7,46) |
| 8 | 72 (×8,11) | 90 (×8,27) | 108 (×8,38) |
| 9 | 80 (×9) | 100 (×9,18) | 120 (×9,31) |
| 10 | 88 (×9,89) | 110 (×10,09) | 132 (×10,23) |

### Coût de la Collaboration Stellaire

| Niveau | Métal | Cristal | Hydrogène | Durée avec un Centre 10 seul | Points |
|---|---|---|---|---|---|
| 1 | 240 000 | 400 000 | 160 000 | 2 j 10 h 10 min 55 s | 800 |
| 2 | 480 000 | 800 000 | 320 000 | 4 j 20 h 21 min 49 s | 1 600 |
| 3 | 960 000 | 1 600 000 | 640 000 | 9 j 16 h 43 min 38 s | 3 200 |
| 4 | 1 920 000 | 3 200 000 | 1 280 000 | 19 j 9 h 27 min 16 s | 6 400 |
| 5 | 3 840 000 | 6 400 000 | 2 560 000 | 38 j 18 h 54 min 33 s | 12 800 |
| 6 | 7 680 000 | 12 800 000 | 5 120 000 | 77 j 13 h 49 min 5 s | 25 600 |
| 7 | 15 360 000 | 25 600 000 | 10 240 000 | 155 j 3 h 38 min 11 s | 51 200 |
| 8 | 30 720 000 | 51 200 000 | 20 480 000 | 310 j 7 h 16 min 22 s | 102 400 |
| 9 | 61 440 000 | 102 400 000 | 40 960 000 | 620 j 14 h 32 min 44 s | 204 800 |
| 10 | 122 880 000 | 204 800 000 | 81 920 000 | 1 241 j 5 h 5 min 27 s | 409 600 |

## Pièges fréquents

- **Lancez depuis le bon Centre** : un Centre local trop haut écarte les Centres plus faibles ; un Centre local trop bas réduit la base. Comparez avant de lancer, comme dans l'exemple.
- **Un niveau par Centre** : au niveau 1, seul le meilleur Centre éligible compte ; chaque niveau en ajoute un.
- **Il faut plusieurs planètes équipées** : sans autre Centre d'innovation de niveau suffisant, la Collaboration ne sert à rien.
- **Pas d'effet en cours de route** : améliorez vos Centres avant de lancer une longue étude, pas pendant.
- **Les lunes ne comptent pas** : un Centre d'innovation ne se construit que sur une planète.

## Pages liées

- [Liste des technologies](/fr/research/technologies)
- [Arbre technologique](/fr/research/tech-tree)
- [Le Théoricien](/fr/dynasty/classes/theorist)
- [Coloniser](/fr/universe/colonization)
