---
wiki_id: 47
locale: "fr"
path: "combat/debris"
url: "https://wiki.dynastynova.com/fr/combat/debris"
title: "Champs de ruines (débris)"
description: "Débris créés par les combats, recyclage et formation des lunes."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:15.769Z"
updated: "2026-10-02T17:40:36.847Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Champs de ruines (débris)

> **En bref** : quand des vaisseaux sont détruits, une part de leur métal et de leur cristal forme un champ de ruines en orbite, 30 % par défaut. Les défenses n'en laissent pas, sauf réglage de l'univers. Ces débris ne disparaissent jamais : il faut les recycler avec des Récupérateurs. Un gros combat peut aussi faire naître une lune.
{.is-info}

> **Paramètre d'univers** : le taux de débris des vaisseaux et des défenses, ainsi que la chance maximale de lune et les débris qui la donnent, peuvent être différents selon l'univers.
> Par défaut : vaisseaux **30 %**, défenses **0 %**, lune **20 % au plus, atteints à 2 000 000 de débris** · Redline : vaisseaux **30 %**, défenses **0 %**, lune **20 % pour 2 000 000**
{.is-info}

<img src="/images/illustrations/ships/recuperateur.jpg" width="180" alt="Récupérateur">

## Règles

### Ce qui part en débris
1. Les vaisseaux détruits **des deux camps**, civils compris, laissent le **taux de débris des vaisseaux** de l'univers (30 % par défaut) de leur coût en **métal et cristal**. L'hydrogène ne laisse rien.
2. Les **défenses** détruites laissent le **taux de débris des défenses** de l'univers : **0 %** par défaut, donc rien. Ce taux compte toutes les défenses détruites, même celles qui seront ensuite [reconstruites](/fr/combat/defense-rebuild).
3. Le total est arrondi à l'inférieur, pour le métal comme pour le cristal.
4. Les combats contre les pirates et les aliens d'[expédition](/fr/fleet/expeditions) laissent **10 %** des vaisseaux détruits, quel que soit l'univers.
5. Une mission [Destruction de lune](/fr/combat/moon-destruction) ne laisse **aucun débris**, ni du combat ni de la lune.
6. Les débris d'un combat **s'ajoutent** au champ déjà présent sur la case.

### Récupérer les débris
7. Les débris **ne disparaissent jamais**. Seul le recyclage les retire. Ils restent même si la planète en dessous est abandonnée.
8. Pour les récupérer, envoyez des **Récupérateurs** en mission **Recyclage**. Seule la soute des Récupérateurs compte ; ce qui ne rentre pas reste en orbite.
9. Le champ appartient à celui qui le recycle, quel que soit le vainqueur du combat.

### Formation d'une lune
10. Après une attaque, la planète visée peut gagner une **lune**. La chance se calcule sur les débris **de ce combat seulement** (métal plus cristal), pas sur le champ déjà en orbite :

$$p = \min\left(D \times \frac{p_{max}}{D_{max}},\ p_{max}\right) \quad\text{et}\quad p = 0 \text{ si } D < \frac{D_{max}}{p_{max}}$$

- $p$ : chance de lune, en % ; $D$ : débris du combat (métal + cristal).
- $p_{max}$ : chance maximale de l'univers (20 % par défaut) ; $D_{max}$ : débris qui donnent cette chance maximale (2 000 000 par défaut).
- Par défaut : **1 % par tranche de 100 000 débris**, rien en dessous de 100 000, 20 % au plus.

11. La lune revient **au propriétaire de la planète**, même s'il a perdu le combat. L'attaquant ne gagne jamais de lune chez un autre.
12. Pas de lune si la case en a déjà une, ni au-dessus d'une planète abandonnée, ni quand le combat a lieu au-dessus de la lune elle-même.
13. La formation **ne consomme pas** les débris : les Récupérateurs récoltent tout dans les deux cas.
14. **Taille de la lune** : elle est tirée parmi **11 tailles également probables**, d'autant plus grandes que la chance était élevée. Avec $X$ tiré entre 0 et 10 :

$$c = 10 + X + 60 \times \frac{p}{p_{max}} \qquad \text{diamètre} = \left\lfloor 1\,000 \sqrt{c} \right\rfloor \text{ km}$$

- Le dernier terme vaut au moins 3. Une lune mesure donc de **3 605 km** (chance de 1 %) à **8 944 km** (chance maximale).
- Une lune démarre avec 1 case ; au plus, elle en aura partie entière((diamètre / 1 000)²), ouvertes par la Base lunaire. Voir [Les lunes](/fr/universe/moons).

## Exemple chiffré

Vous détruisez 100 Intercepteurs (3 000 métal et 1 000 cristal chacun), dans un univers aux réglages par défaut :
- Débris : 30 % × 300 000 métal = **90 000 métal**, et 30 % × 100 000 cristal = **30 000 cristal**.
- Récolte totale : 120 000 ressources. Un Récupérateur emporte 20 000 : il en faut **6** (sans bonus de Pliage Spatial).
- Chance de lune : 120 000 × 20 / 2 000 000 = **1,2 %**. Si elle se forme, elle mesure entre **3 687 et 4 857 km**.

## Données détaillées

Débris laissés par un vaisseau détruit, au taux de 30 % :

| Vaisseau | Métal | Cristal |
|---|---|---|
| Navette de fret | 600 | 600 |
| Cargo stellaire | 1 800 | 1 800 |
| Pionnier spatial | 3 000 | 6 000 |
| Récupérateur | 3 000 | 1 800 |
| Éclaireur | 0 | 300 |
| Collecteur solaire | 0 | 600 |
| Intercepteur | 900 | 300 |
| Assaillant | 1 800 | 1 200 |
| Corvette | 6 000 | 2 100 |
| Cuirassé | 13 500 | 4 500 |
| Frappe-orbital | 15 000 | 7 500 |
| Prédateur | 9 000 | 12 000 |
| Annihilateur | 18 000 | 15 000 |
| Colossus stellaire | 1 500 000 | 1 200 000 |

Chance de lune et diamètres possibles selon les débris du combat, réglages par défaut :

| Débris du combat | Chance de lune | Diamètre (km) |
|---|---|---|
| 50 000 | 0 % | pas de lune |
| 100 000 | 1 % | 3 605 à 4 795 |
| 250 000 | 2,5 % | 4 183 à 5 244 |
| 500 000 | 5 % | 5 000 à 5 916 |
| 1 000 000 | 10 % | 6 324 à 7 071 |
| 2 000 000 | 20 % | 8 366 à 8 944 |
| 5 000 000 | 20 % | 8 366 à 8 944 |

## Pièges fréquents

- **Vos propres pertes nourrissent le champ** : un combat perdu en défense laisse aussi des débris au-dessus de votre planète, que d'autres peuvent recycler.
- **Le champ n'aide pas la lune suivante** : seuls les débris du combat qui vient d'avoir lieu comptent pour la chance de lune.
- **Pliage Spatial augmente la soute** : +5 % par niveau, utile pour recycler avec moins de Récupérateurs.
- **Le premier arrivé se sert** : le champ appartient à celui qui le recycle.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Les lunes](/fr/universe/moons)
- [Station de réparation](/fr/economy/repair-station)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
