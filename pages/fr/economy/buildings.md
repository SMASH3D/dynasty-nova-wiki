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
updated: "2026-10-02T17:40:09.414Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des bâtiments

> **En bref** : une planète compte jusqu'à 17 bâtiments. Une lune en accueille 5 : ses 3 bâtiments lunaires, plus la Fabrique d'automates et le Dock orbital. Les mines produisent les ressources, les centrales l'énergie, les entrepôts stockent, et les installations ouvrent la recherche, les vaisseaux, les défenses et les missiles. Chaque niveau de bâtiment occupe une case.
{.is-info}

> **Paramètre d'univers** : la vitesse de construction divise la durée de construction des bâtiments.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

1. Un bâtiment se construit **niveau par niveau**. Le coût du niveau N vaut le coût du niveau 1 × facteur^(N − 1), arrondi à l'inférieur pour chaque ressource (voir [Formules de l'économie](/fr/economy/formulas)).
2. **Chaque niveau occupe une case** de la planète. Exceptions : la Base planetaire (une case, niveau unique) et la Station de réparation, qui n'en occupe aucune.
3. Un ennemi ne peut **jamais détruire vos bâtiments**. Seul leur propriétaire peut les démolir (voir [Démolir un bâtiment](/fr/economy/demolition)) ; seule la destruction d'une lune emporte les bâtiments de cette lune.
4. Un bâtiment est **payé au lancement** de sa construction, pas à sa mise en file.
5. **Points** : chaque niveau rapporte 1 point par tranche de 1 000 ressources dépensées (métal, cristal et hydrogène), comptés dans les points d'économie.
6. Chaque bâtiment a un **niveau maximum**, sauf les bâtiments lunaires, limités par la place sur la lune.
7. La **Base planetaire** (Base Coloniale sur une colonie) est présente dès la fondation et ne peut pas être démolie.
8. Certains bâtiments demandent une **énergie requise** : la production d'énergie de la planète doit atteindre ce seuil au lancement de la construction, rien n'est consommé.
9. **Sur une lune** : la Base lunaire, la Phalange de capteur et la Porte de saut, plus la Fabrique d'automates et le Dock orbital, aux mêmes coûts et avec les mêmes prérequis que sur une planète. Une lune démarre avec 1 case ; chaque niveau de Base lunaire en ouvre 3 et en occupe 1, sans dépasser ce que permet le diamètre de la lune.

## Exemple chiffré

Faire passer l'Excavateur minéral du niveau 13 au niveau 14 :
- Coût : 60 × 1,5^13 = **11 677 métal** et 15 × 1,5^13 = **2 919 cristal**, soit 14 596 ressources et **14,6 points** d'économie.
- La production passe de 1 346 à **1 594 métal par heure**, la consommation d'énergie de 448 à **531**.
- Durée avec une Fabrique d'automates niveau 4 : 14 596 / (2 500 × 5) heures, soit **4 204 secondes** (1 h 10 min).

## Données détaillées

