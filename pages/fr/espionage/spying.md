---
wiki_id: 52
locale: "fr"
path: "espionage/spying"
url: "https://wiki.dynastynova.com/fr/espionage/spying"
title: "Espionner"
description: "Envoyer des Éclaireurs : niveau de détail, vision partagée, risques et alertes."
tags: ["espionage"]
published: true
created: "2026-10-02T13:09:25.232Z"
updated: "2026-10-15T18:54:25.308Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Espionner

> **En bref** : envoyez des Éclaireurs sur une planète ou une lune pour obtenir un rapport sur ses ressources, sa flotte, ses défenses, ses bâtiments et ses recherches. Ce que vous voyez dépend de votre écart de Renseignement Tactique avec la cible et du nombre d'Éclaireurs envoyés. Si la cible a des vaisseaux en orbite, vos sondes peuvent être abattues.
{.is-info}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Éclaireur">

## Règles

### Envoyer des sondes

1. L'espionnage se fait en mission **Espionnage**, avec des **Éclaireurs seulement** : aucun autre vaisseau ne peut les accompagner. Le bouton d'espionnage rapide de la [vue galaxie](/fr/universe/galaxy-view) lance la même mission.
2. Vous pouvez espionner toute **planète ou lune** qui n'est pas à vous : un joueur protégé, un membre de votre alliance, une planète inhabitée ou abandonnée. L'espace lointain ne s'espionne pas.
3. L'espionnage **ne compte pas** dans la limite d'attaques et ne met pas fin à votre protection.
4. L'hydrogène facturé pour une mission d'espionnage baisse de **5 %** par niveau de **Renseignement Tactique**, jusqu'à **la moitié** au niveau 10 (arrondi à l'unité inférieure). La consommation du vol, elle, ne change pas.
5. Pendant une **maintenance**, l'espionnage est suspendu. Si **vous** êtes en mode vacances, vous ne pouvez envoyer aucune mission.

### La case découverte

6. Une case de la vue galaxie reste illisible tant que personne ne l'a espionnée pour vous. Dès votre premier espionnage, sa planète et son propriétaire s'affichent, **sans limite de durée**.
7. **Vision partagée d'alliance** : chaque case qu'un membre espionne est découverte pour **toute l'alliance**. En rejoignant une alliance, vous lui apportez les cases que vous aviez déjà découvertes. Une case connue grâce à l'alliance porte la mention « Découverte par un membre de l'alliance », sans date : seule la découverte est partagée, jamais le rapport.
8. La vision partagée vaut dès votre arrivée dans l'alliance et disparaît quand vous la quittez. Vos propres découvertes vous restent.
9. Coloniser une planète ou recycler un champ de débris demande que la case ait été espionnée, par vous **ou par votre alliance**. Vos propres planètes et l'espace lointain en sont dispensés.

### Niveau de détail

10. Le **niveau effectif** de votre espionnage se calcule ainsi :

$$N = \max\left(0,\ R_a - R_d + \min\left(5,\ \left\lfloor \frac{E}{2} \right\rfloor\right)\right)$$

- $N$ : niveau effectif de l'espionnage ;
- $R_a$ : votre niveau de Renseignement Tactique, plus les niveaux de Réseau d'informateurs de votre alliance ;
- $R_d$ : le niveau de Renseignement Tactique de la cible, plus les niveaux de Contre-espionnage fédéré de son alliance ;
- $E$ : nombre d'Éclaireurs envoyés ; $\lfloor\ \rfloor$ : partie entière.

