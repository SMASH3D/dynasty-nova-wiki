---
wiki_id: 14
locale: "fr"
path: "universe/colonization"
url: "https://wiki.dynastynova.com/fr/universe/colonization"
title: "Coloniser"
description: "Fonder des colonies avec le Pionnier spatial."
tags: ["universe"]
published: true
created: "2026-10-02T13:08:12.330Z"
updated: "2026-10-15T18:55:02.503Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Coloniser

> **En bref** : pour fonder une colonie, espionnez d'abord la position visée, puis envoyez-y un Pionnier spatial en mission Colonisation. Le nombre de planètes que vous pouvez posséder dépend de votre niveau de Cosmologie Appliquée : 2 planètes au niveau 1, puis une de plus tous les deux niveaux. La colonie démarre vide, avec les ressources et les vaisseaux que vous avez envoyés.
{.is-info}

> **Paramètre d'univers** : le délai pendant lequel l'ancien propriétaire d'une planète abandonnée ne peut pas la recoloniser peut être différent selon l'univers.
> Par défaut : **30 jours** · Redline : **30 jours**
{.is-info}

<img src="/images/illustrations/ships/pionnier-spatial.jpg" width="180" alt="Pionnier spatial">

## Règles

### Avant le départ
1. Il faut un **Pionnier spatial** (Dock orbital 4, Moteur Magnétique 3, Cosmologie Appliquée 1) et une **place de colonie libre**.
2. **Nombre de planètes** (planète mère comprise) = 1 + partie entière((niveau de Cosmologie Appliquée + 1) / 2). Seules les planètes comptent : une lune n'occupe pas de place de colonie.
3. La cible doit avoir été **espionnée**, par vous ou par un membre de votre alliance. Une position jamais espionnée ne peut pas être colonisée.
4. La cible peut être :
   - une **position libre** d'un système ;
   - une planète **abandonnée** par un autre joueur. Son ancien propriétaire, lui, doit attendre 30 jours.
5. L'espace lointain, la Station stellaire et les lunes ne se colonisent pas.
6. La mission **Colonisation** est un aller simple : l'hydrogène du retour n'est pas facturé.

### À l'arrivée
7. Le jeu vérifie à nouveau la place de colonie. Si vous n'en avez plus, ou si la position a été prise entre-temps, la flotte fait demi-tour et un rapport vous l'explique.
8. **Un seul Pionnier spatial est consommé** : il devient la colonie. Les autres vaisseaux de la flotte, autres Pionniers compris, **restent sur la nouvelle colonie** et forment sa première flotte.
9. La cargaison de toute la flotte est déchargée sur la colonie : ce sont ses **ressources de départ**.
10. Sur une position libre, la colonie démarre **sans aucun bâtiment**. Construisez d'abord la **Base Coloniale** (gratuite, 10 secondes) : aucun autre bâtiment ne peut être lancé avant elle. En attendant, la colonie stocke déjà 10 000 de chaque ressource.
11. Sa taille et sa température dépendent de sa position, et elle profite du **bonus de position** (voir [Planètes](/fr/universe/planets)).
12. Sur une planète **abandonnée**, vous reprenez **tout ce qui reste** : bâtiments, ressources, vaisseaux, défenses, et sa lune avec ce qu'elle porte. La dégradation s'arrête, la production reprend à votre profit (voir [Abandonner une colonie](/fr/universe/abandoning-a-planet)).

## Exemple chiffré

Vous avez Cosmologie Appliquée niveau 3 :
- Planètes possibles : 1 + partie entière((3 + 1) / 2) = **3**, soit votre planète mère et 2 colonies.
- Monter au niveau 4 ne change rien (3 planètes). Il faut le niveau 5 pour une 4e planète.

Vous envoyez 2 Pionniers spatiaux chargés à plein vers une position libre déjà espionnée :
- Ils emportent 7 500 × 2 = **15 000 ressources**.
- À l'arrivée, un Pionnier devient la colonie, l'autre reste en orbite de la colonie, et les 15 000 ressources sont déposées sur place.

## Données détaillées

### Planètes selon la Cosmologie Appliquée

| Niveau | 0 | 1 | 3 | 5 | 7 | 9 | 11 | 13 | 15 | 17 | 19 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Planètes au total | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |

Les niveaux pairs n'ajoutent pas de planète (le niveau 2 donne autant que le niveau 1).

### Le Pionnier spatial

| Coût | Structure | Fret | Vitesse de base | Moteur | Consommation |
|---|---|---|---|---|---|
| 10 000 métal, 20 000 cristal, 10 000 hydrogène | 30 000 | 7 500 | 2 500 | Moteur Magnétique | 1 000 |

## Pièges fréquents

- **Espionnez avant de partir** : sans espionnage de la position, par vous ou votre alliance, la mission est refusée.
- **Chargez la flotte** : la colonie n'a pas d'autres ressources que celles que vous apportez.
- **Les escortes ne rentrent pas** : tout vaisseau envoyé avec le Pionnier reste sur la colonie.
- **Une colonie de plus tous les deux niveaux** : vérifiez que vous avez une place libre avant d'envoyer le Pionnier, et qu'elle l'est encore à l'arrivée.
- **Choisissez la position** : près de l'étoile, une petite planète chaude et un bonus de cristal ; au milieu du système, un bonus de métal ; loin, une grande planète froide, meilleure pour l'hydrogène.

## Pages liées

- [Planètes : taille, température, type](/fr/universe/planets)
- [Abandonner une colonie](/fr/universe/abandoning-a-planet)
- [Liste des technologies](/fr/research/technologies)
- [Les missions](/fr/fleet/missions)
- [Espionner](/fr/espionage/spying)
