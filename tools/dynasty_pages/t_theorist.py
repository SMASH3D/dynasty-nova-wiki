"""Le Théoricien : textes vérifiés sur le code (note du 15 octobre 2026, backend 7b255c83)."""

FR = {
    'brief': "« Comprendre avant ». Le Théoricien a toujours une étude en cours et un niveau d'avance. [[b:method]] fait que sa file de recherche ne s'arrête jamais, [[b:network]] met en commun les Centres d'innovation de ses colonies, [[b:prototypes]] lui fait profiter d'un niveau de recherche avant tout le monde.",
    'rules': [
        "La vitesse de recherche générique et la seconde étude en parallèle ([[common_exploration_10]]) sont dans l'[arbre commun](/fr/dynasty/common-tree). L'arbre du Théoricien ne contient que des mécaniques qui lui sont propres. Ses deux **accents** sont la vitesse de construction des Centres d'innovation ([[theorist_network_4]]) et le coût des niveaux de recherche à partir du 11e ([[theorist_prototypes_6:1]]).",
        "**Avances au départ.** Une étude peut partir avec une partie de son temps déjà écoulée. [[theorist_method_1]] ou [[theorist_method_2]], plus [[theorist_method_3:1]] et [[theorist_network_6:2]], ne dépassent jamais **10 %** de l'étude à eux tous. [[theorist_network_9]], [[theorist_method_3:2]] et l'Élan de l'Archiviste s'ajoutent au-delà. Aucune avance n'achève une étude.",
        "**Réseau d'étude.** Sans talent, [Collaboration Stellaire](/fr/research/stellar-collaboration) niveau N met en commun les N meilleurs Centres d'innovation de vos autres planètes, s'ils sont au moins aussi avancés que celui qui étudie. Le réseau raccourcit l'étude, jamais son coût.",
        "**Prototype.** Un prototype fait valoir une recherche des niveaux de plus pendant un temps, partout où le jeu lit son niveau (emplacements de flotte, nombre de planètes, Centres du réseau, combat...), sans dépasser son niveau maximum. Il ne s'applique qu'à une recherche étudiée au moins une fois. Les trois **technologies de combat** (Systèmes Offensifs, Champs de Protection, Métallurgie Avancée) n'ont de prototype d'étude qu'avec [[theorist_prototypes_3:1]].",
        "Prototype, [[theorist_prototypes_8]] et [[theorist_prototypes_9]] **ne s'additionnent pas** sur une même recherche : elle prend le plus grand des trois bonus.",
        "Les réductions de coût des recherches ([[theorist_method_4]], [[theorist_prototypes_6:1]], [[theorist_prototypes_4]]) s'additionnent, puis chaque ressource est arrondie à l'unité supérieure. Elles ne raccourcissent pas l'étude, dont la durée se calcule sur le prix normal.",
    ],
    'example': """Étude de référence : **Systèmes Offensifs 10** (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 sur la planète qui étudie : 512 000 / (1 000 × 11) h = **46 h 32 min 44 s**.

**[[b:method]]**
- [[theorist_method_1]] : l'étude, lancée à la suite de la précédente dans la file, part avec 10 % de son temps écoulé : il reste **41 h 53 min 28 s**.
- Lancée à la main après 10 h de file vide, avec [[theorist_method_2]] au rang 3 et [[theorist_method_3:1]] : 9 % (4 h 11 min 20 s) plus 2 h mises de côté donnent 6 h 11 min 20 s, ramenés au plafond de 10 % : **4 h 39 min 16 s**. [[theorist_method_3:1]] n'a ajouté que 27 min 56 s.
- [[theorist_method_5]] : un clic avance l'étude de 10 % de son temps total, **4 h 39 min 16 s**. Avec [[theorist_method_7]] au rang 3 (19 %), on obtiendrait 8 h 50 min, ramenés au maximum de **6 h**.
- [[theorist_method_4]] au rang 3 (−18 %) : 409 600 → **335 872** métal, 102 400 → **83 968** cristal.

**[[b:network]]** : Centre 10 qui étudie, trois colonies avec des Centres 10, 9 et 8, Collaboration Stellaire 3.
- Sans talent, seul le Centre 10 de colonie entre : niveau effectif 10 + 10 = 20, **24 h 22 min 51 s**.
- [[theorist_network_1]] : les Centres 9 et 8 entrent aussi, niveau effectif 37, **13 h 28 min 25 s**.
- [[theorist_network_2]] au rang 3 : chacun des trois Centres de colonie compte 3 niveaux de plus, niveau effectif 46, **10 h 53 min 37 s**. Avec [[theorist_network_3:2]] en plus, 49 : **10 h 14 min 24 s**.
- [[theorist_network_7]] au rang 3 : l'étude achevée rend 9 % de ce qu'elle a coûté, soit **36 864** métal et **9 216** cristal sur un prix de 512 000.
- [[theorist_network_9]] (4 Centres ou plus) : 20 % de plus au départ. Une étude enchaînée part alors avec 10 % + 20 % = **13 h 57 min 48 s** déjà faits.

**[[theorist_method_9]]** : une seconde étude de 10 h prend **12 h 30 min** avec [[common_exploration_10]] et l'ultime (80 %), 20 h avec [[common_exploration_10]] seul (50 %), **25 h** avec l'ultime seul (40 %).""",
    'branch_notes': {
        'method': """- **[[theorist_method_1]]** ne vaut que pour une étude qui démarre d'elle-même derrière la précédente ; **[[theorist_method_2]]** que pour une étude lancée à la main sur une file vide. Ni l'un ni l'autre ne joue dans le second centre d'innovation.
- **[[theorist_method_3:1]]** compte le temps depuis la fin (achevée ou annulée) de la dernière étude, et ne sert qu'à une étude lancée à la main. Comme [[theorist_method_2]] occupe déjà 9 % des 10 %, il ajoute au plus 1 % de l'étude.
- **[[theorist_method_3:2]]** : seule une étude en cours peut être annulée avec sa progression. Elle la retrouve si vous relancez le même niveau de la même recherche, au-delà du plafond de 10 %. Un brouillon par recherche, le dernier.
- **[[theorist_method_5]]** : 6 h au plus, même avec [[theorist_method_7]], qui n'apporte donc rien au-delà de 31 h 35 min d'étude. La recharge se compte depuis l'usage, pour tout l'empire. Si l'avance achevait l'étude, le bouton est refusé et reste disponible ; [[theorist_method_6:2]] attend lui aussi une étude assez longue.
- **[[theorist_method_8]]** raccourcit la recharge de 20 % de la durée de chaque étude achevée, seulement pendant que l'Éclair recharge.
- **[[theorist_method_9]]** : la seconde étude doit porter sur une autre recherche, et rien ne doit attendre dans la file. Elle ne reçoit ni [[theorist_method_1]], ni [[theorist_method_2]], ni [[theorist_method_3:1]], ni [[theorist_network_6:2]].""",
        'network': """- **[[theorist_network_1]]** et **[[theorist_network_3:1]]** ne s'additionnent pas : la tolérance est de 5 niveaux avec les deux. Un Centre de niveau 0 n'entre jamais.
- **[[theorist_network_2]]** ne vaut que pour les Centres de vos autres planètes mis en commun, pas pour celui qui étudie ni pour le Centre allié.
- **[[theorist_network_6:1]]** : quand un de vos Centres d'innovation finit un niveau, le réseau est recalculé tel qu'il est alors et le temps restant baisse dans la même proportion.
- **[[theorist_network_6:2]]** verse 10 % de la durée de l'étude achevée à la prochaine de la même catégorie, mais sous le plafond de 10 % : avec [[theorist_method_1]], il n'ajoute rien à une étude enchaînée.
- **[[theorist_network_7]]** : 2 Centres en réseau, celui qui étudie compris. La part rendue est prise sur le prix payé, ressource par ressource, et versée à la planète qui étudie.
- **[[theorist_network_8]]** : le Centre allié s'ajoute en plus de la limite de Collaboration Stellaire, s'il entre dans la tolérance. Il compte pour [[theorist_network_7]] et [[theorist_network_9]].
- **[[theorist_network_9]]** : 4 Centres en réseau, celui qui étudie et l'allié compris. Vaut aussi dans le second centre d'innovation.""",
        'prototypes': """- **[[theorist_prototypes_1]]** : toute recherche sauf Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. Un nouveau prototype de la même recherche arrête le précédent.
- **[[theorist_prototypes_3:2]]** : les prérequis de recherche se lisent au niveau atteint avec un prototype, la [[theorist_prototypes_8]] ou la [[theorist_prototypes_9]]. Les prérequis de bâtiment ne changent pas.
- **[[theorist_prototypes_4]]** se déclenche sur une attaque de planète, que vous soyez attaquant ou défenseur, pour chaque technologie de combat où l'adversaire était plus haut que vous. La réduction vise votre niveau suivant, une fois.
- **[[theorist_prototypes_5]]** : jamais sur les technologies de combat.
- **[[theorist_prototypes_6:2]]** fonctionne aussi sur les technologies de combat, sans [[theorist_prototypes_3:1]]. Il arrête le prototype d'étude en cours sur cette recherche et ne rapporte pas de [[theorist_prototypes_7]].
- **[[theorist_prototypes_7]]** : la part est prise sur ce que l'étude a payé, et versée quand son prototype prend fin, même coupé par un nouveau, si la planète vous appartient encore.
- **[[theorist_prototypes_8]]** : une recherche déjà étudiée, +1 niveau en permanence. Une technologie de combat seulement avec [[theorist_prototypes_3:1]]. Le délai de changement part du dernier changement.
- **[[theorist_prototypes_9]]** : toutes vos recherches déjà étudiées, technologies de combat comprises.""",
    },
    'caps_note': "La tolérance du réseau garde la plus grande valeur détenue ([[theorist_network_1]] ou [[theorist_network_3:1]]) : 5 niveaux au plus.",
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chercheur pur | [[b:method]] 15 · [[b:network]] 10 | [[theorist_method_9]], [[theorist_method_1]], [[theorist_method_3:2]], [[theorist_method_4]] −18 %, [[theorist_method_5]] à 19 % (6 h au plus) toutes les 16 h ou automatique, [[theorist_method_8]] ; [[theorist_network_1]], Centres de colonie +3 niveaux, [[theorist_network_5]], [[theorist_network_6:1]] |
| Grand réseau | [[b:network]] 15 · [[b:method]] 10 | [[theorist_network_9]], [[theorist_network_8]], [[theorist_network_7]] 9 %, tolérance de 5 niveaux ou [[theorist_network_3:2]] ; [[theorist_method_1]], [[theorist_method_4]] −18 %, [[theorist_method_5]] à 10 %, [[theorist_method_6:1]] ou [[theorist_method_6:2]] |
| Savant de guerre | [[b:prototypes]] 15 · [[b:method]] 10 | [[theorist_prototypes_9]], prototypes de 48 h, [[theorist_prototypes_3:1]] ou [[theorist_prototypes_3:2]], [[theorist_prototypes_4]] −15 %, [[theorist_prototypes_8]] ; [[theorist_method_5]] pour rattraper les niveaux |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Le plafond de 10 % est partagé** : [[theorist_method_1]] le remplit à lui seul sur une étude enchaînée, et [[theorist_method_3:1]] n'ajoute au plus que 1 % à une étude lancée à la main. [[theorist_method_3:2]] est presque toujours le meilleur choix de la rangée 3.",
        "**[[theorist_method_5]] est plafonné à 6 h** : sur une longue étude, [[theorist_method_7]] ne change rien.",
        "**[[theorist_network_1]] ne crée pas de Centre** : le nombre reste fixé par Collaboration Stellaire, plus 1 avec [[theorist_network_5]] et 1 allié avec [[theorist_network_8]].",
        "**[[theorist_prototypes_5]] ne touche pas le combat** : les technologies de combat ne gagnent jamais deux niveaux de prototype.",
        "**Les bonus de niveau ne s'empilent pas** : une [[theorist_prototypes_9]] n'ajoute rien à une recherche qui a déjà un prototype ou la [[theorist_prototypes_8]].",
        "**[[theorist_method_9]]** va à 80 % seulement avec [[common_exploration_10]] ; sans lui, la seconde étude avance à 40 %.",
        "**[[theorist_prototypes_6:1]]** ne vaut qu'à partir du niveau 11 d'une recherche.",
    ],
    'related': [
        "[Classes](/fr/dynasty/classes)", "[Les talents](/fr/dynasty/talents)", "[Arbre commun](/fr/dynasty/common-tree)",
        "[Collaboration Stellaire](/fr/research/stellar-collaboration)", "[Liste des technologies](/fr/research/technologies)",
    ],
}

