---
wiki_id: 185
locale: "fr"
path: "dynasty/experience"
url: "https://wiki.dynastynova.com/fr/dynasty/experience"
title: "Expérience et niveau"
description: "D'où vient l'expérience, comment elle fait monter votre niveau et la maîtrise de votre classe."
tags: ["dynasty"]
published: true
created: "2026-10-30T20:31:21.434Z"
updated: "2026-10-30T20:31:23.812Z"
---

# Expérience et niveau

> **En bref** : l'expérience (XP) a **deux sources**, et deux seulement : les **quêtes** que vous réclamez, et votre **record de points** au [classement](/fr/players/rankings), qui vaut **10 XP par point**. Construire, rechercher et produire des vaisseaux ou des défenses fait monter vos points, donc votre XP. Les combats, le pillage et le recyclage n'en donnent pas directement. La même XP fait monter votre **niveau** et la **maîtrise de votre classe**.
{.is-info}

> **Paramètre d'univers** : l'XP gagnée par point de classement est divisée par la vitesse d'économie de l'univers. L'XP des quêtes ne change pas.
> Par défaut : **×1, 10 XP par point** · Redline : **×1, 10 XP par point**
{.is-info}

## Règles

### Les deux sources d'XP

1. **Les quêtes** : chaque quête réclamée verse son XP, et chaque grade terminé verse un bonus d'XP. Les montants sont fixes, quel que soit l'univers. Voir [Le didacticiel](/fr/getting-started/tutorial-quests).
2. **Votre record de points** : chaque fois que votre total de points dépasse votre meilleur total, l'écart vous rapporte **10 XP par point**.
3. Votre XP totale est la somme des deux.

$$\text{XP} = \text{XP}_{\text{quêtes}} + \left\lfloor \frac{10 \times R}{v} \right\rfloor$$

- $\text{XP}_{\text{quêtes}}$ : l'XP des quêtes et des grades réclamés.
- $R$ : votre record de points, c'est-à-dire le meilleur total de points que vous avez atteint dans cet univers.
- $v$ : la vitesse d'économie de l'univers (1 sur Redline).
- $\lfloor \cdot \rfloor$ : arrondi à l'entier inférieur.

### Ce qui fait monter vos points, donc votre XP

Rappel : un élément vaut **1 point par 1 000 ressources** de son coût de catalogue (métal, cristal et hydrogène), même si un talent vous l'a fait payer moins cher. Voir [Classements et points](/fr/players/rankings).

4. Chaque **niveau de bâtiment** terminé, y compris un niveau offert par un talent.
5. Chaque **niveau de recherche** terminé.
6. Chaque **vaisseau** et chaque **défense** livrés par le chantier, au fur et à mesure des livraisons.
7. Les **vaisseaux trouvés en expédition** : ils comptent comme s'ils avaient été construits, dès qu'ils rejoignent votre flotte.
8. La **reprise d'une planète abandonnée** : ce qui y est encore debout (bâtiments, vaisseaux, défenses) s'ajoute à vos points.

### Ce qui ne rapporte pas d'XP

9. **Les combats** : gagner une bataille ne donne pas d'XP. Les ressources pillées ou recyclées n'en donnent que lorsque vous les dépensez pour construire.
10. **Les ressources** produites, pillées, recyclées ou trouvées en expédition : tant qu'elles dorment dans vos entrepôts, elles ne rapportent rien.
11. **Les missions d'alliance** : elles font monter l'expérience de l'**alliance**, un compteur distinct du vôtre.

### Pertes et reconstruction

12. **L'XP ne se perd jamais.** Perdre des vaisseaux, tirer des missiles ou démolir un bâtiment fait baisser vos points, pas votre XP.
13. **Reconstruire ne rapporte rien tant que vous n'avez pas dépassé votre record.** Seuls les points gagnés au-delà de votre meilleur total comptent.

### Niveau

