---
wiki_id: 153
locale: "fr"
path: "dynasty/classes/builder"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/builder"
title: "Le Bâtisseur"
description: "Arbre de classe du Bâtisseur : Filon, Chantier, Fonderie."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:40.591Z"
updated: "2026-10-15T18:57:21.610Z"
---

# Le Bâtisseur

> **En bref** : le Bâtisseur est la classe de l'économie de chantier. Ses mines rapportent plus que leur niveau, son chantier avance pendant que ses files sont vides, et chaque niveau qu'il connaît déjà lui coûte moins cher. Filon fait produire les mines ; Chantier met de côté le temps perdu ; Fonderie réduit les prix et protège ce qui attend dans la file.
{.is-info}

## Règles

1. Le Bâtisseur est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Filon, Chantier et Fonderie.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. Les bonus génériques (production des mines, vitesse de construction, entrepôts, Maîtrise du Plasma) viennent de l'[arbre commun](/fr/dynasty/common-tree). Le Bâtisseur n'a que des **mécaniques**, un accent de coût (Devis serré, 5 % sur les bâtiments, ou Achats groupés, 10 % sur les défenses) et un accent de vitesse de construction, Rattrapage, limité aux colonies qui rattrapent la planète mère.
5. Les niveaux en plus de Puits maître, Mines jumelles, Veine mère et Galeries ne valent que pour les trois mines (Excavateur minéral, Extracteur cristallin, Condensateur d'hydrogène) et seulement pour leur production : la mine consomme toujours l'énergie de son niveau réel. Chaque mine gagne 1 niveau de production par Puits maître ou Mines jumelles. La **mine du jour** de Prospection, tant que son jour court, en gagne 1 de plus par Veine mère, dès son premier niveau, et encore 1 par Galeries à partir du niveau 30 (25, 20 puis 15 aux rangs 1 à 3) : 3 niveaux au plus.
6. Première coulée, Prospection et Carottage se calculent sur la **production propre de la mine** : à son niveau de production (niveaux en plus compris), à son taux de fonctionnement et à la vitesse de l'univers, sans Maîtrise du Plasma ni aucun autre bonus en pourcentage. Prospection et Carottage s'ajoutent à la production de la planète et subissent comme elle un manque d'énergie ; le versement de Première coulée n'en dépend pas.
7. « Une fois par jour » veut dire 24 h après la dernière utilisation, pour tout votre empire (Carottage, Coup de collier). Commande d'État revient 7 jours après le paiement de l'ordre désigné.

## Exemple chiffré

Univers à vitesse 1. Un Excavateur minéral produit 30 × N × 1,1^N métal par heure et consomme 10 × N × 1,1^N d'énergie : 4 036 métal et 1 345 d'énergie au niveau 20, 4 662 métal et 1 554 d'énergie au niveau 21.

**Filon complet sur la planète mère (Puits maître, l'Excavateur étant la mine du jour)**
- L'Excavateur passe au niveau 21. Il produit comme un niveau 24 (21 + 1 par Puits maître + 1 par Veine mère + 1 par Galeries, seuil abaissé à 15) : 30 × 24 × 1,1^24 = **7 091 métal par heure**, pour l'énergie d'un niveau 21 (1 554). Le lendemain, s'il n'est plus la mine du jour, il produit comme un niveau 22 : 5 372.
- Première coulée et Grandes coulées (4 h) : 4 × 7 091 = **28 364 métal** versés à la fin du niveau.
- Prospection au rang 3 : 7 091 × 15 % = 1 063 (arrondi inférieur) de plus par heure, soit **25 512 métal** sur les 24 h, à pleine énergie.
- Carottage (production doublée) : 7 091 × 4 = **28 364 métal** de plus en 4 h, à pleine énergie.

**Galeries et Mines jumelles, sur une colonie**
- Avec Galeries au rang 3, son niveau en plus joue dès le niveau 15. Un Excavateur 15, mine du jour, produit comme un niveau 18 : **3 002 métal par heure** au lieu de 1 879, pour l'énergie d'un niveau 15 (626). Les autres jours, il produit comme un niveau 16 : 2 205.

**Fonderie : un niveau déjà connu**
- Excavateur 25 sur une colonie, niveau déjà atteint sur la planète mère : 1 010 046 métal et 252 511 cristal au prix du catalogue.
- Plans connus et Archives de chantier (25 %) plus Devis serré (5 %) : 30 % de moins, arrondi à l'unité supérieure, soit **707 033 métal** et **176 758 cristal**.
- Si cet Excavateur est la mine du jour et que vous avez Double filon : 45 % de moins, soit **555 526 métal** et **138 882 cristal**.
- Désigné pour Commande d'État : la moitié de ce prix déjà réduit, **353 517 métal** et **88 379 cristal**, 35 % du prix du catalogue. Les points se comptent toujours sur le prix du catalogue.

**Chantier : une nuit de 8 h, file de bâtiments vide**
- Avec Plans d'avance au rang 3 (80 %) et Relais automatique (5 h) : 8 h × 80 % = 6 h 24, ramenées au plafond, soit **5 h** versées d'office à l'ordre lancé au réveil.
- Avec Banque d'heures (8 h) : **6 h 24** gardées, à verser sur l'ordre en cours de votre choix.

**Rien ne déborde**
- Le hangar de cristal est plein et 10 000 cristal produits débordent. Le métal est choisi et son hangar a de la place : 10 000 × 1,5 × 50 % = **7 500 métal**. Si le cristal était la ressource choisie, ces 10 000 seraient perdus.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FONDERIE<br/>Payer moins, garder ce qu'on a mis de côté."]:::head
        B3R1{{"Plans connus<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Coup de maître<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Devis serré<br/>1 pt"]:::option
        B3R3B["② Achats groupés<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Archives de chantier<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Acompte<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Crédit de chantier<br/>1 pt"]:::option
        B3R6B["② Paiement en métal<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Coffre de chantier<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Plans d'alliance<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Commande d'État<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["CHANTIER<br/>Le chantier qui travaille pendant que vous dormez."]:::head
        B2R1{{"Le chantier ne dort pas<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Équipes de veille<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Coulée continue<br/>1 pt"]:::option
        B2R3B["② Fondations coulées<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Rattrapage<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Chantier spatial de nuit<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Banque d'heures<br/>1 pt"]:::option
        B2R6B["② Relais automatique<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Plans d'avance<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Avance partagée<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Coup de collier<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["FILON<br/>Des mines qui rapportent plus que leur niveau."]:::head
        B1R1{{"Première coulée<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Grandes coulées<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Puits maître<br/>1 pt"]:::option
        B1R3B["② Mines jumelles<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Prospection<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Veine mère<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Filon choisi<br/>1 pt"]:::option
        B1R6B["② Double filon<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Galeries<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Rien ne déborde<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Carottage<br/>ultime"]]:::ultimate
        B1R8 --- B1R9
    end
    classDef head fill:#111b2e,stroke:#2a3852,color:#e6ecf7,stroke-width:1px;
    classDef key fill:#1c1606,stroke:#f5c542,color:#fde9a8,stroke-width:2px;
    classDef rank fill:#0e1a30,stroke:#4f8cff,color:#e6ecf7,stroke-width:2px;
    classDef option fill:#101827,stroke:#46546e,color:#cfd8e6,stroke-width:1px;
    classDef gate fill:#241b06,stroke:#c99a2e,color:#f5c542,stroke-width:1px;
    classDef ultimate fill:#1a1630,stroke:#e2c068,color:#fff6d8,stroke-width:3px;
    linkStyle default stroke:#33415c,stroke-width:2px,fill:none;
    style B1 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
    style B2 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
    style B3 fill:#0b1322,stroke:#1e2a40,stroke-width:1px;
```

### Filon

*Des mines qui rapportent plus que leur niveau.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Première coulée** | clé | Quand une de vos mines monte de niveau, elle vous verse aussitôt 1 h de sa nouvelle production. |  |
| 2 | **Grandes coulées** | 3 rangs | Une mine qui monte de niveau vous verse 3 h de sa nouvelle production en plus. | 3 × 1 h |
| 3 | **A · Puits maître** | choix | Les mines de votre planète mère produisent comme si elles avaient 1 niveau de plus. | |
|  | **B · Mines jumelles** |  | Les mines de vos colonies produisent comme si elles avaient 1 niveau de plus. | |
| 4 | **Prospection** | 3 rangs | Chaque jour, une de vos mines tirée au sort produit 15 % de plus pendant 24 h. | 3 × 5 % |
| 5 | **Veine mère** | clé | La mine du jour produit comme si elle avait 1 niveau de plus, dès son premier niveau, en plus de Puits maître ou de Mines jumelles. |  |
| 6 | **A · Filon choisi** | choix | Chaque jour, vous choisissez la mine de Prospection au lieu du tirage. | |
|  | **B · Double filon** |  | Tant que son jour court, améliorer la mine du jour coûte 15 % de moins. | |
| 7 | **Galeries** | 3 rangs | La mine du jour produit comme si elle avait 1 niveau de plus encore à partir du niveau 30, seuil abaissé de 15 niveaux, en plus de Veine mère. | 3 × 5 |
| 8 | **Rien ne déborde** | clé | Quand un hangar est plein, 50 pts de la valeur de la production qui déborde est convertie dans la ressource de votre choix, à valeur égale : trois métal valent deux cristal ou un hydrogène. |  |
| 9 | **Carottage** | ultime | Une fois par jour, la mine de votre choix produit deux fois plus pendant 4 h. Vous choisissez la mine et le moment. |  |

- **Première coulée** : chaque niveau terminé d'une mine verse ses heures de production, y compris le niveau offert par Coup de maître. Le versement va directement dans le stock de la planète.
- **Puits maître** vaut pour la planète mère, **Mines jumelles** pour chaque colonie, dès le niveau 1 de la mine.
- **Prospection** : le tirage se fait parmi toutes les mines debout de toutes vos planètes (pas les lunes), chacune avec la même chance quel que soit son niveau. Une nouvelle mine du jour est tirée peu après la fin des 24 h.
- **Veine mère** ne vaut que pour la mine du jour, sur sa planète, tant que son jour court ; les autres mines n'en tirent rien.
- **Filon choisi** : votre choix remplace la mine tirée et part pour 24 h ; vous rechoisissez à la fin de ces 24 h. Sans choix, le tirage continue.
- **Double filon** : la baisse s'additionne aux autres réductions de bâtiment (Plans connus, Devis serré…) et compte au moment où vous lancez l'amélioration ; la mine doit être la mine du jour à cet instant.
- **Galeries** se déclenche sur le niveau réel de la mine (30, puis 25, 20 et 15 aux rangs 1 à 3), pas sur son niveau de production, et seulement sur la mine du jour.
- **Rien ne déborde** : seul le débordement des deux autres ressources est converti, à valeur égale, arrondi à l'inférieur, et seulement dans la place libre du hangar de la ressource choisie (le métal tant que vous n'avez rien choisi). Le choix se fait planète par planète. Il ne joue que sur la production, et après Stock de sécurité (arbre commun).
- **Carottage** : l'Excavateur minéral, l'Extracteur cristallin ou le Condensateur d'hydrogène, au moment que vous choisissez.

### Chantier

*Le chantier qui travaille pendant que vous dormez.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Le chantier ne dort pas** | clé | Quand la file de bâtiments d'une planète est vide, le chantier met de côté une avance égale à 50 % du temps écoulé, jusqu'à 1 h : le prochain ordre dure d'autant moins. |  |
| 2 | **Équipes de veille** | 3 rangs | Votre chantier peut mettre de côté 3 h d'avance en plus. | 3 × 1 h |
| 3 | **A · Coulée continue** | choix | Un ordre qui démarre de lui-même à la suite du précédent part avec 10 % de son temps déjà fait. | |
|  | **B · Fondations coulées** |  | Un ordre lancé à la main part avec 5 % de sa durée déjà faits, 30 min au moins, au plus 50 %. | |
| 4 | **Rattrapage** | 3 rangs | Sur une colonie, un bâtiment encore sous le niveau de votre planète mère se construit 15 % plus vite. | 3 × 5 % |
| 5 | **Chantier spatial de nuit** | clé | Votre chantier spatial vide met lui aussi de l'avance de côté, et elle peut raccourcir vos vaisseaux et défenses. |  |
| 6 | **A · Banque d'heures** | choix | L'avance n'est plus versée d'office : vous la gardez, jusqu'à 8 h, et la versez sur l'ordre de votre choix. | |
|  | **B · Relais automatique** |  | L'avance reste versée d'office au prochain ordre, et vous pouvez en mettre 1 h de plus de côté. | |
| 7 | **Plans d'avance** | 3 rangs | Votre chantier met de côté 30 % du temps de file vide en plus. | 3 × 10 % |
| 8 | **Avance partagée** | clé | L'avance d'une planète peut être versée sur un ordre de n'importe quelle autre de vos planètes, au plus 50 % de cet ordre. |  |
| 9 | **Coup de collier** | ultime | Une fois par jour, le chantier de la planète de votre choix travaille deux fois plus vite pendant 4 h. |  |

- **Le chantier ne dort pas** : l'avance se met de côté planète par planète, tant que sa file de bâtiments est vide. Elle est versée d'office à la prochaine construction ou démolition lancée sur cette file vide, et **toute** l'avance part, même si l'ordre est plus court qu'elle.
- **Coulée continue** ne joue que sur un ordre de la file qui démarre de lui-même. **Fondations coulées** ne joue que sur un ordre lancé sur une file vide : 30 min, ou 5 % de sa durée si c'est plus, sans dépasser la moitié de sa durée.
- **Rattrapage** vaut aussi pour le niveau égal à celui de la planète mère. Il s'ajoute à la vitesse de construction de l'arbre commun ; une durée se divise par (1 + vitesse).
- **Chantier spatial de nuit** : la planète a une seule réserve, qui se remplit tant que l'un au moins de ses deux chantiers (bâtiments, Dock orbital) est vide, au même rythme. Un ordre de vaisseaux ou de défenses lancé sur un Dock orbital vide n'en prend que sa propre durée.
- **Banque d'heures** : le plafond passe à 8 h à la place des 5 h (Équipes de veille n'y ajoute plus rien). Vous versez l'avance sur un ordre en cours de la planète (vaisseaux et défenses avec Chantier spatial de nuit), au plus ce qu'il lui reste.
- **Avance partagée** : le versement vers une autre planète se fait à la main, aussi avec Relais automatique ; tous les apports d'autres planètes réunis ne dépassent pas 50 % de la durée de l'ordre.
- **Coup de collier** ne touche que le chantier de bâtiments. L'ordre en cours gagne aussitôt jusqu'à 4 h (au plus la moitié de ce qui lui reste) ; un ordre qui démarre pendant la fenêtre gagne de même sur ce qu'il reste de la fenêtre.

### Fonderie

*Payer moins, garder ce qu'on a mis de côté.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Plans connus** | clé | Un niveau de bâtiment que vous avez déjà atteint sur une autre de vos planètes coûte 10 % de moins. |  |
| 2 | **Coup de maître** | 3 rangs | Chaque bâtiment terminé a 6 % de chances de monter aussi au niveau suivant, gratuitement. | 3 × 2 % |
| 3 | **A · Devis serré** | choix | Vos bâtiments coûtent 5 % de moins. | |
|  | **B · Achats groupés** |  | Vos défenses coûtent 10 % de moins. | |
| 4 | **Archives de chantier** | 3 rangs | Les niveaux que vous connaissez déjà coûtent encore 15 % de moins. | 3 × 5 % |
| 5 | **Acompte** | clé | Les ressources mises de côté pour l'ordre en tête de votre file de bâtiments sont à l'abri du pillage, jusqu'à 30 % de son coût. |  |
| 6 | **A · Crédit de chantier** | choix | Un ordre démarre même s'il manque jusqu'à 10 % de ses ressources ; le reste est prélevé sur votre production. | |
|  | **B · Paiement en métal** |  | Le cristal ou l'hydrogène qui manque à un ordre se paie en métal : 2 de métal par unité manquante. | |
| 7 | **Coffre de chantier** | 3 rangs | Acompte met 30 % de plus du coût de l'ordre à l'abri. | 3 × 10 % |
| 8 | **Plans d'alliance** | clé | Un niveau qu'un membre de votre alliance a déjà atteint compte comme connu pour Plans connus. |  |
| 9 | **Commande d'État** | ultime | Une fois par semaine, l'amélioration de votre choix coûte 50 % de moins. |  |

- **Plans connus** : le niveau doit être atteint sur une **autre** de vos planètes ou lunes. Les réductions de bâtiment s'additionnent (Plans connus, Archives de chantier, Devis serré : 30 % au plus, 45 % sur la mine du jour avec Double filon) ; le prix est arrondi à l'unité supérieure.
- **Achats groupés** : 10 % sur toutes les défenses, hors plafond de coût de la classe ; les vaisseaux ne sont plus concernés.
- **Coup de maître** : seulement après une amélioration (pas une démolition), et si le niveau suivant est possible (niveau maximal, case libre).
- **Acompte** : l'ordre protégé est le premier ordre **en attente** dans la file de la planète, pas celui en cours (déjà payé), ni une démolition. La part abritée, au plus le stock, est retirée de ce qui peut être pillé ; le taux de pillage s'applique ensuite au reste.
- **Crédit de chantier** : il faut au moins 90 % de **chaque** ressource. Tout le stock disponible part, le manque devient une dette prélevée sur le stock dès qu'il se remplit, avant toute autre dépense. Pas de nouveau crédit tant qu'une dette court. **Paiement en métal** paie en métal le cristal et l'hydrogène qui manquent, s'il y a assez de métal. Les deux ne valent que pour les bâtiments.
- **Commande d'État** : vous désignez sur une planète le prochain niveau d'un bâtiment ; le prix baisse dès la désignation, que vous pouvez changer tant que l'ordre n'est pas payé. La remise porte sur le prix déjà réduit par les autres talents.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| Les mines de la planète mère produisent comme si elles avaient +1 niveau | 1 |
| Les mines des colonies produisent comme si elles avaient +1 niveau | 1 |
| La mine du jour produit comme si elle avait +1 niveau, dès son premier niveau | 1 |
| Galeries s'applique 15 niveaux plus tôt | 15 |
| +15 % de vitesse de construction sur un niveau de colonie que la planète mère a déjà | 15 % |
| −25 % de coût d'un niveau de bâtiment déjà atteint sur une autre de vos planètes | 25 % |
| −5 % de coût en ressources des bâtiments | 5 % |
| −10 % de coût des défenses | 10 % |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur | Filon 15 · Fonderie 10 | Carottage, la mine du jour à 3 niveaux de plus dès le niveau 15, 4 h de production à chaque niveau de mine, Prospection à 15 % sur une mine choisie (Filon choisi) ou −15 % sur son amélioration (Double filon), Rien ne déborde ; niveaux connus −25 % (−30 % avec Devis serré), Coup de maître 6 %, Acompte 30 % |
| Contremaître absent | Chantier 15 · Filon 10 | réserve de 80 % du temps vide, 5 h (Relais automatique) ou 8 h (Banque d'heures) par planète, Dock orbital compris, Rattrapage 15 %, Avance partagée, Coup de collier ; 4 h de production à chaque niveau de mine, Prospection 15 %, Veine mère sur la mine du jour |
| Colonisateur | Fonderie 15 · Chantier 10 | Commande d'État, Plans d'alliance, Acompte jusqu'à 60 %, niveaux connus −25 % ; réserve de 50 % du temps vide jusqu'à 5 h ou 8 h, Rattrapage 15 % sur les colonies, Chantier spatial de nuit |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Le Chantier récompense les files vides** : l'avance n'est versée d'office qu'à un ordre lancé sur une file vide. Un joueur qui garde sa file pleine profite surtout de Coulée continue et de Coup de collier.
- **Une avance plus longue que l'ordre est perdue** : lancer un bâtiment de 10 min avec 5 h de réserve consomme les 5 h. Avec Banque d'heures, versez-la à la main sur un gros ordre.
- **Première coulée, Prospection et Carottage ignorent la Maîtrise du Plasma** : ils portent sur la production propre de la mine. Une planète en manque d'énergie réduit aussi Prospection et Carottage.
- **Les niveaux de production en plus ne coûtent pas d'énergie** : la mine consomme celle de son niveau réel.
- **Rien ne déborde ne sauve pas la ressource choisie** : son propre débordement est perdu, et rien n'est converti quand son hangar est plein.
- **Plans connus ne vaut que pour un niveau déjà atteint** sur une autre de vos planètes (ou chez un membre de votre alliance avec Plans d'alliance) : la planète la plus avancée paie plein tarif.
- **Acompte protège l'ordre en attente** : gardez un ordre en file derrière celui en cours. Au plus 60 % de son coût, jamais plus que le stock ; le pillard prend son taux sur le reste.
- **Les réductions de coût ne changent pas les points** : points et expérience se calculent sur le prix du catalogue.

## Pages liées

- [Les talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Les ressources](/fr/economy/resources)
- [Files de construction](/fr/economy/build-queue)
- [Pillage](/fr/combat/plunder)
