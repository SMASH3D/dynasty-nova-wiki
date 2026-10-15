---
wiki_id: 49
locale: "fr"
path: "combat/simulator"
url: "https://wiki.dynastynova.com/fr/combat/simulator"
title: "Simulateur de combat"
description: "Préparer une attaque avec le simulateur."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:19.413Z"
updated: "2026-10-02T16:36:52.542Z"
---

# Simulateur de combat

> **En bref** : le simulateur rejoue un combat avec le vrai moteur du jeu avant que vous l'engagiez. Aucune flotte n'est envoyée, aucune ressource dépensée. Vous partez d'un rapport d'espionnage ou saisissez le défenseur à la main ; le simulateur livre des taux de victoire, des pertes moyennes et le champ de ruines d'un combat moyen.
{.is-info}

## Règles

### Le défenseur
1. Deux modes : **Depuis un rapport d'espionnage** ou **Saisie manuelle**. Un rapport partagé dans votre alliance peut aussi servir.
2. Depuis un rapport, chaque partie du défenseur compte comme **vue** seulement si l'espionnage a atteint son palier. Le simulateur indique ce qu'il a supposé et la date du rapport.
3. Un rapport qui **n'a pas vu la flotte** est refusé : il n'y a rien à simuler.
4. Des **défenses non vues** sont supposées **absentes** : le taux de victoire affiché est alors un plancher optimiste. Saisissez une estimation si vous en avez une.
5. Des **recherches non vues** sont supposées **égales aux vôtres**, sans vos talents.
6. Modifier une valeur importée fait passer la simulation en **saisie manuelle** : le rapport n'est plus utilisé.
7. Le défenseur combat **sans talents ni bonus de dynastie** : ils ne sont jamais révélés.
8. Les missiles du silo ne combattent jamais : ils ne figurent pas dans le simulateur.

### Votre camp
9. Votre flotte combat avec vos recherches, votre dynastie et vos talents, comme dans un vrai combat.
10. Vous pouvez saisir plus de vaisseaux que vous n'en possédez : le simulateur sert aussi à décider quoi construire.
11. Pour simuler d'autres niveaux de Systèmes Offensifs, Champs de Protection ou Métallurgie Avancée, remplissez les **trois** champs de recherche.

### Le résultat
12. Chaque simulation rejoue le combat **50 fois** et donne les **taux de victoire** de l'attaquant et du défenseur et le taux de match nul, le nombre moyen de rounds, les **pertes** et **survivants** moyens, arrondis à l'unité.
13. Le **détail round par round** est celui d'un seul des 50 combats, à titre d'exemple : il n'illustre pas la série.
14. Le **champ de ruines** est celui d'un combat moyen, débris des deux camps, au taux de débris de votre univers.
15. Certains talents ajoutent un **Butin prévu** (ce qu'une victoire rapporterait au plus, d'après le stock lu par le rapport et les soutes des survivants) ou un **Bilan de chasse**.

### Les limites
16. Une simulation est refusée au-delà de **5 000 000 unités par camp**, de **50 combats**, ou de **10 000 000 déploiements** (unités des deux camps × nombre de combats).

## Exemple chiffré

**Rapport incomplet** : votre rapport a vu la flotte, mais ni les défenses ni les recherches. Le simulateur suppose zéro défense et des technologies égales aux vôtres. Si la cible a en réalité 20 Batteries ioniques, votre vraie chance de victoire sera **plus faible** que celle affichée.

**Limite de taille** : avec 50 combats par simulation, la limite de 10 000 000 déploiements autorise 200 000 unités en tout, par exemple 100 000 de chaque côté. Avec 150 000 unités de chaque côté, (150 000 + 150 000) × 50 = 15 000 000 : la simulation est refusée.

## Pièges fréquents

- **Un rapport incomplet rend le simulateur optimiste** : complétez les catégories manquantes avant de vous fier au résultat.
- **Un vieux rapport ment** : une planète change vite, refaites un espionnage avant d'engager.
- **Le défenseur peut être plus fort que prévu** : ses talents ne sont pas simulés.
- **Les technologies comptent** : si vous connaissez celles de la cible, saisissez-les.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Champs de ruines](/fr/combat/debris)
- [Pillage](/fr/combat/plunder)
