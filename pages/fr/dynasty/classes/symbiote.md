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
updated: "2026-10-06T10:29:52.515Z"
---

# Le Symbiote

> **En bref** : le Symbiote joue ce que les autres subissent : la température de la planète, sa place dans le système, sa taille, sa lune et ses voisins. Thermie fait de la température un atout, Croissance tire le meilleur de la position et des cases, Hôte fait produire les planètes en friche et celles qui ont des voisins.
{.is-info}

## Règles

1. Le Symbiote est une classe **exclusive à [L'Accord](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Thermie, Croissance et Hôte.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6. Le fonctionnement des points, des portes et des choix est décrit sur [Talents](/fr/dynasty/talents).
4. La production des mines, les colonies jeunes et les cases génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). La fusion, les Collecteurs solaires et le manque d'énergie relèvent de l'[Énergéticien](/fr/dynasty/classes/energist). Le Symbiote n'a qu'un accent : 2 cases de plus par planète (*Terrain gagné*), pour 4 au plus avec l'arbre commun.
5. Les règles de température et de bonus de position sur lesquelles jouent ces talents sont décrites sur [Planètes : taille, température, type](/fr/universe/planets).

## Exemple chiffré

**Condensateur d'hydrogène sur une colonie en position 15** (−85 à −45 °C)
- Sans talent, le facteur vaut 1,44 − 0,004 × (−45) = **1,62**. Le bonus de froid est la part au-dessus de 1 : 0,62.
- Avec *Sang-froid* (+10 %) : 1 + 0,62 × 1,10 = **1,68**.
- Avec *Sang-froid* et *Écoute du climat* au rang 3 (+40 %) : 1 + 0,62 × 1,40 = **1,87**.
- Avec en plus *Pôle froid* (+65 % en tout) : 1 + 0,62 × 1,65 = **2,02**.

**Les deux saisons sur une colonie en position 8** (20 à 60 °C)
- Sans talent, le Condensateur lit la température maximale : 1,44 − 0,004 × 60 = **1,20**.
- Avec l'ultime, il lit la minimale : 1,44 − 0,004 × 20 = **1,36**, soit 13 % d'hydrogène en plus.
- Avec la branche entière (+40 %) : 1,28 sans l'ultime, **1,50** avec, soit 17,5 % de plus.

**Bonus de position de l'Excavateur minéral en position 8** (+35 % sans talent)
- *Racines* : 35 × 1,15 = **+40,25 %**.
- *Racines* et *Marcottage* : 35 × 1,45 = **+50,75 %**.
- Avec en plus *Filon de métal* : 35 × 1,65 = **+57,75 %**.
- Une planète mère en position 8 avec *Terre natale* au rang 3, sans autre talent : 35 × ½ = **+17,5 %**.

