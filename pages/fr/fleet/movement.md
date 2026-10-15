---
wiki_id: 35
locale: "fr"
path: "fleet/movement"
url: "https://wiki.dynastynova.com/fr/fleet/movement"
title: "Déplacements"
description: "Vitesse, durée de vol, consommation d'hydrogène et emplacements de flotte."
tags: ["fleet"]
published: true
created: "2026-10-02T13:08:52.470Z"
updated: "2026-10-06T10:31:07.317Z"
---

# Déplacements

> **En bref** : la durée d'un vol dépend de la distance, de la vitesse du vaisseau le plus lent et de la vitesse choisie, de 1 à 100 %. Sa consommation d'hydrogène dépend de la distance, des vaisseaux envoyés et de la vitesse. Voler moins vite coûte beaucoup moins cher. L'hydrogène du voyage voyage dans les soutes, avec la cargaison.
{.is-info}

> **Paramètre d'univers** : la vitesse des flottes divise la durée des vols. Elle ne change pas la consommation.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

### Emplacements de flotte
1. Le nombre de flottes en vol en même temps est limité : **emplacements de flotte = 1 + niveau de Calcul Quantique**, plus jusqu'à 3 emplacements de talents (dont un réservé aux attaques pour l'Amiral). Voir [Les talents](/fr/dynasty/talents).
2. Une flotte occupe son emplacement de son départ à son retour. Les expéditions, y compris pendant leur maintien, et les dépôts à la Station stellaire en occupent un. Les missiles et les sauts par [Porte de saut](/fr/fleet/jump-gate) n'en occupent pas. Le Navigateur dispose en plus de navettes, hors emplacements, pour les transports et stationnements entre ses propres bases.

### Vitesse
3. Vitesse d'un vaisseau = vitesse de base de son moteur × (1 + bonus × niveau de la recherche de ce moteur) : **+10 %** par niveau de Propulseur Chimique, **+20 %** de Moteur Magnétique, **+30 %** de Navigation Transdimensionnelle. Certains vaisseaux changent de moteur avec la recherche (voir [Liste des vaisseaux](/fr/fleet/ships)).
4. Une flotte avance à la vitesse de son **vaisseau le plus lent**.
5. Vous choisissez une **vitesse de 1 à 100 %**, par pas de 1 %. Dans les formules, elle devient la fraction $s$ : $s = 1$ à 100 %, $s = 0,5$ à 50 %.

### Distance
6. La distance dépend de ce qui diffère entre le départ et l'arrivée :

| Trajet | Distance |
|---|---|
| Vers une autre galaxie | 20 000 × écart entre les galaxies |
| Même galaxie, autre système | 2 700 + 95 × écart entre les systèmes |
| Même système, autre position | 1 000 + 5 × écart entre les positions |
| Entre une planète et sa lune | 5 |

7. **La carte est circulaire** pour les galaxies et pour les systèmes : l'écart se compte par le plus court chemin, en passant au besoin par le bord. Sur Redline, la galaxie 9 est voisine de la galaxie 1, et le système 99 du système 1. Les positions, elles, ne bouclent pas.

### Durée
8. Durée d'un trajet, en secondes, arrondie, au moins 1 :

$$
T = \frac{10 + \frac{3\,500}{s}\sqrt{\frac{10 \times D}{V}}}{A \times B}
$$

- $T$ : durée du trajet, en secondes ;
- $s$ : vitesse choisie, en fraction (de 0,01 pour 1 % à 1 pour 100 %) ;
- $D$ : distance du trajet (règle 6) ;
- $V$ : vitesse du vaisseau le plus lent de la flotte ;
- $A$ : vitesse des flottes de l'univers ;
- $B$ : bonus de vitesse, 1 sans bonus (règle 13).

### Consommation d'hydrogène
9. Consommation d'un trajet, arrondie à l'inférieur, au moins 1 dès qu'un vaisseau consomme :

$$
U = \sum_i \frac{F_i \times N_i \times D}{35\,000} \left( s \sqrt{\frac{V}{V_i}} + 1 \right)^2
$$

- $U$ : hydrogène du trajet ;
- $F_i$ : consommation d'un vaisseau du type $i$, celle de son moteur actuel ;
- $N_i$ : nombre de vaisseaux du type $i$ ;
- $D$ : distance du trajet ;
- $s$ : vitesse choisie, en fraction ;
- $V$ : vitesse du vaisseau le plus lent de la flotte ;
- $V_i$ : vitesse du type de vaisseau $i$.

10. Un vaisseau plus rapide que le reste de sa flotte consomme moins. Aucune recherche ne réduit la consommation ; un meilleur moteur l'augmente.
11. **Le retour est payé au départ** : chaque trajet est compté séparément, aller puis retour, pour toutes les missions sauf **Colonisation** et **Stationnement**, qui sont des allers simples. Les dépôts à la Station stellaire ne consomment rien.
12. **L'hydrogène du voyage voyage dans les soutes** : cargaison + hydrogène du voyage ne doivent pas dépasser le fret de la flotte. Un talent du Navigateur allège ce carburant.

