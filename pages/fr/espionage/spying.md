---
wiki_id: 52
locale: "fr"
path: "espionage/spying"
url: "https://wiki.dynastynova.com/fr/espionage/spying"
title: "Espionner"
description: "Envoyer des Éclaireurs : niveau de détail, risques et contre-espionnage."
tags: ["espionage"]
published: true
created: "2026-10-02T13:09:25.232Z"
updated: "2026-10-06T10:31:03.704Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Espionner

> **En bref** : envoyez des Éclaireurs sur une planète pour obtenir un rapport sur ses ressources, sa flotte, ses défenses, ses bâtiments et ses recherches. Ce que vous voyez dépend de votre écart de Renseignement Tactique avec la cible et du nombre d'Éclaireurs. Le défenseur est toujours prévenu, et vos sondes peuvent être abattues.
{.is-info}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Éclaireur">

## Règles

### Envoyer des sondes
1. L'espionnage se fait avec des **Éclaireurs**, en mission Espionnage, ou d'un clic avec le bouton d'espionnage rapide de la [vue galaxie](/fr/universe/galaxy-view). Espionner une case **révèle** aussi, dans la vue galaxie, sa planète et son propriétaire, masqués jusque-là par une écriture illisible.
2. On peut espionner un joueur **protégé**. L'espionnage **ne compte pas** dans la limite d'attaques et ne met pas fin à votre protection de nouveau joueur.
3. Chaque niveau de **Renseignement Tactique** réduit de 5 % l'hydrogène facturé pour une mission d'espionnage, jusqu'à −50 %.
4. Espionner un joueur **en vacances** est possible : la case est cartographiée pour vous et votre alliance, mais le rapport ne révèle rien (ressources, flotte, défenses, bâtiments, recherches). Les sondes ne sont jamais abattues et le joueur absent n'est pas alerté.
5. Pendant une **maintenance**, l'espionnage est suspendu.

### Niveau de détail
6. **Niveau effectif** = (votre Renseignement Tactique − celui de la cible) + min(5, partie entière(nombre d'Éclaireurs / 2)), au minimum 0.
7. Selon ce niveau, le rapport révèle : les **ressources** dès 1, la **flotte** dès 3, les **défenses et missiles** dès 5, les **bâtiments** dès 7, les **recherches** dès 9.
8. Le bonus des Éclaireurs **plafonne à +5** (atteint avec 10 sondes).
9. Les talents d'alliance Réseau d'informateurs (attaque) et Contre-espionnage fédéré (défense) ajoutent chacun 1 niveau par niveau de talent.
10. Au **niveau 10** de Renseignement Tactique, une case espionnée reste **découverte** durablement.

### Risque pour les sondes
11. **Chance de destruction (en %)** = (2 × Renseignement de la cible − votre Renseignement) × nombre de vaisseaux stationnés chez elle × 0,05, bornée entre **5 % et 25 %**.
12. Le risque tombe à **0** si votre niveau est au moins le **double** de celui de la cible, s'il n'y a **aucun vaisseau** en orbite (les défenses ne comptent pas), ou si la cible est inhabitée, abandonnée ou en vacances.
13. **Un seul tirage pour toute la vague** : toutes les sondes sont détruites, ou aucune. Le nombre de sondes ne change pas le risque. Il n'y a pas de combat. Exception : les talents de l'[Ombre](/fr/dynasty/classes/shadow) Sondes larguées et Coques muettes font survivre une partie d'une vague prise.
14. Si vos sondes tombent, un second tirage décide si vous êtes **tracé** (pseudo et coordonnées) ou seulement **identifié** (pseudo).
15. Le défenseur reçoit **toujours** une alerte d'intrusion.

## Exemple chiffré

Vous avez Renseignement Tactique 6, la cible a le niveau 4, et vous envoyez **6 Éclaireurs**.
- Niveau effectif : (6 − 4) + min(5, 3) = **5** : ressources, flotte, défenses et missiles. Pas les bâtiments (il faudrait 7).
- Avec 10 Éclaireurs : (6 − 4) + 5 = **7** : les bâtiments apparaissent.

Risque, si la cible a 30 vaisseaux en orbite : (2 × 4 − 6) × 30 × 0,05 = 3 %, relevé au minimum de **5 %**. Avec Renseignement Tactique 8 (le double de 4), le risque tombe à **0**.

## Données détaillées

| Niveau effectif | Ce que révèle le rapport |
|---|---|
| 0 | Type, taille et températures de la planète seulement |
| 1 à 2 | + ressources |
| 3 à 4 | + flotte |
| 5 à 6 | + défenses et missiles |
| 7 à 8 | + bâtiments |
| 9 et plus | + recherches |

| Éclaireurs envoyés | 1 | 2 à 3 | 4 à 5 | 6 à 7 | 8 à 9 | 10 et plus |
|---|---|---|---|---|---|---|
| Bonus | 0 | +1 | +2 | +3 | +4 | +5 |

## Pièges fréquents

- **Inutile d'envoyer plus de 10 sondes** : le bonus plafonne à +5, et le risque ne dépend pas du nombre.
- **Toutes ou aucune** : si le tirage échoue, vous perdez toutes les sondes envoyées.
- **La cible sait** : elle reçoit une alerte à chaque espionnage, et peut vous identifier si vos sondes tombent.
- **Une orbite vide n'abat aucune sonde** : sans vaisseau stationné, le risque est nul, même avec beaucoup de défenses.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Liste des technologies](/fr/research/technologies)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Missions et station d'alliance](/fr/players/alliance-missions)
