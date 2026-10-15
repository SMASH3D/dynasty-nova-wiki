---
wiki_id: 160
locale: "fr"
path: "dynasty/classes/veteran"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/veteran"
title: "Le Vétéran"
description: "La classe défensive de L'Héritage : Muraille, Relève et Silo."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:55.451Z"
updated: "2026-10-07T22:08:32.225Z"
---

# Le Vétéran

> **En bref** : le Vétéran ne gagne pas les batailles, il fait que chaque attaque contre lui coûte cher à l'attaquant et presque rien à lui-même. Tout le combat tient dans Muraille ; Relève fait revenir les défenses tombées et rembourse les autres ; Silo répond par les missiles. Classe exclusive à L'Héritage.
{.is-info}

## Règles

1. Le Vétéran est une classe **exclusive à [L'Héritage](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Muraille, Relève et Silo.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 (10 points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents).
4. Un Vétéran part de **75 %** de chances de réparation gratuite de chaque défense détruite au lieu de 70 %, grâce au trait Rien ne se perd de L'Héritage. Brancardiers et Ateliers de campagne montent ce taux jusqu'à son plafond de **85 %**. La réparation reste un tirage par défense.
5. La vitesse de construction des défenses générique vient de l'[arbre commun](/fr/dynasty/common-tree). Le Vétéran n'y ajoute que des **accents** étroits : la construction des défenses et des missiles (Brancards rapides, Production en série), **15 % au plus pour les deux ensemble**, et la protection contre le pillage (Abri souterrain), **15 points au plus**, Coffres enterrés de l'arbre commun compris.
6. Les bonus de statistiques de Muraille s'appliquent **après** la recherche et se multiplient avec elle. Le bouclier et la coque de vos défenses comptent aussi contre les frappes de missiles : Béton armé et Pièces lourdes les rendent plus dures à détruire. Les bonus de dégâts (Contre-batterie, Premier rang) ne jouent que pour vos défenses, quand on vous attaque, et se multiplient entre eux.

## Exemple chiffré

**Une attaque détruit 100 Projecteurs balistiques** (2 000 métal pièce)
- Sans talent, chacun a 75 % de chances de revenir : **75** reviennent en moyenne, 25 sont perdus, soit 50 000 métal.
- Avec Brancardiers et Ateliers de campagne au rang 3 (85 %) : **85** reviennent en moyenne, 15 sont perdus, soit 30 000 métal.
- Avec Fonds de reconstruction, Récupération du matériel et Caisse de guerre (50 %) : **15 000 métal** vous sont rendus. La perte réelle tombe à 15 000 métal.
- Avec Rideau léger, les 100 reviennent.

**Pointeurs au rang 3**
- Un Projecteur balistique a 80 d'armement. Systèmes Offensifs niveau 10 : 80 × 2 = 160. Avec +9 % : 160 × 1,09 = 174,4, arrondi à **174**.

**Fosses profondes et Casemates, Arsenal balistique niveau 10**
- 10 emplacements par niveau : 100 emplacements, soit 50 Ogives longue portée (2 emplacements chacune).
- Avec +35 % : 100 × 1,35 = 135 emplacements, soit **67 ogives**.
- Avec Charge creuse au rang 3 et Systèmes Offensifs niveau 10, une ogive inflige 12 000 × 2 × 1,09 = **26 160** dégâts.

**Abri souterrain**
- Le pillage subi passe de 50 % à **40 %**. Avec Coffres enterrés de l'arbre commun : **35 %**, le minimum pour un Vétéran. Sur 2 000 000 de métal en stock, l'attaquant emporte 700 000 au lieu de 1 000 000.

**Prise de guerre** (univers à 30 % de débris des vaisseaux, comme Redline)
- L'attaquant perd 100 Corvettes (20 000 métal et 7 000 cristal pièce) et vous gagnez. Débris : 600 000 métal et 210 000 cristal. **120 000 métal et 42 000 cristal** tombent dans vos stocks ; le reste reste dans le champ.

## Données détaillées

### Vue d'ensemble de l'arbre

Les trois branches de l'arbre de classe, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux ci-dessous.

```mermaid
graph TB
    subgraph B3[" "]
        B3H["SILO<br/>Ce qui répond."]:::head
        B3R1{{"Fosses profondes<br/>1 pt"}}:::key
        B3H --- B3R1
        B3R2("Charge creuse<br/>3 pts"):::rank
        B3R1 --- B3R2
        B3R3A["① Casemates<br/>1 pt"]:::option
        B3R3B["② Allonge<br/>1 pt"]:::option
        B3R2 --- B3R3A
        B3R2 --- B3R3B
        B3G3(["🔒 5 points dans l'arbre"]):::gate
        B3R3A --- B3G3
        B3R3B --- B3G3
        B3R4("Intercepteurs récupérés<br/>3 pts"):::rank
        B3G3 --- B3R4
        B3R5{{"Contre-salve<br/>1 pt"}}:::key
        B3R4 --- B3R5
        B3R6A["① Riposte automatique<br/>1 pt"]:::option
        B3R6B["② Production en série<br/>1 pt"]:::option
        B3R5 --- B3R6A
        B3R5 --- B3R6B
        B3G6(["🔒 12 points dans l'arbre"]):::gate
        B3R6A --- B3G6
        B3R6B --- B3G6
        B3R7("Portée d'impulsion<br/>3 pts"):::rank
        B3G6 --- B3R7
        B3R8{{"Silo lunaire<br/>1 pt"}}:::key
        B3R7 --- B3R8
        B3R9[["✦ Pluie d'acier<br/>ultime"]]:::ultimate
        B3R8 --- B3R9
    end
    subgraph B2[" "]
        B2H["RELÈVE<br/>Ce qui revient."]:::head
        B2R1{{"Brancardiers<br/>1 pt"}}:::key
        B2H --- B2R1
        B2R2("Fonds de reconstruction<br/>3 pts"):::rank
        B2R1 --- B2R2
        B2R3A["① Sous le feu<br/>1 pt"]:::option
        B2R3B["② Brancards rapides<br/>1 pt"]:::option
        B2R2 --- B2R3A
        B2R2 --- B2R3B
        B2G3(["🔒 5 points dans l'arbre"]):::gate
        B2R3A --- B2G3
        B2R3B --- B2G3
        B2R4("Ateliers de campagne<br/>3 pts"):::rank
        B2G3 --- B2R4
        B2R5{{"Récupération du matériel<br/>1 pt"}}:::key
        B2R4 --- B2R5
        B2R6A["① Reconstruction express<br/>1 pt"]:::option
        B2R6B["② Rappel des réservistes<br/>1 pt"]:::option
        B2R5 --- B2R6A
        B2R5 --- B2R6B
        B2G6(["🔒 12 points dans l'arbre"]):::gate
        B2R6A --- B2G6
        B2R6B --- B2G6
        B2R7("Caisse de guerre<br/>3 pts"):::rank
        B2G6 --- B2R7
        B2R8{{"Les dômes d'abord<br/>1 pt"}}:::key
        B2R7 --- B2R8
        B2R9[["✦ Ligne reformée<br/>ultime"]]:::ultimate
        B2R8 --- B2R9
    end
    subgraph B1[" "]
        B1H["MURAILLE<br/>Ce qui tient debout."]:::head
        B1R1{{"Béton armé<br/>1 pt"}}:::key
        B1H --- B1R1
        B1R2("Pointeurs<br/>3 pts"):::rank
        B1R1 --- B1R2
        B1R3A["① Pièces lourdes<br/>1 pt"]:::option
        B1R3B["② Rideau léger<br/>1 pt"]:::option
        B1R2 --- B1R3A
        B1R2 --- B1R3B
        B1G3(["🔒 5 points dans l'arbre"]):::gate
        B1R3A --- B1G3
        B1R3B --- B1G3
        B1R4("Contre-batterie<br/>3 pts"):::rank
        B1G3 --- B1R4
        B1R5{{"Branle-bas de combat<br/>1 pt"}}:::key
        B1R4 --- B1R5
        B1R6A["① Abri souterrain<br/>1 pt"]:::option
        B1R6B["② Prise de guerre<br/>1 pt"]:::option
        B1R5 --- B1R6A
        B1R5 --- B1R6B
        B1G6(["🔒 12 points dans l'arbre"]):::gate
        B1R6A --- B1G6
        B1R6B --- B1G6
        B1R7("Premier rang<br/>3 pts"):::rank
        B1G6 --- B1R7
        B1R8{{"La lune tient<br/>1 pt"}}:::key
        B1R7 --- B1R8
        B1R9[["✦ Dernière salve<br/>ultime"]]:::ultimate
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

### Muraille

*Ce qui tient debout.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Béton armé** | clé | Le bouclier de vos défenses est 5 % plus solide. |  |
| 2 | **Pointeurs** | 3 rangs | Vos défenses font 9 % de dégâts en plus. | 3 × 3 % |
| 3 | **A · Pièces lourdes** | choix | Vos accélérateurs magnétiques, batteries ioniques et éjecteurs à plasma gagnent 10 % de coque. | |
|  | **B · Rideau léger** |  | Vos projecteurs balistiques et canons photoniques détruits en bataille sont toujours réparés. | |
| 4 | **Contre-batterie** | 3 rangs | Vos défenses font 6 % de dégâts en plus contre les vaisseaux qui ont un tir rapide contre elles. | 3 × 2 % |
| 5 | **Branle-bas de combat** | clé | Tant qu'une attaque est en route vers une de vos planètes, ses défenses se construisent deux fois plus vite : le rapport d'espionnage de l'attaquant vieillit pendant son vol. |  |
| 6 | **A · Abri souterrain** | choix | Le taux de pillage que vous subissez baisse de 10 points. | |
|  | **B · Prise de guerre** |  | Après une défense gagnée, 20 % des débris de la flotte ennemie tombent directement dans vos hangars. | |
| 7 | **Premier rang** | 3 rangs | Au premier round, quand la flotte ennemie est encore entière, vos défenses font 9 % de dégâts en plus. | 3 × 3 % |
| 8 | **La lune tient** | clé | La chance de détruire vos lunes baisse de 25 %. |  |
| 9 | **Dernière salve** | ultime | Si une bataille finit en match nul, vos défenses tirent seules 1 salve de plus avant que l'attaquant ne reparte : le raid indécis devient coûteux. |  |

- **Pièces lourdes** ne touche que l'Accélérateur magnétique, la Batterie ionique et l'Éjecteur à plasma.
- **Rideau léger** et **Les dômes d'abord** réparent toujours, même contre Terre brûlée, mais seulement après une bataille : rien contre les missiles.
- **Contre-batterie** joue contre chaque vaisseau qui a un tir rapide contre la défense qui tire.
- **Branle-bas de combat** vaut pour les attaques et les destructions de lune visant cette base. La commande de défenses ne gagne jamais plus de la moitié de son temps restant.
- **Prise de guerre** : seulement sur une défense gagnée ; les ressources dépassent la capacité de vos entrepôts et sont retirées du champ de débris.
- **Premier rang** joue au premier round de chaque bataille, contre toutes les cibles.
- **La lune tient** multiplie la chance de détruire la lune par 0,75 : une chance de 100 % tombe à 75 %.
- **Dernière salve** : seules vos défenses tirent cette salve, pas vos vaisseaux. Si elle achève la flotte ennemie, la bataille devient une victoire de la défense.

### Relève

*Ce qui revient.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Brancardiers** | clé | La réparation gratuite de vos défenses après une bataille gagne 4 points. |  |
| 2 | **Fonds de reconstruction** | 3 rangs | Une défense perdue pour de bon rend 15 % de ce qu'elle a coûté, sur sa planète. | 3 × 5 % |
| 3 | **A · Sous le feu** | choix | 20 % des défenses détruites par une frappe de missiles sont reconstruites gratuitement. | |
|  | **B · Brancards rapides** |  | Vos défenses se construisent 15 % plus vite. | |
| 4 | **Ateliers de campagne** | 3 rangs | La réparation gratuite de vos défenses gagne encore 6 points, jusqu'à son plafond de 85 %. | 3 × 2 pts |
| 5 | **Récupération du matériel** | clé | Une défense perdue pour de bon rend encore 20 % de ce qu'elle a coûté. |  |
| 6 | **A · Reconstruction express** | choix | Pendant 24 h après une bataille, les défenses perdues pour de bon se reconstruisent 50 % plus vite. | |
|  | **B · Rappel des réservistes** |  | Chaque attaque subie avance d'un coup de 1 h la file de défenses de la planète. | |
| 7 | **Caisse de guerre** | 3 rangs | Vos défenses perdues pour de bon rendent encore 15 % de ce qu'elles ont coûté. | 3 × 5 % |
| 8 | **Les dômes d'abord** | clé | Votre barrière défensive et votre dôme protecteur détruits en bataille sont toujours réparés. |  |
| 9 | **Ligne reformée** | ultime | Pendant 6 h après une attaque subie sur une planète, toute défense qu'une nouvelle attaque y détruit est réparée : la deuxième vague tombe sur une ligne intacte. |  |

- **Fonds de reconstruction**, **Récupération du matériel** et **Caisse de guerre** s'additionnent (50 % au plus). Ils rendent le prix payé (métal, cristal et hydrogène), sur la planète, même au-delà de ses entrepôts. Seulement pour les défenses perdues en bataille : une défense détruite par un missile n'est pas remboursée.
- **Sous le feu** est une chance par défense détruite, pas une part garantie.
- **Reconstruction express** : les commandes de défenses lancées dans les 24 h construisent plus vite, pour autant d'unités de chaque type que vous en avez perdu. Une nouvelle perte ajoute ses unités et relance les 24 h.
- **Rappel des réservistes** avance seulement la commande de défenses en cours, sans dépasser sa fin.
- **Ligne reformée** : la fenêtre s'ouvre à chaque attaque subie hors fenêtre. Une attaque qui tombe dedans ne la prolonge pas. Terre brûlée d'un Amiral retire encore ses 15 points : 85 % de réparation au lieu de 100 %.

### Silo

*Ce qui répond.*

| Rangée | Nœud | Type | Effet (nœud plein) | Par rang |
|---|---|---|---|---|
| 1 | **Fosses profondes** | clé | Votre silo à missiles stocke 5 % de missiles en plus. |  |
| 2 | **Charge creuse** | 3 rangs | Vos ogives font 9 % de dégâts en plus. | 3 × 3 % |
| 3 | **A · Casemates** | choix | Votre silo à missiles stocke encore 30 % de missiles en plus. | |
|  | **B · Allonge** |  | Vos missiles portent 2 systèmes plus loin. | |
| 4 | **Intercepteurs récupérés** | 3 rangs | Un intercepteur qui abat une ogive a 15 % de chances de rester au silo. | 3 × 5 % |
| 5 | **Contre-salve** | clé | Pendant 24 h, la base qui a frappé une de vos planètes est à portée de vos missiles, même dans une autre galaxie. |  |
| 6 | **A · Riposte automatique** | choix | Quand une frappe touche une de vos planètes, elle renvoie aussitôt sur la base d'origine autant d'ogives qu'elle en a reçu, jusqu'à 10, prises seulement parmi celles que vous marquez « réserve de riposte » : le reste du silo n'est jamais vidé. | |
|  | **B · Production en série** |  | Vos missiles se construisent 15 % plus vite. | |
| 7 | **Portée d'impulsion** | 3 rangs | Vos missiles portent encore 3 systèmes plus loin. | 3 × 1 |
| 8 | **Silo lunaire** | clé | Vous pouvez construire un arsenal balistique sur vos lunes et lancer vos missiles depuis elles. |  |
| 9 | **Pluie d'acier** | ultime | Une fois par jour, une salve d'au moins 20 ogives ne peut pas être interceptée. |  |

- **Fosses profondes** et **Casemates** s'additionnent : +35 % d'emplacements, arrondi à l'unité inférieure. Un Intercepteur prend 1 emplacement, une Ogive longue portée 2.
- **Allonge** et **Portée d'impulsion** s'additionnent (5 systèmes au plus) sur la portée de base, niveau de Moteur Magnétique × 5 − 1. Jamais hors de la galaxie, sauf contre une base visée par Contre-salve.
- **Intercepteurs récupérés** est une chance par Intercepteur qui abat une ogive.
- **Contre-salve** : la base d'où est partie la salve est à portée de toutes vos bases pendant 24 h.
- **Riposte automatique** : la réserve de riposte se marque base par base. Une base frappée sans ogives marquées ne riposte pas. Une riposte ne déclenche jamais de riposte en retour.
- **Production en série** partage le plafond de 15 % de Brancards rapides : avec les deux, vos missiles ne vont pas plus vite.
- **Pluie d'acier** se déclare au lancement, pour une salve d'au moins 20 ogives, une fois par 24 h glissantes pour tout votre empire. Aucun niveau n'est demandé.

### Plafonds de la classe

Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite.

| Plafond de la classe (talents des deux arbres) | Ce que l'arbre de classe atteint |
|---|---|
| +5 % de bouclier des défenses | 5 % |
| +9 % d'armement des défenses | 9 % |
| +10 % de coque des accélérateurs magnétiques, batteries ioniques et éjecteurs à plasma | 10 % |
| +6 % de dégâts des défenses contre les vaisseaux qui ont un tir rapide contre elles | 6 % |
| −15 pts sur le taux de pillage que vous subissez | 10 pts |
| +9 % de dégâts des défenses au premier round | 9 % |
| −25 % de chance de destruction de vos lunes | 25 % |
| +15 pts de réparation gratuite des défenses après une bataille | 10 pts |
| Une défense perdue pour de bon en bataille rend 50 % de ce qu'elle a coûté | 50 % |
| +15 % de vitesse de construction des défenses | 15 % |
| +35 % de capacité du silo | 35 % |
| +9 % de rendement des ogives | 9 % |
| +5 systèmes de portée des missiles | 5 |

Deux plafonds se partagent : la vitesse de construction de Brancards rapides et de Production en série tient dans un seul accent de 15 %, et la protection de Abri souterrain dans 15 points avec Coffres enterrés. La réparation gratuite bute sur 85 % : 75 % de départ et 10 points de talents l'atteignent tout juste.

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Forteresse | Muraille 15 · Relève 10 | Dernière salve, Branle-bas de combat, défenses +9 % de dégâts et +5 % de bouclier, Contre-batterie, Premier rang, La lune tient ; réparation à 85 %, 35 % rendus sur les pertes |
| Increvable | Relève 15 · Silo 10 | Ligne reformée, Les dômes d'abord, réparation à 85 %, 50 % rendus sur les pertes ; Arsenal +35 % avec Casemates (ou portée +2 avec Allonge), ogives +9 %, Intercepteurs récupérés, Contre-salve |
| Artilleur | Silo 15 · Muraille 10 | Pluie d'acier, Silo lunaire, Riposte automatique ou Production en série, portée +3 à +5 systèmes ; Béton armé, Pointeurs, Contre-batterie, Branle-bas de combat |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.

## Pièges fréquents

- **La réparation reste un tirage** : 85 % est une chance par défense, pas une part garantie du lot (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)).
- **Les frappes de missiles ne sont ni réparées ni remboursées** : seul Sous le feu donne à chaque défense détruite une chance de revenir. Rideau léger, Les dômes d'abord, Ligne reformée et le remboursement de Relève ne jouent qu'après une bataille.
- **Brancards rapides et Production en série ne se cumulent pas** sur les missiles : un seul accent de 15 %.
- **Terre brûlée** d'un Amiral retire 15 points à votre réparation contre lui : à 85 %, il vous reste 70 %.
- **Riposte automatique ne vide jamais votre Arsenal balistique** : seules les ogives marquées « réserve de riposte » sur la base frappée partent. Sans réserve, rien ne part.
- **Rappel des réservistes n'avance que la commande en cours** : sans défense en production, il ne fait rien.
- **Le pillage ne descend jamais sous 30 %**, mais un Vétéran ne va pas sous 35 % : sa protection est plafonnée à 15 points.

## Pages liées

- [Talents](/fr/dynasty/talents)
- [Classes](/fr/dynasty/classes)
- [Arbre commun](/fr/dynasty/common-tree)
- [Dynasties](/fr/dynasty/dynasties)
- [Liste des défenses](/fr/defense/defenses)
- [Missiles](/fr/defense/missiles)
- [Barrière et Dôme](/fr/defense/shield-domes)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Pillage](/fr/combat/plunder)
- [Destruction de lune](/fr/combat/moon-destruction)
