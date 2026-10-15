---
wiki_id: 56
locale: "fr"
path: "players/rankings"
url: "https://wiki.dynastynova.com/fr/players/rankings"
title: "Classements et points"
description: "Les quatre classements de joueurs, les deux classements d'alliance et le calcul des points."
tags: ["players"]
published: true
created: "2026-10-02T13:09:33.068Z"
updated: "2026-10-15T18:54:50.409Z"
---

# Classements et points

> **En bref** : tout ce que vous bâtissez rapporte des points, à raison de **1 point pour 1 000 ressources** de son coût. Les joueurs sont classés sur quatre tableaux : Points (le total), Économie, Recherche et Militaire. Les alliances ont deux classements à elles : Puissance et Progression.
{.is-info}

## Règles

### Calcul des points
1. Un élément vaut **(métal + cristal + hydrogène) / 1 000** points. L'énergie ne compte pas.
2. C'est le **coût de catalogue** qui compte, pas ce que vous avez payé : une réduction de coût (talent, bonus) ne change pas les points gagnés.
3. **Économie** : chaque niveau de bâtiment debout sur vos planètes et vos lunes. Le niveau N rapporte le coût du niveau N ; un bâtiment au niveau 10 compte donc les coûts des niveaux 1 à 10.
4. **Recherche** : chaque niveau de technologie, de la même façon.
5. **Militaire** : **tous les vaisseaux**, y compris les vaisseaux civils (Navette de fret, Cargo stellaire, Pionnier spatial, Récupérateur, Éclaireur, Collecteur solaire), toutes les défenses et tous les missiles, à quai comme en vol.
6. **Points** (le classement général) = Économie + Recherche + Militaire.
7. Les points sont gagnés à la **fin** d'un niveau de bâtiment ou de recherche, et **à chaque livraison** du chantier pour les vaisseaux et les défenses.

### Ce qui fait monter ou baisser
8. **Baissent** : vaisseaux et défenses détruits, missiles tirés, niveau de bâtiment démoli (il retire les points de ce niveau), colonie abandonnée (ses bâtiments, vaisseaux et défenses), lune détruite (ses bâtiments et tout ce qui s'y trouve).
9. **Ne baissent pas** : les vaisseaux remorqués par la Station de réparation et les défenses remises en état après un combat, puisqu'ils ne sont pas perdus. Abandonner une colonie ne retire **aucun point de recherche** : les technologies appartiennent à l'empire.
10. **Montent aussi** : vaisseaux trouvés en expédition, niveau de bâtiment offert (il compte comme un niveau construit), planète abandonnée recolonisée (vous recevez les points de ce qui y est encore debout).

### Le classement
11. Le classement est **calculé en direct**. Les points s'affichent arrondis à l'entier inférieur ; c'est aussi ce nombre arrondi qui sert à la [protection des débutants](/fr/players/beginner-protection).
12. Les flèches de **progression** comparent votre rang et vos points à la dernière photographie quotidienne du classement.
13. Le filtre **Humains** masque les joueurs non humains (marqués « Joueur IA (PvE) ») sans changer les rangs : chacun garde son rang dans l'univers.
14. La **recherche** trouve un joueur ou une alliance par pseudo, nom ou tag. Un clic sur un joueur ouvre sa **fiche** : rang, badges (« Joueur IA (PvE) », « En vacances », « Nouveau joueur ») et bouton pour lui écrire.
15. Deux joueurs à égalité de points sont départagés par un ordre interne, pas par l'ancienneté.

### Classements d'alliance
16. **Alliance Puissance** : la somme des Points de tous les membres. La trésorerie et les talents d'alliance n'y comptent pas.
17. **Alliance Progression** : le niveau et l'expérience de l'alliance ; à égalité, la première arrivée passe devant. Voir [Alliances](/fr/players/alliances).

## Exemple chiffré

- Vous montez l'Excavateur minéral du niveau 13 au niveau 14 pour 11 677 métal et 2 919 cristal : **+14,6 points** d'économie (le classement affiche l'entier inférieur).
- Vous construisez un Cuirassé (45 000 métal, 15 000 cristal) : **+60 points** militaires.
- Vous construisez 10 Cargos stellaires (12 000 ressources chacun) : **+120 points** militaires. Les vaisseaux civils comptent.
- Vous tirez 10 Ogives longue portée : **-250 points** militaires, qu'elles touchent ou non.
- Votre Cuirassé est détruit en combat et la Station de réparation ne le récupère pas : **-60 points** militaires.

## Données détaillées

Points de chaque vaisseau (coût de catalogue) :

| Vaisseau | Métal | Cristal | Hydrogène | Points |
|---|---|---|---|---|
| Navette de fret | 2 000 | 2 000 | 0 | 4 |
| Cargo stellaire | 6 000 | 6 000 | 0 | 12 |
| Pionnier spatial | 10 000 | 20 000 | 10 000 | 40 |
| Récupérateur | 10 000 | 6 000 | 2 000 | 18 |
| Éclaireur | 0 | 1 000 | 0 | 1 |
| Collecteur solaire | 0 | 2 000 | 500 | 2,5 |
| Intercepteur | 3 000 | 1 000 | 0 | 4 |
| Assaillant | 6 000 | 4 000 | 0 | 10 |
| Corvette | 20 000 | 7 000 | 2 000 | 29 |
| Cuirassé | 45 000 | 15 000 | 0 | 60 |
| Frappe-orbital | 50 000 | 25 000 | 15 000 | 90 |
| Prédateur | 30 000 | 40 000 | 15 000 | 85 |
| Annihilateur | 60 000 | 50 000 | 15 000 | 125 |
| Colossus stellaire | 5 000 000 | 4 000 000 | 1 000 000 | 10 000 |

Points de chaque défense et missile :

| Défense | Métal | Cristal | Hydrogène | Points |
|---|---|---|---|---|
| Projecteur balistique | 2 000 | 0 | 0 | 2 |
| Canon photonique | 1 500 | 500 | 0 | 2 |
| Émetteur à haute énergie | 6 000 | 2 000 | 0 | 8 |
| Batterie ionique | 2 000 | 6 000 | 0 | 8 |
| Accélérateur magnétique | 20 000 | 15 000 | 2 000 | 37 |
| Éjecteur à plasma | 50 000 | 50 000 | 30 000 | 130 |
| Barrière défensive | 10 000 | 10 000 | 0 | 20 |
| Dôme protecteur | 50 000 | 50 000 | 0 | 100 |
| Intercepteurs | 8 000 | 2 000 | 0 | 10 |
| Ogives longue portée | 12 500 | 2 500 | 10 000 | 25 |

| Classement | Ce qui compte | Ce qui fait baisser |
|---|---|---|
| Économie | Niveaux de bâtiments, planètes et lunes | Démolition, colonie abandonnée, lune détruite |
| Recherche | Niveaux de technologies | Rien |
| Militaire | Tous les vaisseaux, défenses et missiles | Unités détruites, missiles tirés, colonie abandonnée, lune détruite |
| Points | Somme des trois | Tout ce qui précède |

## Pièges fréquents

- **Une flotte de transport compte** : 100 Cargos stellaires valent 1 200 points militaires, et les perdre les retire.
- **Tirer des missiles coûte des points**, même quand ils sont interceptés.
- **Monter au classement change votre protection** : en passant un palier, vous changez la liste des joueurs que vous pouvez attaquer et de ceux qui peuvent vous attaquer.
- **Abandonner une colonie fait chuter vos points**, mais pas votre recherche.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Alliances](/fr/players/alliances)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des technologies](/fr/research/technologies)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
