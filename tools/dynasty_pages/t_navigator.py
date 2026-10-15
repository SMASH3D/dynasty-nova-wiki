"""Le Navigateur : textes vérifiés sur le code (note du 15 octobre 2026, NavigatorMechanics, Fleet, FlightTalents)."""

FR = {
    'brief': "le Navigateur est le maître des routes. Il décide quand ses flottes arrivent, d'où elles partent et ce qu'elles ramènent. La vitesse, l'hydrogène, les soutes et les emplacements de flotte génériques viennent de l'arbre commun ; le Navigateur garde des mécaniques et deux accents étroits.",
    'rules': [
        "La vitesse de flotte, l'hydrogène, les soutes et les emplacements génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). Le Navigateur n'y ajoute que deux **accents** : +10 % de vitesse sur les Transports, Stationnements et Colonisations ([[navigator_thrust_3:1]]) ou sur les Attaques et Espionnages visant une cible abandonnée ([[navigator_thrust_3:2]]), dans le plafond de vitesse des talents (50 %, 60 % avec l'alliance) ; +15 % de vitesse de construction des Navettes de fret, Cargos stellaires et Récupérateurs ([[navigator_freight_4]]).",
        "Une **cible abandonnée** est une base sans propriétaire, une base d'un adversaire contrôlé par le jeu, ou celle d'un joueur inactif depuis la durée fixée par l'univers.",
        "Les trajets **entre vos propres bases** (planètes et lunes) sont le périmètre propre de la classe : Transport et Stationnement pour [[navigator_lines_1]], [[navigator_lines_6:2]], [[navigator_freight_2]] et [[navigator_lines_8]]. [[navigator_freight_2]] et [[navigator_lines_6:2]] sont **hors des plafonds** de soute et d'hydrogène de l'arbre commun.",
        "Un bonus de vitesse de vol **divise** la durée du trajet : +10 % donne un trajet 1,1 fois plus court. Les nœuds de recharge, eux, **retirent** des heures ou un pourcentage au délai. Voir [Déplacements](/fr/fleet/movement).",
        "Les ordres en vol ([[navigator_thrust_1]], [[navigator_thrust_6:1]], [[navigator_thrust_6:2]], [[navigator_lines_5]], [[navigator_thrust_9]], [[navigator_freight_6:1]]) se donnent depuis le détail de la flotte. Les cycles sont comptés pour tout l'empire, depuis la dernière utilisation.",
    ],
    'example': """**[[navigator_thrust_1]] sur un aller-retour**
- Un Transport aller-retour, aller de 2 h. Après 1 h de vol, [[navigator_thrust_1]] coupe 25 % du temps restant : 3 600 s × 0,75 = 2 700 s. La flotte arrive 1 h 45 après son départ.
- Le retour dure autant que l'aller réel : 1 h 45. Total **3 h 30** au lieu de 4 h : couper 15 min à l'aller en fait gagner 30.
- Avec [[navigator_thrust_4]] au rang 3 (40 %) : 3 600 s × 0,6 = 2 160 s, aller 1 h 36, retour 1 h 36, total **3 h 12**.

**[[navigator_lines_2]] : 100 Corvettes vers une autre galaxie**
- Distance : 20 000. Une Corvette consomme 300. Un trajet à 100 % coûte 300 × 100 × 20 000 / 35 000 × 4 = 68 571 H (arrondi à l'inférieur), soit **137 142 H** aller-retour.
- Soute des 100 Corvettes, sans Pliage Spatial : 100 × 800 = **80 000**. Le carburant ne tient pas.
- Rang 1 (85 % du volume) : 116 571. Rang 2 (70 %) : 96 000. Rang 3 (55 %) : 137 142 × 0,55 = **75 429** : la flotte peut partir.

**[[navigator_thrust_8]] : le seuil de 5 %**
- À quai : 100 Corvettes à 29 000 de coût chacune (20 000 + 7 000 + 2 000), soit 2 900 000. Seuil : 5 % = **145 000**.
- 37 Intercepteurs (4 000 chacun) = 148 000 : la flotte décolle. 36 Intercepteurs (144 000) : elle reste.
- La planète refuge est à 40 min ; le retour est tiré à 1 h. La flotte ne revient jamais plus vite qu'elle n'est partie : elle rentre 40 min + 40 min = **1 h 20** après son décollage.

**[[navigator_thrust_5]] et [[navigator_thrust_7]] : Cargos stellaires et Corvettes vers une autre galaxie** (vitesse de flotte de l'univers ×1, comme Redline ; sans recherche de moteur)
- Sans le nœud, la flotte vole à la vitesse du Cargo stellaire, 7 500 : 10 + 3 500 × √(10 × 20 000 / 7 500) = 18 084 s, soit **5 h 01 min 24 s**.
- [[navigator_thrust_5]] (15 %) : 8 625, soit **4 h 41 min 04 s**. Avec [[navigator_thrust_7]] au rang 3 (30 %) : 9 750, soit **4 h 24 min 22 s**. L'hydrogène ne change pas.""",
    'branch_notes': {
        'thrust': """- **[[navigator_thrust_1]]** : sur une flotte à l'aller ou au retour, refusée s'il reste 5 min ou moins ; le temps restant est arrondi à la seconde supérieure. Sur un aller-retour, le retour reprend la durée de l'aller raccourci (sauf avec [[navigator_lines_9]], [[navigator_freight_3:1]] ou une vitesse changée en vol). Sur une Attaque, l'alerte du défenseur suit la nouvelle heure d'impact.
- **[[navigator_thrust_2]]** retire 4 h par rang au cycle de 24 h : 12 h au rang 3.
- **[[navigator_thrust_3:1]]** et **[[navigator_thrust_3:2]]** occupent l'accent de vitesse de 10 % ; ils s'ajoutent aux 40 % de l'arbre commun au plus.
- **[[navigator_thrust_5]]** : le vaisseau le plus lent compte 15 % plus vite (30 % avec [[navigator_thrust_7]]), sans dépasser le plus rapide de la flotte, vitesses des moteurs comprises. Une flotte d'un seul type ne gagne rien. La durée suit la racine carrée de la vitesse : +30 % de vitesse raccourcit le vol d'environ 12 %.
- **[[navigator_thrust_6:1]]** : seulement vers 100 %. Le temps restant est multiplié par l'ancienne vitesse / 100 (sur un aller-retour à l'aller, le retour aussi) ; l'hydrogène en plus est prélevé sur la base.
- **[[navigator_thrust_6:2]]** : jusqu'à 10 % au plus bas ; l'hydrogène économisé revient dans la soute de la flotte.
- Ni [[navigator_thrust_6:1]] ni [[navigator_thrust_6:2]] ne s'appliquent à l'aller d'une Attaque, d'un Espionnage, d'une Destruction de lune ou d'une Expédition ; ils s'appliquent à tout retour.
- **[[navigator_thrust_8]]** : la menace se mesure au coût total des vaisseaux (métal, cristal, hydrogène), Collecteurs solaires exclus ; un Éclaireur compte comme les autres. La flotte part en Transport à 100 %, sans ressources, vers votre autre planète la plus proche (jamais une lune, ni la planète de la même case), jusqu'à 3 min avant l'impact. Rien ne part si vous n'avez pas d'autre planète ou si la base n'a pas l'hydrogène du vol. La fenêtre de retour se règle entre 15 min et 24 h ; un retour ne vole jamais plus vite que l'aller, il peut donc tomber après la fenêtre si la planète refuge est loin.
- **[[navigator_thrust_9]]** : toute flotte en retour, quelle que soit sa mission. Chaque charge revient 24 h après avoir servi.""",
        'lines': """- **[[navigator_lines_1]]** et **[[navigator_lines_7]]** : un Transport ou un Stationnement vers une de vos bases part hors emplacement tant qu'une navette est libre. La navette reste occupée jusqu'au retour de la flotte. 5 navettes au plus.
- **[[navigator_lines_2]]** : le volume du carburant est arrondi à l'unité supérieure.
- **[[navigator_lines_3:1]]** : la base d'arrivée paie tout l'hydrogène du vol, aller-retour compris ; la base de départ ne paie que la cargaison.
- **[[navigator_lines_3:2]]** : au rappel, le chemin de retour déjà dû compte comme brûlé. 20 000 H payés aller-retour, rappel à mi-chemin de l'aller : 10 000 H non brûlés, 5 000 H rendus dans la soute.
- **[[navigator_lines_4]]** **réduit** la recharge de 10 % par rang (×0,7 au rang 3), elle ne la divise pas : niveau 5, 36 min → 25 min 12 s ; niveau 14, 10 min → 7 min.
- **[[navigator_lines_5]]** : un Transport ou un Stationnement à l'aller, ou toute flotte en retour, dont la destination est à vous. La nouvelle base doit être dans le même système et avoir un Dock orbital si la flotte y atterrit (retour ou stationnement).
- **[[navigator_lines_6:2]]** se multiplie avec les réductions d'hydrogène de l'arbre commun et de l'alliance.
- **[[navigator_lines_8]]** : 1 min fixe, quelle que soit la vitesse choisie ou celle de l'univers.
- **[[navigator_lines_9]]** : la base de retour (planète ou lune) doit avoir un Dock orbital. Le retour vole la vraie distance et paie son hydrogène, sans les bonus des trajets entre vos bases.""",
        'freight': """- **[[navigator_freight_1]]** : Transport seulement (pas Stationnement). La cargaison demandée doit tenir dans la soute à l'envoi ; elle est chargée dans la limite du stock de la base d'arrivée.
- **[[navigator_freight_2]]** s'ajoute au bonus de soute de l'arbre commun : jusqu'à +55 % entre vos bases.
- **[[navigator_freight_3:1]]** : la première base reçoit 50 % de la cargaison, ou la part choisie entre 1 et 99 %. Le vol paie ses trois trajets. Ne se combine ni avec [[navigator_freight_1]] ni avec [[navigator_lines_9]].
- **[[navigator_freight_3:2]]** : ne concerne que les trouvailles de ressources des [expéditions](/fr/fleet/expeditions).
- **[[navigator_freight_4]]** s'ajoute à la vitesse de construction des unités de l'arbre commun : un Cargo stellaire de 10 h se construit en 8 h 41 min 45 s (÷ 1,15).
- **[[navigator_freight_5]]** se demande à l'envoi : la soute doublée sert à tout ce que la flotte charge (pillage, débris, trouvailles, fret). Le cycle part de la première flotte.
- **[[navigator_freight_6:2]]** : la seconde flotte doit partir au plus 1 min après la première.
- **[[navigator_freight_8]]** : joue quand une de vos flottes est entièrement détruite au combat pendant sa propre Attaque (Seconde vague comprise) ou une Destruction de lune. La moitié de ce qu'elle transportait, arrondie à l'inférieur ressource par ressource, revient à sa base de départ.
- **[[navigator_freight_9]]** : la charge part sur la **première** attaque gagnée contre une cible abandonnée du cycle, sans choix. Les abris du défenseur s'appliquent, puis la limite des soutes. 3 000 000 en stock : 1 500 000 au taux habituel de 50 %, 3 000 000 avec [[navigator_freight_9]], dans la limite des soutes.""",
    },
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Coureur | Poussée 15 · Lignes 10 | [[navigator_thrust_9]], [[navigator_thrust_1]] à 40 % toutes les 12 h, une route à +10 %, [[navigator_thrust_5]] à 30 %, [[navigator_thrust_6:1]] ou [[navigator_thrust_6:2]], [[navigator_thrust_8]] ; 2 navettes, carburant à 55 % de son volume, [[navigator_lines_3:1]] ou [[navigator_lines_3:2]], [[navigator_lines_4]], [[navigator_lines_5]], [[navigator_lines_6:1]] ou [[navigator_lines_6:2]] |
| Logisticien d'empire | Lignes 15 · Fret 10 | [[navigator_lines_9]], 5 navettes, [[navigator_lines_8]], [[navigator_lines_5]], [[navigator_lines_6:1]] ou [[navigator_lines_6:2]] ; [[navigator_freight_1]], +30 % de chargement entre vos bases, [[navigator_freight_3:1]] ou [[navigator_freight_3:2]], [[navigator_freight_4]], [[navigator_freight_5]] une fois par 24 h |
| Pilleur de fermes | Fret 15 · Poussée 10 | [[navigator_freight_9]], [[navigator_freight_5]] toutes les 12 h ([[navigator_freight_6:1]] ou [[navigator_freight_6:2]]), [[navigator_freight_8]] ; [[navigator_thrust_1]] à 40 % toutes les 12 h, [[navigator_thrust_3:2]], [[navigator_thrust_5]] à 15 % |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Le carburant prend de la place en soute** : sans [[navigator_lines_2]], une flotte de combat lointaine peut ne pas partir faute de soute.",
        "**[[navigator_thrust_5]] ne regarde que le plus lent** : la flotte vole à la vitesse du plus lent augmentée de 15 % (30 %), sans dépasser le plus rapide. Une flotte d'un seul type n'en profite pas.",
        "**[[navigator_thrust_1]] à l'aller compte double** sur un aller-retour : le retour reprend la durée de l'aller raccourci.",
        "**[[navigator_thrust_3:2]] ne vise que les cibles abandonnées** : une attaque contre un joueur actif garde sa vitesse normale.",
        "**[[navigator_thrust_6:1]] et [[navigator_thrust_6:2]]** ne marchent pas à l'aller d'une Attaque, d'un Espionnage, d'une Destruction de lune ni d'une Expédition.",
        "**[[navigator_thrust_8]] n'emmène que les vaisseaux** : les ressources restent sur la planète. Sans autre planète ou sans l'hydrogène du vol, la flotte ne part pas.",
        "**[[navigator_freight_8]] ne protège pas un convoi** : il ne joue que si votre flotte est anéantie pendant sa propre attaque ou une Destruction de lune.",
        "**[[navigator_freight_9]] part tout seul** sur la première victoire contre une cible abandonnée, même si elle est presque vide.",
        "**[[navigator_lines_1]]** : seuls les Transports et Stationnements vers vos propres bases sont hors emplacement.",
        "**[[navigator_freight_3:1]], [[navigator_freight_1]] et [[navigator_lines_9]] ne se combinent pas** sur un même envoi.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Arbre commun](/fr/dynasty/common-tree)", "[Classes](/fr/dynasty/classes)",
        "[Déplacements](/fr/fleet/movement)", "[Porte de saut](/fr/fleet/jump-gate)", "[Expéditions](/fr/fleet/expeditions)",
        "[Pillage](/fr/combat/plunder)",
    ],
}

