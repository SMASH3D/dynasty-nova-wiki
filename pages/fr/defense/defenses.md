---
wiki_id: 40
locale: "fr"
path: "defense/defenses"
url: "https://wiki.dynastynova.com/fr/defense/defenses"
title: "Liste des défenses"
description: "Les défenses : coûts, statistiques, prérequis."
tags: ["defense", "défenses"]
published: true
created: "2026-10-02T13:09:02.050Z"
updated: "2026-10-02T17:40:06.227Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des défenses

> **En bref** : les défenses protègent votre planète en permanence. Elles ne se déplacent pas, ne peuvent pas être pillées et prennent part à chaque combat livré sur leur planète. Le jeu en compte 8, dont deux uniques (Barrière défensive et Dôme protecteur). Les missiles se construisent au même endroit mais ne combattent pas : voir [Missiles](/fr/defense/missiles).
{.is-info}

> **Paramètre d'univers** : la part des défenses détruites qui part en champ de ruines peut être différente selon l'univers.
> Par défaut : **0 %** · Redline : **0 %**
{.is-info}

> **Paramètre d'univers** : la vitesse de chantier divise la durée de construction des défenses.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

### Construction
1. Les défenses se construisent au **Dock orbital**, sur une planète ou sur une lune qui en possède un.
2. Pendant l'agrandissement du Dock orbital, **aucune commande** de défense n'est acceptée.
3. Les défenses ont **leur propre file**, distincte de celle des vaisseaux : les deux avancent en même temps. La file accepte **2 commandes** (**5** avec le Premium), celle en cours comprise (voir [Files de construction](/fr/economy/build-queue)).
4. À la commande, la planète doit avoir les ressources de **toute la quantité**. Chaque unité est ensuite payée au moment où elle entre en production ; si l'unité suivante ne peut plus être payée, la commande s'arrête là.
5. Commander une défense déjà en attente dans la file l'ajoute à cette commande, sans prendre de place supplémentaire.
6. **Durée d'une unité**, en secondes, jamais moins d'une seconde :
$$t = \frac{T}{(1 + D) \times 2^{A}} \div v$$
   - $T$ : durée de base de la défense (tableau ci-dessous) ; $D$ : niveau du Dock orbital ; $A$ : niveau de l'Assembleur moléculaire ; $v$ : vitesse de chantier de l'univers.
   - Les bonus de vitesse de chantier (talents de dynastie, alliance) divisent ensuite cette durée.

### En combat
7. Chaque défense tire **une fois par round** et ne combat que là où elle est construite (planète ou lune).
8. Attaque, bouclier et structure augmentent de **10 % par niveau** de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. En combat, la **coque** vaut la structure divisée par 10.
9. Les défenses n'ont **aucun tir rapide**. Certains vaisseaux en ont contre elles (tableau ci-dessous).
10. Après un combat, une partie des défenses détruites est reconstruite gratuitement : voir [Reconstruction des défenses](/fr/combat/defense-rebuild). Une défense détruite par un missile est perdue (voir [Missiles](/fr/defense/missiles)).
11. Les défenses détruites ne laissent **aucun champ de ruines**, sauf réglage contraire de l'univers.

### Unicité et points
12. **Barrière défensive et Dôme protecteur** : un seul exemplaire de chacun par planète. Impossible d'en commander plus d'un à la fois, ni d'en commander un tant qu'il en existe un sur la planète ou dans la file.
13. **Points** : chaque défense rapporte 1 point par tranche de 1 000 ressources de son coût (métal, cristal et hydrogène), comptés dans les points militaires.

## Exemple chiffré

**Commander 20 Projecteurs balistiques avec un Dock orbital niveau 4** (Assembleur moléculaire 0, vitesse ×1)
- Coût : 20 × 2 000 = **40 000 métal**, à avoir sur la planète au moment de la commande ; **40 points** militaires une fois construits.
- Une unité : 2 880 / (1 + 4) = **576 secondes**.
- La commande entière : 20 × 576 = 11 520 secondes, soit **3 h 12 min**.

**Une Batterie ionique en combat** avec Systèmes Offensifs 5, Champs de Protection 4 et Métallurgie Avancée 6
- Attaque : 150 × 1,5 = **225**.
- Bouclier : 500 × 1,4 = **700**.
- Coque : 8 000 × 1,6 / 10 = **1 280**.

## Données détaillées

### Coûts et statistiques de base (sans recherche)

