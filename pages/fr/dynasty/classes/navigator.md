---
wiki_id: 155
locale: "fr"
path: "dynasty/classes/navigator"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/navigator"
title: "Le Navigateur"
description: "Arbre de classe du Navigateur : Poussée, Lignes et Fret."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:44.757Z"
updated: "2026-10-15T18:57:24.923Z"
---

# Le Navigateur

> **En bref** : le Navigateur est le maître des routes. Il décide quand ses flottes arrivent, d'où elles partent et ce qu'elles ramènent. La vitesse, l'hydrogène, les soutes et les emplacements de flotte génériques viennent de l'arbre commun ; le Navigateur garde des mécaniques et deux accents étroits.
{.is-info}

## Règles

1. Le Navigateur est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Poussée, Lignes et Fret.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. La vitesse de flotte, l'hydrogène, les soutes et les emplacements génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). Le Navigateur n'y ajoute que deux **accents** : +10 % de vitesse sur les Transports, Stationnements et Colonisations (Route marchande) ou sur les Attaques et Espionnages visant une cible abandonnée (Route de chasse), dans le plafond de vitesse des talents (50 %, 60 % avec l'alliance) ; +15 % de vitesse de construction des Navettes de fret, Cargos stellaires et Récupérateurs (Coques civiles).
5. Une **cible abandonnée** est une base sans propriétaire, une base d'un adversaire contrôlé par le jeu, ou celle d'un joueur inactif depuis la durée fixée par l'univers.
6. Les trajets **entre vos propres bases** (planètes et lunes) sont le périmètre propre de la classe : Transport et Stationnement pour Navettes, Pont aérien, Arrimage et Ascenseur orbital. Arrimage et Pont aérien sont **hors des plafonds** de soute et d'hydrogène de l'arbre commun.
7. Un bonus de vitesse de vol **divise** la durée du trajet : +10 % donne un trajet 1,1 fois plus court. Les nœuds de recharge, eux, **retirent** des heures ou un pourcentage au délai. Voir [Déplacements](/fr/fleet/movement).
8. Les ordres en vol (Postcombustion, Relance, Mise en attente, Changement de cap, Saut de retour, Double fond en vol) se donnent depuis le détail de la flotte. Les cycles sont comptés pour tout l'empire, depuis la dernière utilisation.

## Exemple chiffré

**Postcombustion sur un aller-retour**
- Un Transport aller-retour, aller de 2 h. Après 1 h de vol, Postcombustion coupe 25 % du temps restant : 3 600 s × 0,75 = 2 700 s. La flotte arrive 1 h 45 après son départ.
- Le retour dure autant que l'aller réel : 1 h 45. Total **3 h 30** au lieu de 4 h : couper 15 min à l'aller en fait gagner 30.
- Avec Postcombustion poussée au rang 3 (40 %) : 3 600 s × 0,6 = 2 160 s, aller 1 h 36, retour 1 h 36, total **3 h 12**.

**Soute à carburant : 100 Corvettes vers une autre galaxie**
- Distance : 20 000. Une Corvette consomme 300. Un trajet à 100 % coûte 300 × 100 × 20 000 / 35 000 × 4 = 68 571 H (arrondi à l'inférieur), soit **137 142 H** aller-retour.
- Soute des 100 Corvettes, sans Pliage Spatial : 100 × 800 = **80 000**. Le carburant ne tient pas.
- Rang 1 (85 % du volume) : 116 571. Rang 2 (70 %) : 96 000. Rang 3 (55 %) : 137 142 × 0,55 = **75 429** : la flotte peut partir.

**Décollage d'urgence : le seuil de 5 %**
- À quai : 100 Corvettes à 29 000 de coût chacune (20 000 + 7 000 + 2 000), soit 2 900 000. Seuil : 5 % = **145 000**.
- 37 Intercepteurs (4 000 chacun) = 148 000 : la flotte décolle. 36 Intercepteurs (144 000) : elle reste.
- La planète refuge est à 40 min ; le retour est tiré à 1 h. La flotte ne revient jamais plus vite qu'elle n'est partie : elle rentre 40 min + 40 min = **1 h 20** après son décollage.

**Formation serrée et Sillage : Cargos stellaires et Corvettes vers une autre galaxie** (vitesse de flotte de l'univers ×1, comme Redline ; sans recherche de moteur)
- Sans le nœud, la flotte vole à la vitesse du Cargo stellaire, 7 500 : 10 + 3 500 × √(10 × 20 000 / 7 500) = 18 084 s, soit **5 h 01 min 24 s**.
- Formation serrée (15 %) : 8 625, soit **4 h 41 min 04 s**. Avec Sillage au rang 3 (30 %) : 9 750, soit **4 h 24 min 22 s**. L'hydrogène ne change pas.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FRET<br/>Tout ramener, rien perdre."]:::head
        B3R1{{"Fret retour<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Arrimage<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Livraison groupée<br/>1 pt"]:::option
        B3R3B["② Cales sans fond<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Coques civiles<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Double fond<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Double fond en vol<br/>1 pt"]:::option
        B3R6B["② Double fond partagé<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Cales préparées<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Fret assuré<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Razzia<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["LIGNES<br/>Toutes vos planètes, une seule base."]:::head
        B2R1{{"Navettes<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Soute à carburant<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Plein à l'arrivée<br/>1 pt"]:::option
        B2R3B["② Réservoir rendu<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Portes chaudes<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Changement de cap<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Porte double<br/>1 pt"]:::option
        B2R6B["② Pont aérien<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Navettes en plus<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Ascenseur orbital<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Port d'attache<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["POUSSÉE<br/>Arriver quand on l'a décidé."]:::head
        B1R1{{"Postcombustion<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Réservoirs d'appoint<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Route marchande<br/>1 pt"]:::option
        B1R3B["② Route de chasse<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Postcombustion poussée<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Formation serrée<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Relance<br/>1 pt"]:::option
        B1R6B["② Mise en attente<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Sillage<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Décollage d'urgence<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Saut de retour<br/>ultime"]]:::ultimate
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

### Poussée

*Arriver quand on l'a décidé.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Postcombustion** | clé | Une fois par jour, une de vos flottes en vol coupe 25 % du temps qui lui reste, sans descendre sous 5 min de trajet. |  |
| 2 | **Réservoirs d'appoint** | 3 rangs | Postcombustion se recharge 12 h plus vite. | 3 × 4 h |
| 3 | **A · Route marchande** | choix | Vos transports, déploiements et colonisations vont 10 % plus vite. | |
|  | **B · Route de chasse** |  | Vos espionnages et attaques sur des cibles abandonnées vont 10 % plus vite. | |
| 4 | **Postcombustion poussée** | 3 rangs | Postcombustion coupe 15 % de plus du temps restant. | 3 × 5 % |
| 5 | **Formation serrée** | clé | Dans une flotte mixte, vos vaisseaux lents volent 15 % plus vite, jamais plus vite que le plus rapide. |  |
| 6 | **A · Relance** | choix | Une flotte partie à vitesse réduite peut repasser à pleine vitesse en vol ; l'hydrogène en plus se paie à la relance. | |
|  | **B · Mise en attente** |  | Une flotte qui rentre ou en mission pacifique peut ralentir en vol jusqu'à 10 % de sa vitesse ; l'hydrogène économisé vous est rendu. | |
| 7 | **Sillage** | 3 rangs | Formation serrée gagne 15 % de plus. | 3 × 5 % |
| 8 | **Décollage d'urgence** | clé | Une fois par jour, quand une attaque pesant au moins 5 % de votre flotte à quai arrive sur une de vos planètes, la flotte décolle seule 3 min avant l'impact vers votre planète la plus proche. Elle revient au hasard entre 1 h et 3 h plus tard, une fenêtre que vous pouvez régler. |  |
| 9 | **Saut de retour** | ultime | 2 charges par 24 h glissantes : une flotte qui rentre de mission arrive chez elle à l'instant, déchargée comme à un retour normal. |  |

- **Postcombustion** : sur une flotte à l'aller ou au retour, refusée s'il reste 5 min ou moins ; le temps restant est arrondi à la seconde supérieure. Sur un aller-retour, le retour reprend la durée de l'aller raccourci (sauf avec Port d'attache, Livraison groupée ou une vitesse changée en vol). Sur une Attaque, l'alerte du défenseur suit la nouvelle heure d'impact.
- **Réservoirs d'appoint** retire 4 h par rang au cycle de 24 h : 12 h au rang 3.
- **Route marchande** et **Route de chasse** occupent l'accent de vitesse de 10 % ; ils s'ajoutent aux 40 % de l'arbre commun au plus.
- **Formation serrée** : le vaisseau le plus lent compte 15 % plus vite (30 % avec Sillage), sans dépasser le plus rapide de la flotte, vitesses des moteurs comprises. Une flotte d'un seul type ne gagne rien. La durée suit la racine carrée de la vitesse : +30 % de vitesse raccourcit le vol d'environ 12 %.
- **Relance** : seulement vers 100 %. Le temps restant est multiplié par l'ancienne vitesse / 100 (sur un aller-retour à l'aller, le retour aussi) ; l'hydrogène en plus est prélevé sur la base.
- **Mise en attente** : jusqu'à 10 % au plus bas ; l'hydrogène économisé revient dans la soute de la flotte.
- Ni Relance ni Mise en attente ne s'appliquent à l'aller d'une Attaque, d'un Espionnage, d'une Destruction de lune ou d'une Expédition ; ils s'appliquent à tout retour.
- **Décollage d'urgence** : la menace se mesure au coût total des vaisseaux (métal, cristal, hydrogène), Collecteurs solaires exclus ; un Éclaireur compte comme les autres. La flotte part en Transport à 100 %, sans ressources, vers votre autre planète la plus proche (jamais une lune, ni la planète de la même case), jusqu'à 3 min avant l'impact. Rien ne part si vous n'avez pas d'autre planète ou si la base n'a pas l'hydrogène du vol. La fenêtre de retour se règle entre 15 min et 24 h ; un retour ne vole jamais plus vite que l'aller, il peut donc tomber après la fenêtre si la planète refuge est loin.
- **Saut de retour** : toute flotte en retour, quelle que soit sa mission. Chaque charge revient 24 h après avoir servi.

### Lignes

*Toutes vos planètes, une seule base.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Navettes** | clé | 2 transports ou déploiements entre vos planètes n'occupent plus d'emplacement de flotte. |  |
| 2 | **Soute à carburant** | 3 rangs | Le carburant du trajet compte 45 % de moins de son volume dans vos soutes. | 3 × 15 pts |
| 3 | **A · Plein à l'arrivée** | choix | Le carburant d'un transport ou d'un déploiement entre vos planètes peut être payé par la planète d'arrivée : une planète vidée de son hydrogène peut encore évacuer sa flotte. | |
|  | **B · Réservoir rendu** |  | Une flotte rappelée rapporte 50 % du carburant qu'elle n'a pas brûlé. | |
| 4 | **Portes chaudes** | 3 rangs | Vos portes de saut se rechargent 30 % plus vite. | 3 × 10 % |
| 5 | **Changement de cap** | clé | Une fois toutes les 12 h, un transport, un déploiement ou une flotte qui rentre peut être redirigé vers une autre de vos planètes ou lunes du même système, heure d'arrivée inchangée. |  |
| 6 | **A · Porte double** | choix | Une porte de saut fait 2 sauts avant de se recharger. | |
|  | **B · Pont aérien** |  | Les transports et déploiements entre vos planètes consomment 50 % d'hydrogène en moins. | |
| 7 | **Navettes en plus** | 3 rangs | +3 navettes : des trajets entre vos planètes qui n'occupent pas d'emplacement de flotte. | 3 × 1 |
| 8 | **Ascenseur orbital** | clé | Un transport ou un déploiement entre une planète et sa lune dure 1 min. |  |
| 9 | **Port d'attache** | ultime | Toute mission aller-retour peut rentrer à une autre de vos planètes, choisie au départ ; retour et carburant suivent le trajet réel. |  |

- **Navettes** et **Navettes en plus** : un Transport ou un Stationnement vers une de vos bases part hors emplacement tant qu'une navette est libre. La navette reste occupée jusqu'au retour de la flotte. 5 navettes au plus.
- **Soute à carburant** : le volume du carburant est arrondi à l'unité supérieure.
- **Plein à l'arrivée** : la base d'arrivée paie tout l'hydrogène du vol, aller-retour compris ; la base de départ ne paie que la cargaison.
- **Réservoir rendu** : au rappel, le chemin de retour déjà dû compte comme brûlé. 20 000 H payés aller-retour, rappel à mi-chemin de l'aller : 10 000 H non brûlés, 5 000 H rendus dans la soute.
- **Portes chaudes** **réduit** la recharge de 10 % par rang (×0,7 au rang 3), elle ne la divise pas : niveau 5, 36 min → 25 min 12 s ; niveau 14, 10 min → 7 min.
- **Changement de cap** : un Transport ou un Stationnement à l'aller, ou toute flotte en retour, dont la destination est à vous. La nouvelle base doit être dans le même système et avoir un Dock orbital si la flotte y atterrit (retour ou stationnement).
- **Pont aérien** se multiplie avec les réductions d'hydrogène de l'arbre commun et de l'alliance.
- **Ascenseur orbital** : 1 min fixe, quelle que soit la vitesse choisie ou celle de l'univers.
- **Port d'attache** : la base de retour (planète ou lune) doit avoir un Dock orbital. Le retour vole la vraie distance et paie son hydrogène, sans les bonus des trajets entre vos bases.

### Fret

*Tout ramener, rien perdre.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Fret retour** | clé | Un transport vers une de vos planètes repart chargé d'une cargaison choisie au départ : un trajet au lieu de deux. |  |
| 2 | **Arrimage** | 3 rangs | Vos transports et déploiements entre vos planètes emportent 30 % de plus que leur soute. | 3 × 10 % |
| 3 | **A · Livraison groupée** | choix | Un transport peut livrer deux de vos planètes dans le même vol, la seconde sur la route du retour : 50 % chacune, ou la répartition choisie au départ. | |
|  | **B · Cales sans fond** |  | Vos expéditions ramènent tout ce qu'elles trouvent, même au-delà de leur soute. | |
| 4 | **Coques civiles** | 3 rangs | Vos transporteurs et recycleurs se construisent 15 % plus vite. | 3 × 5 % |
| 5 | **Double fond** | clé | Une fois par jour, une flotte part avec deux fois plus de soute pour toute sa sortie, aller et retour. |  |
| 6 | **A · Double fond en vol** | choix | Double fond se déclenche aussi sur une flotte déjà en vol, avant son arrivée : vous voyez la cible avant de décider. | |
|  | **B · Double fond partagé** |  | Double fond s'applique à 2 flottes parties à moins de 1 min l'une de l'autre. | |
| 7 | **Cales préparées** | 3 rangs | Double fond se recharge 12 h plus vite. | 3 × 4 h |
| 8 | **Fret assuré** | clé | Si une de vos flottes de transport est détruite, 50 % de sa cargaison revient à sa planète de départ ; l'attaquant n'en gagne rien de plus. |  |
| 9 | **Razzia** | ultime | Une fois par jour, une attaque gagnée sur une cible abandonnée emporte 100 % de ce qui est pillable, au lieu de la part habituelle. |  |

- **Fret retour** : Transport seulement (pas Stationnement). La cargaison demandée doit tenir dans la soute à l'envoi ; elle est chargée dans la limite du stock de la base d'arrivée.
- **Arrimage** s'ajoute au bonus de soute de l'arbre commun : jusqu'à +55 % entre vos bases.
- **Livraison groupée** : la première base reçoit 50 % de la cargaison, ou la part choisie entre 1 et 99 %. Le vol paie ses trois trajets. Ne se combine ni avec Fret retour ni avec Port d'attache.
- **Cales sans fond** : ne concerne que les trouvailles de ressources des [expéditions](/fr/fleet/expeditions).
- **Coques civiles** s'ajoute à la vitesse de construction des unités de l'arbre commun : un Cargo stellaire de 10 h se construit en 8 h 41 min 45 s (÷ 1,15).
- **Double fond** se demande à l'envoi : la soute doublée sert à tout ce que la flotte charge (pillage, débris, trouvailles, fret). Le cycle part de la première flotte.
- **Double fond partagé** : la seconde flotte doit partir au plus 1 min après la première.
- **Fret assuré** : joue quand une de vos flottes est entièrement détruite au combat pendant sa propre Attaque (Seconde vague comprise) ou une Destruction de lune. La moitié de ce qu'elle transportait, arrondie à l'inférieur ressource par ressource, revient à sa base de départ.
- **Razzia** : la charge part sur la **première** attaque gagnée contre une cible abandonnée du cycle, sans choix. Les abris du défenseur s'appliquent, puis la limite des soutes. 3 000 000 en stock : 1 500 000 au taux habituel de 50 %, 3 000 000 avec Razzia, dans la limite des soutes.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| +10 % de vitesse aux transports, déploiements et colonisations | 10 % |
| +10 % de vitesse aux espionnages et attaques sur des cibles abandonnées | 10 % |
| +30 % de vitesse pour les vaisseaux les plus lents d'une flotte, sans jamais dépasser son vaisseau le plus rapide | 30 % |
| 2 charges de saut de retour : une flotte qui rentre de sa mission arrive chez elle à l'instant | 2 |
| −45 pts sur la part de son volume que le carburant du trajet occupe dans la soute | 45 pts |
| Une flotte rappelée rapporte à sa base 50 % du carburant qu'elle n'a pas brûlé | 50 % |
| +30 % de vitesse de recharge des portes de saut | 30 % |
| −50 % d'hydrogène pour les transports et déploiements entre vos planètes | 50 % |
| +30 % de chargement pour les transports et déploiements entre vos planètes | 30 % |
| +15 % de vitesse de construction des transporteurs et des recycleurs | 15 % |
| Capacité de cargo boostée : ×2 | ×2 |
| 50 % de la cargaison d'une flotte de transport détruite revient à sa planète de départ | 50 % |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Coureur | Poussée 15 · Lignes 10 | Saut de retour, Postcombustion à 40 % toutes les 12 h, une route à +10 %, Formation serrée à 30 %, Relance ou Mise en attente, Décollage d'urgence ; 2 navettes, carburant à 55 % de son volume, Plein à l'arrivée ou Réservoir rendu, Portes chaudes, Changement de cap, Porte double ou Pont aérien |
| Logisticien d'empire | Lignes 15 · Fret 10 | Port d'attache, 5 navettes, Ascenseur orbital, Changement de cap, Porte double ou Pont aérien ; Fret retour, +30 % de chargement entre vos bases, Livraison groupée ou Cales sans fond, Coques civiles, Double fond une fois par 24 h |
| Pilleur de fermes | Fret 15 · Poussée 10 | Razzia, Double fond toutes les 12 h (Double fond en vol ou Double fond partagé), Fret assuré ; Postcombustion à 40 % toutes les 12 h, Route de chasse, Formation serrée à 15 % |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Le carburant prend de la place en soute** : sans Soute à carburant, une flotte de combat lointaine peut ne pas partir faute de soute.
- **Formation serrée ne regarde que le plus lent** : la flotte vole à la vitesse du plus lent augmentée de 15 % (30 %), sans dépasser le plus rapide. Une flotte d'un seul type n'en profite pas.
- **Postcombustion à l'aller compte double** sur un aller-retour : le retour reprend la durée de l'aller raccourci.
- **Route de chasse ne vise que les cibles abandonnées** : une attaque contre un joueur actif garde sa vitesse normale.
- **Relance et Mise en attente** ne marchent pas à l'aller d'une Attaque, d'un Espionnage, d'une Destruction de lune ni d'une Expédition.
- **Décollage d'urgence n'emmène que les vaisseaux** : les ressources restent sur la planète. Sans autre planète ou sans l'hydrogène du vol, la flotte ne part pas.
- **Fret assuré ne protège pas un convoi** : il ne joue que si votre flotte est anéantie pendant sa propre attaque ou une Destruction de lune.
- **Razzia part tout seul** sur la première victoire contre une cible abandonnée, même si elle est presque vide.
- **Navettes** : seuls les Transports et Stationnements vers vos propres bases sont hors emplacement.
- **Livraison groupée, Fret retour et Port d'attache ne se combinent pas** sur un même envoi.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Déplacements](/fr/fleet/movement)
- [Porte de saut](/fr/fleet/jump-gate)
- [Expéditions](/fr/fleet/expeditions)
- [Pillage](/fr/combat/plunder)
