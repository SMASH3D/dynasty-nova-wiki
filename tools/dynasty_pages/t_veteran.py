"""Le Vétéran : textes vérifiés sur le code (notes du 15 octobre 2026, DONNEES §18)."""

FR = {
    'brief': "le Vétéran ne gagne pas les batailles, il fait que chaque attaque contre lui coûte cher à l'attaquant et presque rien à lui-même. Tout le combat tient dans Muraille ; Relève fait revenir les défenses tombées et rembourse les autres ; Silo répond par les missiles. Classe exclusive à L'Héritage.",
    'rules': [
        "Un Vétéran part de **75 %** de chances de réparation gratuite de chaque défense détruite au lieu de 70 %, grâce au trait Rien ne se perd de L'Héritage. [[veteran_relief_1]] et [[veteran_relief_4]] montent ce taux jusqu'à son plafond de **85 %**. La réparation reste un tirage par défense.",
        "La vitesse de construction des défenses générique vient de l'[arbre commun](/fr/dynasty/common-tree). Le Vétéran n'y ajoute que des **accents** étroits : la construction des défenses et des missiles ([[veteran_relief_3:2]], [[veteran_silo_6:2]]), **15 % au plus pour les deux ensemble**, et la protection contre le pillage ([[veteran_rampart_6:1]]), **15 points au plus**, [[common_prosperity_3:2]] de l'arbre commun compris.",
        "Les bonus de statistiques de Muraille s'appliquent **après** la recherche et se multiplient avec elle. Le bouclier et la coque de vos défenses comptent aussi contre les frappes de missiles : [[veteran_rampart_1]] et [[veteran_rampart_3:1]] les rendent plus dures à détruire. Les bonus de dégâts ([[veteran_rampart_4]], [[veteran_rampart_7]]) ne jouent que pour vos défenses, quand on vous attaque, et se multiplient entre eux.",
    ],
    'example': """**Une attaque détruit 100 Projecteurs balistiques** (2 000 métal pièce)
- Sans talent, chacun a 75 % de chances de revenir : **75** reviennent en moyenne, 25 sont perdus, soit 50 000 métal.
- Avec [[veteran_relief_1]] et [[veteran_relief_4]] au rang 3 (85 %) : **85** reviennent en moyenne, 15 sont perdus, soit 30 000 métal.
- Avec [[veteran_relief_2]], [[veteran_relief_5]] et [[veteran_relief_7]] (50 %) : **15 000 métal** vous sont rendus. La perte réelle tombe à 15 000 métal.
- Avec [[veteran_rampart_3:2]], les 100 reviennent.

**[[veteran_rampart_2]] au rang 3**
- Un Projecteur balistique a 80 d'armement. Systèmes Offensifs niveau 10 : 80 × 2 = 160. Avec +9 % : 160 × 1,09 = 174,4, arrondi à **174**.

**[[veteran_silo_1]] et [[veteran_silo_3:1]], Arsenal balistique niveau 10**
- 10 emplacements par niveau : 100 emplacements, soit 50 Ogives longue portée (2 emplacements chacune).
- Avec +35 % : 100 × 1,35 = 135 emplacements, soit **67 ogives**.
- Avec [[veteran_silo_2]] au rang 3 et Systèmes Offensifs niveau 10, une ogive inflige 12 000 × 2 × 1,09 = **26 160** dégâts.

**[[veteran_rampart_6:1]]**
- Le pillage subi passe de 50 % à **40 %**. Avec [[common_prosperity_3:2]] de l'arbre commun : **35 %**, le minimum pour un Vétéran. Sur 2 000 000 de métal en stock, l'attaquant emporte 700 000 au lieu de 1 000 000.

**[[veteran_rampart_6:2]]** (univers à 30 % de débris des vaisseaux, comme Redline)
- L'attaquant perd 100 Corvettes (20 000 métal et 7 000 cristal pièce) et vous gagnez. Débris : 600 000 métal et 210 000 cristal. **120 000 métal et 42 000 cristal** tombent dans vos stocks ; le reste reste dans le champ.""",
    'branch_notes': {
        'rampart': """- **[[veteran_rampart_3:1]]** ne touche que l'Accélérateur magnétique, la Batterie ionique et l'Éjecteur à plasma.
- **[[veteran_rampart_3:2]]** et **[[veteran_relief_8]]** réparent toujours, même contre [[admiral_campaign_8]], mais seulement après une bataille : rien contre les missiles.
- **[[veteran_rampart_4]]** joue contre chaque vaisseau qui a un tir rapide contre la défense qui tire.
- **[[veteran_rampart_5]]** vaut pour les attaques et les destructions de lune visant cette base. La commande de défenses ne gagne jamais plus de la moitié de son temps restant.
- **[[veteran_rampart_6:2]]** : seulement sur une défense gagnée ; les ressources dépassent la capacité de vos entrepôts et sont retirées du champ de débris.
- **[[veteran_rampart_7]]** joue au premier round de chaque bataille, contre toutes les cibles.
- **[[veteran_rampart_8]]** multiplie la chance de détruire la lune par 0,75 : une chance de 100 % tombe à 75 %.
- **[[veteran_rampart_9]]** : seules vos défenses tirent cette salve, pas vos vaisseaux. Si elle achève la flotte ennemie, la bataille devient une victoire de la défense.""",
        'relief': """- **[[veteran_relief_2]]**, **[[veteran_relief_5]]** et **[[veteran_relief_7]]** s'additionnent (50 % au plus). Ils rendent le prix payé (métal, cristal et hydrogène), sur la planète, même au-delà de ses entrepôts. Seulement pour les défenses perdues en bataille : une défense détruite par un missile n'est pas remboursée.
- **[[veteran_relief_3:1]]** est une chance par défense détruite, pas une part garantie.
- **[[veteran_relief_6:1]]** : les commandes de défenses lancées dans les 24 h construisent plus vite, pour autant d'unités de chaque type que vous en avez perdu. Une nouvelle perte ajoute ses unités et relance les 24 h.
- **[[veteran_relief_6:2]]** avance seulement la commande de défenses en cours, sans dépasser sa fin.
- **[[veteran_relief_9]]** : la fenêtre s'ouvre à chaque attaque subie hors fenêtre. Une attaque qui tombe dedans ne la prolonge pas. [[admiral_campaign_8]] d'un Amiral retire encore ses 15 points : 85 % de réparation au lieu de 100 %.""",
        'silo': """- **[[veteran_silo_1]]** et **[[veteran_silo_3:1]]** s'additionnent : +35 % d'emplacements, arrondi à l'unité inférieure. Un Intercepteur prend 1 emplacement, une Ogive longue portée 2.
- **[[veteran_silo_3:2]]** et **[[veteran_silo_7]]** s'additionnent (5 systèmes au plus) sur la portée de base, niveau de Moteur Magnétique × 5 − 1. Jamais hors de la galaxie, sauf contre une base visée par [[veteran_silo_5]].
- **[[veteran_silo_4]]** est une chance par Intercepteur qui abat une ogive.
- **[[veteran_silo_5]]** : la base d'où est partie la salve est à portée de toutes vos bases pendant 24 h.
- **[[veteran_silo_6:1]]** : la réserve de riposte se marque base par base. Une base frappée sans ogives marquées ne riposte pas. Une riposte ne déclenche jamais de riposte en retour.
- **[[veteran_silo_6:2]]** partage le plafond de 15 % de [[veteran_relief_3:2]] : avec les deux, vos missiles ne vont pas plus vite.
- **[[veteran_silo_9]]** se déclare au lancement, pour une salve d'au moins 20 ogives, une fois par 24 h glissantes pour tout votre empire. Aucun niveau n'est demandé.""",
    },
    'caps_note': "Deux plafonds se partagent : la vitesse de construction de [[veteran_relief_3:2]] et de [[veteran_silo_6:2]] tient dans un seul accent de 15 %, et la protection de [[veteran_rampart_6:1]] dans 15 points avec [[common_prosperity_3:2]]. La réparation gratuite bute sur 85 % : 75 % de départ et 10 points de talents l'atteignent tout juste.",
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Forteresse | Muraille 15 · Relève 10 | [[veteran_rampart_9]], [[veteran_rampart_5]], défenses +9 % de dégâts et +5 % de bouclier, [[veteran_rampart_4]], [[veteran_rampart_7]], [[veteran_rampart_8]] ; réparation à 85 %, 35 % rendus sur les pertes |
| Increvable | Relève 15 · Silo 10 | [[veteran_relief_9]], [[veteran_relief_8]], réparation à 85 %, 50 % rendus sur les pertes ; Arsenal +35 % avec [[veteran_silo_3:1]] (ou portée +2 avec [[veteran_silo_3:2]]), ogives +9 %, [[veteran_silo_4]], [[veteran_silo_5]] |
| Artilleur | Silo 15 · Muraille 10 | [[veteran_silo_9]], [[veteran_silo_8]], [[veteran_silo_6:1]] ou [[veteran_silo_6:2]], portée +3 à +5 systèmes ; [[veteran_rampart_1]], [[veteran_rampart_2]], [[veteran_rampart_4]], [[veteran_rampart_5]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**La réparation reste un tirage** : 85 % est une chance par défense, pas une part garantie du lot (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)).",
        "**Les frappes de missiles ne sont ni réparées ni remboursées** : seul [[veteran_relief_3:1]] donne à chaque défense détruite une chance de revenir. [[veteran_rampart_3:2]], [[veteran_relief_8]], [[veteran_relief_9]] et le remboursement de Relève ne jouent qu'après une bataille.",
        "**[[veteran_relief_3:2]] et [[veteran_silo_6:2]] ne se cumulent pas** sur les missiles : un seul accent de 15 %.",
        "**[[admiral_campaign_8]]** d'un Amiral retire 15 points à votre réparation contre lui : à 85 %, il vous reste 70 %.",
        "**[[veteran_silo_6:1]] ne vide jamais votre Arsenal balistique** : seules les ogives marquées « réserve de riposte » sur la base frappée partent. Sans réserve, rien ne part.",
        "**[[veteran_relief_6:2]] n'avance que la commande en cours** : sans défense en production, il ne fait rien.",
        "**Le pillage ne descend jamais sous 30 %**, mais un Vétéran ne va pas sous 35 % : sa protection est plafonnée à 15 points.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Classes](/fr/dynasty/classes)", "[Arbre commun](/fr/dynasty/common-tree)",
        "[Dynasties](/fr/dynasty/dynasties)", "[Liste des défenses](/fr/defense/defenses)", "[Missiles](/fr/defense/missiles)",
        "[Barrière et Dôme](/fr/defense/shield-domes)", "[Reconstruction des défenses](/fr/combat/defense-rebuild)",
        "[Pillage](/fr/combat/plunder)", "[Destruction de lune](/fr/combat/moon-destruction)",
    ],
}

