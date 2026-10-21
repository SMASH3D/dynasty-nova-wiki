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
| bank_deposit | Dépôt à la banque | Bank deposit | Depósito en el banco |
| alliance_deposit | Don à l'alliance | Alliance donation | Donación a la alianza |

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

## Univers (code, 15 octobre 2026)

Relevé dans `astro-nova-backend` (origin/main 7b255c83) et `Astro-Nova-React` (origin/main), catalogue lu dans un MySQL migré (migrations du même commit). Pages réécrites : `universe`, `universe/universes`, `universe/coordinates`, `universe/galaxy-view`, `universe/planets`, `universe/colonization`, `universe/abandoning-a-planet`, `universe/moons` (FR et EN). Générateurs : `tools/universe_pages/` (`univ_lib.py` porte toutes les constantes ; `python3 tools/universe_pages/p_all.py` régénère). Ce relevé prime sur les §2, §3 et §8 (Lunes, Colonies) quand ils divergent.

### Réglages d'univers et valeurs par défaut
- Défauts servis par `src/Universe/Domain/ReadModel/UniverseDefaultsReadModel::current()`, chacun lu dans le `default()` de son objet valeur (`src/Shared/Domain/ValueObject/`) :
  - `UniverseSpeeds::default()` : économie, construction, recherche, chantier, flotte à 1 (la vitesse flotte n'agit que sur la durée des vols, jamais sur la consommation, docblock de la classe) ;
  - `BashingRule::default()` : 6 attaques, fenêtre 24 h (0 attaque = règle coupée) ;
  - `BeginnerProtection::default()` : paliers 500 → 1:3, 5 000 → 1:5, 500 000 → 1:10, `inactivityDays` 14 ;
  - `DebrisRule` : vaisseaux 30 %, défenses 0 % ; `MoonFormation` : 20 %, 2 000 000 ;
  - `AbandonmentRule` : 60 jours ; bâtiments −1 puis −1 tous les 2 j ; flotte −30 % puis −5 % tous les 2 j ; défenses −35 % puis −5 % tous les 3 j ; satellites −100 % ; verrou ancien propriétaire 30 j ;
  - `ConstructionQueueCapacity` 2 / 5 ; `BookmarkCapacity` 10 / 200 ; `ExpeditionRule` ouverte ; `CosmicEventRule` : chaque événement fermé (`enabled` false par défaut dans `MeteorImpactRule`, `CometShowerRule`, `GiantImpactRule`).
- Pas de défaut pour la carte ni les ressources de départ : fixées à la création (`CreateUniverseRequestPayload` : positions par système `Range(9, 20)`, galaxies `<= 100`).
- Joueurs maximum : appliqué aux seuls univers privés (`Universe::hasRoomForAnotherPlayer()`).
- Fin d'univers : réservée aux univers privés (`Universe::finish()` lève `UniverseNotFinishableException::becausePublic`). Statuts : `opened`, `closed` (inscriptions fermées), `finished`, `suspended` (`UniverseStatus`).
- Mode `pvp` / `pve` (`UniverseMode`) : seul `pve` permet l'accélération payante (`allowsPaidAcceleration()`). Non publié (voir PR, point éditorial).
- Fonctions ouvertes par univers : `Feature` (`launch`, `alliance-missions`), fermées par défaut.
- Pillage : **pas** un réglage d'univers (taux calculé par `LootRate`, `AttackCombatResolver::plunder()`), retiré du tableau de P-11.
- Protection nouvel arrivant : `NewcomerProtection::DURATION_DAYS = 7`, fixe.
- Planète mère : `Base::createFirst()`, `DEFAULT_MOTHER_BASE_SIZE = 163`, ressources = `Universe::getBaseResources()`. Emplacement : `MotherPlanetFinderService` (galaxie puis système tirés, puis position) et `SectorRanges::motherPlanetPreference()` : positions floor(n × 5/15) à ceil(n × 8/15), puis floor(n × 2/15) à ceil(n × 12/15), puis 1 à n (Redline : 5 à 8, puis 2 à 12, puis 1 à 15).
- Changement de règles d'un univers privé annoncé 24 h avant : `Universe::GAMEPLAY_NOTICE_HOURS`.

### Carte et distances
- Cases d'un système : positions 1 à n, espace lointain n + 1 (`Universe::getDeepSpaceSector()`), Station stellaire n + 2, **une par système** (`getBankStationSector()`, `CreateMapRegionHandler` crée les deux à chaque système ; le commentaire « one per galaxy » de `SectorType::BANK_STATION` est périmé).
- Distance : `Game/Domain/ValueObject/Distance.php`, `units()` : 20 000 × ΔG, sinon 2 700 + 95 × ΔS, sinon 1 000 + 5 × ΔP, sinon 5. **Anneaux** depuis le 9 octobre 2026 (commits 3042c4e5 « wrap galaxy distance », #509, et 71ef4a35 « wrap systems round each galaxy », #513) : Δ = min(écart, taille − écart) pour galaxies et systèmes ; positions sans anneau. Remplace `universe-03` « pas circulaire ».
- Navigation de la vue galaxie : boucle aussi (front `useGalaxyPosition.ts`).

### Planètes
- `Universe/Domain/Service/PlanetGeneratorService::generate()` : position ramenée sur 15 avec **arrondi** (`round((p − 1) × 14 / (n − 1)) + 1`), taille = moyenne ± 15 (graine par coordonnées), types de `getPositionConfig()`, biome 1 à 6, température base = 160 − 15 × p, min = base − 20, max = base + 20.
- Température du jour : `Map::getTemperatureAt()` : pic au jour partie entière(jours du mois / 2), interpolation linéaire, arrondi.
- Facteurs : `BaseTemperature::hydrogenSynthesisFactor()` max(0, round(1,44 − 0,004 × Tmax, 3)) ; `solarPlantFactor()` 1 + max(0, T / 100). Collecteur : partie entière(Tmax / 4 + 20) (repris de `tools/economy_pages/econ_lib.py`, branche `audit-economie`).
- Cases : `Base::getSize()` ; la Station de réparation n'occupe pas de case (`occupiesField()`).
- Bonus de position : `Game/Domain/ValueObject/SystemPosition.php` : métal [0,0,0,0,0,17,23,35,23,17,0,…], cristal [40,30,20,0,…] sur 15 ; position lue **sans arrondi** `1 + (p − 1) × 14 / (n − 1)` et interpolation linéaire, arrondie à 0,01 ; production bonus = partie entière(mine × bonus / 100). Planète mère : aucun bonus sauf la part d'un talent (`Base::positionProductionBonus()`, `motherBasePositionBonusPercent()`, DYN-378). Talents qui élargissent le bonus : `amplifiedBy()` (non détaillés dans la rubrique). Tranche `universe-12`.

### Colonisation
- Places : `UserUniverse::maxBasesForAstrophysics()` = 1 + floor((N + 1) / 2) ; seules les planètes comptent (`ColonizeEligibilityChecker`).
- Cible espionnée obligatoire, par soi ou son alliance (`ColonizeEligibilityChecker::hasScouted()`, ALL-306).
- Cibles permises : `MissionTarget::allows(COLONIZE)` : case vide, monde abandonné (sauf ancien propriétaire pendant le verrou), ruine (mécanique des adversaires du jeu, non publiée) ; jamais lune, espace lointain ni station. `FlightPlan` : Pionnier obligatoire, même univers.
- Arrivée : `ColonizationResolver` : place revérifiée (sinon retour, rapport), un seul Pionnier consommé (`loseColonyShip()`), le reste de la flotte reste en garnison, cargaison déchargée (`Base::colonize()`, ressources = cargaison + `Map::consumeResources()`, ce qui est enfoui par les événements cosmiques). Case déjà occupée par un autre joueur : retour sans combat (`ColonizationCombatResolver` vide, TODO).
- Reprise d'un monde abandonné : `takeOver()` : dégradation soldée, tout reste (bâtiments, ressources, flotte, défenses, lune).
- Nouvelle colonie sans bâtiment : `Base::colonize()` passe `firstBuilding: null` ; Base planetaire (Base Coloniale) = bâtiment d'ancrage, préalable à tout autre (`BaseKind::anchorBuilding()`, `Base::checkAnchorBuilding()`), coût 0, durée fixe 10 s (`Building::PLANETARY_BASE_BUILDING_TIME`). Avant elle, stockage de repli 10 000 (`Base::getStorageDetail()`). Pionnier : MySQL `ship` (`colony_ship`) 10 000 / 20 000 / 10 000, structure 30 000, fret 7 500, vitesse 2 500, impulsion, conso 1 000, prérequis Dock orbital 4, Moteur Magnétique 3, Cosmologie Appliquée 1.

### Abandon
- Conditions : `Game/Domain/Service/AbandonEligibilityChecker::blockersFor()` : planète mère ; ordres `PENDING`/`QUEUED` sur la planète (bâtiment, vaisseau ou réparation, défense, recherche) ; activité sur la lune ; flotte du propriétaire touchant la case (`hasMovementTouchingMap`) ; missiles en vol depuis la case. Libellés : front `pages/planet.json`, `abandon.blockers`.
- `AbandonBaseHandler` : une lune ne s'abandonne pas seule ; production soldée ; planète et lune abandonnées ; choc `Base::applyAbandonmentShock()` sur les deux (floor par type ; satellites au taux satellites, sans débris ; épaves des autres vaisseaux au taux de débris vaisseaux de l'univers ; défenses sans débris) ; joueur ramené sur sa planète mère ; points retirés (`BaseAbandonedEvent`).
- Dégradation : `Base::settleAbandonmentDecay()`, pertes composées, au moins 1 unité par pas (`wastedAway()`). Ressources jamais dégradées.
- Fin : `ExpireAbandonedBasesHandler` : 60 jours (`AbandonmentRule::hasExpired()`) ou planète et lune vides (`isStrippedBare()` : bâtiments à 0, ni vaisseau ni défense) ; tout disparaît sauf les débris ; nom d'origine rendu.
- Transport interdit vers un monde abandonné (`MissionTarget::allows(TRANSPORT)`) ; limite d'attaques non appliquée (pas de défenseur, `SendFleetHandler`).

### Lunes
- Formation : `Game/Domain/Service/MoonFormationResolver` (débris de ce combat seulement, lune au propriétaire de la planète, débris non consommés, une lune par case) ; chance `MoonFormation::chanceFor()` = min(débris métal + cristal × max / plafond, max), nulle sous plafond / max.
- Taille : `MoonDiameter::roll()` : cases = 10 + X + 300 × p, X entier tiré de 0 à 10, p = max(0,01, min(1, chance / max) × 0,20) ; diamètre = floor(1 000 × √cases) ; plafond = floor((diamètre / 1 000)²). Le wiki ne publie que les bornes (X = 0 et X = 10), pas le tirage.
- Impact géant (événements cosmiques) : `MoonFormationResolver::resolveImpact()`, fermé par défaut ; chance non publiée.
- Cases : `Base::MOON_INITIAL_SIZE = 1`, `LUNAR_BASE_FIELDS_PER_LEVEL = 3`, `moonFields()` plafonnées par le diamètre ; levée du plafond par un talent (`moonDiameterUnbound`) mentionnée sans détail. *Lunes creusées* ne donne plus de cases depuis le rééquilibrage du 16 octobre 2026 (§18).
- Bâtiments (MySQL `building`, `scope`) : `lunar_base` 20 000 / 40 000 / 20 000, ×2, sans prérequis ni maximum, ancrage de la lune (`BaseKind::anchorBuilding()`, non démolissable) ; `sensor_phalanx` 20 000 / 40 000 / 20 000, ×2, Base lunaire 1 (tranche `moon-02`) ; `jump_gate` 2 000 000 / 4 000 000 / 2 000 000, ×2, Base lunaire 1 et `hyperspace` 7 ; `robotic_factory` et `shipyard` en `scope` `both`.
- Missions vers une lune : front `MissionActionBar.tsx` (espionner, attaquer, détruire, transporter, déployer) ; jamais colonisée (`MissionTarget`).

### Vue galaxie (front `src/features/galaxy`, `src/features/planets/page/GalaxyPage.tsx` ; back `MapReadModel::fromEntity()`)
- Statuts `owned`, `spied`, `discovered`, `empty`, `unknown` (`MapStatus`). Une case est révélée par un espionnage arrivé, du joueur ou d'un membre de son alliance (`SpyMissionResolver` l. 332-358), **sans expiration** (`DiscoveryStatus`, `SpyDiscovery`) ; `discovered` (Renseignement Tactique ≥ 10) et `spied` s'affichent de la même façon (`PlanetModal.tsx`). Contredit l'ancienne règle « avec RT 10, la case reste découverte durablement ».
- Badges (`PlanetCellBadges.tsx`, `utils/cellBadges.ts`, libellés `pages/planet.json`, `newcomer.json`), « Espionnée récemment » = moins de 5 min (`cellPresentation.ts`).
- Espionnage rapide : 1 sonde, vitesse 100 % (`utils/quickSpy.ts`). Partage d'alliance : rétention 30 j (`alliance_chat_retention_days`, `config/services.yaml`). Raccourcis : `useGalaxyKeyboardNavigation.ts`. Affichages Orbites / Liste : `PlanetGrid.tsx`, `galaxyViewStore.ts`.
- Lignes spéciales : `DeepSpaceRow.tsx`, `BankStationRow.tsx` (libellés `pages/bank.json`, « Station stellaire », « Ouvrir la station »).
- Coloniser et recycler exigent une case espionnée (`AllowedMissions.php`).

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

Bâtiments lunaires (Base lunaire, Phalange de capteur, Porte de saut) : présents dans les traductions, absents du catalogue planète. **Mise à jour du 15 octobre 2026** : ils sont désormais dans le catalogue du code (voir « Relevé dans le code » ci-dessous). Coûts et prérequis identiques à OGame (`universe-09`). Diamètre et formation des lunes identiques à OGame : 1 % par 100 000 débris, plafonné à 20 % (`universe-08`).

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
- Durée de construction (h) = (métal + cristal + hydrogène) / (2 500 × (1 + Fabrique d'automates) × 2^Assembleur moléculaire) ÷ vitesse construction. **Corrigé le 15 octobre 2026 d'après le code** : l'hydrogène compte aussi (l'ancienne ligne disait métal + cristal, ce qui ne se voyait pas sur les mines, sans hydrogène). Vérifié sur l'Excavateur 13 : 2 802 s.

### Relevé dans le code (15 octobre 2026)

Source : dépôt `astro-nova-backend`, branche `main` au commit `8bd7652b` (15 octobre 2026). Catalogue lu dans la table `building` après avoir rejoué toutes les migrations sur une base vide ; formules lues dans les fichiers cités. Les valeurs modifiées en production par l'administration ne sont pas visibles ainsi : en cas d'écart avec le jeu, c'est le jeu qu'il faut relever.

Catalogue (coût niv. 1 M / C / H / énergie requise, facteur, max, portée) :

| Code | Coût niv. 1 | Facteur | Max | Portée |
|---|---|---|---|---|
| planetary_base | 0 | 2 | 1 | planète |
| metal_mine | 60 / 15 / 0 | 1,5 | 50 | planète |
| crystal_mine | 48 / 24 / 0 | 1,6 | 50 | planète |
| hydrogen_synthesizer | 225 / 75 / 0 | 1,5 | 50 | planète |
| solar_plant | 75 / 30 / 0 | 1,5 | 50 | planète |
| fusion_plant | 900 / 360 / 180 | 1,8 | 50 | planète |
| metal_storage, crystal_storage, hydrogen_storage | 1 000 / 0 / 0 ; 1 000 / 500 / 0 ; 1 000 / 1 000 / 0 | 2 | 20 | planète |
| research_lab | 200 / 400 / 200 | 2 | 12 | planète |
| robotic_factory | 400 / 120 / 200 | 2 | 10 | **planète et lune** |
| shipyard | 400 / 200 / 100 | 2 | 12 | **planète et lune** |
| nanite_factory | 1 000 000 / 500 000 / 100 000 | 2 | 10 | planète |
| terraformer | 0 / 50 000 / 100 000 / 1 000 | 2 | 10 | planète |
| repair_dock | 200 / 0 / 50 / 50 | 5 (énergie requise : 2,5) | 10 | planète |
| missile_silo | 20 000 / 20 000 / 1 000 | 2 | 10 | planète (lune avec un talent de Vétéran) |
| logistics_center | 20 000 / 40 000 / 0 | 2 | 10 | planète |
| lunar_base | 20 000 / 40 000 / 20 000 | 2 | aucun | lune |
| sensor_phalanx | 20 000 / 40 000 / 20 000 | 2 | aucun | lune ; prérequis Base lunaire 1 |
| jump_gate | 2 000 000 / 4 000 000 / 2 000 000 | 2 | aucun | lune ; prérequis Base lunaire 1, Pliage Spatial 7 (`hyperspace`) |

Prérequis identiques au tableau ci-dessus. Les données lunaires intéressent `universe-09` et `moon-02` : statut laissé au lot des questions.

Formules et règles :
- Coût du niveau N : `Building::getCost()`, coût niv. 1 × facteur^(N − 1), arrondi à l'inférieur par ressource ; l'énergie requise suit `getEnergyMultiplicator()` (le facteur du coût, sauf la Station de réparation : 2,5).
- Points et durée : `Constructable::getTotalCost()` = métal + cristal + hydrogène, énergie exclue ; points = total / 1 000 (`getPoints()`) ; durée `Building::getBuildingTime()`, arrondie à la seconde, puis bonus du joueur dans `Base::buildingTimeOf()`. Démolition : moitié, arrondie (`getDemolitionTime()`).
- Production : `Building::getProduction()`. Mines 30, 20, 10 × N × 1,1^N × vitesse économie ; consommation d'énergie 10 × N × 1,1^N **sans** la vitesse ; Réacteur 30 × N × (1,05 + 0,01 × Science énergétique)^N énergie et 10 × N × 1,1^N × vitesse hydrogène ; arrondis vers zéro (`truncate()`). Base planetaire 20 métal et 10 cristal × vitesse. Facteurs de température : `BaseTemperature::solarPlantFactor()` (1 + max(0, T actuelle / 100)) et `hydrogenSynthesisFactor()` (1,44 − 0,004 × Tmax, arrondi à 3 décimales).
- Déficit d'énergie : `EnergyBalance::ratio()` = min(100 %, production / consommation), même ratio pour les trois mines hors talents (`MineEnergyRatios`). La Base planetaire n'est pas touchée.
- Taux de fonctionnement : `OperatingRate`, pas de 10 %, mines seulement (Réacteur avec un talent).
- Arrêt de la production : `Base::isProductionHalted()` : vacances, planète abandonnée, univers à l'arrêt (univers privé gelé ou terminé).
- Stockage : `Building::getStorage()`, 5 000 × arrondi inférieur(2,5 × e^(20 × N / 33)) ; Base planetaire 10 000 × niveau. Bonus : `Base::storagePercent()` = talents (dont Entrepôts fédérés) + Centre logistique (`LogisticsCenter`, 10 % par niveau), **additionnés**, appliqués à toute la capacité des bâtiments, Base planetaire comprise (`getResourcesStorage()`). Réponse à `economy-11`.
- Plafond : `Storage::fill()` : la production remplit jusqu'à la capacité, jamais au-delà ; un stock déjà au-dessus reste tel quel.
- Files : `ConstructionQueueCapacity`, 2 ordres et 5 en Premium par défaut, réglable par univers. Recherche : une étude à la fois pour tout l'empire, mais chaque planète compte sa propre file (`Base::startResearchStudy()`, `StartConstructionHandler::researchQueue()`). Vaisseaux et défenses : files séparées (`ShipyardLane`). Dock orbital en travaux : aucune commande d'unité (`ShipyardBusyException::underConstruction`).
- Centre d'innovation : le verrou « en travaux = pas de recherche sur cette planète » et l'inverse « recherche lancée d'ici = pas d'amélioration » sont appliqués par le front seulement (`Astro-Nova-React` : `useResearchLabLock.ts`, `BuildingCard.tsx`, `main` du 15 octobre 2026), pas par le serveur.
- Annulation : `CancellationRefundRate`, 80 %, plafond 95 %, relevé par le trait Rien ne se perd (+5 points) ; `Construction::getCancelRefund()` puis prorata du temps restant, deux troncatures successives.
- Démolition interdite : bâtiment d'ancrage de l'astre (Base planetaire, Base lunaire) et niveau 0 (`Base::checkCanDemolishBuilding()`).
- Station de réparation : `RepairDock` (coefficients de 45 % à 54 % du niveau 1 au niveau 10, 10 points de structure par seconde et par niveau, 1 800 à 43 200 s). Taux de débris par défaut : 30 % (`DebrisRule::default()`).
- Modulateur : `Base::planetFields()`, 5 cases par niveau + partie entière(niveau / 2). Base lunaire : 3 cases par niveau, plafonnées par le diamètre (`moonFields()`).
- Vaisseaux et défenses : coût par unité constant (`Ship::getCost`, `Defense::getCost`) ; durée = `build_time` du catalogue / ((1 + Dock orbital) × 2^Assembleur) ÷ vitesse chantier, au moins 1 s (`getConstructionTime()`), puis bonus de vitesse du propriétaire (`Base::unitTimeOf()`). Commande : stock vérifié pour toute la quantité à la commande (`checkHasEnoughResources(magnitude: quantity)`), unités payées une à une à leur entrée en production, commande coupée si l'unité suivante ne peut pas être payée (`Base::startNextUnit()`, `cutUnitOrderShort()`). Même unité que la dernière commande en attente : fusion sans nouvelle place (`findMergeableShipConstruction`, `findMergeableDefenseConstruction`). Réponse à `fleet-09` et `formula-04`.
- Collecteur solaire : `Ship::getProduction()`, partie entière(Tmax / 4 + 20) par unité, jamais négatif (réponse à `formula-05`).
- Recherche : `Research::getResearchTime()` = (métal + cristal) / (1 000 × (1 + niveau effectif du Centre d'innovation)) h ÷ vitesse recherche, puis bonus de vitesse (`Base::researchTimeOf()`).
- Bonus de vitesse : `AllianceBonuses::hasten()`, durée × 100 / (100 + bonus), arrondie au supérieur, au moins 1 s. La démolition n'en profite pas (`Base::demolitionTimeOf()`).
- Lune : sans Base planetaire, la capacité de repli est de 10 000 par ressource (`Base::buildingsStorage()`, `RESOURCE_BASE_STORAGE`).
- Station de réparation : déclenchée par `Base::sufferBattleDamage()`, appelée pour la planète qui défend après **tout** combat (`AttackCombatResolver`) et après une tentative de destruction de lune, qu'elle gagne ou perde : l'ancienne règle « combat perdu en défense » (`economy-08`) est corrigée.
- Déficit d'énergie : `Production::percentages()` tronque ; la Base planetaire est ajoutée après (`Base::productionAt()`).
- Écart corrigé le 15 octobre 2026 : le coût « relevé » de la Fabrique d'automates niveau 5 (12 800 / 3 840 / 6 400) était celui du niveau 6. Niveau 5 : 6 400 / 1 920 / 3 200.

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

### Relevé dans le code (15 octobre 2026)

Source : dépôt `astro-nova-backend`, `main` au commit `7b255c83` (15 octobre 2026). Catalogue lu en SELECT dans les tables `research`, `research_category`, `building`, `ship` et `defense` d'une base MySQL où toutes les migrations ont été rejouées (dernière : `Version20270103112617`) ; noms et rubriques affichés lus dans `Astro-Nova-React` `origin/main` (`src/i18n/locales/{fr,en}/researches.json`, `buildings.json`, `defenses.json`, `pages/research.json`, `talents.json`, `src/features/researches/researchSections.ts`). Les valeurs modifiées en production par l'administration ne sont pas visibles ainsi. Pages générées par `tools/research_pages/` (catalogue et formules dans `research_lib.py`).

Catalogue : **identique** au tableau ci-dessus (coût niv. 1, facteur, maximum, prérequis des 17 recherches, toutes `active`). Les prérequis de bâtiments, vaisseaux et défenses utilisés pour l'arbre sont ceux des tables `building`, `ship`, `defense` (recopiés dans `research_lib.py`).

Formules et règles :
- Coût : `Research::getCost()`, coût niv. 1 × facteur^(N − 1), arrondi à l'inférieur par ressource, énergie comprise (Manipulation Gravitationnelle : 300 000 × 3^(N − 1)). Réductions de talents : `Base::costOf()` / `costReductionOf()` (Protocoles, recherche profonde, niveaux connus, ingénierie inverse) ; la durée, elle, se calcule sur le coût du catalogue.
- Durée : `Research::getResearchTime()` = round((métal + cristal) / (1 000 × (1 + niveau effectif)) × 3 600 / vitesse recherche) secondes. Puis `Base::researchTimeOf()` : niveau effectif + bonus *Labo-mère* (`researchLabBonus()`, seulement si la planète a un Centre), puis `AllianceBonuses::hasten()` = max(1, ⌈durée × 100 / (100 + bonus)⌉) (pas d'arrondi si bonus nul). Bonus : `PlayerBonuses::researchSpeedPercentFor()`, talents plafonnés à 25 % (`RESEARCH_SPEED_TALENT_CEILING`), alliance + talents à 45 % (`RESEARCH_SPEED_CEILING`) ; s'y ajoutent hors plafond les niveaux connus de l'Archiviste (`knownLevelSpeedPercent()`, plafond 25 %) et les Leçons de la défaite sur Systèmes Offensifs, Champs de Protection, Métallurgie Avancée (`defeatLessonsPercentOf()`).
- Réseau : `ResearchNetworkCalculator::forBase()` lit les Centres des **autres** bases du joueur dans l'univers (niveau actuel, travaux en cours non comptés) ; `ResearchLabContributions::eligible()` : rien si Collaboration 0 ou Centre local 0 ; seuil = max(1, Centre local − tolérance) ; tri décroissant ; on garde les N + Centres supplémentaires premiers. `withAllied()` ajoute le meilleur Centre allié (*Échange universitaire*). `ResearchNetwork::effectiveLabLevel()` = local + somme + bonus *Labos de campagne* × nombre de Centres propres. Le réseau est évalué au lancement (`Base::startResearchStudy()`, `launchResearchStudy()`) ; recalcul en cours d'étude seulement avec *Réseau vivant* (`Base::recomputeResearchStudy()`, `networkLiveRecompute`).
- Une étude à la fois : `Base::startResearchStudy()` (file par base, `checkQueueHasRoom()` sur les études de cette base), `researchSlots()` = 1, 2 avec *Second centre d'innovation* (`hasParallelResearch()`). Seconde étude : autre recherche, rien en attente (`hasSecondLaboratoryFor()`) ; allure `TalentMechanics::secondLaboratoryPace()` (50 %, `PARALLEL_RESEARCH_SPEED_CAP_PERCENT`), durée `ResearchStudy::atItsPace()` = ⌈durée × 100 / allure⌉. Nom affiché : « Second centre d'innovation » / « Second Innovation Center » (`talents.json`, `components/constructionQueue.json`) ; les pages `dynasty/*` disent encore « Second laboratoire ».
- Prérequis : recherche vérifiée à chaque niveau sur la base qui lance (`checkCanStudyResearch()`, bâtiments de cette base, recherches de l'empire) ; bâtiment au premier niveau seulement (`checkCanConstructBuilding()` : « has already built this building ») ; en file, les ordres déjà placés comptent (`checkRequirement()` avec `projectedLevelOf()`), revérification au lancement, échec = abandon (`failLaunch()`).
- Énergie requise (Manipulation Gravitationnelle) : `Base::checkHasEnoughEnergyProduction()`, production brute d'énergie de la base (Capteurs, Réacteur, Collecteurs), rien n'est consommé ; `EnergyGate` : avec talents ≥ seuil (sans les surcharges) et centrales seules ≥ 5/6 du seuil. Durée 0 (métal + cristal = 0), points 0 (`getTotalCost()` exclut l'énergie).
- Points : (métal + cristal + hydrogène) / 1 000.
- Centre d'innovation en travaux : blocage par le front seulement (`pages.research.unavailable.locked`), voir §4.

Effets :
- Science Énergétique : `Building::getProduction()`, Réacteur = tronque(30 × N × (1,05 + 0,01 × SE)^N). Aucun autre usage que les prérequis.
- Maîtrise du Plasma : `Base::plasmaProductionBonus()`, `PLASMA_BONUS_METAL` 1,00, `_CRYSTAL` 0,66, `_HYDROGEN` 0,33 % par niveau, sur `ProductionBreakdown::mineOutput` (production brute des bâtiments, Base planetaire exclue, avant le ratio d'énergie), arrondi à l'inférieur ; talent `plasmaEffectPercent()` en plus. Vérifié sur l'ancien relevé : mines 13 → +13 métal, +5 cristal.
- Calcul Quantique : `UserUniverse::getMaxFleets()` = 1 + niveau + talents.
- Diplomatie Stellaire : `AllianceCapacity` (10, 15, 20, 25, 30, 35, 40, 50) ; fondation niveau 1 (`alliance_founding_diplomacy_level`, `config/services.yaml`) ; capacité relevée à chaque niveau terminé par le fondateur, jamais baissée (`RaiseAllianceCapacityHandler`, `raiseCapacityTo()`).
- Propulsion : `ReactorType::getBonusPerLevel()` 0,1 / 0,2 / 0,3 ; `ShipPropulsion::effectiveSpeed()` = vitesse × (1 + bonus × niveau). Changements de moteur (`ship.reactor_upgrades`, `ReactorUpgrades::bestReachedWith()`, le plus haut rang atteint) : Navette de fret → Moteur Magnétique 5 (vitesse 10 000, conso 20) ; Frappe-orbital → Navigation Transdimensionnelle 8 (5 000, 700) ; Récupérateur → Navigation Transdimensionnelle 15 (6 000, 900) et **Moteur Magnétique 17 (4 000, 600), inatteignable** : Moteur Magnétique plafonne à 15 (`research-03`).
- Moteur Magnétique : portée des Ogives longue portée = max(−1, 5 × niveau − 1) systèmes (`MissileRange::forImpulseDrive()`, `SYSTEMS_PER_DRIVE_LEVEL`), plus les talents (`missileRangeSystems()`).
- Pliage Spatial : `Ship::effectiveCargoCapacity()` = round(soute × (1 + 0,05 × niveau)).
- Systèmes Offensifs, Champs de Protection, Métallurgie Avancée : `Ship`/`Defense` `COMBAT_STAT_BONUS_PER_LEVEL` 0,1, round(base × (1 + 0,1 × niveau)) ; doctrine d'alliance et talents en plus (`CombatResearch`). Systèmes Offensifs : dégâts des Ogives × (1 + 0,1 × niveau) (`MissileBarrage::WEAPONS_BONUS_PER_LEVEL`).
- Renseignement Tactique : hydrogène d'une mission d'espionnage × max(0,5 ; 1 − 0,05 × niveau) (`SendFleetHandler`) ; niveau 10 = case « découverte » (`SpyMissionResolver::FULL_DISCOVERY_LEVEL`) ; profondeur des rapports §11.5 (`EspionageTier` 1, 3, 5, 7, 9).
- Cosmologie Appliquée : `UserUniverse::maxBasesForAstrophysics()` = 1 + ⌊(N + 1) / 2⌋ ; `ExpeditionSlots::forAstrophysics()` = ⌊√N⌋ (plus une en Premium dès le niveau 1, non reprise dans les pages : `patch-04`) ; `HoldDuration::maxHoursFor()` = N heures.
- Systèmes Photoniques, Manipulation Ionique, Manipulation Gravitationnelle : aucun usage hors prérequis (`ResearchCode::LASER`, `ION`, `GRAVITON` absents du code des effets).
- Rubriques de la page Recherche du jeu (`researchSections.ts`) : Fondamentale (Science Énergétique, Systèmes Photoniques, Manipulation Ionique, Pliage Spatial, Maîtrise du Plasma), Propulsion (trois moteurs), Combat (Systèmes Offensifs, Champs de Protection, Métallurgie Avancée), Stratégique (Renseignement Tactique, Calcul Quantique, Cosmologie Appliquée, Collaboration Stellaire, Manipulation Gravitationnelle, Diplomatie Stellaire). Elles diffèrent des catégories serveur (`research_category`).
- Texte du jeu trompeur (`pages.research.network.description`, FR et EN) : « Le Centre d'innovation le plus avancé de votre empire accélère cette recherche » ; le code en prend jusqu'à N, N = niveau de Collaboration Stellaire (`research-04`).
- Univers : `UniverseSpeeds::default()` = ×1 partout ; Redline ×1 (§2).

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

## Flotte (code, 15 octobre 2026)

Source : `astro-nova-backend` `main` au commit `7b255c83` ; catalogues lus dans une base migrée (tables `ship`, `rapid_fire`) ; libellés `Astro-Nova-React` `main` (`33217140`), `src/i18n/locales/{fr,en}/pages/fleet.json`, `researches.json`, `defenses.json`, noms des vaisseaux dans `src/data/shipsData.ts` (toujours en français). Pages générées par `tools/fleet_pages/` (`fleet_lib.py` porte les valeurs et les formules ; exemples recalculés par les scripts).

**Vaisseaux** (`Game/Domain/Entity/Ship.php`, table `ship`)
- Coûts, structure, bouclier, attaque, fret, vitesse, consommation, prérequis : identiques au tableau du §6, relevés en base. `build_time` (s, durée de base) : Navette 5 400, Cargo 14 400, Pionnier 100 800, Récupérateur 25 200, Éclaireur 600, Collecteur 2 880, Intercepteur 1 800, Assaillant 5 400, Corvette 28 800, Cuirassé 64 800, Frappe-orbital 86 400, Prédateur 79 200, Annihilateur 115 200, Colossus 12 960 000. Durée = `build_time` / ((1 + Dock) × 2^Assembleur) ÷ vitesse chantier, arrondie, au moins 1 s (`getConstructionTime()`) : 5 400 / 5 = 1 080 s retrouve le relevé de `formula-04`.
- **Changement de moteur** (`reactor_upgrades`, `ReactorUpgrades::bestReachedWith()`, Backend #543 du 11 octobre 2026) : Navette → Moteur Magnétique au niveau 5 (vitesse 10 000, conso 20) ; Récupérateur → Moteur Magnétique 17 (4 000, 600) ou Navigation Transdimensionnelle 15 (6 000, 900), le plus avancé atteint l'emporte ; Frappe-orbital → Navigation Transdimensionnelle 8 (5 000, 700). Le §6 et le §11.2 (« moteur fixe ») sont périmés.
- Vitesse = vitesse du moteur × (1 + bonus × niveau), bonus 0,1 / 0,2 / 0,3 (`ReactorType::getBonusPerLevel()`). Aucune recherche ne baisse la consommation (`fuelConsumptionFor()`).
- Fret : arrondi(fret × (1 + 0,05 × Pliage Spatial)) (`effectiveCargoCapacity()`) ; talents de soute plafonnés à 25 % (`PlayerBonuses::CARGO_TALENT_CEILING`).
- Combat : +10 % par niveau, arrondi ; coque en combat = structure / 10 (`combatStats()`, `COMBAT_HULL_DIVISOR`).
- `warp_factor` : lu par aucun calcul (seulement affiché).
- Points : (M + C + H) / 1 000 par unité (`Constructable::getPoints()`), crédités au seau **militaire** à la livraison pour **tous** les vaisseaux (`AbstractUnitDeliveryPointsHandler`), retirés à la perte (`DeductLostShipsPointsHandler`). L'ancienne règle « les civils ne comptent pas » est fausse.
- Familles du jeu : `type` civil / military / advanced = « Vaisseaux Civils / de Combat / Spéciaux » (`fleet.json`). Le Collecteur solaire est `advanced`.
- Collecteur solaire : ne vole jamais (`FlightViolation::SOLAR_SATELLITE_ABOARD`).

**Tirs rapides** (table `rapid_fire`, 56 lignes, identiques au §6 ; `BattleSimulator::fire`) : cible tirée au hasard, après chaque tir (touché ou non) nouveau tir avec probabilité (f − 1) / f si la dernière cible est dans la table, nouvelle cible au hasard. Facteurs de base, modifiables par talents (non détaillés sur la page).

**Vols** (`FlightPlan`, `FleetFlight`, `Distance`)
- Vitesse de 1 à 100 % par pas de 1 (`FlightPlan::MIN/MAX_SPEED_PERCENT`, `SendFleetRequestPayload` Range 1..100, front `speedScale.ts` pas 1). L'ancien pas de 10 % est périmé.
- Distance : `Distance::units()` (20 000 × Δg ; 2 700 + 95 × Δs ; 1 000 + 5 × Δp ; 5). **Carte circulaire** pour galaxies et systèmes : `Distance::roundTheRing()` (Backend #509 et #513, 9 octobre 2026), écart = min(écart direct, taille − écart direct). Positions non circulaires. Contredit `universe-03` (§11.2).
- Durée = (10 + 3 500 / s × √(10 d / V)) / vitesse flotte / bonus, s en fraction, arrondie, au moins 1 s (`FleetFlight::over()`), identique à l'ancienne écriture 35 000 / S.
- Consommation par trajet : Σ F × N × d / 35 000 × (s √(V / Vᵢ) + 1)², arrondie à l'inférieur, au moins 1 (`legBurn()`, `computeLegConsumption()`) ; aller-retour = deux trajets, sauf Colonisation et Stationnement (`FleetMission::isRoundTrip()`). F = consommation du moteur actuel.
- **Le carburant occupe la soute** : charge = cargaison + volume du carburant (`FlightPlan::loadOf()`, `FlightTalents::fuelVolume()`), talent Soute à carburant au plus −75 %.
- Bonus : vitesse plafonnée à 60 % (`FleetBonus::FLEET_SPEED_CEILING`), carburant à 45 % (`FUEL_CONSUMPTION_CEILING`), jamais sous 1 ; talents d'alliance Propulsion coordonnée et Ravitaillement optimisé, 4 niveaux de 5 %. Bonus hors plafond (retour, trajets internes, rappel, repli éclair) cités sans chiffres.
- Vitesse flotte de l'univers : divise la durée, pas la consommation (`UniverseSpeeds`). Défaut ×1 (`UniverseSpeeds::default()`), Redline ×1 (§2).
- Emplacements : 1 + Calcul Quantique + talents (`UserUniverse::getMaxFleets()`, `FLEET_SLOTS_CEILING` 3, dont l'emplacement d'attaque de l'Amiral) ; comptent les flottes à l'aller, en maintien et au retour, dépôts compris ; missiles et sauts non. Navettes du Navigateur hors emplacements (`takesShuttle()`). Premium : aucun emplacement de flotte.
- Rappel (`Fleet::returnToOrigin()`) : à l'aller ou en maintien, pas au retour, jamais pour un dépôt ; retour = temps déjà volé ; expédition en maintien : tout l'aller, aucun résultat ; aucun remboursement sauf talent Réservoir rendu ; l'attaque rappelée rend sa place dans la limite (`AttackTally::refund()`).
- Retour (`ReturningFleetResolver`) : base de départ disparue, perdue ou sans Dock orbital = flotte perdue (`HOME_DOCK_UNAVAILABLE`) ; déchargement au-delà des entrepôts.

**Missions** (`FleetMission`, `SendFleetHandler`, `FlightPlan::structuralViolations()`, `MissionTarget`)
- 10 missions : les 8 du §1 + `bank_deposit` « Dépôt à la banque » / « Bank deposit » et `alliance_deposit` « Don à l'alliance » / « Alliance donation ». Dépôts : 1 h aller, 1 h retour (`fixedLeg()`), 0 hydrogène, sans rappel, cargos seulement, base de départ avec Dock (`STATION_DEPOSIT_REQUIRES_DOCK`, Backend #569).
- Maintenance : Attaque, Espionnage, Destruction bloquées au départ (`isIntrusive()`). Vacances : l'expéditeur ne peut rien envoyer ; la cible en vacances refuse Attaque, Destruction, Transport (`reachesTargetOwner()`).
- Stationnement : propre base avec Dock ≥ 1 ; à l'arrivée sans Dock, cargaison déposée, vaisseaux renvoyés (`DeploymentResolver`).
- Colonisation : place de colonie libre et cible espionnée (`ColonizeEligibilityChecker`) ; un Pionnier consommé, cargaison = stock de départ, autres vaisseaux en garnison (`ColonizationResolver`).
- Espionnage : hydrogène payé × max(0,5 ; 1 − 0,05 × Renseignement Tactique), arrondi à l'inférieur (`SendFleetHandler`).
- Recyclage : position espionnée au moins une fois par soi ou l'alliance, sauf sa base et l'espace lointain (`RecycleEligibilityChecker`) ; soute des Récupérateurs seulement (`RecycleArrivalResolver`).
- Transport : livraison sans plafond d'entrepôt (`Base::receiveFleet()`).
- Alerte d'attaque : 60 s, jusqu'à 360 s (Oracle) (§18).
- Non publiés : le contrôle serveur de la Destruction de lune (tir ami, protections, limite d'attaques) ne passe que par la vue galaxie (`AllowedMissions`) ; un rapport de recyclage refusé semble laisser la flotte à l'arrivée (`RecycleArrivalResolver::resolve()` sort avant `returnFromMission()`) : deux points signalés dans la PR, à remonter à l'équipe.

**Expéditions** (`ExpeditionRule`, `HoldDuration`, `ExpeditionSlots`, `ExpeditionResolver`)
- Ouvertes par défaut (`ExpeditionRule::default()`, migration `Version20261031100000` pour tous les univers) ; Redline ouvert (note de version, §10).
- Maintien 1 h à niveau de Cosmologie h, par heure ; carburant du maintien = ⌈h × Σ conso de base / 10⌉ (`HoldDuration::fuelFor()`, consommation d'origine), hors économies de carburant.
- Simultanées = ⌊√Cosmologie⌋ (`ExpeditionSlots`), **+1 en Premium** (`PREMIUM_BONUS`, Backend #442) : non écrit dans le wiki tant que `patch-04` est ouvert.
- Rappel en maintien : aucun résultat ni rapport. Le raccourci « skip-hold » est un outil de test interdit en production.
- Points d'expédition = max(200, ⌊Σ structure / 200⌋) (`ExpeditionPoints`), plafond selon le meilleur joueur humain (`ExpeditionFindCap`, table inchangée du §11.3).
- Effets publiés : diviseurs 1 / 2 / 3 (`FoundResource::amountFor()`), vaisseaux = moitié de la valeur (`ExpeditionResolver`), hors soute, échelle `ExpeditionShipLadder::standard` (rang + 1, exclusions) ; retard + maintien × 2/3/5, retour anticipé ÷ 2/3/5 (`ReturnLegShift`) ; pirates −3, aliens +3 (`HostileFaction::RESEARCH_GAP`) ; débris 10 % (`DebrisRule::expedition()`) ; trou noir = perte totale ; épuisement à 10 et 25 expéditions sur 24 h par espace lointain, tous joueurs (`DepletionLevel`, `ExpeditionVisits`) ; état de la zone donné si un Éclaireur est à bord.
- **À republier (décision du 21 octobre 2026, `fleet-12`)** : poids des résultats (`ExpeditionOutcomeWeights::default()`), probabilités de taille et plages de facteur (`FindSize`), choix de la ressource (`FoundResource::fromRoll()`), part des flottes pirates et aliens et sa dispersion, composition des escortes (`HostileFaction`, `EncounterShare`), multiplicateurs d'épuisement (`DepletionLevel::oddsKept()`), talent Flair de prospecteur. Les valeurs ne sont pas recopiées ici (dépôt public) ; celles du §11.3 datent du 2 octobre et étaient publiées sur la page jusqu'au 15 octobre 2026 : retirées de la page, leur maintien au §11.3 est signalé au responsable.

**Porte de saut** (`JumpFleetHandler`, `JumpGateCooldown`, migrations `Version20260918090000`, `Version20260919090000`)
- Recharge : table `LADDER` (§11.6 confirmée), niveau 14 et plus = 10 min, sans vitesse d'univers ; talents −30 % au plus (`JUMP_GATE_RECHARGE_SPEED_CEILING`), Porte double = 2 sauts.
- Lunes du même joueur seulement (`differentOwners`), même univers ; les deux portes vérifiées avant tout mouvement ; aucune ressource ; pas de niveau maximum (`max_level` NULL).

**Dock orbital** (`Base::startNextUnit()`, `UnitConstructionTrait`, `ConstructionQueueCapacity`)
- File de vaisseaux et file de défenses en parallèle, 2 ordres (5 en Premium) chacune, paramètre d'univers (défaut 2 / 5, Redline 2 / 5, §2) ; fusion avec le dernier ordre en attente (unités uniques jamais) ; 1 à 1 000 000 unités.
- Paiement : commande vérifiée en entier, unités payées une à une à l'entrée en production, commande coupée faute de ressources (`cutUnitOrderShort()`), livraison unité par unité.
- Annulation : 80 % de l'unité payée non livrée (`CancellationRefundRate`, 95 % au plus par talent) ; arrêt après l'unité en cours (`stopUnitOrderAfterCurrentUnit()`).
- Dock occupé : ni amélioration ni démolition (`checkShipyardIsNotProducingUnits()`) ; Dock en travaux : aucune commande. Dock constructible sur lune (`scope 'both'`), Assembleur moléculaire non.

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

### Défense : relevé dans le code (15 octobre 2026)

Source : `astro-nova-backend` `main` au commit `7b255c83` ; catalogue dans la table `defense` d'une base migrée (semée par `migrations/2026/01/Version20260107171230` et suivantes), tirs rapides dans `rapid_fire`, Arsenal dans `building` ; libellés : `Astro-Nova-React` `main`, `src/i18n/locales/{fr,en}/defenses.json`, `pages/defense.json`, `researches.json`. Pages générées par `tools/defense_pages/p_defense.py` (valeurs dans `def_lib.py`).

**Catalogue** (`build_time` en secondes, durée à Dock 0) : Projecteur balistique 2 880, Canon photonique 2 880, Émetteur à haute énergie 11 520, Batterie ionique 11 520, Accélérateur magnétique 50 400, Éjecteur à plasma 100 800, Barrière défensive 28 800, Dôme protecteur 144 000, Intercepteurs 11 520, Ogives 21 600. La colonne « Durée (s) » du tableau ci-dessus était relevée avec un Dock orbital niveau 4 (÷ 5). Coûts, structure, bouclier, arme, prérequis, unicité (`unique`) et cases (`silo_slots`) identiques au tableau ci-dessus ; `shot_count` = 1 partout ; `unit_kind` = `missile` pour Intercepteurs et Ogives.

**Construction** (`Base::startDefenseConstruction()`, `startActiveDefenseConstruction()`, `addDefensesToConstruction()`, `StartConstructionHandler`)
- Dock orbital requis (`checkHasShipyard`), refus pendant son agrandissement (`checkShipyardIsNotUnderConstruction`), refus en vacances (`ensureNotOnVacationIn`).
- File des défenses comptée à part de celle des vaisseaux (`countUnfinishedDefenseOrders`, `hasActiveDefenseConstruction`) ; capacité `ConstructionQueueCapacity::default()` 2, Premium 5, par univers.
- Fusion avec une commande non terminée de la même défense (`findMergeableDefenseConstruction`), jamais pour une défense unique.
- Unicité (`checkUniqueDefenseNotAlreadyBuilt`) : quantité 1 au plus, aucune possédée, aucune en file ou en cours.
- Durée : `Defense::getConstructionTime()`, `round(build_time / ((1 + Dock) × 2^Assembleur) / vitesse chantier)`, au moins 1 s, puis `Base::unitTimeOf()` (bonus de vitesse). Paiement unité par unité : voir la rubrique Économie (`fleet-09`).
- Défenses possibles sur une lune : le Dock orbital y est constructible (`building.scope` = `both`), aucune restriction de corps dans la commande. L'Arsenal balistique est `planet` seulement.

**Combat et points**
- `Defense::combatStats()` : arme, bouclier, structure × (1 + 0,1 × niveau de Systèmes Offensifs, Champs de Protection, Métallurgie Avancée), arrondis (`round`) ; coque = structure renforcée / 10, arrondie (`COMBAT_HULL_DIVISOR`). Les missiles sont exclus des combats et des débris (`Defense::isMissile()`).
- Aucune défense n'a de tir rapide (`rapid_fire` : aucune ligne dont l'attaquant est une défense).
- Règle du 1 % : `BattleRules::default()` (`shieldBounceThreshold` 0,01), `BattleLine::takeHit()`.
- Débris des défenses : `DebrisRule` 0 % par défaut, Redline 0 %.
- Points : `Constructable::getPoints()` = coût total / 1 000 ; `Base::defensePoints()` compte les missiles stockés dans les points militaires (`RankingCategory::MILITARY`).

**Arsenal balistique** (`SiloCapacity`, `Base::missileSiloCapacity()`, `checkSiloHasRoom()`)
- 10 cases par niveau (`SLOTS_PER_LEVEL`) ; cases occupées = missiles stockés + unités restantes des commandes en file ou en cours ; une commande qui ne tient pas est refusée avant paiement (`MissileSiloCapacityExceededException`). Cases libres jamais négatives (Arsenal démoli sous son contenu). Bonus de talent en pourcentage, arrondi à l'inférieur (*Fosses profondes*).
- Arsenal : coût 20 000 / 20 000 / 1 000, facteur 2, niveau max 10, prérequis Dock orbital 1, planète seulement (table `building`).

**Portée, vol, cibles** (`MissileRange`, `MissileFlight`, `Distance`, `LaunchMissilesHandler`, `MissileStrike::launch()`)
- Portée = 5 × niveau du Moteur Magnétique (`impulse_drive`) − 1 systèmes, −1 sans le moteur ; jamais d'une galaxie à l'autre (`covers()` : `distance->galaxy > 0` = hors de portée). Bonus de talents en systèmes (*Allonge*, *Portée d'impulsion*) ; *Contre-salve* rend portée illimitée contre une base qui vient de frapper.
- Distance en systèmes mesurée sur l'anneau de la galaxie (`Distance::roundTheRing`, Backend #509 et #513 du 9 octobre 2026). La position ne compte pas. Ce point contredit « la carte n'est pas circulaire » (AGENTS.md §4), déjà signalé par la rubrique Espionnage.
- Vol = 30 s par système (`SECONDS_PER_SYSTEM`), au moins 30 s (`max(1, systèmes)`). La cible n'est pas prévenue : seules les salves du tireur sont listées (`ListMissileStrikesHandler`), et l'aide du jeu le dit (`missiles.strike.rules.noSlot`).
- Cible : la planète de la case (`Map::getBase()` = corps `PLANET`), jamais la lune ; case vide refusée (`MissileTargetNotFoundException`) ; sa propre planète refusée (`CannotStrikeOwnPlanetException`). Tir depuis une lune réservé au talent *Silo lunaire* (`Base::fireMissiles()`), sans effet pratique puisque l'Arsenal ne se construit pas sur une lune.
- Contrôles dans l'ordre : maintenance (`MaintenanceGuard::assertHostilitiesAllowed`, une salve en vol arrive quand même), vacances du tireur, puis, si la planète a un propriétaire : pas soi-même, vacances de la cible (`VacationShieldChecker`), tir ami (`FriendlyFireChecker`, ALL-307), protection des nouveaux arrivants (`NewcomerProtectionChecker`), protection des débutants (`BeginnerProtectionChecker`), limite d'attaques (`AttackTally::registerAttack`, `BashingRule` 6 sur 24 h par couple tireur, défenseur). Planète abandonnée : aucun de ces contrôles. Le tir met fin à la protection de nouvel arrivant du tireur (`breakNewcomerProtectionIn`).

**Impact** (`MissileStrikeResolver`, `MissileInterception`, `MissileBarrage`, `DefenseGrid`, `Base::sufferMissileStrike()`)
- Interception : un Intercepteur pour une Ogive, sans tirage, avant les dégâts ; les Intercepteurs consommés sortent du stock et des points (`BaseMissilesFiredEvent`). Talents : *Pluie d'acier* (salve non interceptable) et *Intercepteurs récupérés* (tirage par unité, non publié).
- Dégâts = ⌊12 000 × (1 + 0,1 × Systèmes Offensifs du tireur) × Ogives arrivées⌋, × (1 + bonus *Charge creuse*).
- Résistance d'une ligne = bouclier + coque de combat du défenseur, recherches, doctrines et talents compris (`Base::defenseGrid()`, `CombatResearch::withBonuses`). Missiles du silo exclus de la grille.
- Ordre (`DefenseGrid::firingOrder`) : ligne désignée d'abord si présente, puis résistance décroissante. `MissileBarrage::shatter()` : sur chaque ligne, `min(quantité, ⌊reste / résistance⌋)` unités détruites ; une ligne qu'on ne peut pas entamer est **sautée** (`continue`), le reste passe aux lignes suivantes. Le commentaire de la classe dit « stopping as soon as the pool can no longer pay » : le code continue, c'est lui qui est publié.
- Pertes définitives, points retirés (`BaseUnitsLostEvent`) ; seule exception, le talent *Sous le feu* (tirage par unité, un cinquième au plus, non publié).
- Rapports pour le tireur et le défenseur (si le rapport n'est pas désactivé, `DeclinableReport::MISSILE_STRIKE_REPORT`), avec la planète d'origine ; les lignes non touchées ne sont pas révélées au tireur.
- Riposte automatique (talent du Vétéran) : réserve marquée, salve égale à celle reçue dans la limite du talent ; non détaillée dans la rubrique Défense.
- Non publiés : graine et tirages (`MissileStrikeDice`), taux des talents (renvoi vers la rubrique Dynastie).

**Exemples recalculés** par `tools/defense_pages/p_defense.py` (Projecteurs à Dock 4, Batterie ionique en combat, Dôme face aux Ogives, salve de 5 Ogives sur [3:55:4], anneau 97 → 3).

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
- Guerres : déclarées par vote ~~des officiers et plus~~ de **tous les membres** (corrigé le 15 octobre 2026, voir §19), à la majorité des voix exprimées ; égalité = rejet.
- Station d'alliance, talents (payés en points de doctrine et ressources), trésorerie commune, demandes d'aide plafonnées par jour.
- Missions d'alliance par cycle : combats, pillage, espionnage, recyclage, dons, bâtiments, recherches, vaisseaux, défenses. Paliers Bronze, Argent, Or selon la contribution ; récompenses en packs de ressources et parfois en Points stellaires. **Périmé** : remplacé par les missions V2, voir §19.
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
- Elle s'ajoute à la protection des débutants par paliers de points. ~~La durée de 7 jours est un **paramètre d'univers** (`patch-01`).~~ **Corrigé le 15 octobre 2026** : 7 jours en dur dans le code, identiques dans tous les univers (§11.7, relevé dans le code).

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
- ~~**La carte n'est pas circulaire** : la galaxie 9 n'est pas voisine de la 1.~~ **Périmé** depuis le 9 octobre 2026 : galaxies et systèmes bouclent (voir « Flotte (code, 15 octobre 2026) »).

**Vitesse**
- Vitesse d'un vaisseau = vitesse de base × (1 + bonus × niveau de la recherche de son moteur) : +10 % par niveau de Propulseur Chimique, +20 % Moteur Magnétique, +30 % Navigation Transdimensionnelle.
- ~~**Le moteur d'un vaisseau est fixe**~~ **Périmé** depuis le 11 octobre 2026 : Navette, Récupérateur et Frappe-orbital changent de moteur comme dans OGame (voir « Flotte (code, 15 octobre 2026) »).
- La flotte va à la vitesse de son vaisseau le plus lent, × bonus du talent Propulsion coordonnée.
- **Le facteur de distorsion (`warpFactor`) n'a aucun effet** : statistique réservée, lue par aucun calcul.

**Durée** (secondes) = (10 + 35 000 / S × √(10 × d / V)) / vitesse Flottes de l'univers, arrondie, minimum 1. V = vitesse de la flotte ; S = facteur de vitesse de 1 à 10 par pas de 1 (1 = 10 %, 10 = 100 %), précisé le 2026-10-06 (la constante est passée de 3 500 à 35 000). **Mis à jour** le 15 octobre 2026 : la vitesse se règle de 1 à 100 % par pas de 1 (voir « Flotte (code, 15 octobre 2026) »).

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
- Explosion (**précisé par le code le 15 octobre 2026** : après tout tir non rebondi, voir ci-dessous) : après un tir qui entame la coque sans la détruire, si la coque passe sous 70 %, l'unité explose avec une probabilité de 1 − fraction de coque restante. Un tir rebondi n'ouvre pas ce tirage.
- **Statistiques de combat** : coque = structure × (1 + 0,1 × Métallurgie Avancée) / 10 ; bouclier × (1 + 0,1 × Champs de Protection) ; arme × (1 + 0,1 × Systèmes Offensifs). Les Doctrines d'alliance ajoutent 5 %.
- Résultat : victoire de l'attaquant si le défenseur est vide ; victoire du défenseur si l'attaquant est vide ; sinon égalité (deux camps debout après 6 rounds, ou deux camps vides).
- Les tirages sont déterministes par combat : un même combat rejoué donne le même résultat.

**Boucliers**
- Règle du 1 % : un tir inférieur à 1 % du bouclier maximal de la cible rebondit sans effet.
- Sinon le bouclier absorbe tant qu'il en reste ; l'excédent passe entièrement sur la coque.
- Régénération complète au début de chaque round, jamais en cours de round.
- Barrière défensive et Dôme protecteur : cibles ordinaires avec un gros bouclier individuel, **pas de bouclier global**. Un seul exemplaire de chaque (impossible d'en commander ou d'en mettre en file un deuxième).

**Pillage** (`combat-04`, `combat-05`)
- Butin = 50 % de chaque ressource de la cible (arrondi inférieur), énergie exclue, **uniquement en cas de victoire**. ~~Paramètre d'univers.~~ **Corrigé par le code (15 octobre 2026)** : taux fixe, aucun réglage d'univers, voir « Relevé dans le code » ci-dessous.
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

#### Relevé dans le code (15 octobre 2026)

Source : dépôt `astro-nova-backend`, `main` au commit `7b255c83` (15 octobre 2026) ; catalogue lu dans les tables `ship`, `defense`, `rapid_fire` et `alliance_talent` d'une base où toutes les migrations ont été rejouées ; libellés du front (`Astro-Nova-React`, `origin/main` du 15 octobre 2026, `src/i18n/locales/{fr,en}`). Les huit pages de la rubrique sont générées par `tools/combat_pages/p_all.py` (constantes et formules dans `combat_lib.py`). Les valeurs modifiées en production par l'administration ne sont pas visibles ainsi.

Moteur (`Game/Domain/Service/BattleSimulator.php`, version d'algorithme 4.3) :
- `BattleRules::default()` : 6 rounds, rebond sous 1 % du bouclier de la cible (`shieldBounceThreshold` 0,01, comparé au bouclier effectif maximal, `BattleLine::takeHit()`), explosion sous 70 % de coque (`explosionThreshold` 0,7). Ces règles ne sont pas réglables par univers (TODO dans `AttackCombatResolver`).
- Précision : `HitChanceParameters::alwaysHit()` dans `AttackCombatResolver`, `MoonDestructionResolver`, `ExpeditionCombatResolver` et `BattleSimulationRunner` : tout tir touche. Le modèle d'esquive (`HitChanceCalculator`, `HitChanceParameters::default()`, sigmoïde vitesse / coque, parité 70 %) existe mais **n'est pas branché** : non publié.
- Round : boucliers rechargés (`BattleLine::resetShields()`), coque jamais réparée en cours de combat ; effectifs du début de round figés (`aliveByType()`), attaquant puis défenseur ; chaque unité tire `shotCount` coups (1 pour toutes les unités du catalogue), dégâts par coup = arme / `shotCount` (`CombatStats::damagePerShot()`), multipliés par la table de talents du camp (`BattleTraits`).
- Cible : `BattleLine::pick()`, uniforme sur toutes les unités vivantes du camp adverse.
- Tir rapide : après chaque tir, nouveau tir avec probabilité (f − 1) / f contre la cible qui vient d'être visée, nouvelle cible tirée à chaque fois (`BattleSimulator::fire()`). Les défenses n'ont aucune ligne d'attaquant dans `rapid_fire`.
- Explosion : `resolveShot()` tire l'explosion après **tout tir non rebondi** qui n'a pas détruit la cible (tir absorbé par le bouclier compris), si coque / coque max < 0,7 ; probabilité 1 − ratio. Écart avec l'ancien wiki (« après un tir qui entame la coque »).
- Résultat : `result()` ; égalité si les deux camps sont vides ou debout.
- Talents du Vétéran : table de premier round et dernière salve des défenses sur un match nul (`BattleTraits::defenderFirstRound`, `defenderLastSalvo`).
- Après le combat, seules les quantités sont conservées (`Base::sufferBattleDamage()`, `Fleet::loseShips()`) : une unité survivante repart intacte. Réponse à `combat-03`.
- Hasard : une graine par arrivée (identifiant de flotte et instant d'arrivée, `BattleDiceFactoryInterface::seedFor()`), flux séparés pour la reconstruction, la lune, le remorquage et la destruction de lune. Le wiki dit seulement que le combat est rejouable et que les tirages suivants sont fixés par le combat ; ni graine, ni sel, ni mode de calcul publiés.

Statistiques effectives (`Ship::combatStats()`, `Defense::combatStats()`, `CombatResearch::withBonuses()`, `AllianceBonuses::boost()`) :
- arme = round(arme × (1 + 0,1 × Systèmes Offensifs)) ; bouclier = round(bouclier × (1 + 0,1 × Champs de Protection)) ; coque = round(round(structure × (1 + 0,1 × Métallurgie Avancée)) / 10) (`COMBAT_HULL_DIVISOR` 10, `COMBAT_STAT_BONUS_PER_LEVEL` 0,1). `round` de PHP (moitié loin de zéro).
- Puis × (1 + (Doctrine + talents) / 100), arrondi à l'inférieur après `round(…, 6)` : Doctrine d'armement sur l'arme, Doctrine de protection sur bouclier et coque, chacune 5 % (`alliance_talent.effect_per_level` 5, `max_level` 1, migration `Version20261010090000`), additionnées aux talents de dynastie avant application. Doctrine active à la fin de la période d'intégration (`AllianceMemberBonuses`, `effectiveFrom`).
- Catalogue de combat relu dans `ship` et `defense` : identique à DONNEES §6 et §7.

Pillage (`AttackCombatResolver::plunder()`, `LootRate`, `Fleet::loadPlunder()`, `Fleet::fit()`) :
- `LootRate::STANDARD_PERCENT` = 50, **constante du code** : il n'existe aucun réglage d'univers de la part pillée (`Universe` n'a pas de champ de pillage). `combat-04` et l'encart de la page Pillage disaient le contraire : corrigé.
- Victoire seulement, sauf talent Percée (Amiral) sur un match nul. Stock mis à jour à l'instant d'arrivée (`updateResources(force: true)`). Arrondi : floor(round(r × 50 / 100, 6)) par ressource, énergie exclue.
- Soute : `CargoBonus::capacityOf()`, `Ship::effectiveCargoCapacity()` = round(fret × (1 + 0,05 × Pliage Spatial)) par vaisseau, × quantité, plus les talents de soute ; moins la cargaison à bord (`freeCargo()`). Dépassement : floor(soute × r / total) par ressource, ou ordre de chargement choisi (talent, `LoadingPriority`).
- Talents : abri du défenseur, plancher 30 % (`PlayerBonuses::LOOT_RATE_FLOOR`) ; pillage relevé contre une planète abandonnée (`ruinLootRatePoints`, Razzia) ; Acompte.
- Une attaque visant une lune pille le stock de la lune (`$targetMap->body($targetBody)`).

Débris (`DebrisFieldCalculator::fromLosses()`, `Shared/Domain/ValueObject/DebrisRule.php`) :
- Défauts : vaisseaux 30 %, défenses 0 % ; expédition 10 % fixe (`DebrisRule::expedition()`). Métal et cristal du coût de chaque unité détruite des deux camps, total arrondi à l'inférieur. Les défenses détruites comptent toutes, reconstruites ou non.
- `Map::addDebris()` ajoute au champ ; aucune expiration dans `Universe/Domain/Entity/Map.php`. Destruction de lune : aucun appel à `addDebris` (`MoonDestructionResolver`).

Formation de lune (`MoonFormationResolver`, `Shared/Domain/ValueObject/MoonFormation.php`, `Game/Domain/ValueObject/MoonDiameter.php`) :
- Chance = min(D × max / Dmax, max), 0 si D < Dmax / max ; défauts 20 % et 2 000 000. Calculée sur les débris du combat (`battleDebris`), pas sur le champ. Impossible sans propriétaire, sur une planète abandonnée ou si la case a déjà une lune. Lune donnée au propriétaire de la planète. Champ non consommé.
- Diamètre : cases = 10 + X + 300 × p, X uniforme sur 0 à 10, p = max(0,01 ; min(1, chance / max) × 0,20) ; diamètre = floor(1 000 × √cases), de 3 605 à 8 944 km ; cases max = floor((diamètre / 1 000)²). Publié comme règle (11 tailles équiprobables) : c'est l'issue affichée dans le rapport, pas un mécanisme caché.
- Redline : 30 % / 0 % et 20 % pour 2 000 000 (§2).

Reconstruction des défenses (`Base::sufferBattleDamage()`, `DefenseRepairRate`, `DynastyTraits`) :
- Tirage indépendant par unité, après tout combat (victoire, défaite ou nul) et aussi dans la destruction de lune. 70 % (`STANDARD_PERCENT`), L'Héritage +5 (`NOTHING_IS_LOST_DEFENSE_REPAIR_POINTS`), talents +15 points au plus (`PlayerBonuses::DEFENSE_REPAIR_POINTS_CEILING`), plafond 85 % (`CEILING_PERCENT`). Terre brûlée (Amiral) baisse ; Ligne reformée (Vétéran) : 100 % ; Les dômes d'abord et Rideau léger : toujours reconstruits.
- Missiles (`MissileStrikeResolver`, `Base::sufferMissileStrike()`) : pas de reconstruction gratuite, sauf talent `missileStrikeRepair`.

Station de réparation (`RepairDock`, `Base::salvageShipWreckage()`) : appelée par `sufferBattleDamage()` après **tout** combat où le défenseur perd des vaisseaux, quel que soit le résultat (constaté aussi dans le lot Économie).

Destruction de lune (`MoonDestructionResolver`, `MoonDestructionOdds`, `FleetComposition::hasOnlyColossi()`, `FlightPlan`) :
- Flotte de Colossus seulement (`INVALID_DESTROY_COMPOSITION`), cible lune (`DESTROY_REQUIRES_MOON`) ; proposée seulement si l'attaque l'est (`AllowedMissions`).
- Tirages sur victoire seulement ; N = Colossus restant après les pertes du combat ; chances (100 − √S) × √N plafonné à 100 et √S / 2 ; Briseur de lunes × (1 − réduction) sur le risque ; La lune tient × 0,75 sur la chance (`resistedBy()`).
- Ni pillage, ni débris, ni formation de lune ; défenses de la lune soumises à la reconstruction. Flottes redirigées vers la planète (`RerouteFleetsOnMoonDestroyedHandler`), points retirés (`DeductMoonPointsHandler`). Rapport `moon_destruction_report` déclinable (`DeclinableReport`).

Rapport de combat (`AttackCombatResolver::fileReports()`, `BattleReportDisclosure`) :
- Un rapport par camp ; aucun pour le défenseur d'une planète abandonnée. Origine de l'attaque donnée aux deux camps. `battle_report` n'est pas dans `DeclinableReport` : toujours reçu.
- Vue partielle de l'attaquant : unités adverses croisées (`EngagementRecorder`), restes du défenseur par round retirés.
- Lignes propres au défenseur : `salvaged`, `forewarnedGuard`, `garrisonRecovered`, `defenseLossRefund`, `warPrize` ; à l'attaquant : `recycled`, `towed`, `raptors`, `secondWave`, `raidEye`.
- Partage dans l'alliance : 30 jours dans le canal (texte du front `notifications.json`, `share.retentionNotice`). Lien public : `battleShowcase.json` (contenu montré et masqué, 10 par 24 h, adversaire prévenu).

Simulateur (`SimulateBattleHandler`, `SimulationAssumptions`, `DeclaredDefender`, `SimulationLimits`, `config/services.yaml`) :
- Rapport refusé s'il n'a pas atteint le palier Flotte (`SpyReportTooShallowException`) ; défenses non vues = vides ; recherches non vues = celles de l'attaquant sans ses talents (`withoutTalents()`, la Doctrine de l'attaquant reste).
- Le défenseur combat sans talents ; l'attaquant avec `CombatModifiers::of($bonuses)` et ses recherches réelles.
- Limites : 5 000 000 unités par camp, 50 itérations, 10 000 000 déploiements. Le front envoie 50 itérations (`SimulatorPage.tsx`, `SIMULATION_ITERATIONS`).
- Débris moyen au taux de l'univers ; Butin prévu et Bilan de chasse réservés à des talents.
- ⚠️ Écart du jeu (à remonter à l'équipe, §11.9) : l'aide dit « Un champ laissé vide vaut ma recherche réelle, jamais zéro » (citation, ponctuation adaptée), mais dès qu'un champ de recherche est rempli, le front n'envoie que celui-là et `CombatResearch::fromMap()` compte les deux autres à 0 (et sans Doctrine ni talents). Le wiki conseille de remplir les trois champs sans parler du défaut.

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

## Espionnage (code, 15 octobre 2026)

Relevé dans `astro-nova-backend` main 7b255c83 (lecture seule), le front `Astro-Nova-React` origin/main (libellés) et la base migrée (SELECT). Pages générées par `tools/espionage_pages/` (constantes dans `esp_lib.py`). Remplace §11.5 là où ils diffèrent.

**Niveau effectif** (`Game/Domain/Service/EffectiveEspionageLevelCalculator.php`)
- `max(0, (espA − espD) + min(MAX_PROBE_BONUS = 5, floor(sondes / PROBES_PER_BONUS = 2)) + talentLevels − mufflingLevels)`. `talentLevels` / `mufflingLevels` : talents de dynastie (`PlayerBonuses::espionageDepthLevels()` / `espionageMufflingLevels()`), qui ne jouent **pas** sur le risque. *Sondes économes* compte des sondes en plus, sans dépasser le plafond.
- `espA` et `espD` (`SpyDetectionOdds::attackerLevel()` / `defenderLevel()`) = Renseignement Tactique + `AllianceBonuses::espionageAttackLevels` (Réseau d'informateurs) / `espionageDefenseLevels` (Contre-espionnage fédéré). Ces niveaux d'alliance entrent **à la fois** dans le niveau effectif et dans le risque. Cible inhabitée : `espD` = 0.
- Paliers (`ValueObject/EspionageTier.php`) : ressources 1, flotte 3, défenses 5 (défenses et missiles), bâtiments 7, recherches 9. `EspionageReach` : des talents ouvrent la flotte et les ressources plus tôt.

**Contre-espionnage** (`Service/CounterEspionageCalculator.php`, `Service/SpyDetectionOdds.php`, `ValueObject/SpyDetectionModifiers.php`)
- `clamp((2 × espD − espA) × vaisseaux × RISK_PER_SHIP = 0,05, MIN_CHANCE = 5, MAX_CHANCE = 25)` ; 0 si aucun vaisseau (sauf talent *Orbite gardée*), si `2 × espD − espA ≤ 0`, si la cible est inhabitée, abandonnée ou en vacances. Vaisseaux comptés sur le corps visé (planète ou lune), et l'autre corps de la case avec *Sentinelles de lune*. Points des talents ajoutés avant la borne.
- `probesShotDown()` : un tirage pour la vague ; prise, toutes les sondes tombent sauf `floor(sondes × survie %)` (talents). Les chances du second tirage (identifié / localisé, `SpyMissionResolver`) ne sont **pas** publiées dans le wiki (`spy-05`).

**Mission** (`Service/SpyMissionResolver.php`, `ValueObject/FlightPlan.php`, `ValueObject/AllowedMissions.php`, `ValueObject/FleetMission.php`, `Application/Command/SendFleet/SendFleetHandler.php`)
- Éclaireurs seuls (`INVALID_SPY_COMPOSITION`) ; jamais sa propre planète (`CannotSpyOwnPlanetException`) ; pas d'espace lointain (`DEEP_SPACE_TARGET`) ; planète ou lune (`fleet->target()->kind`). Autorisé sur joueur protégé et allié ; retiré pendant une maintenance (`isIntrusive()`) ; aucune mission pour un joueur lui-même en vacances (`AllowedMissions::none()`).
- Hydrogène facturé : `max(0,5 ; 1 − niveau × 0,05)` × consommation, arrondi par défaut (`SendFleetHandler`, ligne « Espionage runs cheap »).
- Ressources de la cible mises à jour à l'heure d'arrivée (`updateResources(force)`), dégradation d'abandon réglée avant lecture.
- Alerte au défenseur sauf planète abandonnée, joueur en vacances ou `DeclinableReport::INTRUSION_ALERT` refusé (préférences de rapports, `ReportPreferencesSection.tsx`). Niveaux `IntrusionDetection` : undetected / identified / traced ; libellés « Auteur inconnu », « Auteur identifié », « Origine localisée » ; « Sonde repérée sur … » sans nom (`notifications.json`).
- Rapport : `probes.sent` / `probes.destroyed` (« N sondes perdues sur M ») ; `pruneSpyHistory(keep: SPY_HISTORY_KEPT = 10)` par cible.
- Découverte : `SpyDiscovery` du joueur et, s'il est dans une alliance, de l'alliance (ALL-306). `FULL_DISCOVERY_LEVEL = 10` fait passer le statut de `spied` à `discovered`, mais aucune expiration n'existe et le front traite les deux pareil (`PlanetModal.tsx` : `isSpied = status === 'spied' || 'discovered'`) : **pas d'effet visible**, règle « au niveau 10, la case reste découverte » retirée de P-71.

**Rapport** (`Service/SpyReportGenerator.php`, front `ReportContent.tsx`)
- Toujours : type (biome), taille, cases libres, températures ; pour une lune, diamètre et cases de la lune, températures de la case.
- Inhabitée : `status: uninhabited`, toutes sections nulles. Abandonnée : pas de propriétaire, `abandonedSinceDays`. Vacances : propriétaire nommé, toutes sections nulles.
- Missiles listés à part des défenses (même palier 5). Section nulle affichée « Niveau d'espionnage insuffisant », section vide « Aucun élément détecté » (`notifications.report.locked` / `none`).

**Vision partagée d'alliance (ALL-306)** (`ValueObject/PlanetVision.php`, `ReadModel/MapReadModel.php`, `Application/Command/ShareSpyDiscoveriesWithAlliance/`, `Alliance/Domain/ValueObject/AllianceQuarantine.php`, `Service/SpyReportRequirementChecker.php`)
- Chaque espionnage d'un membre crée la découverte côté alliance ; en rejoignant (ou en fondant), les découvertes du joueur sont fusionnées dans celles de l'alliance. Hors du délai d'installation de 24 h (commentaire d'`AllianceQuarantine`), retirée au départ. Pas de date ni de contenu de rapport partagés (`lastSpiedAt` nul si `visionSource = alliance`).
- Front : badge et ligne « Découverte par un membre de l'alliance » / « Discovered by an alliance member » (`pages/planet.json` `allianceVision`, `allianceDiscoveredBy`).
- Colonisation et recyclage : exigent une découverte du joueur **ou** de son alliance (`TARGET_NOT_SPIED`, `RECYCLE_TARGET_NOT_SPIED`).

**Talents d'alliance** (table `alliance_talent`, migration `migrations/2026/10/Version20261010090000.php` ; `Alliance/Domain/Service/AllianceMemberBonuses.php`)
- `informant_network` « Réseau d'informateurs » / « Informant network » et `federated_counterintelligence` « Contre-espionnage fédéré » / « Federated counterintelligence » : branche `intelligence`, `max_level` 3, `effect_per_level` 1 (niveau entier), coût 300 000 / 150 000 / 50 000 × 2, 1 point de doctrine. Bonus actif après `alliance_quarantine_hours: 24` (`config/services.yaml`).

**Phalange de capteur** (`Game/Domain/Entity/Base.php` `scanWithPhalanx()`, `phalanxSweepCost()`, `PHALANX_SCAN_COST = 5000` ; `ValueObject/PhalanxRange.php` ; `ValueObject/Distance.php` ; `FleetDoctrineRepository::findPhalanxSweepOn()` ; `ReadModel/FleetReadModel::fromPhalanxSweep()`)
- Bâtiment `sensor_phalanx` (table `building`) : coût 20 000 / 40 000 / 20 000, multiplicateur 2, `max_level` NULL, `scope` moon (migration `2026/09/Version20260918090000.php`) ; prérequis `lunar_base` 1 (`2026/09/Version20260921090000.php`). Base lunaire : même coût, aucun prérequis.
- Portée `max(1, niveau² − 1)`, −1 si non construite ; même galaxie ; distance de systèmes **par le plus court côté de l'anneau** (`Distance::roundTheRing`, la carte boucle sur galaxies et systèmes, pas sur les positions).
- Refus avant paiement : pas une lune, cible lune, pas de phalange, hors portée, hydrogène insuffisant ; vacances du scanneur refusées dans `ScanWithPhalanxHandler`.
- Flottes vues : statut `traveling`, `returning` ou `exploring`, départ ou destination = la **planète** de la case (la lune seulement avec un talent de l'Oracle), missions `spy` et `recycle` exclues ; cargaison nulle. Pas de notification au joueur balayé, sauf talent de l'Ombre *Lumière dans le dos* (`NotifyPhalanxSweepHandler`).
- Libellés : « Phalange de capteur » / « Sensor phalanx », « Base lunaire » / « Lunar base » (`buildings.json`).

**Univers** : aucun réglage propre à l'espionnage. Seul le nombre de systèmes par galaxie (fixé à la création, `nbRegions`, 99 sur Redline) change le bouclage de la portée de la phalange.

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
- L'inactivité ne s'accumule pas pendant les vacances. **Nuance (code, 15 octobre 2026)** : sans effet pour les attaques, mais la succession du fondateur compte les jours de vacances (voir le relevé ci-dessous).

**Inactivité**
- Un seul palier, paramètre d'univers : **14 jours** par défaut, **7 jours** sur Redline (`players-10`, confirmé le 2026-10-06 : 7 jours constatés, conforme à `inactivityDays: 7`).
- Effet : perte de la protection des débutants, attaquable par tous quel que soit l'écart de points.
- Pas de suppression de compte, pas d'abandon automatique des planètes. Indicateur d'inactivité dans la galaxie : **ne pas en parler** dans le wiki tant qu'il n'est pas affiché.
- Alliance : un fondateur silencieux est alerté à 7 et 12 jours et perd son siège à 14.

**Alliances**
- Capacité selon la Diplomatie Stellaire **du fondateur** : 10, 15, 20, 25, 30, 35, 40, 50 membres aux niveaux 1 à 8. Niveau 1 requis pour fonder (donc Centre d'innovation 5 et Calcul Quantique 4 ; le Centre logistique n'est plus requis, `economy-10`). Une capacité acquise ne redescend jamais. Talent Ambassades : +2 sièges par niveau sur 3 niveaux, soit 56 au maximum.
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
| Centres d'innovation en réseau (nom affiché ; « Laboratoires en réseau » avant le 15 octobre 2026) | Science | 4 | +5 % de vitesse de recherche |
| Doctrine d'armement | Science | 1 | +5 % de puissance de feu (vaisseaux et défenses) |
| Doctrine de protection | Science | 1 | +5 % de boucliers et de coques |
| Réseau d'informateurs | Renseignement | 3 | +1 niveau d'espionnage pour vos sondes |
| Contre-espionnage fédéré | Renseignement | 3 | +1 niveau d'espionnage en défense |
| Ambassades | Diplomatie | 3 | +2 sièges |
| Parole tenue | Diplomatie | 3 | +1 point de fair-play par jour de pacte respecté |

- Points de doctrine : 2 par niveau d'alliance de 1 à 5, puis 1 par niveau ; plafond 50 points au niveau 45.
- Passer du niveau n au suivant : 10 000 + 2 500 × (n − 1) points d'expérience.
- Expérience d'alliance : constructions (20 × niveau), recherches (40 × niveau), combats gagnés (5 pour 1 000 **ressources** de valeur militaire détruites, soit 5 par point de score ; vainqueur seul, rien sur un match nul, pertes rattrapées par la remise en état des défenses ou la Station de réparation exclues, `Base` l. 7140-7190 ; `AllianceExperiencePolicy::forMilitaryDestroyed()` et `CreditAllianceExperienceHandler`, Backend#595, commit `1c0abe1`, relevé le 17/10/2026 ; avant ce correctif le barème s'appliquait à des points de score, soit 5 par million de ressources), rapports d'espionnage (10), recyclage (2 pour 1 000), missions d'alliance. Plafond glissant sur 7 jours : 800 par membre, 15 000 par alliance.
- Branche Logistique offensive : fermée, réservée aux futures attaques groupées.

**Règlement** (`players-09`)
- **Aucun règlement publié.** Seule mention : « le multi-compte est interdit par les conditions d'utilisation » (écran de parrainage). Le lien « conditions d'utilisation » de l'écran de connexion mène à une page inexistante.
- Sitting et push : ni mentionnés ni détectés. Aucun mécanisme de bannissement, de suspension ou de détection d'IP partagée.
- Sanctions techniques existantes : filtres du chat (sans mute), récompense de parrainage versée seulement quand le filleul atteint 100 points.

#### Relevé dans le code (15 octobre 2026)

Backend `origin/main` 7b255c83 (lecture seule), front `origin/main` 33217140 (libellés), catalogue du MySQL de dev migré (tables `ship`, `defense`, `building`, colonne `base_cost`). Les pages de la rubrique sont régénérées par `tools/players_pages/p_*.py` (constantes dans `players_lib.py`). Ce relevé remplace les lignes périmées ci-dessus quand elles divergent.

**Points et classements**
- 1 point = (métal + cristal + hydrogène) / 1 000 du **coût de catalogue** (`Constructable::getTotalCost()`, `getPoints()`) ; l'énergie est exclue ; le coût réellement payé (réductions) n'intervient pas.
- Bâtiments : à la fin d'un niveau N, + points du niveau N (`Construction::getEarnedPoints()`) ; démolition : − points du niveau démoli (`WheneverConstructionFinished/UpdateUserPointsHandler`). Recherches : bucket RESEARCH. Niveau offert : points du niveau (`WheneverBuildingLevelBonusGranted/UpdateUserPointsHandler`).
- Vaisseaux et défenses : + à chaque lot livré (`AbstractUnitDeliveryPointsHandler`). **Aucun filtre sur les vaisseaux civils** : tous comptent dans le militaire, aussi dans `Fleet::loseShips()`, `Base::shipPoints()` et `RecalculateUserPointsHandler`. **Corrige** l'ancienne règle « les transporteurs ne comptent pas » (`players-01`, P-81, et `fleet/ships` règle 7, rubrique Flotte).
- Baisses : `DeductLostShipsPointsHandler`, `DeductBaseUnitsPointsHandler` (vaisseaux remorqués par la Station de réparation et défenses remises en état exclus, `Base` l. 7190-7300), `DeductFiredMissilesPointsHandler`, `StripAbandonedBasePointsHandler` (économie + militaire, recherche gardée), `DeductMoonPointsHandler`. Hausses : `AddFoundShipsPointsHandler` (expédition), `CreditRecolonizedBasePointsHandler`.
- Total = économie + recherche + militaire (`UserUniverse::addPoints()` / `refreshTotal()`, `PointsBreakdown`) ; affichage et protection : partie entière (`Point::rounded()`).
- Classement en direct, ordre `points DESC, user_id ASC` (`RankingDoctrineRepository::liveRanking()`), progression comparée au dernier `ranking_snapshot` (photographie quotidienne, `app:snapshot-rankings` ; heure de passage non versionnée dans le dépôt). Filtre Humains : rang calculé sur tout l'univers puis filtré.
- Alliance Puissance = somme des `points` des membres ; Progression = expérience d'alliance, à égalité `levelReachedAt` (`AllianceRankingCategory`, `AllianceRankingDoctrineRepository`).
- Libellés : `pages/ranking.json` (Points, Économie, Recherche, Militaire, Alliance Puissance, Alliance Progression, Humains, « Joueur IA (PvE) »).

**Protection des débutants** (`Shared/Domain/ValueObject/BeginnerProtection.php`, `BeginnerProtectionTier(s)`, `Game/Domain/Service/BeginnerProtectionChecker`)
- Défaut : paliers (500, 1:3), (5 000, 1:5), (500 000, 1:10), `inactivityDays` 14. Redline : mêmes paliers, 7 jours (§2, `players-10`).
- Blocage si `plus fort >= plus faible × ratio` (égalité exacte bloquée), palier pris sur le plus faible (`points < upToPoints`), symétrique ; plus faible à 0 point : bloqué contre tout joueur > 0 ; deux joueurs à 0 : permis.
- Seule l'inactivité du défenseur lève la protection (`blocksAttack(defenderInactive)`) ; joueurs IA jamais inactifs (`User::isInactiveIn()`).
- Contrôlée pour l'attaque (`SendFleetHandler`, mission ATTACK seulement) et la salve de missiles (`LaunchMissilesHandler`). La destruction de lune n'est pas contrôlée à l'envoi mais retirée de la galaxie quand l'attaque l'est (`AllowedMissions::forTarget()`, `attackBlocked`).

**Protection nouvel arrivant** (`User/Domain/ValueObject/NewcomerProtection.php`, `NewcomerProtectionChecker`)
- `DURATION_DAYS = 7`, **constante**, pas un paramètre d'univers : aucun champ dans `Universe`, `UniverseSetup` ni l'écran de création d'univers. **Corrige** `patch-01` et §10.
- Comptée depuis la première arrivée (`UserUniverse.joinedAt`, jamais renouvelée). Rompue définitivement par l'envoi d'une mission ATTACK (`FleetMission::engagesNewcomerShield()`, `recordDeparture()`) ou d'une salve (`LaunchMissilesHandler` l. 193), quelle que soit la cible (planète abandonnée comprise). Refuse l'attaque et la salve contre le protégé ; espionnage, transport, etc. libres. Joueurs IA : aucune (`User::getNewcomerProtectionIn()`).
- Ordre des contrôles à l'envoi : vacances, alliés, nouvel arrivant, débutants, limite d'attaques (`SendFleetHandler` l. 185-305) : les deux protections se cumulent (`patch-01`, seconde partie).
- Non décalée au dégel d'un univers privé (`DbalFrozenClockShifter` ne touche pas `joined_at`).
- Libellés : `newcomer.json` (« Protection nouvel arrivant », badge « Nouveau joueur », « Attaquer et désactiver mon bouclier »).

**Limite d'attaques** (`BashingRule`, `Game/Domain/Entity/AttackTally.php`)
- Défaut 6 attaques / 24 h (`BashingRule::default()`), Redline 6 / 24 (§2) ; `maxAttacks` 0 désactive.
- **Tranche fixe** malgré la docblock de `BashingRule` (« rolling window ») : `AttackTally::registerAttack()` remet le compteur à zéro quand `now >= windowStartedAt + windowHours` et rouvre la tranche à cette attaque. Une ligne par (univers, attaquant, défenseur).
- Comptées : mission ATTACK (`SendFleetHandler`, `$defender` seulement si ATTACK) et salves (`LaunchMissilesHandler`). Non comptées : espionnage, transport, recyclage, **destruction de lune**. Rappel d'une attaque : `refund()` (`RecallFleetHandler`). Planète abandonnée : pas de propriétaire, pas de compteur. Boss d'événement exclu (non publié).
- Quota affiché par défenseur dans la galaxie (`MapReadModelAssembler`, `AttackQuota`).

**Mode vacances** (`User/Domain/ValueObject/VacationMode.php`, `VacationBlocker`, `StartVacationModeHandler`, `EndVacationModeHandler`, `VacationShieldChecker`)
- `MINIMUM_HOURS = 48` ; pas de maximum, pas de fin automatique, pas de délai entre deux périodes ; par univers.
- Blocages : `FLEET_IN_MOVEMENT`, `CONSTRUCTION_IN_PROGRESS` (bâtiment, recherche, vaisseaux, défenses), `UNDER_ATTACK`.
- Production soldée au départ puis à zéro (`EmpireProductionSettler`, `ProductionModifier::VACATION_HALT`) ; soldée à zéro au retour.
- Le joueur absent ne peut rien changer (`User::ensureNotOnVacationIn()` : ordres, annulation, démolition, flotte, salve, Phalange, convoi d'alliance) ; lecture libre (galaxie, rapports, chat, alliance).
- Missions refusées contre lui : ATTACK, DESTROY, TRANSPORT (`FleetMission::reachesTargetOwner()`) et salves ; espionnage permis, rapport réduit à « propriétaire absent » ; recyclage permis.
- **Inactivité** : `last_active_at` n'est ni gelé ni remis pendant les vacances ; il est rafraîchi par toute requête authentifiée dans l'univers courant (`PlayerActivityTrackerSubscriber`, au plus toutes les 15 min). Sans effet sur les attaques (le joueur est intouchable), mais **la succession du fondateur compte les jours de vacances** (`AllianceDoctrineRepository::findWithFounderIdleSince()` ne filtre que les univers suspendus). Nuance `players-05`.
- Univers privé gelé (`SuspendUniverseHandler`, `RecallIntrusiveFleetsHandler`, `SuspendedUniverseGuardMiddleware`, `DbalFrozenClockShifter`) : vacances pour tous, attaques, espionnages et destructions en vol rappelés (créneau rendu), lecture seule ; au dégel, décalage de `last_active_at`, échéances de votes, préavis de pactes, demandes d'aide, conservation des rapports ; pas des cycles de missions d'alliance ni de la fenêtre du canal d'alliance.
- Libellés : `vacation.json`.

**Inactivité**
- `BeginnerProtection::isInactive()` : inactif si `lastActiveAt < now − inactivityDays` ; 0 désactive. Toute requête authentifiée compte, pour l'univers courant seulement (`PlayerActivityTrackerSubscriber`, `player_activity_refresh_interval` 900 s).
- Succession du fondateur : alertes 7 et 12 jours, perte du siège à 14 (`config/services.yaml` `alliance_succession_*`), indépendante de l'univers.
- Indicateur « Inactif » : désormais affiché sur la fiche joueur (`PlayerCardModal.tsx`, `pages.ranking.card.inactive`) et calculé pour la galaxie (`MapReadModel::$isInactive`). **Non publié** dans le wiki (`text-01`), question `players-14`.

**Messagerie** (`src/Chat/`)
- Canaux GENERAL, ALLIANCE, PRIVATE (`ChatChannel`). 500 caractères (`MessageBody::MAX_LENGTH`). Anti-flood 5 messages / 60 s (`chat_spam_max_messages`, `chat_spam_window_seconds`, `SpamPolicy`). Liens refusés, termes interdits (liste non publiée). Réactions : palette fermée de 10 (`ReactionEmoji`). Mentions `@pseudo` (`MentionHandle`). Traduction (LibreTranslate). Blocage (`messages.json` `blockConfirmMessage`). Mise en sourdine par la modération (`ChatMute`).
- Canal d'alliance : 30 jours glissants (`alliance_chat_retention_days`) ; général et privé non purgés (`AllianceChatRetention`). Épingles : 3, fondateur et vice-présidence (`messages.json` `errors.pin*`).
- Cartes (`ChatCardType`) : rapport d'espionnage, rapport de combat, coordonnée, contribution, projet collectif, mission d'alliance (canal d'alliance seulement) ; combat exposé partout. Attaque groupée déclarée mais sans fonctionnalité (non publiée).

**Rapports**
- Conservation **7 jours** depuis la création, lu ou non (`player_report_retention_days`, `ReportRetention`). Nouveau dans le wiki.
- Partage : `keptUntil` = partage + 30 jours (`ExtendSharedReportRetentionHandler`, `AllianceChatRetention::keepUntil()`), lisible aussi dans l'historique du destinataire (`PlayerReportDoctrineRepository` l. 367). Suppression d'un rapport partagé : retiré de l'historique, gardé jusqu'au plus tard de `keptUntil` et suppression + 7 jours (`shared_report_grace_days`, `DeletePlayerReportHandler`, `SharedReportGrace`).
- Réglages : `DeclinableReport` (tous les types sauf espionnage et combat, retours par mission), `ReportPreferencesSection.tsx` (groupes, libellés, colonnes « Rapport » et « Notif. »), `pages/settings.json` (`reports`, `incidentsNote`).

### 11.8 Divers
- Parrainage : récompense versée quand le filleul atteint **100 points** (`misc-03`, montant à confirmer).

### 11.9 Textes du jeu à corriger (à remonter à l'équipe)

| Où | Texte actuel | Problème |
|---|---|---|
| Expéditions | « Plus la flotte reste, plus elle a de chances » | La durée ne change pas les probabilités (`fleet-06`) |
| Aide, Boutique et Points stellaires (PvP) | « aucun avantage de jeu » | Le Premium (files plus longues) s'obtient en Points stellaires (`patch-02`) |
| Nom du bâtiment `planetary_base` (FR) | « Base planetaire » | Accent manquant |
| Écran de connexion | Lien « conditions d'utilisation » | Page inexistante (`players-09`) |
| Alliance, station (`pages.alliance.station.levelGrantsPoint`, FR et EN) | « chaque niveau donne 1 point de doctrine » | Le code en donne 2 par niveau du niveau 1 au niveau 5 (`AllianceExperience::pointsAt()`) |
| Boutique (`components/shop.json` `categories.stellar`, `topUp`) | « Crédits », « Ajouter des crédits » | Homonyme des Crédits de la Banque stellaire, qui ne s'achètent pas (`bank-01` : le responsable laisse tel quel, 15 octobre 2026) |

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
- Ultime : branche pleine au-dessus ; niveau 40 en plus pour l'arbre commun seulement (relevé du 15 octobre 2026).
- Brouillon puis validation ; un point validé ne se reprend que par réinitialisation. Réinitialisation par arbre : la 1re gratuite, ensuite 20 Points stellaires et 24 h depuis la précédente.

### Plafonds (talents / total avec l'alliance)
- Vitesse de flotte : commun 40 %, accent 10 %, talents 50 %, total 60 %. Les bonus de vitesse divisent la durée. Vent arrière (25 %), Liaisons internes (40 %), Retour victorieux (30 %) hors budget.
- Hydrogène : commun 20 %, accent 5 %, talents 25 %, total 45 %. Soutes 25 %. Flottes en vol +3.
- Recherche 25 / 45 %. Mines 25 / 45 %. Bâtiments 25 / 45 %, accent 15 % sur une famille (50 % au total). Vaisseaux et défenses 10 %, accent 15 %. Coûts 5 % (accent). Cases +4. Pillage des cibles abandonnées +20 points. Protection contre le pillage 20 points au catalogue (15 pour le Vétéran, 10 pour l'Oracle), taux de pillage jamais sous 30 %.
- Combat : armement des vaisseaux 9 %, coque 13 % (15 octobre 2026), bouclier 3 % ; défenses : armement 9 %, bouclier 5 %, coque 10 % ; dégâts sur tirs rapides 15 % (trait compris).

### Arbre commun
Valeurs par rang (code `CommonTalents`), identiques au document de conception : voir la page `dynasty/common-tree`. Astrométrie touche la catégorie « exploration » : Renseignement Tactique et Cosmologie Appliquée.

### Arbres de classe
Valeurs par rang tirées du catalogue de chaque classe (`AdmiralTalents`, `BuilderTalents`…) et des plafonds de classe (`ClassCaps`). Écarts avec le document de conception, retenus d'après le code : Lire la coque 3,5 %/rang, Feu concentré 7,5 %, Contre-batterie 2 %/rang, Premier rang 3 %/rang, coque de l'Amiral plafonnée à 13 % (relevé du 15 octobre 2026 ; 11 % auparavant).

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

### Relevé dans le code (15 octobre 2026, réécriture de la rubrique)

Source : dépôt Backend `origin/main` 7b255c83, en lecture seule. Le catalogue est exporté par `tools/dynasty_pages/export_talents.php` (TalentTree, TalentKey, TalentTreeRules, ClassCaps, PlayerBonuses, PlayerExperience, DynastyTraits, TalentRespec, ClassChangeAllowance) dans `tools/dynasty_pages/talents.json` ; les textes du client (`talents.json`, `dynasties.json`, `classes.json`, `pages/talents.json`, FR et EN, Frontend `origin/main`) dans `tools/dynasty_pages/labels.json`. Les pages de la rubrique sont générées par `tools/dynasty_pages/p_*.py` ; les textes propres à chaque classe (`t_<classe>.py`) ont été vérifiés nœud par nœud dans le code (notes de vérification gardées hors dépôt).

- **Arêtes** (`PlayerTalents`, `SpentTalents::hasFullParent`) : un nœud demande que le nœud au-dessus de lui, dans sa branche, soit plein. Une branche se remplit de haut en bas.
- **Ultime** (`TalentKey::requiredLevel`) : niveau 40 et branche pleine au-dessus **dans l'arbre commun seulement** ; un ultime de classe ne demande que sa branche pleine (15 points, maîtrise 29). Corrige « Ultime : niveau 40 et branche pleine » ci-dessus.
- **Choix de l'arbre commun** : rangées 3, 6 et 8 en Prospérité et Exploration ; en Logistique, rangées 3 et 6 seulement (la rangée 8, Chargement prioritaire, est une clé). `tools/talent_diagrams.py` lit désormais la forme des arbres dans l'export.
- **Points de classe** : `min(25, intdiv(maîtrise + 1, 2))` (`TalentBudget::classPointsOf`) : 5 points dès la maîtrise 9, 12 dès 23, 15 dès 29.
- **Maîtrise** (`UserUniverse::selectCharacter`, `ClassTenure`) : la première classe entre à la maîtrise 1 avec l'expérience comptée depuis 0, donc au niveau du joueur même choisie tard. Plafond : niveau du joueur et 50.
- **Expérience** (`PlayerExperience::earnedByRecord`, `UserUniverse::refreshTotal`) : 10 par point gagné au-delà du record de points, divisé par la vitesse d'**économie** de l'univers (défaut ×1, Redline ×1) ; perdre des points ne retire rien.
- **Verrous** (`TalentTreeLocks`) : réinitialisation et changement de classe refusés tant qu'une flotte ennemie arrive ou qu'une de vos flottes de combat est à l'aller ; changement de classe refusé aussi en vacances. Un arbre vide ne se réinitialise pas (rien facturé).
- **Builds enregistrés** (`User::ensureTalentBuildsAvailable`, `applyTalentBuildIn`, `TalentBuildSlot::FREE_SLOT_COUNT = 2`, nom de 32 caractères au plus) : enregistrer et appliquer un build sont réservés au Premium ; appliquer est gratuit, hors flotte ennemie en approche, flotte de combat à l'aller ou ordre en production ; lire un lien partagé est ouvert à tous. **Non publié** : point commercial à arbitrer (`dynasty-21`).
- **Traits** (`DynastyTraits`, `PlayerBonuses`) : La rotation Halden (+2 %) et Le diapason (+5 %) s'ajoutent après le plafond de classe (production talents et trait jusqu'à 27 %, plafond total 45 % inchangé ; dégâts 15,5 % pour un Amiral de L'Accord). Rien ne se perd : remboursement 80 → 85 % (plafond 95 %), reconstruction 70 → 75 % (plafond 85 %). Écouter loin : section flotte au niveau d'espionnage effectif 2 au lieu de 3 (`EspionageTier::FLEET = 3`). Le Chœur : `DynastyKey::isPlayable()` faux, aucun trait, classes sans arbre ni nom affiché par le client.
- **Plafonds partagés** (`PlayerBonuses`) : flotte commun 40, accent 10, talents 50, total 60 % ; hydrogène commun 20, accent 10 (Amiral, pondéré par la part des vaisseaux de combat), talents 30, total 45 % ; fret 25 % sans part d'alliance ; flottes +3 ; recherche 25/45 % (Astrométrie dans le même budget) ; mines 25/45 % ; colonies 10 % et jeunes colonies 25 % (mines) / 20 % (bâtiments) hors plafond ; Plasma 50 % ; énergie 15 % (8 % atteints) ; expéditions 20 % et −25 % ; stockage 20/40 % ; bâtiments 25/45 %, accent 15 % (50 % sur la famille : Bâtisseur 15, Énergéticien 10, Théoricien 9, Symbiote 10) ; vaisseaux et défenses 10 %, accent 15 %, sans part d'alliance ; coûts 5 % (Bâtisseur) ; cases 4 ; pillage des cibles abandonnées 20 points ; abri 20 points au catalogue, 15 Vétéran, 10 Oracle, taux jamais sous 30 %. Combat : coque des vaisseaux **13 %** (et non 11 %).
- **Arbre commun** (`CommonTalents`) : Fonderie à plasma **+50 %** (niveau de Plasma ×1,5, `Base::plasmaProductionBonus`), et non +20 % ; Arche = coût −25 %, construction +50 %, colonisations +25 % (sous les 60 %) ; Comptoirs pionniers +24 h de jeunesse par rang (fenêtre de 7 jours, jusqu'à 15 avec Jeunes mondes) ; seul Comptoirs pionniers lit l'état jeune ; Pont de ressources : 2 h de production de la planète de départ, trois ressources additionnées, 24 h glissantes pour l'empire ; Stock de sécurité : 25 % versés au-dessus de la capacité ; Archives volées : pillage d'au moins 1 h de production de la planète mère ; Flair de prospecteur : « rien » 33 → 22,11 %, « ressources » 33 → 43,89 % sur une case neuve ; cible abandonnée = ruine, bot ou joueur inactif depuis `inactivityDays` (14 par défaut, 7 sur Redline, `Base::isAbandonedTarget`). L'ultime d'Exploration s'appelle « Second centre d'innovation » dans le jeu.
- **Arbres de classe** : écarts relevés et corrigés dans les pages (Doctrine de coque +4 %, Économie de guerre −10 %, Percée 30 %, Casemates +30 %, Pointe +12 points et surrégime 131 %, Mise en route 30 jours, Éclair de génie plafonné à 6 h, etc.) : voir la description de la PR `rewrite-dynastie` et PLAN §7 (`dynasty-21` et suivantes).

### Rééquilibrage des classes (backend `main` 59b01c6a, relevé le 17 octobre 2026)

Source : Backend #583 (Bâtisseur, branche Filon et Achats groupés), #584 (Théoricien et Symbiote), #585 (Amiral), #587 (réinitialisations offertes) ; textes du client Frontend #1302 (`talents.json`, `a3b6e039`). Export refait avec `tools/dynasty_pages/export_talents.php` sur `59b01c6a`, libellés relus sur `a3b6e039`. **Pas encore en production au 17 octobre 2026** (branche `production` du backend à `458bc72d`, 2.27.0) : les pages ne sont poussées sur le wiki qu'à la sortie.

- **Bâtisseur** (`BuilderTalents`, `MineLevelBonus`, `PlayerBonuses`) : Première coulée 1 h, Grandes coulées 1 h par rang (4 h en tout, 9 h auparavant) ; Prospection 5 % par rang (15 %) et **une seule** mine du jour (`UserUniverse::drawProspection`, `count: 1`) ; Veine mère = +1 niveau de production sur la mine du jour, dès son premier niveau (`PROSPECTED_MINE_BONUS_LEVEL`) ; Double filon = −15 % sur l'amélioration de la mine du jour tant que son jour court (`CostReductionSource::PROSPECTED_MINE`, additive avec les autres réductions de bâtiment, prix calculé au lancement) ; Galeries = +1 niveau de plus sur la mine du jour à partir du niveau réel 30, seuil abaissé de 5 par rang (25, 20, 15) ; Carottage ×2 (le supplément vaut 1 × la production, `multiplier − 1`) ; Achats groupés = −10 % sur les défenses seulement, hors plafond de coût de la classe (`DEFENSE_COST_REDUCTION_CEILING`), les vaisseaux n'ont plus de réduction de cette source. Une mine gagne donc au plus 3 niveaux de production (lieu, Veine mère, Galeries).
- **Amiral** (`AdmiralTalents`, `LootRate::forAttacker`, `ClassCaps`) : Remorqueurs remplacé par **Part du butin**, +5 points de taux de pillage par rang (+15, soit 65 % sur une victoire), ajoutés avec les points des cibles abandonnées avant les abris du défenseur, toujours plafonnés par les soutes ; Percée prend 30 % de ce taux. Remorquage seul : 20 % (plafond de classe `attack_salvage` 50 → 20). Chantier de guerre : en plus, −5 % de coût par rang sur les vaisseaux de combat (−15 %), hors plafond de coût (`COMBAT_SHIP_COST_REDUCTION_CEILING`), additif avec les autres réductions du vaisseau.
- **Théoricien** : Protocoles 6 % par rang (−18 %, plafond `RESEARCH_COST_REDUCTION_CEILING` 18).
- **Symbiote** (`SymbioteTalents`, `SystemPosition::flooredAt`, `Base::talentedPosition`) : Racines = plancher de 15 % de bonus de position sur les mines de métal et de cristal de chaque planète, planète mère comprise, lunes exclues ; Lunes creusées = +5 points de plancher par rang (30 % au total, `POSITION_BONUS_FLOOR_CEILING`) et ne donne plus de cases lunaires (`lunarBaseFieldsPerLevel` supprimé, 3 cases par niveau de Base lunaire pour tous) ; Marcottage +90 % d'amplitude (plafond 90) ; Terre natale 35 % par rang (105 %) ; Sève montante 8 % par rang (24 %, Hôte au plus +56 %). Ordre : amplitude (Marcottage + Filon de métal ou Veine de cristal, +110 % au plus), puis part de la planète mère, puis plancher (`max`), qui n'est donc pas élargi.
- **Réinitialisations offertes** (`TalentRespec::withGranted`, `spendsGranted`, colonne `class_talent_granted_respecs`) : un rééquilibrage peut offrir des réinitialisations de l'arbre de classe en plus de la première ; gratuites, sans délai, consommées seulement après la première. La migration `Version20270104100000` en offre une à chaque joueur dont la classe est Bâtisseur au moment de la migration ; `Version20270104090000` efface les jours de Prospection tirés sur deux mines.
- Exemples recalculés (script hors dépôt) : Excavateur 21 mine du jour sur la planète mère au niveau de production 24, 7 091 métal/h ; colonie, Excavateur 15 au niveau 18, 3 002 ; Excavateur 25 connu, mine du jour, −45 % : 555 526 / 138 882 ; position 8 sur 15 : 35 × 1,9 = 66,5 %, 35 × 2,1 = 73,5 %, planète mère 35 × 1,9 × 1,05 = 69,825 % ; Hôte +47 % (1 896) et +67 % (2 704) sur un Excavateur 20 ; remorquage 37,8 % × 20 % = 7,56 % ; Protocoles 409 600 → 335 872.

## 19. Alliances (code du jeu, relevé le 15 octobre 2026)

Source : `astro-nova-backend` `main` au commit `7b255c83`, contexte `src/Alliance/`, réglages dans `config/services.yaml`, catalogues dans les migrations `2026/09/Version20260926090000`, `2026/10/Version20261010090000` et `2027/01/Version20270102120000` ; libellés : `Astro-Nova-React` `main` (`33217140`), `src/i18n/locales/{fr,en}/pages/alliance.json`.

**Membres et gouvernance**
- Capacité : `AllianceCapacity` (10 à 50), monte seulement quand le fondateur en place termine un niveau de Diplomatie Stellaire (`RaiseAllianceCapacityHandler`) ; capacité effective = capacité + sièges d'Ambassades (`Alliance::getEffectiveCapacity()`).
- Rangs (`AllianceRole`) : Fondateur, Vice-président, Officier, Membre, Recrue. Fonctions cumulables (`AllianceFunction`) : Diplomate, Stratège, Intendant, Recruteur, Coordinateur. 14 droits (`AlliancePermission`) ; un Officier n'agit que sur un rang inférieur (`AllianceRole::outranks`). Le droit « Mener les attaques groupées » (Stratège) ne mène encore à rien.
- Recrutement (`AllianceRecruitmentMode`) : ouverte, sur candidature (par défaut), sur invitation. Candidatures et invitations n'expirent pas.
- Intégration 24 h (`alliance_quarantine_hours`) : ni talents, ni aide, ni missions ; le vote, la vision partagée et l'interdiction du tir ami s'appliquent dès l'arrivée. Délai de 24 h après départ ou exclusion (`alliance_membership_cooldown_hours`), qui bloque aussi la fondation ; aucun délai après une dissolution.
- Succession (`alliance_succession_*`) : alertes **aux membres** à 7 et 12 jours, perte du siège à 14 ; successeur par rang puis ancienneté dans le rang, présent (vu depuis moins de 14 jours) et membre depuis 24 h ou plus ; sans candidat, rien ne change. Cession volontaire : même condition d'éligibilité.
- Renommage : 500 Points stellaires (nom et tag), description 50, payés par le membre qui agit (`alliance_rename_cost_stellar_points`, `alliance_description_cost_stellar_points`). Devise, couleur, écusson, bannière gratuits. Réservation du nom 30 jours, y compris pour celui qui a dissous.
- Dissolution (`DissolveAllianceHandler`) : canal effacé, demandes annulées, membres libérés sans délai, guerres archivées.
- Tir ami interdit (raid et missile) : `src/Game/Domain/Service/FriendlyFireChecker.php`.

**Pactes, fair-play, votes, guerres**
- Violation : 10 (non-agression) ou 15 (alliance) ; raids et missiles seulement ; plafond 30 points par jour (`alliance_pact_daily_violation_cost_cap`). Déclarer la guerre à un partenaire = violation et fin du pacte (`BreakAlliancePactOnWarDeclarationHandler`).
- Fair-play de 0 à 100, départ à 100 ; mentions (`AllianceFairPlayGrade`) : Exemplaire ≥ 90, Fiable ≥ 70, Douteuse ≥ 40, Peu fiable ≥ 15, Parjure. Gain : 1 + Parole tenue par jour et par alliance, s'il y a au moins un pacte qui engage et aucune violation ce jour-là (`AccrueAllianceFairPlayHandler`).
- Votes (`AllianceVote`, `Alliance::mayVote`, correctif Backend #554) : **tous les membres votent**, recrues comprises ; durée de 1 à 24 h choisie par l'auteur ; clôture anticipée par l'auteur ; égalité ou aucune voix = rejet. Pactes : vote facultatif, l'adoption envoie l'offre. Question libre : droit de diplomatie ou d'annonce, sans effet.
- Guerre : score = combats gagnés par chaque camp, attaque ou défense, nuls exclus (`CountWarVictoryHandler`) ; paix sans vote, acceptée par l'autre camp, ou fin par dissolution ; historique des guerres passées.
- Limite d'attaques : 6 attaques **contre un même défenseur** sur 24 h glissantes (`BashingRule::default()`), réglable par univers.
- Un membre en période d'intégration qui viole un pacte coûte 0 point à l'alliance, la violation restant inscrite (`AllianceFairPlayScorer::costOf`) : publié le 15 octobre 2026 sur accord du responsable (`players-13`). Non publiées : les fréquences des balayages internes.

**Trésorerie, entraide, station**
- Convois (`SendAllianceConvoyHandler`, `FleetMission::ALLIANCE_DEPOSIT`) : petits et grands cargos, base avec Dock orbital, vers la Station stellaire du système, 1 h aller et 1 h retour, sans hydrogène ni rappel, emplacement de flotte, refus en vacances et sous attaque annoncée (Backend #579). À l'arrivée, la trésorerie prend ce que le plafond permet, le surplus rentre (`AllianceConvoyArrivalResolver`).
- Plafond : 5 000 000 par ressource (`alliance_treasury_cap_per_resource`), ×2 par niveau de Soutes mutualisées, avec un plancher de 2 × le métal du palier 3 (`alliance_treasury_station_factor`), sans effet constaté : non publié.
- Vues : solde, plafond, ses propres versements, top 5 des donateurs, totaux donné et reçu par membre sur la liste des membres ; registre détaillé réservé à « Gérer la trésorerie ».
- Aide : 50 000 par membre (+50 000 par niveau de Réseau d'assistance), ×5 pour l'alliance, sur 24 h glissantes, une demande à la fois, expiration 24 h, livraison 1 h après l'accord (`alliance_aid_*`, `AllianceAidRequest::TRANSIT_SECONDS`).
- Station : 3 paliers (`AllianceStationTier`), prix = heures × production de référence de l'univers, 60/30/10, figé à l'achat (`AllianceStationPricing`). Les heures (150, 350, 700) et la référence (médiane des actifs) ne sont pas publiées : le jeu affiche le prix.

**Missions V2** (Backend #571, #572)
- Interrupteur d'univers `alliance-missions`, fermé par défaut, avec surcharge par alliance au BO (`AllianceMissionsGate`). **Ouvert sur Redline** (responsable, 15 octobre 2026, `players-12`). La surcharge par alliance n'est pas publiée.
- Cycles Europe/Paris ; 3 propositions quotidiennes et 5 hebdomadaires, une par famille ; repos 3 et 14 jours ; une mission par famille et par cadence à la fois ; inscriptions pendant 25 % du cycle ; objectif ×1,8 (Avancée), ×3,2 (Épique) ; 2,5 parts par membre (`memberCountedCap`).
- Clôture : 100 % réussite, ×1,25 à 150 %, ×1,5 à 200 %. Taux = 40 % médiane + 60 % production propre (métal + cristal + hydrogène, `ProductionRateReader`) ; effort relatif, 2,5 parts au plus (seuil de 30 % supprimé le 21 octobre 2026) ; versement 60/30/10, réclamation sous 7 jours, transit 30 min.
- **Réglage du 21 octobre 2026** (backend `feat/alliance-missions-tuning`, commit `bb82306f`, relevé avant fusion ; front `7cb27a18` pour les libellés) :
  - Plafond par jour (`AllianceMissionEconomy::dayCountedCap()`) : aucun pour une quotidienne ni pour une mission de participation ou fixe ; hebdomadaire en ressources ou en nombre : max(25 %, ⌈200 % / ⌈heures restantes au choix / 24⌉⌉) de l'objectif par 24 h depuis le choix (`alliance_mission_v2_daily_counted_percent: 25`, `AllianceMissionTiers::TOP_PERCENT = 200`). Lundi 29 %, mardi 34 %, mercredi 40 %, jeudi 50 %.
  - Choix d'une hebdomadaire fermé dans ses 3 derniers jours, soit à partir du vendredi 00:00 Paris (`AllianceMissionPolicy::selectionClosesAt()`, `alliance_mission_weekly_closing_days: 3`, exception `AllianceMissionSelectionClosedException`, 409) ; libellé front « jusqu'au jeudi minuit ».
  - Progression comptée contre l'objectif estimé pendant les inscriptions, plafonds compris (`RecordAllianceMissionProgressHandler`, `AllianceMissionCounting`).
  - Paliers (`AllianceMissionEconomy::tiersOf()`, `AllianceMissionTiers`) : ressources et nombre ×1 / ×1,25 / ×1,5 à 100 / 150 / 200 % ; participation : objectif, ⌈(objectif + inscrits) / 2⌉, tous les inscrits.
  - Entraide (`AllianceMissionFlows::shareableFor()`, `RecordAllianceMissionFlowHandler::share()`) : plus de déduction de ce que l'expéditeur a reçu ; seul un retour vers qui vous a envoyé est refusé ; plafond du receveur = ⌊25 % × sa production × durée de la mission⌋ moins ce qui a déjà compté vers lui, tous envoyeurs (`sharedRecipientRoom()`, `alliance_mission_v2_shared_recipient_percent: 25`) ; marge par membre affichée (`AllianceMissionRecipientReadModel`, libellés `missions.recipients.*`).
  - Objectif en nombre (`targetFor()`, mesure COUNT : Expéditions, Cartographie, Expansion, Victoire nette) × min(1, max(12, heures restantes) / heures du cycle) (`alliance_mission_v2_counted_floor_hours: 12`). Les objectifs en ressources suivent déjà la durée restante (`spanHours()`).
  - Récompenses : 4 h (quotidienne, `daily_reward_hundredths_of_hour: 400`), 16 h (hebdomadaire, `1600`), ×1,5 / ×2 ; plafond 7 jours glissants = min(72 h de taux, 40 % × production propre × 168 h) (`weeklyCap()`, `weekly_cap_hours: 72`, `weekly_cap_income_percent: 40`).
  - Compléments du 21 octobre (backend `1aa76a3e` à `47e05762`, front `c5533073`) : Casse et Victoire nette lisent la valeur frappée pendant le combat, réparations gratuites du défenseur comprises, soit la valeur du rapport (`BattleDamage::struck()`, `BaseAttackResolvedEvent::$attackerStruck`, `WheneverBaseAttackResolved/RecordAllianceMissionProgressHandler`) ; une mission par famille **et par cadence** (`AllianceMissions::ensureFamilyFree()`) ; plafond par jour cumulatif, au jour d (0 = les 24 premières heures) au plus (d + 1) plafonds en tout (`AllianceMissionContributions::counted()`) ; Expansion proposée en hebdomadaire seulement (`AllianceMissionObjective::isOfferedAs()`) et reprise d'une planète abandonnée comptée, sauf laissée par un membre, un allié ou un parti depuis moins de 7 jours (`WheneverBaseRecolonized`, pondération `AllianceMissionTargetWeight`).
  - Dégressivité sur un même joueur, par inscrit et par mission (`AllianceMissionPolicy::yieldPercent()`, `countOnTarget`, `alliance_mission_same_target_decay_percent: 50`, `same_target_max_hits: 3`) : 100, 50, 25 puis 0 % pour Pillage, Casse, Pluie de missiles, Victoire nette. **Publiée** le 21 octobre 2026 (décision de l'équipe, affichée par le jeu dans les libellés `missions.objectives.*.counts`) ; elle était jusque-là non publiée.
  - Exemple du plafond cumulatif recalculé avec l'algorithme de `counted()` (objectif 1 000 000, lundi, plafond 290 000 : 0, 580 000, 780 000).
  - Troisième lot du 21 octobre (Backend#612, commits `07f134f7` à `97d1732a` ; Frontend#1335) : plus de seuil d'effort (`alliance_mission_v2_minimum_effort_percent: 0`, `AllianceMissionShareCalculator` garde `effort > 0`) ; Cartographie à 1 333 centièmes par inscrit et par semaine (migration `Version20270107091000`), ×1,8 / ×3,2 = 13,3 / 24 / 43, plafonnée aux systèmes habités ; remplacement = 20 h (quotidienne) ou 100 h (hebdomadaire) de la référence de l'univers × 2^(rang − 1), 60/30/10, 3 par cycle (`AllianceMissionReplacementPolicy`, `alliance_mission_*_replacement_hours`, référence `AllianceStationPricing::reference()`, la médiane ; son plancher de 1 000 / h n'est pas publié) ; objectif mesuré sur max(inscrits, ⌈50 % des membres actifs⌉) pour les mesures RESOURCES et COUNT, production des inscrits mise à l'échelle de leur moyenne (`AllianceMissionEconomy::targetFor()`, `alliance_mission_v2_enrolled_floor_percent: 50`, actifs = hors intégration, `is_ai = 0`, vus depuis 7 jours, `AllianceMissionTargetSizing::activeMembersOf()`) ; « Toujours m'inscrire » (`PUT /alliance-missions/auto-enrollment`, `EnrollInOpenMissionsHandler`, `EnrollAutoEnrollingMembersHandler`) ; heure de départ par alliance (`AllianceMissionStartHour` 0 à 23, `alliance_mission_cycle_start_hour: 0`, `Alliance::moveMissionStartHour()`, droit « Gérer les missions »). Correction du 21 octobre (`17a926fc`) : changement à tout moment, une fois par 7 jours au plus (`Alliance::missionStartHourMovableFrom()`, `MISSION_START_HOUR_COOLDOWN_DAYS`, refus `AllianceMissionStartHourLockedException` avant la date affichée) ; les missions en cours gardent leur fin et leur emplacement (`AllianceMissions::keptIn()`), les suivantes prennent la nouvelle heure. Mise Épique toujours à 25 % de la cagnotte potentielle, donc ×4 avec les récompenses ; le wiki n'en donne pas de montant (affiché par le jeu).
  - Exemples recalculés : remplacement à une médiane de 6 000 / h (120 000, 240 000, 480 000 ; 600 000) ; plancher des actifs (20 actifs, 4 inscrits à 10 000 / h : 10 membres, 100 000 / h).
  - Non publiés : le saut de l'hebdomadaire tardive par les bots (`AiAllianceStewardship`), les bases par mission (`alliance_mission_template.base_target`, réglables par univers), la surcharge des chiffres par univers (`tunedBy()`).
  - Exemples du wiki recalculés par script (inscrit à 10 000 / h, médiane 6 000 / h, effort égal ; objectif en nombre de 20 ; 16 inscrits pour un objectif de participation de 10).
- Points stellaires (hebdomadaire réussie) : 1 sous l'effort moyen, 2 au-dessus, ×1,5 / ×2, arrondi au supérieur, 8 par compte sur 7 jours.
- Remplacement : 200 000 (quotidienne) ou 1 000 000 (hebdomadaire), doublé à chaque fois, 3 par cycle. **Périmé** au 21 octobre 2026 : indexé sur la médiane, voir le troisième lot ci-dessous. Mise Épique : 25 % de la cagnotte potentielle.
- Expérience : 1 000 / 1 600 / 2 500 (quotidienne), 5 000 / 8 000 / 12 500 (hebdomadaire), plafond 8 000 par semaine et par alliance.
- Catalogue : 5 familles, 13 missions, noms et règles « Ce qui compte » repris des libellés affichés (`missions.objectives.*`), qui citent déjà la pondération des bots et inactifs, l'exclusion des alliés et ex-membres, la dégressivité sur une même cible et les seuils de Victoire nette. Non publiés : le tirage et la galaxie de Cartographie avant le choix, les réglages par univers.

## 20. Banque stellaire (code du jeu, relevé le 15 octobre 2026)

Source : `astro-nova-backend` `main` (`7b255c83`), contexte `src/Bank/` (Backend #540, #568, #570, #579) ; libellés `pages/bank.json` du front.

- Lieu : une Station stellaire par système, après l'espace lointain (`Universe::getBankStationSector()`), seules les missions de dépôt y sont possibles. Accès par la vue galaxie, l'onglet Station de l'alliance ou une notification.
- Ouverture au 7e jour de l'univers (`BankSeed::WINDOW_DAYS`), pas dans un univers à l'arrêt ; banque fermée = `BankClosedException`. Aucun réglage par univers.
- Crédits : centièmes (`Credits::PER_CREDIT`), par univers, sans plafond ni érosion, ni vol ; aucun lien avec le paiement ni les Points stellaires.
- Vente (dépôt) : petits et grands cargos, base avec Dock orbital, 1 à 3 ressources, 1 h aller et retour sans hydrogène ni rappel (`FleetMission::fixedLeg`), prix fixé au départ, Crédits à l'arrivée, refus en vacances et sous attaque annoncée. Taxe 10 % sur les ventes (`ReserveLevels::SALE_TAX_PERCENT`).
- Achat : 1 à 3 ressources, débit immédiat, pas de taxe, une livraison en 1 h (`BankDelivery::TRANSIT_SECONDS`), non plafonnée par le stockage, redirigée vers la planète mère si la planète est perdue, annulée sans remboursement s'il n'y a plus de base.
- Cours (`ReserveLevels`) : produit constant ; vente brut = ⌊M·Δ/(R+Δ)⌋, taxe arrondie au supérieur ; achat coût = ⌈M·q/(R−q)⌉ ; cours = M/R pour 1 000 unités. Parité d'ouverture métal, cristal, hydrogène = 1 : 1,5 : 3.
- Exclusion d'un univers privé : solde confisqué, livraisons annulées (`CloseBankAccountCommand`).
- Non publiés : profondeur initiale des réserves (un tiers de la dépense quotidienne de l'univers, plancher 3 000 000), commandes d'administration (`app:bank:seed`), contrôles de cohérence et rattrapages, idempotence.
- Exemple du wiki recalculé par script (réserves hypothétiques : métal 1 000 000 face à 1 000 Crédits, cristal 666 666 face à 1 000).

## 21. Suppression de compte (code du jeu, relevé le 16 octobre 2026)

Source : `astro-nova-backend` branche `feat/account-deletion` (`9465c47b`, PR Backend#588) et `Astro-Nova-React` branche `feat/account-deletion` (`982a7da0`, PR Frontend#1303), pas encore fusionnées ; arbitrages dans `ACCOUNT_DELETION_BACKLOG.md` à la racine.

- Délai de 7 jours (`AccountDeletion::GRACE_DAYS`), rappel la veille (`isReminderDueAt`, nouveau jeton qui remplace le premier), nouvelle demande 30 jours après une annulation (`COOLDOWN_DAYS`).
- Protection : vacances posées dans chaque univers sans les conditions habituelles (`User::raiseDeletionShield`), production réglée d'abord ; un univers déjà en vacances garde ses vacances. Levée après annulation au plus tôt 48 h après la demande (`shieldLiftableFrom`, `VacationMode::MINIMUM_HOURS`). Le bouclier est lu à l'envoi : les flottes déjà en vol arrivent.
- Alliance : passation à la demande (`Alliance::handOverOnAccountDeletion`), au membre choisi s'il est éligible (`AllianceSuccessionPlanner::isEligible`), sinon meilleur prétendant ou membre le plus ancien ; seul membre : dissolution à J+7 (`ReleaseDeletedMemberHandler`).
- Exécution (`ExecuteAccountDeletionHandler`) : éviction PU-206 par univers (`EvictPlayerFromUniverse` : flottes perdues, ordres remboursés, planètes abandonnées sous la règle de l'univers), compte de la banque fermé (`CloseBankAccountCommand`), messages privés et réactions effacés, messages publics gardés (`senderDeleted`, « Joueur supprimé » / « Deleted player »), vitrines publiées retirées et nom masqué en adversaire (`ForgetDeletedPlayerShowcases`), compte anonymisé (`User::anonymise`), pseudo réservé 30 jours (`ReservedUsername::RESERVATION_DAYS`).
- Abonnements : renouvellement coupé à la demande, rétabli à l'annulation (`SetSubscriptionRenewal`) ; pas de remboursement ; univers privé ouvert jusqu'à la fin de la période payée.
- Libellés FR/EN : `accountDeletion.json` du front, onglet « Compte » / « Account » des Paramètres, bouton « Revenir » / « Come back » du mode vacances.
- Non publiés : gestion par le support (back-office), conservation de l'empreinte de l'adresse d'un compte sanctionné (fair-play), détails du jeton d'annulation.
- Exemple recalculé par script (demande le 16/10 à 10:00 : suppression le 23/10 à 10:00, rappel dès le 22/10 à 10:00, annulation le 17/10 à 08:00, protection levée le 18/10 à 10:00, nouvelle demande dès le 16/11 à 08:00).

