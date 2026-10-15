---
locale: "fr"
path: "economy/stellar-bank"
title: "Banque stellaire"
description: "Échanger ses ressources contre des Crédits, et ses Crédits contre des ressources."
tags: ["economy"]
published: false
---

# Banque stellaire

> **En bref** : à la Station stellaire de votre système, vous vendez du métal, du cristal ou de l'hydrogène contre des **Crédits**, puis vous achetez avec ces Crédits la ressource qui vous manque. La banque est la seule contrepartie : chaque échange fait bouger le cours, et plus une ressource afflue, moins elle vaut. Les Crédits ne s'achètent pas avec de l'argent réel.
{.is-info}

## Règles

### Accès
1. La banque se trouve à la **Station stellaire**, la dernière ligne de chaque système dans la [vue galaxie](/fr/universe/galaxy-view) (bouton « Ouvrir la station »). La station a deux guichets : la Banque stellaire et la [trésorerie d'alliance](/fr/players/alliance-missions).
2. La banque **ouvre au 7e jour de l'univers**. Avant, la page indique qu'elle n'a pas encore ouvert.
3. Les **Crédits** sont la monnaie de la banque. Ils sont propres à chaque univers, ne plafonnent pas, ne s'érodent pas et personne ne peut vous les voler. Ils ne s'achètent pas en argent réel et n'ont rien à voir avec les Points stellaires.
4. Vendre et acheter sont impossibles en [mode vacances](/fr/players/vacation-mode).

### Vendre
5. Vendre, c'est **envoyer des cargos** à la station de votre système, depuis une planète ou une lune qui a un **Dock orbital**. Seuls les **petits et grands cargos** peuvent partir ; un envoi porte de 1 à 3 ressources.
6. Le trajet dure **1 heure à l'aller et 1 heure au retour**, quelle que soit la distance, **sans hydrogène** et **sans rappel possible**. Il occupe un emplacement de flotte.
7. Le **prix est fixé au départ**, au cours du moment. Les Crédits sont versés à l'arrivée des cargos à la station, qui rentrent ensuite à vide.
8. La banque prélève une **taxe de 10 %** sur chaque vente.
9. Une planète sur laquelle une attaque est annoncée ne peut plus vendre.

### Acheter
10. Vous achetez de 1 à 3 ressources avec vos Crédits, débités tout de suite, au cours du moment. **Pas de taxe** à l'achat : le prix monte déjà avec chaque unité prise.
11. La livraison arrive **une heure plus tard** sur la planète choisie, en une seule fois. Ce n'est pas une flotte : elle ne peut pas être interceptée, et elle n'est **pas limitée par les entrepôts** de la planète.
12. Si la planète ne vous appartient plus à l'arrivée, la livraison va sur votre planète mère.
13. Si votre solde ne couvre pas tout l'achat, rien n'est acheté. Une ligne que la banque ne peut pas servir (réserve trop basse, montant trop petit) est simplement ignorée.

### Le cours
14. Chaque ressource a sa **réserve** dans la banque : un stock de cette ressource face à un stock de Crédits. Vendre ajoute des unités à la réserve et en retire des Crédits : le cours baisse. Acheter fait l'inverse : le cours monte.
15. On ne change pas directement une ressource contre une autre : on vend la première, puis on achète la seconde. Les taux croisés affichés sont indicatifs.
16. Un **devis** s'affiche avant chaque opération : Crédits obtenus ou dépensés, taxe, taux réalisé, cours avant et après.
17. La page montre l'évolution des cours sur 24 heures, 7 jours ou 30 jours, les tendances du jour et de la semaine, et l'historique de vos opérations.

## Formules

Pour une ressource dont la réserve compte $R$ unités face à $M$ Crédits :

$$\text{cours} = \frac{M}{R} \times 1\,000$$

$$\text{vente de } \Delta \text{ unités} : \quad \text{brut} = \frac{M \times \Delta}{R + \Delta}, \quad \text{reçu} = \text{brut} - 10\,\% \times \text{brut}$$

$$\text{achat de } q \text{ unités} : \quad \text{coût} = \frac{M \times q}{R - q}$$

- $R$ : unités de la ressource dans la réserve de la banque.
- $M$ : Crédits dans la réserve.
- $\Delta$ : unités vendues ; $q$ : unités achetées (toujours moins que $R$).
- cours : Crédits pour 1 000 unités.

Les Crédits se comptent au centième, et chaque arrondi joue en faveur de la banque. La taxe reste dans la réserve.

## Exemple chiffré

Réserve de métal de 1 000 000 unités face à 1 000 Crédits (cours : 1,00 Crédit pour 1 000 métal), réserve de cristal de 666 666 unités face à 1 000 Crédits (cours : 1,50).

**Vendre 100 000 métal**
- Brut : 1 000 × 100 000 / 1 100 000 = **90,90 Crédits**.
- Taxe : 10 % = **9,09**. Reçu à l'arrivée des cargos : **81,81 Crédits**.
- Taux réalisé : 0,82 Crédit pour 1 000 métal, contre 1,00 au cours affiché. Le cours du métal tombe ensuite à environ 0,83.

**Acheter du cristal avec ces 81,81 Crédits**
- Au plus **50 415 cristal** : 1 000 × 50 415 / 616 251 = 81,81.
- Taux réalisé : environ 1,62 Crédit pour 1 000 cristal, contre 1,50 au cours affiché.

Bilan : 100 000 métal donnent 50 415 cristal. La taxe et le glissement du cours sur une grosse opération coûtent cher : 10 000 métal seuls rapportent 8,91 Crédits, soit 0,89 pour 1 000.

## Pièges fréquents

- **Les gros volumes glissent** : plus vous vendez d'un coup, moins chaque unité rapporte. Plusieurs petites ventes espacées laissent au cours le temps de remonter avec les échanges des autres.
- **Pas de retour en arrière** : une vente part sans rappel, à un prix fixé au départ.
- **Deux sortes de « crédits »** : les Crédits de la banque se gagnent en vendant des ressources ; ils n'ont rien à voir avec les packs de la boutique.
- **Univers privé** : un joueur exclu d'un univers privé perd ses Crédits de cet univers et les livraisons en cours.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Missions et station d'alliance](/fr/players/alliance-missions)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Univers privés](/fr/misc/private-universes)
