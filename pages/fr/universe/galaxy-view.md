---
wiki_id: 12
locale: "fr"
path: "universe/galaxy-view"
url: "https://wiki.dynastynova.com/fr/universe/galaxy-view"
title: "La vue galaxie"
description: "Lire la vue galaxie, système par système."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:08.617Z"
updated: "2026-10-15T18:55:05.771Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# La vue galaxie

> **En bref** : la vue galaxie affiche un système à la fois, position par position, puis l'espace lointain et la Station stellaire. Une case que ni vous ni votre alliance n'avez espionnée reste illisible. Pour chaque planète découverte, vous voyez son propriétaire, ses points, ses badges, sa lune et ses débris. C'est aussi d'ici que vous espionnez d'un clic, partagez une position avec votre alliance, l'ajoutez à vos favoris ou lancez une mission.
{.is-info}

> **Paramètre d'univers** : le nombre d'attaques permises contre un même joueur et sa fenêtre peuvent être différents selon l'univers.
> Par défaut : **6 attaques par 24 h** · Redline : **6 attaques par 24 h**
{.is-info}

> **Paramètre d'univers** : le nombre de favoris peut être différent selon l'univers.
> Par défaut : **10, 200 en Premium** · Redline : **10, 200 en Premium**
{.is-info}

![La vue galaxie en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*La vue galaxie en affichage orbites : chaque planète a son aspect, selon son type et son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

![La vue galaxie en affichage liste](/images/screenshots/french/vue-galaxie.jpg)
*En affichage liste, les positions pas encore espionnées restent illisibles. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

### Se déplacer
1. La vue galaxie montre **un système** : toutes ses positions, puis deux lignes de plus, l'**espace lointain** et la **Station stellaire**.
2. **Navigation** : flèches ← / → du clavier pour changer de système, Ctrl + ← / → (⌘ sur Mac) pour changer de galaxie. Le sélecteur du bas permet aussi de saisir une galaxie et un système. Après le dernier système, on revient au premier.
3. À l'ouverture, la vue affiche le système de votre planète actuelle.
4. Deux affichages sont proposés sur grand écran : **Orbites** (par défaut) et **Liste**. Votre choix est mémorisé.

### Ce que vous voyez
5. **Cases inexplorées** : tant que ni vous ni un membre de votre alliance n'avez espionné une position, tout y reste caché. Une écriture exotique remplace le nom de la planète et celui de son propriétaire, et la vignette reste grise. Une case illisible peut être libre ou occupée : seul l'espionnage le révèle. Seul l'espionnage y est proposé.
6. **Une case espionnée le reste pour de bon** : chaque espionnage arrivé à destination révèle la position, pour vous et pour votre alliance. En rejoignant une alliance, vous lui apportez les cases que vous aviez déjà découvertes.
7. Sur une case découverte, une ligne affiche la position, la vignette avec ses **badges** (tableau ci-dessous), le nom de la planète (une couronne distingue planète mère et colonie), le propriétaire (en vert pour un allié, en rouge pour un ennemi), ses **points** et ses points militaires, et la pastille **« En vacances »** s'il y a lieu.
8. Le propriétaire peut aussi s'afficher **« Abandonnée »** (planète abandonnée, voir [Abandonner une colonie](/fr/universe/abandoning-a-planet)), **« Inhabitée »** (position libre) ou **« Vous »**.
9. Sur une case inexplorée, le nom d'un joueur qui vous a espionné ou attaqué depuis cette position peut apparaître, avec la mention de ce qu'il a fait.
10. Une **lune** s'affiche sur une sous-ligne, sous sa planète, avec son diamètre (et ses cases si c'est la vôtre). Elle a sa propre fiche.
11. En affichage Orbites, survoler une planète découverte montre ses points, sa **taille** en cases, sa **température**, ses débris et sa lune. En affichage Liste, taille et température sont dans la fiche de la case.
12. Un bandeau annonce une **pluie de comètes** quand l'univers en prévoit une, avec les galaxies touchées et un compte à rebours.