14. Votre niveau dépend uniquement de votre XP totale (tableau des seuils dans les [Données détaillées](#données-détaillées)).
15. Chaque niveau donne **1 point** de l'arbre commun, **50 au maximum**. Voir [Les talents](/fr/dynasty/talents).
16. Au-delà du niveau 50, l'XP continue de compter et le niveau de monter, chaque niveau coûtant autant que le 50e (**1 585 249 XP**), mais sans nouveau point de talent.
17. L'XP et le niveau sont **propres à chaque univers**.

### Maîtrise de classe

18. La maîtrise n'a **pas de source à part** : elle monte avec la même XP que votre niveau, en suivant la même courbe.
19. Une classe jouée depuis votre arrivée dans l'univers a sa maîtrise **égale à votre niveau**.
20. Une classe prise en cours de route repart de sa propre maîtrise (0 si vous ne l'avez jamais jouée) et monte avec l'XP gagnée **depuis** que vous l'avez choisie.
21. La maîtrise ne dépasse **jamais votre niveau**, ni 50.
22. La maîtrise donne les points de l'arbre de classe : **1 point par 2 niveaux de maîtrise**, arrondi au supérieur, **25 au maximum**. Voir [Les classes](/fr/dynasty/classes#maîtrise-de-classe).

## Exemple chiffré

Sur Redline (vitesse ×1). Vous avez réclamé le grade 1 du didacticiel (**100 XP**) et votre record est de **2 000 points** :
- XP totale : $100 + 10 \times 2\,000 = 20\,100$, soit le **niveau 16**.

Vous construisez un Cuirassé (45 000 métal, 15 000 cristal, soit 60 000 ressources) :
- **+60 points**, record porté à 2 060 : **+600 XP**, total 20 700.

Il est détruit en combat :
- **−60 points**, retour à 2 000. Votre XP reste à **20 700**.

Vous le reconstruisez :
- **+60 points**, retour à 2 060 : c'est votre record, pas au-delà. **+0 XP**.

Vous en construisez un deuxième :
- **+60 points**, record porté à 2 120 : **+600 XP**, total **21 300**. Vous passez au **niveau 17** (seuil à 20 974).

Le même Cuirassé, dans un univers dont l'économie tourne à ×2 : **+300 XP**.

**Changer de classe.** Au niveau 20 (43 939 XP), vous passez à une classe jamais jouée : maîtrise 0. Vous gagnez ensuite 10 699 XP :
- votre total atteint 54 638 XP : **niveau 21** ;
- la nouvelle classe a monté de 10 699 XP depuis le bas de la courbe : **maîtrise 14**, soit **7 points** de classe.

## Données détaillées

### Seuils des niveaux

| Niveau | XP totale pour l'atteindre | XP jusqu'au niveau suivant | Points communs | Points de classe (maîtrise égale) |
|---|---|---|---|---|
| 1 | 0 | 4 | 1 | 1 |
| 2 | 4 | 18 | 2 | 1 |
| 3 | 22 | 42 | 3 | 2 |
| 4 | 64 | 62 | 4 | 2 |
| 5 | 126 | 79 | 5 | 3 |
| 6 | 205 | 115 | 6 | 3 |
| 7 | 320 | 180 | 7 | 4 |
| 8 | 500 | 282 | 8 | 4 |
| 9 | 782 | 439 | 9 | 5 |
| 10 | 1 221 | 688 | 10 | 5 |
| 11 | 1 909 | 1 073 | 11 | 6 |
| 12 | 2 982 | 1 677 | 12 | 6 |
| 13 | 4 659 | 2 621 | 13 | 7 |
| 14 | 7 280 | 3 804 | 14 | 7 |
| 15 | 11 084 | 4 520 | 15 | 8 |
| 16 | 15 604 | 5 370 | 16 | 8 |
| 17 | 20 974 | 6 379 | 17 | 9 |
| 18 | 27 353 | 7 580 | 18 | 9 |
| 19 | 34 933 | 9 006 | 19 | 10 |
| 20 | 43 939 | 10 699 | 20 | 10 |
| 21 | 54 638 | 12 712 | 21 | 11 |
| 22 | 67 350 | 15 103 | 22 | 11 |
| 23 | 82 453 | 17 944 | 23 | 12 |
| 24 | 100 397 | 21 319 | 24 | 12 |
| 25 | 121 716 | 25 330 | 25 | 13 |
| 26 | 147 046 | 30 094 | 26 | 13 |
| 27 | 177 140 | 35 754 | 27 | 14 |
| 28 | 212 894 | 42 480 | 28 | 14 |
| 29 | 255 374 | 50 471 | 29 | 15 |
| 30 | 305 845 | 59 964 | 30 | 15 |
| 31 | 365 809 | 71 243 | 31 | 16 |
| 32 | 437 052 | 84 644 | 32 | 16 |
| 33 | 521 696 | 100 566 | 33 | 17 |
| 34 | 622 262 | 119 482 | 34 | 17 |
| 35 | 741 744 | 141 957 | 35 | 18 |
| 36 | 883 701 | 168 658 | 36 | 18 |
| 37 | 1 052 359 | 200 383 | 37 | 19 |
| 38 | 1 252 742 | 238 076 | 38 | 19 |
| 39 | 1 490 818 | 282 857 | 39 | 20 |
| 40 | 1 773 675 | 336 063 | 40 | 20 |
| 41 | 2 109 738 | 399 277 | 41 | 21 |
| 42 | 2 509 015 | 474 380 | 42 | 21 |
| 43 | 2 983 395 | 563 611 | 43 | 22 |
| 44 | 3 547 006 | 669 626 | 44 | 22 |
| 45 | 4 216 632 | 795 583 | 45 | 23 |
| 46 | 5 012 215 | 945 233 | 46 | 23 |
| 47 | 5 957 448 | 1 123 030 | 47 | 24 |
| 48 | 7 080 478 | 1 334 273 | 48 | 24 |
| 49 | 8 414 751 | 1 585 249 | 49 | 25 |
| 50 | 10 000 000 | 1 585 249 | 50 | 25 |

Au-delà du niveau 50 : chaque niveau coûte **1 585 249 XP** et ne donne plus de point.

## Pièges fréquents

- **Réclamez vos quêtes** : une quête terminée ne verse son XP qu'une fois réclamée.
- **Stocker ne fait pas monter** : des ressources accumulées, pillées ou recyclées ne rapportent de l'XP qu'une fois investies.
- **Reconstruire après une défaite ne rapporte rien** : il faut d'abord dépasser votre ancien record. Une flotte perdue repousse donc votre prochaine XP « militaire ».
- **Démolir ne retire pas d'XP**, mais les niveaux reconstruits ensuite ne rapportent rien tant que vous n'avez pas dépassé votre record.
- **Changer de classe tard** : la nouvelle classe repart de sa propre maîtrise. Vos points de l'arbre commun, eux, ne bougent pas.
- **Chaque univers a sa propre XP** : jouer dans un autre univers ne fait pas monter votre niveau ici.

## Pages liées

- [Les talents](/fr/dynasty/talents)
- [Les classes](/fr/dynasty/classes)
- [Le didacticiel](/fr/getting-started/tutorial-quests)
- [Classements et points](/fr/players/rankings)
- [Les expéditions](/fr/fleet/expeditions)
