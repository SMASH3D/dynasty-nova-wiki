---
wiki_id: 151
locale: "fr"
path: "dynasty/classes/admiral"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/admiral"
title: "L'Amiral"
description: "La classe du combat frontal : Ligne de feu, Campagne et Butin de guerre."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:36.126Z"
updated: "2026-10-15T18:57:17.926Z"
---

# L'Amiral

> **En bref** : l'Amiral est la classe du combat frontal. Elle ne change pas les vaisseaux que vous construisez, mais ce qu'ils valent une fois face à l'ennemi. Tout le combat tient dans la branche Ligne de feu ; Campagne fait partir vite, enchaîner et rentrer plus tôt ; Butin de guerre ramène davantage de chaque bataille.
{.is-info}

## Règles

1. L'Amiral est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Ligne de feu, Campagne et Butin de guerre.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. La vitesse de flotte, l'hydrogène et les soutes génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). L'Amiral n'y ajoute que des **accents** étroits : la vitesse des attaques, espionnages et destructions de lune (Marche forcée) et des recyclages (Recycleurs rapides), l'hydrogène, la construction et le coût des vaisseaux de combat, et une flotte réservée aux attaques.
5. Les **vaisseaux de combat** sont l'Intercepteur, l'Assaillant, la Corvette, le Cuirassé, le Frappe-orbital, le Prédateur, l'Annihilateur et le Colossus stellaire. Les vaisseaux civils (Navette de fret, Cargo stellaire, Récupérateur, Éclaireur, Pionnier spatial) et le Collecteur solaire n'en sont pas.
6. Les bonus de statistiques s'appliquent **après** la recherche et se multiplient avec elle. Ils jouent en attaque comme en défense. Les bonus de dégâts d'une paire (Lire la coque, Feu concentré) se multiplient entre eux.

## Exemple chiffré

**Canons réglés et Doctrine de coque, sur une Corvette**
- Armement de base 400, Systèmes Offensifs niveau 10 : 400 × 2 = 800. Avec Canons réglés au rang 3 : 800 × 1,09 = **872**.
- Avec Doctrine de coque, les 9 % passent à la coque et s'ajoutent aux 4 % du nœud : coque +13 %, armement 800 sans bonus.

**Remorquage (20 %), Station de réparation niveau 10, 30 % de débris**
- Part de la Station : 54 % × (1 − 30 %) = 37,8 %. Remorquage : 37,8 % × 20 % = **7,56 %**.
- 30 Corvettes perdues en attaque : 30 × 7,56 % = 2,268, soit **2 Corvettes**, et 26,8 % de chances d'en avoir une troisième.
- Les mêmes 30 Corvettes perdues en défense, avec Chantier de démontage : 54 % × 1,2 × 70 % = 45,36 %, soit **13** Corvettes (11 sans le nœud).

**Part du butin et Percée, contre une cible sans abri**
- Une attaque gagnée pille 50 % + 15 points = **65 %** du stock. Sur 2 000 000 de métal, vous emportez **1 300 000**, dans la limite de vos soutes.
- Un match nul pille à 30 % du taux d'une victoire : 65 % × 30 % = **19,5 %** du stock, soit **390 000** métal.