### Lignes spéciales
13. **Espace lointain** (position 16 sur Redline) : la ligne propose l'**expédition**, si l'univers les autorise, et le **recyclage** des débris qui s'y trouvent. Aucune planète ne s'y pose.
14. **Station stellaire** (position 17 sur Redline) : une par système. Le bouton **« Ouvrir la station »** mène à la [Banque stellaire](/fr/economy/stellar-bank) et, si vous avez une alliance, à sa trésorerie.

### Agir depuis une case
15. **Espionnage rapide** : le bouton de la ligne envoie **un Éclaireur** à vitesse maximale depuis votre planète actuelle. Il faut un Éclaireur disponible sur cette planète.
16. **Fiche de la case** : un clic ouvre la fiche, avec les missions possibles (espionner, attaquer, coloniser, transporter, recycler, frappe de missiles ; sur une lune : espionner, attaquer, détruire, transporter ; déployer sur vos propres planètes et lunes).
17. **Coloniser** et **recycler** demandent une case déjà espionnée, par vous ou par votre alliance.
18. **Partager une position** avec votre alliance : chaque membre l'ouvre dans sa propre vue galaxie, avec ce qu'il a le droit d'y voir. Le message reste **30 jours** dans le canal.
19. Une **étoile** ajoute la position (ou la lune) à vos **favoris**.
20. Vous pouvez écrire au propriétaire d'une planète découverte, sauf à un adversaire contrôlé par le jeu.
21. Si vous êtes en mode vacances, aucune mission n'est proposée.

## Exemple chiffré

Sur Redline, vous pouvez attaquer un même joueur **6 fois par 24 heures**. Vous l'avez déjà attaqué deux fois : sur sa ligne, le badge affiche **« Attaques restantes : 4 / 6 »**. Après 4 autres attaques, il affichera 0 / 6 et toute nouvelle attaque sera refusée jusqu'à ce que la première sorte de la fenêtre de 24 heures.

## Données détaillées

### Badges d'une case

Chaque coin de la vignette n'affiche qu'un badge à la fois.

| Coin | Badge | Signification |
|---|---|---|
| Haut gauche | Nouveau joueur | Joueur dans ses 7 premiers jours dans l'univers : ni attaque ni missiles |
| Haut gauche | Débutant protégé / Trop fort pour vous | Écart de points trop grand entre vous (voir [Protection des débutants](/fr/players/beginner-protection)) |
| Haut gauche | Attaques restantes : x / y | Attaques qu'il vous reste contre ce joueur dans la fenêtre en cours, affiché dès la première attaque |
| Haut droit | Champ de ruines | Débris en orbite, à recycler |
| Bas droit | Espionnée récemment | Vous l'avez espionnée il y a moins de 5 minutes |
| Bas droit | Découverte par un membre de l'alliance | Case révélée par l'espionnage d'un membre de votre alliance |
| Bas gauche | Membre de votre alliance, Sous pacte de non-agression, Sous pacte d'alliance, Ennemi | Relation entre votre alliance et la sienne |
| Bas gauche | Joueur IA (PvE) | Planète d'un adversaire contrôlé par le jeu |

## Pièges fréquents

- **Une case illisible ne dit rien** : elle peut cacher un joueur comme être vide. Envoyez un Éclaireur avant de conclure.
- **Pas de colonisation à l'aveugle** : une position jamais espionnée ne peut pas être colonisée.
- **Le compteur d'attaques est par joueur** : il compte toutes ses planètes ensemble.
- **L'espionnage rapide part de la planète sélectionnée** : sans Éclaireur sur cette planète, le bouton ne fonctionne pas.
- **Les débris sont à tout le monde** : un champ de ruines repéré revient au premier qui le recycle.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Protection des débutants](/fr/players/beginner-protection)
- [Limite d'attaques](/fr/players/attack-limit)
- [Espionner](/fr/espionage/spying)
- [Vue Empire et favoris](/fr/misc/empire-and-bookmarks)
- [Banque stellaire](/fr/economy/stellar-bank)
