---
wiki_id: 53
locale: "fr"
path: "espionage/spy-report"
url: "https://wiki.dynastynova.com/fr/espionage/spy-report"
title: "Lire un rapport d'espionnage"
description: "Les sections du rapport, ce qui les débloque, et l'alerte d'intrusion."
tags: ["espionage"]
published: true
created: "2026-10-02T13:09:27.242Z"
updated: "2026-10-02T16:36:58.413Z"
---

# Lire un rapport d'espionnage

> **En bref** : un rapport d'espionnage décrit toujours la planète ou la lune visée, puis ouvre une section par palier atteint : ressources, flotte, défenses et missiles, bâtiments, recherches. Une section marquée « Niveau d'espionnage insuffisant » n'a pas été lue : cela ne veut pas dire que la cible n'a rien.
{.is-info}

## Règles

### L'en-tête

1. Le rapport indique la **cible** (planète ou lune, coordonnées, propriétaire), votre **base de départ**, et le sort de vos sondes : « 2 sondes perdues sur 10 », ou aucune perte.
2. Une case vide donne « Planète inhabitée ». Une planète abandonnée ne donne aucun propriétaire, mais depuis combien de jours elle est abandonnée : ses chiffres sont ceux du jour, dégradation comprise.

### Les caractéristiques, toujours visibles

3. Pour une **planète** : son type, sa taille en cases, les cases encore libres et ses températures minimale et maximale.
4. Pour une **lune** : son diamètre, ses cases, les cases libres et les températures, qui sont celles de sa planète.

### Les sections, selon le niveau effectif

5. Chaque section s'ouvre à son palier de **niveau effectif** (voir [Espionner](/fr/espionage/spying)) :
   - **Ressources** dès 1 : métal, cristal et hydrogène sur place à l'arrivée des sondes, production comprise jusqu'à cet instant (dans la limite des entrepôts) ;
   - **Flotte** dès 3 : les vaisseaux stationnés sur le corps espionné ;
   - **Défenses** et **Missiles** dès 5 : les missiles sont listés à part, car ils ne combattent pas ;
   - **Bâtiments** dès 7 : le niveau de chaque bâtiment ;
   - **Recherches** dès 9 : le niveau de chaque recherche du joueur.
6. Une section **non lue** s'affiche avec la mention « Niveau d'espionnage insuffisant ». Une section lue mais vide affiche « Aucun élément détecté » : là, la cible n'a vraiment rien.
7. Chez un joueur **en vacances**, le rapport donne la planète et son propriétaire, mais **aucune section**, quelle que soit votre avance.
8. Certains talents de dynastie ajoutent des lignes au rapport (activité de la cible, système voisin, production) ou le brouillent (flotte arrondie, stock en partie caché) : voir l'[Ombre](/fr/dynasty/classes/shadow) et l'[Oracle](/fr/dynasty/classes/oracle).

### Vos rapports

9. Le jeu garde vos **10 derniers rapports** d'espionnage sur une même cible ; les plus anciens sont supprimés.
10. Un rapport peut être **partagé** avec votre alliance (voir [Messagerie et rapports](/fr/players/messages-and-reports)) et **importé** dans le [simulateur de combat](/fr/combat/simulator).

### L'alerte d'intrusion (côté cible)

11. Le joueur espionné reçoit une **alerte d'intrusion** sur la planète ou la lune visée. Elle porte l'un de ces trois niveaux :
    - **Auteur inconnu** : la vague est passée, l'alerte dit seulement « Sonde repérée » ;
    - **Auteur identifié** : la vague a été abattue, l'alerte donne le pseudo de l'espion ;
    - **Origine localisée** : en plus, les coordonnées de la planète d'où les sondes sont parties.
12. L'alerte indique aussi combien de sondes votre défense a abattues.

## Exemple chiffré

Vous envoyez **2 Éclaireurs**. Le rapport montre les ressources et la flotte, mais les défenses sont marquées « Niveau d'espionnage insuffisant ».
- Le rapport a atteint le palier 3 avec un bonus de sondes de +1 : votre avance sur cette cible vaut au moins 3 − 1 = **2**.
- Pour lire les **défenses** (palier 5), il faut un bonus de 5 − 2 = 3, soit **6 Éclaireurs**.
- Pour les **bâtiments** (palier 7), il faut le bonus maximal de +5 : **10 Éclaireurs**.
- Les **recherches** (palier 9) demanderaient +7 : hors de portée des sondes. Il faut monter votre Renseignement Tactique.

## Pièges fréquents

- **« Niveau d'espionnage insuffisant » ≠ rien** : ne concluez jamais qu'une planète est sans défense parce que la section n'a pas été lue.
- **Le rapport vieillit** : la cible produit, construit et déplace sa flotte. Espionnez juste avant d'attaquer.
- **Un rapport vide peut signifier des vacances** : vérifiez le statut dans la vue galaxie.
- **Planète et lune sont deux cibles** : la flotte stationnée sur la lune n'apparaît pas dans le rapport de la planète, et l'inverse.

## Pages liées

- [Espionner](/fr/espionage/spying)
- [Pillage](/fr/combat/plunder)
- [Simulateur de combat](/fr/combat/simulator)
- [Messagerie et rapports](/fr/players/messages-and-reports)
