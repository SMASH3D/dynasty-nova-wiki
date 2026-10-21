---
wiki_id: 46
locale: "fr"
path: "combat/plunder"
url: "https://wiki.dynastynova.com/fr/combat/plunder"
title: "Pillage"
description: "Ce que l'attaquant emporte après une victoire."
tags: ["combat"]
published: true
created: "2026-10-02T13:09:13.859Z"
updated: "2026-10-21T16:00:40.477Z"
---

# Pillage

> **En bref** : quand l'attaquant gagne un combat, il emporte **50 % de chaque ressource** stockée sur la planète ou la lune visée, dans la limite de la soute libre de ses vaisseaux survivants. Si la soute est trop petite, chaque ressource est réduite dans la même proportion. Ce taux est le même dans tous les univers.
{.is-info}

## Règles

1. Le pillage n'a lieu **qu'en cas de victoire** de l'attaquant. Un match nul ou une défaite ne rapporte rien.
2. Le stock de la cible est d'abord mis à jour à l'instant de l'arrivée : la production accumulée depuis la dernière visite du joueur compte.
3. Le butin vaut **50 % de chaque ressource** (métal, cristal, hydrogène), arrondi à l'inférieur. L'énergie ne se pille pas.
4. Le butin est limité par la **soute libre des vaisseaux survivants** : leur capacité de fret, augmentée de **5 % par niveau** de Pliage Spatial, moins ce qui est déjà à bord.
5. Si le butin dépasse la soute, **chaque ressource est réduite dans la même proportion** (arrondi à l'inférieur). Il n'y a pas d'ordre de priorité entre les ressources.
6. La cible perd exactement ce qui a été emporté.
7. Le taux ne baisse pas d'une attaque à l'autre : c'est le stock de la cible qui diminue. Piller plusieurs fois le même joueur rapporte donc de moins en moins s'il ne produit pas entre-temps.
8. Une **lune** se pille comme une planète : c'est le stock de la lune qui compte.
9. Les bâtiments, les vaisseaux et les défenses ne se pillent pas.

### Ce qui modifie le pillage
10. Les talents de [dynastie et de classe](/fr/dynasty/talents) peuvent changer ces règles : le défenseur peut mettre une part de son stock à l'abri (le taux qu'il subit ne descend jamais sous **30 %**) ; l'attaquant peut piller davantage sur toute victoire (Amiral) ou sur une planète abandonnée, piller un peu sur un match nul, agrandir ses soutes ou choisir l'ordre de chargement.

## Exemple chiffré

La cible stocke 100 000 métal, 60 000 cristal et 20 000 hydrogène.
- Butin possible : 50 000 métal, 30 000 cristal, 10 000 hydrogène, soit **90 000**.
- Avec 10 Cargos stellaires survivants (250 000 de soute, 300 000 avec Pliage Spatial 4) : tout est emporté.
- Avec 50 Assaillants seulement (5 000 de soute) : la soute ne prend que 5 000 sur 90 000.
- Avec 45 000 de soute libre, soit la moitié du butin : **25 000 métal, 15 000 cristal et 5 000 hydrogène**.
- Après un premier raid complet (90 000 emportés), il reste 50 000 métal, 30 000 cristal et 10 000 hydrogène : une seconde attaque juste après, sans production entre-temps, ne peut plus emporter que **45 000**.

## Données détaillées

Capacité de fret par vaisseau, selon le niveau de Pliage Spatial :

| Vaisseau | Sans Pliage Spatial | Pliage Spatial 5 | Pliage Spatial 10 |
|---|---|---|---|
| Navette de fret | 5 000 | 6 250 | 7 500 |
| Cargo stellaire | 25 000 | 31 250 | 37 500 |
| Pionnier spatial | 7 500 | 9 375 | 11 250 |
| Récupérateur | 20 000 | 25 000 | 30 000 |
| Éclaireur | 5 | 6 | 8 |
| Intercepteur | 50 | 63 | 75 |
| Assaillant | 100 | 125 | 150 |
| Corvette | 800 | 1 000 | 1 200 |
| Cuirassé | 1 500 | 1 875 | 2 250 |
| Frappe-orbital | 500 | 625 | 750 |
| Prédateur | 750 | 938 | 1 125 |
| Annihilateur | 2 000 | 2 500 | 3 000 |
| Colossus stellaire | 1 000 000 | 1 250 000 | 1 500 000 |

## Pièges fréquents

- **Venez avec de la soute** : les vaisseaux de combat transportent peu. Ajoutez des Cargos stellaires à votre flotte d'attaque.
- **Les pertes réduisent la soute** : seuls les vaisseaux survivants emportent le butin.
- **Un match nul ne rapporte rien** : il faut éliminer toute la défense pour piller.
- **Changez de cible** : chaque raid sur le même joueur rapporte moins que le précédent.

## Pages liées

- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Limite d'attaques](/fr/players/attack-limit)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Le stockage](/fr/economy/storage)
