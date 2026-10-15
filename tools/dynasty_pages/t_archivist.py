"""L'Archiviste : textes vérifiés sur le code (note du 15 octobre 2026, backend 7b255c83)."""

FR = {
    'brief': "« Rien ne se perd ». L'Archiviste récupère ce que les autres laissent derrière eux : un savoir que d'autres ont déjà trouvé ([[b:memory]]), les épaves des batailles ([[b:wreck]]), et sa propre flotte quand elle tombe ([[b:registry]]).",
    'rules': [
        "**Niveau connu** : un niveau de recherche que détiennent déjà, à ce niveau ou plus haut, **25 %** des joueurs comptés de l'univers. Sont comptés les joueurs actifs dans les 7 derniers jours, hors mode vacances et hors bots. Le décompte est refait une fois par jour. Toute la branche [[b:memory]] ne touche que ces niveaux.",
        "La vitesse d'un niveau connu ([[archivist_memory_1]], [[archivist_memory_4]]) et celle de [[archivist_registry_8]] s'**ajoutent** à votre vitesse de recherche, en dehors de ses plafonds. Vitesse, coût et niveau connu se fixent au **lancement** de l'étude.",
        "**Récoltes de débris** : le bonus porte sur le métal et le cristal que vos Récupérateurs chargent réellement, donc dans la limite de leur soute. Il est versé au retour, ne prend pas de place en soute et ne retire rien de plus au champ.",
        "**Registre des pertes** : le registre, commun à tout votre empire, garde la liste des vaisseaux perdus au combat, ceux d'une flotte comme ceux qui défendaient une planète. Les défenses n'y entrent jamais. Une commande passée depuis le registre, sur n'importe quelle planète, se fait aux conditions du registre dans la limite des quantités qu'il garde, en puisant d'abord dans les pertes les plus anciennes.",
        "La vitesse du registre s'**ajoute** à la vitesse de construction des vaisseaux : une durée est divisée par (1 + somme des bonus). La réduction de coût du registre s'applique **sur le prix déjà réduit** par vos autres réductions de vaisseaux.",
        "Le seul **accent** de la classe est la vitesse des missions de recyclage ([[archivist_wreck_3:2]]), dans le budget de vitesse de flotte des talents. Le dock, le recyclage pendant le combat et l'hydrogène des débris appartiennent à l'Amiral ; les défenses au Vétéran.",
    ],
    'example': """**[[b:memory]]** : Systèmes Offensifs 10 (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 : **46 h 32 min 44 s** sans talent. Le niveau est connu.
- [[archivist_memory_1]] (+10 %) : **42 h 18 min 51 s**.
- Avec [[archivist_memory_4]] au rang 3 (+25 % au total) : **37 h 14 min 12 s**. Avec [[archivist_memory_6:1]], à 5 niveaux de retard ou plus (+40 %) : **33 h 14 min 49 s**.
- [[archivist_memory_2]] au rang 3 (−12 %) : **360 448** métal et **90 112** cristal.
- [[archivist_memory_5]] : Systèmes Offensifs 11, s'il est connu, dure 93 h 05 min 27 s, ramenées à 74 h 28 min 22 s par les +25 %. Il démarre avec 10 % de ce temps fait, **7 h 26 min 50 s** ; avec [[archivist_memory_7]] au rang 3 (25 %), **18 h 37 min 05 s**.
- Le même Systèmes Offensifs 10, lancé dans les 24 h d'une défaite avec [[archivist_registry_8]] : 25 + 20 = 45 % → **32 h 06 min 02 s**.

**[[b:wreck]]** : 100 Corvettes détruites, univers à 30 % de débris (Redline) : 600 000 métal et 210 000 cristal, soit 810 000 ressources. Il faut 41 Récupérateurs (20 000 de soute chacun, sans Pliage Spatial).
- [[archivist_wreck_1]] et [[archivist_wreck_4]] au rang 3 (+25 %) : +150 000 métal et +52 500 cristal, **1 012 500** rapportés. Le champ perd 810 000, pas plus.
- Arrivée moins d'1 h après le combat, avec [[archivist_wreck_6:2]] (+45 %) : **1 174 500**.
- Avec 30 Récupérateurs seulement (600 000 de soute) : 444 444 métal et 155 555 cristal chargés au prorata, le bonus porte sur eux ; 210 001 ressources restent au champ.

**[[b:registry]]** : 200 Corvettes perdues, soit 4 000 000 métal, 1 400 000 cristal et 400 000 hydrogène (5 800 000 ressources).
- [[archivist_registry_5]] : 5 % de leur prix, soit **290 000** ressources versées aussitôt (200 000 / 70 000 / 20 000) ; **464 000** avec [[archivist_registry_7]] au rang 3 (8 %).
- [[archivist_registry_2]] au rang 3 (−12 %) : 4 000 000 → **3 520 000** métal ; avec [[archivist_registry_6:2]] (−20 % au total), **3 200 000**.
- Une reconstruction qui prend 10 h sans talent : **8 h 41 min 45 s** avec [[archivist_registry_1]] (+15 %), **7 h 41 min 33 s** avec [[archivist_registry_4]] au rang 3 (+30 %), **6 h 40 min** avec [[archivist_registry_6:1]] (+50 %). Avec [[archivist_registry_3:1]] en plus, dans les 24 h qui suivent la perte (+70 %) : **5 h 52 min 57 s**.""",
    'branch_notes': {
        'memory': """- **[[archivist_memory_3:1]]** : un niveau qu'un autre membre de votre alliance détient, à ce niveau ou plus haut. **[[archivist_memory_6:2]]** : le joueur classé juste au-dessus de vous au classement général. Ces deux listes sont relevées une fois par jour.
- **[[archivist_memory_5]]** : le niveau achevé doit être connu, et le suivant connu au moment où vous le lancez. L'avance est une part de la durée réelle de l'étude et s'ajoute au-delà du plafond des avances du Théoricien. Un seul élan à la fois : achever un autre niveau connu le remplace.
- **[[archivist_memory_6:1]]** : le niveau le plus répandu est celui que le plus de joueurs comptés détiennent exactement (le plus bas en cas d'égalité). Seule la part de [[archivist_memory_4]] compte double : 10 + 15 × 2 = 40 %.
- **[[archivist_memory_8]]** lève seulement le niveau de Centre d'innovation demandé : la planète doit tout de même avoir un Centre d'innovation.
- **[[archivist_memory_9]]** : un seul joueur compté suffit. Un niveau détenu seulement par des bots ou des joueurs inactifs ou en vacances ne devient pas connu ainsi.""",
        'wreck': """- **[[archivist_wreck_2]]** : jusqu'à 15 systèmes autour de chacune de vos planètes, dans la même galaxie.
- **[[archivist_wreck_3:1]]** : vous pouvez recycler n'importe quelle case sans l'avoir sondée, que le radar la montre ou non.
- **[[archivist_wreck_5]]** sonne chaque fois qu'un champ de votre radar reçoit des débris et dépasse 50 000 ressources, même s'il les dépassait déjà. Pas pour un champ qu'un autre joueur a mis sous scellés.
- **[[archivist_wreck_6:1]]** : après une attaque contre votre planète, ses Récupérateurs restés à quai récoltent tout le champ au-dessus d'elle, ancien compris, avant ceux de l'attaquant. Métal et cristal vont directement au stock, avec le bonus de [[archivist_wreck_1]] et [[archivist_wreck_4]].
- **[[archivist_wreck_6:2]]** se mesure du dernier ajout de débris au champ jusqu'à l'**arrivée** de vos Récupérateurs. Il s'ajoute aux 25 % de [[archivist_wreck_1]] et [[archivist_wreck_4]], au-delà de leur plafond.
- **[[archivist_wreck_7]]** : les Récupérateurs partent de votre planète la plus proche qui en a, dans la portée du radar, autant qu'il en faut pour le champ, à pleine vitesse. Pas de départ si une de vos flottes vise déjà cette case. Le compte de 24 h s'ouvre au premier départ. Un départ refusé par les règles de vol (hydrogène, emplacements de flotte, case jamais sondée sans [[archivist_wreck_3:1]]) ne coûte rien.
- **[[archivist_wreck_8]]** passe sur les champs voisins après le champ visé, dans la place qui reste en soute, sauf un champ mis sous scellés par un autre joueur.
- **[[archivist_wreck_9]]** : un champ non vide que vous voyez, case sondée par vous ou votre alliance, ou couverte par votre radar. Les 24 h comptent depuis le dernier scellé. Impossible sur un champ déjà scellé par un autre joueur.""",
        'registry': """- **[[archivist_registry_3:1]]** compte 24 h depuis **la dernière** perte encore au registre.
- **[[archivist_registry_5]]** se calcule sur le prix normal des vaisseaux perdus, ressource par ressource, et va à la planète d'où partait la flotte, ou à la planète défendue, si elle vous appartient encore.
- **[[archivist_registry_8]]** : une défaite est une attaque de planète, en attaque comme en défense, où vous avez perdu plus de points d'unités (vaisseaux et défenses) que l'adversaire. Seules les études lancées pendant ces 24 h vont plus vite : une étude déjà en cours ne change pas. Chaque nouvelle défaite relance les 24 h.
- **[[archivist_registry_9]]** : les commandes du registre ont leur propre file, en parallèle de la file normale des vaisseaux.""",
    },
    'caps_note': "Deux bonus passent au-delà de ces plafonds : [[archivist_memory_6:1]] porte la vitesse d'un niveau connu à 40 %, et [[archivist_wreck_6:2]] ajoute 20 points aux récoltes sur un champ frais (45 %).",
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Le rattrapeur | [[b:memory]] 15 · [[b:registry]] 10 | [[archivist_memory_9]], [[archivist_memory_8]] ; niveaux connus +25 % (+40 % avec [[archivist_memory_6:1]]) et −12 %, 25 % d'avance sur chaque niveau enchaîné ; registre +50 % avec [[archivist_registry_6:1]] (sinon +30 % et −20 % avec [[archivist_registry_6:2]]), [[archivist_registry_2]] −12 %, [[archivist_registry_5]] 5 % |
| Le charognard | [[b:wreck]] 15 · [[b:memory]] 10 | [[archivist_wreck_9]], [[archivist_wreck_5]], [[archivist_wreck_7]], [[archivist_wreck_8]] ; récoltes +25 % ; niveaux connus +25 % et −12 %, [[archivist_memory_5]] 10 % |
| L'increvable | [[b:registry]] 15 · [[b:wreck]] 10 | [[archivist_registry_9]], [[archivist_registry_5]] 8 %, [[archivist_registry_8]], registre jusqu'à +70 % ; récoltes +25 %, radar à 15 systèmes, [[archivist_wreck_6:1]] ou [[archivist_wreck_6:2]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Un niveau connu se juge sur les joueurs comptés** (actifs depuis 7 jours, hors vacances, hors bots), et le décompte n'est refait qu'une fois par jour.",
        "**Le premier sur une recherche ne profite pas de la Mémoire** sur cette recherche : il n'y a personne devant lui.",
        "**Tout se fixe au lancement** : un niveau qui devient connu pendant l'étude ne l'accélère pas, et [[archivist_registry_8]] n'accélère pas une étude déjà en cours.",
        "**[[archivist_memory_3:2]] ne sert plus à rien avec [[archivist_memory_9]]**, qui demande déjà moins : un seul détenteur.",
        "**Le bonus de récolte suit la soute** : il porte sur ce que vos Récupérateurs chargent, pas sur tout le champ. Il ne vide pas plus le champ : d'autres joueurs peuvent récolter ce qui reste.",
        "**[[archivist_wreck_7]] sans [[archivist_wreck_3:1]]** échoue sur une case jamais sondée.",
        "**[[archivist_wreck_6:2]] se juge à l'arrivée**, pas au départ : comptez le temps de vol.",
        "**Le registre ne couvre que les vaisseaux perdus au combat**, dans la limite des quantités perdues et pendant 7 jours (21 avec [[archivist_registry_3:2]]). Les défenses n'y entrent pas.",
        "**[[archivist_registry_3:1]] ne dure que 24 h** après la dernière perte.",
    ],
    'related': [
        "[Dynasties](/fr/dynasty/dynasties)", "[Classes](/fr/dynasty/classes)", "[Les talents](/fr/dynasty/talents)",
        "[Arbre commun](/fr/dynasty/common-tree)", "[Champs de débris](/fr/combat/debris)", "[Liste des technologies](/fr/research/technologies)",
    ],
}

