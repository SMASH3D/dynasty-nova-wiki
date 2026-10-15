---
wiki_id: 36
locale: "fr"
path: "fleet/missions"
url: "https://wiki.dynastynova.com/fr/fleet/missions"
title: "Les missions"
description: "Les dix missions de flotte et leurs règles."
tags: ["fleet"]
published: true
created: "2026-10-02T13:08:54.462Z"
updated: "2026-10-06T10:31:05.368Z"
---

# Les missions

> **En bref** : une flotte part toujours avec une mission. Il en existe dix : Attaque, Transport, Stationnement, Colonisation, Espionnage, Recyclage, Expédition et Destruction de lune, plus deux dépôts à la Station stellaire du système, Dépôt à la banque et Don à l'alliance. Chacune a sa cible, ses vaisseaux autorisés et ses règles.
{.is-info}

## Règles

1. Chaque flotte occupe un **emplacement de flotte** jusqu'à son retour (voir [Déplacements](/fr/fleet/movement)).
2. L'hydrogène du **retour est payé au départ**, sauf pour la Colonisation et le Stationnement, qui sont des allers simples. Les deux dépôts à la Station stellaire ne consomment pas d'hydrogène : 1 h à l'aller, 1 h au retour, quelle que soit la distance.
3. Une flotte peut être **rappelée** tant qu'elle est à l'aller ou en maintien d'expédition, sans remboursement d'hydrogène. Les dépôts à la Station stellaire ne se rappellent pas.
4. **Composition** : l'Espionnage n'emporte que des Éclaireurs, le Recyclage que des Récupérateurs, la Destruction de lune que des Colossus stellaires, les dépôts que des Navettes de fret et des Cargos stellaires. La Colonisation exige au moins un Pionnier spatial. Le Collecteur solaire ne vole jamais.
5. Une flotte ne peut pas viser la base dont elle part, sauf pour recycler le champ de ruines de sa propre position. Une planète et sa lune sont deux bases distinctes.
6. **Vacances** : en mode vacances, vous ne pouvez envoyer aucune flotte. Un joueur en vacances ne peut recevoir ni Attaque, ni Destruction de lune, ni Transport ; l'Espionnage passe, et son rapport indique seulement que le joueur est absent.
7. **Maintenance** : pendant une maintenance, l'Attaque, l'Espionnage et la Destruction de lune ne peuvent pas partir ; les flottes déjà en vol arrivent normalement.
8. **Il n'existe ni attaque groupée, ni défense alliée** : le Stationnement ne vise que vos propres bases.
9. Le joueur attaqué reçoit une **alerte 1 minute avant l'impact** d'une Attaque, jusqu'à 6 minutes avec les talents de l'[Oracle](/fr/dynasty/classes/oracle).
10. **Retour** : la flotte rentre sur sa base de départ, qui doit encore vous appartenir et avoir un Dock orbital ; sinon elle est perdue. Ce qu'elle rapporte est déchargé même au-delà de la capacité des entrepôts.

## Données détaillées

