---
wiki_id: 25
locale: "fr"
path: "economy/repair-station"
url: "https://wiki.dynastynova.com/fr/economy/repair-station"
title: "Station de réparation"
description: "Récupérer une part des vaisseaux détruits en défense."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:33.619Z"
updated: "2026-10-02T17:40:15.731Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Station de réparation

> **En bref** : après un combat où votre planète a perdu des vaisseaux en défense, la Station de réparation en récupère une partie et vous les rend réparés, au bout de 30 minutes à 12 heures. La part récupérée augmente avec son niveau. Elle n'occupe aucune case.
{.is-info}

> **Paramètre d'univers** : la part récupérée dépend du taux de débris de l'univers, et la durée de réparation de sa vitesse de chantier.
> Par défaut : débris **30 %**, chantier **×1** · Redline : débris **30 %**, chantier **×1**
{.is-info}

<img src="/images/illustrations/facilities/station-de-reparation.jpg" width="180" alt="Station de réparation">

## Règles

1. La Station intervient après **tout combat où votre planète défend et perd des vaisseaux**, que vous gagniez ou perdiez le combat.
2. Elle récupère une part des vaisseaux détruits : **part = coefficient du niveau × (1 − taux de débris)**. Le coefficient va de 45 % au niveau 1 à 54 % au niveau 10 ; certains talents l'augmentent.
3. La part s'applique **à chaque type de vaisseau séparément**, arrondie à l'inférieur : quelques pertes peuvent ne rien rapporter.
4. **Il n'y a pas de tirage** : la part est fixe.
5. **Durée** : la Station répare **10 points de structure par seconde et par niveau**, multipliés par la vitesse de chantier de l'univers. La durée est comprise entre **30 minutes et 12 heures**. Tous les vaisseaux d'un même combat reviennent en même temps.
6. Pendant la réparation, les vaisseaux sont **hors de la planète** : ils ne défendent pas, ne peuvent être ni détruits ni pillés, et ne comptent ni dans vos flottes ni dans vos points. Ils reviennent intacts.
7. Une réparation **ne peut pas être annulée**.
8. Les vaisseaux récupérés apparaissent dans les **pertes** du rapport de combat, avec une mention.
9. La Station **n'occupe aucune case** et ne consomme pas d'énergie en fonctionnement ; l'énergie n'est qu'un seuil requis pour la construire.
10. Les **défenses** ne sont pas concernées : elles ont leur propre reconstruction (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)).

## Exemple chiffré

Vous perdez **100 Intercepteurs** en défense, avec une Station de réparation niveau 4, sur Redline :
- Part récupérée : 50 % × (1 − 30 %) = **35 %**, soit **35 Intercepteurs**.
- Structure à réparer : 35 × 4 000 = 140 000. Vitesse : 10 × 4 = 40 par seconde, soit 3 500 secondes : environ **58 minutes**.
- Si vous n'aviez perdu que 2 Intercepteurs : 35 % de 2 = 0,7, arrondi à **0** : rien n'est récupéré.

## Données détaillées

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Coefficient | 45 % | 48 % | 49 % | 50 % | 51 % | 52 % | 53 % | 53 % | 54 % | 54 % |
| Part récupérée (débris 30 %) | 31,5 % | 33,6 % | 34,3 % | 35 % | 35,7 % | 36,4 % | 37,1 % | 37,1 % | 37,8 % | 37,8 % |

Prérequis : Dock orbital 2. Coût du niveau 1 : 200 métal, 50 hydrogène, 50 énergie requise ; le coût est multiplié par 5 à chaque niveau, l'énergie requise par 2,5.

## Pièges fréquents

- **Les petites pertes ne rapportent rien** : l'arrondi se fait par type de vaisseau.
- **Les vaisseaux en réparation ne vous défendent pas** : une nouvelle attaque pendant ce temps trouve une orbite plus vide.
- **Le coût grimpe très vite** : ×5 par niveau.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Champs de ruines](/fr/combat/debris)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
