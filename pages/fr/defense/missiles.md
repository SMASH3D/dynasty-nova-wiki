---
wiki_id: 42
locale: "fr"
path: "defense/missiles"
url: "https://wiki.dynastynova.com/fr/defense/missiles"
title: "Missiles"
description: "Arsenal balistique, Intercepteurs et Ogives longue portée."
tags: ["defense", "missiles"]
published: true
created: "2026-10-02T13:09:06.140Z"
updated: "2026-10-02T17:40:28.005Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Missiles

> **En bref** : les missiles se stockent dans l'Arsenal balistique. Les **Ogives longue portée** détruisent les défenses d'une planète ennemie de la même galaxie sans engager de flotte ; leur portée dépend du Moteur Magnétique. Les **Intercepteurs** abattent automatiquement, une pour une, les Ogives qui visent votre planète. Les missiles ne prennent jamais part aux combats de flottes.
{.is-info}

> **Paramètre d'univers** : la limite d'attaques, qui compte aussi les salves de missiles, peut être différente selon l'univers.
> Par défaut : **6 attaques par 24 h** · Redline : **6 attaques par 24 h**
{.is-info}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Arsenal balistique"> <img src="/images/illustrations/defense/intercepteurs.jpg" width="180" alt="Intercepteurs"> <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="180" alt="Ogives longue portée">

## Règles

### L'Arsenal balistique
1. Les missiles sont stockés dans l'**Arsenal balistique**, qui offre **10 cases par niveau** (niveau 10 au plus). Il ne se construit que sur une planète.
2. Un **Intercepteur** occupe **1 case**, une **Ogive longue portée** en occupe **2**.
3. Les missiles en file d'attente ou en construction comptent déjà : une commande qui ne tiendrait pas dans les cases libres est refusée avant toute dépense.
4. Les missiles n'occupent aucune case de la planète. Seul l'Arsenal lui-même occupe une case par niveau.
5. Démolir un niveau d'Arsenal alors qu'il est plein ne détruit aucun missile ; vous ne pouvez simplement plus en commander.
6. Les missiles ne tirent jamais pendant un combat, ne comptent pas dans la puissance défensive de la planète et ne peuvent pas être détruits par une salve.
7. **Points** : comme les défenses, 1 point par tranche de 1 000 ressources, dans les points militaires, tant qu'ils sont au silo. Un missile tiré, ou un Intercepteur consommé, sort de vos points.

### Portée et vol
8. **Portée** : avec le Moteur Magnétique au niveau $N$, une Ogive atteint toute planète située à au plus $5 \times N - 1$ systèmes, **dans la même galaxie** seulement.
   - $N$ : votre niveau de Moteur Magnétique. Une autre galaxie est toujours hors de portée, quel que soit le niveau.
9. Les systèmes d'une galaxie forment un anneau : le système 99 est voisin du système 1. La distance se compte par le plus court côté. La position dans le système ne compte pas.
10. **Durée du vol** : 30 secondes par système de distance, et 30 secondes au moins (même système). La cible n'est **pas prévenue** avant l'impact.
11. Une salve **ne peut pas être rappelée**. Les Ogives quittent le silo au lancement et ne reviennent jamais, même si la planète visée est abandonnée entre-temps.

