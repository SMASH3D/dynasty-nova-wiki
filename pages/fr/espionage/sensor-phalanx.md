---
wiki_id: 54
locale: "fr"
path: "espionage/sensor-phalanx"
url: "https://wiki.dynastynova.com/fr/espionage/sensor-phalanx"
title: "Phalange de capteur"
description: "Observer les flottes depuis une lune : portée, coût, ce qui est vu."
tags: ["espionage", "lune"]
published: true
created: "2026-10-02T13:09:29.181Z"
updated: "2026-10-15T18:54:22.273Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Phalange de capteur

> **En bref** : la Phalange de capteur se construit sur une lune. Elle balaie une planète de la même galaxie et montre toutes les flottes en route qui en partent ou s'y dirigent : composition, mission et horaires. Chaque balayage coûte 5 000 hydrogène, pris sur la lune.
{.is-info}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Phalange de capteur">

> **Paramètre d'univers** : le nombre de systèmes par galaxie peut être différent selon l'univers.
> Par défaut : **fixé à la création de l'univers** · Redline : **99 systèmes**
{.is-info}

## Règles

### Construire

1. La Phalange se construit **uniquement sur une lune**, après la **Base lunaire niveau 1**.
2. Le niveau N coûte 20 000 métal, 40 000 cristal et 20 000 hydrogène, multipliés par 2 à chaque niveau (× 2^(N − 1)). Elle n'a pas de niveau maximum : seules les cases de la lune la limitent.

### Balayer

3. La Phalange balaie une **planète** de la **même galaxie**, à portée. Elle ne peut **jamais viser une lune**.
4. **Portée** = niveau² − 1 systèmes de part et d'autre de la lune, au minimum 1.
5. La galaxie **boucle** sur ses systèmes : le dernier système est voisin du premier. Une lune proche d'un bord voit donc aussi les systèmes de l'autre bout.
6. Chaque balayage coûte **5 000 hydrogène**, pris sur la lune, même si aucune flotte n'est trouvée.
7. Un balayage refusé (hors de portée, autre galaxie, lune visée, hydrogène insuffisant) ne coûte rien.
8. Vous ne pouvez pas balayer si vous êtes en mode vacances.

### Ce que montre le balayage

9. Toutes les flottes **en route** qui ont la planète pour **départ ou destination**, à l'aller comme au retour, y compris les flottes ennemies : leurs **vaisseaux**, leur **mission**, leur départ et leur destination, et leurs **heures de départ et d'arrivée**.
10. La **cargaison** reste invisible.
11. Les missions **Espionnage** et **Recyclage** n'apparaissent pas.
12. Les flottes qui partent de la **lune** de cette planète ou s'y rendent n'apparaissent pas non plus.
13. Le joueur balayé **n'est pas prévenu**.
14. Certains talents de dynastie modifient la Phalange (portée, coût, balayage prolongé, mémoire) ou la trompent : voir l'[Oracle](/fr/dynasty/classes/oracle) et l'[Ombre](/fr/dynasty/classes/shadow).

## Exemple chiffré

Votre lune est en [3:50:8] avec une Phalange niveau 4, dans une galaxie de 99 systèmes.
- Portée : 4² − 1 = **15 systèmes** de part et d'autre, soit les systèmes **35 à 65** de la galaxie 3.
- Vous pouvez balayer une planète en [3:60:5] pour 5 000 hydrogène.
- Une planète en [3:70:5] est hors de portée. Une planète en [4:50:5] est dans une autre galaxie : impossible.
- Près du bord, la portée continue de l'autre côté : depuis [3:5:8], la même Phalange couvre les systèmes **1 à 20** et **89 à 99**.

## Données détaillées

| Niveau | Portée (systèmes de chaque côté) | Métal | Cristal | Hydrogène |
|---|---|---|---|---|
| 1 | 1 | 20 000 | 40 000 | 20 000 |
| 2 | 3 | 40 000 | 80 000 | 40 000 |
| 3 | 8 | 80 000 | 160 000 | 80 000 |
| 4 | 15 | 160 000 | 320 000 | 160 000 |
| 5 | 24 | 320 000 | 640 000 | 320 000 |
| 6 | 35 | 640 000 | 1 280 000 | 640 000 |
| 7 | 48 | 1 280 000 | 2 560 000 | 1 280 000 |
| 8 | 63 | 2 560 000 | 5 120 000 | 2 560 000 |
| 9 | 80 | 5 120 000 | 10 240 000 | 5 120 000 |
| 10 | 99 | 10 240 000 | 20 480 000 | 10 240 000 |

## Pièges fréquents

- **Une flotte stationnée sur une lune échappe à la Phalange** : une lune ne se balaie pas, et le trafic de la lune n'apparaît pas sur le balayage de sa planète.
- **Le balayage est payé même vide** : 5 000 hydrogène à chaque fois.
- **Prévoir l'hydrogène sur la lune** : le coût est prélevé sur la lune, qui ne produit rien. Apportez-y l'hydrogène par transport.
- **Pas de balayage d'une autre galaxie**, quel que soit le niveau.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Porte de saut](/fr/fleet/jump-gate)
- [Espionner](/fr/espionage/spying)
- [Coordonnées](/fr/universe/coordinates)
