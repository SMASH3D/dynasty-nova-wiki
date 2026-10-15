---
wiki_id: 37
locale: "fr"
path: "fleet/expeditions"
url: "https://wiki.dynastynova.com/fr/fleet/expeditions"
title: "Expéditions"
description: "Explorer l'espace lointain : conditions, résultats et taille des trouvailles."
tags: ["fleet"]
published: true
created: "2026-10-02T13:08:56.440Z"
updated: "2026-10-15T18:54:28.222Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Expéditions

> **En bref** : au-delà de la dernière position de chaque système s'étend l'espace lointain. Une flotte qui y tient sa position revient parfois chargée de ressources ou de vaisseaux abandonnés, parfois retardée, ou tombe sur des pirates, des aliens, voire un trou noir. Il faut la Cosmologie Appliquée pour partir.
{.is-info}

> **Paramètre d'univers** : les expéditions peuvent être ouvertes ou fermées selon l'univers.
> Par défaut : **ouvertes** · Redline : **ouvertes**
{.is-info}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Cosmologie Appliquée">

## Règles

### Partir
1. Il faut **Cosmologie Appliquée niveau 1** au minimum.
2. La cible est l'**espace lointain** du système : la position qui suit la dernière (16 sur Redline). Seuls l'Expédition et le Recyclage peuvent y aller.
3. La flotte ne peut pas être composée **uniquement d'Éclaireurs** ; un Éclaireur peut accompagner n'importe quelle autre coque. Le Collecteur solaire ne vole jamais.
4. Vous choisissez la **durée de maintien**, par heure entière : de 1 h jusqu'à autant d'heures que votre niveau de Cosmologie Appliquée.
5. **Expéditions simultanées** = partie entière de la racine carrée du niveau de Cosmologie Appliquée. Elles comptent toutes vos expéditions de l'univers, à l'aller, sur place ou au retour. Chacune occupe **aussi** un emplacement de flotte.
6. **Hydrogène** : l'aller, le retour et le maintien sont payés au départ. Le maintien coûte $\lceil h \times C / 10 \rceil$, où $h$ est le nombre d'heures et $C$ la somme des consommations de base des vaisseaux envoyés (consommation × nombre). Aucun talent d'économie de carburant ne s'applique au maintien. Tout l'hydrogène du voyage doit tenir dans les soutes avec la cargaison.

### Sur place
7. La **durée de maintien ne change pas les chances** de trouver quelque chose. Elle allonge seulement le voyage et la consommation, et un éventuel retard (règle 12).
8. **Rappel** : une flotte rappelée pendant son maintien refait tout le trajet de l'aller pour rentrer et ne rapporte **rien**, ni résultat ni rapport.
9. Une zone trop visitée **s'épuise** : à partir de **10 expéditions** résolues sur l'espace lointain d'un même système en 24 heures, tous joueurs confondus, la zone est « exploitée » et les chances de trouvaille baissent ; à partir de **25**, elle est « épuisée » et elles baissent davantage. La part perdue va au résultat « rien ». Si la flotte emporte au moins un **Éclaireur**, le rapport indique l'état de la zone.

### Résultats
10. **Ressources** : un seul type de ressource par trouvaille, métal, cristal ou hydrogène. Le montant est proportionnel aux points d'expédition de la flotte (règle 15), en équivalent métal : il est divisé par 2 pour le cristal et par 3 pour l'hydrogène. La trouvaille est limitée par la **soute libre** : le surplus est perdu, et le rapport le signale.
11. **Vaisseaux** : des vaisseaux abandonnés rejoignent votre flotte, pour une valeur égale à la moitié d'une trouvaille de ressources. Ils ne prennent pas de place dans la soute. Vous pouvez trouver jusqu'au rang qui suit celui de votre meilleur vaisseau à bord (table plus bas). Jamais de Colossus stellaire, de Pionnier spatial, de Récupérateur ni de Collecteur solaire, qui ne comptent pas non plus pour le rang. Les vaisseaux trouvés rapportent leurs points militaires.
12. **Retard** : le retour est allongé de 2, 3 ou 5 fois la durée de maintien choisie, selon l'ampleur de l'événement. **Retour anticipé** : la durée du retour est divisée par 2, 3 ou 5.
13. **Pirates** et **aliens** : un vrai combat contre une flotte calquée sur la vôtre, plus forte quand l'événement est plus grand, renforcée d'une escorte. Les aliens sont plus forts que les pirates. Les pirates combattent avec vos recherches de combat moins 3 niveaux, les aliens avec 3 niveaux de plus. Vous recevez un rapport de combat ; les survivants gardent leur cargaison, sans pillage. Les débris (10 % des vaisseaux détruits, des deux camps) restent sur l'espace lointain.
14. **Trou noir** : la flotte entière et sa cargaison sont perdues. **Rien** : la flotte rentre comme elle est partie.

