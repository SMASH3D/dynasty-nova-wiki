---
wiki_id: 58
locale: "fr"
path: "players/attack-limit"
url: "https://wiki.dynastynova.com/fr/players/attack-limit"
title: "Limite d'attaques"
description: "6 attaques sur un même joueur par tranche de 24 heures."
tags: ["players"]
published: true
created: "2026-10-02T13:09:37.126Z"
updated: "2026-10-15T18:54:43.237Z"
---

# Limite d'attaques

> **En bref** : vous pouvez attaquer un même joueur au plus **6 fois par tranche de 24 heures**, toutes ses planètes et lunes confondues, salves de missiles comprises. La tranche s'ouvre à votre première attaque contre lui et ne glisse pas. L'attaque de trop est refusée dès l'envoi.
{.is-info}

> **Paramètre d'univers** : le nombre d'attaques et la durée de la tranche peuvent être différents selon l'univers ; un maximum de 0 désactive la règle.
> Par défaut : **6 attaques par 24 h** · Redline : **6 attaques par 24 h**
{.is-info}

## Règles

1. La limite porte sur **un couple attaquant et joueur visé** : toutes les planètes et lunes du joueur visé comptent ensemble. Chaque joueur que vous attaquez a son propre compteur.
2. Comptent : les **attaques de flotte** et les **salves de missiles** (une salve compte pour une attaque, quel que soit le nombre de missiles).
3. Ne comptent pas : l'espionnage, le transport, le stationnement, le recyclage et la destruction de lune. Quand votre quota contre un joueur est épuisé, la vue galaxie ne propose plus ni l'attaque, ni les missiles, ni la destruction de lune contre lui.
4. L'attaque est comptée **à l'envoi**. Celle qui dépasserait le maximum est **refusée à l'envoi**.
5. La **tranche est fixe** : elle s'ouvre à votre première attaque contre ce joueur et dure 24 heures. Une fois écoulée, le compteur repart à zéro, et l'attaque suivante ouvre une nouvelle tranche.
6. **Rappeler** une flotte d'attaque avant son arrivée rend le créneau. Une salve de missiles ne se rappelle pas : son créneau est consommé.
7. Les **planètes abandonnées** ne sont pas concernées : elles n'ont plus de propriétaire. Les joueurs non humains (PvE) le sont, comme les joueurs humains.
8. Les guerres et les pactes d'alliance ne changent rien à la limite. Les membres de votre propre alliance ne peuvent de toute façon pas être attaqués.
9. La vue galaxie affiche le nombre d'attaques qu'il vous reste contre chaque joueur.

## Exemple chiffré

Univers réglé à 6 attaques par 24 h, attaques contre un même joueur X :

| Heure | Action contre X | Attaques restantes |
|---|---|---|
| Lundi 10:00 | Attaque de flotte (la tranche s'ouvre jusqu'à mardi 10:00) | 5 |
| Lundi 12:00 | Attaque de flotte | 4 |
| Lundi 14:00 | Salve de missiles | 3 |
| Lundi 15:00 | Attaque de flotte, rappelée une heure plus tard : créneau rendu | 3 |
| Lundi 18:00 | Attaque de flotte | 2 |
| Lundi 19:00 | Attaque de flotte | 1 |
| Lundi 20:00 | Attaque de flotte | 0 |
| Lundi 23:00 | Attaque de flotte : **refusée à l'envoi** | 0 |
| Mardi 10:00 | La tranche est écoulée | 6 |
| Mardi 11:00 | Attaque de flotte (la tranche s'ouvre jusqu'à mercredi 11:00) | 5 |

## Pièges fréquents

- **La tranche ne glisse pas** : elle part de votre première attaque, pas de la dernière. Mais elle ne se rouvre qu'à votre prochaine attaque.
- **Les missiles comptent** : une salve est une attaque à part entière, et elle ne se rappelle pas.
- **Toutes ses planètes comptent ensemble** : attaquer deux colonies d'un même joueur consomme deux créneaux.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Missiles](/fr/defense/missiles)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Pillage](/fr/combat/plunder)
