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
updated: "2026-10-06T10:29:39.722Z"
---

# L'Archiviste

> **En bref** : « Rien ne se perd ». L'Archiviste récupère ce que les autres laissent derrière eux : un savoir que d'autres ont déjà trouvé (**Mémoire**), les épaves des batailles des autres (**Épave**), et sa propre flotte quand elle tombe (**Registre**). Classe exclusive à [L'Héritage](/fr/dynasty/dynasties).
{.is-info}

## Règles

1. L'Archiviste est une classe **exclusive à L'Héritage** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **3 branches de 9 rangées** (15 points par branche). Les règles de points, de portes et d'ultime sont celles de tous les arbres de classe : voir [Système de talents](/fr/dynasty/talents).
3. **Niveau connu** : un niveau de recherche que **25 %** des joueurs actifs de l'univers détiennent déjà. Toute la branche Mémoire ne touche que ces niveaux.
4. **Récoltes de débris** : le bonus de l'Archiviste est versé au retour des Récupérateurs. Il ne prend pas de place en soute et ne retire rien de plus au champ de débris.
5. **Registre des pertes** : le registre garde pendant **7 jours** la liste des vaisseaux perdus au combat. Tout ce qui y figure se reconstruit à des conditions de faveur, dans la limite des quantités perdues. Il ne couvre que les vaisseaux, pas les défenses.
6. La vitesse de reconstruction du registre s'**ajoute** à la vitesse de construction des vaisseaux (Ateliers de l'arbre commun, alliance). Une durée est divisée par (1 + somme des bonus).
7. Le seul **accent** de la classe est la vitesse des missions de recyclage (Course aux épaves), voir [Système de talents](/fr/dynasty/talents).
8. Le dock, le recyclage pendant le combat et l'hydrogène des débris appartiennent à l'Amiral ; les défenses au Vétéran.

## Exemple chiffré