EN = {
    'brief': "the Navigator is the master of routes. It decides when its fleets arrive, where they leave from and what they bring back. Generic speed, hydrogen, holds and fleet slots come from the common tree; the Navigator keeps mechanics and two narrow accents.",
    'rules': [
        "Generic fleet speed, hydrogen, holds and slots come from the [common tree](/en/dynasty/common-tree). The Navigator only adds two **accents**: +10% speed on Transports, Stationings and Colonizations ([[navigator_thrust_3:1]]) or on Attacks and Espionage aimed at an abandoned target ([[navigator_thrust_3:2]]), within the talents' speed cap (50%, 60% with the alliance); +15% build speed for Cargo Shuttles, Stellar Freighters and Salvagers ([[navigator_freight_4]]).",
        "An **abandoned target** is a base with no owner, a base of a game-controlled opponent, or that of a player inactive for the duration set by the universe.",
        "Trips **between your own bases** (planets and moons) are the class's own scope: Transport and Stationing for [[navigator_lines_1]], [[navigator_lines_6:2]], [[navigator_freight_2]] and [[navigator_lines_8]]. [[navigator_freight_2]] and [[navigator_lines_6:2]] are **outside the common tree's** cargo and hydrogen caps.",
        "A flight speed bonus **divides** the trip's duration: +10% makes a trip 1.1 times shorter. Recharge nodes, on the other hand, **take** hours or a percentage off the delay. See [Movement](/en/fleet/movement).",
        "In-flight orders ([[navigator_thrust_1]], [[navigator_thrust_6:1]], [[navigator_thrust_6:2]], [[navigator_lines_5]], [[navigator_thrust_9]], [[navigator_freight_6:1]]) are given from the fleet's details. Cycles count for the whole empire, from the last use.",
    ],
    'example': """**[[navigator_thrust_1]] on a round trip**
- A round-trip Transport, 2 h out. After 1 h of flight, [[navigator_thrust_1]] cuts 25% of the remaining time: 3,600 s × 0.75 = 2,700 s. The fleet arrives 1 h 45 after leaving.
- The way back lasts as long as the actual way out: 1 h 45. Total **3 h 30** instead of 4 h: cutting 15 min on the way out saves 30.
- With [[navigator_thrust_4]] at rank 3 (40%): 3,600 s × 0.6 = 2,160 s, out 1 h 36, back 1 h 36, total **3 h 12**.

**[[navigator_lines_2]]: 100 Corvettes to another galaxy**
- Distance: 20,000. A Corvette burns 300. One leg at 100% costs 300 × 100 × 20,000 / 35,000 × 4 = 68,571 H (rounded down), so **137,142 H** for the round trip.
- Hold of the 100 Corvettes, without Hyperspace Technology: 100 × 800 = **80,000**. The fuel does not fit.
- Rank 1 (85% of its volume): 116,571. Rank 2 (70%): 96,000. Rank 3 (55%): 137,142 × 0.55 = **75,429**: the fleet can leave.

**[[navigator_thrust_8]]: the 5% threshold**
- Docked: 100 Corvettes costing 29,000 each (20,000 + 7,000 + 2,000), that is 2,900,000. Threshold: 5% = **145,000**.
- 37 Interceptors (4,000 each) = 148,000: the fleet takes off. 36 Interceptors (144,000): it stays.
- The refuge planet is 40 min away; the return is drawn at 1 h. The fleet never comes back faster than it left: it lands 40 min + 40 min = **1 h 20** after taking off.

**[[navigator_thrust_5]] and [[navigator_thrust_7]]: Stellar Freighters and Corvettes to another galaxy** (universe fleet speed ×1, as on Redline; no drive research)
- Without the node, the fleet flies at the Stellar Freighter's speed, 7,500: 10 + 3,500 × √(10 × 20,000 / 7,500) = 18,084 s, that is **5 h 01 min 24 s**.
- [[navigator_thrust_5]] (15%): 8,625, that is **4 h 41 min 04 s**. With [[navigator_thrust_7]] at rank 3 (30%): 9,750, that is **4 h 24 min 22 s**. Hydrogen does not change.""",
    'branch_notes': {
        'thrust': """- **[[navigator_thrust_1]]**: on a fleet flying out or home, refused with 5 min or less left; the remaining time is rounded up to the second. On a round trip, the way back takes the shortened outbound duration (except with [[navigator_lines_9]], [[navigator_freight_3:1]] or a speed changed in flight). On an Attack, the defender's alert follows the new impact time.
- **[[navigator_thrust_2]]** takes 4 h per rank off the 24 h cycle: 12 h at rank 3.
- **[[navigator_thrust_3:1]]** and **[[navigator_thrust_3:2]]** take the 10% speed accent; they add to at most 40% from the common tree.
- **[[navigator_thrust_5]]**: the slowest ship counts 15% faster (30% with [[navigator_thrust_7]]), never past the fleet's fastest, drive research included. A single-type fleet gains nothing. Duration follows the square root of speed: +30% speed shortens the flight by about 12%.
- **[[navigator_thrust_6:1]]**: only up to 100%. The remaining time is multiplied by the old speed / 100 (on a round trip flying out, the way back too); the extra hydrogen is taken from the base.
- **[[navigator_thrust_6:2]]**: down to 10% at the lowest; the hydrogen saved goes back into the fleet's hold.
- Neither [[navigator_thrust_6:1]] nor [[navigator_thrust_6:2]] applies to an Attack, Espionage, Moon destruction or Expedition on its way out; both apply to any return.
- **[[navigator_thrust_8]]**: the threat is measured by the ships' total cost (metal, crystal, hydrogen), Solar Collectors excluded; a Scout counts like any other ship. The fleet leaves as a Transport at 100%, with no resources, for your nearest other planet (never a moon, nor the planet of the same cell), up to 3 min before impact. Nothing leaves if you have no other planet or if the base lacks the flight's hydrogen. The return window can be set between 15 min and 24 h; a return never flies faster than the way out, so it may land after the window when the refuge planet is far.
- **[[navigator_thrust_9]]**: any fleet flying home, whatever its mission. Each charge comes back 24 h after it was used.""",
        'lines': """- **[[navigator_lines_1]]** and **[[navigator_lines_7]]**: a Transport or Stationing to one of your bases leaves outside the slots while a shuttle is free. The shuttle stays taken until the fleet is back. 5 shuttles at most.
- **[[navigator_lines_2]]**: the fuel's volume is rounded up.
- **[[navigator_lines_3:1]]**: the arrival base pays all of the flight's hydrogen, round trip included; the departure base only pays the cargo.
- **[[navigator_lines_3:2]]**: on recall, the way back already owed counts as burned. 20,000 H paid for the round trip, recalled halfway out: 10,000 H unburned, 5,000 H returned into the hold.
- **[[navigator_lines_4]]** **cuts** the recharge by 10% per rank (×0.7 at rank 3), it does not divide it: level 5, 36 min → 25 min 12 s; level 14, 10 min → 7 min.
- **[[navigator_lines_5]]**: a Transport or Stationing flying out, or any fleet flying home, whose destination is yours. The new base must be in the same system and have an Orbital Dock if the fleet lands there (return or stationing).
- **[[navigator_lines_6:2]]** multiplies with the common tree's and the alliance's hydrogen reductions.
- **[[navigator_lines_8]]**: a fixed 1 min, whatever the chosen speed or the universe's.
- **[[navigator_lines_9]]**: the home base (planet or moon) must have an Orbital Dock. The way back flies the real distance and pays its hydrogen, without the bonuses of trips between your bases.""",
        'freight': """- **[[navigator_freight_1]]**: Transport only (not Stationing). The requested cargo must fit in the hold when sending; it is loaded within the arrival base's stock.
- **[[navigator_freight_2]]** adds to the common tree's cargo bonus: up to +55% between your bases.
- **[[navigator_freight_3:1]]**: the first base gets 50% of the cargo, or the share chosen between 1 and 99%. The flight pays its three legs. It combines with neither [[navigator_freight_1]] nor [[navigator_lines_9]].
- **[[navigator_freight_3:2]]**: only concerns the resource finds of [expeditions](/en/fleet/expeditions).
- **[[navigator_freight_4]]** adds to the common tree's unit build speed: a 10 h Stellar Freighter builds in 8 h 41 min 45 s (÷ 1.15).
- **[[navigator_freight_5]]** is requested when sending: the doubled hold serves everything the fleet loads (plunder, debris, finds, freight). The cycle starts from the first fleet.
- **[[navigator_freight_6:2]]**: the second fleet must leave at most 1 min after the first.
- **[[navigator_freight_8]]**: works when one of your fleets is entirely destroyed in combat during its own Attack (Second Wave included) or a Moon destruction. Half of what it carried, rounded down resource by resource, goes back to its departure base.
- **[[navigator_freight_9]]**: the charge is spent on the **first** won attack against an abandoned target in the cycle, with no choice. The defender's shelters apply, then the holds' limit. 3,000,000 in stock: 1,500,000 at the usual 50% rate, 3,000,000 with [[navigator_freight_9]], within the holds' limit.""",
    },
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Runner | Thrust 15 · Lines 10 | [[navigator_thrust_9]], [[navigator_thrust_1]] at 40% every 12 h, a route at +10%, [[navigator_thrust_5]] at 30%, [[navigator_thrust_6:1]] or [[navigator_thrust_6:2]], [[navigator_thrust_8]]; 2 shuttles, fuel at 55% of its volume, [[navigator_lines_3:1]] or [[navigator_lines_3:2]], [[navigator_lines_4]], [[navigator_lines_5]], [[navigator_lines_6:1]] or [[navigator_lines_6:2]] |
| Empire Logistician | Lines 15 · Freight 10 | [[navigator_lines_9]], 5 shuttles, [[navigator_lines_8]], [[navigator_lines_5]], [[navigator_lines_6:1]] or [[navigator_lines_6:2]]; [[navigator_freight_1]], +30% load between your bases, [[navigator_freight_3:1]] or [[navigator_freight_3:2]], [[navigator_freight_4]], [[navigator_freight_5]] once per 24 h |
| Farm Raider | Freight 15 · Thrust 10 | [[navigator_freight_9]], [[navigator_freight_5]] every 12 h ([[navigator_freight_6:1]] or [[navigator_freight_6:2]]), [[navigator_freight_8]]; [[navigator_thrust_1]] at 40% every 12 h, [[navigator_thrust_3:2]], [[navigator_thrust_5]] at 15% |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**Fuel takes up hold space**: without [[navigator_lines_2]], a distant combat fleet may be unable to leave for lack of hold.",
        "**[[navigator_thrust_5]] only looks at the slowest ship**: the fleet flies at the slowest speed raised by 15% (30%), never past the fastest. A single-type fleet does not benefit.",
        "**[[navigator_thrust_1]] on the way out counts twice** on a round trip: the way back takes the shortened outbound duration.",
        "**[[navigator_thrust_3:2]] only targets abandoned targets**: an attack on an active player keeps its normal speed.",
        "**[[navigator_thrust_6:1]] and [[navigator_thrust_6:2]]** do not work on an Attack, Espionage, Moon destruction or Expedition on its way out.",
        "**[[navigator_thrust_8]] only takes the ships**: resources stay on the planet. Without another planet or without the flight's hydrogen, the fleet does not leave.",
        "**[[navigator_freight_8]] does not protect a convoy**: it only works when your fleet is wiped out during its own attack or a Moon destruction.",
        "**[[navigator_freight_9]] fires on its own** on the first victory against an abandoned target, even a nearly empty one.",
        "**[[navigator_lines_1]]**: only Transports and Stationings to your own bases are outside the slots.",
        "**[[navigator_freight_3:1]], [[navigator_freight_1]] and [[navigator_lines_9]] do not combine** on the same send.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Common tree](/en/dynasty/common-tree)", "[Classes](/en/dynasty/classes)",
        "[Movement](/en/fleet/movement)", "[Jump gate](/en/fleet/jump-gate)", "[Expeditions](/en/fleet/expeditions)",
        "[Plunder](/en/combat/plunder)",
    ],
}
