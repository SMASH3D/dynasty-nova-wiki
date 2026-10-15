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
updated: "2026-10-15T16:10:30.873Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Le stockage

> **En bref** : chaque planète stocke ses propres ressources, dans la limite de ses entrepôts. Quand le stock d'une ressource atteint sa capacité, sa production s'arrête jusqu'à ce que vous en dépensiez. Le surplus, lui, reste utilisable.
{.is-info}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Dépôt d'alliages"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Chambre cristalline"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Citerne d'hydrogène">

## Règles

1. Chaque planète a une **capacité par ressource** : métal, cristal, hydrogène.
2. La **Base planetaire** fournit **10 000** de capacité pour chaque ressource.
3. Les entrepôts augmentent la capacité : **Dépôt d'alliages** (métal), **Chambre cristalline** (cristal), **Citerne d'hydrogène** (hydrogène), jusqu'au niveau 20.
4. La production remplit l'entrepôt **jusqu'à sa capacité, jamais au-delà**. Quand le stock **atteint** la capacité, la **production de cette ressource s'arrête** ; elle reprend dès que le stock repasse en dessous.
5. Le **surplus reste utilisable** : construction, recherche, chantier, transport.
6. Le **Centre logistique** agrandit les entrepôts de **10 % par niveau**, jusqu'à +100 % au niveau 10 (voir [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)).
7. Le talent d'alliance **Entrepôts fédérés** ajoute 10 % de capacité par niveau.
8. Ces bonus, et ceux des talents de dynastie, **s'additionnent** : ils ne se multiplient pas entre eux. Ils s'appliquent à toute la capacité de la planète, **les 10 000 de la Base planetaire compris**.

## Exemple chiffré

Capacités relevées en jeu :
- Dépôt d'alliages niveau 2 : 40 000, plus 10 000 de la Base planetaire, soit **50 000 métal**.
- Chambre cristalline niveau 1 : 20 000 + 10 000 = **30 000 cristal**.

Avec 50 000 de capacité et une production de 1 366 métal/h, un stock vide est plein en **un peu moins de 37 heures**.

Ajoutez un Centre logistique niveau 3 (+30 %) et le talent Entrepôts fédérés niveau 2 (+20 %) :
- Bonus total : 30 % + 20 % = **+50 %** (et non 1,3 × 1,2).
- Capacité en métal : 50 000 × 1,5 = **75 000**.

## Données détaillées

| Entrepôt | Niveau 1 | Niveau 2 | Coût relevé |
|---|---|---|---|
| Dépôt d'alliages | 20 000 | 40 000 | niveau 3 : 4 000 métal |
| Chambre cristalline | 20 000 | 40 000 | niveau 2 : 2 000 métal, 1 000 cristal |
| Citerne d'hydrogène | 20 000 | 40 000 | niveau 2 : 2 000 métal, 2 000 cristal |

À ces capacités s'ajoutent les 10 000 de la Base planetaire. Les tables complètes seront ajoutées sur la page de chaque entrepôt.

## Pièges fréquents

- **Un entrepôt plein, c'est de la production perdue** : surveillez la barre de ressources, surtout avant une absence.
- **Un stock important attire les pillards** : l'attaquant emporte 50 % de chaque ressource.
- **Chaque planète compte à part** : les entrepôts d'une colonie ne servent qu'à elle.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Pillage](/fr/combat/plunder)