### Taille des trouvailles
15. **Points d'expédition** = max(200, structure totale de la flotte / 200, arrondi à l'inférieur), plafonnés selon les points du **meilleur joueur humain** de l'univers (table plus bas). Plus la flotte est grande, plus elle rapporte, jusqu'au plafond.

## Exemple chiffré

50 Cargos stellaires et 1 Éclaireur partent de [2:40:8] vers l'espace lointain [2:40:16], avec Propulseur Chimique 6, à 100 %, pour 3 heures de maintien. Le meilleur joueur de l'univers a 500 000 points.
- Distance : 1 000 + 5 × 8 = **1 040**. Vitesse de la flotte : celle du Cargo, 7 500 × 1,6 = 12 000. Trajet : **3 268 s** (54 min 28 s) à l'aller comme au retour.
- Hydrogène : 297 par trajet, soit 594 pour l'aller-retour, plus le maintien $\lceil 3 \times 2\,501 / 10 \rceil$ = 751 : **1 345** payés au départ. Ils voyagent dans les 1 250 005 de soute.
- Structure totale : 50 × 12 000 + 1 000 = 601 000. Points d'expédition : 601 000 / 200 = **3 005**, sous le plafond de **6 000** (meilleur joueur sous 1 000 000 de points).
- Avec Cosmologie Appliquée 5 : jusqu'à 5 heures de maintien et **2** expéditions simultanées.

## Données détaillées

### Maintien et expéditions simultanées

| Cosmologie Appliquée | Maintien maximal | Expéditions simultanées |
|---|---|---|
| 1 | 1 h | 1 |
| 2 | 2 h | 1 |
| 3 | 3 h | 1 |
| 4 | 4 h | 2 |
| 6 | 6 h | 2 |
| 9 | 9 h | 3 |
| 12 | 12 h | 3 |
| 16 | 16 h | 4 |

### Plafond des points d'expédition

| Points du meilleur joueur | Plafond |
|---|---|
| moins de 10 000 | 200 |
| moins de 100 000 | 2 500 |
| moins de 1 000 000 | 6 000 |
| moins de 5 000 000 | 9 000 |
| moins de 25 000 000 | 12 000 |
| moins de 50 000 000 | 15 000 |
| moins de 75 000 000 | 18 000 |
| moins de 100 000 000 | 21 000 |
| 100 000 000 ou plus | 25 000 |

### Rang des vaisseaux trouvés

| Rang | Vaisseau |
|---|---|
| 1 | Éclaireur |
| 2 | Navette de fret |
| 3 | Intercepteur |
| 4 | Cargo stellaire |
| 5 | Assaillant |
| 6 | Corvette |
| 7 | Cuirassé |
| 8 | Prédateur |
| 9 | Frappe-orbital |
| 10 | Annihilateur |

Exemple : une flotte dont le meilleur vaisseau est un Cuirassé (rang 7) peut trouver jusqu'au Prédateur (rang 8). Une flotte sans vaisseau de cette table compte comme rang 1.

## Pièges fréquents

- **Rester plus longtemps ne sert à rien** pour les chances : choisissez la durée selon votre emploi du temps. Elle allonge en plus un éventuel retard.
- **Prévoyez de la soute** : une trouvaille de ressources qui ne rentre pas est perdue, et l'hydrogène du voyage occupe déjà une partie des soutes.
- **Changez de système** : l'espace lointain très fréquenté s'épuise, quel que soit le joueur qui l'a visité.
- **Un rappel annule tout** : la flotte rentre bredouille, après un retour aussi long que l'aller.
- **Le trou noir existe** : n'envoyez pas votre flotte principale.

## Pages liées

- [Les missions](/fr/fleet/missions)
- [Déplacements](/fr/fleet/movement)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des technologies](/fr/research/technologies)
- [Coordonnées](/fr/universe/coordinates)
- [Champs de ruines](/fr/combat/debris)