EN = {
    'brief': "the Veteran does not win battles, it makes every attack on it cost the attacker dearly and itself next to nothing. All the combat lies in Rampart; Relief brings fallen defences back and refunds the others; Silo answers with missiles. Class exclusive to The Heritage.",
    'rules': [
        "A Veteran starts with a **75%** chance of free repair for each destroyed defence instead of 70%, thanks to The Heritage's Nothing Is Lost trait. [[veteran_relief_1]] and [[veteran_relief_4]] raise this rate up to its ceiling of **85%**. The repair stays a roll per defence.",
        "Generic defence build speed comes from the [common tree](/en/dynasty/common-tree). The Veteran only adds narrow **accents**: defence and missile build speed ([[veteran_relief_3:2]], [[veteran_silo_6:2]]), **15% at most for both together**, and protection against plunder ([[veteran_rampart_6:1]]), **15 points at most**, the common tree's [[common_prosperity_3:2]] included.",
        "Rampart's stat bonuses apply **after** research and multiply with it. Your defences' shield and hull also count against missile strikes: [[veteran_rampart_1]] and [[veteran_rampart_3:1]] make them harder to destroy. Damage bonuses ([[veteran_rampart_4]], [[veteran_rampart_7]]) only work for your defences, when you are attacked, and multiply with each other.",
    ],
    'example': """**An attack destroys 100 Ballistic Projectors** (2,000 metal each)
- Without talents, each has a 75% chance to come back: **75** come back on average, 25 are lost, that is 50,000 metal.
- With [[veteran_relief_1]] and [[veteran_relief_4]] at rank 3 (85%): **85** come back on average, 15 are lost, that is 30,000 metal.
- With [[veteran_relief_2]], [[veteran_relief_5]] and [[veteran_relief_7]] (50%): **15,000 metal** is given back. The real loss drops to 15,000 metal.
- With [[veteran_rampart_3:2]], all 100 come back.

**[[veteran_rampart_2]] at rank 3**
- A Ballistic Projector has 80 weapons. Weapon Systems level 10: 80 × 2 = 160. With +9%: 160 × 1.09 = 174.4, rounded down to **174**.

**[[veteran_silo_1]] and [[veteran_silo_3:1]], Ballistic Arsenal level 10**
- 10 slots per level: 100 slots, that is 50 Long-Range Warheads (2 slots each).
- With +35%: 100 × 1.35 = 135 slots, that is **67 warheads**.
- With [[veteran_silo_2]] at rank 3 and Weapon Systems level 10, a warhead deals 12,000 × 2 × 1.09 = **26,160** damage.

**[[veteran_rampart_6:1]]**
- Plunder suffered drops from 50% to **40%**. With the common tree's [[common_prosperity_3:2]]: **35%**, the lowest a Veteran can reach. With 2,000,000 metal in stock, the attacker takes 700,000 instead of 1,000,000.

**[[veteran_rampart_6:2]]** (universe with 30% ship debris, like Redline)
- The attacker loses 100 Corvettes (20,000 metal and 7,000 crystal each) and you win. Debris: 600,000 metal and 210,000 crystal. **120,000 metal and 42,000 crystal** drop into your stores; the rest stays in the field.""",
    'branch_notes': {
        'rampart': """- **[[veteran_rampart_3:1]]** only affects the Magnetic Accelerator, Ion Battery and Plasma Ejector.
- **[[veteran_rampart_3:2]]** and **[[veteran_relief_8]]** always repair, even against [[admiral_campaign_8]], but only after a battle: nothing against missiles.
- **[[veteran_rampart_4]]** works against every ship that has rapid fire against the firing defence.
- **[[veteran_rampart_5]]** applies to attacks and moon destructions aimed at this base. A defence order never gains more than half of its remaining time.
- **[[veteran_rampart_6:2]]**: only on a won defence; the resources go past your storage capacity and are taken out of the debris field.
- **[[veteran_rampart_7]]** works in the first round of every battle, against every target.
- **[[veteran_rampart_8]]** multiplies the chance of destroying the moon by 0.75: a 100% chance drops to 75%.
- **[[veteran_rampart_9]]**: only your defences fire this salvo, not your ships. If it finishes the enemy fleet, the battle becomes a defence victory.""",
        'relief': """- **[[veteran_relief_2]]**, **[[veteran_relief_5]]** and **[[veteran_relief_7]]** add up (50% at most). They give back the price paid (metal, crystal and hydrogen), on the planet, even past its storage. Only for defences lost in battle: a defence destroyed by a missile is not refunded.
- **[[veteran_relief_3:1]]** is a chance per destroyed defence, not a guaranteed share.
- **[[veteran_relief_6:1]]**: defence orders started within 24 h build faster, for as many units of each type as you lost. A new loss adds its units and restarts the 24 h.
- **[[veteran_relief_6:2]]** only moves the running defence order forward, never past its end.
- **[[veteran_relief_9]]**: the window opens on every attack suffered outside a window. An attack landing inside it does not extend it. An Admiral's [[admiral_campaign_8]] still takes its 15 points off: 85% repair instead of 100%.""",
        'silo': """- **[[veteran_silo_1]]** and **[[veteran_silo_3:1]]** add up: +35% slots, rounded down. An Interception Missile takes 1 slot, a Long-Range Warhead 2.
- **[[veteran_silo_3:2]]** and **[[veteran_silo_7]]** add up (5 systems at most) on the base range, Impulse Drive level × 5 − 1. Never outside the galaxy, except against a base targeted by [[veteran_silo_5]].
- **[[veteran_silo_4]]** is a chance per Interception Missile that downs a warhead.
- **[[veteran_silo_5]]**: the base the salvo came from is within range of all your bases for 24 h.
- **[[veteran_silo_6:1]]**: the riposte reserve is marked base by base. A struck base with no marked warheads does not answer. A riposte never triggers a riposte in return.
- **[[veteran_silo_6:2]]** shares [[veteran_relief_3:2]]'s 15% cap: with both, your missiles build no faster.
- **[[veteran_silo_9]]** is declared at launch, for a salvo of at least 20 warheads, once per rolling 24 h for your whole empire. No level is required.""",
    },
    'caps_note': "Two caps are shared: the build speed of [[veteran_relief_3:2]] and [[veteran_silo_6:2]] fits in a single 15% accent, and the protection of [[veteran_rampart_6:1]] in 15 points with [[common_prosperity_3:2]]. Free repair stops at 85%: a 75% start and 10 talent points just reach it.",
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Fortress | Rampart 15 · Relief 10 | [[veteran_rampart_9]], [[veteran_rampart_5]], defences +9% damage and +5% shield, [[veteran_rampart_4]], [[veteran_rampart_7]], [[veteran_rampart_8]]; repair at 85%, 35% back on losses |
| Unbreakable | Relief 15 · Silo 10 | [[veteran_relief_9]], [[veteran_relief_8]], repair at 85%, 50% back on losses; Arsenal +35% with [[veteran_silo_3:1]] (or range +2 with [[veteran_silo_3:2]]), warheads +9%, [[veteran_silo_4]], [[veteran_silo_5]] |
| Artillerist | Silo 15 · Rampart 10 | [[veteran_silo_9]], [[veteran_silo_8]], [[veteran_silo_6:1]] or [[veteran_silo_6:2]], range +3 to +5 systems; [[veteran_rampart_1]], [[veteran_rampart_2]], [[veteran_rampart_4]], [[veteran_rampart_5]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**Repair is still a roll**: 85% is a chance per defence, not a guaranteed share of the batch (see [Defense rebuild](/en/combat/defense-rebuild)).",
        "**Missile strikes are neither repaired nor refunded**: only [[veteran_relief_3:1]] gives each destroyed defence a chance to come back. [[veteran_rampart_3:2]], [[veteran_relief_8]], [[veteran_relief_9]] and Relief's refunds only work after a battle.",
        "**[[veteran_relief_3:2]] and [[veteran_silo_6:2]] do not stack** on missiles: a single 15% accent.",
        "**An Admiral's [[admiral_campaign_8]]** takes 15 points off your repair against them: at 85%, you are left with 70%.",
        "**[[veteran_silo_6:1]] never empties your Ballistic Arsenal**: only the warheads marked as \"riposte reserve\" on the struck base leave. Without a reserve, nothing leaves.",
        "**[[veteran_relief_6:2]] only moves the running order**: with no defence in production, it does nothing.",
        "**Plunder never goes below 30%**, but a Veteran does not go below 35%: its protection is capped at 15 points.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Classes](/en/dynasty/classes)", "[Common tree](/en/dynasty/common-tree)",
        "[Dynasties](/en/dynasty/dynasties)", "[Defenses list](/en/defense/defenses)", "[Missiles](/en/defense/missiles)",
        "[Defensive Barrier and Protective Dome](/en/defense/shield-domes)", "[Defense rebuild](/en/combat/defense-rebuild)",
        "[Plunder](/en/combat/plunder)", "[Moon destruction](/en/combat/moon-destruction)",
    ],
}
