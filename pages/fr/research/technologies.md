---
wiki_id: 28
locale: "fr"
path: "research/technologies"
url: "https://wiki.dynastynova.com/fr/research/technologies"
title: "Liste des technologies"
description: "Toutes les technologies : effets, niveaux maximum, prérequis."
tags: ["research"]
published: true
created: "2026-10-02T13:08:39.261Z"
updated: "2026-10-02T17:40:12.608Z"
game_version: "Serveur 2.1.0 · Client 3.1.0"
---

# Liste des technologies

> **En bref** : les 17 technologies se recherchent dans un Centre d'innovation. Un niveau acquis vaut pour toutes vos planètes de l'univers. Elles débloquent bâtiments, vaisseaux et défenses, et donnent des bonus permanents : production, énergie, vitesse, soute, combat, espionnage, colonies, emplacements de flotte. Une seule étude avance à la fois dans tout l'empire.
{.is-info}

> **Paramètre d'univers** : la vitesse de recherche divise la durée des recherches.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

1. Une recherche se lance depuis une planète équipée d'un **Centre d'innovation**. Ses prérequis de bâtiment (le niveau du Centre d'innovation, le plus souvent) se lisent sur **cette planète**, ses prérequis de recherche sur tout l'empire.
2. Un niveau acquis profite à **toutes vos planètes** de l'univers.
3. **Coût** du niveau N = coût du niveau 1 × facteur^(N − 1), arrondi à l'inférieur pour chaque ressource. La recherche est **payée au lancement**.
4. **Durée** (formule plus bas) : elle ne dépend que du métal et du cristal du niveau, du **niveau effectif** du Centre d'innovation et de la vitesse de recherche de l'univers. L'hydrogène ne la change pas.
5. **Niveau effectif** = Centre d'innovation de la planète qui lance la recherche, plus les Centres mis en réseau par la [Collaboration Stellaire](/fr/research/stellar-collaboration). Il est fixé au lancement.
6. **Bonus de vitesse** (alliance, talents) : la durée est divisée par (1 + bonus). Les talents de vitesse de recherche plafonnent à 25 %, alliance et talents ensemble à 45 % ; quelques talents de classe s'y ajoutent au-delà (voir [Le Théoricien](/fr/dynasty/classes/theorist) et les autres classes). Une réduction de coût par un talent ne raccourcit pas la durée : celle-ci se calcule sur le coût du catalogue.
7. **Une seule étude à la fois pour tout l'empire.** Chaque planète a sa propre file de recherche (même taille que les [files de construction](/fr/economy/build-queue)) ; les études en file, toutes planètes confondues, passent à tour de rôle dans l'ordre où elles ont été placées. Une étude en file n'est payée qu'à son tour ; si sa planète n'a pas les ressources à ce moment-là, elle est abandonnée sans frais.
8. **Second centre d'innovation** (talent ultime de l'arbre commun) : une seconde étude peut avancer en même temps que la première, à 50 % de la vitesse normale. Elle doit porter sur une autre technologie, et ne démarre en parallèle que si aucune étude n'attend en file (voir [L'arbre commun](/fr/dynasty/common-tree)).
9. **Points** : 1 point de recherche par tranche de 1 000 ressources dépensées (métal, cristal et hydrogène).
10. **Manipulation Gravitationnelle** se paie en **énergie** : la production d'énergie de la planète qui lance la recherche doit atteindre le seuil demandé, rien n'est consommé. Elle ne prend aucun temps et ne rapporte aucun point.
11. **Annulation** : comme pour un bâtiment, 80 % du coût × part du temps restant (voir [Files de construction](/fr/economy/build-queue)).
12. Tant que le Centre d'innovation d'une planète est **en chantier**, le jeu n'y lance ni n'y met en file aucune recherche.
13. Chaque technologie a un **niveau maximum**.

### Formule de durée

$$t = \frac{M + C}{1\,000 \times (1 + L)} \times \frac{3\,600}{v}$$

- $t$ : durée en secondes, arrondie à la seconde ;
- $M$, $C$ : métal et cristal du niveau étudié (coût du catalogue) ;
- $L$ : niveau effectif du Centre d'innovation (règle 5) ;
- $v$ : vitesse de recherche de l'univers.

Avec un bonus de vitesse $b$ en pour cent (règle 6) :

$$t' = \left\lceil \frac{100 \times t}{100 + b} \right\rceil$$

- $t'$ : durée finale en secondes, arrondie au supérieur et jamais sous 1 seconde ;
- $b$ : somme des bonus de vitesse de recherche (alliance et talents), plafonnée comme dit en règle 6.

### Production du Réacteur thermonucléaire

$$E = 30 \times N \times (1{,}05 + 0{,}01 \times S)^N$$

