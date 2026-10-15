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
updated: "2026-10-07T22:08:23.088Z"
---

# L'Énergéticien

> **En bref** : pour l'Énergéticien, l'énergie n'est jamais perdue. Surrégime pousse les mines au-delà de leur plein régime et convertit le surplus en hydrogène ; Centrales rend les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires plus forts et moins chers à faire tourner ; Continuité empêche un manque d'énergie de freiner les mines.
{.is-info}

## Règles

1. L'Énergéticien est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Surrégime, Centrales et Continuité.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. Le bonus générique d'énergie, +8 % sur les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires (Réseau optimisé), vient de l'[arbre commun](/fr/dynasty/common-tree). L'Énergéticien n'a que des **mécaniques**, et un seul accent : la vitesse de construction des Capteurs photovoltaïques et du Réacteur thermonucléaire (Allumage rapide, 10 %).
5. Le surplus de production d'une mine en surrégime se calcule sur sa **production propre**, à côté de la Maîtrise du Plasma et des bonus de production, sans être multiplié par eux et hors du plafond de production des mines. Le manque d'énergie freine ensuite toute la production de la base ; l'électrolyse convertit enfin l'énergie restée inutilisée.
6. **Surrégime** : une mine réglée à 100 % tourne à 110 %. Pointe et Surchauffe montent ce taux à **131 %** sur une mine par base ; Surrégime large permet trois mines par base, à 119 % au plus. Cœur d'étoile porte une mine désignée par base à 140 %.
7. **Délestage** : en déficit, chaque mine récupère une part des points de rendement qui lui manquent, **15 points au plus** (30 avec Transformateurs).

## Exemple chiffré

Univers à vitesse 1. Un Excavateur minéral niveau 20 produit **4 036 métal par heure** et consomme **1 345 d'énergie** (voir [L'énergie](/fr/economy/energy)).

**Surrégime complet**
- Câbles supraconducteurs au rang 3 : 1 345 × 0,91 = **1 223** d'énergie (arrondi inférieur).
- Surrégime, Pointe et Surchauffe au rang 3 (131 %) : 4 036 + 4 036 × 31 % = 4 036 + 1 251 = **5 287 métal par heure**.
- Avec Régulation fine au rang 3, le surcoût passe de 25 % à 13 % : 1 223 × 1,13 = **1 381** d'énergie, à peine 36 de plus que la mine sans aucun talent.
- Cœur d'étoile sur cette mine (140 %) : 4 036 + 1 614 = **5 650 métal par heure**. Les 9 points au-delà de 131 % coûtent 4 % chacun : surcoût 13 + 36 = 49 %, soit 1 223 × 1,49 = **1 822** d'énergie.

**Délestage, base à 50 % d'énergie**
- Avec Délestage au rang 3 et Délestage d'urgence (40 %), il manque 50 points ; 40 % de 50 = 20, ramenés à 15 : les mines tournent à **65 %**. Avec Transformateurs au rang 3 (30 points au plus) : **70 %**.
- L'Excavateur 20 produit alors 2 623 puis **2 825 métal par heure**, au lieu de 2 018.

**Réacteur thermonucléaire niveau 10, Science Énergétique 3**
- Production : 30 × 10 × 1,08^10 = 647 d'énergie. Avec Surgénérateur (Science Énergétique comptée au niveau 4) : 30 × 10 × 1,09^10 = **710**, puis **766** avec Réseau optimisé (+8 %).
- Il brûle 10 × 10 × 1,1^10 = **259 hydrogène par heure**, 207 avec Cœur froid, **0** sur la base de Fusion à froid : 6 216 hydrogène économisés par jour.

**Collecteurs solaires, planète à 60 °C de température maximale**
- 100 Collecteurs : 100 × (60 / 4 + 20) = 3 500 d'énergie. Voilure au rang 3 et Réseau optimisé (+23 %) : **4 305**. Pendant une Éruption : 4 305 × 1,5 = **6 457**.
- Une défense en détruit 100, sans Station de réparation : **49** restent sur la base avec La nuit est courte, **70** avec Ateliers orbitaux au rang 3.

