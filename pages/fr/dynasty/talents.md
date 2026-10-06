---
locale: "fr"
path: "dynasty/talents"
url: "https://wiki.dynastynova.com/fr/dynasty/talents"
title: "Les talents"
description: "Les deux arbres, les points, les portes, le brouillon, la réinitialisation et les plafonds."
tags: ["dynasty"]
published: false
---

# Les talents

> **En bref** : vous avez deux arbres. L'**arbre commun** reçoit 1 point par niveau, 50 au maximum, et porte les bonus génériques. L'**arbre de classe** reçoit 1 point par 2 niveaux de maîtrise, 25 au maximum, et porte les mécaniques de votre classe. Vous préparez vos choix en brouillon, puis vous validez. Un point validé ne se reprend que par une réinitialisation.
{.is-info}

## Règles

### Deux arbres, deux réserves
1. L'**arbre commun** : 3 branches de 10 rangées, 28 points par branche. Il reçoit **1 point par niveau** de votre personnage, **50 au maximum**.
2. L'**arbre de classe** : 3 branches de 9 rangées, 15 points par branche. Il reçoit **1 point par 2 niveaux de maîtrise** de votre classe, arrondi au supérieur, **25 au maximum**. Voir [Maîtrise de classe](/fr/dynasty/classes#maîtrise-de-classe).
3. Les deux réserves sont **séparées** : un point commun ne va jamais dans l'arbre de classe, et l'inverse.

### Nœuds et rangées
4. Chaque rangée d'une branche contient un nœud. Trois sortes de nœuds :
   - **à rangs** : chaque point ajoute un rang (3 rangs dans l'arbre de classe, 3 ou 5 dans l'arbre commun) ;
   - **choix** : un seul point, deux options **A** et **B**, une seule à la fois ;
   - **clé** : un seul point, une mécanique.
5. La dernière rangée de chaque branche est un **ultime**. Chaque arbre a trois ultimes, et votre budget n'en permet qu'**un**.

### Portes
6. Une rangée s'ouvre quand les rangées au-dessus d'elle contiennent assez de points, **toutes branches confondues**.

| Arbre | Rangées 1 à 3 | Rangées 4 à 6 | Rangées 7 et 8 | Rangées 9 et 10 |
|---|---|---|---|---|
| Commun | ouvertes | 8 points | 20 points | 32 points |
| Classe | ouvertes | 5 points | 12 points (rangées 7 à 9) | |

7. Un **ultime** demande en plus le **niveau 40** et sa **branche pleine**.

### Brouillon et validation
8. Vous placez et retirez vos points librement en **brouillon**. Rien ne s'applique tant que vous n'avez pas cliqué sur **Valider**.
9. Un point validé est **définitif** : il ne se reprend que par une réinitialisation.