**Briseur de lunes**
- Contre une lune de 8 944 km, le risque de perdre votre flotte est √8 944 / 2 = 47,29 % ; avec le nœud : 47,29 % × 0,75 = **35,47 %**. La chance de détruire la lune ne change pas.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["BUTIN DE GUERRE<br/>Ce qu'on ramène d'une bataille."]:::head
        B3R1{{"Remorquage<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Part du butin<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Personne en orbite<br/>1 pt"]:::option
        B3R3B["② Percée<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Cale sèche<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Recyclage de combat<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Réparation d'urgence<br/>1 pt"]:::option
        B3R6B["② Recycleurs rapides<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Raffinage<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Chantier de démontage<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Rapaces<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["CAMPAGNE<br/>Partir vite, frapper, rentrer."]:::head
        B2R1{{"Marche forcée<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Le plein sur l'ennemi<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Escorte rapide<br/>1 pt"]:::option
        B2R3B["② Économie de guerre<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Retour victorieux<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Escadre d'assaut<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Rappel ordonné<br/>1 pt"]:::option
        B2R6B["② Ligne de ravitaillement<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Chantier de guerre<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Terre brûlée<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Seconde vague<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["LIGNE DE FEU<br/>Ce que vaut votre flotte au contact."]:::head
        B1R1{{"Blindage<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Canons réglés<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Doctrine du feu<br/>1 pt"]:::option
        B1R3B["② Doctrine de coque<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Salves<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Le maître de cadence<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Salve de siège<br/>1 pt"]:::option
        B1R6B["② Contre-mesures<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Lire la coque<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Briseur de lunes<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Feu concentré<br/>ultime"]]:::ultimate
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

### Ligne de feu

*Ce que vaut votre flotte au contact.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Blindage** | clé | Le bouclier de vos vaisseaux est 3 % plus solide. |  |
| 2 | **Canons réglés** | 3 rangs | Vos vaisseaux font 9 % de dégâts en plus. | 3 × 3 % |
| 3 | **A · Doctrine du feu** | choix | Vos défenses reçoivent 50 % du bonus d'armement de vos vaisseaux. | |
|  | **B · Doctrine de coque** |  | Le bonus de vos vaisseaux passe de l'armement à la coque, et leur coque gagne encore 4 %. | |
| 4 | **Salves** | 3 rangs | Vos feux rapides contre les vaisseaux que vous contrez enchaînent 9 % de tirs en plus. | 3 × 3 % |
| 5 | **Le maître de cadence** | clé | Désignez un type de vaisseau : ses feux rapides les plus forts montent de 1. |  |
| 6 | **A · Salve de siège** | choix | Vos feux rapides contre les défenses enchaînent 10 % de tirs en plus. | |
|  | **B · Contre-mesures** |  | Vous subissez 10 % de dégâts en moins des unités qui vous contrent. | |
| 7 | **Lire la coque** | 3 rangs | Vos tirs font 10,5 % de dégâts en plus contre les unités que vous contrez. | 3 × 3,5 % |
| 8 | **Briseur de lunes** | clé | Quand vous détruisez une lune, le risque de perdre vos vaisseaux baisse de 25 %. |  |
| 9 | **Feu concentré** | ultime | Avant une attaque, désignez un type d'unité ennemie : tous vos tirs contre lui font 7,5 % de dégâts en plus. |  |

- **Doctrine du feu** : vos défenses reçoivent la moitié du bonus d'armement de vos vaisseaux, soit +4,5 % avec Canons réglés au rang 3. Elle ne sert que lorsqu'on vous attaque.
- **Doctrine de coque** : Canons réglés ne donne plus d'armement, ses points vont à la coque.
- **Salves** et **Salve de siège** allongent les chaînes de tirs rapides de vos vaisseaux (contre les vaisseaux, contre les défenses).
- **Le maître de cadence** : vous désignez, dans l'onglet Compétences, un type parmi la Corvette, le Frappe-orbital, l'Annihilateur et le Colossus stellaire. Il **ne s'ajoute pas** à Salves ou Salve de siège : chaque tir rapide prend le meilleur des deux.
- **Contre-mesures** protège vos vaisseaux et vos défenses, en attaque comme en défense. Toutes sources confondues, cette réduction ne dépasse jamais 15 %.
- **Lire la coque** joue sur toute paire où le tireur a un tir rapide contre sa cible. Le diapason de L'Accord ajoute 5 % au-delà du plafond.
- **Feu concentré** se règle à l'envoi d'une mission Attaque (pas d'une destruction de lune). Il ne joue pas quand on vous attaque.

### Campagne

*Partir vite, frapper, rentrer.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Marche forcée** | clé | Vos attaques, espionnages et destructions vont 10 % plus vite. |  |
| 2 | **Le plein sur l'ennemi** | 3 rangs | Une attaque gagnée vous rend 30 % de l'hydrogène brûlé à l'aller. | 3 × 10 % |
| 3 | **A · Escorte rapide** | choix | Dans une flotte d'attaque, vos transporteurs volent 25 % plus vite, sans dépasser le vaisseau le plus rapide. | |
|  | **B · Économie de guerre** |  | Vos vaisseaux de combat brûlent 10 % d'hydrogène en moins. | |
| 4 | **Retour victorieux** | 3 rangs | Après une attaque gagnée, votre flotte rentre 30 % plus vite. | 3 × 10 % |
| 5 | **Escadre d'assaut** | clé | Vous pouvez avoir 1 flotte de plus en vol, réservée aux attaques. |  |
| 6 | **A · Rappel ordonné** | choix | Une flotte rappelée rentre 20 % plus vite. | |
|  | **B · Ligne de ravitaillement** |  | Une attaque perdue ou nulle vous rend 15 % de l'hydrogène brûlé à l'aller. | |
| 7 | **Chantier de guerre** | 3 rangs | Vos vaisseaux de combat se construisent 15 % plus vite et coûtent 15 % de moins. | 3 × 5 % |
| 8 | **Terre brûlée** | clé | Les défenses que vous détruisez ont 15 pts de chances en moins d'être réparées gratuitement (70 % d'habitude). |  |
| 9 | **Seconde vague** | ultime | Une flotte qui vient de gagner une attaque repart 1 fois vers une autre cible, à 1 système au plus, sans rentrer. |  |

- **Le plein sur l'ennemi** rend une part de l'hydrogène de l'aller sur une attaque gagnée dont la flotte survit. Il est chargé hors capacité et livré au retour.
- **Escorte rapide** accélère les Navettes de fret et Cargos stellaires d'une mission Attaque, sans dépasser le vaisseau le plus rapide. **Économie de guerre** réduit la part d'hydrogène brûlée par vos vaisseaux de combat : une flotte où ils brûlent la moitié du carburant économise 5 %.
- **Escadre d'assaut** ne sert qu'à la mission Attaque (ni espionnage ni destruction de lune).
- **Ligne de ravitaillement** : une défaite détruit toute la flotte, il n'y a donc rien à rendre ; en pratique, elle ne joue que sur un match nul.
- **Chantier de guerre** : la baisse de coût ne vaut que pour les vaisseaux de combat, hors plafond de coût de la classe ; elle s'additionne aux autres réductions du vaisseau.
- **Terre brûlée** vaut pour vos attaques et vos destructions de lune.
- **Seconde vague** : à l'envoi, vous nommez une seconde cible, une planète d'un autre joueur ou abandonnée, dans la même galaxie, à 1 système au plus de la première. Si l'attaque est gagnée et la flotte survit, elle y repart aussitôt, une fois par vol, en prenant l'hydrogène du saut dans ses soutes. Trêve, alliance, mode vacances, protections et limite d'attaques sont vérifiés au moment du saut : en cas de refus, la flotte rentre.

### Butin de guerre

*Ce qu'on ramène d'une bataille.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Remorquage** | clé | Votre dock récupère les vaisseaux perdus en attaque à 20 % de son efficacité. |  |
| 2 | **Part du butin** | 3 rangs | Vos attaques gagnées pillent 15 points de plus, au-delà de la moitié habituelle des ressources de la cible. | 3 × 5 pts |
| 3 | **A · Personne en orbite** | choix | Le remorquage marche même quand toute votre flotte est détruite. | |
|  | **B · Percée** |  | Une attaque qui finit sur un match nul pille quand même, à 30 % du taux de pillage normal. | |
| 4 | **Cale sèche** | 3 rangs | Votre dock répare vos vaisseaux 24 % plus vite. | 3 × 8 % |
| 5 | **Recyclage de combat** | clé | Les recycleurs envoyés avec une attaque ramassent les débris dès la fin du combat. |  |
| 6 | **A · Réparation d'urgence** | choix | La réparation la plus courte au dock dure 15 min de moins (30 min d'habitude). | |
|  | **B · Recycleurs rapides** |  | Vos missions de recyclage vont 10 % plus vite. | |
| 7 | **Raffinage** | 3 rangs | Chaque récolte de débris vous rapporte aussi 12 % de son tonnage en hydrogène. | 3 × 4 % |
| 8 | **Chantier de démontage** | clé | Votre dock récupère vos vaisseaux perdus en défense avec 20 % d'efficacité en plus. |  |
| 9 | **Rapaces** | ultime | Après une attaque gagnée, vos vaisseaux de combat chargent 30 % des débris dans leurs soutes libres, après le pillage. |  |

- **Remorquage** : c'est la Station de réparation de la planète de départ qui remorque. Une lune n'a pas de Station : une flotte partie d'une lune ne remorque rien. Le remorquage utilise un **arrondi probabiliste** : la partie décimale devient une chance d'avoir un vaisseau de plus.
- **Part du butin** : les points s'ajoutent au taux de pillage de la victoire (50 %), avec ceux des cibles abandonnées de l'arbre commun ; les abris du défenseur se retirent ensuite, et vos soutes plafonnent toujours ce que vous emportez.
- **Percée** : 30 % du taux de pillage d'une victoire, Part du butin compris, abris du défenseur déduits.
- **Cale sèche** accélère toutes les réparations de la Station ; une réparation reste comprise entre 30 min (15 min avec Réparation d'urgence) et 12 h.
- **Recyclage de combat** : les Récupérateurs de la flotte d'attaque ramassent les débris de ce combat, après le pillage.
- **Raffinage** ajoute l'hydrogène seulement dans la place qui reste en soute.
- **Chantier de démontage** ne joue qu'en défense, pas sur le remorquage.
- **Rapaces** : après une attaque gagnée, vos vaisseaux de combat chargent 30 % des débris du combat dans leurs soutes libres, après le pillage et les Récupérateurs.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| +3 % de bouclier des vaisseaux | 3 % |
| +9 % sur l'armement des vaisseaux, ou sur leur coque en doctrine de coque | 9 % |
| Vos défenses reçoivent sur leur armement 50 % du bonus d'arsenal de vos vaisseaux | 50 % |
| +13 % de coque des vaisseaux, en doctrine de coque seulement | 4 % |
| +9 % de chaîne de feu rapide contre les vaisseaux | 9 % |
| +1 aux feux rapides les plus forts d'un type de vaisseau désigné | 1 |
| +10 % de chaîne de feu rapide contre les défenses | 10 % |
| −10 % de dégâts subis des tirs ennemis qui ont un feu rapide contre vos unités | 10 % |
| +15 % de dégâts de contre, sur les unités contre lesquelles le tireur a un feu rapide | 10,5 % |
| −25 % de risque de perdre vos vaisseaux lors d'une destruction de lune | 25 % |
| +10 % de vitesse aux attaques, espionnages et destructions | 10 % |
| Une attaque victorieuse rend 30 % de l'hydrogène brûlé pour atteindre la cible | 30 % |
| +25 % de vitesse des transporteurs d'une flotte d'attaque, sans dépasser le plus rapide | 25 % |
| −10 % de consommation d'hydrogène des vaisseaux de combat | 10 % |
| +30 % de vitesse au retour d'une attaque gagnée | 30 % |
| +1 slot de flotte réservé aux attaques | 1 |
| +20 % de vitesse au retour d'une flotte rappelée | 20 % |
| Une attaque perdue ou nulle rend 15 % de l'hydrogène brûlé pour atteindre la cible | 15 % |
| +15 % de vitesse de construction des vaisseaux de combat | 15 % |
| −15 % de coût des vaisseaux de combat | 15 % |
| −15 pts de réparation gratuite des défenses que vous détruisez | 15 pts |
| Les vaisseaux perdus en attaque sont récupérés à 20 % du taux du dock de réparation de la base d'origine | 20 % |
| +15 pts de taux de pillage sur une attaque gagnée | 15 pts |
| Une attaque nulle pille à 30 % du taux d'une attaque gagnée | 30 % |
| +24 % de vitesse de réparation au dock | 24 % |
| −15 min sur la durée minimale de réparation au dock | 15 min |
| +10 % de vitesse des flottes en mission de recyclage | 10 % |
| Une récolte de débris rapporte en plus 12 % du tonnage récolté en hydrogène | 12 % |
| +20 % du facteur de récupération au dock | 20 % |
| Après une attaque gagnée, vos vaisseaux de combat chargent 30 % des débris | 30 % |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chasseur de flottes | Ligne de feu 15 · Campagne 10 | Feu concentré, armement +9 % (ou coque +13 %), bouclier +3 %, Salves, Lire la coque ; Marche forcée, hydrogène rendu sur les victoires, retour victorieux, une flotte d'attaque en plus |
| Raideur | Campagne 15 · Butin de guerre 10 | Seconde vague, Chantier de guerre, Terre brûlée ; remorquage à 20 %, pillage à 65 % (Part du butin), Personne en orbite ou Percée, réparations plus rapides, recyclage de combat |
| Pilleur de batailles | Butin de guerre 15 · Ligne de feu 10 | Rapaces, remorquage, pillage à 65 %, Raffinage, Chantier de démontage ; armement +9 %, bouclier +3 %, Salves, Le maître de cadence |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Feu concentré se règle avant le départ** : le type d'unité visé se désigne dans le formulaire d'envoi. Espionnez d'abord.
- **Doctrine de coque retire l'armement** : avec elle, Canons réglés ne donne plus aucun dégât.
- **Le maître de cadence peut ne rien ajouter** : avec Salves au rang 3 et Salve de siège, chaque tir rapide est déjà mieux servi.
- **Seconde vague ne va pas loin** : la seconde cible doit être à 1 système au plus de la première, et la flotte paie le saut avec l'hydrogène de ses soutes.
- **Pas de Station de réparation, pas de remorquage** : une flotte partie d'une lune ne remorque rien. Sans Personne en orbite, une flotte entièrement détruite ne rend rien.
- **Retour victorieux ne compte pas dans le plafond de vitesse**, mais Marche forcée, si : elle occupe l'accent de vitesse de 10 % de la classe.
- **Terre brûlée frappe aussi un Vétéran** : sa réparation des défenses perd 15 points contre vous.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Classes](/fr/dynasty/classes)
- [Arbre commun](/fr/dynasty/common-tree)
- [Dynasties](/fr/dynasty/dynasties)
- [Tirs rapides](/fr/fleet/rapid-fire)
- [Pillage](/fr/combat/plunder)
- [Champs de débris](/fr/combat/debris)
- [Station de réparation](/fr/economy/repair-station)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Destruction de lune](/fr/combat/moon-destruction)
