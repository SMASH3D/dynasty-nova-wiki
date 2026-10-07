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
updated: "2026-10-06T10:29:41.875Z"
---

# Le Bâtisseur

> **En bref** : le Bâtisseur est la classe dont les mines rapportent plus que leur niveau, dont le chantier travaille pendant qu'il dort, et qui paie chaque niveau moins cher, surtout quand il rattrape ses colonies. Classe commune à toutes les dynasties. Ses trois branches : **Filon**, **Chantier** et **Fonderie**.
{.is-info}

*« Ce qui tient debout. »* Le chantier et la mine : produire plus, construire plus vite, gaspiller moins.

## Règles

1. L'arbre du Bâtisseur suit les règles de tout [arbre de classe](/fr/dynasty/talents) : 3 branches de 9 rangées, 15 points par branche, 25 points au maximum.
2. Les bonus génériques (production des mines, vitesse de construction, entrepôts, Maîtrise du Plasma) viennent de l'[arbre commun](/fr/dynasty/common-tree), branche Prospérité. Le Bâtisseur n'a que des **mécaniques**, et un seul bonus d'accent : le **coût**, au choix des bâtiments ou des vaisseaux et défenses (5 %).
3. **Rattrapage** est son accent de vitesse de construction : il ne joue que sur une colonie, pour un bâtiment encore sous le niveau atteint sur votre planète mère (15 % au plus).
4. Un bâtiment profite d'au plus **1 niveau de production en plus** par Veine mère, et d'au plus 1 autre par Puits maître ou Mines jumelles.
5. Tout l'arbre ne sert que vous, sauf **Acompte** : c'est le seul talent qu'un autre joueur rencontre, quand il pille la planète.

## Exemple chiffré

Planète avec un Excavateur minéral au niveau 20 (4 036 métal par heure ; 4 662 au niveau 21, à pleine énergie).

- **Première coulée + Grandes coulées** (9 h) : l'Excavateur passe au niveau 21 et verse aussitôt 9 × 4 662 = **41 958 métal**.
- **Veine mère** (dès le niveau 20) : l'Excavateur 20 produit comme un niveau 21, soit **4 662 au lieu de 4 036** par heure (+15 %).
- **Prospection** au rang 3 (+30 %) sur l'Excavateur 21 : 4 662 × 1,3 = **6 061 par heure** pendant 24 h, soit environ 33 600 métal de plus dans la journée.
- **Carottage** (production triplée pendant 4 h) sur le même Excavateur : 2 × 4 662 × 4 = **37 296 métal** de plus.
- **Plans connus + Archives de chantier** (−25 %) : faire passer l'Excavateur d'une colonie du niveau 13 au niveau 14 quand la planète mère a déjà atteint le 14 coûte environ **8 758 métal et 2 189 cristal** au lieu de 11 677 et 2 919.

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

### Filon : « Des mines qui rapportent plus que leur niveau. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Première coulée** | Quand une mine monte de niveau, elle verse aussitôt une part de sa nouvelle production. | 3 h |
| 2 | 3 rangs | **Grandes coulées** | Une mine qui monte de niveau verse davantage de sa nouvelle production. | +2 h par rang (9 h au total) |
| 3 | choix | **A : Puits maître** / **B : Mines jumelles** | A : les mines de la planète mère produisent comme si elles avaient 1 niveau de plus. <br> B : les mines des colonies produisent comme si elles avaient 1 niveau de plus. | +1 niveau |
| 4 | 3 rangs | **Prospection** | Chaque jour, une mine tirée au sort produit davantage pendant 24 h. | +10 % par rang (30 %) |
| 5 | clé | **Veine mère** | À partir du niveau 20, chaque mine produit comme si elle avait 1 niveau de plus, en plus de Puits maître ou de Mines jumelles. | +1 niveau dès le niveau 20 |
| 6 | choix | **A : Filon choisi** / **B : Double filon** | A : vous choisissez chaque jour la mine de Prospection. <br> B : deux mines sont tirées chaque jour au lieu d'une. | choix / 2 mines |
| 7 | 3 rangs | **Galeries** | Veine mère s'applique plus tôt. | −3 niveaux par rang (dès le niveau 11) |
| 8 | clé | **Rien ne déborde** | Quand un entrepôt est plein, la production qui déborde est convertie, unité pour unité, dans la ressource de votre choix. | 50 % |
| 9 | ultime | **Carottage** | Une fois par jour, la mine de votre choix produit trois fois plus pendant 4 h. Vous choisissez la mine et le moment. | ×3 pendant 4 h |

