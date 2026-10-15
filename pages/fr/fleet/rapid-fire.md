---
wiki_id: 33
locale: "fr"
path: "fleet/rapid-fire"
url: "https://wiki.dynastynova.com/fr/fleet/rapid-fire"
title: "Tirs rapides"
description: "Quelles unités tirent plusieurs fois sur quelles cibles."
tags: ["fleet", "combat"]
published: true
created: "2026-10-02T13:08:48.505Z"
updated: "2026-10-02T16:36:31.430Z"
---

# Tirs rapides

> **En bref** : certains vaisseaux ont un **tir rapide** contre certaines unités. Après chaque tir sur l'une d'elles, ils ont une chance de tirer à nouveau dans le même round, sur une nouvelle cible tirée au hasard. Le facteur affiché est le nombre moyen de tirs enchaînés contre ce type d'unité. Les défenses n'ont pas de tir rapide.
{.is-info}

## Règles

1. À chaque round, chaque unité tire au moins une fois (une fois par tir de base) sur une unité adverse **tirée au hasard** parmi celles encore en vie. Le tir rapide ne guide jamais le tir vers les unités qu'il contre.
2. Après chaque tir, touché ou manqué, si le tireur a un tir rapide de facteur $f$ contre l'unité qu'il vient de viser, il tire à nouveau avec la probabilité $(f - 1) / f$, sur une **nouvelle cible tirée au hasard**.
3. La chaîne continue tant que le tirage réussit **et** que la dernière cible visée fait partie de ses tirs rapides. Dès qu'elle tombe sur une unité qui n'en fait pas partie, elle s'arrête après ce tir.
4. Contre une flotte composée uniquement de la cible, le tireur tire donc $f$ fois en moyenne par round.
5. Un tir enchaîné suit les règles d'un tir normal : un tir inférieur à 1 % du bouclier de la cible rebondit.
6. Certains talents renforcent les tirs rapides (voir [Les talents](/fr/dynasty/talents)) : le tableau ci-dessous donne les facteurs de base.

## Exemple chiffré

Une Corvette a un tir rapide de **6** contre l'Intercepteur.
- Après un tir sur un Intercepteur, elle retire avec une probabilité de 5 / 6 = **83,3 %**.
- Face à une flotte composée uniquement d'Intercepteurs, elle tire **6 fois en moyenne** par round, au lieu d'une.
- Face à une flotte moitié Intercepteurs, moitié Cuirassés, la chaîne s'arrête dès qu'elle tombe sur un Cuirassé : elle tire nettement moins.

## Données détaillées

### Qui tire rapidement sur qui

| Tireur | Cibles (facteur) |
|---|---|
| Navette de fret | Éclaireur 5, Collecteur solaire 5 |
| Cargo stellaire | Éclaireur 5, Collecteur solaire 5 |
| Pionnier spatial | Éclaireur 5, Collecteur solaire 5 |
| Récupérateur | Éclaireur 5, Collecteur solaire 5 |
| Intercepteur | Éclaireur 5, Collecteur solaire 5 |
| Assaillant | Éclaireur 5, Collecteur solaire 5, Navette de fret 3 |
| Corvette | Projecteur balistique 10, Intercepteur 6, Éclaireur 5, Collecteur solaire 5 |
| Cuirassé | Éclaireur 5, Collecteur solaire 5 |
| Frappe-orbital | Projecteur balistique 20, Canon photonique 20, Émetteur à haute énergie 10, Batterie ionique 10, Accélérateur magnétique 5, Éjecteur à plasma 5, Éclaireur 5, Collecteur solaire 5 |
| Prédateur | Cuirassé 7, Éclaireur 5, Collecteur solaire 5, Corvette 4, Assaillant 4, Cargo stellaire 3, Navette de fret 3 |
| Annihilateur | Canon photonique 10, Éclaireur 5, Collecteur solaire 5, Prédateur 2 |
| Colossus stellaire | Collecteur solaire 1 250, Éclaireur 1 250, Navette de fret 250, Pionnier spatial 250, Cargo stellaire 250, Récupérateur 250, Projecteur balistique 200, Intercepteur 200, Canon photonique 200, Assaillant 100, Émetteur à haute énergie 100, Batterie ionique 100, Accélérateur magnétique 50, Corvette 33, Cuirassé 30, Frappe-orbital 25, Prédateur 15, Annihilateur 5 |
| Éclaireur, Collecteur solaire | aucun |
| Toutes les défenses | aucun |

### Qui est visé par quoi

| Cible | Vaisseaux qui ont un tir rapide contre elle |
|---|---|
| Navette de fret | Colossus stellaire 250, Assaillant 3, Prédateur 3 |
| Cargo stellaire | Colossus stellaire 250, Prédateur 3 |
| Pionnier spatial | Colossus stellaire 250 |
| Récupérateur | Colossus stellaire 250 |
| Éclaireur | Colossus stellaire 1 250, Cuirassé 5, Frappe-orbital 5, Pionnier spatial 5, Corvette 5, Annihilateur 5, Assaillant 5, Cargo stellaire 5, Intercepteur 5, Prédateur 5, Récupérateur 5, Navette de fret 5 |
| Collecteur solaire | Colossus stellaire 1 250, Cuirassé 5, Frappe-orbital 5, Pionnier spatial 5, Corvette 5, Annihilateur 5, Assaillant 5, Cargo stellaire 5, Intercepteur 5, Prédateur 5, Récupérateur 5, Navette de fret 5 |
| Intercepteur | Colossus stellaire 200, Corvette 6 |
| Assaillant | Colossus stellaire 100, Prédateur 4 |
| Corvette | Colossus stellaire 33, Prédateur 4 |
| Cuirassé | Colossus stellaire 30, Prédateur 7 |
| Frappe-orbital | Colossus stellaire 25 |
| Prédateur | Colossus stellaire 15, Annihilateur 2 |
| Annihilateur | Colossus stellaire 5 |
| Colossus stellaire | personne |
| Projecteur balistique | Colossus stellaire 200, Frappe-orbital 20, Corvette 10 |
| Canon photonique | Colossus stellaire 200, Frappe-orbital 20, Annihilateur 10 |
| Émetteur à haute énergie | Colossus stellaire 100, Frappe-orbital 10 |
| Accélérateur magnétique | Colossus stellaire 50, Frappe-orbital 5 |
| Batterie ionique | Colossus stellaire 100, Frappe-orbital 10 |
| Éjecteur à plasma | Frappe-orbital 5 |
| Barrière défensive | personne |
| Dôme protecteur | personne |

## Pièges fréquents

- **Les Éclaireurs et Collecteurs relancent les tirs adverses** : presque tous les vaisseaux ont un tir rapide de 5 contre eux. Laisser beaucoup d'Éclaireurs ou de Collecteurs en orbite pendant une attaque donne à l'attaquant des tirs supplémentaires.
- **Les tirs rapides ne garantissent rien** : la cible suivante est tirée au hasard. Dans une flotte variée, les chaînes sont plus courtes que le facteur affiché.
- **Le Colossus stellaire n'est visé par aucun tir rapide** : il ne peut être abattu qu'à la force des tirs normaux.
- **Un tir rapide ne contourne pas la règle du 1 %** : un tir trop faible contre un gros bouclier rebondit, même s'il fait partie d'une chaîne.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Simulateur de combat](/fr/combat/simulator)
