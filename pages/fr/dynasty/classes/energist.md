---
wiki_id: 154
locale: "fr"
path: "dynasty/classes/energist"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/energist"
title: "L'Énergéticien"
description: "Arbre de classe de l'Énergéticien : Surrégime, Centrales, Continuité."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:42.744Z"
updated: "2026-10-06T10:29:43.975Z"
---

# L'Énergéticien

> **En bref** : pour l'Énergéticien, l'énergie n'est jamais perdue. Son surplus devient du minerai, son manque ne bloque plus rien, et ses centrales coûtent moins que celles des autres. Classe commune à toutes les dynasties. Ses trois branches : **Surrégime**, **Centrales** et **Continuité**.
{.is-info}

*« Le pouls. »* Le maître de l'énergie : un seul levier qui fait tourner vos trois mines à la fois.

## Règles

1. L'arbre de l'Énergéticien suit les règles de tout [arbre de classe](/fr/dynasty/talents) : 3 branches de 9 rangées, 15 points par branche, 25 points au maximum.
2. Le bonus générique d'énergie (+8 % sur toutes les centrales et les Collecteurs solaires) vient de l'[arbre commun](/fr/dynasty/common-tree), branche Prospérité. L'Énergéticien n'a que des **mécaniques**, et un seul accent : la vitesse de construction des Capteurs photovoltaïques et du Réacteur thermonucléaire (10 %).
3. Il n'a **aucun bonus de combat**. C'est la seule classe qui joue sur le manque d'énergie, le Réacteur thermonucléaire et les Collecteurs solaires.
4. **Surrégime** : une mine peut tourner au-dessus de son plein régime, en consommant plus d'énergie. Le rendement s'arrête à **125 %** (Pointe et Surchauffe comprises), et à **140 %** sur une seule mine avec Cœur d'étoile.
5. **Électrolyse** ne transforme que l'énergie que rien n'utilise : le surrégime se sert d'abord, l'électrolyse prend le reste. Il faut toujours au moins 3 d'énergie pour 1 d'hydrogène.

## Exemple chiffré

Un Excavateur minéral au niveau 20 produit **4 036 métal par heure** et consomme **1 345 d'énergie** (voir [L'énergie](/fr/economy/energy)).