### Chantier : « Le chantier qui travaille pendant que vous dormez. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Le chantier ne dort pas** | Quand la file de bâtiments d'une planète est vide, le chantier met de côté une avance égale à une part du temps écoulé ; le prochain ordre dure d'autant moins. | 50 % du temps, jusqu'à 1 h |
| 2 | 3 rangs | **Équipes de veille** | Le chantier peut mettre plus d'avance de côté. | +1 h par rang (4 h) |
| 3 | choix | **A : Coulée continue** / **B : Fondations coulées** | A : un ordre qui démarre de lui-même à la suite du précédent part avec une part de son temps déjà faite. <br> B : un ordre lancé à la main part avec 30 min déjà faites, au plus la moitié de sa durée. | 10 % / 30 min |
| 4 | 3 rangs | **Rattrapage** | Sur une colonie, un bâtiment encore sous le niveau de votre planète mère se construit plus vite (accent). | +5 % par rang (15 %) |
| 5 | clé | **Chantier spatial de nuit** | Le Dock orbital vide met lui aussi de l'avance de côté, et elle raccourcit vos vaisseaux et défenses. | déblocage |
| 6 | choix | **A : Banque d'heures** / **B : Relais automatique** | A : l'avance n'est plus versée d'office ; vous la gardez et la versez sur l'ordre de votre choix. <br> B : l'avance reste versée d'office, et son plafond augmente. | jusqu'à 8 h / +1 h (5 h) |
| 7 | 3 rangs | **Plans d'avance** | Le chantier met de côté une plus grande part du temps de file vide. | +10 % par rang (80 %) |
| 8 | clé | **Avance partagée** | L'avance d'une planète peut être versée sur un ordre de n'importe quelle autre de vos planètes. | au plus 50 % de l'ordre |
| 9 | ultime | **Coup de collier** | Une fois par jour, le chantier de la planète de votre choix travaille deux fois plus vite pendant 4 h. | ×2 pendant 4 h |

### Fonderie : « Payer moins, garder ce qu'on a mis de côté. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Plans connus** | Un niveau de bâtiment déjà atteint sur une autre de vos planètes coûte moins cher. | −10 % |
| 2 | 3 rangs | **Coup de maître** | Chaque bâtiment terminé a une chance de monter aussi au niveau suivant, gratuitement. | 2 % par rang (6 %) |
| 3 | choix | **A : Devis serré** / **B : Achats groupés** | A : vos bâtiments coûtent moins cher. <br> B : vos vaisseaux et défenses coûtent moins cher. | −5 % (accent) |
| 4 | 3 rangs | **Archives de chantier** | Les niveaux connus coûtent encore moins cher. | −5 % par rang (−25 % avec Plans connus) |
| 5 | clé | **Acompte** | Les ressources mises de côté pour l'ordre en tête de la file de bâtiments sont à l'abri du pillage, jusqu'à une part de son coût. | 30 % |
| 6 | choix | **A : Crédit de chantier** / **B : Paiement en métal** | A : un ordre démarre même s'il manque une part de ses ressources ; le reste est prélevé sur votre production. <br> B : le cristal ou l'hydrogène qui manque se paie en métal. | 10 % / 2 métal par unité |
| 7 | 3 rangs | **Coffre de chantier** | Acompte met une plus grande part du coût à l'abri. | +10 % par rang (60 %) |
| 8 | clé | **Plans d'alliance** | Un niveau qu'un membre de votre alliance a déjà atteint compte comme connu pour Plans connus. | déblocage |
| 9 | ultime | **Commande d'État** | Une fois par semaine, l'amélioration de votre choix coûte moitié prix. | −50 %, 1 par semaine |

### Ce que 25 points donnent

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur | Filon 15 · Fonderie 10 | Carottage, Veine mère dès le niveau 11, une mine à +30 % chaque jour, 9 h de production à chaque niveau ; colonies rattrapées à −25 %, Coup de maître, Acompte |
| Contremaître absent | Chantier 15 · Filon 10 | le chantier rattrape la nuit jusqu'à 5 à 8 h par planète, avance partagée, Coup de collier ; Veine mère, Prospection, 9 h de production à chaque niveau |
| Colonisateur | Fonderie 15 · Chantier 10 | Commande d'État chaque semaine, Plans d'alliance, coûts −25 % sur tout rattrapage ; avance du chantier et Rattrapage sur les colonies |

## Pièges fréquents

- **Le Chantier récompense les files vides** : un joueur qui garde ses files pleines en tire peu. Coulée continue et Coup de collier sont là pour lui.
- **Plans connus ne vaut que pour un niveau déjà atteint** sur une autre de vos planètes (ou chez un allié avec Plans d'alliance) : la planète la plus avancée paie plein tarif.
- **Acompte ne protège que l'ordre en tête de file**, et au plus 60 % de son coût : un pillard prend toujours le reste du stock.
- **Les réductions de coût ne changent pas les points** : les points et l'expérience se calculent sur le coût du catalogue, avant réduction.

## Pages liées

- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Les ressources](/fr/economy/resources)
- [Files de construction](/fr/economy/build-queue)
