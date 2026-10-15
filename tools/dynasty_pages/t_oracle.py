"""L'Oracle : textes vérifiés sur le code (notes du 15 octobre 2026, DONNEES §18)."""

FR = {
    'brief': "l'Oracle ne frappe pas plus fort, il sait avant. Chacune de ses branches vend une information, jamais une statistique : Veille regarde bouger les flottes depuis une lune, Présage prépare les raids, Préavis évite d'être là quand le coup tombe.",
    'rules': [
        "La protection générique contre le pillage et la vitesse de retour des flottes viennent de l'[arbre commun](/fr/dynasty/common-tree). L'Oracle n'y ajoute que deux **accents** étroits : [[oracle_omen_7]] (vitesse des attaques, dans l'accent de vitesse de 10 % de la classe) et [[oracle_warning_8]] (protection contre le pillage, 10 points au plus avec [[common_prosperity_3:2]]). Le pistage des espions appartient à l'[Ombre](/fr/dynasty/classes/shadow).",
        "Sans talent, seule une mission **Attaque** est annoncée, **60 s** avant l'impact, ou dès son départ si le vol dure moins. Le délai d'une flotte est fixé **à son départ**, d'après vos talents à ce moment ; une flotte accélérée en vol garde le même délai sur sa nouvelle heure d'impact. Dans le temps gagné avant les 60 s, l'alerte ne donne que la base visée et l'heure d'arrivée à la minute près ; l'heure exacte et l'origine arrivent à 60 s, sauf avec [[oracle_warning_3:2]]. L'alerte ne donne jamais la composition de la flotte.",
        "La [Phalange de capteur](/fr/espionage/sensor-phalanx) se construit sur une lune et ne vise jamais une lune. Un balayage coûte 5 000 hydrogène, sauf celui de [[oracle_watch_9]], et il est impossible en mode vacances. Il montre seulement les **mouvements** (flottes qui partent de la planète ou y arrivent), jamais les vaisseaux posés, ni les missions d'espionnage et de recyclage. Par défaut, personne n'est prévenu d'un balayage : seule l'Ombre, avec [[shadow_counterlight_5]], l'apprend.",
        "Les lectures de Présage partent de **vos** rapports d'espionnage. La part pillable y est calculée à votre taux de pillage (50 % sur Redline, plus vos talents contre une cible abandonnée), **sans** la protection du défenseur, que le rapport ne montre pas : c'est un maximum.",
    ],
    'example': """**Délai d'alerte selon les talents de [[b:warning]]**

| Talents pris | Délai avant l'impact |
|---|---|
| aucun | 1 min |
| [[oracle_warning_1]] | 2 min 30 |
| + [[oracle_warning_4]] au rang 3 | 3 min 30 |
| + [[oracle_warning_7]] au rang 3 | 4 min 30 |
| + [[oracle_warning_9]] (branche pleine) | 6 min |

Une attaque dont le vol dure 75 s est annoncée à son départ, 75 s avant l'impact : [[oracle_warning_2]], qui demande 90 s, ne joue pas.

**Phalange de capteur niveau 3 avec [[oracle_watch_1]] et [[oracle_watch_2]] au rang 3**
- Portée : la Phalange porte comme un niveau 4, soit 4² − 1 = **15 systèmes** de part et d'autre, au lieu de 8.
- Coût d'un balayage : 5 000 × (1 − 0,24) = **3 800 hydrogène**.
- Avec [[oracle_watch_8]], un joueur qui a 3 planètes à portée se balaie en entier pour 3 800 hydrogène au lieu de 11 400.
- Avec [[oracle_watch_6:2]] et une autre lune au système 70, une Phalange niveau 4 au système 40 (portée d'un niveau 5 : 24 systèmes) balaie les planètes des systèmes 16 à 64 **et** 46 à 94 de la même galaxie.

**[[oracle_omen_1]]** : le rapport lit 1 200 000 métal, 800 000 cristal et 300 000 hydrogène. À 50 %, la part pillable est 600 000 + 400 000 + 150 000 = **1 150 000**.
- Sans Pliage Spatial : 1 150 000 / 25 000 = **46 Cargos stellaires**, ou 1 150 000 / 5 000 = **230 Navettes de fret**.
- Pliage Spatial niveau 5 (+25 % de soute) : un Cargo stellaire porte 31 250, il en faut 36,8, arrondi à **37** ; une Navette de fret porte 6 250, il en faut **184**.
- Avec en plus [[common_logistics_3:1]] (+10 %) : 34 375 par Cargo stellaire, soit **34**.

**[[oracle_warning_6:1]]** : l'alerte arrondit la valeur de la flotte (coût de ses vaisseaux en métal, cristal et hydrogène) au multiple le plus proche de la moitié de sa puissance de dix.
- 200 Cuirassés (60 000 chacun) et 50 Cargos stellaires (12 000 chacun) : 12 600 000, affiché **15 000 000**.
- 1 200 Intercepteurs (4 000 chacun) : 4 800 000, affiché **5 000 000**.

**[[oracle_warning_8]]** : 2 000 000 de ressources en stock. Un raid gagnant emporte 50 % sans talent, soit 1 000 000 ; avec [[oracle_warning_8]], 45 %, soit **900 000** ; avec en plus [[common_prosperity_3:2]], 40 %, soit **800 000**.

**[[oracle_omen_7]]** : un trajet de 60 min sans autre bonus de vitesse dure 60 / 1,09, soit environ **55 min 3 s**, si l'attaque part au plus 30 min après votre dernier rapport sur la cible.""",
    'branch_notes': {
        'watch': """- **[[oracle_watch_1]]** n'agit que sur une Phalange déjà construite : (niveau + 1)² − 1 systèmes.
- **[[oracle_watch_3:1]]** : les autres membres de votre alliance reçoivent une notification avec ce que le balayage a vu. Rien sans alliance.
- **[[oracle_watch_3:2]]** vaut pour tous vos balayages, ceux de [[oracle_watch_7]], [[oracle_watch_8]] et [[oracle_watch_9]] compris.
- **[[oracle_watch_4]]** suit les flottes en direct, retour compris, jusqu'à 3 h après la fin du balayage (après sa fermeture pour un balayage resté ouvert).
- **[[oracle_watch_5]]** est une information d'alerte : il marche sans lune. L'heure donnée suppose que la flotte rentre tout droit ; un retour plus rapide peut la ramener plus tôt.
- **[[oracle_watch_6:1]]** ne sert que contre un joueur qui a [[shadow_counterlight_5]] : sans lui, aucun balayage n'est signalé.
- **[[oracle_watch_6:2]]** : la portée de votre Phalange se mesure aussi depuis chacune de vos autres lunes, même sans Phalange.
- **[[oracle_watch_7]]** ne s'ouvre jamais sur votre propre planète.
- **[[oracle_watch_8]]** ajoute les autres **planètes** du joueur à portée de la lune à Phalange (ou des relais) ; sans effet sur vos propres planètes.
- **[[oracle_watch_9]]** : c'est votre lune la plus proche dont la Phalange atteint la planète de départ qui balaie, relais compris. Il faut une Phalange bâtie sur cette lune. Le relevé montre les mouvements de cette planète au moment où vous lisez l'alerte.""",
        'omen': """- **[[oracle_omen_1]]** compte les soutes de vos Navettes de fret et Cargos stellaires avec votre Pliage Spatial et vos talents de soute, arrondi au-dessus.
- **[[oracle_omen_2]]** : une cible est une planète ou une lune, avec un seuil de part pillable totale. Le stock est prolongé au rythme mesuré entre vos deux derniers rapports, sans plafond de hangars ; une ressource qui a baissé compte pour 0. Une notification par rapport. Le nœud donne aussi cette projection sur chaque rapport. Après une réinitialisation qui laisse moins de places, seules les premières cibles comptent.
- **[[oracle_omen_3:1]]** s'appuie sur ce que vos vagues précédentes sur ce corps ont prouvé.
- **[[oracle_omen_3:2]]** s'affiche sur la lecture du rapport ; le simulateur, lui, refuse toujours un rapport qui n'a pas lu la flotte. « Dangereuse » : le propriétaire a plus de points militaires publics que vous. « Probablement vide » : le stock lu est sous 10 000 et vous avez au moins 1,2 fois ses points militaires. « Inconnue » sinon.
- **[[oracle_omen_4]]** : les recherches ne s'affichent au rang 3 que si vos Éclaireurs pouvaient les lire chez ce défenseur. Jamais la flotte ni les défenses.
- **[[oracle_omen_5]]** et **[[oracle_omen_6:2]]** donnent des moyennes sur les combats simulés.
- **[[oracle_omen_6:1]]** répartit les Cargos stellaires et Navettes de fret d'**une** base choisie ; une ferme dont le rapport n'a pas lu le stock est écartée. Vous lancez les envois.
- **[[oracle_omen_7]]** : mission Attaque seulement, pas une destruction de lune ; c'est votre rapport le plus récent sur ce corps précis (planète ou lune) qui compte. La vitesse divise la durée.
- **[[oracle_omen_8]]** : trois verdicts, tenir, tomber ou inconnu. Sans [[oracle_warning_6:1]], « tomber » si l'attaquant a plus de points militaires publics que vous, « inconnu » s'il manque un classement. Avec [[oracle_warning_6:1]], 20 combats simulés contre la vraie flotte et vos défenses du moment, [[oracle_warning_2]] comprise : « tenir » si l'attaquant en gagne moins de la moitié. Seul le verdict est montré.
- **[[oracle_omen_9]]** cherche la plus petite part, par vingtièmes, de toute la flotte de combat de la base choisie (chaque type gardé), puis ajoute les Cargos stellaires et Navettes de fret de cette base, dans la limite de ce qui y stationne. Sans recherches lues dans le rapport, le défenseur est supposé à vos niveaux. Si toute la flotte de combat ne suffit pas, aucun plan n'est proposé.""",
        'warning': """- **[[oracle_warning_2]]** : +2 % de bouclier et +2 % de dégâts par rang, pour les vaisseaux posés et les défenses de la base attaquée, si l'alerte de **cette** attaque est réellement tombée 90 s avant l'impact. L'attaquant ne la voit pas dans son simulateur.
- **[[oracle_warning_3:1]]** : petite sous 100 000 de valeur (coût des vaisseaux en ressources), moyenne sous 1 000 000, grande sous 10 000 000, écrasante au-delà.
- **[[oracle_warning_5]]** : sans ce nœud, une destruction de lune n'est pas annoncée du tout.
- **[[oracle_warning_6:1]]** : l'écart entre la valeur affichée et la vraie ne dépasse pas 20 % de la vraie. Pris avec [[oracle_warning_3:1]], c'est l'estimation qui s'affiche.
- **[[oracle_warning_6:2]]** : toute flotte, quelle que soit sa mission, qui quitte le corps visé (planète ou lune) pendant qu'une attaque **déjà annoncée** vole vers lui. Sa vitesse et sa réduction s'appliquent après tous les autres bonus, hors plafonds.
- **[[oracle_warning_8]]** vaut sur toutes vos bases ; le taux de pillage ne descend jamais sous 30 %.""",
    },
    'caps_note': "La ligne du pillage se complète avec [[common_prosperity_3:2]] de l'arbre commun (5 points) : 10 points en tout, le taux subi passe de 50 à 40 %. Le délai d'alerte s'ajoute aux 60 s que le jeu donne à tous : 360 s, soit 6 min, au plus.",
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Sentinelle | Préavis 15 · Veille 10 | alerte 6 min avant l'impact, [[oracle_warning_8]], garde +6 % de bouclier et de dégâts, [[oracle_warning_3:1]] ou [[oracle_warning_3:2]], [[oracle_warning_5]], [[oracle_warning_6:1]] ou [[oracle_warning_6:2]] ; Phalange +1 niveau à 3 800 hydrogène, [[oracle_watch_3:1]] ou [[oracle_watch_3:2]], mémoire de 3 h, [[oracle_watch_5]], [[oracle_watch_6:1]] ou [[oracle_watch_6:2]] |
| Augure | Présage 15 · Préavis 10 | [[oracle_omen_9]], [[oracle_omen_8]], [[oracle_omen_7]], [[oracle_omen_5]], carnet de 15 cibles, [[oracle_omen_4]] ; alerte 3 min 30 avant l'impact, garde +6 %, [[oracle_warning_5]], [[oracle_warning_6:1]] (qui fait simuler [[oracle_omen_8]]) ou [[oracle_warning_6:2]] |
| Guetteur | Veille 15 · Présage 10 | [[oracle_watch_9]], [[oracle_watch_8]], balayages ouverts 30 min, mémoire de 3 h ; [[oracle_omen_1]], carnet de 15 cibles, [[oracle_omen_4]], [[oracle_omen_5]], [[oracle_omen_6:1]] ou [[oracle_omen_6:2]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**[[oracle_warning_2]] demande 90 secondes d'alerte** : la minute que le jeu donne à tous ne suffit pas, il faut au moins [[oracle_warning_1]]. Une attaque au vol plus court que 90 s ne la déclenche jamais.",
        "**Les talents d'alerte comptent au départ de la flotte ennemie** : prendre [[oracle_warning_1]] pendant qu'une attaque vole déjà ne l'annonce pas plus tôt.",
        "**L'alerte avancée est floue** : base visée et heure à la minute près, sans origine, jusqu'aux 60 dernières secondes. Pour partir à la dernière seconde, [[oracle_warning_3:2]] compte plus que le délai.",
        "**Pas de lune, pas de Phalange** : la Phalange se construit sur une lune et ne vise jamais une lune ; [[oracle_watch_3:2]] montre seulement les flottes qui partent de la lune ou y arrivent. [[oracle_watch_5]], lui, n'a pas besoin de lune.",
        "**[[oracle_watch_6:1]] ne sert que contre l'Ombre** : par défaut, personne n'est prévenu d'un balayage.",
        "**[[oracle_omen_1]], [[oracle_omen_5]], [[oracle_omen_2]] et [[oracle_omen_9]] sont des maximums** : ils ignorent la protection du défenseur contre le pillage et la taille de ses hangars.",
        "**[[oracle_omen_7]]** ne vaut que pour une attaque lancée au plus 30 minutes après votre rapport d'espionnage sur le même corps. Elle compte dans l'accent de vitesse de la classe (10 % au plus).",
        "**[[oracle_warning_3:1]] et [[oracle_warning_6:1]] mesurent un coût, pas une force** : 1 000 Navettes de fret (4 000 000) sortent « grande » comme une flotte de combat du même prix.",
        "**[[oracle_warning_8]] et [[common_prosperity_3:2]] se cumulent** : 10 points de protection au total, le pillage subi passe de 50 à 40 %. C'est le plafond de l'Oracle.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Classes](/fr/dynasty/classes)", "[Arbre commun](/fr/dynasty/common-tree)",
        "[Dynasties](/fr/dynasty/dynasties)", "[Phalange de capteur](/fr/espionage/sensor-phalanx)",
        "[Lire un rapport d'espionnage](/fr/espionage/spy-report)", "[Pillage](/fr/combat/plunder)",
        "[Simulateur](/fr/combat/simulator)", "[L'Ombre](/fr/dynasty/classes/shadow)",
    ],
}

