---
wiki_id: 156
locale: "fr"
path: "dynasty/classes/oracle"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/oracle"
title: "L'Oracle"
description: "La classe de l'information anticipée, exclusive à L'Accord : Veille, Présage et Préavis."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:46.872Z"
updated: "2026-10-07T22:08:26.135Z"
---

# L'Oracle

> **En bref** : l'Oracle ne frappe pas plus fort, il sait avant. Chacune de ses branches vend une information, jamais une statistique : Veille regarde bouger les flottes depuis une lune, Présage prépare les raids, Préavis évite d'être là quand le coup tombe.
{.is-info}

## Règles

1. L'Oracle est une classe **exclusive à [L'Accord](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Veille, Présage et Préavis.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. La protection générique contre le pillage et la vitesse de retour des flottes viennent de l'[arbre commun](/fr/dynasty/common-tree). L'Oracle n'y ajoute que deux **accents** étroits : Frappe préparée (vitesse des attaques, dans l'accent de vitesse de 10 % de la classe) et La cache (protection contre le pillage, 10 points au plus avec Coffres enterrés). Le pistage des espions appartient à l'[Ombre](/fr/dynasty/classes/shadow).
5. Sans talent, seule une mission **Attaque** est annoncée, **60 s** avant l'impact, ou dès son départ si le vol dure moins. Le délai d'une flotte est fixé **à son départ**, d'après vos talents à ce moment ; une flotte accélérée en vol garde le même délai sur sa nouvelle heure d'impact. Dans le temps gagné avant les 60 s, l'alerte ne donne que la base visée et l'heure d'arrivée à la minute près ; l'heure exacte et l'origine arrivent à 60 s, sauf avec Heure juste. L'alerte ne donne jamais la composition de la flotte.
6. La [Phalange de capteur](/fr/espionage/sensor-phalanx) se construit sur une lune et ne vise jamais une lune. Un balayage coûte 5 000 hydrogène, sauf celui de Balayage réflexe, et il est impossible en mode vacances. Il montre seulement les **mouvements** (flottes qui partent de la planète ou y arrivent), jamais les vaisseaux posés, ni les missions d'espionnage et de recyclage. Par défaut, personne n'est prévenu d'un balayage : seule l'Ombre, avec Lumière dans le dos, l'apprend.
7. Les lectures de Présage partent de **vos** rapports d'espionnage. La part pillable y est calculée à votre taux de pillage (50 % sur Redline, plus vos talents contre une cible abandonnée), **sans** la protection du défenseur, que le rapport ne montre pas : c'est un maximum.

## Exemple chiffré

**Délai d'alerte selon les talents de Préavis**

| Talents pris | Délai avant l'impact |
|---|---|
| aucun | 1 min |
| Oreille tendue | 2 min 30 |
| + Tour de garde au rang 3 | 3 min 30 |
| + Veilleurs de quart au rang 3 | 4 min 30 |
| + Le grand préavis (branche pleine) | 6 min |

Une attaque dont le vol dure 75 s est annoncée à son départ, 75 s avant l'impact : Garde prévenue, qui demande 90 s, ne joue pas.