EN = {
    'brief': "\"Nothing is lost\". The Archivist recovers what others leave behind: knowledge someone already found ([[b:memory]]), battle wreckage ([[b:wreck]]), and its own fleet when it falls ([[b:registry]]).",
    'rules': [
        "**Known level**: a research level already held, at that level or higher, by **25%** of the universe's counted players. Counted players are those active in the last 7 days, not in vacation mode and not bots. The count is redone once a day. The whole [[b:memory]] branch only affects these levels.",
        "The speed of a known level ([[archivist_memory_1]], [[archivist_memory_4]]) and that of [[archivist_registry_8]] **add** to your research speed, outside its caps. Speed, cost and known status are set when the study **starts**.",
        "**Debris harvests**: the bonus applies to the metal and crystal your Salvagers actually load, so within their hold. It is paid on return, takes no hold space and takes nothing more from the field.",
        "**Loss registry**: the registry, shared by your whole empire, lists the ships lost in combat, those of a fleet as well as those defending a planet. Defences never enter it. An order placed from the registry, on any planet, gets the registry's terms within the quantities it holds, drawing first on the oldest losses.",
        "The registry's speed **adds** to the ships' build speed: a duration is divided by (1 + sum of bonuses). The registry's cost reduction applies **on the price already reduced** by your other ship reductions.",
        "The class's only **accent** is the speed of recycling missions ([[archivist_wreck_3:2]]), within the talents' fleet speed budget. The dock, combat recycling and debris hydrogen belong to the Admiral; defences to the Veteran.",
    ],
    'example': """**[[b:memory]]**: Weapon Systems 10 (409,600 metal, 102,400 crystal), universe research speed ×1, Innovation Center 10: **46 h 32 min 44 s** with no talent. The level is known.
- [[archivist_memory_1]] (+10%): **42 h 18 min 51 s**.
- With [[archivist_memory_4]] at rank 3 (+25% in total): **37 h 14 min 12 s**. With [[archivist_memory_6:1]], 5 or more levels behind (+40%): **33 h 14 min 49 s**.
- [[archivist_memory_2]] at rank 3 (−12%): **360,448** metal and **90,112** crystal.
- [[archivist_memory_5]]: Weapon Systems 11, if known, takes 93 h 05 min 27 s, brought down to 74 h 28 min 22 s by the +25%. It starts with 10% of that time done, **7 h 26 min 50 s**; with [[archivist_memory_7]] at rank 3 (25%), **18 h 37 min 05 s**.
- The same Weapon Systems 10, started within 24 h of a defeat with [[archivist_registry_8]]: 25 + 20 = 45% → **32 h 06 min 02 s**.

**[[b:wreck]]**: 100 Corvettes destroyed, universe with 30% debris (Redline): 600,000 metal and 210,000 crystal, that is 810,000 resources. It takes 41 Salvagers (20,000 hold each, without Hyperspace Technology).
- [[archivist_wreck_1]] and [[archivist_wreck_4]] at rank 3 (+25%): +150,000 metal and +52,500 crystal, **1,012,500** brought back. The field loses 810,000, no more.
- Arriving less than 1 h after the battle, with [[archivist_wreck_6:2]] (+45%): **1,174,500**.
- With only 30 Salvagers (600,000 hold): 444,444 metal and 155,555 crystal loaded pro rata, the bonus applies to them; 210,001 resources stay in the field.

**[[b:registry]]**: 200 Corvettes lost, that is 4,000,000 metal, 1,400,000 crystal and 400,000 hydrogen (5,800,000 resources).
- [[archivist_registry_5]]: 5% of their price, that is **290,000** resources paid at once (200,000 / 70,000 / 20,000); **464,000** with [[archivist_registry_7]] at rank 3 (8%).
- [[archivist_registry_2]] at rank 3 (−12%): 4,000,000 → **3,520,000** metal; with [[archivist_registry_6:2]] (−20% in total), **3,200,000**.
- A rebuild taking 10 h with no talent: **8 h 41 min 45 s** with [[archivist_registry_1]] (+15%), **7 h 41 min 33 s** with [[archivist_registry_4]] at rank 3 (+30%), **6 h 40 min** with [[archivist_registry_6:1]] (+50%). With [[archivist_registry_3:1]] on top, within 24 h of the loss (+70%): **5 h 52 min 57 s**.""",
    'branch_notes': {
        'memory': """- **[[archivist_memory_3:1]]**: a level another member of your alliance holds, at that level or higher. **[[archivist_memory_6:2]]**: the player ranked just above you in the general ranking. Both lists are read again once a day.
- **[[archivist_memory_5]]**: the completed level must be known, and the next one known when you start it. The head start is a share of the study's real duration and adds past the Theorist's head start ceiling. One momentum at a time: completing another known level replaces it.
- **[[archivist_memory_6:1]]**: the most common level is the one the most counted players hold exactly (the lowest on a tie). Only the [[archivist_memory_4]] share counts double: 10 + 15 × 2 = 40%.
- **[[archivist_memory_8]]** only waives the required Innovation Center level: the planet must still have an Innovation Center.
- **[[archivist_memory_9]]**: a single counted player is enough. A level held only by bots or by inactive or vacationing players does not become known this way.""",
        'wreck': """- **[[archivist_wreck_2]]**: up to 15 systems around each of your planets, in the same galaxy.
- **[[archivist_wreck_3:1]]**: you may recycle any cell without having scouted it, whether the radar shows it or not.
- **[[archivist_wreck_5]]** rings every time a field in your radar receives debris and exceeds 50,000 resources, even if it already did. Not for a field another player has sealed.
- **[[archivist_wreck_6:1]]**: after an attack on your planet, its Salvagers still docked harvest the whole field above it, old debris included, before the attacker's. Metal and crystal go straight to the stock, with the [[archivist_wreck_1]] and [[archivist_wreck_4]] bonus.
- **[[archivist_wreck_6:2]]** is measured from the last debris added to the field to the **arrival** of your Salvagers. It adds to the 25% of [[archivist_wreck_1]] and [[archivist_wreck_4]], past their cap.
- **[[archivist_wreck_7]]**: the Salvagers leave from your nearest planet that has some, within radar range, as many as the field needs, at full speed. No departure if one of your fleets already targets that cell. The 24 h count opens at the first departure. A departure refused by the flight rules (hydrogen, fleet slots, cell never scouted without [[archivist_wreck_3:1]]) costs nothing.
- **[[archivist_wreck_8]]** sweeps the neighbouring fields after the targeted one, in the hold space left, except a field sealed by another player.
- **[[archivist_wreck_9]]**: a non-empty field you see, a cell scouted by you or your alliance, or covered by your radar. The 24 h are counted from the last seal. Impossible on a field already sealed by another player.""",
        'registry': """- **[[archivist_registry_3:1]]** counts 24 h from **the last** loss still in the registry.
- **[[archivist_registry_5]]** is computed on the normal price of the ships lost, resource by resource, and goes to the planet the fleet left from, or to the defended planet, if it is still yours.
- **[[archivist_registry_8]]**: a defeat is a planet attack, attacking or defending, where you lost more unit points (ships and defences) than the opponent. Only studies started during those 24 h go faster: a study already running does not change. Each new defeat restarts the 24 h.
- **[[archivist_registry_9]]**: registry orders get their own queue, alongside the normal ship queue.""",
    },
    'caps_note': "Two bonuses go past these caps: [[archivist_memory_6:1]] takes a known level's speed to 40%, and [[archivist_wreck_6:2]] adds 20 points to harvests on a fresh field (45%).",
    'builds': """| Build | Split | What it gets |
|---|---|---|
| The catcher-up | [[b:memory]] 15 · [[b:registry]] 10 | [[archivist_memory_9]], [[archivist_memory_8]]; known levels +25% (+40% with [[archivist_memory_6:1]]) and −12%, 25% head start on each chained level; registry +50% with [[archivist_registry_6:1]] (otherwise +30% and −20% with [[archivist_registry_6:2]]), [[archivist_registry_2]] −12%, [[archivist_registry_5]] 5% |
| The scavenger | [[b:wreck]] 15 · [[b:memory]] 10 | [[archivist_wreck_9]], [[archivist_wreck_5]], [[archivist_wreck_7]], [[archivist_wreck_8]]; harvests +25%; known levels +25% and −12%, [[archivist_memory_5]] 10% |
| The unbreakable | [[b:registry]] 15 · [[b:wreck]] 10 | [[archivist_registry_9]], [[archivist_registry_5]] 8%, [[archivist_registry_8]], registry up to +70%; harvests +25%, radar at 15 systems, [[archivist_wreck_6:1]] or [[archivist_wreck_6:2]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**A known level is judged on counted players** (active within 7 days, not on vacation, not bots), and the count is only redone once a day.",
        "**The first on a research gets nothing from Memory** on that research: nobody is ahead of them.",
        "**Everything is set at start**: a level becoming known during the study does not speed it up, and [[archivist_registry_8]] does not speed up a study already running.",
        "**[[archivist_memory_3:2]] becomes useless with [[archivist_memory_9]]**, which already asks for less: a single holder.",
        "**The harvest bonus follows the hold**: it applies to what your Salvagers load, not to the whole field. It does not drain the field further: other players can still harvest what is left.",
        "**[[archivist_wreck_7]] without [[archivist_wreck_3:1]]** fails on a cell never scouted.",
        "**[[archivist_wreck_6:2]] is judged on arrival**, not on departure: count the flight time.",
        "**The registry only covers ships lost in combat**, within the quantities lost and for 7 days (21 with [[archivist_registry_3:2]]). Defences do not enter it.",
        "**[[archivist_registry_3:1]] only lasts 24 h** after the last loss.",
    ],
    'related': [
        "[Dynasties](/en/dynasty/dynasties)", "[Classes](/en/dynasty/classes)", "[Talents](/en/dynasty/talents)",
        "[Common tree](/en/dynasty/common-tree)", "[Debris fields](/en/combat/debris)", "[Technology list](/en/research/technologies)",
    ],
}