- $E$ : énergie produite, arrondie à l'inférieur ;
- $N$ : niveau du Réacteur thermonucléaire ;
- $S$ : niveau de Science Énergétique.

## Exemple chiffré

Renseignement Tactique niveau 4, lancé depuis une planète dont le Centre d'innovation est au niveau 4, sans Collaboration Stellaire :
- Coût : 200 × 2^3 = **1 600 métal**, **8 000 cristal** et **1 600 hydrogène**.
- Durée : (1 600 + 8 000) / (1 000 × (1 + 4)) = 1,92 h, soit **1 h 55 min 12 s**.
- Avec 15 % de vitesse de recherche (talents) : 6 912 × 100 / 115, arrondi au supérieur, soit **1 h 40 min 11 s**.
- Points de recherche gagnés : (1 600 + 8 000 + 1 600) / 1 000 = **11,2**.

Manipulation Gravitationnelle : le niveau 1 demande une production d'énergie de **300 000**, le niveau 2 **900 000**, le niveau 3 **2 700 000** (facteur 3).

Maîtrise du Plasma niveau 1, sur une planète avec Excavateur minéral et Extracteur cristallin au niveau 13 (vitesse ×1) : les mines produisent 1 346 métal et 897 cristal par heure ; le Plasma ajoute **13 métal** (1 %) et **5 cristal** (0,66 %) par heure.

## Données détaillées

### Effets

