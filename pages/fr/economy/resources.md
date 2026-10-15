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
updated: "2026-10-02T17:40:45.988Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Les ressources

> **En bref** : trois ressources se stockent, le métal, le cristal et l'hydrogène, produites en continu par vos mines, même quand vous n'êtes pas connecté. L'énergie, quatrième ressource, ne se stocke pas : elle alimente les mines. Chaque planète a son propre stock.
{.is-info}

> **Paramètre d'univers** : la vitesse d'économie (production) peut être différente selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Métal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Cristal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogène"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Énergie">

## Règles

1. **Métal** : la ressource de base de toute construction. Produit par l'Excavateur minéral.
2. **Cristal** : indispensable aux technologies et aux composants avancés. Produit par l'Extracteur cristallin.
3. **Hydrogène** : le carburant des flottes, utilisé aussi par la recherche et le Réacteur thermonucléaire. Produit par le Condensateur d'hydrogène, davantage sur une planète froide.
4. **Énergie** : produite par les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires, consommée par les mines. Elle ne se stocke pas (voir [L'énergie](/fr/economy/energy)).
5. La production est **continue**, calculée à l'heure, et chaque planète a **son propre stock**, limité par ses entrepôts.
6. La **Base planetaire** fournit un petit revenu fixe : **20 métal et 10 cristal par heure**.
7. La production s'arrête quand le stock d'une ressource atteint sa capacité (voir [Le stockage](/fr/economy/storage)), pendant le [mode vacances](/fr/players/vacation-mode), ou quand un univers privé est gelé (voir [Univers privés](/fr/misc/private-universes)).
8. Bonus possibles : technologie Maîtrise du Plasma, talent d'alliance Extraction coordonnée (+5 % par niveau), température de la planète pour l'hydrogène, et **bonus de position** des colonies (jusqu'à +40 % de cristal en positions 1 à 3, jusqu'à +35 % de métal en positions 6 à 10 ; voir [Planètes](/fr/universe/planets)).

## Exemple chiffré

Production relevée en jeu sur une planète avec Excavateur minéral 13 et Extracteur cristallin 13, sans déficit d'énergie :
- Métal : 1 346 (Excavateur) + 20 (Base planetaire) = **1 366 par heure**, soit environ **32 800 par jour**.
- Cristal : 897 (Extracteur) + 10 (Base planetaire) = **907 par heure**.

## Données détaillées

### Production relevée en jeu (par heure, à pleine énergie)

| Niveau | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 |
|---|---|---|---|---|---|---|---|---|---|---|
| Excavateur minéral (métal) | 1 346 | 1 594 | 1 879 | 2 205 | 2 577 | 3 002 | 3 486 | 4 036 | 4 662 | 5 372 |
| Extracteur cristallin (cristal) | 897 | 1 063 | 1 253 | 1 470 | 1 718 | 2 001 | 2 324 | 2 690 | 3 108 | 3 581 |

| Niveau | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|
| Condensateur d'hydrogène (planète à 60 °C max) | 254 | 311 | 376 | 451 | 538 | 637 | 751 | 882 | 1 031 | 1 200 |

La production d'hydrogène varie avec la température maximale de la planète (voir [Planètes](/fr/universe/planets)).

## Pièges fréquents

- **L'hydrogène part en fumée** : chaque vol en consomme, aller et retour payés au départ pour la plupart des missions.
- **Un stock plein ne produit plus** : videz vos entrepôts ou agrandissez-les.
- **Le stock est local** : les ressources d'une colonie ne servent pas sur la planète mère, il faut les transporter.

## Pages liées

- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Liste des bâtiments](/fr/economy/buildings)
- [Planètes : taille, température, type](/fr/universe/planets)