**Collecteur solaire en position 8** (température maximale 60 °C)
- Sans talent : 60 / 4 + 20 = **35** énergie par Collecteur.
- *Peau de lumière* au rang 3 : 15 × 1,45 + 20 = 41,75, arrondi à **41** énergie.
- *Satellites d'altitude* : la planète est lue à 100 °C, 100 / 4 + 20 = **45** énergie.

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

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Sang-froid** | Les bonus de température de vos planètes (le froid pour le Condensateur d'hydrogène, la chaleur pour les Capteurs photovoltaïques) sont plus forts. | 1 rang | +10 % |
| 2 | **Climatiseur planétaire** | Sur chaque planète, vous décalez la température vers le froid ou vers le chaud. Réglable une fois par semaine. | 3 × 10 °C | 30 °C |
| 3 | **A · Pôle froid** ou **B · Pôle chaud** | A : le bonus de froid du Condensateur d'hydrogène est encore plus fort. <br> B : le bonus de chaleur des Capteurs photovoltaïques et des Collecteurs solaires est encore plus fort. | 1 rang | +25 % |
| 4 | **Peau de lumière** | La part de l'énergie des Collecteurs solaires qui vient de la température est plus forte. | 3 × 15 % | +45 % |
| 5 | **La saison longue** | Les Capteurs photovoltaïques produisent toujours comme au plus chaud du mois, au lieu de suivre le cycle. | 1 rang | déblocage |
| 6 | **A · Racines profondes** ou **B · Soleil d'hiver** | A : sur une planète trop chaude, le facteur du Condensateur d'hydrogène ne descend jamais sous ×1. <br> B : sur une planète froide, le facteur des Capteurs photovoltaïques ne descend jamais sous ×1,25. | 1 rang | A : ×1 <br> B : ×1,25 |
| 7 | **Écoute du climat** | Les bonus de température sont encore plus forts. | 3 × 10 % | +30 % (+40 % avec Sang-froid) |
| 8 | **Satellites d'altitude** | Vos Collecteurs solaires produisent comme si la planète était plus chaude. | 1 rang | +40 °C |
| 9 | **Les deux saisons** *(ultime)* | Votre Condensateur d'hydrogène lit la température **minimale** de la planète, et non la maximale. | 1 rang | déblocage |

La rangée 3 amplifie votre force, la rangée 6 corrige votre faiblesse : le joueur des planètes froides et celui des planètes chaudes ne font pas les mêmes choix.

### Croissance

*Le bon endroit, la bonne taille.*

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Racines** | Le bonus de position de vos planètes est plus fort. | 1 rang | +15 % |
| 2 | **Terre natale** | Votre planète mère, qui n'a jamais de bonus de position, en reçoit une part. | 3 × ⅙ | ½ |
| 3 | **A · Filon de métal** ou **B · Veine de cristal** | A : le bonus de position de l'Excavateur minéral (positions 6 à 10) est encore plus fort. <br> B : celui de l'Extracteur cristallin (positions 1 à 3) est encore plus fort. | 1 rang | +20 % |
| 4 | **Lunes creusées** | Chaque niveau de Base lunaire donne des cases en plus de ses 3, dans la limite du diamètre de la lune. | 3 × 1 case | 6 cases par niveau |
| 5 | **Marcottage** | Le bonus de position est encore plus fort. | 1 rang | +30 % (+45 % avec Racines) |
| 6 | **A · Terrain gagné** ou **B · Lune pleine** | A : chacune de vos planètes gagne 2 cases (accent). <br> B : vos lunes ne sont plus limitées par leur diamètre. | 1 rang | A : +2 cases <br> B : déblocage |
| 7 | **Sol vivant** | Le Modulateur planétaire et la Base lunaire coûtent moins cher. | 3 × 8 % | −24 % |
| 8 | **Terraformeur vivant** | Chaque niveau de Modulateur planétaire donne une case de plus, en plus de la case des niveaux pairs (Modulateur 6 : 33 → 39 cases). | 1 rang | +1 case par niveau |
| 9 | **Transplantation** *(ultime)* | Une fois par semaine, vous déplacez une colonie vers une position libre de son système, bâtiments et lune compris, si aucune flotte n'est en vol vers elle ou depuis elle. | 1 rang | 1 par semaine |

Chaque point de Croissance vaut sur les bonnes positions et rien sur les autres ; l'ultime répare un mauvais placement.

### Hôte

*Faire vivre un monde avec ce qu'il a.*

Une planète est **en friche** tant que moins de la moitié de ses cases sont bâties. C'est une notion propre au Symbiote, à ne pas confondre avec la colonie jeune de l'arbre commun.

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Jeune pousse** | Sur une planète en friche, vos bâtiments se construisent plus vite. | 1 rang | +10 % |
| 2 | **Sève montante** | Les mines de vos planètes en friche produisent davantage. | 3 × 5 % | +15 % |
| 3 | **A · Petits mondes** ou **B · Géants** | A : sur une planète de moins de 150 cases, vos bâtiments coûtent 15 % de moins. <br> B : sur une planète de plus de 200 cases, vos mines produisent 8 % de plus. | 1 rang | A : −15 % <br> B : +8 % |
| 4 | **Longue friche** | Une planète reste en friche plus longtemps : le seuil monte au-dessus de la moitié des cases bâties. | 3 × 10 pts | 80 % des cases |
| 5 | **Voisinage** | Chaque planète d'un autre joueur dans le système d'une de vos planètes augmente ses mines. | 1 rang | +1 % par voisin, 8 % au plus |
| 6 | **A · Foule** ou **B · Solitude** | A : +2 % par voisin, jusqu'à 15 %. <br> B : une planète seule dans son système, sans aucun autre joueur, produit 10 % de plus dans ses mines. | 1 rang | A : 15 % au plus <br> B : +10 % |
| 7 | **Marées** | Quand plusieurs de vos planètes partagent un système, les mines de chacune produisent davantage. | 3 × 3 % | +9 % |
| 8 | **Repousse** | Une planète pillée produit davantage dans ses mines pendant les 6 heures qui suivent. | 1 rang | +20 % pendant 6 h |
| 9 | **Friche éternelle** *(ultime)* | Une planète de votre choix, planète mère comprise, reste en friche pour toujours, quel que soit le nombre de cases bâties. En changer prend une semaine. | 1 rang | 1 planète |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Climatologue | Thermie 15 · Hôte 10 | Les deux saisons, bonus de température +40 à +65 %, Capteurs photovoltaïques au plus chaud du mois, climatiseur de 30 °C ; planètes en friche +15 %, petits mondes ou géants, friche jusqu'à 80 % des cases, Voisinage |
| Colon | Croissance 15 · Thermie 10 | Transplantation, bonus de position +45 à +65 %, planète mère à la moitié de son bonus, une case de plus par niveau de Modulateur ; bonus de température +40 %, un pôle, saison longue |
| Jardinier | Hôte 15 · Croissance 10 | Friche éternelle, planètes en friche +15 %, Voisinage, Marées, Repousse ; bonus de position +45 %, Terre natale, +2 cases ou lune pleine |

## Pièges fréquents

- **Un bonus de température ne change jamais de signe** : sur une planète trop chaude pour le Condensateur d'hydrogène (facteur sous 1), *Sang-froid* n'ajoute rien. C'est *Racines profondes* qui relève le plancher.
- **Le bonus de position ne concerne que deux mines** : l'Extracteur cristallin en positions 1 à 3, l'Excavateur minéral en positions 6 à 10. Ailleurs, Racines et Marcottage n'apportent rien.
- **« En friche » n'est pas « jeune »** : une colonie est jeune pendant ses 7 premiers jours (arbre commun) ; une planète est en friche tant que ses cases ne sont pas assez bâties.
- **Le Climatiseur ne se règle qu'une fois par semaine** par planète, et jamais sur une lune.
- **Transplantation** est refusée tant qu'une flotte est en vol vers la colonie ou depuis elle.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Classes](/fr/dynasty/classes)
- [Arbre commun](/fr/dynasty/common-tree)
- [Dynasties](/fr/dynasty/dynasties)
- [Planètes : taille, température, type](/fr/universe/planets)
- [L'énergie](/fr/economy/energy)
- [L'Énergéticien](/fr/dynasty/classes/energist)
