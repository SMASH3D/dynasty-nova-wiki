---
locale: "fr"
path: "dynasty/classes/oracle"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/oracle"
title: "L'Oracle"
description: "La classe de l'information anticipée, exclusive à L'Accord : Veille, Présage et Préavis."
tags: ["dynasty"]
published: false
---

# L'Oracle

> **En bref** : l'Oracle ne frappe pas plus fort, il sait avant. Chacune de ses branches vend une information, jamais une statistique : Veille regarde bouger les flottes depuis une lune, Présage prépare les raids, Préavis évite d'être là quand le coup tombe.
{.is-info}

## Règles

1. L'Oracle est une classe **exclusive à [L'Accord](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.
2. Son arbre compte **trois branches** : Veille, Présage et Préavis.
3. Chaque branche a 9 rangées et coûte 15 points. Avec 25 points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6. Le fonctionnement des points, des portes et des choix est décrit sur [Talents](/fr/dynasty/talents).
4. La protection générique contre le pillage et la vitesse de retour des flottes viennent de l'[arbre commun](/fr/dynasty/common-tree). L'Oracle n'y ajoute que deux accents étroits : *Frappe préparée* (vitesse des attaques) et *La cache* (protection contre le pillage). Le pistage des espions appartient à l'[Ombre](/fr/dynasty/classes/shadow).
5. Sans talent, une attaque contre vous est annoncée **1 minute** avant l'impact. Les talents de Préavis s'ajoutent à ce délai.
6. Veille demande une lune : la [Phalange de capteur](/fr/espionage/sensor-phalanx) s'y construit, et chaque balayage se paie, sauf celui de l'ultime.

## Exemple chiffré

**Délai d'alerte selon les talents de Préavis**

| Talents pris | Délai avant l'impact |
|---|---|
| aucun | 1 min |
| Oreille tendue | 2 min 30 |
| + Tour de garde au rang 3 | 3 min 30 |
| + Veilleurs de quart au rang 3 | 4 min 30 |
| + Le grand préavis (niveau 40, branche pleine) | 6 min |

**Phalange de niveau 3 avec Longue-vue et Lentilles au rang 3**
- Portée : la Phalange porte comme un niveau 4, soit 4² − 1 = **15 systèmes** de part et d'autre, au lieu de 8.
- Coût d'un balayage : 5 000 × (1 − 0,24) = **3 800 hydrogène**.
- Avec *Vue d'empire*, un joueur qui a 3 planètes à portée se balaie en entier pour 3 800 hydrogène au lieu de 11 400.

**Pesée** : le rapport lit 1 200 000 métal, 800 000 cristal et 300 000 hydrogène, soit 2 300 000 ressources. Avec un pillage de 50 %, la part pillable est de **1 150 000**. Il faut 1 150 000 / 25 000 = **46 Cargos stellaires**, ou 1 150 000 / 5 000 = **230 Navettes de fret**.

**La cache** : 2 000 000 de ressources en stock. Un raid gagnant emporte 50 % sans talent, soit 1 000 000 ; avec *La cache*, 45 %, soit **900 000**.

## Données détaillées

### Veille

*Voir bouger les flottes.*

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Longue-vue** | Votre Phalange porte comme si elle avait un niveau de plus. | 1 rang | +1 niveau |
| 2 | **Lentilles** | Vos balayages coûtent moins d'hydrogène. | 3 × 8 % | −24 % |
| 3 | **A · Veille partagée** ou **B · Lune et planète** | A : chacun de vos balayages est remis à toute votre alliance. <br> B : un balayage montre aussi les flottes qui partent de la lune de la planète ou y arrivent. | 1 rang | déblocage |
| 4 | **Mémoire de phalange** | Les flottes vues par un balayage restent suivies, avec leur heure d'arrivée, après la fin du balayage. | 3 × 1 h | 3 h |
| 5 | **Le retour annoncé** | Une attaque annoncée vous dit aussi à quelle heure la flotte ennemie sera rentrée chez elle. | 1 rang | déblocage |
| 6 | **A · Balayage silencieux** ou **B · Relais de lunes** | A : vos balayages ne sont jamais signalés à la planète balayée, quels que soient les talents de son propriétaire. <br> B : une planète à portée de n'importe laquelle de vos lunes peut être balayée depuis votre lune à Phalange. | 1 rang | déblocage |
| 7 | **Regard prolongé** | Un balayage reste ouvert : les flottes qui partent de la planète ou y arrivent pendant ce temps s'ajoutent à son relevé. | 3 × 10 min | 30 min |
| 8 | **Vue d'empire** | Un balayage montre aussi les flottes de toutes les autres planètes du même joueur à portée, pour le prix d'un seul. | 1 rang | déblocage |
| 9 | **Balayage réflexe** *(ultime)* | Quand une attaque contre vous est annoncée, une de vos lunes à portée balaie gratuitement la planète d'où elle est partie. | 1 rang | gratuit |

### Présage

*Savoir avant de frapper.*

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Pesée** | Chaque rapport d'espionnage indique combien de transporteurs il faut pour emporter la part pillable. | 1 rang | déblocage |
| 2 | **Carnet de fermes** | Vous suivez des cibles : le jeu projette leur stock d'après vos deux derniers rapports et vous prévient quand la part pillable atteint le seuil choisi. | 3 × 5 cibles | 15 cibles |
| 3 | **A · Mesure de l'écart** ou **B · Lecture des classements** | A : le rapport dit combien d'Éclaireurs il faut pour lire le palier suivant. <br> B : un rapport trop court pour le simulateur reçoit une tendance de défense (probablement vide, inconnue, dangereuse) au lieu d'un refus. | 1 rang | déblocage |
| 4 | **Œil du raid** | Vos rapports de combat en attaque lisent la cible comme un rapport d'espionnage : d'abord le stock restant après pillage, puis les bâtiments, puis les recherches. | 3 × 1 palier | 3 paliers |
| 5 | **Butin prévu** | Le simulateur donne aussi le butin attendu : la part pillable, bornée par les soutes de vos vaisseaux survivants. | 1 rang | déblocage |
| 6 | **A · Tournée de fermes** ou **B · Bilan de chasse** | A : choisissez jusqu'à 5 fermes ; le jeu répartit vos transporteurs entre elles selon leur part pillable et prépare les envois. <br> B : le simulateur donne le champ de ruines attendu et le gain net de vos pertes. | 1 rang | A : 5 fermes <br> B : déblocage |
| 7 | **Frappe préparée** | Une attaque lancée moins de 30 minutes après votre rapport sur la cible va plus vite (accent de vitesse). | 3 × 3 % | +9 % |
| 8 | **Le choc annoncé** | Une attaque contre vous reçoit un verdict, tenir ou tomber, tiré des classements militaires publics ; simulé contre la vraie flotte quand votre préavis en mesure la puissance (*Dénombrement*). | 1 rang | déblocage |
| 9 | **Le plan de raid** *(ultime)* | Depuis un rapport qui a lu la flotte, le jeu propose la plus petite flotte, prise sur la planète de votre choix, qui gagne au moins 9 combats simulés sur 10 et emporte toute la part pillable. | 1 rang | 9 sur 10 |

Présage ne révèle rien que vous n'ayez déjà payé : vos rapports, vos combats et les classements publics.

### Préavis

*Ne pas être là quand le coup tombe.*

| Rangée | Nœud | Effet | Par rang | Total |
|---|---|---|---|---|
| 1 | **Oreille tendue** | Les attaques contre vous sont annoncées plus tôt. | 1 rang | +90 s |
| 2 | **Garde prévenue** | Si l'alerte est tombée au moins 90 secondes avant l'impact, les défenses et les vaisseaux de la planète gagnent du bouclier et des dégâts, contre les attaques seulement. | 3 × 2 % | +6 % |
| 3 | **A · Gabarit ennemi** ou **B · Heure juste** | A : l'alerte donne la taille de la flotte ennemie (petite, moyenne, grande, écrasante). <br> B : l'alerte donne dès sa première seconde l'heure d'arrivée exacte et l'origine. | 1 rang | déblocage |
| 4 | **Tour de garde** | L'alerte tombe encore plus tôt. | 3 × 20 s | +60 s |
| 5 | **Le colosse annoncé** | Les destructions de lune visant vos lunes sont annoncées comme les attaques, avec le même délai. | 1 rang | déblocage |
| 6 | **A · Dénombrement** ou **B · Repli éclair** | A : l'alerte donne la puissance de la flotte ennemie à 25 % près, jamais ses vaisseaux. <br> B : une flotte qui quitte une planète visée par une attaque annoncée va 20 % plus vite et brûle 50 % d'hydrogène en moins. | 1 rang | A : ±25 % <br> B : +20 %, −50 % |
| 7 | **Veilleurs de quart** | L'alerte tombe encore plus tôt. | 3 × 20 s | +60 s |
| 8 | **La cache** | Le pillage que vous subissez baisse de 5 points (accent). | 1 rang | −5 pts |
| 9 | **Le grand préavis** *(ultime)* | L'alerte tombe encore plus tôt. | 1 rang | +90 s |

L'alerte ne donne jamais la composition de la flotte ennemie : au plus sa taille ou sa puissance.

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Sentinelle | Préavis 15 · Veille 10 | alerte 6 min avant l'impact, La cache, garde +6 %, destructions de lune annoncées ; Phalange +1 niveau à 3 800 hydrogène, mémoire de 3 h, Le retour annoncé, balayage silencieux ou relais de lunes |
| Augure | Présage 15 · Préavis 10 | Le plan de raid, Butin prévu, carnet de 15 fermes, Œil du raid ; alerte 3 min 30 avant l'impact, Dénombrement ou Repli éclair |
| Guetteur | Veille 15 · Présage 10 | Balayage réflexe, Vue d'empire, balayages ouverts 30 min ; Pesée, carnet de fermes, Œil du raid, Butin prévu, tournée ou bilan |

## Pièges fréquents

- **Garde prévenue demande 90 secondes d'alerte** : la minute que le jeu donne à tous ne suffit pas. Il faut au moins *Oreille tendue*.
- **Pas de lune, pas de Veille** : la Phalange se construit sur une lune et ne cible jamais une lune ; *Lune et planète* montre seulement les flottes qui partent de la lune ou y arrivent.
- **Frappe préparée** ne vaut que pour une attaque lancée moins de 30 minutes après votre rapport d'espionnage sur la même cible. Elle compte dans l'accent de vitesse de la classe (10 % au plus).
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
