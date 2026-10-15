---
wiki_id: 157
locale: "fr"
path: "dynasty/classes/shadow"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/shadow"
title: "L'Ombre"
description: "Arbre de classe de l'Ombre : Pénétration, Discrétion et Contre-jour."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:49.095Z"
updated: "2026-10-15T18:57:28.237Z"
---

# L'Ombre

> **En bref** : l'Ombre joue les deux sens du renseignement : lire chez les autres sans se faire prendre, et rendre son propre territoire illisible. Ses talents sont des règles, pas des pourcentages génériques, et elle n'a aucun accent.
{.is-info}

## Règles

1. L'Ombre est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **trois branches** : Pénétration, Discrétion et Contre-jour.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. Les talents de l'Ombre s'appuient sur les règles de l'[espionnage](/fr/espionage/spying) : niveau effectif = écart de Renseignement Tactique + 1 par paire d'Éclaireurs (+5 au plus) ; paliers du rapport : ressources dès 1, flotte dès 3, défenses et missiles dès 5, bâtiments dès 7, recherches dès 9 ; chance de détection bornée entre 5 % et 25 %, nulle si votre Renseignement Tactique vaut au moins le double de celui de la cible ou si l'orbite est vide.
5. Les points de détection (Basse signature pour l'espion, Sentinelles pour la cible) s'appliquent **avant** la borne de 5 % à 25 % : ils ne font jamais descendre la chance sous 5 % ni monter au-delà de 25 %, et ne créent pas de chance là où elle est nulle.
6. La **profondeur** (Sondes économes, Le seuil, Brouillage) ne change jamais la chance de détection.
7. Une vague **prise** est identifiée (le défenseur apprend votre pseudo) ; un second tirage peut la **tracer** (il apprend aussi la planète d'origine). Le défenseur reçoit une alerte d'intrusion à chaque vague, même non détectée.

## Exemple chiffré

**Le risque d'une vague, des deux côtés**
- Cible : Renseignement Tactique 8, 40 vaisseaux en orbite. Espion : Renseignement Tactique 8. Chance : (2 × 8 − 8) × 40 × 0,05 = **16 %**.
- L'espion a Basse signature au rang 3 : 16 − 6 = **10 %**. Sa Prudence (15 %) ne le fait pas renoncer.
- Si la cible a Sentinelles au rang 3 : 16 + 6 − 6 = **16 %** : la vague fait demi-tour.
- Contre une cible à 8 % : 8 − 6 = 2, relevé à la borne : **5 %**.

**Lire les défenses avec 4 Éclaireurs, à Renseignement Tactique égal**
- Sans talent : 4 Éclaireurs donnent +2 ; niveau effectif 2 : seules les ressources se lisent.
- Sondes économes au rang 3 : la vague compte pour 4 + 6 = 10 Éclaireurs, soit +5 ; niveau 5 : ressources, flotte, défenses et missiles.
- Si la cible a Brouillage : niveau 4, les défenses restent fermées. Avec Le seuil en plus : 5 à nouveau.

**Une vague de 9 Éclaireurs prise**
- Sondes larguées seule : 9 × 20 % = 1,8, arrondi à l'inférieur : **1** rentre, 8 sont perdus.
- Avec Coques muettes au rang 3 : 9 × 41 % = 3,69 : **3** rentrent.
- Sans adresse et Coques muettes au rang 3 : 9 × 21 % = 1,89 : **1** rentre.

**Flotte voilée** : 117 Corvettes sont lues 120 ; 1 234 Intercepteurs, 1 200 ; 19 Cuirassés, 19.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["CONTRE-JOUR<br/>Votre territoire ne se lit pas."]:::head
        B3R1{{"Orbite gardée<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Sentinelles<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Alerte partagée<br/>1 pt"]:::option
        B3R3B["② Rapport d'incident<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Coffre caché<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Lumière dans le dos<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Sentinelles de lune<br/>1 pt"]:::option
        B3R6B["② Flotte voilée<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Filature<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Brouillage<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Retour de sonde<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["DISCRÉTION<br/>Entrer, lire, repartir."]:::head
        B2R1{{"Le risque mesuré<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Basse signature<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Sondes larguées<br/>1 pt"]:::option
        B2R3B["② Sans adresse<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Coques muettes<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Prudence<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Silhouette<br/>1 pt"]:::option
        B2R6B["② Écran de fumée<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Fausse piste<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Le vide parfait<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Ni vu ni connu<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["PÉNÉTRATION<br/>Ce que le rapport dit."]:::head
        B1R1{{"Stock à l'arrivée<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Sondes économes<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Lecture des cales<br/>1 pt"]:::option
        B1R3B["② Lecture des hangars<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Dossier vivant<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Regard en orbite<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Repérage de système<br/>1 pt"]:::option
        B1R6B["② Lecture de combat<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Rapport d'activité<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Le seuil<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Mouchard<br/>ultime"]]:::ultimate
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

### Pénétration

*Ce que le rapport dit.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Stock à l'arrivée** | clé | Chaque rapport calcule ce que la planète aura en stock quand votre raid y arrivera, production comprise et sous ses hangars : vous savez ce que vous pillerez. |  |
| 2 | **Sondes économes** | 3 rangs | Votre vague compte pour 6 sondes de plus dans la profondeur, sans jamais dépasser les +5 niveaux tirés des sondes : les bâtiments se lisent avec bien moins de sondes. | 3 × 2 |
| 3 | **A · Lecture des cales** | choix | Les ressources s'ouvrent 1 palier plus tôt : elles se lisent toujours, même avec un écart négatif et une seule sonde. | |
|  | **B · Lecture des hangars** |  | La flotte s'ouvre 1 palier plus tôt : à écart égal, moins de sondes suffisent à la lire. | |
| 4 | **Dossier vivant** | 3 rangs | Chaque nouveau rapport reprend les sections que vos rapports des dernières 24 h avaient lues, datées : une vague complète le matin, des passages légers ensuite gardent bâtiments et défenses. | 3 × 8 h |
| 5 | **Regard en orbite** | clé | Une vague lit aussi l'autre corps de la case (la lune d'une planète, la planète d'une lune), 2 niveaux plus bas, dans un second rapport. C'est là que se cachent les flottes à l'abri. |  |
| 6 | **A · Repérage de système** | choix | La vague liste aussi les autres planètes du système, « actif » ou « inactif », avec une fourchette de stock : on trouve ses fermes en un seul passage. | |
|  | **B · Lecture de combat** |  | Armes, bouclier et coque de la cible se lisent dès le palier de la flotte (3) au lieu de celui des recherches (9) : on simule sans vague complète. | |
| 7 | **Rapport d'activité** | 3 rangs | Le rapport dit quand la cible a joué pour la dernière fois, avec 3 degrés de précision : dans l'heure, dans la journée ou plus tôt ; puis à 15 min près ; puis sur quelle planète. On frappe quand elle dort. | 3 × 1 |
| 8 | **Le seuil** | clé | Vos rapports lisent 1 niveau effectif de plus, profondeur seule, jamais compté par le jet de détection. |  |
| 9 | **Mouchard** | ultime | Une vague non détectée peut laisser une sonde en orbite 6 h. Elle vous envoie un rapport ressources et flotte chaque fois que la flotte au sol change (départ, retour, mise à l'abri). Chaque envoi rejoue la détection à 50 % de la chance ; prise, elle est détruite. |  |

- **Stock à l'arrivée** : quand la section ressources se lit, le rapport donne aussi la production horaire et les entrepôts de la cible, pour projeter le stock à l'arrivée de votre raid.
- **Sondes économes** : il faut au moins 1 Éclaireur dans la vague ; le bonus tiré des Éclaireurs reste plafonné à +5.
- **Lecture des cales** : les ressources se lisent toujours, même avec un écart négatif et un seul Éclaireur. **Lecture des hangars** : la flotte se lit dès le niveau effectif 2 ; avec Écouter loin de [L'Accord](/fr/dynasty/dynasties), dès 1.
- **Dossier vivant** : seules les sections du même corps (la planète ou sa lune) sont reprises ; le jeu garde les 10 derniers rapports par case.
- **Regard en orbite** : le second rapport a le même résultat de détection que la vague.
- **Repérage de système** : seules les planètes sont listées, avec le pseudo, le statut (actif, inactif, abandonnée, en vacances) et une fourchette du stock total : moins de 10 000, 10 000, 50 000, 100 000, 250 000, 500 000, 1 000 000, 2 500 000, 5 000 000 et plus. Pas de stock pour un joueur en vacances.
- **Lecture de combat** donne Systèmes Offensifs, Champs de Protection et Métallurgie Avancée tant que la flotte se lit et pas les recherches ; le palier de la flotte suit Lecture des hangars.
- **Rapport d'activité** : présent même dans un rapport qui ne lit rien d'autre (pas sur une base abandonnée). Au rang 2, l'heure est arrondie au quart d'heure inférieur ; au rang 3, la base que le joueur a sélectionnée en dernier.
- **Mouchard** : se demande à l'envoi. L'Éclaireur laissé en orbite est perdu pour votre flotte. Il fait un rapport à chaque départ ou arrivée de flotte sur la base. Pris, il est détruit et l'alerte du défenseur vous nomme, sans donner votre planète. Un seul par base visée : en reposer un relance les 6 h.

### Discrétion

*Entrer, lire, repartir.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Le risque mesuré** | clé | L'écran d'envoi et chaque rapport affichent la chance de détection que la vague affronte : vous voyez le risque avant de partir. |  |
| 2 | **Basse signature** | 3 rangs | Vos vagues ont 6 pts de chance en moins d'être détectées. Le plafond d'une cible bien gardée s'applique après. | 3 × 2 pts |
| 3 | **A · Sondes larguées** | choix | 20 % des sondes d'une vague prise survivent et rentrent. | |
|  | **B · Sans adresse** |  | Une vague prise est identifiée mais jamais tracée : le défenseur apprend qui, jamais d'où. | |
| 4 | **Coques muettes** | 3 rangs | Les sondes d'une vague prise gagnent 21 % de survie : davantage rentrent. | 3 × 7 % |
| 5 | **Prudence** | clé | Une vague qui affronte 15 % de risque ou plus fait demi-tour avant l'orbite : ni rapport, ni perte, ni alerte. Elle vous a appris que la cible est gardée. Désactivable à l'envoi. |  |
| 6 | **A · Silhouette** | choix | Les phalanges adverses voient vos flottes, mais pas leur composition ni leur cargaison. | |
|  | **B · Écran de fumée** |  | Vos attaques apparaissent chez la cible comme « flotte inconnue », sans nombre de vaisseaux, jusqu'à 15 min de l'impact. | |
| 7 | **Fausse piste** | 3 rangs | Une vague tracée a 90 % de chances de donner au défenseur une fausse origine : une planète inactive de votre galaxie. | 3 × 30 % |
| 8 | **Le vide parfait** | clé | Une vague qui ne courait aucun risque (cible deux fois moins avancée, ou orbite vide) ne laisse qu'une trace vague : « activité repérée dans votre système », sans planète, sans nom, à l'heure près. |  |
| 9 | **Ni vu ni connu** | ultime | Une fois par jour, une vague prise n'est pas abattue : elle échappe à la défense et toutes ses sondes rentrent. |  |

- **Le risque mesuré** : l'écran d'envoi calcule la chance au moment de l'envoi ; le tirage se fait à l'arrivée des Éclaireurs.
- **Sondes larguées** et **Coques muettes** s'additionnent ; le nombre d'Éclaireurs sauvés est arrondi à l'inférieur, un Éclaireur seul ne rentre jamais. Sans adresse étant l'autre choix, la survie est alors de 21 % au plus.
- **Prudence** : compare la chance bornes comprises. La vague a fait le vol aller-retour et payé son hydrogène. Vous recevez une notification.
- **Silhouette** : vaut pour tout balayage de Phalange de capteur, y compris ceux partagés en alliance.
- **Écran de fumée** : seulement les Attaques à l'aller, pour tout autre joueur (cible et Phalanges).
- **Fausse piste** : la fausse origine est une planète d'un joueur inactif de votre galaxie ; s'il n'y en a aucune, la vraie origine est donnée. Inutile avec Sans adresse, puisque la vague n'est jamais tracée.
- **Le vide parfait** : « aucun risque » veut dire une chance de 0 % ; une cible qui a Orbite gardée garde ses orbites vides à 5 %. Le défenseur reçoit « activité repérée » dans son système, à l'heure près, au lieu de l'alerte.
- **Ni vu ni connu** : se déclenche seul sur la **première** vague prise du cycle. Elle reste prise : le défenseur reçoit son alerte et peut la tracer.

### Contre-jour

*Votre territoire ne se lit pas.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Orbite gardée** | clé | Le contre-espionnage joue même sur une orbite vide, au plancher de 5 % : vos colonies sans flotte ne sont plus un livre ouvert. |  |
| 2 | **Sentinelles** | 3 rangs | Les vagues sur vos planètes ont 6 pts de chance en plus d'être détectées. | 3 × 2 pts |
| 3 | **A · Alerte partagée** | choix | Vos alertes d'intrusion sont copiées à toute votre alliance. | |
|  | **B · Rapport d'incident** |  | Une intrusion non détectée vous dit quand même combien de sondes, et de quelle galaxie. | |
| 4 | **Coffre caché** | 3 rangs | Les rapports ennemis sur vos planètes et lunes affichent 30 % de stock en moins. Le stock reste pillable : l'attaquant vient avec trop peu de soutes. | 3 × 10 % |
| 5 | **Lumière dans le dos** | clé | Vous êtes prévenu quand une phalange balaie l'une de vos planètes, et par qui. |  |
| 6 | **A · Sentinelles de lune** | choix | Le contre-espionnage d'une planète compte aussi les vaisseaux de sa lune, et l'inverse. | |
|  | **B · Flotte voilée** |  | Les rapports ennemis donnent votre flotte arrondie à 10 % près : « ≈ » devant chaque nombre. | |
| 7 | **Filature** | 3 rangs | Une vague détectée a 15 pts de chance en plus d'être tracée : l'espion laisse son adresse. | 3 × 5 pts |
| 8 | **Brouillage** | clé | Les rapports adverses sur vos planètes lisent 1 niveau effectif plus bas, profondeur seule : de quoi annuler Le seuil d'une Ombre d'en face. |  |
| 9 | **Retour de sonde** | ultime | Une vague tracée vous rapporte, sans sonde et sans que l'espion le sache, un rapport sur sa planète d'origine, lu au palier 3 : ressources et flotte. |  |

- **Orbite gardée** : l'écart de Renseignement Tactique doit rester en votre faveur. Avec Sentinelles au rang 3, une orbite vide est gardée à 6 %.
- **Alerte partagée** : chaque alerte d'intrusion reçue est copiée en notification aux autres membres de votre alliance.
- **Coffre caché** : chaque ressource est lue à 70 % au rang 3 (arrondi à l'inférieur), dans tout rapport d'un autre joueur sur vos bases : vague, Mouchard, Retour de sonde, Repérage de système.
- **Lumière dans le dos** : vous apprenez le pseudo et la lune du joueur. Rien contre un Oracle qui a Balayage silencieux.
- **Sentinelles de lune** : seulement si vous possédez aussi l'autre corps de la case.
- **Flotte voilée** : chaque nombre de vaisseaux est arrondi par pas de 1, 10, 100… selon sa taille ; sous 20 vaisseaux d'un type, le nombre reste exact.
- **Brouillage** ne joue pas sur un Mouchard, qui lit toujours au palier 3.
- **Retour de sonde** : seulement sur une vague tracée. Le rapport lit la planète d'origine, ou la fausse origine si Fausse piste a joué. L'espion reçoit « activité repérée » dans son système, à l'heure près.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| Les ressources sont lisibles 1 palier plus tôt dans vos rapports d'espionnage | 1 |
| La flotte est lisible 1 palier plus tôt dans vos rapports d'espionnage | 1 |
| +1 niveau de profondeur pour vos rapports d'espionnage, jamais pour le jet de détection | 1 |
| −6 pts de chance d'être détecté pour vos vagues d'espionnage | 6 pts |
| +41 % des sondes d'une vague prise survivent et rentrent | 41 % |
| +6 pts de chance de détecter les vagues sur vos planètes | 6 pts |
| +15 pts de chance de tracer une vague détectée jusqu'à sa planète d'origine | 15 pts |
| Les rapports adverses sur vos planètes lisent 1 niveau effectif plus bas, profondeur seule | 1 |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chasseur | Pénétration 15 · Discrétion 10 | Mouchard, Lecture de combat ou Repérage de système, Le seuil, activité à la base près, Dossier vivant de 24 h ; −6 points de détection, Prudence, survie 41 % (ou Sans adresse), Silhouette (Phalanges sans composition) ou Écran de fumée |
| Fantôme | Discrétion 15 · Pénétration 10 | Ni vu ni connu, Le vide parfait, Fausse piste à 90 %, survie 41 % ; Stock à l'arrivée, bâtiments lus avec 4 Éclaireurs si votre Renseignement Tactique a 2 niveaux d'avance, Dossier vivant de 24 h, Regard en orbite |
| Gardien | Contre-jour 15 · Discrétion 10 | Retour de sonde, Brouillage, stock lu à 70 %, Filature +15 points, Orbite gardée ; ses propres vagues à −6 points avec Prudence |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Écouter loin et Lecture des hangars se cumulent** : une Ombre de L'Accord qui prend Lecture des hangars lit la flotte **deux paliers** plus tôt.
- **Le seuil ne réduit pas le risque** : il ajoute de la profondeur, jamais de discrétion.
- **Basse signature bute sur la borne de 5 %** : contre une cible peu gardée, une partie des 6 points ne sert à rien.
- **Plus de « toutes ou aucune »** : avec Sondes larguées et Coques muettes, une partie des Éclaireurs d'une vague prise rentre. Sans ces talents, toute la vague tombe ; un Éclaireur seul ne rentre jamais.
- **Sans adresse et Fausse piste ne vont pas ensemble** : une vague jamais tracée n'a pas d'origine à fausser.
- **Ni vu ni connu part tout seul** sur la première vague prise du cycle, même une vague d'un seul Éclaireur.
- **Mouchard coûte un Éclaireur** à chaque pose.
- **Coffre caché ne protège rien** : il fausse le rapport ennemi, le stock reste entièrement pillable.
- **Brouillage annule Le seuil** : contre une Ombre qui a pris Contre-jour jusqu'à la rangée 8, votre niveau effectif en plus disparaît.
- **Retour de sonde se remarque** : l'espion apprend qu'il y a eu de l'activité dans son système.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Dynasties](/fr/dynasty/dynasties)
- [Espionner](/fr/espionage/spying)
- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
