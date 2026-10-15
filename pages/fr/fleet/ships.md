---
wiki_id: 32
locale: "fr"
path: "fleet/ships"
url: "https://wiki.dynastynova.com/fr/fleet/ships"
title: "Liste des vaisseaux"
description: "Les 14 vaisseaux : coûts, statistiques, prérequis."
tags: ["fleet", "vaisseaux"]
published: true
created: "2026-10-02T13:08:46.712Z"
updated: "2026-10-15T18:54:37.578Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des vaisseaux

> **En bref** : Dynasty Nova compte 14 vaisseaux, construits au Dock orbital. Le jeu les range en trois familles : civils (transporter, coloniser, recycler, espionner), de combat et spéciaux. Cette page donne pour chacun son coût, sa durée de construction, ses prérequis, ses statistiques et son moteur.
{.is-info}

> **Paramètre d'univers** : la vitesse de chantier divise la durée de construction des vaisseaux.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

1. Les vaisseaux se construisent au **Dock orbital**, sur une planète ou une lune. Une commande n'est acceptée que si la base peut la payer en entier ; chaque unité est ensuite payée au moment où elle entre en production (voir [Dock orbital](/fr/fleet/orbital-dock)).
2. Un vaisseau coûte **toujours le même prix**, quel que soit le nombre déjà construit.
3. Le jeu les classe en trois familles : **Vaisseaux Civils**, **Vaisseaux de Combat** et **Vaisseaux Spéciaux**.
4. Chaque vaisseau a un **moteur d'origine**. La Navette de fret, le Récupérateur et le Frappe-orbital **passent d'eux-mêmes à un meilleur moteur** quand la recherche de ce moteur atteint un niveau donné : leur vitesse de base et leur consommation changent avec lui (table plus bas). Si plusieurs objectifs sont atteints, le moteur le plus avancé l'emporte.
5. **Vitesse** = vitesse de base du moteur × (1 + bonus × niveau de la recherche de ce moteur) : **+10 %** par niveau de Propulseur Chimique, **+20 %** de Moteur Magnétique, **+30 %** de Navigation Transdimensionnelle. Une flotte avance à la vitesse de son vaisseau le plus lent (voir [Déplacements](/fr/fleet/movement)).
6. **Consommation** : aucune recherche ne la baisse. Un meilleur moteur consomme davantage.
7. **Fret** : +5 % par niveau de Pliage Spatial, arrondi à l'unité.
8. **Combat** : l'attaque, le bouclier et la structure augmentent de 10 % par niveau de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. La **coque en combat** vaut la structure divisée par 10.
9. **Points** : chaque vaisseau rapporte 1 point par tranche de 1 000 ressources de son coût (métal, cristal et hydrogène). **Tous les vaisseaux**, civils compris, comptent dans les points militaires : ils sont crédités à la livraison et retirés quand le vaisseau est perdu.
10. Le **Collecteur solaire** ne vole jamais : il reste en orbite et produit partie entière(Tmax / 4 + 20) énergie, jamais moins de 0, où Tmax est la température maximale de la planète en °C (voir [L'énergie](/fr/economy/energy)).
11. Un vaisseau détruit est perdu. Après un combat où votre base se défend, la [Station de réparation](/fr/economy/repair-station) en récupère une partie.

## Exemple chiffré

**Une Navette de fret avant et après son changement de moteur**, avec Propulseur Chimique 6 :
- Moteur Magnétique 4 : elle garde le Propulseur Chimique, vitesse 5 000 × (1 + 0,1 × 6) = **8 000**, consommation **10**.
- Moteur Magnétique 5 : elle passe au Moteur Magnétique, vitesse 10 000 × (1 + 0,2 × 5) = **20 000**, consommation **20**.

**10 Cargos stellaires avec Pliage Spatial 3** : fret d'un Cargo 25 000 × (1 + 0,05 × 3) = 28 750, soit **287 500 ressources** pour la flotte.

**Un Intercepteur** avec Propulseur Chimique 6, Systèmes Offensifs 2, Champs de Protection 0, Métallurgie Avancée 3 : vitesse 12 500 × 1,6 = **20 000** ; attaque 50 × 1,2 = **60** ; bouclier **10** ; coque en combat 4 000 × 1,3 / 10 = **520**.

## Données détaillées

### Coûts, durées et rôles

La durée de base se divise par (1 + niveau du Dock orbital) × 2^(niveau de l'Assembleur moléculaire) et par la vitesse de chantier (voir [Dock orbital](/fr/fleet/orbital-dock)).

| Vaisseau | Famille | Métal | Cristal | Hydrogène | Points | Durée de base | Rôle |
|---|---|---|---|---|---|---|---|
| <img src="/images/illustrations/ships/navette-de-fret.jpg" width="48" alt="Navette de fret"> Navette de fret | civil | 2 000 | 2 000 | 0 | 4 | 1 h 30 min | Petit transport rapide |
| <img src="/images/illustrations/ships/cargo-stellaire.jpg" width="48" alt="Cargo stellaire"> Cargo stellaire | civil | 6 000 | 6 000 | 0 | 12 | 4 h | Gros transport |
| <img src="/images/illustrations/ships/pionnier-spatial.jpg" width="48" alt="Pionnier spatial"> Pionnier spatial | civil | 10 000 | 20 000 | 10 000 | 40 | 28 h | Fonde une colonie |
| <img src="/images/illustrations/ships/recuperateur.jpg" width="48" alt="Récupérateur"> Récupérateur | civil | 10 000 | 6 000 | 2 000 | 18 | 7 h | Recycle les champs de ruines |
| <img src="/images/illustrations/ships/eclaireur.jpg" width="48" alt="Éclaireur"> Éclaireur | civil | 0 | 1 000 | 0 | 1 | 10 min | Sonde d'espionnage |
| <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="48" alt="Collecteur solaire"> Collecteur solaire | spécial | 0 | 2 000 | 500 | 2,5 | 48 min | Produit de l'énergie en orbite, ne vole pas |
| <img src="/images/illustrations/ships/intercepteur.jpg" width="48" alt="Intercepteur"> Intercepteur | combat | 3 000 | 1 000 | 0 | 4 | 30 min | Chasseur de base |
| <img src="/images/illustrations/ships/assaillant.jpg" width="48" alt="Assaillant"> Assaillant | combat | 6 000 | 4 000 | 0 | 10 | 1 h 30 min | Chasseur plus résistant |
| <img src="/images/illustrations/ships/corvette.jpg" width="48" alt="Corvette"> Corvette | combat | 20 000 | 7 000 | 2 000 | 29 | 8 h | Spécialiste anti-Intercepteur |
| <img src="/images/illustrations/ships/cuirasse.jpg" width="48" alt="Cuirassé"> Cuirassé | combat | 45 000 | 15 000 | 0 | 60 | 18 h | Vaisseau de ligne |
| <img src="/images/illustrations/ships/frappe-orbital.jpg" width="48" alt="Frappe-orbital"> Frappe-orbital | spécial | 50 000 | 25 000 | 15 000 | 90 | 24 h | Spécialiste anti-défenses |
| <img src="/images/illustrations/ships/predateur.jpg" width="48" alt="Prédateur"> Prédateur | spécial | 30 000 | 40 000 | 15 000 | 85 | 22 h | Chasseur de flottes |
| <img src="/images/illustrations/ships/annihilateur.jpg" width="48" alt="Annihilateur"> Annihilateur | spécial | 60 000 | 50 000 | 15 000 | 125 | 32 h | Le plus puissant de la flotte standard |
| <img src="/images/illustrations/ships/colossus-stellaire.jpg" width="48" alt="Colossus stellaire"> Colossus stellaire | spécial | 5 000 000 | 4 000 000 | 1 000 000 | 10 000 | 3 600 h | Vaisseau ultime, détruit les lunes |

### Statistiques de base (sans recherche, moteur d'origine)

| Vaisseau | Structure | Coque en combat | Bouclier | Attaque | Fret | Vitesse | Moteur | Consommation |
|---|---|---|---|---|---|---|---|---|
| Navette de fret | 4 000 | 400 | 10 | 5 | 5 000 | 5 000 | Propulseur Chimique | 10 |
| Cargo stellaire | 12 000 | 1 200 | 25 | 5 | 25 000 | 7 500 | Propulseur Chimique | 50 |
| Pionnier spatial | 30 000 | 3 000 | 100 | 50 | 7 500 | 2 500 | Moteur Magnétique | 1 000 |
| Récupérateur | 16 000 | 1 600 | 10 | 1 | 20 000 | 2 000 | Propulseur Chimique | 300 |
| Éclaireur | 1 000 | 100 | 0 | 0 | 5 | 100 000 000 | Propulseur Chimique | 1 |
| Collecteur solaire | 2 000 | 200 | 1 | 1 | 0 | 0 | aucun | 0 |
| Intercepteur | 4 000 | 400 | 10 | 50 | 50 | 12 500 | Propulseur Chimique | 20 |
| Assaillant | 10 000 | 1 000 | 25 | 150 | 100 | 10 000 | Moteur Magnétique | 75 |
| Corvette | 27 000 | 2 700 | 50 | 400 | 800 | 15 000 | Moteur Magnétique | 300 |
| Cuirassé | 60 000 | 6 000 | 200 | 1 000 | 1 500 | 10 000 | Navigation Transdimensionnelle | 500 |
| Frappe-orbital | 75 000 | 7 500 | 500 | 1 000 | 500 | 4 000 | Moteur Magnétique | 700 |
| Prédateur | 70 000 | 7 000 | 400 | 700 | 750 | 10 000 | Navigation Transdimensionnelle | 250 |
| Annihilateur | 110 000 | 11 000 | 500 | 2 000 | 2 000 | 5 000 | Navigation Transdimensionnelle | 1 000 |
| Colossus stellaire | 9 000 000 | 900 000 | 50 000 | 200 000 | 1 000 000 | 100 | Navigation Transdimensionnelle | 1 |

Chaque vaisseau tire une fois par round, plus les tirs supplémentaires de ses [tirs rapides](/fr/fleet/rapid-fire).

### Changements de moteur

| Vaisseau | Moteur d'origine · vitesse · consommation | Change de moteur à | Nouveau moteur · vitesse · consommation |
|---|---|---|---|
| Navette de fret | Propulseur Chimique · 5 000 · 10 | Moteur Magnétique 5 | Moteur Magnétique · 10 000 · 20 |
| Récupérateur | Propulseur Chimique · 2 000 · 300 | Moteur Magnétique 17 | Moteur Magnétique · 4 000 · 600 |
| Récupérateur | Propulseur Chimique · 2 000 · 300 | Navigation Transdimensionnelle 15 | Navigation Transdimensionnelle · 6 000 · 900 |
| Frappe-orbital | Moteur Magnétique · 4 000 · 700 | Navigation Transdimensionnelle 8 | Navigation Transdimensionnelle · 5 000 · 700 |

Le Récupérateur passe à la Navigation Transdimensionnelle dès son niveau 15, même sans Moteur Magnétique 17 : chaque objectif suffit à lui seul.

### Prérequis

| Vaisseau | Dock orbital | Recherches |
|---|---|---|
| Navette de fret | 2 | Propulseur Chimique 2 |
| Cargo stellaire | 4 | Propulseur Chimique 6 |
| Pionnier spatial | 4 | Moteur Magnétique 3, Cosmologie Appliquée 1 |
| Récupérateur | 4 | Propulseur Chimique 6, Champs de Protection 2 |
| Éclaireur | 3 | Propulseur Chimique 3, Renseignement Tactique 2 |
| Collecteur solaire | 1 | aucune |
| Intercepteur | 1 | aucune |
| Assaillant | 3 | Métallurgie Avancée 2 |
| Corvette | 5 | Moteur Magnétique 4, Manipulation Ionique 2 |
| Cuirassé | 7 | Navigation Transdimensionnelle 4 |
| Frappe-orbital | 8 | Moteur Magnétique 6, Maîtrise du Plasma 5 |
| Prédateur | 8 | Navigation Transdimensionnelle 5, Systèmes Photoniques 12, Manipulation Ionique 5 |
| Annihilateur | 9 | Navigation Transdimensionnelle 6, Métallurgie Avancée 6 |
| Colossus stellaire | 12 | Navigation Transdimensionnelle 7, Pliage Spatial 6, Manipulation Gravitationnelle 1 |

## Pièges fréquents

- **Le moteur change, la consommation aussi** : une Navette de fret au Moteur Magnétique va deux fois plus vite au départ mais consomme le double. Un Récupérateur à la Navigation Transdimensionnelle consomme trois fois plus qu'au Propulseur Chimique.
- **Un tir trop faible rebondit** : un tir inférieur à 1 % du bouclier de la cible n'a aucun effet (voir [Déroulement d'un combat](/fr/combat/how-combat-works)).
- **Le Colossus stellaire est très lent** : vitesse de base 100. Une flotte qui en contient un avance à son rythme.
- **Le facteur de distorsion n'a aucun effet** : le jeu l'affiche, mais aucun calcul ne s'en sert.
- **Le fret ne sert pas qu'au transport** : il limite aussi le pillage, le recyclage, les trouvailles d'expédition et l'hydrogène du voyage, qui voyage dans les soutes.
- **Les civils comptent aussi** : perdre des Cargos ou des Éclaireurs fait baisser vos points militaires.

## Pages liées

- [Tirs rapides](/fr/fleet/rapid-fire)
- [Dock orbital](/fr/fleet/orbital-dock)
- [Déplacements](/fr/fleet/movement)
- [Les missions](/fr/fleet/missions)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Station de réparation](/fr/economy/repair-station)
- [Glossaire](/fr/getting-started/glossary)
