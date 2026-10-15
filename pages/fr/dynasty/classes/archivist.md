---
wiki_id: 152
locale: "fr"
path: "dynasty/classes/archivist"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/archivist"
title: "L'Archiviste"
description: "Arbre de classe de l'Archiviste : Mémoire, Épave, Registre."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:38.434Z"
updated: "2026-10-07T22:08:19.914Z"
---

# L'Archiviste

> **En bref** : « Rien ne se perd ». L'Archiviste récupère ce que les autres laissent derrière eux : un savoir que d'autres ont déjà trouvé (Mémoire), les épaves des batailles (Épave), et sa propre flotte quand elle tombe (Registre).
{.is-info}

## Règles

1. L'Archiviste est une classe **exclusive à [L'Héritage](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Mémoire, Épave et Registre.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. **Niveau connu** : un niveau de recherche que détiennent déjà, à ce niveau ou plus haut, **25 %** des joueurs comptés de l'univers. Sont comptés les joueurs actifs dans les 7 derniers jours, hors mode vacances et hors bots. Le décompte est refait une fois par jour. Toute la branche Mémoire ne touche que ces niveaux.
5. La vitesse d'un niveau connu (Niveaux connus, Fonds d'archives) et celle de Leçons de la défaite s'**ajoutent** à votre vitesse de recherche, en dehors de ses plafonds. Vitesse, coût et niveau connu se fixent au **lancement** de l'étude.
6. **Récoltes de débris** : le bonus porte sur le métal et le cristal que vos Récupérateurs chargent réellement, donc dans la limite de leur soute. Il est versé au retour, ne prend pas de place en soute et ne retire rien de plus au champ.
7. **Registre des pertes** : le registre, commun à tout votre empire, garde la liste des vaisseaux perdus au combat, ceux d'une flotte comme ceux qui défendaient une planète. Les défenses n'y entrent jamais. Une commande passée depuis le registre, sur n'importe quelle planète, se fait aux conditions du registre dans la limite des quantités qu'il garde, en puisant d'abord dans les pertes les plus anciennes.
8. La vitesse du registre s'**ajoute** à la vitesse de construction des vaisseaux : une durée est divisée par (1 + somme des bonus). La réduction de coût du registre s'applique **sur le prix déjà réduit** par vos autres réductions de vaisseaux.
9. Le seul **accent** de la classe est la vitesse des missions de recyclage (Course aux épaves), dans le budget de vitesse de flotte des talents. Le dock, le recyclage pendant le combat et l'hydrogène des débris appartiennent à l'Amiral ; les défenses au Vétéran.

## Exemple chiffré

