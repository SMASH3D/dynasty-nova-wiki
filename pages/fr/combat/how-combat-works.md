---
wiki_id: 44
locale: "fr"
path: "combat/how-combat-works"
url: "https://wiki.dynastynova.com/fr/combat/how-combat-works"
title: "Déroulement d'un combat"
description: "Rounds, tirs, boucliers, explosions et résultat."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:10.079Z"
updated: "2026-10-02T16:36:45.627Z"
---

# Déroulement d'un combat

> **En bref** : un combat dure au plus 6 rounds. À chaque round, les boucliers se rechargent, l'attaquant tire, puis le défenseur. Chaque tir vise une unité adverse au hasard et touche toujours. Un tir trop faible rebondit sur les boucliers ; les dégâts de coque, eux, restent d'un round à l'autre et peuvent faire exploser l'unité touchée.
{.is-info}

## Règles

### Statistiques de combat
1. Chaque unité combat avec trois valeurs : **attaque**, **bouclier** et **coque**. Elles partent des statistiques du catalogue ([vaisseaux](/fr/fleet/ships), [défenses](/fr/defense/defenses)) et montent avec trois recherches, de **10 % par niveau** : Systèmes Offensifs pour l'attaque, Champs de Protection pour le bouclier, Métallurgie Avancée pour la coque.
2. La **coque de combat** vaut le dixième de la structure.
3. Les talents d'alliance **Doctrine d'armement** et **Doctrine de protection** ajoutent chacun **5 %** : le premier à l'attaque, le second au bouclier et à la coque. Ils s'appliquent après la recherche, à partir de la fin de la période d'intégration du membre.
4. Les talents de [dynastie et de classe](/fr/dynasty/talents) peuvent ajouter leurs propres pourcentages. Ils s'additionnent à la Doctrine et le total est appliqué en une fois.

$$A = \mathrm{arr}\left(A_0 (1 + 0{,}1\,W)\right) \times \left(1 + \frac{b_A}{100}\right) \qquad B = \mathrm{arr}\left(B_0 (1 + 0{,}1\,S)\right) \times \left(1 + \frac{b_P}{100}\right) \qquad C = \frac{\mathrm{arr}\left(T (1 + 0{,}1\,M)\right)}{10} \times \left(1 + \frac{b_P}{100}\right)$$

- $A$, $B$, $C$ : attaque, bouclier et coque de combat ; $A_0$, $B_0$ : attaque et bouclier du catalogue ; $T$ : structure du catalogue.
- $W$, $S$, $M$ : niveaux de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée.
- $b_A$ : Doctrine d'armement plus talents d'attaque, en % ; $b_P$ : Doctrine de protection plus talents de bouclier ou de coque, en %.
- $\mathrm{arr}$ : arrondi à l'entier le plus proche. La coque est arrondie à l'entier ; le dernier produit est arrondi à l'inférieur.

### Déroulement d'un round
5. Un combat compte **6 rounds au plus**. Il s'arrête dès qu'un camp n'a plus d'unité.
6. Au début de chaque round, **tous les boucliers se rechargent** entièrement. La **coque ne se répare pas** : les dégâts reçus au round précédent restent.
7. **L'attaquant tire, puis le défenseur.** Chaque unité vivante au début du round tire, même si elle est détruite pendant le round : en pratique, les tirs sont simultanés.
8. Chaque unité tire **un coup par round**, sur une **unité adverse tirée au hasard** parmi les unités encore vivantes, toutes catégories confondues. **Tout tir touche.**

### Tirs rapides
9. Après chaque tir, si le tireur a un [tir rapide](/fr/fleet/rapid-fire) de facteur $f$ contre l'unité qu'il vient de viser, il tire à nouveau avec une chance de $(f - 1) / f$, sur une **nouvelle cible tirée au hasard**. Il continue tant que le tirage réussit.
10. Le tir rapide donne donc des tirs en plus, il ne guide pas le tir vers les unités contrées. Contre des cibles toutes du même type, un facteur $f$ donne en moyenne $f$ tirs.
11. Dans le catalogue, seuls des vaisseaux ont des tirs rapides. Les défenses tirent une fois par round.

### Dégâts
12. **Règle du 1 %** : un tir dont les dégâts sont inférieurs à **1 % du bouclier maximal** de la cible **rebondit** sans aucun effet.
13. Sinon, le **bouclier absorbe** les dégâts tant qu'il en reste, et l'excédent passe entièrement sur la **coque**. À zéro de coque, l'unité est détruite.
14. **Explosion** : après chaque tir qui n'a pas rebondi, si la coque de la cible est **sous 70 %** de sa coque de combat, elle explose avec une chance égale à **1 − part de coque restante**. Un tir absorbé par le bouclier ouvre aussi ce tirage, puisque la coque était déjà entamée ; un tir qui rebondit, jamais.

