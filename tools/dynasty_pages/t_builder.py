"""Le Bâtisseur : textes vérifiés sur le code (backend 7b255c83, notes du 15 octobre 2026 ; branche Filon et Achats groupés revus sur 59b01c6a le 17 octobre 2026)."""

FR = {
    'brief': "le Bâtisseur est la classe de l'économie de chantier. Ses mines rapportent plus que leur niveau, son chantier avance pendant que ses files sont vides, et chaque niveau qu'il connaît déjà lui coûte moins cher. Filon fait produire les mines ; Chantier met de côté le temps perdu ; Fonderie réduit les prix et protège ce qui attend dans la file.",
    'rules': [
        "Les bonus génériques (production des mines, vitesse de construction, entrepôts, Maîtrise du Plasma) viennent de l'[arbre commun](/fr/dynasty/common-tree). Le Bâtisseur n'a que des **mécaniques**, un accent de coût ([[builder_foundry_3:1]], 5 % sur les bâtiments, ou [[builder_foundry_3:2]], 10 % sur les défenses) et un accent de vitesse de construction, [[builder_yard_4]], limité aux colonies qui rattrapent la planète mère.",
        "Les niveaux en plus de [[builder_lode_3:1]], [[builder_lode_3:2]], [[builder_lode_5]] et [[builder_lode_7]] ne valent que pour les trois mines (Excavateur minéral, Extracteur cristallin, Condensateur d'hydrogène) et seulement pour leur production : la mine consomme toujours l'énergie de son niveau réel. Chaque mine gagne 1 niveau de production par [[builder_lode_3:1]] ou [[builder_lode_3:2]]. La **mine du jour** de [[builder_lode_4]], tant que son jour court, en gagne 1 de plus par [[builder_lode_5]], dès son premier niveau, et encore 1 par [[builder_lode_7]] à partir du niveau 30 (25, 20 puis 15 aux rangs 1 à 3) : 3 niveaux au plus.",
        "[[builder_lode_1]], [[builder_lode_4]] et [[builder_lode_9]] se calculent sur la **production propre de la mine** : à son niveau de production (niveaux en plus compris), à son taux de fonctionnement et à la vitesse de l'univers, sans Maîtrise du Plasma ni aucun autre bonus en pourcentage. [[builder_lode_4]] et [[builder_lode_9]] s'ajoutent à la production de la planète et subissent comme elle un manque d'énergie ; le versement de [[builder_lode_1]] n'en dépend pas.",
        "« Une fois par jour » veut dire 24 h après la dernière utilisation, pour tout votre empire ([[builder_lode_9]], [[builder_yard_9]]). [[builder_foundry_9]] revient 7 jours après le paiement de l'ordre désigné.",
    ],
    'example': """Univers à vitesse 1. Un Excavateur minéral produit 30 × N × 1,1^N métal par heure et consomme 10 × N × 1,1^N d'énergie : 4 036 métal et 1 345 d'énergie au niveau 20, 4 662 métal et 1 554 d'énergie au niveau 21.

**Filon complet sur la planète mère ([[builder_lode_3:1]], l'Excavateur étant la mine du jour)**
- L'Excavateur passe au niveau 21. Il produit comme un niveau 24 (21 + 1 par [[builder_lode_3:1]] + 1 par [[builder_lode_5]] + 1 par [[builder_lode_7]], seuil abaissé à 15) : 30 × 24 × 1,1^24 = **7 091 métal par heure**, pour l'énergie d'un niveau 21 (1 554). Le lendemain, s'il n'est plus la mine du jour, il produit comme un niveau 22 : 5 372.
- [[builder_lode_1]] et [[builder_lode_2]] (4 h) : 4 × 7 091 = **28 364 métal** versés à la fin du niveau.
- [[builder_lode_4]] au rang 3 : 7 091 × 15 % = 1 063 (arrondi inférieur) de plus par heure, soit **25 512 métal** sur les 24 h, à pleine énergie.
- [[builder_lode_9]] (production doublée) : 7 091 × 4 = **28 364 métal** de plus en 4 h, à pleine énergie.

**[[builder_lode_7]] et [[builder_lode_3:2]], sur une colonie**
- Avec [[builder_lode_7]] au rang 3, son niveau en plus joue dès le niveau 15. Un Excavateur 15, mine du jour, produit comme un niveau 18 : **3 002 métal par heure** au lieu de 1 879, pour l'énergie d'un niveau 15 (626). Les autres jours, il produit comme un niveau 16 : 2 205.

**Fonderie : un niveau déjà connu**
- Excavateur 25 sur une colonie, niveau déjà atteint sur la planète mère : 1 010 046 métal et 252 511 cristal au prix du catalogue.
- [[builder_foundry_1]] et [[builder_foundry_4]] (25 %) plus [[builder_foundry_3:1]] (5 %) : 30 % de moins, arrondi à l'unité supérieure, soit **707 033 métal** et **176 758 cristal**.
- Si cet Excavateur est la mine du jour et que vous avez [[builder_lode_6:2]] : 45 % de moins, soit **555 526 métal** et **138 882 cristal**.
- Désigné pour [[builder_foundry_9]] : la moitié de ce prix déjà réduit, **353 517 métal** et **88 379 cristal**, 35 % du prix du catalogue. Les points se comptent toujours sur le prix du catalogue.

**Chantier : une nuit de 8 h, file de bâtiments vide**
- Avec [[builder_yard_7]] au rang 3 (80 %) et [[builder_yard_6:2]] (5 h) : 8 h × 80 % = 6 h 24, ramenées au plafond, soit **5 h** versées d'office à l'ordre lancé au réveil.
- Avec [[builder_yard_6:1]] (8 h) : **6 h 24** gardées, à verser sur l'ordre en cours de votre choix.

**[[builder_lode_8]]**
- Le hangar de cristal est plein et 10 000 cristal produits débordent. Le métal est choisi et son hangar a de la place : 10 000 × 1,5 × 50 % = **7 500 métal**. Si le cristal était la ressource choisie, ces 10 000 seraient perdus.""",
    'branch_notes': {
        'lode': """- **[[builder_lode_1]]** : chaque niveau terminé d'une mine verse ses heures de production, y compris le niveau offert par [[builder_foundry_2]]. Le versement va directement dans le stock de la planète.
- **[[builder_lode_3:1]]** vaut pour la planète mère, **[[builder_lode_3:2]]** pour chaque colonie, dès le niveau 1 de la mine.
- **[[builder_lode_4]]** : le tirage se fait parmi toutes les mines debout de toutes vos planètes (pas les lunes), chacune avec la même chance quel que soit son niveau. Une nouvelle mine du jour est tirée peu après la fin des 24 h.
- **[[builder_lode_5]]** ne vaut que pour la mine du jour, sur sa planète, tant que son jour court ; les autres mines n'en tirent rien.
- **[[builder_lode_6:1]]** : votre choix remplace la mine tirée et part pour 24 h ; vous rechoisissez à la fin de ces 24 h. Sans choix, le tirage continue.
- **[[builder_lode_6:2]]** : la baisse s'additionne aux autres réductions de bâtiment ([[builder_foundry_1]], [[builder_foundry_3:1]]…) et compte au moment où vous lancez l'amélioration ; la mine doit être la mine du jour à cet instant.
- **[[builder_lode_7]]** se déclenche sur le niveau réel de la mine (30, puis 25, 20 et 15 aux rangs 1 à 3), pas sur son niveau de production, et seulement sur la mine du jour.
- **[[builder_lode_8]]** : seul le débordement des deux autres ressources est converti, à valeur égale, arrondi à l'inférieur, et seulement dans la place libre du hangar de la ressource choisie (le métal tant que vous n'avez rien choisi). Le choix se fait planète par planète. Il ne joue que sur la production, et après [[common_prosperity_8:2]] (arbre commun).
- **[[builder_lode_9]]** : l'Excavateur minéral, l'Extracteur cristallin ou le Condensateur d'hydrogène, au moment que vous choisissez.""",
        'yard': """- **[[builder_yard_1]]** : l'avance se met de côté planète par planète, tant que sa file de bâtiments est vide. Elle est versée d'office à la prochaine construction ou démolition lancée sur cette file vide, et **toute** l'avance part, même si l'ordre est plus court qu'elle.
- **[[builder_yard_3:1]]** ne joue que sur un ordre de la file qui démarre de lui-même. **[[builder_yard_3:2]]** ne joue que sur un ordre lancé sur une file vide : 30 min, ou 5 % de sa durée si c'est plus, sans dépasser la moitié de sa durée.
- **[[builder_yard_4]]** vaut aussi pour le niveau égal à celui de la planète mère. Il s'ajoute à la vitesse de construction de l'arbre commun ; une durée se divise par (1 + vitesse).
- **[[builder_yard_5]]** : la planète a une seule réserve, qui se remplit tant que l'un au moins de ses deux chantiers (bâtiments, Dock orbital) est vide, au même rythme. Un ordre de vaisseaux ou de défenses lancé sur un Dock orbital vide n'en prend que sa propre durée.
- **[[builder_yard_6:1]]** : le plafond passe à 8 h à la place des 5 h ([[builder_yard_2]] n'y ajoute plus rien). Vous versez l'avance sur un ordre en cours de la planète (vaisseaux et défenses avec [[builder_yard_5]]), au plus ce qu'il lui reste.
- **[[builder_yard_8]]** : le versement vers une autre planète se fait à la main, aussi avec [[builder_yard_6:2]] ; tous les apports d'autres planètes réunis ne dépassent pas 50 % de la durée de l'ordre.
- **[[builder_yard_9]]** ne touche que le chantier de bâtiments. L'ordre en cours gagne aussitôt jusqu'à 4 h (au plus la moitié de ce qui lui reste) ; un ordre qui démarre pendant la fenêtre gagne de même sur ce qu'il reste de la fenêtre.""",
        'foundry': """- **[[builder_foundry_1]]** : le niveau doit être atteint sur une **autre** de vos planètes ou lunes. Les réductions de bâtiment s'additionnent ([[builder_foundry_1]], [[builder_foundry_4]], [[builder_foundry_3:1]] : 30 % au plus, 45 % sur la mine du jour avec [[builder_lode_6:2]]) ; le prix est arrondi à l'unité supérieure.
- **[[builder_foundry_3:2]]** : 10 % sur toutes les défenses, hors plafond de coût de la classe ; les vaisseaux ne sont plus concernés.
- **[[builder_foundry_2]]** : seulement après une amélioration (pas une démolition), et si le niveau suivant est possible (niveau maximal, case libre).
- **[[builder_foundry_5]]** : l'ordre protégé est le premier ordre **en attente** dans la file de la planète, pas celui en cours (déjà payé), ni une démolition. La part abritée, au plus le stock, est retirée de ce qui peut être pillé ; le taux de pillage s'applique ensuite au reste.
- **[[builder_foundry_6:1]]** : il faut au moins 90 % de **chaque** ressource. Tout le stock disponible part, le manque devient une dette prélevée sur le stock dès qu'il se remplit, avant toute autre dépense. Pas de nouveau crédit tant qu'une dette court. **[[builder_foundry_6:2]]** paie en métal le cristal et l'hydrogène qui manquent, s'il y a assez de métal. Les deux ne valent que pour les bâtiments.
- **[[builder_foundry_9]]** : vous désignez sur une planète le prochain niveau d'un bâtiment ; le prix baisse dès la désignation, que vous pouvez changer tant que l'ordre n'est pas payé. La remise porte sur le prix déjà réduit par les autres talents.""",
    },
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur | Filon 15 · Fonderie 10 | [[builder_lode_9]], la mine du jour à 3 niveaux de plus dès le niveau 15, 4 h de production à chaque niveau de mine, [[builder_lode_4]] à 15 % sur une mine choisie ([[builder_lode_6:1]]) ou −15 % sur son amélioration ([[builder_lode_6:2]]), [[builder_lode_8]] ; niveaux connus −25 % (−30 % avec [[builder_foundry_3:1]]), [[builder_foundry_2]] 6 %, [[builder_foundry_5]] 30 % |
| Contremaître absent | Chantier 15 · Filon 10 | réserve de 80 % du temps vide, 5 h ([[builder_yard_6:2]]) ou 8 h ([[builder_yard_6:1]]) par planète, Dock orbital compris, [[builder_yard_4]] 15 %, [[builder_yard_8]], [[builder_yard_9]] ; 4 h de production à chaque niveau de mine, [[builder_lode_4]] 15 %, [[builder_lode_5]] sur la mine du jour |
| Colonisateur | Fonderie 15 · Chantier 10 | [[builder_foundry_9]], [[builder_foundry_8]], [[builder_foundry_5]] jusqu'à 60 %, niveaux connus −25 % ; réserve de 50 % du temps vide jusqu'à 5 h ou 8 h, [[builder_yard_4]] 15 % sur les colonies, [[builder_yard_5]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Le Chantier récompense les files vides** : l'avance n'est versée d'office qu'à un ordre lancé sur une file vide. Un joueur qui garde sa file pleine profite surtout de [[builder_yard_3:1]] et de [[builder_yard_9]].",
        "**Une avance plus longue que l'ordre est perdue** : lancer un bâtiment de 10 min avec 5 h de réserve consomme les 5 h. Avec [[builder_yard_6:1]], versez-la à la main sur un gros ordre.",
        "**[[builder_lode_1]], [[builder_lode_4]] et [[builder_lode_9]] ignorent la Maîtrise du Plasma** : ils portent sur la production propre de la mine. Une planète en manque d'énergie réduit aussi [[builder_lode_4]] et [[builder_lode_9]].",
        "**Les niveaux de production en plus ne coûtent pas d'énergie** : la mine consomme celle de son niveau réel.",
        "**[[builder_lode_8]] ne sauve pas la ressource choisie** : son propre débordement est perdu, et rien n'est converti quand son hangar est plein.",
        "**[[builder_foundry_1]] ne vaut que pour un niveau déjà atteint** sur une autre de vos planètes (ou chez un membre de votre alliance avec [[builder_foundry_8]]) : la planète la plus avancée paie plein tarif.",
        "**[[builder_foundry_5]] protège l'ordre en attente** : gardez un ordre en file derrière celui en cours. Au plus 60 % de son coût, jamais plus que le stock ; le pillard prend son taux sur le reste.",
        "**Les réductions de coût ne changent pas les points** : points et expérience se calculent sur le prix du catalogue.",
    ],
    'related': [
        "[Les talents](/fr/dynasty/talents)", "[Arbre commun](/fr/dynasty/common-tree)", "[Classes](/fr/dynasty/classes)",
        "[Les ressources](/fr/economy/resources)", "[Files de construction](/fr/economy/build-queue)",
        "[Pillage](/fr/combat/plunder)",
    ],
}