- **Surrégime** (110 %, +25 % d'énergie) : 4 036 × 1,1 = **4 440 métal par heure**, pour 1 345 × 0,25 = **336 d'énergie** de plus.
- Avec **Régulation fine** au rang 3 (surcoût ramené à 13 %) : la même mine ne demande plus que **175 d'énergie** de plus.
- Avec **Pointe** et **Surchauffe** au rang 3 (125 %) : 4 036 × 1,25 = **5 045 métal par heure**.
- **Électrolyse** : 1 000 d'énergie inutilisée donnent **250 hydrogène par heure** (333 avec Électrolyse poussée).
- **Délestage** au rang 3 : avec 80 % d'énergie, il manque 20 points ; vos mines en ignorent 30 %, soit 6 points, et tournent à **86 %**. L'Excavateur produit 3 471 métal par heure au lieu de 3 229.
- **Fusion à froid** sur un Réacteur thermonucléaire 10 (Science Énergétique 3) : **259 hydrogène par heure** économisés, soit 6 216 par jour.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["CONTINUITÉ<br/>Jamais en panne."]:::head
        B3R1{{"Report de charge<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Délestage<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Délestage d'urgence<br/>1 pt"]:::option
        B3R3B["② Mise en route<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Réserve tournante<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Priorité de charge<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Accumulateurs<br/>1 pt"]:::option
        B3R6B["② Allumage rapide<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Transformateurs<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Éruption<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Réseau interplanétaire<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["CENTRALES<br/>L'énergie la moins chère de la galaxie."]:::head
        B2R1{{"La nuit est courte<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Voilure<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Plein soleil<br/>1 pt"]:::option
        B2R3B["② Cœur froid<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Plein midi<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Surgénérateur<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Veille froide<br/>1 pt"]:::option
        B2R6B["② Essaim<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Ateliers orbitaux<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Lancement en grappe<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Fusion à froid<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["SURRÉGIME<br/>Chaque watt en trop devient du minerai."]:::head
        B1R1{{"Surrégime<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Régulation fine<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Pointe<br/>1 pt"]:::option
        B1R3B["② Surrégime large<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Surchauffe<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Électrolyse<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Électrolyse poussée<br/>1 pt"]:::option
        B1R6B["② Échangeur<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Câbles supraconducteurs<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Disjoncteur<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Cœur d'étoile<br/>ultime"]]:::ultimate
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

### Surrégime : « Chaque watt en trop devient du minerai. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Surrégime** | Sur chaque base, une mine peut tourner au-dessus de son plein régime, pour plus d'énergie consommée. | 110 %, +25 % d'énergie, 1 mine |
| 2 | 3 rangs | **Régulation fine** | Le surcoût d'énergie du surrégime baisse. | −4 points par rang (+13 %) |
| 3 | choix | **A : Pointe** / **B : Surrégime large** | A : le surrégime gagne du rendement, sans énergie en plus. <br> B : jusqu'à 3 mines en surrégime sur chaque base. | +6 points / 3 mines |
| 4 | 3 rangs | **Surchauffe** | Le surrégime gagne encore du rendement, sans énergie en plus. | +3 points par rang (119 %, 125 % avec Pointe) |
| 5 | clé | **Électrolyse** | L'énergie que rien n'utilise devient de l'hydrogène. Le surrégime se sert d'abord. | 4 d'énergie pour 1 hydrogène |
| 6 | choix | **A : Électrolyse poussée** / **B : Échangeur** | A : il faut moins d'énergie pour une unité d'hydrogène. <br> B : sur chaque base, l'électrolyse peut donner du métal ou du cristal à la place. | 3 d'énergie pour 1 / 3 métal ou 2 cristal pour 1 hydrogène |
| 7 | 3 rangs | **Câbles supraconducteurs** | Vos mines consomment moins d'énergie. | −3 % par rang (−9 %) |
| 8 | clé | **Disjoncteur** | Quand l'énergie vient à manquer, le surrégime recule de lui-même avant que la base ne tombe en déficit, puis revient dès qu'il le peut. | déblocage |
| 9 | ultime | **Cœur d'étoile** | Sur chaque base, la mine de votre choix peut dépasser le surrégime. Chaque tranche de 5 points au-delà coûte plus d'énergie. | jusqu'à 140 %, +20 % d'énergie par tranche |

### Centrales : « L'énergie la moins chère de la galaxie. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **La nuit est courte** | Après une défense, une part de vos Collecteurs solaires détruits est relevée gratuitement, sur la part qui ne part pas en débris. Avec 30 % de débris, 70 % des Collecteurs détruits restent, et 49 % de ceux-là reviennent : 100 détruits → 34 relevés. | 49 % |
| 2 | 3 rangs | **Voilure** | Vos Collecteurs solaires produisent plus d'énergie. | +5 % par rang (15 %) |
| 3 | choix | **A : Plein soleil** / **B : Cœur froid** | A : vos Capteurs photovoltaïques produisent plus d'énergie. <br> B : votre Réacteur thermonucléaire brûle moins d'hydrogène. | +10 % / −20 % |
| 4 | 3 rangs | **Plein midi** | Vos Capteurs photovoltaïques lisent une température rapprochée du maximum du mois. | 15 % par rang (45 %) |
| 5 | clé | **Surgénérateur** | Votre Réacteur thermonucléaire compte la Science Énergétique avec un niveau de plus. | +1 niveau |
| 6 | choix | **A : Veille froide** / **B : Essaim** | A : le Réacteur thermonucléaire se règle comme une mine, de l'arrêt au plein régime, et brûle d'autant moins d'hydrogène. <br> B : vos Collecteurs solaires coûtent moins cher. | réglage / −20 % |
| 7 | 3 rangs | **Ateliers orbitaux** | La nuit est courte relève plus de Collecteurs détruits. | +7 points par rang (70 %) |
| 8 | clé | **Lancement en grappe** | Vos Collecteurs solaires se construisent sur leur propre file, à côté du Dock orbital, qui reste libre pour vos vaisseaux. | déblocage |
| 9 | ultime | **Fusion à froid** | Sur la base de votre choix, le Réacteur thermonucléaire ne brûle plus d'hydrogène. | 1 base |

### Continuité : « Jamais en panne. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Report de charge** | Un niveau de mine qui s'achève ne tire sa nouvelle consommation que plus tard : le temps de monter la centrale qui va avec. | 4 h |
| 2 | 3 rangs | **Délestage** | Vos mines ignorent une part du manque d'énergie. | 10 % par rang (30 %) |
| 3 | choix | **A : Délestage d'urgence** / **B : Mise en route** | A : vos mines ignorent encore plus du manque d'énergie. <br> B : sur une colonie de moins de 7 jours, vos mines ignorent tout le manque d'énergie. | +10 % (40 %) / colonies de moins de 7 jours |
| 4 | 3 rangs | **Réserve tournante** | Le Report de charge dure plus longtemps. | +2 h par rang (10 h) |
| 5 | clé | **Priorité de charge** | Sur chaque base, la mine de votre choix est servie en premier quand l'énergie manque ; les autres se partagent le reste. | déblocage |
| 6 | choix | **A : Accumulateurs** / **B : Allumage rapide** | A : votre surplus d'énergie se stocke et couvre seul un déficit. <br> B : vos Capteurs photovoltaïques et Réacteurs thermonucléaires se construisent plus vite (accent). | jusqu'à 12 h de surplus / +10 % |
| 7 | 3 rangs | **Transformateurs** | Le délestage peut rattraper plus de points d'énergie, en plus des 15 qu'il rattrape déjà. | +5 points par rang (30 points) |
| 8 | clé | **Éruption** | Une fois par jour, sur la base de votre choix, Capteurs photovoltaïques et Collecteurs solaires produisent plus d'énergie pendant 4 h. | ×1,5 pendant 4 h |
| 9 | ultime | **Réseau interplanétaire** | Le surplus de vos planètes alimente celles qui manquent d'énergie, jusqu'à une part de leur consommation. | 20 % |

### Ce que 25 points donnent

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur à excédent | Surrégime 15 · Centrales 10 | trois mines à 119 % ou une à 125 %, une mine jusqu'à 140 % avec Cœur d'étoile, électrolyse du reste ; Capteurs plus forts ou Réacteur qui brûle 20 % de moins, et le Surgénérateur |
| Grimpeur | Continuité 15 · Surrégime 10 | plus de déficit : report de 10 h, priorité de charge, Éruption, puis réseau entre planètes ; surrégime et électrolyse pour ne rien perdre |
| Seigneur des Collecteurs | Centrales 15 · Continuité 10 | Collecteurs relevés à 70 %, construits sur leur propre file et 20 % moins chers, une base dont le Réacteur ne brûle rien ; report de charge et priorité de charge |

## Pièges fréquents

- **Le surrégime se paie toujours en énergie** : sans surplus, il fait tomber la base en déficit et ralentit les trois mines. Disjoncteur évite ce piège.
- **L'électrolyse ne crée rien à partir d'une énergie déjà utilisée** : passez d'abord vos mines en surrégime, convertissez ensuite ce qui reste.
- **Aucun talent de Continuité ne produit de minerai** : la branche retire le frein qui empêche de monter une mine avant sa centrale.
- **La rangée 3 des Centrales décide de votre énergie** : les Capteurs photovoltaïques ne coûtent rien mais dépendent de la température de la planète ; le Réacteur brûle de l'hydrogène mais monte avec la Science Énergétique.

## Pages liées

- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [L'énergie](/fr/economy/energy)
- [Planètes : taille, température, type](/fr/universe/planets)