**Électrolyse**
- 1 000 d'énergie inutilisée donnent **250 hydrogène par heure** avec Électrolyse, **333** avec Électrolyse poussée, à condition que le Condensateur d'hydrogène de la base produise au moins 84 (ou 111) hydrogène par heure : l'électrolyse ne dépasse jamais 3 fois sa production.

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

### Surrégime

*Chaque watt en trop devient du minerai.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Surrégime** | clé | Vos mines peuvent tourner à 110 % de leur plein régime, pour 25 % d'énergie consommée en plus : 1 par base. |  |
| 2 | **Régulation fine** | 3 rangs | Le surcoût d'énergie du surrégime baisse de 12 points. | 3 × 4 pts |
| 3 | **A · Pointe** | choix | Le surrégime gagne 12 points de rendement, sans énergie en plus. | |
|  | **B · Surrégime large** |  | Vous pouvez passer jusqu'à 3 mines en surrégime sur chaque base. | |
| 4 | **Surchauffe** | 3 rangs | Le surrégime gagne encore 9 points de rendement, sans énergie en plus. | 3 × 3 pts |
| 5 | **Électrolyse** | clé | L'énergie que rien n'utilise n'est plus perdue : elle devient de l'hydrogène, à raison de 4 d'énergie par unité, jusqu'à trois fois ce que produit la mine de cette ressource sur la base. Le surrégime se sert d'abord. |  |
| 6 | **A · Électrolyse poussée** | choix | Il ne faut plus que 3 d'énergie inutilisée pour une unité d'hydrogène. | |
|  | **B · Échangeur** |  | Sur chaque base, l'électrolyse peut donner du métal ou du cristal à la place : 3 de métal ou 2 de cristal pour ce qui aurait fait 1 d'hydrogène, toujours plafonné par la mine de métal ou de cristal de la base. | |
| 7 | **Câbles supraconducteurs** | 3 rangs | Vos mines consomment 9 % d'énergie en moins. | 3 × 3 % |
| 8 | **Disjoncteur** | clé | Quand l'énergie vient à manquer, le surrégime recule de lui-même avant que la base ne tombe en déficit, puis revient dès qu'il le peut. |  |
| 9 | **Cœur d'étoile** | ultime | Sur chaque base, la mine de votre choix peut dépasser le surrégime jusqu'à 140 % de son plein régime. Chaque tranche de 5 points au-delà coûte 20 % d'énergie en plus. |  |

