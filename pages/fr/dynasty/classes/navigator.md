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
updated: "2026-10-06T10:29:46.081Z"
---

# Le Navigateur

> **En bref** : le Navigateur est le maître des routes. Il décide quand ses flottes arrivent, d'où elles partent et ce qu'elles ramènent. La vitesse, l'hydrogène, les soutes et les emplacements de flotte génériques viennent de l'[arbre commun](/fr/dynasty/common-tree) (Logistique) ; le Navigateur garde des mécaniques et deux accents étroits. Classe commune à toutes les dynasties.
{.is-info}

*Devise : « Arriver ».*

## Règles

1. L'arbre de classe suit les règles communes à toutes les classes : 3 branches de 9 rangées, 15 points par branche, 25 points au maximum. Voir [Système de talents](/fr/dynasty/talents).
2. **Accents** du Navigateur :
   - vitesse : **+10 %** sur les missions pacifiques (Route marchande) ou sur les cibles abandonnées (Route de chasse), dans le plafond de vitesse des talents (50 %, 60 % avec l'alliance) ;
   - construction : **+15 %** sur les Navettes de fret, Cargos stellaires et Récupérateurs (Coques civiles).
3. Ce qui ne sert que vos trajets entre vos propres planètes (Pont aérien, Arrimage) est **hors des plafonds** de l'arbre commun.
4. Un bonus de vitesse **divise la durée** du trajet : +10 % = un trajet 1,1 fois plus court. Voir [Déplacements](/fr/fleet/movement).

## Exemple chiffré

**Postcombustion sur un retour de 1 h**
- Rang de base : la flotte coupe 25 % du temps restant : **1 h → 45 min**.
- Avec Postcombustion poussée au rang 3 (40 %) : **1 h → 36 min**.
- Avec Réservoirs d'appoint au rang 3, Postcombustion revient toutes les **12 h** au lieu de 24 h.

**Soute à carburant : 100 Corvettes vers une autre galaxie**
- Distance : 20 000. Consommation de la Corvette : 300. À 100 % de vitesse, un aller coûte 300 × 100 × 20 000 / 35 000 × 4 = **68 571 H**, soit **137 143 H** aller-retour.
- Soute des 100 Corvettes, sans bonus : 100 × 800 = **80 000**. Le carburant ne tient pas.
- Au rang 3 de Soute à carburant, il ne compte que pour 55 % de son volume : 137 143 × 0,55 = **75 429** : la flotte peut partir.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["FRET<br/>Tout ramener, rien perdre"]:::head
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
        B2H["LIGNES<br/>Toutes vos planètes, une seule base"]:::head
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
        B1H["POUSSÉE<br/>Arriver quand on l'a décidé"]:::head
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

### Poussée : « Arriver quand on l'a décidé »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Postcombustion** | une fois par 24 h, une de vos flottes en vol coupe 25 % du temps qui lui reste, jamais sous 5 min (retour de 1 h → 45 min) | 25 % |
| 2 | 3 rangs | **Réservoirs d'appoint** | Postcombustion se recharge 4 h plus vite par rang : toutes les 12 h au rang 3, deux fois par jour | 3 × 4 h |
| 3 | choix | **A · Route marchande** / **B · Route de chasse** | A : transports, déploiements (Stationnement) et colonisations 10 % plus rapides (accent) <br> B : espionnages et attaques sur cibles abandonnées 10 % plus rapides (accent) ; un trajet de 1 h → 54 min 33 s | 10 % / 10 % |
| 4 | 3 rangs | **Postcombustion poussée** | +5 % du temps restant coupé par rang : 40 % au rang 3 (retour de 1 h → 36 min) | 3 × 5 % |
| 5 | clé | **Formation serrée** | dans une flotte mixte, les vaisseaux lents volent 15 % plus vite, jamais plus vite que le plus rapide (Cargo stellaire 7 500 → 8 625 avec des Intercepteurs à 12 500) | 15 % |
| 6 | choix | **A · Relance** / **B · Mise en attente** | A : une flotte partie à vitesse réduite peut repasser à 100 % en vol, l'hydrogène en plus payé à la relance (une mise à l'abri lancée à 10 % pour 8 h, relancée à mi-chemin : les 4 h restantes deviennent environ 24 min) <br> B : une flotte qui rentre ou en mission pacifique peut ralentir en vol jusqu'à 10 %, l'hydrogène économisé est rendu (30 min restantes deviennent environ 5 h) | déblocage / déblocage |
| 7 | 3 rangs | **Sillage** | Formation serrée +5 % par rang : 30 % au rang 3 (Cargo stellaire 7 500 → 9 750) | 3 × 5 % |
| 8 | clé | **Décollage d'urgence** | une fois par 24 h, quand une attaque pesant au moins 5 % de la puissance de votre flotte à quai arrive sur une de vos planètes (un Éclaireur ne compte pas), la flotte décolle seule 3 min avant l'impact vers votre planète la plus proche. Elle revient à un moment tiré au sort entre 1 h et 3 h après son décollage (fenêtre réglable). Attaque à 4 h 12 : départ à 4 h 09, retour entre 5 h 09 et 7 h 09 | déblocage |
| 9 | ultime | **Saut de retour** | 2 charges par 24 h glissantes : une flotte qui rentre de mission arrive chez elle à l'instant, déchargée comme à un retour normal | 2 charges |

