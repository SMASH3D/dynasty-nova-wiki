---
wiki_id: 21
locale: "fr"
path: "economy/buildings"
url: "https://wiki.dynastynova.com/fr/economy/buildings"
title: "Liste des bâtiments"
description: "Tous les bâtiments : rôle, niveau maximum, prérequis."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:26.048Z"
updated: "2026-10-15T16:27:40.705Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des bâtiments

> **En bref** : une planète compte jusqu'à 17 bâtiments. Une lune en accueille 5 : ses 3 bâtiments lunaires, plus la Fabrique d'automates et le Dock orbital. Les mines produisent les ressources, les centrales l'énergie, les entrepôts stockent, et les installations débloquent la recherche, les vaisseaux, les défenses et les missiles. Chaque niveau de bâtiment occupe une case de la planète.
{.is-info}

> **Paramètre d'univers** : la vitesse de construction des bâtiments peut être différente selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

1. Un bâtiment se construit **niveau par niveau**. Chaque niveau coûte plus cher que le précédent.
2. **Chaque niveau occupe une case** de la planète. Exceptions : la Base planetaire (une seule case, niveau unique) et la Station de réparation, qui n'occupe aucune case.
3. Les bâtiments ne peuvent **jamais être détruits par un ennemi**. Seul leur propriétaire peut les démolir (voir [Démolir un bâtiment](/fr/economy/demolition)).
4. Un bâtiment est **payé au lancement** de sa construction, pas à sa mise en file.
5. **Points** : chaque niveau rapporte 1 point par tranche de 1 000 ressources dépensées, comptés dans les points d'économie.
6. Chaque bâtiment a un **niveau maximum** : aller plus haut ne débloquerait rien.
7. La **Base planetaire** (Base Coloniale sur une colonie) est présente dès la fondation, ne peut pas être démolie, fournit le stockage de base et un petit revenu fixe.

## Exemple chiffré

Coûts relevés en jeu pour faire passer l'Excavateur minéral du niveau 13 au niveau 14 :
- **11 677 métal et 2 919 cristal**, soit 14 596 ressources, donc **14,6 points** d'économie.
- La production passe de 1 346 à **1 594 métal/h**, et la consommation d'énergie de 448 à **531**.

## Données détaillées

### Rôle, niveau maximum et prérequis

| Bâtiment | Catégorie | Rôle | Niveau max | Prérequis |
|---|---|---|---|---|
| <img src="/images/illustrations/buildings/base-planetaire.jpg" width="48" alt="Base planetaire / Base Coloniale"> Base planetaire / Base Coloniale | base | Cœur de la planète : stockage de base (10 000 de chaque ressource), revenu fixe (20 métal et 10 cristal par heure) | 1 | aucun |
| <img src="/images/illustrations/buildings/excavateur-mineral.jpg" width="48" alt="Excavateur minéral"> Excavateur minéral | production | Produit le métal | 50 | aucun |
| <img src="/images/illustrations/buildings/extracteur-cristallin.jpg" width="48" alt="Extracteur cristallin"> Extracteur cristallin | production | Produit le cristal | 50 | aucun |
| <img src="/images/illustrations/buildings/condensateur-d-hydrogene.jpg" width="48" alt="Condensateur d'hydrogène"> Condensateur d'hydrogène | production | Produit l'hydrogène, davantage sur une planète froide | 50 | aucun |
| <img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="48" alt="Capteurs photovoltaïques"> Capteurs photovoltaïques | énergie | Produit l'énergie, davantage sur une planète chaude | 50 | aucun |
| <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="48" alt="Réacteur thermonucléaire"> Réacteur thermonucléaire | énergie | Produit de l'énergie en consommant de l'hydrogène | 50 | Condensateur d'hydrogène 5, Science Énergétique 3 |
| <img src="/images/illustrations/buildings/depot-alliages.jpg" width="48" alt="Dépôt d'alliages"> Dépôt d'alliages | stockage | Augmente le stockage de métal | 20 | aucun |
| <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="48" alt="Chambre cristalline"> Chambre cristalline | stockage | Augmente le stockage de cristal | 20 | aucun |
| <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="48" alt="Citerne d'hydrogène"> Citerne d'hydrogène | stockage | Augmente le stockage d'hydrogène | 20 | aucun |
| <img src="/images/illustrations/facilities/centre-d-innovation.jpg" width="48" alt="Centre d'innovation"> Centre d'innovation | recherche | Permet la recherche et la rend plus rapide | 12 | aucun |
| <img src="/images/illustrations/facilities/fabrique-d-automates.jpg" width="48" alt="Fabrique d'automates"> Fabrique d'automates | installation | Accélère la construction des bâtiments | 10 | aucun |
| <img src="/images/illustrations/facilities/dock-orbital.jpg" width="48" alt="Dock orbital"> Dock orbital | installation | Construit vaisseaux et défenses | 12 | Fabrique d'automates 2 |
| <img src="/images/illustrations/facilities/assembleur-moleculaire.jpg" width="48" alt="Assembleur moléculaire"> Assembleur moléculaire | installation | Accélère fortement la construction | 10 | Fabrique d'automates 10, Calcul Quantique 10 |
| <img src="/images/illustrations/facilities/station-de-reparation.jpg" width="48" alt="Station de réparation"> Station de réparation | chantier | Récupère une part des vaisseaux détruits en défense | 10 | Dock orbital 2 |
| <img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="48" alt="Modulateur planétaire"> Modulateur planétaire | ressource | Ajoute des cases à la planète | 10 | Assembleur moléculaire 1, Science Énergétique 12 |
| <img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="48" alt="Arsenal balistique"> Arsenal balistique | ressource | Stocke les missiles | 10 | Dock orbital 1 |
| <img src="/images/illustrations/facilities/centre-logistique.jpg" width="48" alt="Centre logistique"> Centre logistique | ressource | Agrandit les entrepôts de 10 % par niveau | 10 | Calcul Quantique 2 |