EN = {
    'brief': "the Builder is the class of the construction economy. Its mines pay more than their level, its yard moves forward while its queues are empty, and every level it already knows costs it less. Lode makes the mines produce; Yard banks lost time; Foundry cuts prices and protects what waits in the queue.",
    'rules': [
        "Generic bonuses (mine production, construction speed, storage, Plasma Technology) come from the [common tree](/en/dynasty/common-tree). The Builder only has **mechanics**, a cost accent ([[builder_foundry_3:1]], 5% on buildings, or [[builder_foundry_3:2]], 10% on defences) and a construction speed accent, [[builder_yard_4]], limited to colonies catching up with the home planet.",
        "The extra levels of [[builder_lode_3:1]], [[builder_lode_3:2]], [[builder_lode_5]] and [[builder_lode_7]] only apply to the three mines (Mineral Excavator, Crystal Extractor, Hydrogen Condenser) and only to their production: the mine still draws the energy of its real level. Every mine gains 1 production level from [[builder_lode_3:1]] or [[builder_lode_3:2]]. The **mine of the day** of [[builder_lode_4]], while its day runs, gains 1 more from [[builder_lode_5]], from its first level, and 1 more again from [[builder_lode_7]] from level 30 (25, 20 then 15 at ranks 1 to 3): 3 levels at most.",
        "[[builder_lode_1]], [[builder_lode_4]] and [[builder_lode_9]] are computed on the **mine's own production**: at its production level (extra levels included), its operating rate and the universe speed, without Plasma Technology or any other percentage bonus. [[builder_lode_4]] and [[builder_lode_9]] add to the planet's production and, like it, suffer from an energy shortfall; the [[builder_lode_1]] payout does not.",
        "\"Once a day\" means 24 h after the last use, for your whole empire ([[builder_lode_9]], [[builder_yard_9]]). [[builder_foundry_9]] comes back 7 days after the designated order is paid.",
    ],
    'example': """Universe at speed 1. A Mineral Excavator produces 30 × N × 1.1^N metal per hour and draws 10 × N × 1.1^N energy: 4,036 metal and 1,345 energy at level 20, 4,662 metal and 1,554 energy at level 21.

**Full Lode on the home planet ([[builder_lode_3:1]], the Excavator being the mine of the day)**
- The Excavator reaches level 21. It produces as a level 24 (21 + 1 from [[builder_lode_3:1]] + 1 from [[builder_lode_5]] + 1 from [[builder_lode_7]], threshold lowered to 15): 30 × 24 × 1.1^24 = **7,091 metal per hour**, for the energy of a level 21 (1,554). The next day, if it is no longer the mine of the day, it produces as a level 22: 5,372.
- [[builder_lode_1]] and [[builder_lode_2]] (4 h): 4 × 7,091 = **28,364 metal** paid when the level ends.
- [[builder_lode_4]] at rank 3: 7,091 × 15% = 1,063 (rounded down) more per hour, that is **25,512 metal** over the 24 h, at full energy.
- [[builder_lode_9]] (production doubled): 7,091 × 4 = **28,364 more metal** in 4 h, at full energy.

**[[builder_lode_7]] and [[builder_lode_3:2]], on a colony**
- With [[builder_lode_7]] at rank 3, its extra level applies from level 15. A level 15 Excavator, mine of the day, produces as a level 18: **3,002 metal per hour** instead of 1,879, for the energy of a level 15 (626). On other days, it produces as a level 16: 2,205.

**Foundry: an already known level**
- Level 25 Excavator on a colony, a level the home planet already reached: 1,010,046 metal and 252,511 crystal at catalogue price.
- [[builder_foundry_1]] and [[builder_foundry_4]] (25%) plus [[builder_foundry_3:1]] (5%): 30% less, rounded up, that is **707,033 metal** and **176,758 crystal**.
- If this Excavator is the mine of the day and you have [[builder_lode_6:2]]: 45% less, that is **555,526 metal** and **138,882 crystal**.
- Designated for [[builder_foundry_9]]: half of this already reduced price, **353,517 metal** and **88,379 crystal**, 35% of the catalogue price. Points are still counted on the catalogue price.

**Yard: an 8 h night, empty building queue**
- With [[builder_yard_7]] at rank 3 (80%) and [[builder_yard_6:2]] (5 h): 8 h × 80% = 6 h 24 min, brought down to the ceiling, that is **5 h** paid automatically to the order started in the morning.
- With [[builder_yard_6:1]] (8 h): **6 h 24 min** kept, to pay onto the running order of your choice.

**[[builder_lode_8]]**
- The crystal storage is full and 10,000 crystal produced overflow. Metal is chosen and its storage has room: 10,000 × 1.5 × 50% = **7,500 metal**. Had crystal been the chosen resource, those 10,000 would be lost.""",
    'branch_notes': {
        'lode': """- **[[builder_lode_1]]**: every completed level of a mine pays its hours of production, including the level granted by [[builder_foundry_2]]. The payout goes straight into the planet's stock.
- **[[builder_lode_3:1]]** applies to the home planet, **[[builder_lode_3:2]]** to every colony, from the mine's level 1.
- **[[builder_lode_4]]**: the draw is made among all standing mines of all your planets (not moons), each with the same chance whatever its level. A new mine of the day is drawn shortly after the 24 h end.
- **[[builder_lode_5]]** only applies to the mine of the day, on its planet, while its day runs; the other mines get nothing from it.
- **[[builder_lode_6:1]]**: your choice replaces the drawn mine and lasts 24 h; you choose again when those 24 h end. Without a choice, the draw goes on.
- **[[builder_lode_6:2]]**: the cut adds to the other building reductions ([[builder_foundry_1]], [[builder_foundry_3:1]]…) and counts when you start the upgrade; the mine must be the mine of the day at that moment.
- **[[builder_lode_7]]** triggers on the mine's real level (30, then 25, 20 and 15 at ranks 1 to 3), not its production level, and only on the mine of the day.
- **[[builder_lode_8]]**: only the overflow of the two other resources is converted, at equal value, rounded down, and only into the free space of the chosen resource's storage (metal as long as you have chosen nothing). The choice is made planet by planet. It only applies to production, and after [[common_prosperity_8:2]] (common tree).
- **[[builder_lode_9]]**: the Mineral Excavator, Crystal Extractor or Hydrogen Condenser, at the time you choose.""",
        'yard': """- **[[builder_yard_1]]**: the head start is banked planet by planet, while its building queue is empty. It is paid automatically to the next construction or demolition started on that empty queue, and the **whole** head start goes, even if the order is shorter than it.
- **[[builder_yard_3:1]]** only applies to a queued order that starts on its own. **[[builder_yard_3:2]]** only applies to an order started on an empty queue: 30 min, or 5% of its duration if that is more, never past half its duration.
- **[[builder_yard_4]]** also applies to the level equal to the home planet's. It adds to the common tree's construction speed; a duration is divided by (1 + speed).
- **[[builder_yard_5]]**: the planet has a single bank, which fills while at least one of its two yards (buildings, Orbital Dock) is empty, at the same rate. A ship or defense order started on an empty Orbital Dock only takes its own duration from it.
- **[[builder_yard_6:1]]**: the ceiling becomes 8 h instead of 5 h ([[builder_yard_2]] no longer adds anything). You pay the head start onto a running order of the planet (ships and defenses with [[builder_yard_5]]), at most what it has left.
- **[[builder_yard_8]]**: paying another planet is done by hand, also with [[builder_yard_6:2]]; all contributions from other planets together never exceed 50% of the order's duration.
- **[[builder_yard_9]]** only affects the building yard. The running order gains up to 4 h at once (at most half of what it has left); an order starting during the window gains the same way on what is left of the window.""",
        'foundry': """- **[[builder_foundry_1]]**: the level must be reached on **another** of your planets or moons. Building reductions add up ([[builder_foundry_1]], [[builder_foundry_4]], [[builder_foundry_3:1]]: 30% at most, 45% on the mine of the day with [[builder_lode_6:2]]); the price is rounded up.
- **[[builder_foundry_3:2]]**: 10% on every defence, outside the class's cost cap; ships are no longer covered.
- **[[builder_foundry_2]]**: only after an upgrade (not a demolition), and if the next level is possible (maximum level, free field).
- **[[builder_foundry_5]]**: the protected order is the first order **waiting** in the planet's queue, not the running one (already paid), nor a demolition. The sheltered share, at most the stock, is removed from what can be plundered; the plunder rate then applies to the rest.
- **[[builder_foundry_6:1]]**: you need at least 90% of **each** resource. The whole available stock goes, the shortfall becomes a debt taken from the stock as soon as it fills, before any other spending. No new credit while a debt runs. **[[builder_foundry_6:2]]** pays missing crystal and hydrogen in metal, if there is enough metal. Both only apply to buildings.
- **[[builder_foundry_9]]**: you designate on a planet the next level of a building; the price drops as soon as it is designated, and you can change it until the order is paid. The discount applies to the price already reduced by the other talents.""",
    },
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Miner | Lode 15 · Foundry 10 | [[builder_lode_9]], the mine of the day 3 levels higher from level 15, 4 h of production at every mine level, [[builder_lode_4]] at 15% on one chosen mine ([[builder_lode_6:1]]) or −15% on its upgrade ([[builder_lode_6:2]]), [[builder_lode_8]]; known levels −25% (−30% with [[builder_foundry_3:1]]), [[builder_foundry_2]] 6%, [[builder_foundry_5]] 30% |
| Absent Foreman | Yard 15 · Lode 10 | bank of 80% of idle time, 5 h ([[builder_yard_6:2]]) or 8 h ([[builder_yard_6:1]]) per planet, Orbital Dock included, [[builder_yard_4]] 15%, [[builder_yard_8]], [[builder_yard_9]]; 4 h of production at every mine level, [[builder_lode_4]] 15%, [[builder_lode_5]] on the mine of the day |
| Colonizer | Foundry 15 · Yard 10 | [[builder_foundry_9]], [[builder_foundry_8]], [[builder_foundry_5]] up to 60%, known levels −25%; bank of 50% of idle time up to 5 h or 8 h, [[builder_yard_4]] 15% on colonies, [[builder_yard_5]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**The Yard rewards empty queues**: the head start is only paid automatically to an order started on an empty queue. A player who keeps their queue full mostly benefits from [[builder_yard_3:1]] and [[builder_yard_9]].",
        "**A head start longer than the order is lost**: starting a 10 min building with 5 h banked uses up the 5 h. With [[builder_yard_6:1]], pay it by hand onto a big order.",
        "**[[builder_lode_1]], [[builder_lode_4]] and [[builder_lode_9]] ignore Plasma Technology**: they apply to the mine's own production. An energy shortfall also reduces [[builder_lode_4]] and [[builder_lode_9]].",
        "**Extra production levels cost no energy**: the mine draws that of its real level.",
        "**[[builder_lode_8]] does not save the chosen resource**: its own overflow is lost, and nothing is converted when its storage is full.",
        "**[[builder_foundry_1]] only covers a level already reached** on another of your planets (or by a member of your alliance with [[builder_foundry_8]]): your most advanced planet pays full price.",
        "**[[builder_foundry_5]] protects the waiting order**: keep an order queued behind the running one. At most 60% of its cost, never more than the stock; the raider takes their rate on the rest.",
        "**Cost reductions do not change points**: points and experience are computed on the catalogue price.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Common tree](/en/dynasty/common-tree)", "[Classes](/en/dynasty/classes)",
        "[Resources](/en/economy/resources)", "[Build queues](/en/economy/build-queue)",
        "[Plunder](/en/combat/plunder)",
    ],
}