Postcombustion sur une attaque à l'aller : l'alerte du défenseur est mise à jour avec la nouvelle heure d'arrivée. Relance et Mise en attente ne s'appliquent jamais à une Attaque, un Espionnage ou une Destruction de lune à l'aller : une frappe n'arrive jamais à une heure que le défenseur ne voit pas.

### Lignes : « Toutes vos planètes, une seule base »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Navettes** | 2 transports ou stationnements entre vos planètes n'occupent plus d'emplacement de flotte | 2 |
| 2 | 3 rangs | **Soute à carburant** | le carburant du trajet compte 15 % de moins par rang dans la soute : 55 % de son volume au rang 3 (voir l'exemple chiffré) | 3 × 15 % |
| 3 | choix | **A · Plein à l'arrivée** / **B · Réservoir rendu** | A : le carburant d'un transport ou d'un stationnement entre vos planètes peut être payé par la planète d'arrivée ; une planète vidée de son hydrogène peut encore évacuer sa flotte <br> B : une flotte rappelée rapporte la moitié du carburant qu'elle n'a pas brûlé (20 000 H payés aller-retour, rappel à mi-chemin de l'aller : 10 000 H non brûlés, 5 000 H rendus) | déblocage / 50 % |
| 4 | 3 rangs | **Portes chaudes** | vos [Portes de saut](/fr/fleet/jump-gate) se rechargent 10 % plus vite par rang : 30 % au rang 3 (niveau 5 : 36 min → 25 min 12 s ; niveau 14 : 10 min → 7 min) | 3 × 10 % |
| 5 | clé | **Changement de cap** | une fois toutes les 12 h, un transport, un stationnement ou une flotte qui rentre peut être redirigé vers une autre de vos planètes ou lunes du même système, heure d'arrivée inchangée | 12 h |
| 6 | choix | **A · Porte double** / **B · Pont aérien** | A : une Porte de saut fait 2 sauts avant de se recharger <br> B : les transports et stationnements entre vos planètes consomment moitié moins d'hydrogène (200 Navettes de fret vers une colonie d'une autre galaxie : 9 143 → 4 571 H aller-retour) | 2 sauts / 50 % |
| 7 | 3 rangs | **Navettes en plus** | +1 trajet entre vos planètes hors emplacement par rang : 5 au rang 3 | 3 × 1 |
| 8 | clé | **Ascenseur orbital** | un transport ou un stationnement entre une planète et sa lune dure 1 min | 1 min |
| 9 | ultime | **Port d'attache** | toute mission aller-retour peut rentrer à une autre de vos planètes, choisie au départ ; le retour et son carburant suivent le trajet réel | déblocage |

### Fret : « Tout ramener, rien perdre »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Fret retour** | un transport vers une de vos planètes repart chargé d'une cargaison choisie au départ : 20 Cargos stellaires livrent 500 000 de métal et ramènent 500 000 de cristal, un trajet au lieu de deux | déblocage |
| 2 | 3 rangs | **Arrimage** | vos transports et stationnements entre vos planètes emportent 10 % de plus que leur soute par rang : +30 % au rang 3 (20 Cargos stellaires : 500 000 → 650 000) | 3 × 10 % |
| 3 | choix | **A · Livraison groupée** / **B · Cales sans fond** | A : un transport peut livrer deux de vos planètes dans le même vol, la seconde sur la route du retour (50 % chacune, ou la répartition choisie au départ) <br> B : vos [expéditions](/fr/fleet/expeditions) ramènent tout ce qu'elles trouvent, même au-delà de leur soute | déblocage / déblocage |
| 4 | 3 rangs | **Coques civiles** | Navettes de fret, Cargos stellaires et Récupérateurs construits 5 % plus vite par rang : +15 % au rang 3 (accent ; 10 h → 8 h 42) | 3 × 5 % |
| 5 | clé | **Double fond** | une fois par 24 h, une flotte part avec une soute doublée pour toute sa sortie, aller et retour (40 Cargos stellaires : 1 000 000 → 2 000 000) | ×2 |
| 6 | choix | **A · Double fond en vol** / **B · Double fond partagé** | A : Double fond se déclenche aussi sur une flotte déjà en vol, avant son arrivée : vous voyez la cible avant de décider <br> B : Double fond s'applique à 2 flottes parties à moins d'1 min l'une de l'autre | déblocage / 2 flottes |
| 7 | 3 rangs | **Cales préparées** | Double fond se recharge 4 h plus vite par rang : toutes les 12 h au rang 3 | 3 × 4 h |
| 8 | clé | **Fret assuré** | si une de vos flottes de transport est détruite, la moitié de sa cargaison revient à sa planète de départ ; l'attaquant n'en gagne rien de plus (30 Cargos stellaires chargés de 750 000 : 375 000 sauvés) | 50 % |
| 9 | ultime | **Razzia** | une fois par 24 h, une attaque gagnée sur une cible abandonnée emporte tout ce qui est pillable au lieu de la part habituelle (3 000 000 en stock : 1 500 000 au taux de 50 % → 3 000 000, dans la limite de la soute) | 100 % |

Razzia ne touche que les cibles abandonnées (joueurs inactifs, mondes en ruine, adversaires contrôlés par le jeu), jamais un joueur actif.

### Ce que 25 points donnent

| Build | Répartition | Ressenti |
|---|---|---|
| **Coureur** | Poussée 15 · Lignes 10 | Saut de retour, Postcombustion deux fois par jour à 40 %, Formation serrée à 30 %, Décollage d'urgence ; 2 navettes hors emplacement, carburant allégé, Changement de cap |
| **Logisticien d'empire** | Lignes 15 · Fret 10 | Port d'attache, 5 navettes hors emplacement, Ascenseur orbital, Pont aérien ou Porte double ; Fret retour, +30 % de chargement entre vos planètes, Livraison groupée, Double fond |
| **Pilleur de fermes** | Fret 15 · Poussée 10 | Razzia, Double fond toutes les 12 h (en vol ou sur deux flottes), Fret assuré ; Postcombustion, Route de chasse, Formation serrée à 15 % |

## Pièges fréquents

- **Le carburant prend de la place en soute** : sans Soute à carburant, une flotte de combat lointaine peut ne pas pouvoir partir faute de soute.
- **Formation serrée nivelle les vitesses** : tous les vaisseaux sauf le plus rapide volent 15 % plus vite, sans jamais dépasser le plus rapide. La flotte avance toujours à la vitesse du plus lent. Une flotte d'un seul type n'en profite pas.
- **Route de chasse ne vise que les cibles abandonnées** : une attaque contre un joueur actif garde sa vitesse normale.
- **Relance et Mise en attente** ne marchent pas sur une attaque à l'aller.
- **Navettes** : seuls les transports et stationnements entre vos propres planètes sont hors emplacement.

## Pages liées

- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Déplacements](/fr/fleet/movement)
- [Porte de saut](/fr/fleet/jump-gate)
- [Expéditions](/fr/fleet/expeditions)
- [Pillage](/fr/combat/plunder)