EN = {
    'brief': "the Oracle does not hit harder, it knows first. Each of its branches sells information, never a statistic: Watch sees fleets move from a moon, Omen prepares raids, Forewarning keeps you away when the blow lands.",
    'rules': [
        "Generic plunder protection and fleet return speed come from the [common tree](/en/dynasty/common-tree). The Oracle only adds two narrow **accents**: [[oracle_omen_7]] (attack speed, within the class's 10% speed accent) and [[oracle_warning_8]] (plunder protection, 10 points at most with [[common_prosperity_3:2]]). Tracking spies belongs to the [Shadow](/en/dynasty/classes/shadow).",
        "With no talent, only an **Attack** mission is announced, **60 s** before impact, or as soon as it leaves if the flight is shorter. A fleet's lead is set **when it leaves**, from your talents at that moment; a fleet sped up in flight keeps the same lead on its new impact time. In the time gained before the 60 s, the alert only gives the targeted base and the arrival time to the minute; the exact time and the origin come at 60 s, except with [[oracle_warning_3:2]]. The alert never gives the fleet's composition.",
        "The [Sensor phalanx](/en/espionage/sensor-phalanx) is built on a moon and never targets a moon. A sweep costs 5,000 hydrogen, except the one from [[oracle_watch_9]], and is impossible in vacation mode. It only shows **movements** (fleets leaving or reaching the planet), never parked ships, nor espionage and recycling missions. By default, nobody is told of a sweep: only the Shadow, with [[shadow_counterlight_5]], learns of it.",
        "Omen's readings start from **your** espionage reports. The plunderable share is computed at your plunder rate (50% on Redline, plus your talents against an abandoned target), **without** the defender's protection, which the report does not show: it is a maximum.",
    ],
    'example': """**Alert lead by [[b:warning]] talents**

| Talents taken | Lead before impact |
|---|---|
| none | 1 min |
| [[oracle_warning_1]] | 2 min 30 |
| + [[oracle_warning_4]] at rank 3 | 3 min 30 |
| + [[oracle_warning_7]] at rank 3 | 4 min 30 |
| + [[oracle_warning_9]] (full branch) | 6 min |

An attack whose flight lasts 75 s is announced when it leaves, 75 s before impact: [[oracle_warning_2]], which needs 90 s, does not work.

**Sensor phalanx level 3 with [[oracle_watch_1]] and [[oracle_watch_2]] at rank 3**
- Reach: the phalanx reaches like a level 4, that is 4² − 1 = **15 systems** on each side, instead of 8.
- Cost of a sweep: 5,000 × (1 − 0.24) = **3,800 hydrogen**.
- With [[oracle_watch_8]], a player with 3 planets in reach is swept entirely for 3,800 hydrogen instead of 11,400.
- With [[oracle_watch_6:2]] and another moon in system 70, a level 4 phalanx in system 40 (reach of a level 5: 24 systems) sweeps the planets of systems 16 to 64 **and** 46 to 94 of the same galaxy.

**[[oracle_omen_1]]**: the report reads 1,200,000 metal, 800,000 crystal and 300,000 hydrogen. At 50%, the plunderable share is 600,000 + 400,000 + 150,000 = **1,150,000**.
- Without Hyperspace Technology: 1,150,000 / 25,000 = **46 Stellar Freighters**, or 1,150,000 / 5,000 = **230 Cargo Shuttles**.
- Hyperspace Technology level 5 (+25% hold): a Stellar Freighter carries 31,250, it takes 36.8, rounded up to **37**; a Cargo Shuttle carries 6,250, it takes **184**.
- Adding [[common_logistics_3:1]] (+10%): 34,375 per Stellar Freighter, that is **34**.

**[[oracle_warning_6:1]]**: the alert rounds the fleet's value (its ships' cost in metal, crystal and hydrogen) to the nearest multiple of half its power of ten.
- 200 Battleships (60,000 each) and 50 Stellar Freighters (12,000 each): 12,600,000, shown as **15,000,000**.
- 1,200 Interceptors (4,000 each): 4,800,000, shown as **5,000,000**.

**[[oracle_warning_8]]**: 2,000,000 resources in stock. A winning raid takes 50% with no talent, that is 1,000,000; with [[oracle_warning_8]], 45%, that is **900,000**; adding [[common_prosperity_3:2]], 40%, that is **800,000**.

**[[oracle_omen_7]]**: a 60 min trip with no other speed bonus lasts 60 / 1.09, about **55 min 3 s**, if the attack leaves at most 30 min after your last report on the target.""",
    'branch_notes': {
        'watch': """- **[[oracle_watch_1]]** only works on a phalanx already built: (level + 1)² − 1 systems.
- **[[oracle_watch_3:1]]**: the other members of your alliance get a notification with what the sweep saw. Nothing without an alliance.
- **[[oracle_watch_3:2]]** applies to all your sweeps, those of [[oracle_watch_7]], [[oracle_watch_8]] and [[oracle_watch_9]] included.
- **[[oracle_watch_4]]** follows the fleets live, return trip included, up to 3 h after the sweep ends (after it closes, for a sweep left open).
- **[[oracle_watch_5]]** is alert information: it works without a moon. The time given assumes the fleet flies straight home; a faster return may bring it back sooner.
- **[[oracle_watch_6:1]]** only matters against a player holding [[shadow_counterlight_5]]: without it, no sweep is reported.
- **[[oracle_watch_6:2]]**: your phalanx's reach is also measured from each of your other moons, even without a phalanx.
- **[[oracle_watch_7]]** never opens on your own planet.
- **[[oracle_watch_8]]** adds the player's other **planets** in reach of the phalanx moon (or the relays); no effect on your own planets.
- **[[oracle_watch_9]]**: the sweep comes from your nearest moon whose phalanx reaches the departure planet, relays included. That moon needs a phalanx built. The reading shows that planet's movements at the moment you read the alert.""",
        'omen': """- **[[oracle_omen_1]]** counts the holds of your Cargo Shuttles and Stellar Freighters with your Hyperspace Technology and your hold talents, rounded up.
- **[[oracle_omen_2]]**: a target is a planet or a moon, with a threshold on the total plunderable share. The stock is carried forward at the pace measured between your last two reports, with no storage cap; a resource that went down counts as 0. One notification per report. The node also gives this projection on every report. After a reset that leaves fewer slots, only the first targets count.
- **[[oracle_omen_3:1]]** relies on what your previous waves on that body proved.
- **[[oracle_omen_3:2]]** shows on the report's reading; the simulator still refuses a report that did not read the fleet. "Dangerous": the owner has more public military points than you. "Probably empty": the stock read is under 10,000 and you have at least 1.2 times their military points. "Unknown" otherwise.
- **[[oracle_omen_4]]**: research only shows at rank 3 if your Scouts could read it on that defender. Never the fleet or the defences.
- **[[oracle_omen_5]]** and **[[oracle_omen_6:2]]** give averages over the simulated fights.
- **[[oracle_omen_6:1]]** shares the Stellar Freighters and Cargo Shuttles of **one** chosen base; a farm whose report did not read the stock is left out. You launch the sends.
- **[[oracle_omen_7]]**: Attack mission only, not a moon destruction; your most recent report on that very body (planet or moon) is the one that counts. Speed divides the duration.
- **[[oracle_omen_8]]**: three verdicts, hold, fall or unknown. Without [[oracle_warning_6:1]], "fall" if the attacker has more public military points than you, "unknown" if a ranking is missing. With [[oracle_warning_6:1]], 20 simulated fights against the real fleet and your current defence, [[oracle_warning_2]] included: "hold" if the attacker wins fewer than half. Only the verdict is shown.
- **[[oracle_omen_9]]** looks for the smallest share, in twentieths, of the chosen base's whole combat fleet (every type kept), then adds that base's Stellar Freighters and Cargo Shuttles, within what is stationed there. Without research read in the report, the defender is assumed at your levels. If the whole combat fleet is not enough, no plan is offered.""",
        'warning': """- **[[oracle_warning_2]]**: +2% shield and +2% damage per rank, for the parked ships and defences of the attacked base, if the alert for **that** attack really came 90 s before impact. The attacker does not see it in their simulator.
- **[[oracle_warning_3:1]]**: small under 100,000 of value (ships' cost in resources), medium under 1,000,000, large under 10,000,000, overwhelming beyond.
- **[[oracle_warning_5]]**: without this node, a moon destruction is not announced at all.
- **[[oracle_warning_6:1]]**: the gap between the value shown and the real one never exceeds 20% of the real one. Taken with [[oracle_warning_3:1]], the estimate is what shows.
- **[[oracle_warning_6:2]]**: any fleet, whatever its mission, leaving the targeted body (planet or moon) while an attack **already announced** is flying at it. Its speed and reduction apply after every other bonus, outside the caps.
- **[[oracle_warning_8]]** applies to all your bases; the plunder rate never drops below 30%.""",
    },
    'caps_note': "The plunder row is completed by the common tree's [[common_prosperity_3:2]] (5 points): 10 points in all, the rate you suffer drops from 50 to 40%. The alert lead adds to the 60 s the game gives everyone: 360 s, that is 6 min, at most.",
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Sentinel | Forewarning 15 · Watch 10 | alert 6 min before impact, [[oracle_warning_8]], guard +6% shield and damage, [[oracle_warning_3:1]] or [[oracle_warning_3:2]], [[oracle_warning_5]], [[oracle_warning_6:1]] or [[oracle_warning_6:2]]; phalanx +1 level at 3,800 hydrogen, [[oracle_watch_3:1]] or [[oracle_watch_3:2]], 3 h memory, [[oracle_watch_5]], [[oracle_watch_6:1]] or [[oracle_watch_6:2]] |
| Augur | Omen 15 · Forewarning 10 | [[oracle_omen_9]], [[oracle_omen_8]], [[oracle_omen_7]], [[oracle_omen_5]], 15-target ledger, [[oracle_omen_4]]; alert 3 min 30 before impact, guard +6%, [[oracle_warning_5]], [[oracle_warning_6:1]] (which makes [[oracle_omen_8]] simulate) or [[oracle_warning_6:2]] |
| Lookout | Watch 15 · Omen 10 | [[oracle_watch_9]], [[oracle_watch_8]], sweeps open 30 min, 3 h memory; [[oracle_omen_1]], 15-target ledger, [[oracle_omen_4]], [[oracle_omen_5]], [[oracle_omen_6:1]] or [[oracle_omen_6:2]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**[[oracle_warning_2]] needs 90 seconds of alert**: the minute the game gives everyone is not enough, you need at least [[oracle_warning_1]]. An attack whose flight is shorter than 90 s never triggers it.",
        "**Alert talents count when the enemy fleet leaves**: taking [[oracle_warning_1]] while an attack is already flying does not announce it earlier.",
        "**The early alert is vague**: targeted base and time to the minute, no origin, until the last 60 seconds. To leave at the last second, [[oracle_warning_3:2]] matters more than the lead.",
        "**No moon, no phalanx**: the phalanx is built on a moon and never targets a moon; [[oracle_watch_3:2]] only shows the fleets leaving or reaching the moon. [[oracle_watch_5]], however, needs no moon.",
        "**[[oracle_watch_6:1]] only matters against the Shadow**: by default, nobody is told of a sweep.",
        "**[[oracle_omen_1]], [[oracle_omen_5]], [[oracle_omen_2]] and [[oracle_omen_9]] are maximums**: they ignore the defender's plunder protection and the size of their storage.",
        "**[[oracle_omen_7]]** only applies to an attack launched at most 30 minutes after your espionage report on the same body. It counts in the class's speed accent (10% at most).",
        "**[[oracle_warning_3:1]] and [[oracle_warning_6:1]] measure a cost, not a strength**: 1,000 Cargo Shuttles (4,000,000) come out \"large\" like a combat fleet of the same price.",
        "**[[oracle_warning_8]] and [[common_prosperity_3:2]] stack**: 10 points of protection in all, the plunder you suffer drops from 50 to 40%. That is the Oracle's cap.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Classes](/en/dynasty/classes)", "[Common tree](/en/dynasty/common-tree)",
        "[Dynasties](/en/dynasty/dynasties)", "[Sensor phalanx](/en/espionage/sensor-phalanx)",
        "[Reading a spy report](/en/espionage/spy-report)", "[Plunder](/en/combat/plunder)",
        "[Battle simulator](/en/combat/simulator)", "[The Shadow](/en/dynasty/classes/shadow)",
    ],
}
