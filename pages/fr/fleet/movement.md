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

> **En bref** : la durée d'un vol dépend de la distance, de la vitesse du vaisseau le plus lent et du pourcentage de vitesse choisi. Sa consommation d'hydrogène dépend de la distance, des vaisseaux envoyés et de la vitesse. Voler moins vite coûte beaucoup moins cher.
{.is-info}

> **Paramètre d'univers** : la vitesse des flottes peut être différente selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

### Emplacements de flotte
1. Le nombre de flottes en vol en même temps est limité : **emplacements de flotte = 1 + niveau de Calcul Quantique**. Une expédition occupe aussi un emplacement.

### Vitesse
2. Vitesse d'un vaisseau = vitesse de base × (1 + bonus × niveau de la recherche de son moteur) : **+10 %** par niveau de Propulseur Chimique, **+20 %** de Moteur Magnétique, **+30 %** de Navigation Transdimensionnelle.
3. Une flotte avance à la vitesse de son **vaisseau le plus lent**. Les bonus de vitesse (talents personnels et talent d'alliance Propulsion coordonnée) **divisent la durée du vol** : +50 % = un vol 1,5 fois plus court, au plus +60 % au total. Voir [Les talents](/fr/dynasty/talents).
4. Vous choisissez un **pourcentage de vitesse** de 10 à 100 %, par pas de 10. Dans les formules, il devient le facteur $S$, de 1 à 10 : $S = 1$ pour 10 %, $S = 10$ pour 100 %.

### Distance

5. Résumé du calcul des distances

| Trajet | Distance |
|---|---|
| Vers une autre galaxie | 20 000 × écart entre les galaxies |
| Même galaxie, autre système | 2 700 + 95 × écart entre les systèmes |
| Même système | 1 000 + 5 × écart entre les positions |
| Entre une planète et sa lune | 5 |

### Durée

6. Calcul

$$
T =
\frac{
10 + \frac{35000}{S}\sqrt{\frac{10 \times D}{V}}
}{
A
}
$$

- $T$ est la durée du vol de la flotte, en secondes.
- $D$ est la distance de vol calculée précédemment (voir [Coordonnées](/fr/universe/coordinates)).
- $V$ est la vitesse du vaisseau le plus lent de la flotte.
- $S$ est le facteur de vitesse choisi, de 1 (10 %) à 10 (100 %), par pas de 1.
- $A$ est le facteur d'accélération de la vitesse des flottes de l'univers.

### Consommation d'hydrogène

7. **Consommation d'un trajet**

La consommation d'un trajet est calculée comme la somme, pour chaque type de vaisseau, de :

$$
U =
\sum_i
\left(
\frac{
F_i \times N_i \times D
}{
35\,000
}
\left(
\frac{S}{10}\sqrt{\frac{V}{V_i}} + 1
\right)^2
\right)
$$

- $U$ est la consommation de carburant du trajet.
- $F_i$ est la consommation du type de vaisseau $i$.
- $N_i$ est le nombre de vaisseaux du type $i$ dans la flotte.
- $D$ est la distance du trajet.
- $S$ est le facteur de vitesse choisi, de 1 (10 %) à 10 (100 %).
- $V$ est la vitesse du vaisseau le plus lent de la flotte.
- $V_i$ est la vitesse du type de vaisseau $i$.

8. Un vaisseau plus rapide que le reste de sa flotte consomme moins.
9. **Le retour est payé au départ** (aller et retour facturés ensemble) pour toutes les missions, sauf **Colonisation** et **Stationnement**.
10. Le talent d'alliance Ravitaillement optimisé retire 5 % par niveau. Aucune recherche ne réduit la consommation d'un vaisseau.

### Rappel
11. Une flotte peut être **rappelée à tout moment avant la fin de son trajet aller**. Le rappel ne redébite rien et **ne rembourse pas** l'hydrogène.

## Exemple chiffré

10 Intercepteurs (vitesse 20 000 avec Propulseur Chimique 6, consommation 20 chacun) attaquent de [2:40:8] vers [2:50:3]. Distance : 2 700 + 95 × 10 = **3 650**.

| Vitesse | $S$ | Durée d'un trajet | Hydrogène d'un trajet | Facturé au départ (aller-retour) |
|---|---|---|---|---|
| 100 % | 10 | 10 + 35 000 / 10 × √(10 × 3 650 / 20 000) ≈ **4 738 s** (1 h 18 min 58 s) | 20 × 10 × 3 650 / 35 000 × (10 / 10 + 1)² ≈ **83** | **166** |
| 50 % | 5 | 10 + 35 000 / 5 × √1,825 ≈ **9 466 s** (2 h 37 min 46 s) | 20 × 10 × 3 650 / 35 000 × (5 / 10 + 1)² ≈ **46** | **92** |

À mi-vitesse, le vol dure deux fois plus longtemps mais coûte **45 % d'hydrogène en moins**.

## Données détaillées

### Vitesse de base et moteur

| Moteur | Bonus par niveau | Vaisseaux |
|---|---|---|
| Propulseur Chimique | +10 % | Navette de fret, Cargo stellaire, Récupérateur, Éclaireur, Intercepteur |
| Moteur Magnétique | +20 % | Pionnier spatial, Assaillant, Corvette, Frappe-orbital |
| Navigation Transdimensionnelle | +30 % | Cuirassé, Prédateur, Annihilateur, Colossus stellaire |

Les vitesses et consommations de base sont sur la page [Liste des vaisseaux](/fr/fleet/ships).

## Pièges fréquents

- **Le plus lent impose son rythme** : un seul Récupérateur (vitesse 2 000) ralentit toute une flotte d'Intercepteurs.
- **Le retour se paie au départ** : prévoyez l'hydrogène de l'aller-retour avant d'attaquer.
- **Rappeler ne rembourse rien** : l'hydrogène dépensé est perdu.
- **Calcul Quantique limite vos flottes** : au niveau 2, seulement 3 flottes en vol, expéditions comprises.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Les missions](/fr/fleet/missions)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Expéditions](/fr/fleet/expeditions)
- [Missions et station d'alliance](/fr/players/alliance-missions)
