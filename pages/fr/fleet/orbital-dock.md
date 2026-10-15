---
wiki_id: 34
locale: "fr"
path: "fleet/orbital-dock"
url: "https://wiki.dynastynova.com/fr/fleet/orbital-dock"
title: "Dock orbital (chantier)"
description: "Construire vaisseaux et défenses : files, paiement, livraison, durées."
tags: ["fleet"]
published: true
created: "2026-10-02T13:08:50.428Z"
updated: "2026-10-15T19:28:18.335Z"
---

# Dock orbital (chantier)

> **En bref** : le Dock orbital construit les vaisseaux et les défenses. Chaque niveau accélère la production, l'Assembleur moléculaire la divise par deux à chaque niveau. Une commande est vérifiée en entier quand vous la passez, puis chaque unité est payée au moment où elle entre en production et livrée dès qu'elle est terminée.
{.is-info}

> **Paramètre d'univers** : la vitesse de chantier divise la durée de construction des vaisseaux et des défenses.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

> **Paramètre d'univers** : la taille des files de construction peut être différente selon l'univers.
> Par défaut : **2 ordres**, **5 en Premium** · Redline : **2 ordres**, **5 en Premium**
{.is-info}

<img src="/images/illustrations/facilities/dock-orbital.jpg" width="180" alt="Dock orbital">

## Règles

### Le bâtiment
1. Le Dock orbital se construit sur une planète **ou une lune**. Prérequis : Fabrique d'automates 2. Niveau maximum : **12**. Il faut au moins le niveau 1 pour commander un vaisseau ou une défense, en plus des prérequis propres à chaque unité.
2. Sur une lune, le Dock travaille sans Assembleur moléculaire, qui ne se construit que sur une planète.

### Les files
3. Chaque base a **une file de vaisseaux et une file de défenses**, qui avancent **en parallèle**. Chacune accepte 2 ordres (5 en Premium), celui en cours compris (voir [Files de construction](/fr/economy/build-queue)).
4. Commander le même vaisseau ou la même défense que le **dernier ordre en attente** l'ajoute à cet ordre, sans prendre de place dans la file. La Barrière défensive et le Dôme protecteur, uniques, ne se fusionnent jamais.
5. Une commande compte au moins 1 unité et au plus **1 000 000**.

### Paiement et livraison
6. Une commande n'est acceptée que si la base peut la **payer en entier** au moment où vous la passez.
7. Chaque unité est ensuite **payée au moment où elle entre en production**, pas avant. Si la première ne peut pas être payée au lancement, l'ordre est abandonné sans frais.
8. Les unités sont **livrées une par une**, chacune dès qu'elle est terminée, et rapportent aussitôt leurs points militaires.
9. Après chaque livraison, l'unité suivante est payée. Si la base ne peut plus la payer, la commande **s'arrête là** : les unités déjà livrées sont gardées, les autres ne coûtent rien.
10. **Durée d'une unité**, en secondes, jamais moins d'une seconde :

$$t = \frac{T}{(1 + D) \times 2^{A}} \div v$$

- $t$ : durée de construction d'une unité, arrondie à la seconde ;
- $T$ : durée de base de l'unité (table plus bas, et [Liste des défenses](/fr/defense/defenses)) ;
- $D$ : niveau du Dock orbital de la base ;
- $A$ : niveau de l'Assembleur moléculaire de la base ;
- $v$ : vitesse de chantier de l'univers.

Les bonus de vitesse des talents divisent ensuite cette durée, comme pour les bâtiments (voir [Formules de l'économie](/fr/economy/formulas)). La durée d'une unité est fixée quand la commande démarre ; la commande dure cette durée × le nombre d'unités.

### Annuler
11. Annuler un ordre **en attente** ne coûte rien et ne rend rien.
12. Annuler une commande **en cours** rend **80 %** de l'unité payée mais pas encore livrée ; les unités livrées sont gardées, les suivantes ne coûtent rien. Des talents montent ce taux, jusqu'à 95 %.
13. Vous pouvez aussi demander d'**arrêter après l'unité en cours** : elle se termine normalement, le reste de la commande est abandonné sans frais.

### Pendant les travaux
14. Tant que le Dock a une commande de vaisseaux ou de défenses, en attente ou en cours, il ne peut être **ni amélioré ni démoli**.
15. Pendant que le Dock est en travaux, aucun vaisseau ni aucune défense ne peut y être commandé. Les autres bâtiments se construisent normalement.

## Exemple chiffré

**Une Navette de fret** (durée de base 5 400 s) :
- Dock orbital 4, sans Assembleur : 5 400 / 5 = **1 080 s** (18 min).
- Dock orbital 7 et Assembleur moléculaire 1 : 5 400 / (8 × 2) = 337,5, arrondi à **338 s**. Dix Navettes : 3 380 s (56 min 20 s).

**Annulation** : vous commandez 10 Navettes de fret et annulez après la 3e livraison. La 4e est en production et payée : vous récupérez 80 % de son coût, soit **1 600 métal et 1 600 cristal**. Les 3 Navettes livrées restent, les 6 suivantes n'ont rien coûté.

## Données détaillées

### Durée d'un vaisseau selon le Dock orbital (en secondes, vitesse ×1, sans talent)

| Vaisseau | Durée de base (s) | Dock 4 | Dock 8 | Dock 12 | Dock 12 et Assembleur 2 |
|---|---|---|---|---|---|
| Navette de fret | 5 400 | 1 080 | 600 | 415 | 104 |
| Cargo stellaire | 14 400 | 2 880 | 1 600 | 1 108 | 277 |
| Pionnier spatial | 100 800 | 20 160 | 11 200 | 7 754 | 1 938 |
| Récupérateur | 25 200 | 5 040 | 2 800 | 1 938 | 485 |
| Éclaireur | 600 | 120 | 67 | 46 | 12 |
| Collecteur solaire | 2 880 | 576 | 320 | 222 | 55 |
| Intercepteur | 1 800 | 360 | 200 | 138 | 35 |
| Assaillant | 5 400 | 1 080 | 600 | 415 | 104 |
| Corvette | 28 800 | 5 760 | 3 200 | 2 215 | 554 |
| Cuirassé | 64 800 | 12 960 | 7 200 | 4 985 | 1 246 |
| Frappe-orbital | 86 400 | 17 280 | 9 600 | 6 646 | 1 662 |
| Prédateur | 79 200 | 15 840 | 8 800 | 6 092 | 1 523 |
| Annihilateur | 115 200 | 23 040 | 12 800 | 8 862 | 2 215 |
| Colossus stellaire | 12 960 000 | 2 592 000 | 1 440 000 | 996 923 | 249 231 |

Le Dock orbital lui-même : coût du niveau 1 de 400 métal, 200 cristal et 100 hydrogène, doublé à chaque niveau (voir [Liste des bâtiments](/fr/economy/buildings)).

## Pièges fréquents

- **Gardez les ressources pour la suite** : une commande longue s'arrête dès qu'une unité ne peut plus être payée.
- **Les files ne se partagent pas** : vaisseaux et défenses avancent en même temps, mais chaque file est limitée à 2 ordres (5 en Premium).
- **Ne lancez pas l'amélioration du Dock en pleine production** : elle est refusée tant qu'une commande attend ou tourne.
- **Une lune construit plus lentement** : pas d'Assembleur moléculaire sur une lune.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Files de construction](/fr/economy/build-queue)
- [Formules de l'économie](/fr/economy/formulas)
- [Station de réparation](/fr/economy/repair-station)
- [Liste des bâtiments](/fr/economy/buildings)