| Défense | Métal | Cristal | Hydrogène | Points | Structure | Coque en combat | Bouclier | Attaque | Durée de base |
|---|---|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/defense/projecteur-balistique.jpg" width="48" alt="Projecteur balistique"> Projecteur balistique | 2 000 | 0 | 0 | 2 | 2 000 | 200 | 20 | 80 | 48 min |
| <img src="/images/illustrations/defense/canon-photonique.jpg" width="48" alt="Canon photonique"> Canon photonique | 1 500 | 500 | 0 | 2 | 2 000 | 200 | 25 | 100 | 48 min |
| <img src="/images/illustrations/defense/emetteur-a-haute-energie.jpg" width="48" alt="Émetteur à haute énergie"> Émetteur à haute énergie | 6 000 | 2 000 | 0 | 8 | 8 000 | 800 | 100 | 250 | 3 h 12 min |
| <img src="/images/illustrations/defense/batterie-ionique.jpg" width="48" alt="Batterie ionique"> Batterie ionique | 2 000 | 6 000 | 0 | 8 | 8 000 | 800 | 500 | 150 | 3 h 12 min |
| <img src="/images/illustrations/defense/accelerateur-magnetique.jpg" width="48" alt="Accélérateur magnétique"> Accélérateur magnétique | 20 000 | 15 000 | 2 000 | 37 | 35 000 | 3 500 | 200 | 1 100 | 14 h |
| <img src="/images/illustrations/defense/ejecteur-a-plasma.jpg" width="48" alt="Éjecteur à plasma"> Éjecteur à plasma | 50 000 | 50 000 | 30 000 | 130 | 100 000 | 10 000 | 300 | 3 000 | 1 j 4 h |
| <img src="/images/illustrations/defense/barriere-defensive.jpg" width="48" alt="Barrière défensive"> Barrière défensive | 10 000 | 10 000 | 0 | 20 | 20 000 | 2 000 | 2 000 | 1 | 8 h |
| <img src="/images/illustrations/defense/dome-protecteur.jpg" width="48" alt="Dôme protecteur"> Dôme protecteur | 50 000 | 50 000 | 0 | 100 | 100 000 | 10 000 | 10 000 | 1 | 1 j 16 h |

La durée de base est celle d'une unité avec un Dock orbital niveau 0 ; le Dock la divise ensuite (règle 6).

### Prérequis

| Défense | Prérequis | Exemplaires par planète |
|---|---|---|
| Projecteur balistique | Dock orbital 1 | illimité |
| Canon photonique | Dock orbital 2, Systèmes Photoniques 3 | illimité |
| Émetteur à haute énergie | Dock orbital 4, Systèmes Photoniques 6, Science Énergétique 3 | illimité |
| Batterie ionique | Dock orbital 4, Manipulation Ionique 4 | illimité |
| Accélérateur magnétique | Dock orbital 6, Systèmes Offensifs 3, Champs de Protection 1, Science Énergétique 6 | illimité |
| Éjecteur à plasma | Dock orbital 8, Maîtrise du Plasma 7 | illimité |
| Barrière défensive | Dock orbital 1, Champs de Protection 2 | 1 |
| Dôme protecteur | Dock orbital 6, Champs de Protection 6 | 1 |

### Durée d'une unité selon le Dock orbital

Assembleur moléculaire 0, vitesse de chantier ×1, sans bonus. « non » : niveau de Dock insuffisant.

| Défense | Dock 2 | Dock 4 | Dock 6 | Dock 8 | Dock 10 | Dock 12 |
|---|---|---|---|---|---|---|
| Projecteur balistique | 16 min | 9 min 36 s | 6 min 51 s | 5 min 20 s | 4 min 22 s | 3 min 42 s |
| Canon photonique | 16 min | 9 min 36 s | 6 min 51 s | 5 min 20 s | 4 min 22 s | 3 min 42 s |
| Émetteur à haute énergie | non | 38 min 24 s | 27 min 26 s | 21 min 20 s | 17 min 27 s | 14 min 46 s |
| Batterie ionique | non | 38 min 24 s | 27 min 26 s | 21 min 20 s | 17 min 27 s | 14 min 46 s |
| Accélérateur magnétique | non | non | 2 h | 1 h 33 min 20 s | 1 h 16 min 22 s | 1 h 4 min 37 s |
| Éjecteur à plasma | non | non | non | 3 h 6 min 40 s | 2 h 32 min 44 s | 2 h 9 min 14 s |
| Barrière défensive | 2 h 40 min | 1 h 36 min | 1 h 8 min 34 s | 53 min 20 s | 43 min 38 s | 36 min 55 s |
| Dôme protecteur | non | non | 5 h 42 min 51 s | 4 h 26 min 40 s | 3 h 38 min 11 s | 3 h 4 min 37 s |

Chaque niveau d'Assembleur moléculaire divise encore ces durées par deux.

### Vaisseaux qui ont un tir rapide contre les défenses

| Défense | Tirs rapides subis |
|---|---|
| Projecteur balistique | Frappe-orbital 20, Corvette 10, Colossus stellaire 200 |
| Canon photonique | Frappe-orbital 20, Annihilateur 10, Colossus stellaire 200 |
| Émetteur à haute énergie | Frappe-orbital 10, Colossus stellaire 100 |
| Batterie ionique | Frappe-orbital 10, Colossus stellaire 100 |
| Accélérateur magnétique | Frappe-orbital 5, Colossus stellaire 50 |
| Éjecteur à plasma | Frappe-orbital 5 |
| Barrière défensive | aucun |
| Dôme protecteur | aucun |

## Pièges fréquents

- **Le Dock orbital bloque les commandes pendant son agrandissement** : lancez vos défenses avant de l'agrandir.
- **Une grosse commande peut s'arrêter en route** : chaque unité est payée à son tour. Si vous dépensez les ressources ailleurs entre-temps, la commande s'arrête à la dernière unité payée.
- **Le Frappe-orbital est l'ennemi des défenses** : il a un tir rapide contre presque toutes. Face à lui, l'Éjecteur à plasma et les deux boucliers résistent le mieux.
- **Les défenses ne rapportent rien à l'attaquant** : elles ne laissent pas de champ de ruines par défaut. Une planète très défendue coûte cher à attaquer sans rien rendre en débris.

## Pages liées

- [Missiles](/fr/defense/missiles)
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Tirs rapides](/fr/fleet/rapid-fire)
- [Files de construction](/fr/economy/build-queue)
