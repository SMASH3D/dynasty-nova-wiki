---
wiki_id: 50
locale: "fr"
path: "combat/moon-destruction"
url: "https://wiki.dynastynova.com/fr/combat/moon-destruction"
title: "Destruction de lune"
description: "Détruire une lune avec des Colossus stellaires."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:21.362Z"
updated: "2026-10-15T18:53:55.673Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Destruction de lune

> **En bref** : une flotte composée uniquement de Colossus stellaires peut tenter de détruire la lune d'un autre joueur. Elle doit d'abord gagner le combat contre ce qui défend la lune. Ensuite, deux tirages indépendants décident si la lune est détruite et si les Colossus sont perdus.
{.is-info}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Colossus stellaire">

## Règles

### La mission
1. La mission **Destruction de lune** demande une flotte composée **uniquement de Colossus stellaires**, et vise la **lune** d'un autre joueur. Elle n'est pas proposée sur une planète.
2. Elle suit les mêmes conditions qu'une attaque : elle n'est pas proposée contre un joueur protégé, un membre de votre alliance ou une cible dont la [limite d'attaques](/fr/players/attack-limit) est atteinte.

### Le combat
3. Un **combat classique** a lieu d'abord, contre les vaisseaux et les défenses **de la lune**. Voir [Déroulement d'un combat](/fr/combat/how-combat-works).
4. Les défenses de la lune détruites suivent la [reconstruction des défenses](/fr/combat/defense-rebuild).
5. Ce combat ne laisse **ni pillage, ni débris, ni lune nouvelle**.

### Les deux tirages
6. Les tirages n'ont lieu qu'en cas de **victoire** de l'attaquant. Sur un match nul ou une défaite, la lune n'est pas touchée et les survivants rentrent.
7. Avec $S$ le diamètre de la lune et $N$ le nombre de Colossus **survivants** :

$$p_{lune} = \min\left(100,\ (100 - \sqrt{S}) \times \sqrt{N}\right) \qquad p_{flotte} = \frac{\sqrt{S}}{2}$$

- $p_{lune}$ : chance de détruire la lune, en % ; $p_{flotte}$ : chance de perdre toute la flotte, en %.
- $S$ : diamètre de la lune en km ; $N$ : Colossus stellaires encore debout après le combat.

8. Les deux tirages sont **indépendants** et ont lieu tous les deux, que la lune soit détruite ou non. Les quatre issues sont possibles, la pire étant une flotte perdue au-dessus d'une lune intacte.
9. La perte de la flotte est **un seul tirage pour toute la flotte** et **ne dépend pas du nombre de Colossus** : envoyer plus de Colossus n'améliore que la chance de détruire la lune.
10. Le talent **Briseur de lunes** ([Amiral](/fr/dynasty/classes/admiral)) multiplie le risque de perdre la flotte par 0,75. Le talent **La lune tient** ([Vétéran](/fr/dynasty/classes/veteran)) multiplie la chance de détruire la lune du Vétéran par 0,75.

### Les suites
11. Si la lune est détruite : tout ce qu'elle portait disparaît, et les points correspondants sont retirés à son propriétaire. Les flottes en route vers la lune, ou qui devaient y rentrer, sont redirigées vers la planète.
12. Chaque camp reçoit un rapport **Destruction de lune**, qui donne les deux chances même quand le combat est perdu. Ce rapport peut être désactivé dans les réglages des rapports.
13. Une lune dont le propriétaire est en vacances ne peut pas être visée.

## Exemple chiffré

Une lune de **8 944 km** (la plus grande taille possible) et **100 Colossus** survivants :
- √8 944 ≈ 94,6.
- Chance de détruire la lune : (100 − 94,6) × √100 ≈ **54,3 %**.
- Chance de perdre les Colossus : 94,6 / 2 ≈ **47,3 %**.
- Avec Briseur de lunes, le risque tombe à 47,3 % × 0,75 ≈ **35,5 %**. Contre un Vétéran qui a La lune tient, la chance de destruction tombe à 54,3 % × 0,75 ≈ **40,7 %**.

## Données détaillées

Chance de détruire la lune selon son diamètre et le nombre de Colossus survivants, et risque de perdre la flotte (sans talent). Les lunes mesurent de 3 605 à 8 944 km.

| Diamètre | 1 Colossus | 4 Colossus | 25 Colossus | 100 Colossus | 400 Colossus | Perte de la flotte |
|---|---|---|---|---|---|---|
| 3 605 km | 40,0 % | 79,9 % | 100,0 % | 100,0 % | 100,0 % | 30,0 % |
| 6 324 km | 20,5 % | 41,0 % | 100,0 % | 100,0 % | 100,0 % | 39,8 % |
| 8 944 km | 5,4 % | 10,9 % | 27,1 % | 54,3 % | 100,0 % | 47,3 % |

## Pièges fréquents

- **Une grosse lune est plus dure et plus dangereuse** : plus le diamètre est grand, plus la destruction est difficile et plus le risque de perdre la flotte est élevé.
- **Le nombre ne protège pas la flotte** : le risque de perte dépend seulement du diamètre.
- **Il faut gagner le combat d'abord** : sans victoire, aucun tirage. Les Colossus perdus pendant le combat ne comptent plus dans $N$.
- **Ni butin ni débris** : une destruction de lune ne rapporte rien en ressources, à aucun des deux camps.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Champs de ruines et formation des lunes](/fr/combat/debris)