**Mémoire** : Systèmes Offensifs 10 (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 : **46 h 32 min** sans talent. Le niveau est connu.
- Niveaux connus (+10 %) : **42 h 18 min**.
- Avec Fonds d'archives au rang 3 (+25 % au total) : **37 h 14 min**.
- Redécouverte au rang 3 (−12 %) : **360 448** métal et **90 112** cristal.
- Élan : Systèmes Offensifs 11 (93 h 05 min au même Centre), s'il est connu, démarre avec 10 % de son temps fait, soit **9 h 18 min** ; avec Lancée au rang 3 (25 %), **23 h 16 min**.

**Épave** : un champ de débris de 400 000 ressources.
- Ferrailleur (+10 %) : **440 000** rapportés.
- Avec Tri des métaux au rang 3 (+25 % au total) : **500 000**. Le champ perd toujours 400 000 ressources, pas plus.

**Registre** : 200 Corvettes perdues, soit 4 000 000 métal, 1 400 000 cristal et 400 000 hydrogène (5 800 000 ressources).
- Indemnité : 5 % de leur valeur, soit **290 000** ressources versées aussitôt ; **464 000** avec Fonds de guerre au rang 3 (8 %).
- Plans conservés au rang 3 (−12 %) : 4 000 000 → **3 520 000** métal ; avec Remise de guerre (−20 % au total), **3 200 000**.
- Une reconstruction qui prend 10 h sans talent : **8 h 41 min** avec Registre des pertes (+15 %), **7 h 41 min** avec Chaînes de relève au rang 3 (+30 %), **6 h 40 min** avec Retour au front (+50 %). Avec Relève éclair en plus, pendant les 24 h qui suivent la perte (+70 %) : **5 h 53 min**.

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

Types de rangée : *clé* (1 point), *3 rangs*, *choix* (un point, option A ou B), *ultime*.

### Mémoire : « Ce que d'autres ont déjà trouvé. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Niveaux connus** | Un niveau de recherche que 25 % des joueurs actifs de l'univers détiennent déjà est connu : vous l'étudiez plus vite, et le Centre d'innovation le signale. | +10 % |
| 2 | 3 rangs | **Redécouverte** | Vos niveaux connus coûtent moins. | −4 % par rang (−12 %) |
| 3 | choix | **A : Bibliothèque d'alliance** | Un niveau qu'un membre de votre alliance détient compte comme connu. | déblocage |
| | | **B : Bibliothèque publique** | Un niveau est connu dès que 10 % des joueurs actifs le détiennent. | 10 % |
| 4 | 3 rangs | **Fonds d'archives** | Vos niveaux connus s'étudient encore plus vite. | +5 % par rang (+25 % au total) |
| 5 | clé | **Élan** | Quand vous terminez un niveau connu, le niveau suivant de la même recherche, s'il est connu, démarre avec une part de son temps déjà faite. | 10 % |
| 6 | choix | **A : Retard comblé** | Sur une recherche où vous avez 5 niveaux de retard ou plus sur le niveau le plus répandu, Fonds d'archives compte double : 10 + 15 × 2 = +40 % sur un niveau connu. | ×2 |
| | | **B : Au coude à coude** | Tout niveau que détient le joueur classé juste au-dessus de vous compte comme connu. | déblocage |
| 7 | 3 rangs | **Lancée** | L'Élan donne plus d'avance au niveau suivant. | +5 % par rang (25 %) |
| 8 | clé | **Mémoire vive** | Un niveau connu se lance sans le niveau de Centre d'innovation requis : il suffit d'avoir les autres prérequis. | déblocage |
| 9 | ultime | **Bibliothèque universelle** | Un niveau compte comme connu dès qu'un seul joueur de l'univers le détient. Seul le premier à l'atteindre n'en profite pas sur cette recherche. | déblocage |

### Épave : « Arriver le premier sur ce qui flotte. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Ferrailleur** | Vos récoltes de débris rapportent plus. Le bonus est versé au retour, ne prend pas de place en soute et ne vide pas davantage le champ. | +10 % |
| 2 | 3 rangs | **Radar d'épaves** | Les champs de débris apparaissent pour vous sur la carte autour de vos planètes, même sur les cases jamais explorées. | 5 systèmes par rang (15) |
| 3 | choix | **A : Charognard** | Vous recyclez un champ sans avoir sondé sa case : vous partez dès que vous le voyez. | déblocage |
| | | **B : Course aux épaves** | Vos missions de recyclage vont plus vite (accent). | +10 % |
| 4 | 3 rangs | **Tri des métaux** | Vos récoltes de débris rapportent encore plus. | +5 % par rang (+25 % au total) |
| 5 | clé | **Alerte d'épave** | Vous êtes prévenu dès qu'un champ de plus de 50 000 ressources apparaît dans la portée de votre radar. | 50 000 |
| 6 | choix | **A : Garnison de récupération** | Quand une de vos planètes est attaquée, ses Récupérateurs à quai récoltent le champ dès la fin du combat, avant ceux de l'attaquant. | déblocage |
| | | **B : Épaves fraîches** | Sur un champ apparu il y a moins d'1 h, vos récoltes rapportent 20 points de plus, en plus de Ferrailleur et Tri des métaux. Comme eux, ce bonus est créé au retour : il ne vide pas davantage le champ (25 % → 45 % avec la branche pleine). | +20 points |
| 7 | 3 rangs | **Équipe d'astreinte** | Quand l'alerte sonne, vos Récupérateurs partent seuls depuis la planète la plus proche, même si vous dormez. | 1 départ par jour et par rang (3) |
| 8 | clé | **Ramasse-tout** | Dans le même vol, vos Récupérateurs récoltent aussi les champs des positions voisines (±1 dans le même système), dans la limite de leur soute. | ±1 position |
| 9 | ultime | **Scellés** | Une fois toutes les 24 h, vous mettez sous scellés un champ que vous voyez : pendant 1 h, les autres joueurs ne le voient plus et ne peuvent plus y envoyer de Récupérateurs. Ceux déjà en vol arrivent normalement. | 1 h |

### Registre : « Se relever plus vite qu'on ne tombe. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Registre des pertes** | Le registre garde 7 jours la liste des vaisseaux que vous perdez au combat : ils se reconstruisent plus vite, dans la limite des quantités perdues. | +15 % |
| 2 | 3 rangs | **Plans conservés** | Les vaisseaux du registre coûtent moins. | −4 % par rang (−12 %) |
| 3 | choix | **A : Relève éclair** | Pendant les 24 h qui suivent une perte, le registre se reconstruit encore plus vite. | +20 % |
| | | **B : Longue mémoire** | Le registre garde vos pertes 21 jours au lieu de 7. | 21 jours |
| 4 | 3 rangs | **Chaînes de relève** | Les vaisseaux du registre se reconstruisent encore plus vite. | +5 % par rang (+30 % au total) |
| 5 | clé | **Indemnité** | Après une bataille où vous perdez des vaisseaux, une part de leur coût vous est versée aussitôt sur la planète d'où ils étaient partis, ressource par ressource. | 5 % |
| 6 | choix | **A : Retour au front** | Les vaisseaux du registre se reconstruisent encore plus vite. | +20 % (+50 % au total) |
| | | **B : Remise de guerre** | Les vaisseaux du registre coûtent encore moins. | −8 % (−20 % au total) |
| 7 | 3 rangs | **Fonds de guerre** | L'Indemnité verse une part de plus de la valeur perdue. | +1 point par rang (8 %) |
| 8 | clé | **Leçons de la défaite** | Après une bataille où vous perdez plus que vous ne détruisez, vos recherches Systèmes Offensifs, Champs de Protection et Métallurgie Avancée avancent plus vite pendant 24 h. | +20 % |
| 9 | ultime | **Chantier de relève** | Le registre se reconstruit dans une seconde file du Dock orbital, en parallèle de votre file normale. | 2e file |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Le rattrapeur | Mémoire 15 · Registre 10 | Bibliothèque universelle ; niveaux connus +25 % plus vite et −12 % ; 25 % d'avance sur chaque niveau enchaîné ; registre +30 % et Indemnité 5 %. |
| Le charognard | Épave 15 · Mémoire 10 | Scellés, alerte, départs automatiques, champs voisins ; récoltes +25 % ; niveaux connus +25 %. |
| L'increvable | Registre 15 · Épave 10 | Chantier de relève, Indemnité 8 %, Leçons de la défaite ; récoltes +25 %, radar à 15 systèmes, Garnison de récupération. |

## Pièges fréquents

- **Un niveau connu se juge sur les joueurs actifs** de l'univers, pas sur tous les comptes.
- **Le premier sur une recherche ne profite pas de la Mémoire** sur cette recherche : il n'y a personne devant lui.
- **Le bonus de récolte ne vide pas plus le champ** : d'autres joueurs peuvent encore récolter ce qui reste.
- **Le registre ne couvre que les vaisseaux perdus au combat**, dans la limite des quantités perdues et pendant 7 jours (21 avec Longue mémoire). Les défenses n'y entrent pas.
- **Relève éclair ne dure que 24 h** après chaque perte.

## Pages liées

- [Dynasties](/fr/dynasty/dynasties)
- [Classes](/fr/dynasty/classes)
- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Champs de débris](/fr/combat/debris)
- [Liste des technologies](/fr/research/technologies)
