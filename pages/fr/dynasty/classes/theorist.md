---
wiki_id: 159
locale: "fr"
path: "dynasty/classes/theorist"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/theorist"
title: "Le Théoricien"
description: "Arbre de classe du Théoricien : Méthode, Réseau, Prototypes."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:53.373Z"
updated: "2026-10-21T16:00:47.301Z"
---

# Le Théoricien

> **En bref** : « Comprendre avant ». Le Théoricien a toujours une étude en cours et un niveau d'avance. Méthode fait que sa file de recherche ne s'arrête jamais, Réseau met en commun les Centres d'innovation de ses colonies, Prototypes lui fait profiter d'un niveau de recherche avant tout le monde.
{.is-info}

## Règles

1. Le Théoricien est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Méthode, Réseau et Prototypes.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. La vitesse de recherche générique et la seconde étude en parallèle (Second centre d'innovation) sont dans l'[arbre commun](/fr/dynasty/common-tree). L'arbre du Théoricien ne contient que des mécaniques qui lui sont propres. Ses deux **accents** sont la vitesse de construction des Centres d'innovation (Paillasses en kit) et le coût des niveaux de recherche à partir du 11e (Brevets).
5. **Avances au départ.** Une étude peut partir avec une partie de son temps déjà écoulée. Fil continu ou Départ lancé, plus Veille de nuit et Partage des résultats, ne dépassent jamais **10 %** de l'étude à eux tous. Symposium, Brouillon conservé et l'Élan de l'Archiviste s'ajoutent au-delà. Aucune avance n'achève une étude.
6. **Réseau d'étude.** Sans talent, [Collaboration Stellaire](/fr/research/stellar-collaboration) niveau N met en commun les N meilleurs Centres d'innovation de vos autres planètes, s'ils sont au moins aussi avancés que celui qui étudie. Le réseau raccourcit l'étude, jamais son coût.
7. **Prototype.** Un prototype fait valoir une recherche des niveaux de plus pendant un temps, partout où le jeu lit son niveau (emplacements de flotte, nombre de planètes, Centres du réseau, combat...), sans dépasser son niveau maximum. Il ne s'applique qu'à une recherche étudiée au moins une fois. Les trois **technologies de combat** (Systèmes Offensifs, Champs de Protection, Métallurgie Avancée) n'ont de prototype d'étude qu'avec Prototype de combat.
8. Prototype, Spécialité et Révolution **ne s'additionnent pas** sur une même recherche : elle prend le plus grand des trois bonus.
9. Les réductions de coût des recherches (Protocoles, Brevets, Ingénierie inverse) s'additionnent, puis chaque ressource est arrondie à l'unité supérieure. Elles ne raccourcissent pas l'étude, dont la durée se calcule sur le prix normal.

## Exemple chiffré

Étude de référence : **Systèmes Offensifs 10** (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 sur la planète qui étudie : 512 000 / (1 000 × 11) h = **46 h 32 min 44 s**.

**Méthode**
- Fil continu : l'étude, lancée à la suite de la précédente dans la file, part avec 10 % de son temps écoulé : il reste **41 h 53 min 28 s**.
- Lancée à la main après 10 h de file vide, avec Départ lancé au rang 3 et Veille de nuit : 9 % (4 h 11 min 20 s) plus 2 h mises de côté donnent 6 h 11 min 20 s, ramenés au plafond de 10 % : **4 h 39 min 16 s**. Veille de nuit n'a ajouté que 27 min 56 s.
- Éclair de génie : un clic avance l'étude de 10 % de son temps total, **4 h 39 min 16 s**. Avec Coup de génie au rang 3 (19 %), on obtiendrait 8 h 50 min, ramenés au maximum de **6 h**.
- Protocoles au rang 3 (−18 %) : 409 600 → **335 872** métal, 102 400 → **83 968** cristal.

**Réseau** : Centre 10 qui étudie, trois colonies avec des Centres 10, 9 et 8, Collaboration Stellaire 3.
- Sans talent, seul le Centre 10 de colonie entre : niveau effectif 10 + 10 = 20, **24 h 22 min 51 s**.
- Liaison montante : les Centres 9 et 8 entrent aussi, niveau effectif 37, **13 h 28 min 25 s**.
- Labos de campagne au rang 3 : chacun des trois Centres de colonie compte 3 niveaux de plus, niveau effectif 46, **10 h 53 min 37 s**. Avec Labo-mère en plus, 49 : **10 h 14 min 24 s**.
- Bourses d'étude au rang 3 : l'étude achevée rend 9 % de ce qu'elle a coûté, soit **36 864** métal et **9 216** cristal sur un prix de 512 000.
- Symposium (4 Centres ou plus) : 20 % de plus au départ. Une étude enchaînée part alors avec 10 % + 20 % = **13 h 57 min 48 s** déjà faits.

**Centre d'innovation jumeau** : une seconde étude de 10 h prend **12 h 30 min** avec Second centre d'innovation et l'ultime (80 %), 20 h avec Second centre d'innovation seul (50 %), **25 h** avec l'ultime seul (40 %).

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["PROTOTYPES<br/>Un niveau d'avance sur tout le monde."]:::head
        B3R1{{"Prototype<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Essais prolongés<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Prototype de combat<br/>1 pt"]:::option
        B3R3B["② Feu vert<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Ingénierie inverse<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Double prototype<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Brevets<br/>1 pt"]:::option
        B3R6B["② Banc d'essai<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Retombées<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Spécialité<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Révolution<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["RÉSEAU<br/>Chaque colonie est un centre d'innovation."]:::head
        B2R1{{"Liaison montante<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Labos de campagne<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Antenne lointaine<br/>1 pt"]:::option
        B2R3B["② Labo-mère<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Paillasses en kit<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Un labo de plus<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Réseau vivant<br/>1 pt"]:::option
        B2R6B["② Partage des résultats<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Bourses d'étude<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Échange universitaire<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Symposium<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["MÉTHODE<br/>Une étude n'attend jamais."]:::head
        B1R1{{"Fil continu<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Départ lancé<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Veille de nuit<br/>1 pt"]:::option
        B1R3B["② Brouillon conservé<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Protocoles<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Éclair de génie<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Esprit vif<br/>1 pt"]:::option
        B1R6B["② Réflexe<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Coup de génie<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Inspiration<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Centre d'innovation jumeau<br/>ultime"]]:::ultimate
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

### Méthode

*Une étude n'attend jamais.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Fil continu** | clé | Une étude qui démarre d'elle-même, à la suite de la précédente dans la file, part avec 10 % de son temps déjà écoulé. |  |
| 2 | **Départ lancé** | 3 rangs | Une étude lancée à la main sur une file de recherche vide part avec 9 % de son temps déjà écoulé, sans dépasser le plafond de 10 % des avances. | 3 × 3 % |
| 3 | **A · Veille de nuit** | choix | Quand votre file de recherche est vide, le centre d'innovation met de côté 25 % du temps qui passe, jusqu'à 2 h d'avance versées à la prochaine étude. | |
|  | **B · Brouillon conservé** |  | Une étude annulée garde sa progression : relancée plus tard au même niveau, elle reprend où elle s'était arrêtée. | |
| 4 | **Protocoles** | 3 rangs | Vos recherches coûtent 18 % de moins. | 3 × 6 % |
| 5 | **Éclair de génie** | clé | Une fois par jour, d'un bouton, l'étude en cours avance d'un coup de 10 % de son temps total, 6 h au plus, sans jamais l'achever. |  |
| 6 | **A · Esprit vif** | choix | L'Éclair de génie se recharge en 16 h. | |
|  | **B · Réflexe** |  | L'Éclair de génie part tout seul dès qu'il est prêt et qu'une étude tourne, même sans vous connecter. | |
| 7 | **Coup de génie** | 3 rangs | L'Éclair de génie avance l'étude de 9 % de plus. | 3 × 3 % |
| 8 | **Inspiration** | clé | Chaque étude achevée fait revenir l'Éclair de génie plus tôt, de 20 % de sa durée. |  |
| 9 | **Centre d'innovation jumeau** | ultime | Votre seconde recherche (Second centre d'innovation) avance à 80 % de la vitesse normale. Sans le Second centre d'innovation, vous en menez quand même une seconde, à 40 %. |  |

- **Fil continu** ne vaut que pour une étude qui démarre d'elle-même derrière la précédente ; **Départ lancé** que pour une étude lancée à la main sur une file vide. Ni l'un ni l'autre ne joue dans le second centre d'innovation.
- **Veille de nuit** compte le temps depuis la fin (achevée ou annulée) de la dernière étude, et ne sert qu'à une étude lancée à la main. Comme Départ lancé occupe déjà 9 % des 10 %, il ajoute au plus 1 % de l'étude.
- **Brouillon conservé** : seule une étude en cours peut être annulée avec sa progression. Elle la retrouve si vous relancez le même niveau de la même recherche, au-delà du plafond de 10 %. Un brouillon par recherche, le dernier.
- **Éclair de génie** : 6 h au plus, même avec Coup de génie, qui n'apporte donc rien au-delà de 31 h 35 min d'étude. La recharge se compte depuis l'usage, pour tout l'empire. Si l'avance achevait l'étude, le bouton est refusé et reste disponible ; Réflexe attend lui aussi une étude assez longue.
- **Inspiration** raccourcit la recharge de 20 % de la durée de chaque étude achevée, seulement pendant que l'Éclair recharge.
- **Centre d'innovation jumeau** : la seconde étude doit porter sur une autre recherche, et rien ne doit attendre dans la file. Elle ne reçoit ni Fil continu, ni Départ lancé, ni Veille de nuit, ni Partage des résultats.

### Réseau

*Chaque colonie est un centre d'innovation.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Liaison montante** | clé | Le réseau d'étude accepte les centres d'innovation jusqu'à 2 niveaux sous celui qui étudie. |  |
| 2 | **Labos de campagne** | 3 rangs | Chacun de vos centres d'innovation mis en réseau compte 3 niveaux de plus. | 3 × 1 |
| 3 | **A · Antenne lointaine** | choix | Le réseau d'étude accepte les centres d'innovation jusqu'à 5 niveaux sous celui qui étudie : pour un empire de jeunes colonies. | |
|  | **B · Labo-mère** |  | Le centre d'innovation qui étudie compte 3 niveaux de plus : pour un empire compact. | |
| 4 | **Paillasses en kit** | 3 rangs | Vos centres d'innovation se construisent 9 % plus vite. | 3 × 3 % |
| 5 | **Un labo de plus** | clé | Le réseau d'étude met en commun 1 centre d'innovation de plus que Collaboration Stellaire ne l'autorise. |  |
| 6 | **A · Réseau vivant** | choix | Quand un centre d'innovation du réseau monte de niveau pendant une étude, son temps restant est recalculé, jamais plus lent. | |
|  | **B · Partage des résultats** |  | Une étude achevée verse 10 % de son temps en avance à la prochaine étude de la même famille, même lancée à la main. | |
| 7 | **Bourses d'étude** | 3 rangs | Une étude achevée avec au moins 2 centres d'innovation en réseau rend 9 % de son coût à la planète qui étudie. | 3 × 3 % |
| 8 | **Échange universitaire** | clé | Votre réseau d'étude accepte 1 centre d'innovation allié : le meilleur d'un membre de votre alliance, dans la tolérance du réseau. L'allié ne perd rien. |  |
| 9 | **Symposium** | ultime | Une étude lancée avec au moins 4 centres d'innovation en réseau part avec 20 % de son temps déjà écoulé, au-delà du plafond des avances. |  |

- **Liaison montante** et **Antenne lointaine** ne s'additionnent pas : la tolérance est de 5 niveaux avec les deux. Un Centre de niveau 0 n'entre jamais.
- **Labos de campagne** ne vaut que pour les Centres de vos autres planètes mis en commun, pas pour celui qui étudie ni pour le Centre allié.
- **Réseau vivant** : quand un de vos Centres d'innovation finit un niveau, le réseau est recalculé tel qu'il est alors et le temps restant baisse dans la même proportion.
- **Partage des résultats** verse 10 % de la durée de l'étude achevée à la prochaine de la même catégorie, mais sous le plafond de 10 % : avec Fil continu, il n'ajoute rien à une étude enchaînée.
- **Bourses d'étude** : 2 Centres en réseau, celui qui étudie compris. La part rendue est prise sur le prix payé, ressource par ressource, et versée à la planète qui étudie.
- **Échange universitaire** : le Centre allié s'ajoute en plus de la limite de Collaboration Stellaire, s'il entre dans la tolérance. Il compte pour Bourses d'étude et Symposium.
- **Symposium** : 4 Centres en réseau, celui qui étudie et l'allié compris. Vaut aussi dans le second centre d'innovation.

### Prototypes

*Un niveau d'avance sur tout le monde.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Prototype** | clé | Pendant 12 h après la fin d'un niveau de recherche civile ou de propulsion, vous profitez déjà de l'effet du niveau suivant. |  |
| 2 | **Essais prolongés** | 3 rangs | Vos prototypes durent 36 h de plus. | 3 × 12 h |
| 3 | **A · Prototype de combat** | choix | Le prototype couvre aussi Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. | |
|  | **B · Feu vert** |  | Pendant un prototype, vous pouvez déjà lancer ce qui demande le niveau suivant de cette recherche. | |
| 4 | **Ingénierie inverse** | 3 rangs | Après une bataille contre un joueur plus avancé que vous dans une technologie de combat, votre prochain niveau de cette technologie coûte 15 % de moins, une fois par niveau. | 3 × 5 % |
| 5 | **Double prototype** | clé | Pendant les 6 h qui suivent la fin d'une étude, son prototype vaut 2 niveaux au lieu d'un. Pas sur les technologies de combat. |  |
| 6 | **A · Brevets** | choix | Les niveaux de recherche au-delà du 10e coûtent 3 % de moins. | |
|  | **B · Banc d'essai** |  | Une fois par jour, lancez à la main un prototype de 6 h sur une recherche déjà étudiée, par exemple juste avant une attaque. | |
| 7 | **Retombées** | 3 rangs | Quand un prototype expire, la planète qui a mené l'étude reçoit 6 % de son coût. | 3 × 2 % |
| 8 | **Spécialité** | clé | Choisissez une recherche : son prototype ne s'arrête jamais. Vous pouvez en changer une fois par semaine. Calcul Quantique et Cosmologie Appliquée sont exclues. |  |
| 9 | **Révolution** | ultime | Une fois par semaine, d'un bouton : pendant 12 h, toutes vos recherches valent 1 niveau de plus. Gardez-la pour la grande offensive ou la nuit de défense. |  |

- **Prototype** : toute recherche sauf Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. Un nouveau prototype de la même recherche arrête le précédent.
- **Feu vert** : les prérequis de recherche se lisent au niveau atteint avec un prototype, la Spécialité ou la Révolution. Les prérequis de bâtiment ne changent pas.
- **Ingénierie inverse** se déclenche sur une attaque de planète, que vous soyez attaquant ou défenseur, pour chaque technologie de combat où l'adversaire était plus haut que vous. La réduction vise votre niveau suivant, une fois.
- **Double prototype** : jamais sur les technologies de combat.
- **Banc d'essai** fonctionne aussi sur les technologies de combat, sans Prototype de combat. Il arrête le prototype d'étude en cours sur cette recherche et ne rapporte pas de Retombées.
- **Retombées** : la part est prise sur ce que l'étude a payé, et versée quand son prototype prend fin, même coupé par un nouveau, si la planète vous appartient encore.
- **Spécialité** : une recherche déjà étudiée, +1 niveau en permanence. Une technologie de combat seulement avec Prototype de combat. Le délai de changement part du dernier changement.
- **Révolution** : toutes vos recherches déjà étudiées, technologies de combat comprises.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| −18 % de coût des recherches | 18 % |
| Le réseau d'étude accepte les centres d'innovation jusqu'à 5 niveaux sous celui qui étudie | 5 (plafonné) |
| Chacun de vos centres d'innovation mis en réseau compte +3 niveaux | 3 |
| Le centre d'innovation compte pour +3 niveaux dans la durée des recherches | 3 |
| +9 % de vitesse de construction des centres d'innovation | 9 % |
| Le réseau d'étude mutualise +1 centre d'innovation au-delà de ce que son niveau autorise | 1 |
| −3 % de coût des niveaux de recherche élevés | 3 % |

La tolérance du réseau garde la plus grande valeur détenue (Liaison montante ou Antenne lointaine) : 5 niveaux au plus.

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chercheur pur | Méthode 15 · Réseau 10 | Centre d'innovation jumeau, Fil continu, Brouillon conservé, Protocoles −18 %, Éclair de génie à 19 % (6 h au plus) toutes les 16 h ou automatique, Inspiration ; Liaison montante, Centres de colonie +3 niveaux, Un labo de plus, Réseau vivant |
| Grand réseau | Réseau 15 · Méthode 10 | Symposium, Échange universitaire, Bourses d'étude 9 %, tolérance de 5 niveaux ou Labo-mère ; Fil continu, Protocoles −18 %, Éclair de génie à 10 %, Esprit vif ou Réflexe |
| Savant de guerre | Prototypes 15 · Méthode 10 | Révolution, prototypes de 48 h, Prototype de combat ou Feu vert, Ingénierie inverse −15 %, Spécialité ; Éclair de génie pour rattraper les niveaux |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Le plafond de 10 % est partagé** : Fil continu le remplit à lui seul sur une étude enchaînée, et Veille de nuit n'ajoute au plus que 1 % à une étude lancée à la main. Brouillon conservé est presque toujours le meilleur choix de la rangée 3.
- **Éclair de génie est plafonné à 6 h** : sur une longue étude, Coup de génie ne change rien.
- **Liaison montante ne crée pas de Centre** : le nombre reste fixé par Collaboration Stellaire, plus 1 avec Un labo de plus et 1 allié avec Échange universitaire.
- **Double prototype ne touche pas le combat** : les technologies de combat ne gagnent jamais deux niveaux de prototype.
- **Les bonus de niveau ne s'empilent pas** : une Révolution n'ajoute rien à une recherche qui a déjà un prototype ou la Spécialité.
- **Centre d'innovation jumeau** va à 80 % seulement avec Second centre d'innovation ; sans lui, la seconde étude avance à 40 %.
- **Brevets** ne vaut qu'à partir du niveau 11 d'une recherche.

## Pages liées

- [Classes](/fr/dynasty/classes)
- [Les talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Liste des technologies](/fr/research/technologies)