**Phalange de capteur niveau 3 avec Longue-vue et Lentilles au rang 3**
- Portée : la Phalange porte comme un niveau 4, soit 4² − 1 = **15 systèmes** de part et d'autre, au lieu de 8.
- Coût d'un balayage : 5 000 × (1 − 0,24) = **3 800 hydrogène**.
- Avec Vue d'empire, un joueur qui a 3 planètes à portée se balaie en entier pour 3 800 hydrogène au lieu de 11 400.
- Avec Relais de lunes et une autre lune au système 70, une Phalange niveau 4 au système 40 (portée d'un niveau 5 : 24 systèmes) balaie les planètes des systèmes 16 à 64 **et** 46 à 94 de la même galaxie.

**Pesée** : le rapport lit 1 200 000 métal, 800 000 cristal et 300 000 hydrogène. À 50 %, la part pillable est 600 000 + 400 000 + 150 000 = **1 150 000**.
- Sans Pliage Spatial : 1 150 000 / 25 000 = **46 Cargos stellaires**, ou 1 150 000 / 5 000 = **230 Navettes de fret**.
- Pliage Spatial niveau 5 (+25 % de soute) : un Cargo stellaire porte 31 250, il en faut 36,8, arrondi à **37** ; une Navette de fret porte 6 250, il en faut **184**.
- Avec en plus Cales élargies (+10 %) : 34 375 par Cargo stellaire, soit **34**.

**Dénombrement** : l'alerte arrondit la valeur de la flotte (coût de ses vaisseaux en métal, cristal et hydrogène) au multiple le plus proche de la moitié de sa puissance de dix.
- 200 Cuirassés (60 000 chacun) et 50 Cargos stellaires (12 000 chacun) : 12 600 000, affiché **15 000 000**.
- 1 200 Intercepteurs (4 000 chacun) : 4 800 000, affiché **5 000 000**.

**La cache** : 2 000 000 de ressources en stock. Un raid gagnant emporte 50 % sans talent, soit 1 000 000 ; avec La cache, 45 %, soit **900 000** ; avec en plus Coffres enterrés, 40 %, soit **800 000**.

**Frappe préparée** : un trajet de 60 min sans autre bonus de vitesse dure 60 / 1,09, soit environ **55 min 3 s**, si l'attaque part au plus 30 min après votre dernier rapport sur la cible.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["PRÉAVIS<br/>Ne pas être là quand le coup tombe."]:::head
        B3R1{{"Oreille tendue<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Garde prévenue<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Gabarit ennemi<br/>1 pt"]:::option
        B3R3B["② Heure juste<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Tour de garde<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Le colosse annoncé<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Dénombrement<br/>1 pt"]:::option
        B3R6B["② Repli éclair<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Veilleurs de quart<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"La cache<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Le grand préavis<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["PRÉSAGE<br/>Savoir avant de frapper."]:::head
        B2R1{{"Pesée<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Carnet de fermes<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Mesure de l'écart<br/>1 pt"]:::option
        B2R3B["② Lecture des classements<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Œil du raid<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Butin prévu<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Tournée de fermes<br/>1 pt"]:::option
        B2R6B["② Bilan de chasse<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Frappe préparée<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Le choc annoncé<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Le plan de raid<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["VEILLE<br/>Voir bouger les flottes."]:::head
        B1R1{{"Longue-vue<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Lentilles<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Veille partagée<br/>1 pt"]:::option
        B1R3B["② Lune et planète<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Mémoire de phalange<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Le retour annoncé<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Balayage silencieux<br/>1 pt"]:::option
        B1R6B["② Relais de lunes<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Regard prolongé<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"Vue d'empire<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Balayage réflexe<br/>ultime"]]:::ultimate
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

### Veille

*Voir bouger les flottes.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Longue-vue** | clé | Votre phalange porte comme si elle avait 1 niveau de plus : elle couvre davantage de systèmes. |  |
| 2 | **Lentilles** | 3 rangs | Vos balayages de phalange coûtent 24 % d'hydrogène en moins. | 3 × 8 % |
| 3 | **A · Veille partagée** | choix | Chacun de vos balayages de phalange est remis à toute votre alliance. | |
|  | **B · Lune et planète** |  | Un balayage montre aussi les flottes qui partent de la lune de la planète ou y arrivent, là où les joueurs mettent leur flotte à l'abri. | |
| 4 | **Mémoire de phalange** | 3 rangs | Les flottes vues par un balayage restent suivies, avec leur heure d'arrivée, 3 h après la fin du balayage. | 3 × 1 h |
| 5 | **Le retour annoncé** | clé | Une attaque annoncée vous dit aussi à quelle heure la flotte ennemie sera rentrée chez elle : vous savez combien de temps son port reste vide. |  |
| 6 | **A · Balayage silencieux** | choix | Vos balayages ne sont jamais annoncés à la planète balayée, quels que soient les talents de son propriétaire. | |
|  | **B · Relais de lunes** |  | Une planète à portée de n'importe laquelle de vos lunes peut être balayée depuis votre lune à phalange. | |
| 7 | **Regard prolongé** | 3 rangs | Un balayage reste ouvert 30 min : les flottes qui partent de la planète ou y arrivent pendant ce temps s'ajoutent à son relevé. | 3 × 10 min |
| 8 | **Vue d'empire** | clé | Un balayage montre aussi les flottes de toutes les autres planètes du même joueur à portée, pour le prix d'un seul. |  |
| 9 | **Balayage réflexe** | ultime | Quand une attaque contre vous est annoncée, une de vos lunes à portée balaie gratuitement la planète d'où elle est partie : vous voyez ce qui y reste et ce qui y rentre. |  |

- **Longue-vue** n'agit que sur une Phalange déjà construite : (niveau + 1)² − 1 systèmes.
- **Veille partagée** : les autres membres de votre alliance reçoivent une notification avec ce que le balayage a vu. Rien sans alliance.
- **Lune et planète** vaut pour tous vos balayages, ceux de Regard prolongé, Vue d'empire et Balayage réflexe compris.
- **Mémoire de phalange** suit les flottes en direct, retour compris, jusqu'à 3 h après la fin du balayage (après sa fermeture pour un balayage resté ouvert).
- **Le retour annoncé** est une information d'alerte : il marche sans lune. L'heure donnée suppose que la flotte rentre tout droit ; un retour plus rapide peut la ramener plus tôt.
- **Balayage silencieux** ne sert que contre un joueur qui a Lumière dans le dos : sans lui, aucun balayage n'est signalé.
- **Relais de lunes** : la portée de votre Phalange se mesure aussi depuis chacune de vos autres lunes, même sans Phalange.
- **Regard prolongé** ne s'ouvre jamais sur votre propre planète.
- **Vue d'empire** ajoute les autres **planètes** du joueur à portée de la lune à Phalange (ou des relais) ; sans effet sur vos propres planètes.
- **Balayage réflexe** : c'est votre lune la plus proche dont la Phalange atteint la planète de départ qui balaie, relais compris. Il faut une Phalange bâtie sur cette lune. Le relevé montre les mouvements de cette planète au moment où vous lisez l'alerte.

### Présage

*Savoir avant de frapper.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Pesée** | clé | Chaque rapport d'espionnage indique combien de transporteurs il faut pour emporter la part pillable. |  |
| 2 | **Carnet de fermes** | 3 rangs | Vous suivez 15 cibles. Le jeu projette leur stock d'après vos deux derniers rapports et vous prévient quand la part pillable atteint le seuil choisi. | 3 × 5 |
| 3 | **A · Mesure de l'écart** | choix | Le rapport dit combien de sondes il faut pour lire le palier suivant : plus de vague à l'aveugle. | |
|  | **B · Lecture des classements** |  | Un rapport trop court pour le simulateur reçoit une tendance de défense (probablement vide, inconnue, dangereuse) au lieu d'un refus. | |
| 4 | **Œil du raid** | 3 rangs | Vos rapports de combat en attaque lisent la cible comme une sonde, sur 3 paliers : d'abord le stock restant après pillage, puis les bâtiments, puis les recherches que vos sondes auraient pu lire. | 3 × 1 |
| 5 | **Butin prévu** | clé | Le simulateur donne aussi le butin attendu, au plus : la part pillable bornée par les soutes de vos vaisseaux survivants. |  |
| 6 | **A · Tournée de fermes** | choix | Choisissez jusqu'à 5 fermes : le jeu répartit vos transporteurs entre elles selon leur part pillable et prépare les envois. | |
|  | **B · Bilan de chasse** |  | Le simulateur donne le champ de débris attendu et le gain net de vos pertes. | |
| 7 | **Frappe préparée** | 3 rangs | Une attaque lancée moins de 30 min après votre rapport sur la cible va 9 % plus vite. | 3 × 3 % |
| 8 | **Le choc annoncé** | clé | Une attaque contre vous reçoit un verdict, tenir ou tomber, tiré des classements militaires publics ; simulé contre la vraie flotte quand votre préavis en mesure la puissance. |  |
| 9 | **Le plan de raid** | ultime | Depuis un rapport qui a lu la flotte, le jeu propose la plus petite flotte, prise sur la base de votre choix, qui gagne au moins 9 combats simulés sur 10 et emporte toute la part pillable. |  |

- **Pesée** compte les soutes de vos Navettes de fret et Cargos stellaires avec votre Pliage Spatial et vos talents de soute, arrondi au-dessus.
- **Carnet de fermes** : une cible est une planète ou une lune, avec un seuil de part pillable totale. Le stock est prolongé au rythme mesuré entre vos deux derniers rapports, sans plafond de hangars ; une ressource qui a baissé compte pour 0. Une notification par rapport. Le nœud donne aussi cette projection sur chaque rapport. Après une réinitialisation qui laisse moins de places, seules les premières cibles comptent.
- **Mesure de l'écart** s'appuie sur ce que vos vagues précédentes sur ce corps ont prouvé.
- **Lecture des classements** s'affiche sur la lecture du rapport ; le simulateur, lui, refuse toujours un rapport qui n'a pas lu la flotte. « Dangereuse » : le propriétaire a plus de points militaires publics que vous. « Probablement vide » : le stock lu est sous 10 000 et vous avez au moins 1,2 fois ses points militaires. « Inconnue » sinon.
- **Œil du raid** : les recherches ne s'affichent au rang 3 que si vos Éclaireurs pouvaient les lire chez ce défenseur. Jamais la flotte ni les défenses.
- **Butin prévu** et **Bilan de chasse** donnent des moyennes sur les combats simulés.
- **Tournée de fermes** répartit les Cargos stellaires et Navettes de fret d'**une** base choisie ; une ferme dont le rapport n'a pas lu le stock est écartée. Vous lancez les envois.
- **Frappe préparée** : mission Attaque seulement, pas une destruction de lune ; c'est votre rapport le plus récent sur ce corps précis (planète ou lune) qui compte. La vitesse divise la durée.
- **Le choc annoncé** : trois verdicts, tenir, tomber ou inconnu. Sans Dénombrement, « tomber » si l'attaquant a plus de points militaires publics que vous, « inconnu » s'il manque un classement. Avec Dénombrement, 20 combats simulés contre la vraie flotte et vos défenses du moment, Garde prévenue comprise : « tenir » si l'attaquant en gagne moins de la moitié. Seul le verdict est montré.
- **Le plan de raid** cherche la plus petite part, par vingtièmes, de toute la flotte de combat de la base choisie (chaque type gardé), puis ajoute les Cargos stellaires et Navettes de fret de cette base, dans la limite de ce qui y stationne. Sans recherches lues dans le rapport, le défenseur est supposé à vos niveaux. Si toute la flotte de combat ne suffit pas, aucun plan n'est proposé.

### Préavis

*Ne pas être là quand le coup tombe.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Oreille tendue** | clé | Les attaques contre vous sont annoncées 90 s plus tôt, en plus des 60 s de préavis que le jeu donne à tous. |  |
| 2 | **Garde prévenue** | 3 rangs | Si le préavis est tombé au moins 90 s avant l'impact, les défenses et les vaisseaux de la planète gagnent 6 % de bouclier et 6 % de dégâts, contre les attaques seulement. | 3 × 2 % |
| 3 | **A · Gabarit ennemi** | choix | Le préavis donne la taille de la flotte ennemie (petite, moyenne, grande, écrasante), pour décider de tenir ou de fuir. | |
|  | **B · Heure juste** |  | Le préavis donne dès sa première seconde l'heure d'arrivée exacte et l'origine, pour partir à la dernière seconde. | |
| 4 | **Tour de garde** | 3 rangs | Vos préavis d'attaque gagnent encore 60 s. | 3 × 20 s |
| 5 | **Le colosse annoncé** | clé | Les destructions de lune visant vos lunes sont annoncées comme les attaques, avec le même préavis. |  |
| 6 | **A · Dénombrement** | choix | Le préavis donne la puissance de la flotte ennemie à 25 % près, jamais ses vaisseaux. | |
|  | **B · Repli éclair** |  | Une flotte qui quitte une planète visée par une attaque annoncée va 20 % plus vite et brûle 50 % d'hydrogène en moins. | |
| 7 | **Veilleurs de quart** | 3 rangs | Vos préavis d'attaque gagnent 60 s. | 3 × 20 s |
| 8 | **La cache** | clé | Le pillage que vous subissez baisse de 5 points : une part de chaque ressource reste hors de portée des raids. |  |
| 9 | **Le grand préavis** | ultime | Vos préavis d'attaque gagnent encore 90 s : l'alerte tombe bien avant l'impact. |  |

- **Garde prévenue** : +2 % de bouclier et +2 % de dégâts par rang, pour les vaisseaux posés et les défenses de la base attaquée, si l'alerte de **cette** attaque est réellement tombée 90 s avant l'impact. L'attaquant ne la voit pas dans son simulateur.
- **Gabarit ennemi** : petite sous 100 000 de valeur (coût des vaisseaux en ressources), moyenne sous 1 000 000, grande sous 10 000 000, écrasante au-delà.
- **Le colosse annoncé** : sans ce nœud, une destruction de lune n'est pas annoncée du tout.
- **Dénombrement** : l'écart entre la valeur affichée et la vraie ne dépasse pas 20 % de la vraie. Pris avec Gabarit ennemi, c'est l'estimation qui s'affiche.
- **Repli éclair** : toute flotte, quelle que soit sa mission, qui quitte le corps visé (planète ou lune) pendant qu'une attaque **déjà annoncée** vole vers lui. Sa vitesse et sa réduction s'appliquent après tous les autres bonus, hors plafonds.
- **La cache** vaut sur toutes vos bases ; le taux de pillage ne descend jamais sous 30 %.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| La phalange porte comme si elle avait +1 niveau | 1 |
| −24 % de coût en hydrogène d'un balayage de phalange | 24 % |
| Un balayage de phalange reste ouvert 30 min : les flottes qui partent de la planète balayée ou s'y dirigent s'y ajoutent | 30 min |
| +9 % de vitesse pour une attaque lancée peu après votre rapport sur la cible | 9 % |
| +300 s de préavis avant l'impact d'une attaque | 300 s |
| +20 % de vitesse pour une flotte qui quitte un monde visé par une attaque annoncée encore en vol, quelle que soit sa mission | 20 % |
| −50 % de consommation d'hydrogène pour cette flotte, sur tout le trajet | 50 % |
| −10 pts sur le taux de pillage que vous subissez | 5 pts |

La ligne du pillage se complète avec Coffres enterrés de l'arbre commun (5 points) : 10 points en tout, le taux subi passe de 50 à 40 %. Le délai d'alerte s'ajoute aux 60 s que le jeu donne à tous : 360 s, soit 6 min, au plus.

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Sentinelle | Préavis 15 · Veille 10 | alerte 6 min avant l'impact, La cache, garde +6 % de bouclier et de dégâts, Gabarit ennemi ou Heure juste, Le colosse annoncé, Dénombrement ou Repli éclair ; Phalange +1 niveau à 3 800 hydrogène, Veille partagée ou Lune et planète, mémoire de 3 h, Le retour annoncé, Balayage silencieux ou Relais de lunes |
| Augure | Présage 15 · Préavis 10 | Le plan de raid, Le choc annoncé, Frappe préparée, Butin prévu, carnet de 15 cibles, Œil du raid ; alerte 3 min 30 avant l'impact, garde +6 %, Le colosse annoncé, Dénombrement (qui fait simuler Le choc annoncé) ou Repli éclair |
| Guetteur | Veille 15 · Présage 10 | Balayage réflexe, Vue d'empire, balayages ouverts 30 min, mémoire de 3 h ; Pesée, carnet de 15 cibles, Œil du raid, Butin prévu, Tournée de fermes ou Bilan de chasse |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **Garde prévenue demande 90 secondes d'alerte** : la minute que le jeu donne à tous ne suffit pas, il faut au moins Oreille tendue. Une attaque au vol plus court que 90 s ne la déclenche jamais.
- **Les talents d'alerte comptent au départ de la flotte ennemie** : prendre Oreille tendue pendant qu'une attaque vole déjà ne l'annonce pas plus tôt.
- **L'alerte avancée est floue** : base visée et heure à la minute près, sans origine, jusqu'aux 60 dernières secondes. Pour partir à la dernière seconde, Heure juste compte plus que le délai.
- **Pas de lune, pas de Phalange** : la Phalange se construit sur une lune et ne vise jamais une lune ; Lune et planète montre seulement les flottes qui partent de la lune ou y arrivent. Le retour annoncé, lui, n'a pas besoin de lune.
- **Balayage silencieux ne sert que contre l'Ombre** : par défaut, personne n'est prévenu d'un balayage.
- **Pesée, Butin prévu, Carnet de fermes et Le plan de raid sont des maximums** : ils ignorent la protection du défenseur contre le pillage et la taille de ses hangars.
- **Frappe préparée** ne vaut que pour une attaque lancée au plus 30 minutes après votre rapport d'espionnage sur le même corps. Elle compte dans l'accent de vitesse de la classe (10 % au plus).
- **Gabarit ennemi et Dénombrement mesurent un coût, pas une force** : 1 000 Navettes de fret (4 000 000) sortent « grande » comme une flotte de combat du même prix.
- **La cache et Coffres enterrés se cumulent** : 10 points de protection au total, le pillage subi passe de 50 à 40 %. C'est le plafond de l'Oracle.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Classes](/fr/dynasty/classes)
- [Arbre commun](/fr/dynasty/common-tree)
- [Dynasties](/fr/dynasty/dynasties)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Pillage](/fr/combat/plunder)
- [Simulateur](/fr/combat/simulator)
- [L'Ombre](/fr/dynasty/classes/shadow)
