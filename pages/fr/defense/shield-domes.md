---
wiki_id: 41
locale: "fr"
path: "defense/shield-domes"
url: "https://wiki.dynastynova.com/fr/defense/shield-domes"
title: "Barrière défensive et Dôme protecteur"
description: "Les deux boucliers planétaires."
tags: ["defense"]
published: true
created: "2026-10-02T13:09:03.978Z"
updated: "2026-10-02T17:40:30.973Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Barrière défensive et Dôme protecteur

> **En bref** : la Barrière défensive et le Dôme protecteur sont des défenses à très gros bouclier, limitées à un exemplaire chacune par planète. Elles encaissent les tirs pour elles-mêmes : elles ne protègent pas les autres unités.
{.is-info}

<img src="/images/illustrations/defense/barriere-defensive.jpg" width="180" alt="Barrière défensive"> <img src="/images/illustrations/defense/dome-protecteur.jpg" width="180" alt="Dôme protecteur">

## Règles

1. **Un seul exemplaire de chaque** par planète. Une commande ne peut porter que sur une unité, et elle est refusée s'il en existe déjà une sur la planète ou dans la file.
2. En combat, ce sont des **cibles ordinaires** dotées d'un gros bouclier individuel. Elles **ne créent pas de bouclier global** autour de la planète.
3. Elles tirent très peu (attaque 1) : leur rôle est d'absorber des tirs.
4. Un tir inférieur à 1 % de leur bouclier rebondit sans effet (voir [Déroulement d'un combat](/fr/combat/how-combat-works)).
5. Comme toute défense, elles peuvent être reconstruites gratuitement après un combat (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)). Si elles sont perdues, vous pouvez en reconstruire une.
6. Face aux missiles, elles comptent bouclier + coque comme les autres défenses. Sans cible désignée, les Ogives frappent d'abord la défense la plus résistante : souvent le Dôme. Détruites par des Ogives, elles sont perdues (voir [Missiles](/fr/defense/missiles)).

## Exemple chiffré

**Un Dôme protecteur sans recherche** (bouclier 10 000, coque 10 000)
- Seuil du 1 % : 100. Un Intercepteur (vaisseau, attaque 50) est en dessous : **chacun de ses tirs rebondit**, le Dôme ne perd rien.
- Un Cuirassé (attaque 1 000) passe le seuil : 10 tirs vident le bouclier, les suivants entament la coque.

**Le même Dôme face aux Ogives longue portée**
- Résistance : 10 000 + 10 000 = **20 000**. Une Ogive fait 12 000 dégâts sans recherche : il en faut **2** qui passent les Intercepteurs.
- Avec Champs de Protection 6 et Métallurgie Avancée 6 chez le défenseur, la résistance monte à 32 000 : il faut **3** Ogives à un tireur sans recherche, mais **2** à un tireur à Systèmes Offensifs 4 (16 800 par Ogive).

## Données détaillées

|  | Barrière défensive | Dôme protecteur |
|---|---|---|
| Coût (métal / cristal) | 10 000 / 10 000 | 50 000 / 50 000 |
| Points | 20 | 100 |
| Structure | 20 000 | 100 000 |
| Coque en combat | 2 000 | 10 000 |
| Bouclier | 2 000 | 10 000 |
| Attaque | 1 | 1 |
| Durée de base | 8 h | 1 j 16 h |
| Prérequis | Dock orbital 1, Champs de Protection 2 | Dock orbital 6, Champs de Protection 6 |
| Exemplaires | 1 | 1 |
| Résistance face aux Ogives (sans recherche) | 4 000 | 20 000 |

La durée de base est divisée par (1 + niveau du Dock orbital) et par 2 à chaque niveau d'Assembleur moléculaire (voir [Liste des défenses](/fr/defense/defenses)).

## Pièges fréquents

- **Pas de bulle protectrice** : vos autres défenses et vaisseaux restent exposés.
- **Le Dôme attire les Ogives** : c'est souvent la défense la plus résistante, donc la première visée par une salve sans cible désignée.
- **Pas de deuxième commande en attente** : tant qu'un Dôme est dans la file, un second est refusé.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Missiles](/fr/defense/missiles)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
