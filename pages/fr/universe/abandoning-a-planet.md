---
wiki_id: 15
locale: "fr"
path: "universe/abandoning-a-planet"
url: "https://wiki.dynastynova.com/fr/universe/abandoning-a-planet"
title: "Abandonner une colonie"
description: "Conditions et conséquences d'un abandon."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:14.263Z"
updated: "2026-10-15T18:55:00.934Z"
---

# Abandonner une colonie

> **En bref** : vous pouvez abandonner définitivement une colonie pour récupérer sa place. La planète reste sur la carte avec ce qu'elle contient, mais perd aussitôt une partie de ses bâtiments, de sa flotte et de ses défenses, puis se dégrade jusqu'à disparaître au bout de 60 jours. Tout autre joueur peut la piller ou la recoloniser pendant ce temps, et récupère alors ce qui reste.
{.is-info}

> **Paramètre d'univers** : toutes les valeurs de dégradation d'une planète abandonnée (pertes immédiates, rythme des pertes, durée de vie, délai avant que l'ancien propriétaire puisse la reprendre) peuvent être différentes selon l'univers.
> Par défaut : **valeurs du tableau ci-dessous** · Redline : **identiques**
{.is-info}

## Règles

### Conditions
1. La **planète mère** ne peut pas être abandonnée. Une lune ne s'abandonne pas seule : elle part avec sa planète.
2. L'abandon est impossible tant que quelque chose est en cours **sur cette planète ou sur sa lune** : construction de bâtiment, de vaisseaux ou de défenses, réparation, recherche lancée depuis cette planète, flotte en route depuis ou vers elle, frappe de missiles encore en vol. Le jeu affiche la liste de tout ce qui bloque. Vos autres planètes, elles, peuvent être occupées.
3. Pour confirmer, vous devez saisir le nom de la planète. **L'abandon est irréversible.**

### Conséquences immédiates
4. Vous perdez la planète **définitivement**. Rien n'est remboursé, et ses points sortent de votre score.
5. Vous récupérez **immédiatement une place de colonie**. Si vous regardiez cette planète, le jeu vous ramène sur votre planète mère.
6. Les ressources restent sur place, sans jamais se dégrader. La production s'arrête.
7. Le **premier choc**, sur la planète comme sur sa lune : chaque bâtiment perd **1 niveau**, la flotte perd **30 %** de chaque type de vaisseau et les défenses **35 %** de chaque type (arrondi à l'inférieur). Les Collecteurs solaires sont **tous perdus**.
8. Les vaisseaux détruits par ce choc laissent un **champ de ruines** en orbite, au taux de débris des vaisseaux de l'univers (30 % par défaut). Les défenses et les Collecteurs solaires n'en laissent pas.
9. La **lune** de la planète, et tout ce qu'elle porte, est abandonnée avec elle.

### Ensuite
10. Les bâtiments perdent 1 niveau **tous les 2 jours**. La flotte restante perd 5 % de ce qui reste tous les 2 jours, les défenses 5 % tous les 3 jours : au moins une unité à chaque fois, tant qu'il en reste.
11. Les autres joueurs peuvent l'**espionner, l'attaquer, la piller ou la recoloniser**. Personne ne peut y transporter de ressources. La limite d'attaques ne s'applique pas : la planète n'a plus de propriétaire.
12. Celui qui la recolonise reprend **tout ce qui reste**, lune comprise, et la dégradation s'arrête.
13. La planète **disparaît** au bout de **60 jours**, ou plus tôt quand il ne reste plus rien sur elle ni sur sa lune (tous les bâtiments à 0, plus aucun vaisseau ni défense). Les ressources disparaissent avec elle ; la position redevient libre, sous son nom d'origine. Les champs de ruines en orbite, eux, restent.
14. L'ancien propriétaire ne peut pas la recoloniser pendant **30 jours**.

## Exemple chiffré

Vous abandonnez une colonie avec un Excavateur minéral niveau 10, 1 000 Intercepteurs, 200 défenses d'un même type et 50 Collecteurs solaires.
- Aussitôt : Excavateur niveau **9** ; 300 Intercepteurs détruits, il en reste **700** ; il reste **130** défenses ; plus aucun Collecteur solaire.
- Les 300 Intercepteurs détruits laissent 300 × 3 000 × 30 % = **270 000 métal** et 300 × 1 000 × 30 % = **90 000 cristal** de débris.
- L'Excavateur tombe à 0 au bout de 18 jours. La planète dure tout de même 60 jours, tant qu'il reste des vaisseaux ou des défenses.

Ce qui reste au fil des jours :

| Jour | Excavateur minéral | Intercepteurs | Défenses |
|---|---|---|---|
| 0 | 9 | 700 | 130 |
| 2 | 8 | 665 | 130 |
| 6 | 6 | 601 | 118 |
| 10 | 4 | 543 | 113 |
| 20 | 0 | 422 | 98 |
| 40 | 0 | 255 | 72 |
| 60 | 0 | 156 | 53 |

Si un joueur la recolonise au bout de 6 jours, il récupère l'Excavateur au niveau **6**, 601 Intercepteurs, 118 défenses et toutes les ressources.

## Données détaillées

| Élément | Perte immédiate | Perte ensuite |
|---|---|---|
| Bâtiments | −1 niveau | −1 niveau tous les 2 jours |
| Vaisseaux | −30 % | −5 % de ce qui reste tous les 2 jours |
| Défenses | −35 % | −5 % de ce qui reste tous les 3 jours |
| Collecteurs solaires | −100 % |  |
| Ressources | aucune perte | aucune perte |
| Planète |  | disparaît au bout de 60 jours, ou plus tôt s'il n'y reste plus rien |
| Recolonisation par l'ancien propriétaire |  | interdite pendant 30 jours |

## Pièges fréquents

- **Videz la planète avant** : rapatriez flotte et ressources avant d'abandonner, sinon elles restent à la merci des pillards et de celui qui la recolonisera.
- **La lune est perdue aussi** : une lune et ses bâtiments partent avec la planète.
- **Pas de retour en arrière** : vous ne pourrez pas la reprendre avant 30 jours, et elle aura continué à se dégrader.
- **Tout doit être à l'arrêt, lune comprise** : une construction, une recherche ou une flotte en route bloque l'abandon.

## Pages liées

- [Coloniser](/fr/universe/colonization)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Les lunes](/fr/universe/moons)
- [Champs de débris](/fr/combat/debris)