### Résultat
15. **Victoire de l'attaquant** si le défenseur n'a plus d'unité ; **victoire du défenseur** si l'attaquant n'a plus d'unité ; sinon **match nul** : les deux camps encore debout après 6 rounds, ou les deux détruits.
16. Une unité qui survit au combat **repart intacte** : les dégâts de coque ne durent que le temps du combat.
17. Les missiles du silo ne combattent pas : ce sont des munitions, tirées par une autre mission.
18. Ensuite viennent le [pillage](/fr/combat/plunder) (victoire seulement), le [champ de ruines](/fr/combat/debris) et la chance de lune, la [reconstruction des défenses](/fr/combat/defense-rebuild) et la [Station de réparation](/fr/economy/repair-station).

### Le hasard
19. Le hasard d'un combat (cibles, tirs rapides, explosions) est fixé à l'arrivée de la flotte : rejoué, le même combat donne exactement le même résultat, tir pour tir. Les tirages qui suivent (reconstruction des défenses, lune) sont eux aussi fixés par ce combat.

## Exemple chiffré

**Un Cuirassé sans recherche** : attaque 1 000, bouclier 200, coque de combat 60 000 / 10 = **6 000**.

**Le même Cuirassé avec Systèmes Offensifs, Champs de Protection et Métallurgie Avancée au niveau 10, et les deux Doctrines** :
- Attaque : 1 000 × 2 = 2 000, puis × 1,05 = **2 100**.
- Bouclier : 200 × 2 = 400, puis × 1,05 = **420**.
- Coque : 60 000 × 2 / 10 = 12 000, puis × 1,05 = **12 600**.

**Ce Cuirassé sans recherche tire sur un Intercepteur sans recherche** (bouclier 10, coque 400) : le bouclier absorbe 10, la coque prend 990. L'Intercepteur est **détruit**.

**4 Intercepteurs tirent sur ce Cuirassé** (attaque 50) :
- Seuil du 1 % : 2. Les tirs passent.
- Les 4 tirs (200 au total) vident le bouclier (200), **sans toucher la coque**. Au round suivant, le bouclier est de nouveau plein.

**Un Intercepteur tire sur un Dôme protecteur** (bouclier 10 000) : seuil du 1 % à 100, le tir de 50 **rebondit**. Les Intercepteurs ne peuvent rien contre le Dôme, quel que soit leur nombre.

**Une unité dont la coque est tombée à 60 %** : à chaque tir qui ne rebondit pas, elle explose avec une chance de 1 − 0,60 = **40 %**.

**Un Colossus stellaire contre une flotte d'Intercepteurs** : son tir rapide de 200 lui donne en moyenne 200 tirs par round.

## Données détaillées

Statistiques de combat sans recherche ni bonus. Chaque niveau de recherche ajoute 10 % de la valeur de base.

| Unité | Attaque | Bouclier | Coque de combat | Tir qui rebondit en dessous de |
|---|---|---|---|---|
| Navette de fret | 5 | 10 | 400 | 0,1 |
| Cargo stellaire | 5 | 25 | 1 200 | 0,25 |
| Pionnier spatial | 50 | 100 | 3 000 | 1 |
| Récupérateur | 1 | 10 | 1 600 | 0,1 |
| Éclaireur | 0 | 0 | 100 | 0 |
| Collecteur solaire | 1 | 1 | 200 | 0,01 |
| Intercepteur | 50 | 10 | 400 | 0,1 |
| Assaillant | 150 | 25 | 1 000 | 0,25 |
| Corvette | 400 | 50 | 2 700 | 0,5 |
| Cuirassé | 1 000 | 200 | 6 000 | 2 |
| Frappe-orbital | 1 000 | 500 | 7 500 | 5 |
| Prédateur | 700 | 400 | 7 000 | 4 |
| Annihilateur | 2 000 | 500 | 11 000 | 5 |
| Colossus stellaire | 200 000 | 50 000 | 900 000 | 500 |
| Projecteur balistique | 80 | 20 | 200 | 0,2 |
| Canon photonique | 100 | 25 | 200 | 0,25 |
| Émetteur à haute énergie | 250 | 100 | 800 | 1 |
| Batterie ionique | 150 | 500 | 800 | 5 |
| Accélérateur magnétique | 1 100 | 200 | 3 500 | 2 |
| Éjecteur à plasma | 3 000 | 300 | 10 000 | 3 |
| Barrière défensive | 1 | 2 000 | 2 000 | 20 |
| Dôme protecteur | 1 | 10 000 | 10 000 | 100 |

## Pièges fréquents

- **Les petits tirs s'écrasent sur les boucliers** : des unités faibles, même nombreuses, peuvent ne jamais entamer une grosse cible, puisque son bouclier se recharge à chaque round.
- **La cible est aléatoire** : vous ne choisissez pas ce que vos vaisseaux visent. Les unités nombreuses et bon marché absorbent beaucoup de tirs.
- **6 rounds, pas plus** : si personne n'est éliminé, c'est un match nul et l'attaquant ne pille rien.
- **Les blessures comptent** : une unité entamée explose plus facilement aux rounds suivants. Une rafale de petits tirs peut achever une cible déjà touchée.

## Pages liées

- [Tirs rapides](/fr/fleet/rapid-fire)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Pillage](/fr/combat/plunder)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Simulateur de combat](/fr/combat/simulator)