- **Surrégime** : seule une mine réglée à 100 % peut passer en surrégime ; baisser son taux l'arrête. Le surcoût d'énergie s'applique sur la consommation déjà réduite par Câbles supraconducteurs.
- **Électrolyse** : l'énergie restée inutilisée une fois tout servi, surrégime compris. Par heure, l'électrolyse ne donne jamais plus de 3 fois ce que produit le Condensateur d'hydrogène de la base : pas de Condensateur, pas d'hydrogène. Elle s'arrête tant que la réserve de Accumulateurs se remplit.
- **Échangeur** se choisit base par base ; il exclut Électrolyse poussée, donc il faut 4 d'énergie pour 3 métal ou 2 cristal. Le plafond est alors 3 fois la production de l'Excavateur minéral ou de l'Extracteur cristallin de la base.
- **Disjoncteur** : si le surrégime devait faire passer la base en déficit, tout le surrégime de la base (Cœur d'étoile compris) recule de la même part, juste assez pour garder l'énergie à l'équilibre ; il revient seul quand l'énergie le permet.
- **Cœur d'étoile** : la mine désignée doit être en surrégime. Chaque point au-delà du taux de surrégime coûte 4 % d'énergie (20 % par tranche de 5 points), ajoutés au surcoût du surrégime : 36 % depuis 131 %, 84 % depuis 119 %.

### Centrales

*L'énergie la moins chère de la galaxie.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **La nuit est courte** | clé | Après une défense, 49 % de vos satellites solaires détruits sont relevés gratuitement, sur la part qui ne part pas en débris. |  |
| 2 | **Voilure** | 3 rangs | Vos satellites solaires produisent 15 % d'énergie en plus. | 3 × 5 % |
| 3 | **A · Plein soleil** | choix | Vos centrales solaires produisent 10 % d'énergie en plus. | |
|  | **B · Cœur froid** |  | Votre centrale à fusion brûle 20 % d'hydrogène en moins. | |
| 4 | **Plein midi** | 3 rangs | Votre centrale solaire lit une température rapprochée de 45 % du maximum du mois. | 3 × 15 % |
| 5 | **Surgénérateur** | clé | Votre centrale à fusion compte la science de l'énergie avec 1 niveau de plus. |  |
| 6 | **A · Veille froide** | choix | Votre centrale à fusion se règle comme une mine, de l'arrêt au plein régime, et brûle d'autant moins d'hydrogène. | |
|  | **B · Essaim** |  | Vos satellites solaires coûtent 20 % de moins. | |
| 7 | **Ateliers orbitaux** | 3 rangs | La nuit est courte relève 21 points de plus de vos satellites détruits. | 3 × 7 pts |
| 8 | **Lancement en grappe** | clé | Vos satellites solaires se construisent sur leur propre file, à côté du chantier spatial : il reste libre pour vos vaisseaux pendant qu'une grappe se monte. |  |
| 9 | **Fusion à froid** | ultime | Sur la base de votre choix, la centrale à fusion ne brûle plus d'hydrogène. |  |

- **La nuit est courte** : après un combat où la base perd des Collecteurs solaires, 49 % des Collecteurs détruits (arrondi inférieur) restent aussitôt sur la base. Ceux que la Station de réparation a déjà pris en charge sont décomptés : vous récupérez le plus grand des deux nombres. Le champ de débris est calculé sur toutes les pertes.
- **Voilure**, **Plein soleil** : ces pourcentages s'ajoutent aux 8 % de Réseau optimisé (23 % pour les Collecteurs, 18 % pour les Capteurs).
- **Plein midi** : les Capteurs lisent la température du jour plus 45 % de l'écart jusqu'au maximum du mois. Les Capteurs ne gagnent rien sous 0 °C : sur une planète froide, le nœud ne change rien.
- **Veille froide** : sans ce nœud, le Réacteur tourne toujours à 100 %, quel que soit son réglage. Avec lui, son énergie et sa consommation d'hydrogène suivent le taux choisi.
- **Essaim** s'applique en plus du plafond de 5 % des réductions de coût.
- **Lancement en grappe** : les Collecteurs bâtis sur leur propre file ne puisent pas dans l'avance du Dock orbital d'un Bâtisseur.
- **Fusion à froid** : vous désignez la base, et pouvez en changer.

### Continuité

*Jamais en panne.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Report de charge** | clé | Un niveau de mine qui s'achève ne tire sa nouvelle consommation que 4 h plus tard : le temps de monter la centrale qui va avec. |  |
| 2 | **Délestage** | 3 rangs | Vos mines ignorent 30 % du manque d'énergie. | 3 × 10 % |
| 3 | **A · Délestage d'urgence** | choix | Vos mines ignorent encore 10 % du manque d'énergie. | |
|  | **B · Mise en route** |  | Sur une colonie de moins de 30 jours, vos mines ignorent tout le manque d'énergie : montez-les avant la première centrale. | |
| 4 | **Réserve tournante** | 3 rangs | Le Report de charge dure 6 h de plus. | 3 × 2 h |
| 5 | **Priorité de charge** | clé | Sur chaque base, la mine de votre choix est servie en premier quand l'énergie manque ; les autres se partagent le reste. |  |
| 6 | **A · Accumulateurs** | choix | Votre surplus d'énergie se stocke, jusqu'à 12 h de surplus, et couvre seul un déficit. | |
|  | **B · Allumage rapide** |  | Vos centrales solaires et à fusion se construisent 10 % plus vite. | |
| 7 | **Transformateurs** | 3 rangs | Le délestage peut rattraper 15 points d'énergie de plus, en plus des 15 qu'il rattrape déjà. | 3 × 5 pts |
| 8 | **Éruption** | clé | Une fois par jour, sur la base de votre choix, centrales solaires et satellites produisent une fois et demie plus d'énergie pendant 4 h. |  |
| 9 | **Réseau interplanétaire** | ultime | Le surplus de vos planètes alimente celles qui manquent d'énergie, jusqu'à 20 % de leur consommation. |  |

- **Report de charge** : le niveau qui s'achève produit aussitôt ; seule sa consommation attend, celle du niveau précédent restant en vigueur pendant le délai.
- **Mise en route** : sur une colonie fondée par un Pionnier spatial depuis moins de 30 jours, pas sur la planète mère.
- **Priorité de charge** : la mine désignée tourne à plein tant que la production d'énergie couvre **sa** consommation ; les autres se partagent le reste, avec leur délestage.
- **Accumulateurs** : la base garde au plus 12 heures de son surplus du moment. En déficit, la réserve couvre tout le manque, les mines tournant à plein, jusqu'à épuisement.
- **Éruption** : sur une base qui a des Capteurs photovoltaïques ou des Collecteurs solaires, 24 h après la précédente, pour tout votre empire.
- **Réseau interplanétaire** : chaque planète en déficit reçoit au plus le plus petit de son manque et de 20 % de sa consommation, dans la limite du surplus des autres, partagé à proportion. Les lunes n'y prennent pas part. Le partage se refait régulièrement.
- **Éruption** et **Réseau interplanétaire** ne comptent pas pour l'énergie qu'exige une recherche comme Manipulation Gravitationnelle.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| −12 pts de surcoût d'énergie du surrégime | 12 pts |
| −9 % d'énergie consommée par les mines | 9 % |
| +15 % d'énergie des satellites solaires | 15 % |
| +10 % d'énergie des centrales solaires | 10 % |
| −20 % de consommation d'hydrogène de la centrale à fusion | 20 % |
| La centrale solaire lit une température du jour rapprochée de 45 % de l'écart qui la sépare du maximum du mois | 45 % |
| La centrale à fusion lit la science de l'énergie comme si elle avait +1 niveau | 1 |
| −20 % de coût des satellites solaires | 20 % |
| Un niveau de mine qui s'achève ne tire sa nouvelle consommation d'énergie que 10 h plus tard | 10 h |
| Les trois mines ignorent 40 % de plus de l'étranglement énergétique | 40 % |
| +10 % de vitesse de construction des centrales solaires et à fusion | 10 % |
| Le délestage peut rattraper 15 pts d'énergie de plus | 15 pts |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur à excédent | Surrégime 15 · Centrales 10 | une mine à 131 % ou trois à 119 % par base, surcoût de 13 %, électrolyse, mines −9 % d'énergie, Disjoncteur, une mine jusqu'à 140 % avec Cœur d'étoile ; Collecteurs +15 %, Plein soleil ou Cœur froid, Plein midi, Surgénérateur |
| Grimpeur | Continuité 15 · Surrégime 10 | report de 10 h, délestage jusqu'à 30 points (40 % du manque), Priorité de charge, Éruption, Réseau interplanétaire ; une mine à 131 % ou trois à 119 %, électrolyse |
| Seigneur des Collecteurs | Centrales 15 · Continuité 10 | Collecteurs relevés à 70 %, Lancement en grappe, Essaim −20 %, Fusion à froid sur une base ; report de 10 h, délestage, Priorité de charge |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Le surrégime se paie toujours en énergie** : sans surplus, il fait passer la base en déficit et freine les trois mines. Disjoncteur le fait reculer à temps.
- **Une mine en surrégime doit rester à 100 %** : baisser son taux arrête le surrégime.
- **L'électrolyse ne crée rien à partir d'une énergie déjà utilisée**, ni sans Condensateur d'hydrogène sur la base, ni tant que la réserve de Accumulateurs se remplit.
- **Le délestage est borné** : en déficit profond, il ne rend que 15 points de rendement (30 avec Transformateurs).
- **Aucun talent de Continuité ne produit de minerai** : la branche retire le frein qui empêche de monter une mine avant sa centrale.
- **La rangée 3 des Centrales décide de votre énergie** : les Capteurs photovoltaïques ne brûlent rien mais dépendent de la température, et Plein midi ne sert à rien sur une planète froide ; le Réacteur brûle de l'hydrogène mais monte avec la Science Énergétique.
- **Éruption et Réseau interplanétaire ne débloquent pas Manipulation Gravitationnelle** : l'énergie qu'elle exige se lit sans eux.

## Pages liées

- [Les talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [L'énergie](/fr/economy/energy)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Station de réparation](/fr/economy/repair-station)