11. Selon ce niveau, le rapport révèle : les **ressources** dès 1, la **flotte** dès 3, les **défenses et missiles** dès 5, les **bâtiments** dès 7, les **recherches** dès 9. Le type, la taille et les températures de la planète sont toujours visibles.
12. Chaque paire d'Éclaireurs ajoute 1 niveau, jusqu'à **+5 avec 10 Éclaireurs**. Au-delà, le bonus ne monte plus : les bâtiments et les recherches demandent une vraie avance en Renseignement Tactique.
13. **Talents d'alliance** : **Réseau d'informateurs** ajoute 1 niveau à votre Renseignement Tactique quand vous espionnez, **Contre-espionnage fédéré** 1 niveau à celui de vos planètes espionnées, par niveau de talent (3 niveaux chacun, branche Renseignement). Ces niveaux comptent comme de la recherche : ils changent le détail **et** le risque. Ils s'appliquent après **24 heures** dans l'alliance (voir [Missions et station d'alliance](/fr/players/alliance-missions)).
14. Certains **talents de dynastie** de l'[Ombre](/fr/dynasty/classes/shadow) lisent plus profond ou ouvrent la flotte et les ressources plus tôt. Ceux-là ne changent pas le risque.

### Risque pour les sondes

15. La **chance d'être abattu** se calcule ainsi, puis se borne entre **5 % et 25 %** :

$$C = (2 \times R_d - R_a) \times V \times 0{,}05$$

- $C$ : chance, en pourcentage, que la vague soit abattue ;
- $R_d$ et $R_a$ : les niveaux de la règle 10 ;
- $V$ : nombre de vaisseaux stationnés sur la planète ou la lune espionnée.

16. Le risque est **nul** si votre niveau atteint le **double** de celui de la cible, s'il n'y a **aucun vaisseau** en orbite (les défenses ne comptent pas), ou si la cible est inhabitée, abandonnée ou en vacances.
17. **Un seul tirage pour toute la vague** : toutes les sondes sont abattues, ou aucune. Le nombre d'Éclaireurs ne change pas le risque. Il n'y a pas de combat. Exceptions : certains talents de l'[Ombre](/fr/dynasty/classes/shadow) ramènent une partie d'une vague prise.
18. Une vague abattue rapporte **quand même** son rapport, qui indique combien de sondes ont été perdues. Les sondes perdues sont détruites pour de bon.

### Ce que voit la cible

19. La cible reçoit une **alerte d'intrusion** : « Sonde repérée », sans nom, si la vague est passée sans encombre.
20. Si la vague a été abattue, l'alerte **identifie** l'espion (son pseudo), et peut aussi **localiser son origine** (pseudo et coordonnées de la planète de départ).
21. Pas d'alerte sur une planète abandonnée, chez un joueur en vacances, ni pour un joueur qui a désactivé les alertes d'intrusion dans ses préférences de rapports.

## Exemple chiffré

Vous avez Renseignement Tactique 6, la cible le niveau 4.
- Avec **6 Éclaireurs** : (6 − 4) + min(5, 3) = **5** : ressources, flotte, défenses et missiles. Pas les bâtiments (il faut 7).
- Avec **10 Éclaireurs** : (6 − 4) + 5 = **7** : les bâtiments apparaissent. Les recherches (9) restent hors de portée, même avec plus de sondes.

Risque, si la cible a 30 vaisseaux en orbite : (2 × 4 − 6) × 30 × 0,05 = 3, relevé au plancher de **5 %**. Avec 100 vaisseaux : 10, soit **10 %**.

Si votre alliance détient Réseau d'informateurs niveau 2, votre niveau compte pour 6 + 2 = 8, le double de 4 : le risque tombe à **0 %**, et 6 Éclaireurs lisent désormais au niveau **7** (bâtiments compris).

## Données détaillées

| Niveau effectif | Le rapport révèle aussi |
|---|---|
| 0 | rien de plus que la planète (type, taille, températures) |
| 1 à 2 | ressources |
| 3 à 4 | ressources, flotte |
| 5 à 6 | ressources, flotte, défenses et missiles |
| 7 à 8 | ressources, flotte, défenses et missiles, bâtiments |
| 9 et plus | ressources, flotte, défenses et missiles, bâtiments, recherches |

| Éclaireurs envoyés | 1 | 2 à 3 | 4 à 5 | 6 à 7 | 8 à 9 | 10 et plus |
|---|---|---|---|---|---|---|
| Bonus | 0 | +1 | +2 | +3 | +4 | +5 |

Hydrogène facturé pour une mission d'espionnage, selon votre niveau de Renseignement Tactique (part du coût normal) :

| Niveau | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Facturé | 100 % | 95 % | 90 % | 85 % | 80 % | 75 % |

| Niveau | 6 | 7 | 8 | 9 | 10 | 11 à 15 |
|---|---|---|---|---|---|---|
| Facturé | 70 % | 65 % | 60 % | 55 % | 50 % | 50 % |

## Pièges fréquents

- **Inutile d'envoyer plus de 10 sondes** : le bonus plafonne à +5, et le risque ne dépend pas du nombre.
- **Toutes ou aucune** : si le tirage échoue, vous perdez toute la vague.
- **Une orbite vide n'abat aucune sonde** : sans vaisseau stationné, le risque est nul, même avec beaucoup de défenses.
- **Le talent d'alliance de la cible compte aussi** : Contre-espionnage fédéré augmente à la fois sa protection et le risque pour vos sondes.
- **Espionner un allié est permis** : il reçoit l'alerte comme n'importe qui.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Liste des technologies](/fr/research/technologies)
- [Missions et station d'alliance](/fr/players/alliance-missions)