**Mémoire** : Systèmes Offensifs 10 (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 : **46 h 32 min 44 s** sans talent. Le niveau est connu.
- Niveaux connus (+10 %) : **42 h 18 min 51 s**.
- Avec Fonds d'archives au rang 3 (+25 % au total) : **37 h 14 min 12 s**. Avec Retard comblé, à 5 niveaux de retard ou plus (+40 %) : **33 h 14 min 49 s**.
- Redécouverte au rang 3 (−12 %) : **360 448** métal et **90 112** cristal.
- Élan : Systèmes Offensifs 11, s'il est connu, dure 93 h 05 min 27 s, ramenées à 74 h 28 min 22 s par les +25 %. Il démarre avec 10 % de ce temps fait, **7 h 26 min 50 s** ; avec Lancée au rang 3 (25 %), **18 h 37 min 05 s**.
- Le même Systèmes Offensifs 10, lancé dans les 24 h d'une défaite avec Leçons de la défaite : 25 + 20 = 45 % → **32 h 06 min 02 s**.

**Épave** : 100 Corvettes détruites, univers à 30 % de débris (Redline) : 600 000 métal et 210 000 cristal, soit 810 000 ressources. Il faut 41 Récupérateurs (20 000 de soute chacun, sans Pliage Spatial).
- Ferrailleur et Tri des métaux au rang 3 (+25 %) : +150 000 métal et +52 500 cristal, **1 012 500** rapportés. Le champ perd 810 000, pas plus.
- Arrivée moins d'1 h après le combat, avec Épaves fraîches (+45 %) : **1 174 500**.
- Avec 30 Récupérateurs seulement (600 000 de soute) : 444 444 métal et 155 555 cristal chargés au prorata, le bonus porte sur eux ; 210 001 ressources restent au champ.

**Registre** : 200 Corvettes perdues, soit 4 000 000 métal, 1 400 000 cristal et 400 000 hydrogène (5 800 000 ressources).
- Indemnité : 5 % de leur prix, soit **290 000** ressources versées aussitôt (200 000 / 70 000 / 20 000) ; **464 000** avec Fonds de guerre au rang 3 (8 %).
- Plans conservés au rang 3 (−12 %) : 4 000 000 → **3 520 000** métal ; avec Remise de guerre (−20 % au total), **3 200 000**.
- Une reconstruction qui prend 10 h sans talent : **8 h 41 min 45 s** avec Registre des pertes (+15 %), **7 h 41 min 33 s** avec Chaînes de relève au rang 3 (+30 %), **6 h 40 min** avec Retour au front (+50 %). Avec Relève éclair en plus, dans les 24 h qui suivent la perte (+70 %) : **5 h 52 min 57 s**.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["REGISTRE<br/>Se relever plus vite qu'on ne tombe."]:::head
        B3R1{{"Registre des pertes<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Plans conservés<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Relève éclair<br/>1 pt"]:::option
        B3R3B["② Longue mémoire<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Chaînes de relève<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Indemnité<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Retour au front<br/>1 pt"]:::option
        B3R6B["② Remise de guerre<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Fonds de guerre<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Leçons de la défaite<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Chantier de relève<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["ÉPAVE<br/>Arriver le premier sur ce qui flotte."]:::head
        B2R1{{"Ferrailleur<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Radar d'épaves<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Charognard<br/>1 pt"]:::option
        B2R3B["② Course aux épaves<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Tri des métaux<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Alerte d'épave<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Garnison de récupération<br/>1 pt"]:::option
        B2R6B["② Épaves fraîches<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Équipe d'astreinte<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Ramasse-tout<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Scellés<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["MÉMOIRE<br/>Ce que d'autres ont déjà trouvé."]:::head
        B1R1{{"Niveaux connus<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Redécouverte<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Bibliothèque d'alliance<br/>1 pt"]:::option
        B1R3B["② Bibliothèque publique<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Fonds d'archives<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Élan<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Retard comblé<br/>1 pt"]:::option
        B1R6B["② Au coude à coude<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Lancée<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Mémoire vive<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Bibliothèque universelle<br/>ultime"]]:::ultimate
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

### Mémoire

*Ce que d'autres ont déjà trouvé.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Niveaux connus** | clé | Un niveau de recherche que 25 % des joueurs actifs de l'univers détiennent déjà est connu : vous l'étudiez 10 % plus vite, et le centre d'innovation le signale. |  |
| 2 | **Redécouverte** | 3 rangs | Vos niveaux connus coûtent 12 % de moins. | 3 × 4 % |
| 3 | **A · Bibliothèque d'alliance** | choix | Un niveau qu'un membre de votre alliance détient compte comme connu. | |
|  | **B · Bibliothèque publique** |  | Un niveau est connu dès que 10 % des joueurs actifs le détiennent. | |
| 4 | **Fonds d'archives** | 3 rangs | Vos niveaux connus s'étudient encore 15 % plus vite. | 3 × 5 % |
| 5 | **Élan** | clé | Quand vous terminez un niveau connu, le niveau suivant de la même recherche, s'il est connu, démarre avec 10 % de son temps déjà fait. |  |
| 6 | **A · Retard comblé** | choix | Sur une recherche où vous avez 5 niveaux de retard ou plus sur le niveau le plus répandu, Fonds d'archives compte deux fois. | |
|  | **B · Au coude à coude** |  | Tout niveau que détient le joueur classé juste au-dessus de vous compte comme connu. | |
| 7 | **Lancée** | 3 rangs | L'Élan donne 15 % d'avance en plus au niveau suivant. | 3 × 5 % |
| 8 | **Mémoire vive** | clé | Un niveau connu se lance sans le niveau de centre d'innovation requis : il suffit d'avoir les autres prérequis. |  |
| 9 | **Bibliothèque universelle** | ultime | Un niveau compte comme connu dès qu'un seul joueur de l'univers le détient. Seul le premier à l'atteindre n'en profite pas sur cette recherche. |  |

- **Bibliothèque d'alliance** : un niveau qu'un autre membre de votre alliance détient, à ce niveau ou plus haut. **Au coude à coude** : le joueur classé juste au-dessus de vous au classement général. Ces deux listes sont relevées une fois par jour.
- **Élan** : le niveau achevé doit être connu, et le suivant connu au moment où vous le lancez. L'avance est une part de la durée réelle de l'étude et s'ajoute au-delà du plafond des avances du Théoricien. Un seul élan à la fois : achever un autre niveau connu le remplace.
- **Retard comblé** : le niveau le plus répandu est celui que le plus de joueurs comptés détiennent exactement (le plus bas en cas d'égalité). Seule la part de Fonds d'archives compte double : 10 + 15 × 2 = 40 %.
- **Mémoire vive** lève seulement le niveau de Centre d'innovation demandé : la planète doit tout de même avoir un Centre d'innovation.
- **Bibliothèque universelle** : un seul joueur compté suffit. Un niveau détenu seulement par des bots ou des joueurs inactifs ou en vacances ne devient pas connu ainsi.

### Épave

*Arriver le premier sur ce qui flotte.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Ferrailleur** | clé | Vos récoltes de débris rapportent 10 % de plus. Le bonus est versé au retour, ne prend pas de place en soute et ne vide pas davantage le champ. |  |
| 2 | **Radar d'épaves** | 3 rangs | Les champs de débris apparaissent pour vous sur la carte jusqu'à 15 systèmes autour de vos planètes, même sur les cases jamais explorées. | 3 × 5 |
| 3 | **A · Charognard** | choix | Vous recyclez un champ sans avoir sondé sa case : vous partez dès que vous le voyez. | |
|  | **B · Course aux épaves** |  | Vos missions de recyclage vont 10 % plus vite. | |
| 4 | **Tri des métaux** | 3 rangs | Vos récoltes de débris rapportent encore 15 % de plus. | 3 × 5 % |
| 5 | **Alerte d'épave** | clé | Vous êtes prévenu dès qu'un champ de plus de 50 000 ressources apparaît dans la portée de votre radar : la course commence avant les autres. |  |
| 6 | **A · Garnison de récupération** | choix | Quand une de vos planètes est attaquée, ses recycleurs à quai récoltent le champ dès la fin du combat, avant ceux de l'attaquant. | |
|  | **B · Épaves fraîches** |  | Sur un champ apparu il y a moins de 1 h, vos récoltes rapportent 20 % de plus. | |
| 7 | **Équipe d'astreinte** | 3 rangs | Quand l'alerte sonne, vos recycleurs partent seuls depuis la planète la plus proche, même si vous dormez, jusqu'à 3 fois par jour. | 3 × 1 |
| 8 | **Ramasse-tout** | clé | Dans le même vol, vos recycleurs récoltent aussi les champs des positions voisines (±1 dans le même système), dans la limite de leur soute. |  |
| 9 | **Scellés** | ultime | Une fois par jour, vous mettez sous scellés un champ que vous voyez : pendant 1 h, les autres joueurs ne le voient plus et ne peuvent plus y envoyer de recycleurs. Ceux déjà en vol arrivent normalement. |  |

- **Radar d'épaves** : jusqu'à 15 systèmes autour de chacune de vos planètes, dans la même galaxie.
- **Charognard** : vous pouvez recycler n'importe quelle case sans l'avoir sondée, que le radar la montre ou non.
- **Alerte d'épave** sonne chaque fois qu'un champ de votre radar reçoit des débris et dépasse 50 000 ressources, même s'il les dépassait déjà. Pas pour un champ qu'un autre joueur a mis sous scellés.
- **Garnison de récupération** : après une attaque contre votre planète, ses Récupérateurs restés à quai récoltent tout le champ au-dessus d'elle, ancien compris, avant ceux de l'attaquant. Métal et cristal vont directement au stock, avec le bonus de Ferrailleur et Tri des métaux.
- **Épaves fraîches** se mesure du dernier ajout de débris au champ jusqu'à l'**arrivée** de vos Récupérateurs. Il s'ajoute aux 25 % de Ferrailleur et Tri des métaux, au-delà de leur plafond.
- **Équipe d'astreinte** : les Récupérateurs partent de votre planète la plus proche qui en a, dans la portée du radar, autant qu'il en faut pour le champ, à pleine vitesse. Pas de départ si une de vos flottes vise déjà cette case. Le compte de 24 h s'ouvre au premier départ. Un départ refusé par les règles de vol (hydrogène, emplacements de flotte, case jamais sondée sans Charognard) ne coûte rien.
- **Ramasse-tout** passe sur les champs voisins après le champ visé, dans la place qui reste en soute, sauf un champ mis sous scellés par un autre joueur.
- **Scellés** : un champ non vide que vous voyez, case sondée par vous ou votre alliance, ou couverte par votre radar. Les 24 h comptent depuis le dernier scellé. Impossible sur un champ déjà scellé par un autre joueur.

### Registre

*Se relever plus vite qu'on ne tombe.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Registre des pertes** | clé | Le registre garde 7 jours la liste des vaisseaux que vous perdez au combat : ils se reconstruisent 15 % plus vite, dans la limite des quantités perdues. |  |
| 2 | **Plans conservés** | 3 rangs | Les vaisseaux du registre coûtent 12 % de moins. | 3 × 4 % |
| 3 | **A · Relève éclair** | choix | Pendant les 24 h qui suivent une perte, le registre se reconstruit encore 20 % plus vite. | |
|  | **B · Longue mémoire** |  | Le registre garde vos pertes 21 jours, pour qui reconstruit sur la durée. | |
| 4 | **Chaînes de relève** | 3 rangs | Les vaisseaux du registre se reconstruisent encore 15 % plus vite. | 3 × 5 % |
| 5 | **Indemnité** | clé | Après une bataille où vous perdez des vaisseaux, 5 % de leur valeur vous est versée aussitôt sur la planète d'où ils étaient partis. |  |
| 6 | **A · Retour au front** | choix | Les vaisseaux du registre se reconstruisent encore 20 % plus vite. | |
|  | **B · Remise de guerre** |  | Les vaisseaux du registre coûtent encore 8 % de moins. | |
| 7 | **Fonds de guerre** | 3 rangs | L'Indemnité vous verse 3 % de plus de la valeur perdue. | 3 × 1 pts |
| 8 | **Leçons de la défaite** | clé | Après une bataille où vous perdez plus que vous ne détruisez, vos recherches Systèmes Offensifs, Champs de Protection et Métallurgie Avancée avancent 20 % plus vite pendant 24 h. |  |
| 9 | **Chantier de relève** | ultime | Le registre se reconstruit dans une seconde file de chantier, en parallèle de votre file normale : plus besoin de choisir entre vous réarmer et continuer à construire. |  |

- **Relève éclair** compte 24 h depuis **la dernière** perte encore au registre.
- **Indemnité** se calcule sur le prix normal des vaisseaux perdus, ressource par ressource, et va à la planète d'où partait la flotte, ou à la planète défendue, si elle vous appartient encore.
- **Leçons de la défaite** : une défaite est une attaque de planète, en attaque comme en défense, où vous avez perdu plus de points d'unités (vaisseaux et défenses) que l'adversaire. Seules les études lancées pendant ces 24 h vont plus vite : une étude déjà en cours ne change pas. Chaque nouvelle défaite relance les 24 h.
- **Chantier de relève** : les commandes du registre ont leur propre file, en parallèle de la file normale des vaisseaux.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| +25 % de vitesse de recherche sur les niveaux connus | 25 % |
| −12 % de coût de recherche sur les niveaux connus | 12 % |
| Un niveau est connu dès que 10 % des joueurs de l'univers le détiennent | 10 % |
| +25 % de ressources rapportées par une récolte de débris | 25 % |
| +10 % de vitesse des flottes en mission de recyclage | 10 % |

Deux bonus passent au-delà de ces plafonds : Retard comblé porte la vitesse d'un niveau connu à 40 %, et Épaves fraîches ajoute 20 points aux récoltes sur un champ frais (45 %).

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Le rattrapeur | Mémoire 15 · Registre 10 | Bibliothèque universelle, Mémoire vive ; niveaux connus +25 % (+40 % avec Retard comblé) et −12 %, 25 % d'avance sur chaque niveau enchaîné ; registre +50 % avec Retour au front (sinon +30 % et −20 % avec Remise de guerre), Plans conservés −12 %, Indemnité 5 % |
| Le charognard | Épave 15 · Mémoire 10 | Scellés, Alerte d'épave, Équipe d'astreinte, Ramasse-tout ; récoltes +25 % ; niveaux connus +25 % et −12 %, Élan 10 % |
| L'increvable | Registre 15 · Épave 10 | Chantier de relève, Indemnité 8 %, Leçons de la défaite, registre jusqu'à +70 % ; récoltes +25 %, radar à 15 systèmes, Garnison de récupération ou Épaves fraîches |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Un niveau connu se juge sur les joueurs comptés** (actifs depuis 7 jours, hors vacances, hors bots), et le décompte n'est refait qu'une fois par jour.
- **Le premier sur une recherche ne profite pas de la Mémoire** sur cette recherche : il n'y a personne devant lui.
- **Tout se fixe au lancement** : un niveau qui devient connu pendant l'étude ne l'accélère pas, et Leçons de la défaite n'accélère pas une étude déjà en cours.
- **Bibliothèque publique ne sert plus à rien avec Bibliothèque universelle**, qui demande déjà moins : un seul détenteur.
- **Le bonus de récolte suit la soute** : il porte sur ce que vos Récupérateurs chargent, pas sur tout le champ. Il ne vide pas plus le champ : d'autres joueurs peuvent récolter ce qui reste.
- **Équipe d'astreinte sans Charognard** échoue sur une case jamais sondée.
- **Épaves fraîches se juge à l'arrivée**, pas au départ : comptez le temps de vol.
- **Le registre ne couvre que les vaisseaux perdus au combat**, dans la limite des quantités perdues et pendant 7 jours (21 avec Longue mémoire). Les défenses n'y entrent pas.
- **Relève éclair ne dure que 24 h** après la dernière perte.

## Pages liées

- [Dynasties](/fr/dynasty/dynasties)
- [Classes](/fr/dynasty/classes)
- [Les talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Champs de débris](/fr/combat/debris)
- [Liste des technologies](/fr/research/technologies)