### Bâtiments lunaires

| Bâtiment | Rôle |
|---|---|
| <img src="/images/illustrations/facilities/base-lunaire.jpg" width="48" alt="Base lunaire"> Base lunaire | Rend la surface d'une lune constructible : chaque niveau ouvre 3 cases et en occupe 1 |
| <img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="48" alt="Phalange de capteur"> Phalange de capteur | Repère les flottes autour d'une planète (voir [Phalange de capteur](/fr/espionage/sensor-phalanx)) |
| <img src="/images/illustrations/facilities/porte-de-saut.jpg" width="48" alt="Porte de saut"> Porte de saut | Saut instantané entre deux lunes (voir [Porte de saut](/fr/fleet/jump-gate)) |

Sur une lune, on peut aussi construire la **Fabrique d'automates** et le **Dock orbital**, aux mêmes coûts et avec les mêmes prérequis que sur une planète. Les autres bâtiments de planète n'y sont pas constructibles.

### Coûts relevés en jeu

Coût d'un niveau précis, relevé sur une planète de l'univers Redline. Le coût, l'énergie et la production de chaque niveau sont dans l'[annexe : les bâtiments niveau par niveau](/fr/economy/building-levels).

| Bâtiment | Niveau | Métal | Cristal | Hydrogène | Énergie requise |
|---|---|---|---|---|---|
| Excavateur minéral | 14 | 11 677 | 2 919 | 0 | |
| Extracteur cristallin | 14 | 21 617 | 10 808 | 0 | |
| Condensateur d'hydrogène | 10 | 8 649 | 2 883 | 0 | |
| Capteurs photovoltaïques | 14 | 14 596 | 5 838 | 0 | |
| Réacteur thermonucléaire | 2 | 1 620 | 648 | 324 | |
| Dépôt d'alliages | 3 | 4 000 | 0 | 0 | |
| Chambre cristalline | 2 | 2 000 | 1 000 | 0 | |
| Citerne d'hydrogène | 2 | 2 000 | 2 000 | 0 | |
| Centre d'innovation | 5 | 3 200 | 6 400 | 3 200 | |
| Fabrique d'automates | 5 | 6 400 | 1 920 | 3 200 | |
| Dock orbital | 5 | 6 400 | 3 200 | 1 600 | |
| Assembleur moléculaire | 1 | 1 000 000 | 500 000 | 100 000 | |
| Station de réparation | 1 | 200 | 0 | 50 | 50 |
| Modulateur planétaire | 1 | 0 | 50 000 | 100 000 | 1 000 |
| Arsenal balistique | 1 | 20 000 | 20 000 | 1 000 | |
| Centre logistique | 1 | 20 000 | 40 000 | 0 | |

L'**énergie requise** n'est pas consommée : la production d'énergie de la planète doit simplement atteindre ce seuil au lancement de la construction.

## Pièges fréquents

- **Mines et énergie vont ensemble** : chaque niveau de mine consomme plus d'énergie. Sans centrale suffisante, toute la production ralentit (voir [L'énergie](/fr/economy/energy)).
- **Les cases sont limitées** : chaque niveau en occupe une. Pensez au Modulateur planétaire avant de saturer votre planète.
- **Un ordre en file n'est pas payé** : il ne sera payé qu'au lancement. Si la planète n'a plus les ressources à ce moment-là, l'ordre est abandonné sans frais.
- **Niveaux maximum** : inutile de chercher à dépasser le niveau 12 du Centre d'innovation ou du Dock orbital, ni le niveau 10 de la Fabrique d'automates.

## Pages liées

- [Annexe : les bâtiments niveau par niveau](/fr/economy/building-levels)
- [Les ressources](/fr/economy/resources)
- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Files de construction](/fr/economy/build-queue)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Arbre technologique](/fr/research/tech-tree)