EN = {
    'brief': "\"Understand first\". The Theorist always has a study running and a level ahead. [[b:method]] keeps the research queue from ever stopping, [[b:network]] pools the Innovation Centers of its colonies, [[b:prototypes]] lets it enjoy a research level before anyone else.",
    'rules': [
        "Generic research speed and the second parallel study ([[common_exploration_10]]) are in the [common tree](/en/dynasty/common-tree). The Theorist's tree only holds mechanics of its own. Its two **accents** are the Innovation Centers' build speed ([[theorist_network_4]]) and the cost of research levels from the 11th on ([[theorist_prototypes_6:1]]).",
        "**Head starts.** A study may start with part of its time already elapsed. [[theorist_method_1]] or [[theorist_method_2]], plus [[theorist_method_3:1]] and [[theorist_network_6:2]], never exceed **10%** of the study all together. [[theorist_network_9]], [[theorist_method_3:2]] and the Archivist's momentum add on top. No head start ever completes a study.",
        "**Research network.** With no talent, [Stellar Collaboration](/en/research/stellar-collaboration) level N pools the N best Innovation Centers of your other planets, if they are at least as advanced as the studying one. The network shortens the study, never its cost.",
        "**Prototype.** A prototype makes a research count some levels higher for a while, wherever the game reads its level (fleet slots, number of planets, network Centers, combat...), never past its maximum level. It only applies to a research studied at least once. The three **combat technologies** (Weapon Systems, Shielding Technology, Armor Technology) only get a study prototype with [[theorist_prototypes_3:1]].",
        "Prototype, [[theorist_prototypes_8]] and [[theorist_prototypes_9]] **do not add up** on the same research: it takes the largest of the three bonuses.",
        "Research cost reductions ([[theorist_method_4]], [[theorist_prototypes_6:1]], [[theorist_prototypes_4]]) add up, then each resource is rounded up. They do not shorten the study, whose duration is computed on the normal price.",
    ],
    'example': """Reference study: **Weapon Systems 10** (409,600 metal, 102,400 crystal), universe research speed ×1, Innovation Center 10 on the studying planet: 512,000 / (1,000 × 11) h = **46 h 32 min 44 s**.

**[[b:method]]**
- [[theorist_method_1]]: the study, started after the previous one in the queue, begins with 10% of its time elapsed: **41 h 53 min 28 s** remain.
- Started by hand after 10 h of empty queue, with [[theorist_method_2]] at rank 3 and [[theorist_method_3:1]]: 9% (4 h 11 min 20 s) plus 2 h banked make 6 h 11 min 20 s, brought down to the 10% ceiling: **4 h 39 min 16 s**. [[theorist_method_3:1]] only added 27 min 56 s.
- [[theorist_method_5]]: one click moves the study ahead by 10% of its total time, **4 h 39 min 16 s**. With [[theorist_method_7]] at rank 3 (19%), that would be 8 h 50 min, brought down to the **6 h** maximum.
- [[theorist_method_4]] at rank 3 (−18%): 409,600 → **335,872** metal, 102,400 → **83,968** crystal.

**[[b:network]]**: studying Center 10, three colonies with Centers 10, 9 and 8, Stellar Collaboration 3.
- With no talent, only the colony's Center 10 joins: effective level 10 + 10 = 20, **24 h 22 min 51 s**.
- [[theorist_network_1]]: Centers 9 and 8 join too, effective level 37, **13 h 28 min 25 s**.
- [[theorist_network_2]] at rank 3: each of the three colony Centers counts 3 levels higher, effective level 46, **10 h 53 min 37 s**. With [[theorist_network_3:2]] on top, 49: **10 h 14 min 24 s**.
- [[theorist_network_7]] at rank 3: the completed study gives back 9% of what it cost, that is **36,864** metal and **9,216** crystal on a 512,000 price.
- [[theorist_network_9]] (4 Centers or more): 20% more at the start. A chained study then starts with 10% + 20% = **13 h 57 min 48 s** already done.

**[[theorist_method_9]]**: a second 10 h study takes **12 h 30 min** with [[common_exploration_10]] and the ultimate (80%), 20 h with [[common_exploration_10]] alone (50%), **25 h** with the ultimate alone (40%).""",
    'branch_notes': {
        'method': """- **[[theorist_method_1]]** only works for a study that starts on its own after the previous one; **[[theorist_method_2]]** only for a study started by hand on an empty queue. Neither works in the second Innovation Center.
- **[[theorist_method_3:1]]** counts the time since the last study ended (completed or cancelled), and only serves a study started by hand. Since [[theorist_method_2]] already takes 9% of the 10%, it adds at most 1% of the study.
- **[[theorist_method_3:2]]**: only a running study can be cancelled with its progress. It gets it back when you start the same level of the same research again, past the 10% ceiling. One draft per research, the latest.
- **[[theorist_method_5]]**: 6 h at most, even with [[theorist_method_7]], which therefore adds nothing past 31 h 35 min of study. The recharge counts from use, for the whole empire. If the advance would complete the study, the button is refused and stays available; [[theorist_method_6:2]] also waits for a long enough study.
- **[[theorist_method_8]]** shortens the recharge by 20% of each completed study's duration, only while the burst is recharging.
- **[[theorist_method_9]]**: the second study must be another research, and nothing may wait in the queue. It gets neither [[theorist_method_1]], [[theorist_method_2]], [[theorist_method_3:1]] nor [[theorist_network_6:2]].""",
        'network': """- **[[theorist_network_1]]** and **[[theorist_network_3:1]]** do not add up: the tolerance is 5 levels with both. A level 0 Center never joins.
- **[[theorist_network_2]]** only applies to the pooled Centers of your other planets, not to the studying one nor to the allied Center.
- **[[theorist_network_6:1]]**: when one of your Innovation Centers finishes a level, the network is recomputed as it stands and the remaining time drops in the same proportion.
- **[[theorist_network_6:2]]** passes 10% of the completed study's duration to the next one of the same category, but under the 10% ceiling: with [[theorist_method_1]], it adds nothing to a chained study.
- **[[theorist_network_7]]**: 2 Centers in the network, the studying one included. The share is taken on the price paid, resource by resource, and paid to the studying planet.
- **[[theorist_network_8]]**: the allied Center comes on top of Stellar Collaboration's limit, if it is within the tolerance. It counts for [[theorist_network_7]] and [[theorist_network_9]].
- **[[theorist_network_9]]**: 4 Centers in the network, the studying one and the ally included. Also works in the second Innovation Center.""",
        'prototypes': """- **[[theorist_prototypes_1]]**: every research except Weapon Systems, Shielding Technology and Armor Technology. A new prototype of the same research ends the previous one.
- **[[theorist_prototypes_3:2]]**: research requirements are read at the level reached with a prototype, [[theorist_prototypes_8]] or [[theorist_prototypes_9]]. Building requirements do not change.
- **[[theorist_prototypes_4]]** triggers on a planet attack, whether you attack or defend, for each combat technology where the opponent was higher than you. The discount targets your next level, once.
- **[[theorist_prototypes_5]]**: never on combat technologies.
- **[[theorist_prototypes_6:2]]** also works on combat technologies, without [[theorist_prototypes_3:1]]. It ends the running study prototype of that research and gives no [[theorist_prototypes_7]].
- **[[theorist_prototypes_7]]**: the share is taken on what the study paid, and paid when its prototype ends, even cut short by a new one, if the planet is still yours.
- **[[theorist_prototypes_8]]**: a research already studied, +1 level for good. A combat technology only with [[theorist_prototypes_3:1]]. The change delay counts from the last change.
- **[[theorist_prototypes_9]]**: all your researches already studied, combat technologies included.""",
    },
    'caps_note': "The network tolerance keeps the largest value held ([[theorist_network_1]] or [[theorist_network_3:1]]): 5 levels at most.",
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Pure researcher | [[b:method]] 15 · [[b:network]] 10 | [[theorist_method_9]], [[theorist_method_1]], [[theorist_method_3:2]], [[theorist_method_4]] −18%, [[theorist_method_5]] at 19% (6 h at most) every 16 h or automatic, [[theorist_method_8]]; [[theorist_network_1]], colony Centers +3 levels, [[theorist_network_5]], [[theorist_network_6:1]] |
| Great network | [[b:network]] 15 · [[b:method]] 10 | [[theorist_network_9]], [[theorist_network_8]], [[theorist_network_7]] 9%, 5-level tolerance or [[theorist_network_3:2]]; [[theorist_method_1]], [[theorist_method_4]] −18%, [[theorist_method_5]] at 10%, [[theorist_method_6:1]] or [[theorist_method_6:2]] |
| War scholar | [[b:prototypes]] 15 · [[b:method]] 10 | [[theorist_prototypes_9]], 48 h prototypes, [[theorist_prototypes_3:1]] or [[theorist_prototypes_3:2]], [[theorist_prototypes_4]] −15%, [[theorist_prototypes_8]]; [[theorist_method_5]] to catch up on levels |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**The 10% ceiling is shared**: [[theorist_method_1]] fills it alone on a chained study, and [[theorist_method_3:1]] adds at most 1% to a study started by hand. [[theorist_method_3:2]] is almost always the better row 3 choice.",
        "**[[theorist_method_5]] is capped at 6 h**: on a long study, [[theorist_method_7]] changes nothing.",
        "**[[theorist_network_1]] does not create a Center**: the number stays set by Stellar Collaboration, plus 1 with [[theorist_network_5]] and 1 ally with [[theorist_network_8]].",
        "**[[theorist_prototypes_5]] does not touch combat**: combat technologies never get two prototype levels.",
        "**Level bonuses do not stack**: a [[theorist_prototypes_9]] adds nothing to a research that already has a prototype or the [[theorist_prototypes_8]].",
        "**[[theorist_method_9]]** reaches 80% only with [[common_exploration_10]]; without it, the second study runs at 40%.",
        "**[[theorist_prototypes_6:1]]** only applies from a research's level 11.",
    ],
    'related': [
        "[Classes](/en/dynasty/classes)", "[Talents](/en/dynasty/talents)", "[Common tree](/en/dynasty/common-tree)",
        "[Stellar Collaboration](/en/research/stellar-collaboration)", "[Technology list](/en/research/technologies)",
    ],
}