### Cibles et restrictions
12. Une salve part d'une planète et vise une **planète** : jamais une lune, ni une case vide, ni l'une de vos planètes.
13. Interdit sur un membre de votre alliance, sur un joueur **en mode vacances** et sur un joueur protégé ([Protection des débutants](/fr/players/beginner-protection)). Vous ne pouvez pas tirer pendant vos propres vacances.
14. Une salve **compte comme une attaque** dans la [limite d'attaques](/fr/players/attack-limit) sur le joueur visé. Comme elle ne se rappelle pas, le créneau est consommé.
15. Tirer **met fin à votre propre protection de nouveau joueur**, définitivement.
16. Une planète abandonnée peut être visée : personne ne la défend, la limite d'attaques ne s'applique pas.
17. Pendant une **maintenance**, aucun tir n'est accepté ; une salve déjà en vol arrive normalement.

### À l'impact
18. **Interception** : chaque Intercepteur de la planète visée abat **une Ogive**, automatiquement, avant tout dégât. Il est consommé.
19. **Dégâts** : chaque Ogive qui passe apporte $12\,000 \times (1 + 0{,}1 \times S)$ dégâts, mis en commun pour toute la salve (arrondi à l'inférieur).
   - $S$ : niveau de Systèmes Offensifs du tireur.
20. **Résistance** d'une défense : son bouclier + sa coque de combat, avec les recherches et bonus du défenseur (voir [Liste des défenses](/fr/defense/defenses), règle 8).
21. **Ordre des cibles** : la cible désignée d'abord (si la planète en a), puis les défenses par résistance décroissante. Sans cible désignée, la plus résistante d'abord.
22. Une défense n'est détruite qu'**entière**. Sur chaque ligne, la salve détruit autant d'unités que ses dégâts restants en paient ; si elle ne peut plus en payer une seule, elle passe à la ligne suivante, moins résistante. Ce qui reste à la fin est perdu.
23. Une salve **ne détruit que des défenses** : jamais les bâtiments, la flotte en orbite, les ressources ni les missiles du silo.
24. Les défenses détruites par une Ogive sont **perdues définitivement** : pas de reconstruction gratuite. Leurs points sont retirés.
25. Le tireur et le défenseur reçoivent un rapport : Ogives tirées, interceptées, arrivées, défenses touchées et planète d'origine.
26. Certains talents de dynastie modifient la portée, la capacité de l'Arsenal, les dégâts et l'interception (voir [Dynastie et talents](/fr/dynasty)).

## Exemple chiffré

**Remplir un Arsenal balistique niveau 3**
- Capacité : 3 × 10 = **30 cases**.
- 10 Intercepteurs (10 cases) + 10 Ogives longue portée (20 cases) = 30 : l'Arsenal est plein.
- Coût des 10 Ogives : 125 000 métal, 25 000 cristal, 100 000 hydrogène, soit 250 points militaires, retirés quand elles partent.

**Portée et vol** (Moteur Magnétique 4)
- Portée : 5 × 4 − 1 = **19 systèmes**.
- De [3:40:8] vers [3:55:4] : 15 systèmes, à portée. Vol : 15 × 30 = 450 secondes, soit **7 min 30 s**.
- De [5:97:6] vers [5:3:10] : l'anneau passe par 98, 99, 1, 2, 3, soit **5 systèmes**, à portée dès le Moteur Magnétique 2 ; vol de 2 min 30 s.
- Vers [4:40:8] : autre galaxie, **hors de portée**.

**Une salve de 5 Ogives** tirée avec Systèmes Offensifs 6, sur une planète qui a 3 Intercepteurs, 1 Dôme protecteur, 2 Éjecteurs à plasma et 40 Projecteurs balistiques (défenseur à Champs de Protection 4 et Métallurgie Avancée 5)
- Interception : 3 Ogives abattues, **2 arrivent**. Les 3 Intercepteurs sont consommés.
- Dégâts : 2 × 12 000 × 1,6 = **38 400**.
- Résistances : Dôme 29 000, Éjecteur à plasma 15 420, Projecteur balistique 328.
- Sans cible désignée : 1 Dôme protecteur (1 × 29 000) : 38 400 → 9 400 ; 28 Projecteurs balistiques (28 × 328) : 9 400 → 216. Les Éjecteurs (il faudrait 15 420) sont sautés. Bilan : **1 Dôme protecteur, 28 Projecteurs balistiques**, 216 dégâts perdus.
- Cible désignée « Éjecteur à plasma » : 2 Éjecteurs à plasma (2 × 15 420) : 38 400 → 7 560 ; 23 Projecteurs balistiques (23 × 328) : 7 560 → 16. Le Dôme est sauté. Bilan : **2 Éjecteurs à plasma, 23 Projecteurs balistiques**, 16 dégâts perdus.

## Données détaillées

### Missiles

| Missile | Métal | Cristal | Hydrogène | Points | Cases d'Arsenal | Dégâts | Durée de base | Prérequis |
|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/intercepteurs.jpg" width="48" alt="Intercepteurs"> Intercepteurs | 8 000 | 2 000 | 0 | 10 | 1 | aucun | 3 h 12 min | Dock orbital 1, Arsenal balistique 2 |
| <img src="/images/illustrations/defense/ogives-longue-portee.jpg" width="48" alt="Ogives longue portée"> Ogives longue portée | 12 500 | 2 500 | 10 000 | 25 | 2 | 12 000 | 6 h | Dock orbital 1, Arsenal balistique 4, Moteur Magnétique 1 |

Les dégâts sont ceux d'une Ogive sans recherche (règle 19). Un Intercepteur ne fait aucun dégât : il ne sert qu'à abattre une Ogive. Le Moteur Magnétique 1 requis pour les Ogives donne déjà une portée de 4 systèmes.

### Arsenal balistique

Prérequis : Dock orbital 1. Le coût double à chaque niveau.

| Niveau | Métal | Cristal | Hydrogène | Cases | Ogives au plus | Intercepteurs au plus |
|---|---|---|---|---|---|---|
| 1 | 20 000 | 20 000 | 1 000 | 10 | 5 | 10 |
| 2 | 40 000 | 40 000 | 2 000 | 20 | 10 | 20 |
| 3 | 80 000 | 80 000 | 4 000 | 30 | 15 | 30 |
| 4 | 160 000 | 160 000 | 8 000 | 40 | 20 | 40 |
| 5 | 320 000 | 320 000 | 16 000 | 50 | 25 | 50 |
| 6 | 640 000 | 640 000 | 32 000 | 60 | 30 | 60 |
| 7 | 1 280 000 | 1 280 000 | 64 000 | 70 | 35 | 70 |
| 8 | 2 560 000 | 2 560 000 | 128 000 | 80 | 40 | 80 |
| 9 | 5 120 000 | 5 120 000 | 256 000 | 90 | 45 | 90 |
| 10 | 10 240 000 | 10 240 000 | 512 000 | 100 | 50 | 100 |

### Portée selon le Moteur Magnétique

| Moteur Magnétique | Portée (systèmes) | Vol jusqu'à la limite |
|---|---|---|
| 1 | 4 | 2 min |
| 2 | 9 | 4 min 30 s |
| 3 | 14 | 7 min |
| 4 | 19 | 9 min 30 s |
| 5 | 24 | 12 min |
| 6 | 29 | 14 min 30 s |
| 7 | 34 | 17 min |
| 8 | 39 | 19 min 30 s |
| 9 | 44 | 22 min |
| 10 | 49 | 24 min 30 s |

Sur Redline, une galaxie compte 99 systèmes : par le plus court côté de l'anneau, aucun n'est à plus de 49 systèmes. Le niveau 10 couvre donc toute votre galaxie.

### Résistance des défenses face aux Ogives (sans recherche du défenseur)

| Défense | Résistance (bouclier + coque) | Ogives pour une unité |
|---|---|---|
| Dôme protecteur | 20 000 | 2 |
| Éjecteur à plasma | 10 300 | 1 |
| Barrière défensive | 4 000 | 1 |
| Accélérateur magnétique | 3 700 | 1 |
| Batterie ionique | 1 300 | 1 |
| Émetteur à haute énergie | 900 | 1 |
| Canon photonique | 225 | 1 |
| Projecteur balistique | 220 | 1 |

« Ogives pour une unité » : Ogives arrivées nécessaires, sans recherche chez le tireur, pour détruire une unité seule.

## Pièges fréquents

- **« Intercepteurs » n'est pas l'« Intercepteur »** : le missile (pluriel) et le vaisseau de combat (singulier) n'ont rien à voir.
- **Pas de missile entre galaxies** : la portée ne compte que les systèmes de votre galaxie.
- **Le Dôme part en premier** : sans cible désignée, la défense la plus résistante est frappée d'abord. Désignez une cible si vous visez autre chose.
- **Une salve trop faible passe à côté** : une Ogive seule ne détruit pas un Dôme sans recherche ; ses dégâts vont aux défenses suivantes.
- **Une salve coûte un créneau d'attaque** : elle compte dans la limite d'attaques sur le joueur, même si elle ne détruit rien.
- **Fin de la protection de nouveau joueur** : votre première salve y met fin, comme une attaque de flotte.
- **Les missiles ne défendent pas contre les flottes** : seuls les Intercepteurs servent en défense, et uniquement contre les Ogives.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes)
- [Limite d'attaques](/fr/players/attack-limit)
- [Protection des débutants](/fr/players/beginner-protection)
- [Mode vacances](/fr/players/vacation-mode)
- [Maintenance](/fr/misc/maintenance)