### Réinitialisation
10. Chaque arbre se réinitialise **séparément** et rend tous ses points.
11. La **première** réinitialisation de chaque arbre est **gratuite**. Les suivantes coûtent **20 Points stellaires** et demandent **24 heures** d'attente depuis la précédente.
12. Un [changement de classe](/fr/dynasty/classes#changer-de-classe) vide l'arbre de classe et rend sa prochaine réinitialisation gratuite. L'arbre commun ne bouge pas.

### Plafonds
13. Chaque bonus a un **plafond pour les talents** et un **plafond total**, talents d'alliance compris. Un point qui ferait dépasser un plafond n'ajoute rien.
14. Une classe peut renforcer un bonus commun, mais seulement sur un **périmètre étroit** (un type de mission, une famille de vaisseaux ou de bâtiments). C'est un **accent**, avec son propre plafond.
15. Les bonus de vitesse de flotte (talents et alliance) **divisent la durée du vol** : +50 % de vitesse = un vol 1,5 fois plus court. Voir [Déplacements](/fr/fleet/movement).

## Exemple chiffré

**Au niveau 20, avec une classe jouée depuis le début**
- Arbre commun : **20 points**. Les rangées 7 et 8 viennent de s'ouvrir.
- Arbre de classe : maîtrise 20, soit **10 points**. Les rangées 4 à 6 sont ouvertes, les rangées 7 à 9 attendent 12 points.

**Une branche commune pleine**
- Elle coûte 28 points. Ses rangées 1 à 8 en contiennent 22, mais la rangée 9 demande 32 points au-dessus d'elle : il faut en avoir placé **10 ailleurs** avant de la finir.
- Au niveau 50, il reste 22 points pour une deuxième branche, assez pour aller jusqu'à sa rangée 8, sans son ultime.
- Dans l'arbre de classe, les rangées 1 à 8 d'une branche contiennent 14 points : la porte de 12 s'ouvre sans rien placer ailleurs. Avec 25 points, il en reste 10 pour une deuxième branche, jusqu'à sa rangée 6.

**Une réinitialisation**
- Première réinitialisation de l'arbre commun : gratuite.
- Deuxième, le lendemain : 20 Points stellaires, possible 24 heures après la première.

## Données détaillées

### Points par niveau

L'expérience vient des quêtes et de votre record de points : **10 points d'expérience par point** de [classement](/fr/players/rankings), dans un univers à vitesse ×1.

> **Paramètre d'univers** : l'expérience par point de classement est divisée par la vitesse de l'univers.
> Par défaut : **10 par point** à vitesse ×1 · Redline : **10 par point**
{.is-info}

| Niveau | Expérience totale | Points communs | Points de classe (maîtrise égale) | Ce qui s'ouvre |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | commun et classe, rangées 1 à 3 |
| 8 | 500 | 8 | 4 | commun, rangées 4 à 6 |
| 10 | 1 221 | 10 | 5 | classe, rangées 4 à 6 |
| 20 | 43 939 | 20 | 10 | commun, rangées 7 et 8 |
| 24 | 100 397 | 24 | 12 | classe, rangées 7 à 9 |
| 32 | 437 052 | 32 | 16 | commun, rangées 9 et 10 |
| 40 | 1 773 675 | 40 | 20 | ultimes (avec la branche pleine) |
| 50 | 10 000 000 | 50 | 25 | tout le budget |

Au-delà du niveau 50, l'expérience continue de compter mais ne donne plus de point.

### Plafonds des bonus partagés

| Bonus | Arbre commun | Accent de classe | Plafond des talents | Plafond total (avec l'alliance) |
|---|---|---|---|---|
| Vitesse de flotte | 40 % | +10 % (attaques pour l'Amiral, missions pacifiques ou cibles abandonnées pour le Navigateur, recyclage pour l'Archiviste, attaque préparée pour l'Oracle) | 50 % | 60 % |
| Hydrogène consommé | −20 % | −5 % (vaisseaux de combat, Amiral) | −25 % | −45 % |
| Soutes | +25 % | | +25 % | +25 % |
| Flottes en vol | +2 | +1 (attaques, Amiral) | +3 | +3 |
| Recherche | +15 % | | +25 % | +45 % |
| Production des mines | +25 % | | +25 % | +45 % |
| Vitesse des bâtiments | +25 % | +15 % sur une famille (Centre d'innovation pour le Théoricien, centrales pour l'Énergéticien, rattrapage des colonies pour le Bâtisseur) | +40 % sur la famille | +50 % sur la famille |
| Vitesse des vaisseaux et défenses | +10 % | +15 % sur une famille (vaisseaux de combat pour l'Amiral, défenses et missiles pour le Vétéran, transporteurs et Récupérateurs pour le Navigateur) | +25 % sur la famille | |
| Coûts | | −5 % (Bâtisseur) | −5 % | |
| Cases de planète | +2 | +2 (Symbiote) | +4 | |
| Pillage des cibles abandonnées | +20 points | | +20 points | |
| Ressources à l'abri du pillage | 5 points | Vétéran (Abri souterrain), Oracle (La cache) | 15 points pour le Vétéran, 10 pour l'Oracle, arbre commun compris | taux de pillage jamais sous 30 % |

Les bonus qui ne servent qu'à vous, entre vos propres planètes ou sur vos retours (Vent arrière, Liaisons internes, Retour victorieux…), sont **hors** du plafond de vitesse.

## Pièges fréquents

- **Valider trop vite** : un point validé ne se reprend pas sans réinitialisation, et seule la première est gratuite.
- **Viser deux ultimes** : deux branches pleines demandent 56 points communs ou 30 points de classe. Le budget n'en permet qu'une.
- **Empiler un bonus au-delà de son plafond** : les points en trop ne donnent rien. Vérifiez le plafond avant d'ajouter un talent d'alliance sur le même bonus.
- **Lire +50 % de vitesse comme un vol deux fois plus court** : la vitesse divise la durée. +50 % donne un vol de 1 h en 40 min.

## Pages liées

- [Les classes](/fr/dynasty/classes)
- [L'arbre commun](/fr/dynasty/common-tree)
- [Missions et station d'alliance](/fr/players/alliance-missions)
- [Classements et points](/fr/players/rankings)
- [Déplacements](/fr/fleet/movement)