| Technologie | Effet |
|---|---|
| <img src="/images/illustrations/research/science-energetique.jpg" width="48" alt="Science Énergétique"> Science Énergétique | Augmente la production d'énergie du Réacteur thermonucléaire (formule plus bas) : un Réacteur niveau 10 donne 488 énergie sans Science Énergétique, 1 213 avec Science Énergétique 10. Aucun effet sur les Capteurs photovoltaïques ni les Collecteurs solaires. |
| <img src="/images/illustrations/research/systemes-photoniques.jpg" width="48" alt="Systèmes Photoniques"> Systèmes Photoniques | Aucun effet propre : prérequis de technologies, de vaisseaux et de défenses. |
| <img src="/images/illustrations/research/manipulation-ionique.jpg" width="48" alt="Manipulation Ionique"> Manipulation Ionique | Aucun effet propre : prérequis de technologies, de vaisseaux et de défenses. |
| <img src="/images/illustrations/research/pliage-spatial.jpg" width="48" alt="Pliage Spatial"> Pliage Spatial | +5 % de capacité de soute par niveau (transport, pillage, recyclage, trouvailles d'expédition). Niveau 7 requis pour la Porte de saut. |
| <img src="/images/illustrations/research/maitrise-du-plasma.jpg" width="48" alt="Maîtrise du Plasma"> Maîtrise du Plasma | Par niveau : 1 % de métal, 0,66 % de cristal et 0,33 % d'hydrogène en plus, calculés sur la production brute des mines de chaque planète (Base planetaire exclue). |
| <img src="/images/illustrations/research/propulseur-chimique.jpg" width="48" alt="Propulseur Chimique"> Propulseur Chimique | +10 % de vitesse par niveau pour les vaisseaux qui volent au Propulseur Chimique. |
| <img src="/images/illustrations/research/moteur-magnetique.jpg" width="48" alt="Moteur Magnétique"> Moteur Magnétique | +20 % de vitesse par niveau pour les vaisseaux qui volent au Moteur Magnétique. Portée des Ogives longue portée : 5 × niveau − 1 systèmes. Au niveau 5, la Navette de fret passe à ce moteur. |
| <img src="/images/illustrations/research/navigation-transdimensionnelle.jpg" width="48" alt="Navigation Transdimensionnelle"> Navigation Transdimensionnelle | +30 % de vitesse par niveau pour les vaisseaux qui volent à la Navigation Transdimensionnelle. Le Frappe-orbital y passe au niveau 8, le Récupérateur au niveau 15. |
| <img src="/images/illustrations/research/systemes-offensifs.jpg" width="48" alt="Systèmes Offensifs"> Systèmes Offensifs | +10 % d'attaque par niveau pour vos vaisseaux et vos défenses, et +10 % de dégâts par niveau pour vos Ogives longue portée. |
| <img src="/images/illustrations/research/champs-de-protection.jpg" width="48" alt="Champs de Protection"> Champs de Protection | +10 % de bouclier par niveau pour vos vaisseaux et vos défenses. |
| <img src="/images/illustrations/research/metallurgie-avancee.jpg" width="48" alt="Métallurgie Avancée"> Métallurgie Avancée | +10 % de structure par niveau pour vos vaisseaux et vos défenses. |
| <img src="/images/illustrations/research/renseignement-tactique.jpg" width="48" alt="Renseignement Tactique"> Renseignement Tactique | Profondeur des rapports d'espionnage et contre-espionnage (voir [Espionner](/fr/espionage/spying)) ; −5 % par niveau sur l'hydrogène des missions d'espionnage, jusqu'à −50 % ; au niveau 10, une position espionnée reste découverte durablement. |
| <img src="/images/illustrations/research/calcul-quantique.jpg" width="48" alt="Calcul Quantique"> Calcul Quantique | Emplacements de flotte = 1 + niveau. Une expédition occupe aussi un emplacement. |
| <img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="48" alt="Cosmologie Appliquée"> Cosmologie Appliquée | Nombre de planètes, expéditions simultanées et maintien maximal d'une expédition (tableau plus bas). Niveau 1 requis pour les expéditions. |
| <img src="/images/illustrations/research/collaboration-stellaire.jpg" width="48" alt="Collaboration Stellaire"> Collaboration Stellaire | Met en réseau les Centres d'innovation de vos autres planètes pour raccourcir les recherches (voir [Collaboration Stellaire](/fr/research/stellar-collaboration)). |
| <img src="/images/illustrations/research/manipulation-gravitationnelle.jpg" width="48" alt="Manipulation Gravitationnelle"> Manipulation Gravitationnelle | Prérequis du Colossus stellaire. Se paie en énergie produite, ne prend aucun temps et ne rapporte aucun point. |
| <img src="/images/illustrations/research/diplomatie-stellaire.jpg" width="48" alt="Diplomatie Stellaire"> Diplomatie Stellaire | Niveau 1 requis pour fonder une alliance. Fixe la capacité de l'alliance que vous fondez (tableau plus bas). |

### Coûts, maxima et prérequis

| Technologie | Rubrique en jeu | Coût du niveau 1 (métal / cristal / hydrogène) | Facteur | Niveau max | Prérequis |
|---|---|---|---|---|---|
| Science Énergétique | Recherche Fondamentale | 0 / 800 / 400 | 2 | 25 | Centre d'innovation 1 |
| Systèmes Photoniques | Recherche Fondamentale | 200 / 100 / 0 | 2 | 20 | Centre d'innovation 1, Science Énergétique 2 |
| Manipulation Ionique | Recherche Fondamentale | 1 000 / 300 / 100 | 2 | 15 | Centre d'innovation 4, Science Énergétique 4, Systèmes Photoniques 5 |
| Pliage Spatial | Recherche Fondamentale | 0 / 4 000 / 2 000 | 2 | 15 | Centre d'innovation 7, Science Énergétique 5, Systèmes Photoniques 7, Manipulation Ionique 5 |
| Maîtrise du Plasma | Recherche Fondamentale | 2 000 / 4 000 / 1 000 | 2 | 20 | Centre d'innovation 4, Science Énergétique 8, Systèmes Photoniques 10, Manipulation Ionique 5 |
| Propulseur Chimique | Recherche en Propulsion | 400 / 0 / 600 | 2 | 15 | Centre d'innovation 1, Science Énergétique 1 |
| Moteur Magnétique | Recherche en Propulsion | 2 000 / 4 000 / 600 | 2 | 15 | Centre d'innovation 2, Science Énergétique 1, Propulseur Chimique 3 |
| Navigation Transdimensionnelle | Recherche en Propulsion | 10 000 / 20 000 / 6 000 | 2 | 15 | Centre d'innovation 7, Science Énergétique 1, Pliage Spatial 3 |
| Systèmes Offensifs | Recherche de Combat | 800 / 200 / 0 | 2 | 20 | Centre d'innovation 4 |
| Champs de Protection | Recherche de Combat | 200 / 600 / 0 | 2 | 20 | Centre d'innovation 6, Science Énergétique 3 |
| Métallurgie Avancée | Recherche de Combat | 1 000 / 0 / 0 | 2 | 20 | Centre d'innovation 2 |
| Renseignement Tactique | Recherche Stratégique | 200 / 1 000 / 200 | 2 | 15 | Centre d'innovation 3 |
| Calcul Quantique | Recherche Stratégique | 0 / 400 / 600 | 2 | 20 | Centre d'innovation 1 |
| Cosmologie Appliquée | Recherche Stratégique | 4 000 / 8 000 / 4 000 | 1,75 | 20 | Centre d'innovation 3, Renseignement Tactique 4, Moteur Magnétique 3 |
| Collaboration Stellaire | Recherche Stratégique | 240 000 / 400 000 / 160 000 | 2 | 10 | Centre d'innovation 10, Calcul Quantique 8, Pliage Spatial 8 |
| Manipulation Gravitationnelle | Recherche Stratégique | 300 000 énergie requise | 3 | 10 | Centre d'innovation 12, Science Énergétique 12, Systèmes Photoniques 12, Manipulation Ionique 8 |
| Diplomatie Stellaire | Recherche Stratégique | 5 000 / 10 000 / 5 000 | 2 | 8 | Centre d'innovation 5, Calcul Quantique 4 |

Le coût du niveau N se calcule avec le facteur : par exemple, Systèmes Offensifs niveau 5 coûte 800 × 2^4 = 12 800 métal et 3 200 cristal. Les tables complètes niveau par niveau sont prévues sur des pages à part.

### Cosmologie Appliquée

| Niveau | Planètes au total (planète mère comprise) | Expéditions simultanées | Maintien maximal d'une expédition |
|---|---|---|---|
| 0 | 1 | 0 | aucun |
| 1 | 2 | 1 | 1 h |
| 2 | 2 | 1 | 2 h |
| 3 | 3 | 1 | 3 h |
| 4 | 3 | 2 | 4 h |
| 5 | 4 | 2 | 5 h |
| 6 | 4 | 2 | 6 h |
| 7 | 5 | 2 | 7 h |
| 8 | 5 | 2 | 8 h |
| 9 | 6 | 3 | 9 h |
| 10 | 6 | 3 | 10 h |
| 11 | 7 | 3 | 11 h |
| 12 | 7 | 3 | 12 h |
| 13 | 8 | 3 | 13 h |
| 14 | 8 | 3 | 14 h |
| 15 | 9 | 3 | 15 h |
| 16 | 9 | 4 | 16 h |
| 17 | 10 | 4 | 17 h |
| 18 | 10 | 4 | 18 h |
| 19 | 11 | 4 | 19 h |
| 20 | 11 | 4 | 20 h |

Planètes au total = 1 + partie entière((niveau + 1) / 2). Expéditions simultanées = partie entière(√niveau), prises sur vos emplacements de flotte. Maintien maximal = niveau, en heures.

### Diplomatie Stellaire

| Niveau du fondateur | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| Membres de l'alliance | 10 | 15 | 20 | 25 | 30 | 35 | 40 | 50 |

Seul compte le niveau du **fondateur** de l'alliance. La capacité monte dès que le fondateur termine un niveau, et ne redescend jamais.

### Changement de moteur

Trois vaisseaux changent de moteur quand une technologie de propulsion atteint un niveau donné. Leur vitesse de base et leur consommation deviennent alors celles du nouveau moteur, et c'est la technologie de ce moteur qui les accélère.

| Vaisseau | Moteur de départ | Change de moteur à | Vitesse de base | Consommation de base |
|---|---|---|---|---|
| Navette de fret | Propulseur Chimique | Moteur Magnétique 5 | 5 000 → 10 000 | 10 → 20 |
| Frappe-orbital | Moteur Magnétique | Navigation Transdimensionnelle 8 | 4 000 → 5 000 | 700 → 700 |
| Récupérateur | Propulseur Chimique | Navigation Transdimensionnelle 15 | 2 000 → 6 000 | 300 → 900 |

## Pièges fréquents

- **Le Centre de la planète compte** : la durée et les prérequis se lisent sur la planète qui lance la recherche. Lancez depuis votre meilleur Centre ; une colonie au Centre trop faible ne peut pas lancer une technologie qui en demande davantage.
- **L'hydrogène n'allonge pas la recherche** : seuls le métal et le cristal entrent dans la durée. L'hydrogène compte dans les points.
- **Une étude en file n'est pas payée** : préparez les ressources sur la bonne planète avant son tour.
- **Calcul Quantique limite vos flottes** : avec le niveau 2, vous n'avez que 3 flottes en vol, expéditions comprises.
- **Une colonie de plus tous les deux niveaux** : Cosmologie Appliquée 2 ne donne pas de planète de plus que le niveau 1.
- **Science Énergétique n'améliore que le Réacteur thermonucléaire**, pas les Capteurs photovoltaïques ni les Collecteurs solaires.
- **Manipulation Gravitationnelle ne consomme pas d'énergie**, mais il faut la produire au moment du lancement : Capteurs, Réacteur et Collecteurs solaires de la planète comptent.
- **Systèmes Photoniques et Manipulation Ionique n'ont pas d'effet propre** : on les monte pour ce qu'ils débloquent.

## Pages liées

- [Arbre technologique](/fr/research/tech-tree)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Files de construction](/fr/economy/build-queue)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Déplacements](/fr/fleet/movement)
- [Coloniser](/fr/universe/colonization)
- [Expéditions](/fr/fleet/expeditions)
- [Alliances](/fr/players/alliances)
- [L'arbre commun](/fr/dynasty/common-tree)