| Bâtiment | Catégorie | Rôle | Coût du niveau 1 (métal / cristal / hydrogène) | Facteur | Niveau max | Prérequis | Où |
|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/buildings/base-planetaire.jpg" width="48" alt="Base planetaire / Base Coloniale"> Base planetaire / Base Coloniale | base | Cœur de la planète : 10 000 de stockage par ressource, 20 métal et 10 cristal par heure | donnée à la fondation |  | 1 | aucun | planète |
| <img src="/images/illustrations/buildings/excavateur-mineral.jpg" width="48" alt="Excavateur minéral"> Excavateur minéral | production | Produit le métal | 60 / 15 / 0 | 1,5 | 50 | aucun | planète |
| <img src="/images/illustrations/buildings/extracteur-cristallin.jpg" width="48" alt="Extracteur cristallin"> Extracteur cristallin | production | Produit le cristal | 48 / 24 / 0 | 1,6 | 50 | aucun | planète |
| <img src="/images/illustrations/buildings/condensateur-d-hydrogene.jpg" width="48" alt="Condensateur d'hydrogène"> Condensateur d'hydrogène | production | Produit l'hydrogène, davantage sur une planète froide | 225 / 75 / 0 | 1,5 | 50 | aucun | planète |
| <img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="48" alt="Capteurs photovoltaïques"> Capteurs photovoltaïques | énergie | Produit l'énergie, davantage par temps chaud | 75 / 30 / 0 | 1,5 | 50 | aucun | planète |
| <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="48" alt="Réacteur thermonucléaire"> Réacteur thermonucléaire | énergie | Produit de l'énergie en consommant de l'hydrogène | 900 / 360 / 180 | 1,8 | 50 | Condensateur d'hydrogène 5, Science Énergétique 3 | planète |
| <img src="/images/illustrations/buildings/depot-alliages.jpg" width="48" alt="Dépôt d'alliages"> Dépôt d'alliages | stockage | Stocke le métal | 1 000 / 0 / 0 | 2 | 20 | aucun | planète |
| <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="48" alt="Chambre cristalline"> Chambre cristalline | stockage | Stocke le cristal | 1 000 / 500 / 0 | 2 | 20 | aucun | planète |
| <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="48" alt="Citerne d'hydrogène"> Citerne d'hydrogène | stockage | Stocke l'hydrogène | 1 000 / 1 000 / 0 | 2 | 20 | aucun | planète |
| <img src="/images/illustrations/facilities/centre-d-innovation.jpg" width="48" alt="Centre d'innovation"> Centre d'innovation | recherche | Permet la recherche et la rend plus rapide | 200 / 400 / 200 | 2 | 12 | aucun | planète |
| <img src="/images/illustrations/facilities/fabrique-d-automates.jpg" width="48" alt="Fabrique d'automates"> Fabrique d'automates | installation | Accélère la construction des bâtiments | 400 / 120 / 200 | 2 | 10 | aucun | planète et lune |
| <img src="/images/illustrations/facilities/dock-orbital.jpg" width="48" alt="Dock orbital"> Dock orbital | installation | Construit vaisseaux et défenses, et les construit plus vite à chaque niveau | 400 / 200 / 100 | 2 | 12 | Fabrique d'automates 2 | planète et lune |
| <img src="/images/illustrations/facilities/assembleur-moleculaire.jpg" width="48" alt="Assembleur moléculaire"> Assembleur moléculaire | installation | Divise par deux, à chaque niveau, la durée des bâtiments, des vaisseaux et des défenses | 1 000 000 / 500 000 / 100 000 | 2 | 10 | Fabrique d'automates 10, Calcul Quantique 10 | planète |
| <img src="/images/illustrations/facilities/station-de-reparation.jpg" width="48" alt="Station de réparation"> Station de réparation | chantier | Récupère une part des vaisseaux perdus en défense | 200 / 0 / 50 · 50 énergie requise | 5 (énergie requise : 2,5) | 10 | Dock orbital 2 | planète |
| <img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="48" alt="Modulateur planétaire"> Modulateur planétaire | ressource | Ajoute des cases à la planète | 0 / 50 000 / 100 000 · 1 000 énergie requise | 2 | 10 | Assembleur moléculaire 1, Science Énergétique 12 | planète |
| <img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="48" alt="Arsenal balistique"> Arsenal balistique | ressource | Stocke les missiles | 20 000 / 20 000 / 1 000 | 2 | 10 | Dock orbital 1 | planète |
| <img src="/images/illustrations/facilities/centre-logistique.jpg" width="48" alt="Centre logistique"> Centre logistique | ressource | Agrandit les entrepôts de 10 % par niveau | 20 000 / 40 000 / 0 | 2 | 10 | Calcul Quantique 2 | planète |
| <img src="/images/illustrations/facilities/base-lunaire.jpg" width="48" alt="Base lunaire"> Base lunaire | installation | Rend la surface de la lune constructible : chaque niveau ouvre 3 cases et en occupe 1 | 20 000 / 40 000 / 20 000 | 2 | aucun | aucun | lune |
| <img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="48" alt="Phalange de capteur"> Phalange de capteur | installation | Repère les flottes autour d'une planète | 20 000 / 40 000 / 20 000 | 2 | aucun | Base lunaire 1 | lune |
| <img src="/images/illustrations/facilities/porte-de-saut.jpg" width="48" alt="Porte de saut"> Porte de saut | installation | Saut instantané entre deux lunes | 2 000 000 / 4 000 000 / 2 000 000 | 2 | aucun | Base lunaire 1, Pliage Spatial 7 | lune |

Le coût du niveau N se calcule avec le facteur : par exemple, le Dock orbital niveau 5 coûte 400 × 2^4 = 6 400 métal, 3 200 cristal et 1 600 hydrogène.

## Pièges fréquents

- **Mines et énergie vont ensemble** : chaque niveau de mine consomme plus d'énergie. Sans centrale suffisante, toute la production ralentit (voir [L'énergie](/fr/economy/energy)).
- **Les cases sont limitées** : chaque niveau en occupe une. Pensez au Modulateur planétaire avant de saturer votre planète.
- **Un ordre en file n'est pas payé** : il ne sera payé qu'au lancement. Si la planète n'a plus les ressources à ce moment-là, l'ordre est abandonné sans frais.
- **Les facteurs ne sont pas tous égaux** : l'Extracteur cristallin (1,6) et le Réacteur (1,8) renchérissent plus vite que les autres mines.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Formules de l'économie](/fr/economy/formulas)
- [Files de construction](/fr/economy/build-queue)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Arbre technologique](/fr/research/tech-tree)