| Mission | Cible | Ce qui se passe | À savoir |
|---|---|---|---|
| **Attaque** | Planète ou lune d'un autre joueur | Combat contre la flotte et les défenses ; en cas de victoire, [pillage](/fr/combat/plunder) | Ni vos bases, ni celles d'un membre de votre alliance (pas de tir ami). Soumise aux [protections](/fr/players/beginner-protection) et à la [limite d'attaques](/fr/players/attack-limit). Lancer une attaque met fin à votre protection de nouveau joueur |
| **Transport** | Une base, la vôtre ou celle de n'importe quel joueur, alliés compris | La cargaison est livrée, même au-delà des entrepôts ; la flotte revient | Impossible vers un joueur en vacances |
| **Stationnement** | Une de **vos** planètes ou lunes, avec un Dock orbital | La flotte et sa cargaison restent sur place | Aller simple. Si la base n'a plus de Dock orbital à l'arrivée, la cargaison est déposée et les vaisseaux rentrent |
| **Colonisation** | Position libre (pas une lune), espionnée au préalable | Un Pionnier spatial fonde la colonie et disparaît ; la cargaison devient le stock de départ, les autres vaisseaux y restent | Aller simple ; il faut une place de colonie libre (voir [Coloniser](/fr/universe/colonization)). Sinon, la flotte rentre |
| **Espionnage** | Planète ou lune d'un autre joueur | Les Éclaireurs envoient un rapport et rentrent, sauf ceux abattus | Éclaireurs seulement. Possible sur un joueur protégé ou en vacances. Hydrogène réduit de 5 % par niveau de Renseignement Tactique, au plus de moitié. Voir [Espionner](/fr/espionage/spying) |
| **Recyclage** | Une position, ou l'espace lointain | Les Récupérateurs ramassent les débris, dans la limite de leur propre soute | Récupérateurs seulement. La position doit avoir été espionnée au moins une fois, par vous ou un membre de votre alliance, sauf votre propre base et l'espace lointain. Voir [Champs de ruines](/fr/combat/debris) |
| **Expédition** | L'espace lointain du système | La flotte tient sa position puis revient, avec une trouvaille ou non | Voir [Expéditions](/fr/fleet/expeditions) |
| **Destruction de lune** | Lune d'un autre joueur | Combat, puis tentative de destruction | Colossus stellaires seulement. Voir [Destruction de lune](/fr/combat/moon-destruction) |
| **Dépôt à la banque** | La Station stellaire du système | Les ressources sont vendues contre des Crédits ; la flotte rentre à vide | Navettes de fret et Cargos stellaires seulement, depuis une base avec un Dock orbital. 1 h aller, 1 h retour, sans hydrogène, sans rappel. Voir [Banque stellaire](/fr/economy/stellar-bank) |
| **Don à l'alliance** | La Station stellaire du système | La trésorerie prend ce que son plafond permet, le reste rentre avec la flotte | Mêmes conditions que le dépôt à la banque. Voir [Missions et station d'alliance](/fr/players/alliance-missions) |

## Exemple chiffré

Vous envoyez 5 Cargos stellaires de [2:40:8] vers [2:40:12], à 100 %, avec Propulseur Chimique 6. Distance : 1 000 + 5 × 4 = 1 020 ; trajet de 3 237 s (53 min 57 s).
- En **Transport** chez un allié : l'aller (29) **et** le retour (29) sont prélevés au départ, soit **58 hydrogène**. La flotte revient.
- En **Stationnement** sur votre colonie : seul l'aller est payé, **29 hydrogène**, et la flotte y reste.
- En **Don à l'alliance** vers la Station stellaire : **0 hydrogène**, 1 h à l'aller et 1 h au retour.

Trente Éclaireurs envoyés de [2:40:8] vers [4:12:3] (distance 2 × 20 000) avec Renseignement Tactique 4 : l'aller-retour brûle 274 hydrogène, et vous n'en payez que 274 × 0,8 = **219** (arrondi à l'inférieur).

## Pièges fréquents

- **Stationnement ≠ transport** : le Stationnement ne vise que vos propres bases dotées d'un Dock orbital. Pour livrer un allié, utilisez le Transport.
- **Une attaque coûte votre protection** : la première attaque lancée met fin à vos 7 jours de protection de nouveau joueur. L'espionnage et le transport ne la retirent pas.
- **Espionnez avant de recycler ou de coloniser** : une position jamais espionnée refuse le Recyclage et la Colonisation.
- **Les emplacements sont limités** : chaque mission, expéditions et dépôts compris, occupe un emplacement jusqu'au retour de la flotte.
- **Un pacte n'empêche pas l'attaque** : contre une alliance sous pacte, l'attaque part, mais elle coûte des points de fair-play à votre alliance (voir [Pactes, fair-play et guerres](/fr/players/pacts-and-wars)).

## Pages liées

- [Déplacements](/fr/fleet/movement)
- [Pillage](/fr/combat/plunder)
- [Limite d'attaques](/fr/players/attack-limit)
- [Expéditions](/fr/fleet/expeditions)
- [Espionner](/fr/espionage/spying)
- [Banque stellaire](/fr/economy/stellar-bank)
- [Missions et station d'alliance](/fr/players/alliance-missions)
