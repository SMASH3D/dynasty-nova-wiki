---
wiki_id: 158
locale: "fr"
path: "dynasty/classes/symbiote"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/symbiote"
title: "Le Symbiote"
description: "La classe de l'environnement, exclusive à L'Accord : Thermie, Croissance et Hôte."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:51.224Z"
updated: "2026-10-07T22:08:29.190Z"
---

# Le Symbiote

> **En bref** : le Symbiote joue ce que les autres subissent : la température de la planète, sa place dans le système, sa taille, sa lune et ses voisins. Thermie fait de la température un atout, Croissance tire le meilleur de la position et des cases, Hôte fait produire les planètes en friche et celles qui ont des voisins.
{.is-info}

## Règles

1. Le Symbiote est une classe **exclusive à [L'Accord](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Thermie, Croissance et Hôte.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. La production générique des mines, les colonies jeunes et les cases génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). La fusion, la production propre des Collecteurs solaires et le manque d'énergie relèvent de l'[Énergéticien](/fr/dynasty/classes/energist). Le Symbiote n'a qu'un **accent** : 2 cases de plus par planète (Terrain gagné), pour 4 au plus avec Arpenteurs (arbre commun).
5. Les bonus de mines de l'Hôte sont des mécaniques à part : ils s'ajoutent entre eux et aux autres bonus, tous calculés sur la **production brute** des trois mines (Excavateur minéral, Extracteur cristallin, Condensateur d'hydrogène), et ils restent **hors** du plafond de production des talents. Jamais sur une lune.
6. Les talents de température élargissent seulement la **part de bonus** d'un facteur, jamais son signe. Condensateur d'hydrogène : facteur 1,44 − 0,004 × température maximale, amplifié seulement au-dessus de 1. Capteurs photovoltaïques : facteur 1 + température du jour / 100, amplifié seulement au-dessus de 0 °C. Collecteur solaire : température maximale / 4 + 20 d'énergie, seule la part température est amplifiée, arrondi à l'unité inférieure. Le détail des températures est sur [Planètes : taille, température, type](/fr/universe/planets).
7. Le bonus de position **dépend du nombre de positions du système**, un paramètre d'univers (15 sur Redline). Dans un système à 15 positions, l'Extracteur cristallin gagne +40, +30 et +20 % en positions 1 à 3, l'Excavateur minéral +17, +23, +35, +23 et +17 % en positions 6 à 10. Ailleurs, la position est ramenée sur une échelle de 15 et le bonus est calculé entre les deux positions voisines : dans un système à 9 positions, la position 2 donne +22,5 % de cristal. Le Condensateur d'hydrogène n'a jamais de bonus de position.
8. Une planète est **en friche** tant que ses cases bâties sont strictement moins de 50 % de son total de cases (Modulateur planétaire et cases bonus compris). Cette notion n'existe que pour un Symbiote qui a Jeune pousse ou Sève montante, et ne s'applique jamais à une lune. Elle n'a rien à voir avec la colonie jeune de l'arbre commun.

## Exemple chiffré

**Condensateur d'hydrogène en position 15 d'un système à 15 positions** (−85 à −45 °C)
- Sans talent : 1,44 − 0,004 × (−45) = **1,62**. La part de bonus est 0,62.
- Avec Sang-froid (+10 %) : 1 + 0,62 × 1,10 = **1,68**.
- Avec en plus Écoute du climat au rang 3 (+40 % en tout) : 1 + 0,62 × 1,40 = **1,87**.
- Avec en plus Pôle froid (+65 % en tout) : 1 + 0,62 × 1,65 = **2,02**.
- Branche pleine, avec Les deux saisons et Climatiseur planétaire réglé vers le froid : le Condensateur lit −85 − 30 = −115 °C, facteur 1,44 + 0,46 = 1,90, puis 1 + 0,90 × 1,65 = **2,485**.
- Au niveau 20, vitesse d'économie ×1 (Redline) : 10 × 20 × 1,1²⁰ = 1 345,5 hydrogène par heure avant facteur, soit **2 179** sans talent et **3 343** avec la branche pleine (+53 %).

**Les deux saisons sur une colonie en position 8 d'un système à 15 positions** (20 à 60 °C)
- Sans talent, le Condensateur lit la température maximale : 1,44 − 0,004 × 60 = **1,20**.
- Avec l'ultime, il lit la minimale : 1,44 − 0,004 × 20 = **1,36**, soit 13 % d'hydrogène en plus.

**Bonus de position de l'Excavateur minéral en position 8 d'un système à 15 positions** (+35 % sans talent)
- Racines : 35 × 1,15 = **+40,25 %**.
- Racines et Marcottage : 35 × 1,45 = **+50,75 %**.
- Avec en plus Filon de métal : 35 × 1,65 = **+57,75 %**.
- Une planète mère au même endroit, avec Racines, Marcottage et Terre natale au rang 3 : 35 × 1,45 × ½ = **+25,375 %**.

**Collecteur solaire en position 8 d'un système à 15 positions** (température maximale 60 °C)
- Sans talent : 60 / 4 + 20 = **35** énergie par Collecteur.
- Peau de lumière au rang 3 : 15 × 1,45 + 20 = 41,75, arrondi à **41**.
- Satellites d'altitude : la planète est lue à 100 °C, 100 / 4 + 20 = **45**.
- Peau de lumière au rang 3, Pôle chaud, Satellites d'altitude et Climatiseur planétaire réglé vers le chaud : (60 + 30 + 40) / 4 = 32,5, × 1,70 (45 + 25 % d'amplitude) = 55,25, + 20 = **75**.

**Hôte sur une colonie de 210 cases dont 100 bâties, Excavateur minéral niveau 20** (4 036 métal par heure bruts, vitesse ×1)
- En friche (100 / 210 = 47,6 %) avec Sève montante au rang 3 : +15 %. Géants (plus de 200 cases) : +8 %. Trois planètes d'autres joueurs dans le système avec Foule : 3 × 2 = +6 %. Une autre de vos planètes dans le système avec Marées au rang 3 : +9 %.
- Total **+38 %** : 4 036 × 0,38 = **1 533** métal par heure en plus.
- Dans les 6 h qui suivent un raid qui a emporté des ressources, Repousse ajoute 20 % : +58 %, soit **2 340**.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["HÔTE<br/>Faire vivre un monde avec ce qu'il a."]:::head
        B3R1{{"Jeune pousse<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Sève montante<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Petits mondes<br/>1 pt"]:::option
        B3R3B["② Géants<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Longue friche<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Voisinage<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Foule<br/>1 pt"]:::option
        B3R6B["② Solitude<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Marées<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Repousse<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Friche éternelle<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["CROISSANCE<br/>Le bon endroit, la bonne taille."]:::head
        B2R1{{"Racines<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Terre natale<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Filon de métal<br/>1 pt"]:::option
        B2R3B["② Veine de cristal<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Lunes creusées<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Marcottage<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Terrain gagné<br/>1 pt"]:::option
        B2R6B["② Lune pleine<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Sol vivant<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Terraformeur vivant<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Transplantation<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["THERMIE<br/>La planète décide, vous l'écoutez."]:::head
        B1R1{{"Sang-froid<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Climatiseur planétaire<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Pôle froid<br/>1 pt"]:::option
        B1R3B["② Pôle chaud<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Peau de lumière<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"La saison longue<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Racines profondes<br/>1 pt"]:::option
        B1R6B["② Soleil d'hiver<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Écoute du climat<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Satellites d'altitude<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Les deux saisons<br/>ultime"]]:::ultimate
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

### Thermie

*La planète décide, vous l'écoutez.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Sang-froid** | clé | Les bonus de température de vos planètes, le froid pour l'hydrogène et la chaleur pour le solaire, sont 10 % plus forts. |  |
| 2 | **Climatiseur planétaire** | 3 rangs | Sur chaque planète, décalez la température de 30° vers le froid ou vers le chaud, réglable une fois par semaine. | 3 × 10° |
| 3 | **A · Pôle froid** | choix | Le bonus de froid de votre synthétiseur d'hydrogène est encore 25 % plus fort. | |
|  | **B · Pôle chaud** |  | Le bonus de chaleur de vos centrales solaires et de vos satellites est encore 25 % plus fort. | |
| 4 | **Peau de lumière** | 3 rangs | La part de l'énergie de vos satellites solaires qui vient de la température est 45 % plus forte. | 3 × 15 % |
| 5 | **La saison longue** | clé | Vos centrales solaires produisent toujours comme au plus chaud du mois, au lieu de suivre le cycle. |  |
| 6 | **A · Racines profondes** | choix | Sur une planète trop chaude, le rendement de votre synthétiseur d'hydrogène ne descend jamais sous ×1. | |
|  | **B · Soleil d'hiver** |  | Sur une planète froide, le rendement de vos centrales solaires ne descend jamais sous ×1,25. | |
| 7 | **Écoute du climat** | 3 rangs | Les bonus de température de vos planètes sont encore 30 % plus forts. | 3 × 10 % |
| 8 | **Satellites d'altitude** | clé | Vos satellites solaires produisent comme si la planète était 40° plus chaude. |  |
| 9 | **Les deux saisons** | ultime | Votre synthétiseur d'hydrogène lit la température la plus froide de la planète, et non la plus chaude. |  |

- **Sang-froid** et **Écoute du climat** s'additionnent (40 % au plus) et jouent sur le Condensateur d'hydrogène et les Capteurs photovoltaïques, pas sur les Collecteurs solaires.
- **Climatiseur planétaire** : jamais sur une lune. Le premier réglage est immédiat ; ensuite chaque planète attend 7 jours entre deux réglages, revenir à « aucun décalage » compris. Le décalage vaut pour le Condensateur, les Capteurs et les Collecteurs à la fois, dans le même sens : vers le froid, plus d'hydrogène et moins d'énergie solaire.
- **Pôle froid** ne vise que le Condensateur (65 % d'amplitude au plus avec les deux nœuds ci-dessus). **Pôle chaud** vise les Capteurs **et** la part température des Collecteurs.
- **Peau de lumière** ne touche que la part température d'un Collecteur (température maximale / 4), jamais ses 20 d'énergie de base.
- **La saison longue** : la température d'une planète suit le mois, de sa minimale le 1er à sa maximale au milieu du mois. Avec ce nœud, les Capteurs lisent toujours la maximale.
- **Racines profondes** relève le Condensateur à ×1 là où il tombe sous 1 (température maximale lue au-dessus de 110 °C). **Soleil d'hiver** relève les Capteurs à ×1,25 partout où leur facteur est plus bas.
- **Satellites d'altitude** s'ajoute au décalage du Climatiseur.
- **Les deux saisons** lit la température minimale, soit 40 °C sous la maximale, décalage compris.

### Croissance

*Le bon endroit, la bonne taille.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Racines** | clé | Le bonus de position de vos planètes dans leur système est 15 % plus fort. |  |
| 2 | **Terre natale** | 3 rangs | Votre planète mère reçoit ⅙ du bonus de sa position dans le système par rang, ½ au rang 3. | 3 × 16,67 % |
| 3 | **A · Filon de métal** | choix | Le bonus de position de vos mines de métal, au milieu du système, est encore 20 % plus fort. | |
|  | **B · Veine de cristal** |  | Le bonus de position de vos mines de cristal, près de l'étoile, est encore 20 % plus fort. | |
| 4 | **Lunes creusées** | 3 rangs | Chaque niveau de base lunaire creuse +3 cases en plus de ses 3, dans la limite du diamètre de la lune. | 3 × 1 |
| 5 | **Marcottage** | clé | Le bonus de position de vos planètes est encore 30 % plus fort. |  |
| 6 | **A · Terrain gagné** | choix | Chacune de vos planètes gagne 2 cases constructibles. | |
|  | **B · Lune pleine** |  | Vos lunes ne sont plus limitées par leur diamètre : chaque niveau de base lunaire leur donne toutes ses cases. | |
| 7 | **Sol vivant** | 3 rangs | Votre terraformeur et votre base lunaire coûtent 24 % de moins. | 3 × 8 % |
| 8 | **Terraformeur vivant** | clé | Chaque niveau de terraformeur donne +1 case en plus de ses 5. |  |
| 9 | **Transplantation** | ultime | Une fois par semaine, déplacez une colonie vers une position libre de son système, bâtiments et lune compris, si aucune flotte n'est en vol vers elle ou depuis elle. |  |

- **Racines**, **Marcottage** et **Filon de métal** ou **Veine de cristal** s'additionnent puis multiplient le bonus de position : +65 % au plus sur une mine. Rien là où la position ne donne rien.
- **Terre natale** : la planète mère n'a jamais de bonus de position sans ce nœud. La part s'applique au bonus déjà élargi par les nœuds ci-dessus.
- **Lunes creusées** : chaque niveau de Base lunaire donne 6 cases au rang 3, toujours dans la limite du diamètre de la lune, sauf avec Lune pleine.
- **Terrain gagné** ne vaut que pour les planètes, pas les lunes.
- **Sol vivant** ne vise que le Modulateur planétaire et la Base lunaire ; la réduction s'ajoute aux autres réductions de prix des bâtiments, au-delà de leur plafond commun.
- **Terraformeur vivant** : 6 cases par niveau de Modulateur au lieu de 5, et la case de plus des niveaux pairs reste (Modulateur 6 : 33 → 39 cases).
- **Transplantation** : une fois tous les 7 jours pour **tout l'empire**, jamais la planète mère. La position visée doit être libre, sans lune et hors espace lointain. Refusée si une flotte d'un autre joueur se dirige vers la colonie, si l'une de vos flottes vole vers elle ou depuis elle, ou en mode vacances. La colonie garde sa taille et ses bâtiments, mais prend la température et le bonus de position de sa nouvelle place.

### Hôte

*Faire vivre un monde avec ce qu'il a.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Jeune pousse** | clé | Sur une planète en friche, dont moins de 50 % des cases sont bâties, vos bâtiments se construisent 10 % plus vite. |  |
| 2 | **Sève montante** | 3 rangs | Vos planètes en friche produisent 15 % de plus dans leurs mines. | 3 × 5 % |
| 3 | **A · Petits mondes** | choix | Sur une planète de moins de 150 cases, vos bâtiments coûtent 15 % de moins. | |
|  | **B · Géants** |  | Sur une planète de plus de 200 cases, vos mines produisent 8 % de plus. | |
| 4 | **Longue friche** | 3 rangs | Une planète reste en friche plus longtemps : son seuil monte de 30 pts au-dessus de 50 % de ses cases bâties. | 3 × 10 pts |
| 5 | **Voisinage** | clé | Chaque planète d'un autre joueur dans le système d'une de vos planètes augmente ses mines de 1 %, jusqu'à 8 %. |  |
| 6 | **A · Foule** | choix | Chaque planète d'un autre joueur dans le système augmente vos mines de 2 %, jusqu'à 15 %. | |
|  | **B · Solitude** |  | Une planète seule dans son système, sans aucun autre joueur, produit 10 % de plus dans ses mines. | |
| 7 | **Marées** | 3 rangs | Quand plusieurs de vos planètes partagent un système, les mines de chacune produisent 9 % de plus. | 3 × 3 % |
| 8 | **Repousse** | clé | Une planète pillée produit 20 % de plus dans ses mines pendant les 6 h qui suivent. |  |
| 9 | **Friche éternelle** | ultime | 1 planète de votre choix, planète mère comprise, reste en friche pour toujours, quel que soit le nombre de cases bâties. En changer prend 7 jours. |  |

- **Jeune pousse** compte dans l'accent de vitesse des bâtiments. Une vitesse divise la durée : +10 % = durée ÷ 1,1.
- **Petits mondes** et **Géants** lisent le **total** de cases de la planète, qui grandit avec le Modulateur planétaire et les cases bonus. La planète mère démarre à 163 cases : ni petite, ni géante. Petits mondes s'ajoute aux autres réductions de prix des bâtiments.
- **Longue friche** porte le seuil de friche à 60, 70 puis 80 % des cases bâties.
- **Voisinage** compte toute planète d'un autre joueur dans le système, alliés et bots compris ; les lunes ne comptent pas. Le décompte est refait régulièrement, avec un court retard.
- **Foule** **remplace** le taux de Voisinage (2 % par voisin au lieu de 1 %, 15 % au plus au lieu de 8 %) : ils ne s'additionnent pas. **Solitude** vaut quand aucun autre joueur n'a de planète dans le système ; vos propres planètes n'empêchent rien.
- **Marées** : il suffit d'une autre de vos planètes dans le système. Le bonus ne grandit pas avec leur nombre, et il s'ajoute à Voisinage, Foule ou Solitude.
- **Repousse** ne se déclenche que si le raid a emporté des ressources. Un nouveau raid relance les 6 h.
- **Friche éternelle** : jamais une lune. La première planète désignée l'est tout de suite. En désigner une autre retire aussitôt le statut à l'ancienne, et la nouvelle ne l'obtient que 7 jours plus tard.
- Au plus, l'Hôte ajoute +47 % aux mines d'une planète (15 + 8 + 15 + 9), et +20 % de plus pendant 6 h après un raid.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| Les bonus de température (le froid pour l'hydrogène, la chaleur pour le solaire) gagnent 40 % d'amplitude | 40 % |
| Le bonus de froid du synthétiseur d'hydrogène gagne 25 % d'amplitude | 25 % |
| Le bonus de chaleur de la centrale solaire et des satellites gagne 25 % d'amplitude | 25 % |
| La part de l'énergie des satellites solaires qui vient de la température gagne 45 % d'amplitude | 45 % |
| Le bonus de position dans le système gagne 45 % d'amplitude | 45 % |
| La planète mère reçoit 50 % du bonus de position de sa place dans le système | 50 % |
| Le bonus de position des mines de métal gagne 20 % d'amplitude | 20 % |
| Le bonus de position des mines de cristal gagne 20 % d'amplitude | 20 % |
| +4 champs sur chaque planète | 2 |
| −24 % de coût du terraformeur et de la base lunaire | 24 % |
| −15 % de coût des bâtiments sur un petit monde | 15 % |

La ligne des cases se complète avec Arpenteurs de l'arbre commun (+2) : l'arbre de classe n'en donne que 2 sur les 4. Les bonus de l'Hôte, le Climatiseur, les planchers de rendement, les cases de la Base lunaire et du Modulateur sont des mécaniques bornées à ce que l'arbre donne : aucun point n'y est perdu.

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Climatologue | Thermie 15 · Hôte 10 | Les deux saisons, bonus de température +40 % sur les deux facteurs et +25 % de plus sur l'un, Climatiseur de 30 °C, Peau de lumière, La saison longue, Satellites d'altitude ; Jeune pousse, planètes en friche +15 %, petits mondes ou géants, friche jusqu'à 80 % des cases, Voisinage, Foule ou Solitude |
| Colon | Croissance 15 · Thermie 10 | Transplantation, bonus de position +45 % (+65 % sur une mine), planète mère à la moitié de son bonus, Lunes creusées, Sol vivant, Terraformeur vivant ; bonus de température **+10 %** seulement (+35 % sur un bâtiment avec le pôle), Climatiseur de 30 °C, Peau de lumière, La saison longue |
| Jardinier | Hôte 15 · Croissance 10 | Friche éternelle, planètes en friche +15 %, Voisinage, Marées, Repousse ; bonus de position +45 % (+65 % sur une mine), Terre natale, Lunes creusées, +2 cases ou Lune pleine |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Un bonus de température ne change jamais de signe** : sur une planète trop chaude pour le Condensateur d'hydrogène (facteur sous 1), Sang-froid n'ajoute rien, c'est Racines profondes qui relève le plancher. De même, sous 0 °C, les Capteurs photovoltaïques n'ont pas de bonus à élargir : seul Soleil d'hiver les aide.
- **Climatiseur planétaire tire dans les deux sens** : vers le froid, la planète gagne de l'hydrogène mais perd de l'énergie solaire ; vers le chaud, l'inverse.
- **10 points en Thermie ne donnent pas les +40 %** : Écoute du climat est en rangée 7. Sans elle, l'amplitude générale reste à 10 %.
- **Le bonus de position ne concerne que deux mines**, et ses positions dépendent du nombre de positions du système : positions 1 à 3 et 6 à 10 dans un système à 15 positions (Redline). Sur les autres positions, Racines et Marcottage n'apportent rien.
- **« En friche » n'est pas « jeune »** : une colonie est jeune pendant ses premiers jours (arbre commun) ; une planète est en friche tant que ses cases ne sont pas assez bâties. Chaque niveau construit la rapproche du seuil.
- **Foule remplace Voisinage**, elle ne s'y ajoute pas.
- **Le total de cases bouge** : un niveau de Modulateur planétaire ou Terrain gagné peut faire perdre Petits mondes (passer de 149 à 151 cases) ou gagner Géants.
- **Repousse veut un vrai butin** : un raid gagnant sur un stock vide ne déclenche rien.
- **Transplantation ne sert qu'une fois par semaine pour tout l'empire**, et la colonie déplacée change de température : son Condensateur et ses Capteurs produisent autrement.
- **Friche éternelle n'a pas de recouvrement** : en changeant de planète, l'ancienne perd le statut tout de suite et la nouvelle l'obtient 7 jours plus tard.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Classes](/fr/dynasty/classes)
- [Arbre commun](/fr/dynasty/common-tree)
- [Dynasties](/fr/dynasty/dynasties)
- [Planètes : taille, température, type](/fr/universe/planets)
- [L'énergie](/fr/economy/energy)
- [L'Énergéticien](/fr/dynasty/classes/energist)
