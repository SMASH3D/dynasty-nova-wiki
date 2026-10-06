# Données relevées dans le jeu

Relevé du 2 octobre 2026, univers **Redline** (vitesses ×1), compte SMASH.
Sources : API du jeu (appels faits à l'affichage des pages), traductions embarquées dans l'application, aide intégrée (`/help`).
Ces données servent de base aux pages du wiki. Les valeurs dépendant du joueur (durées, production) sont données pour ma planète : Fabrique d'automates 4, Assembleur moléculaire 0, Centre d'innovation 4, température 20 à 60 °C.

---

## 1. Nomenclature FR / EN / ES

### Constat important

**Les vaisseaux ne sont pas traduits** : l'interface anglaise affiche « Navette de fret », « Intercepteur »… Les noms et descriptions des vaisseaux sont codés en dur en français dans le fichier `shipsData`. Tout le reste (bâtiments, recherches, défenses, missions) existe en FR, EN et ES.

Les noms anglais des recherches ne suivent pas toujours les noms FR et ES (ex. `laser` : « Laser Technology » en EN, « Systèmes Photoniques » en FR, « Sistemas Fotónicos » en ES). Même chose pour `astrophysics` : « Astrophysics » en EN, alors que sa description anglaise parle d'« Applied cosmology ».

### Bâtiments

| Code | FR | EN | ES |
|---|---|---|---|
| planetary_base | Base planetaire | Planetary Base | Base Planetaria |
| planetary_base_colony | Base Coloniale | Colonial Base | Base Colonial |
| metal_mine | Excavateur minéral | Mineral Excavator | Excavadora Mineral |
| crystal_mine | Extracteur cristallin | Crystal Extractor | Extractor de Cristal |
| hydrogen_synthesizer | Condensateur d'hydrogène | Hydrogen Condenser | Condensador de Hidrógeno |
| solar_plant | Capteurs photovoltaïques | Photovoltaic Sensors | Sensores Fotovoltaicos |
| fusion_plant | Réacteur thermonucléaire | Thermonuclear Reactor | Reactor Termonuclear |
| metal_storage | Dépôt d'alliages | Alloy Depot | Depósito de Aleaciones |
| crystal_storage | Chambre cristalline | Crystal Chamber | Cámara de Cristal |
| hydrogen_storage | Citerne d'hydrogène | Hydrogen Tank | Tanque de Hidrógeno |
| research_lab | Centre d'innovation | Innovation Center | Centro de Innovación |
| robotic_factory | Fabrique d'automates | Automaton Factory | Fábrica de Autómatas |
| shipyard | Dock orbital | Orbital Dock | Hangar Orbital |
| nanite_factory | Assembleur moléculaire | Molecular Assembler | Ensamblador Molecular |
| repair_dock | Station de réparation | Repair Station | Estación de Reparación |
| terraformer | Modulateur planétaire | Planetary Modulator | Modulador Planetario |
| missile_silo | Arsenal balistique | Ballistic Arsenal | Arsenal Balístico |
| logistics_center | Centre logistique | Logistics Center | Centro Logístico |
| lunar_base | Base lunaire | Lunar base | Base lunar |
| sensor_phalanx | Phalange de capteur | Sensor phalanx | Falange sensorial |
| jump_gate | Porte de saut | Jump gate | Puerta de salto |

### Recherches

| Code | FR | EN | ES |
|---|---|---|---|
| energy_science | Science Énergétique | Energy Science | Ciencia Energética |
| plasma | Maîtrise du Plasma | Plasma Technology | Maestría del Plasma |
| quantum_computing | Calcul Quantique | Quantum Computing | Computación Cuántica |
| research_network | Collaboration Stellaire | Stellar Collaboration | Colaboración Estelar |
| interstellar_diplomacy | Diplomatie Stellaire | Stellar Diplomacy | Diplomacia Estelar |
| combustion_drive | Propulseur Chimique | Combustion Drive | Motor de Combustión |
| impulse_drive | Moteur Magnétique | Impulse Drive | Motor de Impulso |
| hyperspace_drive | Navigation Transdimensionnelle | Hyperspace Drive | Motor Hiperespacial |
| laser | Systèmes Photoniques | Laser Technology | Sistemas Fotónicos |
| ion | Manipulation Ionique | Ion Technology | Manipulación Iónica |
| hyperspace | Pliage Spatial | Hyperspace Technology | Plegado Espacial |
| weapons | Systèmes Offensifs | Weapon Systems | Sistemas Ofensivos |
| shielding | Champs de Protection | Shielding Technology | Campos de Protección |
| armor | Métallurgie Avancée | Armor Technology | Metalurgia Avanzada |
| graviton | Manipulation Gravitationnelle | Graviton Technology | Tecnología de Gravitones |
| espionage | Renseignement Tactique | Espionage Technology | Inteligencia Táctica |
| astrophysics | Cosmologie Appliquée | Astrophysics | Astrofísica |

### Défenses et missiles

| Code | FR | EN | ES |
|---|---|---|---|
| ballistic_projector | Projecteur balistique | Ballistic Projector | Proyector balístico |
| photonic_cannon | Canon photonique | Photonic Cannon | Cañón fotónico |
| high_energy_emitter | Émetteur à haute énergie | High-Energy Emitter | Emisor de alta energía |
| ion_battery | Batterie ionique | Ion Battery | Batería iónica |
| magnetic_accelerator | Accélérateur magnétique | Magnetic Accelerator | Acelerador magnético |
| plasma_ejector | Éjecteur à plasma | Plasma Ejector | Eyector de plasma |
| defensive_barrier | Barrière défensive | Defensive Barrier | Barrera defensiva |
| protective_dome | Dôme protecteur | Protective Dome | Cúpula protectora |
| interceptors | Intercepteurs | Interceptors (wiki EN : **Interception Missile**, `glossary-03`) | Interceptores |
| long_range_warheads | Ogives longue portée | Long-Range Warheads | Ojivas de largo alcance |

### Vaisseaux (FR seulement, voir constat)

| Code | FR (affiché dans toutes les langues) | EN provisoire (wiki) | Équivalent OGame |
|---|---|---|---|
| small_cargo | Navette de fret | Cargo Shuttle | Petit transporteur |
| large_cargo | Cargo stellaire | Stellar Freighter | Grand transporteur |
| colony_ship | Pionnier spatial | Space Pioneer | Vaisseau de colonisation |
| recycler | Récupérateur | Salvager | Recycleur |
| espionage_probe | Éclaireur | Scout | Sonde d'espionnage |
| solar_satellite | Collecteur solaire | Solar Collector | Satellite solaire |
| light_fighter | Intercepteur | Interceptor | Chasseur léger |
| heavy_fighter | Assaillant | Assailant | Chasseur lourd |
| cruiser | Corvette | Corvette | Croiseur |
| battleship | Cuirassé | Battleship | Vaisseau de bataille |
| bomber | Frappe-orbital | Orbital Striker | Bombardier |
| predator | Prédateur | Predator | Traqueur |
| destroyer | Annihilateur | Annihilator | Destructeur |
| battle_cruiser | Colossus stellaire | Stellar Colossus | Étoile de la mort |

Attention : le code `battle_cruiser` désigne le Colossus (équivalent de l'Étoile de la mort), et le code `predator` l'équivalent du Traqueur d'OGame.

### Missions

| Code | FR | EN | ES |
|---|---|---|---|
| attack | Attaque | Attack | Ataque |
| spy | Espionnage | Espionage | Espionaje |
| transport | Transport | Transport | Transporte |
| colonize | Colonisation | Colonization | Colonización |
| deploy | Stationnement | Stationing | Estacionamiento |
| expedition | Expédition | Expedition | Expedición |
| recycle | Recyclage | Recycling | Reciclaje |
| destroy | Destruction de lune | Moon destruction | Destrucción de luna |

**Il n'y a ni attaque groupée ni défense alliée** (`fleet-05`). L'attaque groupée est un chantier à part, non planifié (le terme existe déjà dans les traductions). La défense alliée est en réflexion. Le Stationnement ne vise que ses propres bases ; le Transport peut viser un allié.

---

## 2. Univers Redline (`/universes/{id}`)

| Paramètre | Valeur |
|---|---|
| Galaxies × systèmes × positions | 9 × 99 × 15 |
| Joueurs max / inscrits | 1 000 / 235 |
| Vitesses économie, construction, recherche, chantier, flotte | ×1 partout |
| Mode, type, visibilité | pvp, quantum, public. Le type (andromeda, orion, quantum, vega) et le biome d'univers (1 à 8) sont tirés au hasard et purement cosmétiques (`universe-01`) |
| Ouverture | 26 septembre 2026, 16:00 UTC |
| Ressources de départ | 500 métal, 500 cristal |
| Anti-bash | 6 attaques sur 24 h |
| Protection débutants | paliers 500 → 1:3, 5 000 → 1:5, 500 000 → 1:10 ; perdue après `inactivityDays` = 7 jours d'inactivité sur Redline (confirmé, `players-10`), 14 par défaut selon l'équipe (`players-06`), réglable par univers |
| Débris (« Champ de ruines » dans le jeu en FR) | 30 % pour les vaisseaux, 0 % pour les défenses |
| Formation de lune | chance max 20 %, atteinte pour 2 000 000 de débris |
| Files de construction | 2 ordres par file, 5 en Premium (l'ordre en cours compris) |
| Favoris | 10, 200 en Premium |
| Règle d'abandon (planète abandonnée) | durée de vie max 60 jours ; bâtiments −1 niveau au départ puis −1 tous les 2 jours ; flotte −30 % puis −5 % tous les 2 jours ; défenses −35 % puis −5 % tous les 3 jours ; collecteurs solaires perdus à 100 % ; l'ancien propriétaire ne peut pas recoloniser pendant 30 jours |

---

## 3. Planètes et position (équipe, `universe-05`, `universe-06`)

- **Taille** (cases) = taille moyenne de la position ± 15, tirée au hasard à la génération. La **planète mère démarre toujours à 163 cases** et est placée de préférence dans le tiers central du système.
- **Température** : base = 160 − 15 × position ; min = base − 20 ; max = base + 20. La température actuelle oscille entre min et max au fil du mois, avec un pic à mi-mois.
- La température agit sur : le Condensateur (1,44 − 0,004 × Tmax), le Collecteur solaire (Tmax / 4 + base), les Capteurs photovoltaïques (× (1 + T actuelle / 100) si positive).
- **Types** : desert, dry (aride), normal, jungle, water, ice, gas. Le type ne change que le nom généré et les visuels. Valeurs techniques : `unknown` (case non explorée), `deep_space` (position N+1 en bout de système, jamais de corps, seulement débris et flottes).
- **Biome de planète** (1 à 6) : variante visuelle, masquée par un skin de boutique. Les lunes n'ont ni type ni biome.

| Position | Taille moyenne | Types possibles | Temp. min / max (°C) |
|---|---|---|---|
| 1 | 145 | desert, dry | 125 / 165 |
| 2 | 150 | desert, dry | 110 / 150 |
| 3 | 155 | desert, dry, normal | 95 / 135 |
| 4 | 160 | dry, normal | 80 / 120 |
| 5 | 163 | normal, water | 65 / 105 |
| 6 | 185 | normal, water, jungle | 50 / 90 |
| 7 | 190 | normal, water, jungle | 35 / 75 |
| 8 | 195 | water, jungle | 20 / 60 |
| 9 | 200 | water, jungle, normal | 5 / 45 |
| 10 | 205 | jungle, normal | −10 / 30 |
| 11 | 225 | ice, normal | −25 / 15 |
| 12 | 230 | ice, gas | −40 / 0 |
| 13 | 235 | ice, gas | −55 / −15 |
| 14 | 242 | ice, gas | −70 / −30 |
| 15 | 245 | ice, gas | −85 / −45 |

### Exemple : ma planète mère (`/bases/{id}`)

- Type « water », biome 5, température 20 à 60 °C (actuelle 23).
- Taille : 163 cases, 66 utilisées, 97 libres. Chaque bâtiment occupe 1 case par niveau, sauf la Station de réparation (0).
- Champs `moonDiameter`, `moonMaxFields`, `jumpGateReadyAt` : les **lunes existent**.
- Énergie : production 1 171, consommation 1 108, taux d'utilisation 95 %.
- Une ligne « Bonus de position » (`position_bonus`) et « Doctrine d'alliance » (`alliance_bonus`) peuvent modifier la production.
- Renommer la planète : premier renommage gratuit, puis coût en Points stellaires.

---

## 4. Bâtiments (`/buildings`, `/buildings/{code}`)

Coût du niveau N = coût du niveau 1 × facteur^(N−1). Points = (métal + cristal + hydrogène) / 1 000.

| Code | Catégorie | Niveau max | Coût niv. 1 (M / C / H / énergie) | Facteur | Prérequis |
|---|---|---|---|---|---|
| planetary_base | base | 1 | (donnée au départ) | | aucun |
| metal_mine | production | 50 | 60 / 15 / 0 | 1,5 | aucun |
| crystal_mine | production | 50 | 48 / 24 / 0 | 1,6 | aucun |
| hydrogen_synthesizer | production | 50 | 225 / 75 / 0 | 1,5 | aucun |
| solar_plant | energy | 50 | 75 / 30 / 0 | 1,5 | aucun |
| fusion_plant | energy | 50 | 900 / 360 / 180 | 1,8 | Condensateur 5, Science énergétique 3 |
| metal_storage | storage | 20 | 1 000 / 0 / 0 | 2 | aucun |
| crystal_storage | storage | 20 | 1 000 / 500 / 0 | 2 | aucun |
| hydrogen_storage | storage | 20 | 1 000 / 1 000 / 0 | 2 | aucun |
| research_lab | research | 12 | 200 / 400 / 200 | 2 | aucun |
| robotic_factory | facility | 10 | 400 / 120 / 200 | 2 | aucun |
| shipyard | facility | 12 | 400 / 200 / 100 | 2 | Fabrique d'automates 2 |
| nanite_factory | facility | 10 | 1 000 000 / 500 000 / 100 000 | 2 | Fabrique d'automates 10, Calcul quantique 10 |
| repair_dock | shipyard | 10 | 200 / 0 / 50 / 50 énergie | 5 | Dock orbital 2 |
| terraformer | resource | 10 | 0 / 50 000 / 100 000 / 1 000 énergie | 2 | Assembleur moléculaire 1, Science énergétique 12 |
| missile_silo | resource | 10 | 20 000 / 20 000 / 1 000 | 2 | Dock orbital 1 |
| logistics_center | resource | 10 | 20 000 / 40 000 / 0 | 2 | Calcul quantique 2 |

Bâtiments lunaires (Base lunaire, Phalange de capteur, Porte de saut) : présents dans les traductions, absents du catalogue planète. Coûts et prérequis identiques à OGame (`universe-09`). Diamètre et formation des lunes identiques à OGame : 1 % par 100 000 débris, plafonné à 20 % (`universe-08`).

### Production et consommation observées

| Bâtiment | Niveau | Production / h | Énergie |
|---|---|---|---|
| Base planétaire | 1 | 20 métal, 10 cristal | 0 |
| Excavateur minéral | 13 → 22 | 1 346, 1 594, 1 879, 2 205, 2 577, 3 002, 3 486, 4 036, 4 662, 5 372 | −448 → −1 790 |
| Extracteur cristallin | 13 → 22 | 897, 1 063, 1 253, 1 470, 1 718, 2 001, 2 324, 2 690, 3 108, 3 581 | identique au métal |
| Condensateur d'hydrogène | 9 → 18 | 254, 311, 376, 451, 538, 637, 751, 882, 1 031, 1 200 | −212 → −1 000 |
| Capteurs photovoltaïques | 13 → 22 | | +1 104 → +4 405 |
| Réacteur thermonucléaire | 1 → 10 | −11 → −259 hydrogène | +32 → +647 |

Formules vérifiées sur ces valeurs (identiques à OGame) :

- Excavateur minéral : 30 × N × 1,1^N métal/h ; consommation 10 × N × 1,1^N.
- Extracteur cristallin : 20 × N × 1,1^N cristal/h ; consommation 10 × N × 1,1^N.
- Condensateur : consommation **10** × N × 1,1^N (20 dans OGame : **divergence**). Production 10 × N × 1,1^N × (1,44 − 0,004 × Tmax) ✅ (équipe, `economy-04`).
- Réacteur thermonucléaire : 30 × N × (1,05 + 0,01 × Science énergétique)^N énergie ; consommation 10 × N × 1,1^N hydrogène.
- Capteurs photovoltaïques : 20 × N × 1,1^N × (1 + T actuelle / 100) quand la température actuelle est positive ✅ (équipe). Vérifié : T = 23 °C donne ×1,23, soit 1 104 au niveau 13.
- Collecteur solaire : Tmax / 4 + énergie de base par unité ✅ (équipe). Vérifié : 60 / 4 + 20 = 35.
- Stockage : 5 000 × arrondi inférieur(2,5 × e^(20 × N / 33)). Niveau 1 = 20 000, niveau 2 = 40 000, plus 10 000 de la Base planétaire.
- Durée de construction (h) = (métal + cristal) / (2 500 × (1 + Fabrique d'automates) × 2^Assembleur moléculaire). Vérifié sur l'Excavateur 13 : 2 802 s.

### Station de réparation

Part des vaisseaux détruits récupérée (`salvagedShare`, relevée dans le jeu) : niv. 1 31,5 % ; 2 33,6 % ; 3 34,3 % ; 4 35 % ; 5 35,7 % ; 6 36,4 % ; 7 37,1 % ; 8 37,1 % ; 9 37,8 % ; 10 37,8 %. Durée de construction : 72 s au niv. 1, ×5 à chaque niveau.

Règles (équipe, `economy-08`) :
- N'intervient qu'après un combat **perdu en défense**.
- Part = coefficient du niveau × (1 − taux de débris de l'univers). Coefficient de 45 % au niv. 1 à 54 % au niv. 10, le niveau maximum du jeu (le wiki s'arrête au niveau 10). Avec 30 % de débris : 31,5 % au niv. 1, 35 % au niv. 4.
- Appliquée à chaque type de vaisseau séparément, arrondie à l'inférieur : quelques pertes peuvent ne rien rapporter.
- Délai : 10 points de structure réparés par seconde et par niveau, × vitesse chantier de l'univers ; borné entre 30 min et 12 h. Tous les vaisseaux d'un même combat reviennent ensemble.
- Pendant la réparation, les vaisseaux sont hors stock : ils ne défendent pas, ne peuvent être ni détruits ni pillés, ne comptent ni dans les flottes ni dans les points. Ils reviennent intacts. Réparation non annulable.
- Pas de consommation d'énergie en fonctionnement (l'énergie est un seuil requis pour construire).
- Les vaisseaux récupérés figurent dans les pertes du rapport de combat.

### Démolition

Règles (équipe, `economy-07`) :
- Démolir un niveau ne coûte rien et ne rend rien. Seul gain : la case libérée. Les points du niveau sont retirés.
- Durée = moitié de la durée de construction du niveau retiré (bonus Fabrique d'automates et Assembleur moléculaire compris).
- Impossible sur la Base planétaire ou un bâtiment au niveau 0. On ne peut pas mettre en file une amélioration et une démolition du même bâtiment.
- Le Dock orbital ne peut être ni amélioré ni démoli pendant qu'il produit des unités.

### Modulateur planétaire (équipe, `economy-09`)

Coût niv. 1 : 50 000 cristal, 100 000 hydrogène, **1 000 énergie requise** (seuil de production brute, non consommée). Coût ×2 par niveau. Prérequis : Assembleur moléculaire 1, Science énergétique 12. Max 10. Chaque niveau ajoute 5 cases, +1 aux niveaux pairs ; il occupe lui-même 1 case par niveau. Une planète pleine accepte toujours une montée du Modulateur.

| Niveau | Cristal | Hydrogène | Énergie requise | Cases ajoutées | Gain net | Cumul brut |
|---|---|---|---|---|---|---|
| 1 | 50 000 | 100 000 | 1 000 | +5 | +4 | 5 |
| 2 | 100 000 | 200 000 | 2 000 | +6 | +5 | 11 |
| 3 | 200 000 | 400 000 | 4 000 | +5 | +4 | 16 |
| 4 | 400 000 | 800 000 | 8 000 | +6 | +5 | 22 |
| 5 | 800 000 | 1 600 000 | 16 000 | +5 | +4 | 27 |
| 6 | 1 600 000 | 3 200 000 | 32 000 | +6 | +5 | 33 |
| 7 | 3 200 000 | 6 400 000 | 64 000 | +5 | +4 | 38 |
| 8 | 6 400 000 | 12 800 000 | 128 000 | +6 | +5 | 44 |
| 9 | 12 800 000 | 25 600 000 | 256 000 | +5 | +4 | 49 |
| 10 | 25 600 000 | 51 200 000 | 512 000 | +6 | +5 | 55 |

### Centre logistique (équipe et jeu, 2 octobre 2026 au soir)

**N'est plus un prérequis de Diplomatie Stellaire.** Il agrandit les entrepôts de 10 % par niveau (`storagePercent` : 10 à 100 %). Prérequis : Calcul Quantique 2. Max 10. Coût niveau 1 : 20 000 métal, 40 000 cristal, ×2 par niveau. Diplomatie Stellaire ne demande plus que Centre d'innovation 5 et Calcul Quantique 4.

### Annulation et remboursement (équipe, `economy-05`, `economy-06`, `fleet-01`)

- Bâtiments et recherches : payés **au lancement**. Une commande encore en file n'a rien payé : l'annuler ne coûte et ne rend rien.
- Annulation d'un bâtiment ou d'une recherche lancé : remboursement = 80 % × (temps restant / durée totale), arrondi à l'inférieur par ressource. (Les 72,7 % observés = annulation après environ 9 % du temps.)
- Vaisseaux et défenses : payés **par unité à la mise en file**. Annulation : 80 % des unités payées mais non livrées, sans prorata ; les unités livrées sont conservées.
- L'énergie n'est jamais remboursée (elle n'est pas dépensée).

---

## 5. Recherches (`/researches`, `/researches/{code}`)

| Code | Catégorie | Niveau max | Coût niv. 1 (M / C / H) | Facteur | Prérequis |
|---|---|---|---|---|---|
| energy_science | energy | 25 | 0 / 800 / 400 | 2 | Centre d'innovation 1 |
| plasma | energy | 20 | 2 000 / 4 000 / 1 000 | 2 | Centre 4, Science énergétique 8, Systèmes photoniques 10, Manipulation ionique 5 |
| quantum_computing | computer | 20 | 0 / 400 / 600 | 2 | Centre 1 |
| research_network | computer | 10 | 240 000 / 400 000 / 160 000 | 2 | Centre 10, Calcul quantique 8, Pliage spatial 8 |
| interstellar_diplomacy | computer | 8 | 5 000 / 10 000 / 5 000 | 2 | Centre 5, Calcul quantique 4 (Centre logistique 3 retiré le 2 octobre au soir) |
| combustion_drive | drive | 15 | 400 / 0 / 600 | 2 | Centre 1, Science énergétique 1 |
| impulse_drive | drive | 15 | 2 000 / 4 000 / 600 | 2 | Centre 2, Science énergétique 1, Propulseur chimique 3 |
| hyperspace_drive | drive | 15 | 10 000 / 20 000 / 6 000 | 2 | Centre 7, Science énergétique 1, Pliage spatial 3 |
| laser | weapons | 20 | 200 / 100 / 0 | 2 | Centre 1, Science énergétique 2 |
| ion | weapons | 15 | 1 000 / 300 / 100 | 2 | Centre 4, Science énergétique 4, Systèmes photoniques 5 |
| hyperspace | weapons | 15 | 0 / 4 000 / 2 000 | 2 | Centre 7, Science énergétique 5, Systèmes photoniques 7, Manipulation ionique 5 |
| weapons | weapons | 20 | 800 / 200 / 0 | 2 | Centre 4 |
| graviton | weapons | 10 | 300 000 énergie au niv. 1, ×3 par niveau | 3 | Centre 12, Science énergétique 12, Systèmes photoniques 12, Manipulation ionique 8 |
| shielding | defense | 20 | 200 / 600 / 0 | 2 | Centre 6, Science énergétique 3 |
| armor | defense | 20 | 1 000 / 0 / 0 | 2 | Centre 2 |
| espionage | exploration | 15 | 200 / 1 000 / 200 | 2 | Centre 3 |
| astrophysics | exploration | 20 | 4 000 / 8 000 / 4 000 | 1,75 | Centre 3, Renseignement tactique 4, Moteur magnétique 3 |

- Durée (h) = (métal + cristal) / (1 000 × (1 + niveau effectif du Centre d'innovation)). Vérifié sur Renseignement tactique 4 : 6 912 s.
- Graviton : durée 0 et 0 point (payé en énergie).
- Effets observés : Maîtrise du Plasma niv. 1 → +13 métal/h et +5 cristal/h sur ma planète ; Diplomatie Stellaire niv. 1 → capacité d'alliance +10 ; Calcul Quantique → emplacements de flotte (« Améliorez Calcul Quantique »).
- Bonus de combat : Systèmes Offensifs +10 % attaque, Champs de Protection +10 % bouclier, Métallurgie Avancée +10 % structure, par niveau (vaisseaux et défenses). Pliage Spatial +5 % de capacité de fret par niveau.
- Vitesse : Propulseur Chimique +10 %, Moteur Magnétique +20 %, Navigation Transdimensionnelle +30 % par niveau selon le moteur du vaisseau.
- Collaboration Stellaire : « Le Centre d'innovation le plus avancé de votre empire accélère cette recherche, à condition qu'il soit au moins aussi avancé que celui de cette base. »

---

## 6. Vaisseaux (`/ships?page=1&itemsPerPage=100`)

Coût M / C / H ; structure (coque) ; bouclier ; attaque ; fret ; vitesse ; facteur de distorsion (`warpFactor`) ; consommation ; durée (s, ma planète, Dock orbital 4).

| Vaisseau | Type | Coût | Prérequis | Structure | Bouclier | Attaque | Fret | Vitesse | Distorsion | Conso | Durée |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Navette de fret | civil | 2 000 / 2 000 / 0 | Dock 2, Propulseur chimique 2 | 4 000 | 10 | 5 | 5 000 | 5 000 | 1 | 10 | 1 080 |
| Cargo stellaire | civil | 6 000 / 6 000 / 0 | Dock 4, Propulseur chimique 6 | 12 000 | 25 | 5 | 25 000 | 7 500 | 1 | 50 | 2 880 |
| Pionnier spatial | civil | 10 000 / 20 000 / 10 000 | Dock 4, Moteur magnétique 3, Cosmologie appliquée 1 | 30 000 | 100 | 50 | 7 500 | 2 500 | 1 | 1 000 | 20 160 |
| Récupérateur | civil | 10 000 / 6 000 / 2 000 | Dock 4, Propulseur chimique 6, Champs de protection 2 | 16 000 | 10 | 1 | 20 000 | 2 000 | 1 | 300 | 5 040 |
| Éclaireur | civil | 0 / 1 000 / 0 | Dock 3, Propulseur chimique 3, Renseignement tactique 2 | 1 000 | 0 | 0 | 5 | 100 000 000 | 1 | 1 | 120 |
| Collecteur solaire | advanced | 0 / 2 000 / 500 | Dock 1 | 2 000 | 1 | 1 | 0 | 0 | 0 | 0 | 576 |
| Intercepteur | military | 3 000 / 1 000 / 0 | Dock 1 | 4 000 | 10 | 50 | 50 | 12 500 | 1 | 20 | 360 |
| Assaillant | military | 6 000 / 4 000 / 0 | Dock 3, Métallurgie avancée 2 | 10 000 | 25 | 150 | 100 | 10 000 | 1 | 75 | 1 080 |
| Corvette | military | 20 000 / 7 000 / 2 000 | Dock 5, Moteur magnétique 4, Manipulation ionique 2 | 27 000 | 50 | 400 | 800 | 15 000 | 1 | 300 | 5 760 |
| Cuirassé | military | 45 000 / 15 000 / 0 | Dock 7, Navigation transdimensionnelle 4 | 60 000 | 200 | 1 000 | 1 500 | 10 000 | 4 | 500 | 12 960 |
| Frappe-orbital | advanced | 50 000 / 25 000 / 15 000 | Dock 8, Moteur magnétique 6, Maîtrise du plasma 5 | 75 000 | 500 | 1 000 | 500 | 4 000 | 8 | 700 | 17 280 |
| Prédateur | advanced | 30 000 / 40 000 / 15 000 | Dock 8, Navigation transdimensionnelle 5, Systèmes photoniques 12, Manipulation ionique 5 | 70 000 | 400 | 700 | 750 | 10 000 | 5 | 250 | 15 840 |
| Annihilateur | advanced | 60 000 / 50 000 / 15 000 | Dock 9, Navigation transdimensionnelle 6, Métallurgie avancée 6 | 110 000 | 500 | 2 000 | 2 000 | 5 000 | 8 | 1 000 | 23 040 |
| Colossus stellaire | advanced | 5 000 000 / 4 000 000 / 1 000 000 | Dock 12, Navigation transdimensionnelle 7, Pliage spatial 6, Manipulation gravitationnelle 1 | 9 000 000 | 50 000 | 200 000 | 1 000 000 | 100 | 5 | 1 | 2 592 000 |

- Tous tirent 1 fois par tour (`shotCount` = 1).
- Collecteur solaire : +35 énergie sur ma planète.
- Moteurs : Propulseur chimique pour Navette, Cargo, Récupérateur, Éclaireur, Intercepteur ; Moteur magnétique pour Assaillant, Corvette, Pionnier, Frappe-orbital ; Navigation transdimensionnelle pour Cuirassé, Prédateur, Annihilateur, Colossus.
- Les statistiques sont celles d'OGame. La nouveauté est le **facteur de distorsion**, absent d'OGame.

### Tirs rapides (`rapidFire`)

« Ce vaisseau cible ces unités en priorité et enchaîne ses tirs sur elles. Le facteur est le nombre moyen de tirs sur chacune. »

| Tireur | Cibles (facteur) |
|---|---|
| Navette, Cargo, Pionnier, Récupérateur, Intercepteur, Cuirassé | Éclaireur 5, Collecteur 5 |
| Assaillant | Éclaireur 5, Collecteur 5, Navette 3 |
| Corvette | Projecteur balistique 10, Intercepteur 6, Éclaireur 5, Collecteur 5 |
| Frappe-orbital | Projecteur 20, Canon photonique 20, Émetteur 10, Batterie ionique 10, Accélérateur 5, Éjecteur à plasma 5, Éclaireur 5, Collecteur 5 |
| Prédateur | Cuirassé 7, Corvette 4, Assaillant 4, Navette 3, Cargo 3, Éclaireur 5, Collecteur 5 |
| Annihilateur | Canon photonique 10, Prédateur 2, Éclaireur 5, Collecteur 5 |
| Colossus stellaire | Éclaireur 1 250, Collecteur 1 250, Pionnier 250, Cargo 250, Récupérateur 250, Navette 250, Projecteur 200, Intercepteur 200, Canon photonique 200, Assaillant 100, Émetteur 100, Batterie ionique 100, Accélérateur 50, Corvette 33, Cuirassé 30, Frappe-orbital 25, Prédateur 15, Annihilateur 5 |
| Éclaireur, Collecteur solaire, toutes les défenses | aucun |

---

## 7. Défenses (`/defenses?page=1&itemsPerPage=50`)

| Défense | Type | Coût | Prérequis | Structure | Bouclier | Attaque | Unique | Cases de silo | Durée (s) |
|---|---|---|---|---|---|---|---|---|---|
| Projecteur balistique | standard | 2 000 / 0 / 0 | Dock 1 | 2 000 | 20 | 80 | non | | 576 |
| Canon photonique | standard | 1 500 / 500 / 0 | Dock 2, Systèmes photoniques 3 | 2 000 | 25 | 100 | non | | 576 |
| Émetteur à haute énergie | standard | 6 000 / 2 000 / 0 | Dock 4, Systèmes photoniques 6, Science énergétique 3 | 8 000 | 100 | 250 | non | | 2 304 |
| Batterie ionique | standard | 2 000 / 6 000 / 0 | Dock 4, Manipulation ionique 4 | 8 000 | 500 | 150 | non | | 2 304 |
| Accélérateur magnétique | standard | 20 000 / 15 000 / 2 000 | Dock 6, Systèmes offensifs 3, Champs de protection 1, Science énergétique 6 | 35 000 | 200 | 1 100 | non | | 10 080 |
| Éjecteur à plasma | advanced | 50 000 / 50 000 / 30 000 | Dock 8, Maîtrise du plasma 7 | 100 000 | 300 | 3 000 | non | | 20 160 |
| Barrière défensive | advanced | 10 000 / 10 000 / 0 | Dock 1, Champs de protection 2 | 20 000 | 2 000 | 1 | **oui** | | 5 760 |
| Dôme protecteur | advanced | 50 000 / 50 000 / 0 | Dock 6, Champs de protection 6 | 100 000 | 10 000 | 1 | **oui** | | 28 800 |
| Intercepteurs (missile) | advanced | 8 000 / 2 000 / 0 | Dock 1, Arsenal balistique 2 | 8 000 | 1 | 1 | non | 1 | 2 304 |
| Ogives longue portée (missile) | advanced | 12 500 / 2 500 / 10 000 | Dock 1, Arsenal balistique 4, Moteur magnétique 1 | 15 000 | 1 | 12 000 | non | 2 | 4 320 |

### Missiles (aide du jeu)

- Les munitions (missiles) ne tirent jamais pendant un combat et ne comptent pas dans la puissance défensive de la base.
- Une salve ne détruit que des défenses, jamais les bâtiments, la flotte en orbite ou les ressources. **Les défenses détruites par missile sont perdues définitivement** (pas de reconstruction à 70 %).
- Sans cible désignée, les ogives frappent d'abord la défense la plus robuste (bouclier + coque). Une cible désignée passe en premier, puis le reste par robustesse décroissante.
- Une salve compte comme une attaque dans le quota anti-bash, sur toutes les colonies du joueur ciblé, et elle ne peut pas être rappelée. La protection des débutants s'applique.
- Les ogives ne reviennent jamais, même si la planète cible est abandonnée entre-temps.

---

## 8. Règles tirées de l'aide et des textes du jeu

### Énergie et ressources
- L'énergie n'est jamais stockée. Si la consommation dépasse la production, l'extraction de métal, cristal et hydrogène baisse **dans la même proportion**. Une ligne « Déficit énergétique » apparaît dans le détail de production.
- Réduire le taux de fonctionnement d'une mine baisse sa production et sa consommation dans la même proportion.
- Stockage dépassé : la production de la ressource s'arrête jusqu'à ce que le surplus soit dépensé. Le surplus reste utilisable.

### Combat, pillage, débris
- Le pillage est plafonné par la capacité de fret de la flotte envoyée.
- « Piller le même joueur rapporte moins à chaque fois. » Exact de fait : l'attaquant prend 50 % du stock à chaque attaque, donc chaque raid rapporte moins si le joueur ne produit pas entre-temps (`text-01`). Le taux, lui, ne baisse pas.
- La Station de réparation récupère une part des vaisseaux détruits (voir §4).
- Rapport de combat en vue partielle : seules les unités ennemies engagées sont listées.
- Formation de lune : chance selon le champ de débris (max 20 %), le champ n'est pas consommé.

### Lunes
- Une lune naît des débris d'un combat. Elle appartient au propriétaire de la planète et se développe indépendamment.
- Une lune commence avec 1 case. Chaque niveau de Base lunaire ouvre 3 cases et en occupe 1 (2 nettes), dans la limite fixée par le diamètre.
- Phalange de capteur : révèle les flottes en vol autour d'une planète, composition comprise. Portée qui croît avec le carré du niveau, jamais hors de la galaxie. Chaque scan coûte de l'hydrogène, même sans résultat. Les cargaisons restent invisibles. Les lunes ne peuvent pas être scannées. Le joueur scanné n'est jamais prévenu.
- Porte de saut : transfert instantané et sans carburant entre deux lunes équipées, sans ressources. Recharge sur les deux portes, réduite par les niveaux jusqu'à 10 minutes minimum.
- Destruction de lune avec des Colossus : deux tirages indépendants (lune détruite, flotte perdue). Envoyer plus de Colossus n'améliore que la chance de détruire la lune.

### Flottes
- Le nombre d'emplacements de flotte dépend de Calcul Quantique.
- La vitesse est réglable : plus vite = plus court, mais plus d'hydrogène consommé.
- Le trajet planète ↔ lune existe et prend un court temps de vol.

### Colonies
- Abandon d'une colonie : définitif, rien n'est remboursé, ressources et bâtiments restent (qui se dégradent), une partie de la flotte et des défenses est détruite, la lune part avec la planète, l'emplacement de colonie est rendu immédiatement. La planète mère ne peut pas être abandonnée. Bloqué si une construction, recherche, flotte ou frappe de missile est en cours.
- D'autres joueurs peuvent espionner, piller ou recoloniser une planète abandonnée (règles d'abandon au §2).

### Mode vacances
- Met l'empire en pause : aucune production sur aucune planète, personne ne peut vous atteindre. **Séjour minimum de 48 h.**
- Impossible si une flotte est en vol, une construction ou une recherche en cours, ou une attaque en approche.

### Protection des débutants
- Texte du jeu : « En dessous du plafond d'une tranche, personne ne peut attaquer un joueur autant de fois plus fort **ou plus faible** ; la tranche est celle du plus faible. » Confirmé par l'équipe (players-03) : c'est ce texte qui fait foi.

### Alliances
- Rejoindre ou quitter : 24 h d'attente avant de rejoindre une autre alliance. Nouveau membre : 24 h de « quarantaine » sans les avantages.
- Pactes : non-agression (−10 points de fair-play si violé), alliance (−15). Dénonciation publique avec 24 h de préavis. +1 point de fair-play par jour de pacte tenu. Les pactes ne changent rien au combat.
- Guerres : déclarées par vote des officiers et plus, à la majorité des voix exprimées ; égalité = rejet.
- Station d'alliance, talents (payés en points de doctrine et ressources), trésorerie commune, demandes d'aide plafonnées par jour.
- Missions d'alliance par cycle : combats, pillage, espionnage, recyclage, dons, bâtiments, recherches, vaisseaux, défenses. Paliers Bronze, Argent, Or selon la contribution ; récompenses en packs de ressources et parfois en Points stellaires.
- Partage de rapports et de positions dans le canal d'alliance (conservés 30 jours).
- Capacité d'alliance augmentée par Diplomatie Stellaire.

### Premium et boutique
- Premium : files de 5 ordres au lieu de 2, 200 favoris au lieu de 10, vue Empire, un lot cosmétique chaque mois.
- **Univers PvP : la boutique ne vend que du cosmétique** (avatars, cadres, couleurs de pseudo, emblèmes). Aucune ressource, aucun bonus de production, aucune accélération.
- Points stellaires : gagnés par missions quotidiennes, batailles gagnées, événements, ou achetés.
- Parrainage : Points stellaires quand un filleul atteint un seuil de points.

### Maintenance
- Pendant une maintenance, l'espionnage, les attaques et les frappes de missiles sont suspendus. Le reste du jeu continue normalement.

---

## 9. Quêtes (didacticiel, `/universes/{id}/quests`)

7 paliers (« grades »), pas d'autre palier prévu. Chaque quête rapporte des ressources et de l'expérience. L'expérience servira à la progression du personnage, fonctionnalité à venir (`start-02`). Chaque palier terminé donne un bonus d'expérience (29, 60, 121, 240, 479, 960, 1 922). Aucun Point stellaire sur Redline. Le palier suivant se débloque quand le précédent est terminé.

| Palier | Objectifs |
|---|---|
| 1 | Excavateur 1, Extracteur 1, Capteurs 1, Excavateur 3, Extracteur 2, Capteurs 3, Dépôt d'alliages 1, Centre d'innovation 1, Condensateur 1 |
| 2 | Excavateur 5, Extracteur 4, Capteurs 5, Condensateur 3, Science énergétique 1, Calcul quantique 1, Fabrique d'automates 2, Dock orbital 1 et 2, Propulseur chimique 2, 1 Navette de fret, 1 Projecteur balistique |
| 3 | Excavateur 8, Extracteur 7, Capteurs 8, Condensateur 8, Chambre cristalline 1, Dock 3, Propulseur chimique 3, Centre d'innovation 3, Renseignement tactique 2, 1 Éclaireur, Science énergétique 2, Systèmes photoniques 3, 1 Canon photonique, 1 Intercepteur |
| 4 | Excavateur 11, Extracteur 10, Capteurs 11, Condensateur 11, Citerne 1, Dock 4, Propulseur chimique 5 et 6, 1 Cargo stellaire, Métallurgie avancée 2, 1 Assaillant, Centre d'innovation 4, Science énergétique 4, Systèmes photoniques 5, Manipulation ionique 4, 1 Batterie ionique |
| 5 | Excavateur 14, Extracteur 12, Condensateur 12 et 13, Réacteur thermonucléaire 1, Dépôt d'alliages 4, Moteur magnétique 2 et 3, 1 Pionnier spatial, coloniser une planète, Renseignement tactique 4, Cosmologie appliquée 1, Centre d'innovation 6, Champs de protection 2, 1 Barrière défensive |
| 6 | Excavateur 15 et 16, Extracteur 13 et 14, Condensateur 14 et 15, Réacteur 3, Chambre cristalline 4, 1 Récupérateur, 1 recyclage, Systèmes photoniques 6, 1 Émetteur à haute énergie, Dock 5, Moteur magnétique 4, 1 Corvette, Station de réparation 1 |
| 7 | Excavateur 17 et 18, Extracteur 15 et 16, Condensateur 16 et 17, Réacteur 5, Citerne 4, Dock 6, Systèmes offensifs 3, Science énergétique 5 et 6, 1 Accélérateur magnétique, Champs de protection 5 et 6, 1 Dôme protecteur, Arsenal balistique 1, Calcul quantique 2, Centre logistique 1, 5 recyclages |

---

## 10. Note de version (reçue le 2 octobre 2026)

### Favoris
- Une étoile marque n'importe quelle planète ou lune de la galaxie, avec une note privée facultative.
- Page Favoris (menu, à côté des Rapports) : occupant actuel, note modifiable, raccourcis vers la galaxie, l'envoi de flotte et l'espionnage rapide.
- À l'envoi de flotte, la destination peut être choisie parmi les favoris (panneau latéral avec recherche).
- En vue orbitale, une étoile signale les corps en favoris.
- 10 favoris en gratuit, 200 en Premium (confirme le paramètre `bookmarks` de l'univers).

### Expéditions
- Au-delà de la dernière orbite de chaque système s'étend l'**espace lointain** (la position `deep_space`, N+1).
- Résultats possibles : métal, cristal ou hydrogène ; vaisseaux abandonnés à récupérer ; retour retardé ou anticipé ; pirates ; aliens ; rares trous noirs qui détruisent toute la flotte.
- Taille des trouvailles : plus la flotte est grande, plus elle rapporte, dans une limite qui augmente avec le score du premier joueur de l'univers.
- Épuisement : une zone trop visitée finit par s'épuiser. Un Éclaireur à bord indique l'état de la zone.

Détails tirés de l'aide du jeu et des réponses de l'équipe (`patch-03`) :
- Il faut **Cosmologie Appliquée** pour lancer une expédition.
- Durée sur place choisie par le joueur : de 1 h jusqu'à autant d'heures que le niveau de Cosmologie Appliquée (niveau 5 : jusqu'à 5 h).
- Expéditions simultanées : 1 dès le niveau 1, 2 au niveau 4, 3 au niveau 9, 4 au niveau 16. Chacune occupe aussi un emplacement de flotte.
- Une flotte composée uniquement de sondes est refusée : il faut au moins une autre coque.
- L'hydrogène couvre l'aller, le retour et chaque heure passée sur place.
- L'Éclaireur embarqué n'est pas perdu.

### Protection des nouveaux arrivants
- Chaque joueur est protégé des attaques pendant **7 jours après sa première arrivée** dans un univers.
- Le temps restant s'affiche en haut de l'écran. Les planètes protégées portent un badge « Nouveau joueur ».
- Lancer une attaque ou une salve de missiles met fin à la protection, définitivement. Un avertissement s'affiche avant de confirmer.
- Espionnage, transport et autres missions ne la retirent pas.
- Elle s'ajoute à la protection des débutants par paliers de points. La durée de 7 jours est un **paramètre d'univers** (`patch-01`).

### Premium contre Points stellaires
- Un mois de Premium s'échange contre **350 Points stellaires**, depuis la page Premium.
- Sans reconduction : à la fin du mois, le compte redevient standard.

### Améliorations
- File de construction : les ordres en attente affichent leur durée estimée (recalculée au lancement). Lignes plus lisibles, niveau affiché sur mobile.
- Galaxie au clavier : ← / → pour changer de système ; Ctrl + ← / → (⌘ sur Mac) pour changer de galaxie.

---

## 11. Règles détaillées (réponses de l'équipe, 2 octobre 2026)

Source : réponses de l'équipe de développement. Elles priment sur les textes d'aide du jeu quand les deux divergent (liste des textes à corriger au §11.9).

### 11.1 Effets des recherches (`research-01`, `research-02`)

| Recherche | Effet |
|---|---|
| Science Énergétique | Un seul effet : la production du Réacteur thermonucléaire = base × N × (1,05 + 0,01 × Science Énergétique)^N, avec N le niveau du réacteur. Aucun effet sur les Capteurs ni les Collecteurs. Sert surtout de prérequis. |
| Calcul Quantique | Emplacements de flotte = 1 + niveau. Une expédition occupe aussi un emplacement. |
| Renseignement Tactique | Profondeur des rapports d'espionnage (§11.5) ; contre-espionnage (§11.5) ; −5 % par niveau sur l'hydrogène d'une mission d'espionnage, plancher 50 % ; au niveau 10, une case espionnée passe en « découverte » durable. |
| Cosmologie Appliquée | Bases possibles = 1 + partie entière((niveau + 1) / 2) : 1 au niveau 0, 2 au niveau 1, 3 au niveau 3, 4 au niveau 5, 5 au niveau 7. Expéditions simultanées = partie entière(√niveau). Niveau 1 requis pour les expéditions. Maintien maximal = niveau, en heures. |
| Pliage Spatial | +5 % de capacité de soute par niveau (transport, pillage, recyclage, trouvailles d'expédition). Aucun effet en combat ni sur la vitesse. Niveau 7 requis pour la Porte de saut. |
| Collaboration Stellaire | Au niveau N, met en réseau les N meilleurs Centres d'innovation des autres bases, si leur niveau est au moins égal à celui de la base qui recherche. Niveau effectif = Centre local + somme des Centres en réseau. Aucun effet sur le coût. |
| Diplomatie Stellaire | Capacité de l'alliance du fondateur (§11.7). |
| Systèmes Offensifs, Champs de Protection, Métallurgie Avancée | +10 % par niveau sur l'attaque, le bouclier, la structure (§11.4). |

Durée d'une recherche (h) = (métal + cristal) / (1 000 × (1 + niveau effectif)) / vitesse recherche de l'univers.

### 11.2 Déplacements (`fleet-02`, `fleet-03`, `universe-03`)

**Distance d**
| Cas | Distance |
|---|---|
| Autre galaxie | 20 000 × écart de galaxies |
| Même galaxie, autre système | 2 700 + 95 × écart de systèmes |
| Même système | 1 000 + 5 × écart de positions |
| Planète et sa lune | 5 |

- L'espace lointain est la position N+1 du système et suit la formule normale.
- **La carte n'est pas circulaire** : la galaxie 9 n'est pas voisine de la 1.

**Vitesse**
- Vitesse d'un vaisseau = vitesse de base × (1 + bonus × niveau de la recherche de son moteur) : +10 % par niveau de Propulseur Chimique, +20 % Moteur Magnétique, +30 % Navigation Transdimensionnelle.
- **Le moteur d'un vaisseau est fixe** : pas de changement de moteur à un certain niveau comme dans OGame.
- La flotte va à la vitesse de son vaisseau le plus lent, × bonus du talent Propulsion coordonnée.
- **Le facteur de distorsion (`warpFactor`) n'a aucun effet** : statistique réservée, lue par aucun calcul.

**Durée** (secondes) = (10 + 35 000 / S × √(10 × d / V)) / vitesse Flottes de l'univers, arrondie, minimum 1. V = vitesse de la flotte ; S = facteur de vitesse de 1 à 10 par pas de 1 (1 = 10 %, 10 = 100 %), précisé le 2026-10-06 (la constante est passée de 3 500 à 35 000).

**Consommation** par trajet = somme, pour chaque type de vaisseau, de conso × quantité × d / 35 000 × (S / 10 × √(V flotte / V vaisseau) + 1)², arrondie à l'inférieur, minimum 1.
- Flotte homogène : formule OGame (vitesse% / 10 + 1)² à un facteur près. Les vaisseaux plus rapides que la flotte paient moins.
- **Le retour est payé au départ** (×2) pour toutes les missions sauf Colonisation et Stationnement.
- Un rappel ne redébite ni ne rembourse rien. Rappel possible à tout moment avant la fin du trajet aller.
- Talent Ravitaillement optimisé : −5 % par niveau. Aucune recherche ne réduit la consommation de base.
- Maintien d'expédition : hydrogène = plafond(heures × somme des consommations / 10), payé au départ, à faire tenir dans la soute avec la cargaison.

### 11.3 Expéditions (`fleet-06`)

Conditions : expéditions activées dans l'univers ; Cosmologie Appliquée ≥ 1 ; cible = espace lointain (position N+1) ; flotte pas uniquement composée d'Éclaireurs ; maintien de 1 h à niveau de Cosmologie heures ; un emplacement de flotte et un emplacement d'expédition libres.

| Résultat | Probabilité |
|---|---|
| Ressources | 33 % |
| Rien | 33 % |
| Vaisseaux | 17 % |
| Retard | 7 % |
| Pirates | 5,5 % |
| Aliens | 2,3 % |
| Retour anticipé | 2 % |
| Trou noir | 0,2 % |

- Pas de matière noire, de Points stellaires ni de marchand.
- **La durée de maintien ne change pas les probabilités** (le texte du jeu qui dit le contraire est faux).
- Épuisement d'une case : à partir de 10 expéditions terminées dessus en 24 h, chances de trouvaille × 0,75 ; à partir de 25, × 0,5 ; le reste va à « rien ».
- Taille : normale 89 % (facteur 10 à 50), grande 10 % (50 à 100), énorme 1 % (100 à 200).
- Points d'expédition = max(200, structure totale de la flotte / 200), plafonnés selon les points du meilleur joueur humain de l'univers :

| Meilleur joueur | Plafond |
|---|---|
| < 10 000 | 200 |
| < 100 000 | 2 500 |
| < 1 M | 6 000 |
| < 5 M | 9 000 |
| < 25 M | 12 000 |
| < 50 M | 15 000 |
| < 75 M | 18 000 |
| < 100 M | 21 000 |
| ≥ 100 M | 25 000 |

- Ressources : gain = facteur × points, en équivalent métal. Métal dans 50 % des cas, cristal 33 % (montant / 2), hydrogène 17 % (montant / 3). Limité à la soute libre, le surplus est perdu.
- Vaisseaux : budget = facteur × points / 2, dépensé en vaisseaux jusqu'à un rang au-dessus du meilleur vaisseau à bord. Jamais de Colossus, Pionnier, Récupérateur ni Collecteur.
- Retard : retour allongé de (maintien × 2, 3 ou 5) selon la taille. Retour anticipé : retour divisé par 2, 3 ou 5.
- Pirates et aliens : vrai combat contre une flotte proportionnelle à la vôtre (pirates 30 / 50 / 80 %, aliens 40 / 60 / 90 %, plus une escorte fixe), avec vos technologies −3 (pirates) ou +3 (aliens). Débris à 10 % sur la case. Pas de pillage.
- Trou noir : flotte perdue.

### 11.4 Combat (`combat-01` à `combat-09`, `defense-01`, `defense-02`)

**Moteur**
- 6 rounds au plus, arrêt dès qu'un camp est vide.
- Chaque round : boucliers rechargés, effectifs figés, l'attaquant tire puis le défenseur. Une unité vivante en début de round tire toutes ses salves même si elle meurt pendant le round (tir simultané en pratique).
- Cible tirée uniformément parmi les unités adverses vivantes. Tout tir touche.
- Tir rapide : après chaque tir, si le facteur f du couple tireur / cible dépasse 1, le tireur retire avec une probabilité 1 − 1/f sur une nouvelle cible aléatoire, tant que le tirage réussit. Identique à OGame.
- Explosion : après un tir qui entame la coque sans la détruire, si la coque passe sous 70 %, l'unité explose avec une probabilité de 1 − fraction de coque restante. Un tir rebondi n'ouvre pas ce tirage.
- **Statistiques de combat** : coque = structure × (1 + 0,1 × Métallurgie Avancée) / 10 ; bouclier × (1 + 0,1 × Champs de Protection) ; arme × (1 + 0,1 × Systèmes Offensifs). Les Doctrines d'alliance ajoutent 5 %.
- Résultat : victoire de l'attaquant si le défenseur est vide ; victoire du défenseur si l'attaquant est vide ; sinon égalité (deux camps debout après 6 rounds, ou deux camps vides).
- Les tirages sont déterministes par combat : un même combat rejoué donne le même résultat.

**Boucliers**
- Règle du 1 % : un tir inférieur à 1 % du bouclier maximal de la cible rebondit sans effet.
- Sinon le bouclier absorbe tant qu'il en reste ; l'excédent passe entièrement sur la coque.
- Régénération complète au début de chaque round, jamais en cours de round.
- Barrière défensive et Dôme protecteur : cibles ordinaires avec un gros bouclier individuel, **pas de bouclier global**. Un seul exemplaire de chaque (impossible d'en commander ou d'en mettre en file un deuxième).

**Pillage** (`combat-04`, `combat-05`)
- Butin = 50 % de chaque ressource de la cible (arrondi inférieur), énergie exclue, **uniquement en cas de victoire**. Paramètre d'univers.
- Si le total dépasse la soute libre des survivants, chaque ressource est réduite dans la même proportion. Pas d'ordre de priorité. La soute tient compte du Pliage Spatial et de ce qui est déjà à bord.
- **Pas de pillage dégressif** : 50 % à chaque attaque.

**Débris** (`combat-06`)
- Les débris ne disparaissent jamais ; seul le recyclage les retire. Ils survivent à la disparition d'une base abandonnée et ne sont pas consommés par la formation d'une lune.
- Taux par défaut : 30 % des vaisseaux détruits des deux camps (civils compris), 0 % des défenses, paramètre d'univers. 10 % fixe pour les combats d'expédition. Métal et cristal uniquement.
- La destruction de lune ne laisse aucun débris.

**Reconstruction des défenses** (`combat-09`)
- Tirage indépendant à 70 % **par unité détruite**. 10 détruites : entre 0 et 10 reviennent, 7 en moyenne. 2 détruites : 0, 1 ou 2.
- Barrière et Dôme : 70 % de chance de les garder, 30 % de les perdre définitivement.
- Défenses détruites par missile : perdues définitivement.
- Les vaisseaux ne sont jamais réparés gratuitement ; seule la Station de réparation en récupère une part, sans tirage.

**Destruction de lune** (`combat-08`)
- Mission dédiée, flotte uniquement composée de Colossus stellaires, cible une lune d'un autre joueur.
- Un combat classique a lieu d'abord ; les tirages n'ont lieu que sur victoire nette.
- S = diamètre en km, N = Colossus survivants : chance de détruire la lune = min(100, (100 − √S) × √N) % ; chance de perdre les Colossus = √S / 2 %, un seul tirage pour toute la flotte, que la lune saute ou non.
- Exemple : 8 944 km et 100 Colossus donnent 54,3 % et 47,3 %.
- Si la lune saute, tout ce qu'elle portait disparaît et les points sont retirés ; les flottes en route vers ou depuis la lune sont redirigées vers la planète. Pas de pillage ni de débris.

**Arsenal balistique** (`defense-02`)
- 10 cases par niveau. Intercepteurs : 1 case ; Ogives longue portée : 2 cases. Les missiles en file ou en construction comptent.
- Les missiles n'occupent pas de cases de la planète. Niveau 2 requis pour les Intercepteurs, 4 pour les Ogives.
- Démolir le silo sous son contenu ne détruit rien.

### 11.5 Espionnage (`spy-01`, `spy-02`, `spy-04`)

**Détail du rapport**
- Niveau effectif = max(0, (Renseignement de l'espion − Renseignement de la cible) + min(5, partie entière(Éclaireurs / 2))). Les talents Réseau d'informateurs et Contre-espionnage fédéré s'ajoutent aux niveaux respectifs.
- Paliers : ressources dès 1, flotte dès 3, défenses et missiles dès 5, bâtiments dès 7, recherches dès 9.
- Type, taille et températures sont toujours visibles.
- Différence avec OGame : pas d'écart au carré, bonus de sondes plafonné à +5. Avec 10 sondes, il faut 2 niveaux d'avance pour voir les bâtiments, 4 pour les recherches.

**Destruction des Éclaireurs**
- Chance % = (2 × Renseignement du défenseur − Renseignement de l'espion) × nombre de vaisseaux stationnés × 0,05, bornée entre 5 % et 25 %.
- 0 % si l'espion a au moins le double du niveau du défenseur, s'il n'y a aucun vaisseau en orbite (les défenses ne comptent pas), ou si la cible est inhabitée, abandonnée ou en vacances.
- Le nombre de sondes ne change pas le risque. Un seul tirage pour toute la vague : toutes détruites ou aucune. Pas de combat.
- Si les sondes tombent, un second tirage décide si l'espion est tracé (pseudo et coordonnées) ou seulement identifié (pseudo).
- Le défenseur reçoit toujours une alerte d'intrusion.

**Phalange de capteur**
- Portée = niveau² − 1 systèmes de part et d'autre, minimum 1, même galaxie : 1, 3, 8, 15, 24, 35, 48, 63, 80.
- 5 000 hydrogène par scan. Uniquement sur une lune ; ne peut pas cibler une lune.
- Montre toutes les flottes ayant la planète pour origine ou destination, aller et retour : composition, mission, heure d'arrivée. Cargaison masquée.

### 11.6 Porte de saut (`fleet-07`)

| Niveau | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14+ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Recharge (min) | 60 | 53 | 47 | 41 | 36 | 31 | 27 | 23 | 19 | 17 | 14 | 13 | 11 | 10 |

- La recharge frappe les deux lunes, départ et arrivée.
- Coût : 2 M métal, 4 M cristal, 2 M hydrogène, doublé à chaque niveau. Lune uniquement. Prérequis : Base lunaire 1, Pliage Spatial 7.
- Saut instantané, sans carburant, entre deux lunes du même joueur, coques seulement.

### 11.7 Joueurs (`players-04` à `players-09`)

**Limite d'attaques** (`combat-05`)
- 6 attaques (flottes et salves de missiles confondues) par **tranche de 24 h fixe** sur un même joueur : la fenêtre s'ouvre à la première attaque et se remet à zéro 24 h plus tard. (Le brief disait « 24 h glissantes » : corrigé.)
- La 7e attaque est refusée à l'envoi. Un rappel avant impact rend le créneau.
- Paramètre d'univers ; 0 désactive la règle. Les planètes abandonnées ne sont pas concernées.
- Les espionnages ne comptent pas. Les guerres et pactes d'alliance ne modifient ni le combat, ni le pillage, ni la limite.

**Mode vacances**
- 48 h minimum, aucune durée maximale, aucune fin automatique, aucun délai entre deux périodes. Par univers.
- Conditions d'entrée : aucune flotte en vol, aucune construction, recherche ou unité en cours, aucune attaque en approche.
- Effets : production à zéro ; toutes les actions du joueur refusées (flottes, missiles, constructions, démolitions, Phalange).
- Les autres joueurs ne peuvent ni l'attaquer, ni détruire sa lune, ni lui transporter des ressources, ni lui tirer des missiles. Espionnage et recyclage restent possibles, mais le rapport d'espionnage est vide.
- L'inactivité ne s'accumule pas pendant les vacances.

**Inactivité**
- Un seul palier, paramètre d'univers : **14 jours** par défaut, **7 jours** sur Redline (`players-10`, confirmé le 2026-10-06 : 7 jours constatés, conforme à `inactivityDays: 7`).
- Effet : perte de la protection des débutants, attaquable par tous quel que soit l'écart de points.
- Pas de suppression de compte, pas d'abandon automatique des planètes. Indicateur d'inactivité dans la galaxie : **ne pas en parler** dans le wiki tant qu'il n'est pas affiché.
- Alliance : un fondateur silencieux est alerté à 7 et 12 jours et perd son siège à 14.

**Alliances**
- Capacité selon la Diplomatie Stellaire **du fondateur** : 10, 15, 20, 25, 30, 35, 40, 50 membres aux niveaux 1 à 8. Niveau 1 requis pour fonder (donc Centre logistique 3). Une capacité acquise ne redescend jamais. Talent Ambassades : +2 sièges par niveau sur 3 niveaux, soit 56 au maximum.
- Guerre : déclarée par vote, mutuelle quand les deux camps déclarent, terminée par une paix acceptée. Elle compte les victoires et marque les cases ennemies sur la carte, sans effet sur les règles de combat.

**Talents d'alliance** (14 talents, 5 branches)
- Coût par niveau : 1 point de doctrine et 300 000 métal, 150 000 cristal, 50 000 hydrogène, doublés à chaque niveau. Exception, les deux Doctrines : un seul niveau, 2 points, 3 M métal, 1,5 M cristal, 0,5 M hydrogène.
- Les bonus de membre s'activent après 24 h d'ancienneté.

| Talent | Branche | Niveaux | Effet par niveau |
|---|---|---|---|
| Soutes mutualisées | Logistique | 3 | Plafond du fonds commun ×2 (5 M → 40 M par ressource) |
| Réseau d'assistance | Logistique | 3 | +50 000 d'aide reçue par membre et par jour |
| Propulsion coordonnée | Logistique | 4 | +5 % de vitesse de flotte |
| Ravitaillement optimisé | Logistique | 4 | −5 % d'hydrogène consommé |
| Extraction coordonnée | Économie | 4 | +5 % de production métal, cristal, hydrogène |
| Entrepôts fédérés | Économie | 2 | +10 % de capacité des entrepôts |
| Bâtisseurs associés | Économie | 2 | +10 % de vitesse de construction |
| Laboratoires en réseau | Science | 4 | +5 % de vitesse de recherche |
| Doctrine d'armement | Science | 1 | +5 % de puissance de feu (vaisseaux et défenses) |
| Doctrine de protection | Science | 1 | +5 % de boucliers et de coques |
| Réseau d'informateurs | Renseignement | 3 | +1 niveau d'espionnage pour vos sondes |
| Contre-espionnage fédéré | Renseignement | 3 | +1 niveau d'espionnage en défense |
| Ambassades | Diplomatie | 3 | +2 sièges |
| Parole tenue | Diplomatie | 3 | +1 point de fair-play par jour de pacte respecté |

- Points de doctrine : 2 par niveau d'alliance de 1 à 5, puis 1 par niveau ; plafond 50 points au niveau 45.
- Passer du niveau n au suivant : 10 000 + 2 500 × (n − 1) points d'expérience.
- Expérience d'alliance : constructions (20 × niveau), recherches (40 × niveau), raids gagnés (5 pour 1 000 points militaires détruits), rapports d'espionnage (10), recyclage (2 pour 1 000), missions d'alliance. Plafond glissant sur 7 jours : 800 par membre, 15 000 par alliance.
- Branche Logistique offensive : fermée, réservée aux futures attaques groupées.

**Règlement** (`players-09`)
- **Aucun règlement publié.** Seule mention : « le multi-compte est interdit par les conditions d'utilisation » (écran de parrainage). Le lien « conditions d'utilisation » de l'écran de connexion mène à une page inexistante.
- Sitting et push : ni mentionnés ni détectés. Aucun mécanisme de bannissement, de suspension ou de détection d'IP partagée.
- Sanctions techniques existantes : filtres du chat (sans mute), récompense de parrainage versée seulement quand le filleul atteint 100 points.

### 11.8 Divers
- Parrainage : récompense versée quand le filleul atteint **100 points** (`misc-03`, montant à confirmer).

### 11.9 Textes du jeu à corriger (à remonter à l'équipe)

| Où | Texte actuel | Problème |
|---|---|---|
| Expéditions | « Plus la flotte reste, plus elle a de chances » | La durée ne change pas les probabilités (`fleet-06`) |
| Aide, Boutique et Points stellaires (PvP) | « aucun avantage de jeu » | Le Premium (files plus longues) s'obtient en Points stellaires (`patch-02`) |
| Nom du bâtiment `planetary_base` (FR) | « Base planetaire » | Accent manquant |
| Écran de connexion | Lien « conditions d'utilisation » | Page inexistante (`players-09`) |

---

## 14. Réponses du 2 octobre 2026 au soir

- `universe-10` : si un système n'a pas 15 positions, la position est d'abord ramenée sur une échelle de 15 pour garder les mêmes profils (taille, température, types).
- `universe-11` : le Pionnier spatial est consommé à la colonisation. La colonie démarre avec les ressources embarquées par le Pionnier et les vaisseaux qui l'accompagnent.
- `players-11` : les missiles tirés font baisser les points militaires du tireur.
- `misc-05` : une attaque qui arrive pendant une maintenance aboutit ; on ne peut simplement pas en lancer de nouvelles après la mise en maintenance.

## 15. Ajustements du 2 octobre 2026 (soir)

- **Bonus de position**, sur les mines des **colonies uniquement** (jamais la planète mère, pour ne pas créer d'inégalités) : cristal +40 / +30 / +20 % en positions 1, 2 et 3 ; métal +17 / +23 / +35 / +23 / +17 % en positions 6 à 10. Le bonus a sa propre ligne dans le détail de production.
- **Taille des galaxies variable** : le nombre de systèmes par galaxie dépend de l'univers (99 sur Redline ; 499 fixes dans OGame).

## 16. Précisions du 2 octobre 2026 (soir)

- **Positions masquées** : tant qu'une position n'a pas été espionnée, une police exotique affiche un texte illisible et masque même le nom de la planète (et du propriétaire).
- **Biome et aspect** : chaque planète a un biome et un aspect visuel accordé à son type.
- **Pas de pay to win** : parti pris fort face à OGame, à mettre en avant.
- **Skins de planète** et **univers privés** : à documenter (levée de la consigne `misc-04`).

## 13. Positionnement face à OGame (équipe, 2 octobre 2026)

Source unique pour la page P-06 « Vous venez d'OGame ? ».

### Absent de Dynasty Nova
- Attaques groupées et défense alliée (chantier à part, non planifié). Pas de stationnement chez un allié.
- Officiers : remplacés par un abonnement Premium unique.
- Matière noire : remplacée par les Points stellaires, sans avantage de jeu en PvP.
- Marchand, place de marché, échanges de ressources.
- Classes de joueur et d'alliance (planifiées).
- Formes de vie, objets et boosters, relocalisation de planète.
- Vaisseaux Éclaireur (le « pathfinder » d'OGame), Faucheur, Foreuse. Attention : dans Dynasty Nova, « Éclaireur » désigne la sonde d'espionnage.
- Changement de moteur selon la recherche.
- Carte circulaire.
- Suppression de compte pour inactivité, paliers d'inactivité multiples.
- Règlement et conditions d'utilisation (à rédiger).
- Dépôt de ravitaillement : le Centre logistique va le devenir (annoncé pour le 2 octobre au soir).

### Nouveau
- Espace profond (case après la dernière position, seule destination des expéditions et du recyclage). **Les systèmes comptent de 9 à 20 positions selon l'univers** (15 sur Redline).
- Base planétaire (Base coloniale sur une colonie) : indémolissable, porte le stockage de base et un petit revenu fixe.
- Cinq vitesses d'univers indépendantes.
- Univers réglables : protection débutant, anti-bash, débris (vaisseaux et défenses), chance et seuil de formation de lune, abandon, taille des files, favoris, ouverture programmée.
- Bots PvE (raider, opportuniste, mineur), signalés, plafond de 6 attaques de bots par humain et par jour. **Livrés mais pas activés en production : ne pas documenter.**
- Protection nouvel arrivant (7 jours, cumulée avec la protection par points).
- Premium : 4,99 € par mois, 13,99 € pour 3 mois, 25,99 € pour 6 mois, ou 350 Points stellaires pour un mois. Donne 5 ordres par file au lieu de 2, 200 favoris au lieu de 10, la vue Empire et un lot mensuel (deux avatars, un skin de planète, 30 Points stellaires).
- Points stellaires : 25 pour 0,49 €, 200 pour 3,99 €, 500 pour 9,99 € ; parrainage : 30 quand le filleul atteint 100 points ; missions d'alliance. Usages : cosmétiques, renommage d'une base (gratuit la première fois, puis 20), Premium. Accélérations et packs de ressources réservés au mode PvE, pas encore ouvert.
- Quêtes : 102 quêtes en 7 grades débloqués en bloc, XP par univers, packs de ressources à consommer sur la base de son choix.
- Alliances enrichies (niveau, expérience, 14 talents, trésorerie, projets, missions, pactes, guerres votées, succession automatique, canal de chat).
- Chat à trois canaux (général, alliance, privé), anti-flood, liste noire, blocage ; notifications ; news ; favoris annotés.
- Abandon volontaire de planète avec dégradation sur 60 jours ; recolonisable par tous sauf l'ancien propriétaire pendant 30 jours.
- Maintenance = trêve sur tous les univers.
- Combats rejouables (graine déterministe).

### Fonctionne autrement
- Pillage : 50 % de chaque ressource, chargement proportionnel à la soute, pas de règle des tiers.
- Anti-bash : 6 attaques par 24 h, missiles compris, fenêtre fixe, 7e refusée à l'envoi, rappel = créneau rendu.
- Débris : jamais expirés ; défenses 0 %, vaisseaux 30 %, expéditions 10 %.
- Annulation : 80 % au prorata du temps restant (100 % dans OGame). Démolition gratuite, moitié du temps, ne rend rien.
- Files : quatre files (bâtiments, recherche, vaisseaux, défenses) de 2 ordres, 5 en Premium. Un ordre en file n'est payé qu'à son tour, abandonné sans frais si la base ne peut pas payer.
- Station de réparation : part complémentaire au taux de débris (45 % à 57 % de ce que les débris laissent), durée 30 min à 12 h, n'occupe aucune case.
- Protection débutant : paliers réglables, symétriques, levée après un délai d'inactivité réglable par univers (7 jours sur Redline).
- Espionnage : écart de Renseignement + bonus de sondes plafonné à +5, sans carré ; contre-espionnage en un tirage de 5 à 25 % pour toute la vague ; au niveau 10, case découverte durablement.
- Phalange : 5 000 hydrogène par scan (10 000 dans OGame), portée identique.
- Collecteur solaire : Tmax / 4 + base (OGame : (T + 140) / 6). Capteurs photovoltaïques : bonus de 1 + T actuelle / 100.
- Température vivante : oscille chaque mois entre min et max, pic à mi-mois.
- Expéditions : pas de matière noire ni de marchand, pirates et aliens joués par le moteur de combat, plafond fixé par le meilleur joueur humain, épuisement après 10 puis 25 expéditions en 24 h, durée sans effet sur les chances.
- Formation de lune : chance et seuil réglables (20 % pour 2 M par défaut). Une lune naît avec 1 case, la Base lunaire en creuse 3 par niveau.
- Mode vacances : 48 h minimum, pas de maximum ni de délai ; espionnage et recyclage possibles avec rapport vide.
- Traqueur (Prédateur) : exige en plus Manipulation Ionique 5.
- Prévu mais pas livré : attaques groupées, mode PvE ouvert, Points stellaires des quêtes, vie sociale des bots, esquive au combat (désactivée), cadeaux, thèmes d'interface.

---

## 12. Wiki.js

- Langues activées (namespaces) : **fr et en uniquement**. L'espagnol n'est pas activé.
- Compte `smashed1944`, groupe « Membre » : droits de création accordés le 2 octobre 2026. Arborescence créée (non publiée).

## 17. Actualités du jeu (`/news`, relevées le 6 octobre 2026)

Source : page Actualités du jeu (https://play.dynastynova.com/news), API `GET /news` (authentifiée), 14 annonces en FR, EN et ES (champs `title`, `body`, `startsAt`, `callToAction`). Seules les informations utiles au wiki sont reprises.

- **3.6.0 (4 oct.)** : boutique en rotation (vitrine du jour renouvelée à minuit, heure de Paris ; « À la une » hebdomadaire renouvelée le lundi ; Collection ; liste d'envies avec notification au retour, date jamais annoncée ; un cosmétique ne s'achète que pendant son passage en vitrine ; packs à prix réduit où l'on ne paie que ce qu'on n'a pas ; éditions limitées à une seule vitrine). Rapports à la carte (Paramètres : rapports reçus et annoncés par la cloche ; retours de flotte mission par mission ; espionnage, combats et incidents toujours reçus). Messagerie depuis la galaxie, la fiche d'une planète ou le classement. Écrans d'alliance repensés, score en cours de chaque guerre. Correction : centre logistique visible dans le détail du stockage ; skin conservé dans la vue 3D.
- **3.5.0 (3 oct.)** : annonce d'alliance épinglée (fondateur et vice-président, visible des membres). Trésorerie : vue « Par membre ». Centre logistique : +10 % de stockage par niveau. **Premium : une expédition simultanée de plus pour les abonnés** (`patch-04`). Tag d'alliance dans le classement. Fonder une alliance ne demande plus que Diplomatie Stellaire 1 (plus le centre logistique). Boutique triée par emplacement et rareté, aperçu 3D. Carte galaxie : un joueur trop fort n'est plus présenté comme « débutant protégé ». **Correction : les temps de vol étaient dix fois trop courts** (constante 3 500 passée à 35 000). Bouclier nouvel arrivant retiré à ceux qui avaient déjà attaqué. Adversaires contrôlés par le jeu améliorés.
- **Skins de planète (3 oct.)** : raretés Commun 50, Rare 75, Épique 100, Légendaire 125 Points stellaires ; aperçu 3D ; application depuis le panneau « Apparence » de n'importe quelle planète ; purement cosmétique. Légendaires cités : Dynastie, Spore, Les Terrasses, La ruche.
- **Premium en points (2 oct.)** : 350 Points stellaires = 1 mois, sans reconduction, lot du mois livré tout de suite, impossible si déjà Premium.
- **Bouclier nouvel arrivant (2 oct.)** : 7 jours, rétroactif à sa mise en place ; protège aussi des adversaires contrôlés par le jeu ; badge « Nouveau joueur » avec date de fin ; attaque ou salve de missiles = fin définitive (avertissement) ; espionner, transporter, coloniser, recycler, partir en expédition ne le brisent pas.
- **Expéditions (2 oct.)** et **3.1.0** : conformes à DONNEES §10 ; navigation clavier dans la galaxie (flèches, Ctrl ou Cmd + flèches) ; filtre de rapports « Expédition ».
- **1er oct. (Serveur 2.0.0 · Client 3.0.0)** : skins à anneaux ; espionnage des joueurs en vacances rétabli (case cartographiée pour soi et son alliance, rapport vide, sondes jamais abattues, aucune alerte).
- **30 sept.** : favoris (10, 200 en Premium), vue Empire, bonus de position (DONNEES §15), Synthétiseur d'hydrogène dépendant de la température (plus froid = plus de production, consommation d'énergie inchangée).
- **Univers privés (30 sept.)** : formules Escouade (25), Flotte (75), Armada (200) ; EN : Squad, Fleet, Armada ; à la semaine, au mois ou pour une durée fixe ; à partir de 4,99 € la semaine (`misc-06` en partie répondue).
- **Premium (30 sept.)** : files de 2 à 5 ordres, lot mensuel (2 avatars, 1 skin, 30 Points stellaires, jamais vendus en boutique, conservés après l'abonnement), formules 1, 3 ou 6 mois dès 4,33 € par mois.

## 18. Dynasties et talents (code du jeu, relevé le 6 octobre 2026)

Source : code du serveur (dépôt Backend, fusion « dynasties, classes and talents v2 », #469, puis #473 et #474) et textes du client (`talents.json`, `classes.json`, `dynasties.json`, FR et EN). Règles confirmées par l'équipe (déduites du code). **Pas encore en jeu au 6 octobre 2026** (dernière version serveur publiée : 2.7.0) : les pages de la rubrique `dynasty` restent non publiées jusqu'à la sortie.

### Dynasties et traits
- Une dynastie par univers, choisie une fois, jamais changée. Deux traits passifs, deux classes exclusives.
- **L'Héritage** : *Rien ne se perd* (remboursement d'annulation +5 points, 80 → 85 % ; reconstruction gratuite des défenses +5 points, 70 → 75 %), *La rotation Halden* (mines +2 %). Classes exclusives : Archiviste, Vétéran.
- **L'Accord** : *Le diapason* (+5 % de dégâts sur les unités contre lesquelles le vaisseau a un tir rapide), *Écouter loin* (flotte ennemie lue un palier plus tôt dans les rapports d'espionnage). Classes exclusives : Symbiote, Oracle.
- **Le Chœur** : non jouable (avatars seulement). Classes exclusives prévues : Essaim, Rémanence, sans arbre.
- Un trait déplace la valeur de départ, jamais le plafond. Il s'ajoute aux talents d'alliance.

### Classes
- 6 communes (Bâtisseur, Énergéticien, Théoricien, Amiral, Navigateur, Ombre), 4 exclusives.
- Changement de classe : dans la même dynastie, **50 Points stellaires**, **une fois tous les 7 jours** ; vide l'arbre de classe et remet sa réinitialisation à « gratuite » ; l'arbre commun ne bouge pas.
- Maîtrise de classe : de 0 au niveau 50. Une classe jouée depuis le début = niveau du joueur. Une classe prise ensuite part de sa maîtrise enregistrée et suit la courbe d'expérience du joueur, sans dépasser son niveau. Jamais jouée = 0 jusqu'à la première expérience, puis niveau 1. Chaque classe garde sa maîtrise.

### Expérience et niveaux
- Expérience = quêtes + **10 par point** du record de points, divisé par la vitesse de l'univers.
- Seuils d'expérience (début de niveau) : 1 : 0 · 8 : 500 · 10 : 1 221 · 20 : 43 939 · 24 : 100 397 · 25 : 121 716 · 32 : 437 052 · 40 : 1 773 675 · 50 : 10 000 000. Au-delà du niveau 50, chaque niveau coûte autant que le 50e et ne rapporte rien.

### Règles des arbres
- Arbre commun : 3 × 10, rangs par rangée 3, 5, 1, 5, 1, 1, 5, 1, 5, 1 (28 par branche), portes à 0/0/0/8/8/8/20/20/32/32 points placés au-dessus (toutes branches), 1 point par niveau, 50 au maximum.
- Arbre de classe : 3 × 9, rangs 1, 3, 1, 3, 1, 1, 3, 1, 1 (15 par branche), portes 0/0/0/5/5/5/12/12/12, ⌈maîtrise / 2⌉ points, 25 au maximum.
- Ultime : niveau 40 et branche pleine.
- Brouillon puis validation ; un point validé ne se reprend que par réinitialisation. Réinitialisation par arbre : la 1re gratuite, ensuite 20 Points stellaires et 24 h depuis la précédente.

### Plafonds (talents / total avec l'alliance)
- Vitesse de flotte : commun 40 %, accent 10 %, talents 50 %, total 60 %. Les bonus de vitesse divisent la durée. Vent arrière (25 %), Liaisons internes (40 %), Retour victorieux (30 %) hors budget.
- Hydrogène : commun 20 %, accent 5 %, talents 25 %, total 45 %. Soutes 25 %. Flottes en vol +3.
- Recherche 25 / 45 %. Mines 25 / 45 %. Bâtiments 25 / 45 %, accent 15 % sur une famille (50 % au total). Vaisseaux et défenses 10 %, accent 15 %. Coûts 5 % (accent). Cases +4. Pillage des cibles abandonnées +20 points. Protection contre le pillage 20 points au catalogue (15 pour le Vétéran, 10 pour l'Oracle), taux de pillage jamais sous 30 %.
- Combat : armement des vaisseaux 9 %, coque 11 %, bouclier 3 % ; défenses : armement 9 %, bouclier 5 %, coque 10 % ; dégâts sur tirs rapides 15 % (trait compris).

### Arbre commun
Valeurs par rang (code `CommonTalents`), identiques au document de conception : voir la page `dynasty/common-tree`. Astrométrie touche la catégorie « exploration » : Renseignement Tactique et Cosmologie Appliquée.

### Arbres de classe
Valeurs par rang tirées du catalogue de chaque classe (`AdmiralTalents`, `BuilderTalents`…) et des plafonds de classe (`ClassCaps`). Écarts avec le document de conception, retenus d'après le code : Lire la coque 3,5 %/rang, Feu concentré 7,5 %, Contre-batterie 2 %/rang, Premier rang 3 %/rang, coque de l'Amiral plafonnée à 11 %.

### Réponses et vérifications du 6 octobre 2026 (questions `dynasty-04` à `dynasty-20`)
- Vaisseaux de combat (Amiral) : les 8 vaisseaux non civils hors Collecteur solaire (Intercepteur, Assaillant, Corvette, Cuirassé, Frappe-orbital, Prédateur, Annihilateur, Colossus stellaire).
- Pluie d'acier : 24 h glissantes. Décollage d'urgence : fenêtre de retour comptée depuis le décollage.
- La nuit est courte : 49 % de la part qui ne part pas en débris (30 % de débris : 0,7 × 0,49 ≈ 34 % des Collecteurs détruits).
- Recherche « civile » (Prototype) : toute recherche qui n'augmente ni la puissance militaire ni la vitesse des vaisseaux.
- Terraformeur vivant : se cumule avec la case des niveaux pairs (Modulateur 6 : 33 → 39 cases).
- La lune tient et Briseur de lunes : en relatif, chance ou risque × 0,75 (code `MoonDestructionOdds`).
- Chantier de démontage : part de la Station de réparation × 1,2 (code `RepairDock`).
- Épaves fraîches : +20 points ajoutés après le plafond de 25 % de Ferrailleur et Tri des métaux (jusqu'à 45 %). Indemnité : payée ressource par ressource sur le coût des vaisseaux perdus.
- Formation serrée : seul le vaisseau le plus lent est accéléré, plafonné par le plus rapide ; la flotte vole à une seule vitesse.
- Prudence : comparée au risque après les bornes de 5 % et 25 %.
- Protection contre le pillage : le plafond de classe porte sur le total, arbre commun compris (Vétéran 15 points ; Oracle 10 points, d'après Backend #476). Baisse en points du taux de pillage, jamais sous 30 %.
- Écouter loin et Lecture des hangars se cumulent : 2 paliers plus tôt pour la flotte (décision de l'équipe, Backend #476). Retard comblé ne double que Fonds d'archives : 40 % au plus sur un niveau connu (Backend #476).
- Température actuelle d'une planète (code `Map::getTemperatureAt`) : suit le mois du calendrier, minimale le 1er, maximale au jour floor(jours du mois / 2) (le 15, le 14 en février), minimale le dernier jour, linéaire jour par jour, arrondie.
- Alerte d'attaque : 60 s avant l'impact (code `Fleet::ATTACK_ALERT_LEAD_TIME_IN_SECONDS`), jusqu'à 360 s avec les talents de l'Oracle.