### Bonus
13. Les bonus de vitesse (talents personnels et talent d'alliance Propulsion coordonnée, +5 % par niveau) **divisent la durée** : +50 % = un trajet 1,5 fois plus court. Ensemble, ils plafonnent à **+60 %** ; quelques talents de trajet s'ajoutent hors plafond (retour, trajets entre vos bases, rappel).
14. Les baisses de consommation (talents personnels et talent d'alliance Ravitaillement optimisé, 5 % par niveau) plafonnent ensemble à **45 %**, sans jamais descendre sous 1 par trajet.

### Rappel et retour
15. Une flotte peut être **rappelée** tant qu'elle est à l'aller ou en maintien d'expédition, pas sur le chemin du retour. Les dépôts à la Station stellaire ne se rappellent pas.
16. Une flotte rappelée rentre en autant de temps qu'elle en a déjà passé à l'aller ; une expédition rappelée pendant son maintien refait tout le trajet. Le rappel **ne rembourse pas** l'hydrogène (sauf talent du Navigateur). Une attaque rappelée ne compte plus dans la [limite d'attaques](/fr/players/attack-limit).
17. Au retour, la flotte se pose sur sa base de départ, avec sa cargaison, même au-delà de la capacité des entrepôts. **Il faut que cette base vous appartienne encore et ait un Dock orbital** : sinon, la flotte est perdue.

## Exemple chiffré

10 Intercepteurs (vitesse 12 500 × 1,6 = 20 000 avec Propulseur Chimique 6, consommation 20 chacun) attaquent de [2:40:8] vers [2:50:3]. Distance : 2 700 + 95 × 10 = **3 650**.

| Vitesse | Durée d'un trajet | Hydrogène d'un trajet | Payé au départ (aller-retour) |
|---|---|---|---|
| 100 % | 4 738 s (1 h 18 min 58 s) | 83 | 166 |
| 50 % | 9 466 s (2 h 37 min 46 s) | 46 | 92 |
| 10 % | 47 292 s (13 h 8 min 12 s) | 25 | 50 |

Par exemple à 100 % : 10 + 3 500 / 1 × √(10 × 3 650 / 20 000) ≈ 4 738 s, et 20 × 10 × 3 650 / 35 000 × (1 + 1)² ≈ 83 hydrogène. À mi-vitesse, le vol dure deux fois plus longtemps mais coûte **45 % d'hydrogène en moins**.

**Carte circulaire** : de la galaxie 1 à la galaxie 9 sur Redline, l'écart est de 1 galaxie, soit une distance de 20 000, et non 8 × 20 000. Du système 3 au système 97 d'une même galaxie, l'écart est de 5 systèmes : distance 3 175.

## Données détaillées

### Moteurs

| Moteur | Bonus par niveau | Vaisseaux (moteur d'origine) |
|---|---|---|
| Propulseur Chimique | +10 % | Navette de fret, Cargo stellaire, Récupérateur, Éclaireur, Intercepteur |
| Moteur Magnétique | +20 % | Pionnier spatial, Assaillant, Corvette, Frappe-orbital |
| Navigation Transdimensionnelle | +30 % | Cuirassé, Prédateur, Annihilateur, Colossus stellaire |

Les vitesses, consommations et changements de moteur sont sur la page [Liste des vaisseaux](/fr/fleet/ships).

### Ordres de vol des talents

Des talents ajoutent des ordres de vol : changer de vitesse en vol (Relance à 100 %, Mise en attente jusqu'à 10 %), Port d'attache, Fret retour, Livraison groupée, Ordre de chargement, Postcombustion, Redirection, Saut de retour. Ils sont décrits sur [Les talents](/fr/dynasty/talents) et l'arbre du [Navigateur](/fr/dynasty/classes/navigator).

## Pièges fréquents

- **Le plus lent impose son rythme** : un seul Récupérateur (vitesse 2 000) ralentit toute une flotte d'Intercepteurs.
- **Le retour se paie au départ** : prévoyez l'hydrogène de l'aller-retour avant d'attaquer, et la place dans les soutes pour le transporter.
- **Rappeler ne rembourse rien** : l'hydrogène dépensé est perdu.
- **Ne retirez pas le Dock orbital d'une base qui attend une flotte** : sans Dock à l'arrivée, la flotte qui rentre est perdue.
- **Pensez au bord de la carte** : la galaxie la plus proche n'est pas toujours celle qu'on croit.
- **Calcul Quantique limite vos flottes** : au niveau 2, seulement 3 flottes en vol, expéditions et dépôts compris.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Les missions](/fr/fleet/missions)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Expéditions](/fr/fleet/expeditions)
- [Porte de saut](/fr/fleet/jump-gate)
- [Missions et station d'alliance](/fr/players/alliance-missions)
