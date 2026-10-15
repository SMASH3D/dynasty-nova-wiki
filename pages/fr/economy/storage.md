---
wiki_id: 20
locale: "fr"
path: "economy/storage"
url: "https://wiki.dynastynova.com/fr/economy/storage"
title: "Le stockage"
description: "Capacités de stockage et débordement."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:24.087Z"
updated: "2026-10-15T18:54:19.377Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Le stockage

> **En bref** : chaque planète stocke ses propres ressources, dans la limite de ses entrepôts. La production remplit les entrepôts jusqu'à leur capacité, jamais au-delà, puis s'arrête jusqu'à ce que vous dépensiez. Ce qui dépasse déjà la capacité reste utilisable.
{.is-info}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Dépôt d'alliages"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Chambre cristalline"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Citerne d'hydrogène">

## Règles

1. Chaque planète a une **capacité par ressource** : métal, cristal, hydrogène.
2. La **Base planetaire** fournit **10 000** de capacité pour chaque ressource. Une **lune**, qui n'a ni Base planetaire ni entrepôts, stocke elle aussi 10 000 de chaque ressource.
3. Chaque entrepôt ajoute sa capacité à une ressource : **Dépôt d'alliages** (métal), **Chambre cristalline** (cristal), **Citerne d'hydrogène** (hydrogène). Au niveau N, il contient 5 000 × partie entière(2,5 × e^(20 × N / 33)), jusqu'au niveau 20.
4. La production remplit l'entrepôt **jusqu'à sa capacité, jamais au-delà**. Quand le stock **atteint** la capacité, la **production de cette ressource s'arrête** ; elle reprend dès que le stock repasse en dessous.
5. Un stock **au-dessus** de la capacité reste entièrement utilisable : construction, recherche, chantier, transport.
6. Le **Centre logistique** agrandit la capacité de **10 % par niveau**, jusqu'à +100 % au niveau 10 (voir [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)).
7. Le talent d'alliance **Entrepôts fédérés** ajoute **10 %** de capacité par niveau (2 niveaux), et certains talents de dynastie en ajoutent aussi.
8. Ces bonus **s'additionnent** : ils ne se multiplient pas entre eux. Ils s'appliquent à toute la capacité de la planète, **les 10 000 de la Base planetaire compris**.

## Exemple chiffré

Dépôt d'alliages niveau 2 : 40 000, plus 10 000 de la Base planetaire, soit **50 000 métal**. Avec une production de 1 366 métal par heure, un stock vide est plein en 50 000 / 1 366 = **36,6 heures**.

Ajoutez un Centre logistique niveau 3 (+30 %) et Entrepôts fédérés niveau 2 (+20 %) :
- Bonus total : 30 % + 20 % = **+50 %** (et non 1,3 × 1,2).
- Capacité en métal : 50 000 × 1,5 = **75 000**.

## Données détaillées

Capacité d'un entrepôt au niveau N, sans la Base planetaire ni les bonus, et coût pour atteindre ce niveau (métal / cristal) :

| Niveau | Capacité | Dépôt d'alliages (métal) | Chambre cristalline | Citerne d'hydrogène |
|---|---|---|---|---|
| 1 | 20 000 | 1 000 | 1 000 / 500 | 1 000 / 1 000 |
| 2 | 40 000 | 2 000 | 2 000 / 1 000 | 2 000 / 2 000 |
| 3 | 75 000 | 4 000 | 4 000 / 2 000 | 4 000 / 4 000 |
| 4 | 140 000 | 8 000 | 8 000 / 4 000 | 8 000 / 8 000 |
| 5 | 255 000 | 16 000 | 16 000 / 8 000 | 16 000 / 16 000 |
| 6 | 470 000 | 32 000 | 32 000 / 16 000 | 32 000 / 32 000 |
| 7 | 865 000 | 64 000 | 64 000 / 32 000 | 64 000 / 64 000 |
| 8 | 1 590 000 | 128 000 | 128 000 / 64 000 | 128 000 / 128 000 |
| 9 | 2 920 000 | 256 000 | 256 000 / 128 000 | 256 000 / 256 000 |
| 10 | 5 355 000 | 512 000 | 512 000 / 256 000 | 512 000 / 512 000 |
| 11 | 9 820 000 | 1 024 000 | 1 024 000 / 512 000 | 1 024 000 / 1 024 000 |
| 12 | 18 005 000 | 2 048 000 | 2 048 000 / 1 024 000 | 2 048 000 / 2 048 000 |
| 13 | 33 005 000 | 4 096 000 | 4 096 000 / 2 048 000 | 4 096 000 / 4 096 000 |
| 14 | 60 510 000 | 8 192 000 | 8 192 000 / 4 096 000 | 8 192 000 / 8 192 000 |
| 15 | 110 925 000 | 16 384 000 | 16 384 000 / 8 192 000 | 16 384 000 / 16 384 000 |
| 16 | 203 350 000 | 32 768 000 | 32 768 000 / 16 384 000 | 32 768 000 / 32 768 000 |
| 17 | 372 785 000 | 65 536 000 | 65 536 000 / 32 768 000 | 65 536 000 / 65 536 000 |
| 18 | 683 385 000 | 131 072 000 | 131 072 000 / 65 536 000 | 131 072 000 / 131 072 000 |
| 19 | 1 252 785 000 | 262 144 000 | 262 144 000 / 131 072 000 | 262 144 000 / 262 144 000 |
| 20 | 2 296 600 000 | 524 288 000 | 524 288 000 / 262 144 000 | 524 288 000 / 524 288 000 |

## Pièges fréquents

- **Un entrepôt plein, c'est de la production perdue** : surveillez la barre de ressources, surtout avant une absence.
- **Un stock important attire les pillards** : voir [Pillage](/fr/combat/plunder).
- **Chaque planète compte à part** : les entrepôts d'une colonie ne servent qu'à elle.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Formules de l'économie](/fr/economy/formulas)
- [Pillage](/fr/combat/plunder)
