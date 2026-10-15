"""Le Symbiote : textes vérifiés sur le code (notes du 15 octobre 2026, DONNEES §18)."""

FR = {
    'brief': "le Symbiote joue ce que les autres subissent : la température de la planète, sa place dans le système, sa taille, sa lune et ses voisins. Thermie fait de la température un atout, Croissance tire le meilleur de la position et des cases, Hôte fait produire les planètes en friche et celles qui ont des voisins.",
    'rules': [
        "La production générique des mines, les colonies jeunes et les cases génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). La fusion, la production propre des Collecteurs solaires et le manque d'énergie relèvent de l'[Énergéticien](/fr/dynasty/classes/energist). Le Symbiote n'a qu'un **accent** : 2 cases de plus par planète ([[symbiote_growth_6:1]]), pour 4 au plus avec [[common_exploration_5]] (arbre commun).",
        "Les bonus de mines de l'Hôte sont des mécaniques à part : ils s'ajoutent entre eux et aux autres bonus, tous calculés sur la **production brute** des trois mines (Excavateur minéral, Extracteur cristallin, Condensateur d'hydrogène), et ils restent **hors** du plafond de production des talents. Jamais sur une lune.",
        "Les talents de température élargissent seulement la **part de bonus** d'un facteur, jamais son signe. Condensateur d'hydrogène : facteur 1,44 − 0,004 × température maximale, amplifié seulement au-dessus de 1. Capteurs photovoltaïques : facteur 1 + température du jour / 100, amplifié seulement au-dessus de 0 °C. Collecteur solaire : température maximale / 4 + 20 d'énergie, seule la part température est amplifiée, arrondi à l'unité inférieure. Le détail des températures est sur [Planètes : taille, température, type](/fr/universe/planets).",
        "Le bonus de position **dépend du nombre de positions du système**, un paramètre d'univers (15 sur Redline). Dans un système à 15 positions, l'Extracteur cristallin gagne +40, +30 et +20 % en positions 1 à 3, l'Excavateur minéral +17, +23, +35, +23 et +17 % en positions 6 à 10. Ailleurs, la position est ramenée sur une échelle de 15 et le bonus est calculé entre les deux positions voisines : dans un système à 9 positions, la position 2 donne +22,5 % de cristal. Le Condensateur d'hydrogène n'a jamais de bonus de position.",
        "Une planète est **en friche** tant que ses cases bâties sont strictement moins de 50 % de son total de cases (Modulateur planétaire et cases bonus compris). Cette notion n'existe que pour un Symbiote qui a [[symbiote_host_1]] ou [[symbiote_host_2]], et ne s'applique jamais à une lune. Elle n'a rien à voir avec la colonie jeune de l'arbre commun.",
    ],
    'example': """**Condensateur d'hydrogène en position 15 d'un système à 15 positions** (−85 à −45 °C)
- Sans talent : 1,44 − 0,004 × (−45) = **1,62**. La part de bonus est 0,62.
- Avec [[symbiote_thermal_1]] (+10 %) : 1 + 0,62 × 1,10 = **1,68**.
- Avec en plus [[symbiote_thermal_7]] au rang 3 (+40 % en tout) : 1 + 0,62 × 1,40 = **1,87**.
- Avec en plus [[symbiote_thermal_3:1]] (+65 % en tout) : 1 + 0,62 × 1,65 = **2,02**.
- Branche pleine, avec [[symbiote_thermal_9]] et [[symbiote_thermal_2]] réglé vers le froid : le Condensateur lit −85 − 30 = −115 °C, facteur 1,44 + 0,46 = 1,90, puis 1 + 0,90 × 1,65 = **2,485**.
- Au niveau 20, vitesse d'économie ×1 (Redline) : 10 × 20 × 1,1²⁰ = 1 345,5 hydrogène par heure avant facteur, soit **2 179** sans talent et **3 343** avec la branche pleine (+53 %).

**[[symbiote_thermal_9]] sur une colonie en position 8 d'un système à 15 positions** (20 à 60 °C)
- Sans talent, le Condensateur lit la température maximale : 1,44 − 0,004 × 60 = **1,20**.
- Avec l'ultime, il lit la minimale : 1,44 − 0,004 × 20 = **1,36**, soit 13 % d'hydrogène en plus.

**Bonus de position de l'Excavateur minéral en position 8 d'un système à 15 positions** (+35 % sans talent)
- [[symbiote_growth_1]] : 35 × 1,15 = **+40,25 %**.
- [[symbiote_growth_1]] et [[symbiote_growth_5]] : 35 × 1,45 = **+50,75 %**.
- Avec en plus [[symbiote_growth_3:1]] : 35 × 1,65 = **+57,75 %**.
- Une planète mère au même endroit, avec [[symbiote_growth_1]], [[symbiote_growth_5]] et [[symbiote_growth_2]] au rang 3 : 35 × 1,45 × ½ = **+25,375 %**.

**Collecteur solaire en position 8 d'un système à 15 positions** (température maximale 60 °C)
- Sans talent : 60 / 4 + 20 = **35** énergie par Collecteur.
- [[symbiote_thermal_4]] au rang 3 : 15 × 1,45 + 20 = 41,75, arrondi à **41**.
- [[symbiote_thermal_8]] : la planète est lue à 100 °C, 100 / 4 + 20 = **45**.
- [[symbiote_thermal_4]] au rang 3, [[symbiote_thermal_3:2]], [[symbiote_thermal_8]] et [[symbiote_thermal_2]] réglé vers le chaud : (60 + 30 + 40) / 4 = 32,5, × 1,70 (45 + 25 % d'amplitude) = 55,25, + 20 = **75**.

**Hôte sur une colonie de 210 cases dont 100 bâties, Excavateur minéral niveau 20** (4 036 métal par heure bruts, vitesse ×1)
- En friche (100 / 210 = 47,6 %) avec [[symbiote_host_2]] au rang 3 : +15 %. [[symbiote_host_3:2]] (plus de 200 cases) : +8 %. Trois planètes d'autres joueurs dans le système avec [[symbiote_host_6:1]] : 3 × 2 = +6 %. Une autre de vos planètes dans le système avec [[symbiote_host_7]] au rang 3 : +9 %.
- Total **+38 %** : 4 036 × 0,38 = **1 533** métal par heure en plus.
- Dans les 6 h qui suivent un raid qui a emporté des ressources, [[symbiote_host_8]] ajoute 20 % : +58 %, soit **2 340**.""",
    'branch_notes': {
        'thermal': """- **[[symbiote_thermal_1]]** et **[[symbiote_thermal_7]]** s'additionnent (40 % au plus) et jouent sur le Condensateur d'hydrogène et les Capteurs photovoltaïques, pas sur les Collecteurs solaires.
- **[[symbiote_thermal_2]]** : jamais sur une lune. Le premier réglage est immédiat ; ensuite chaque planète attend 7 jours entre deux réglages, revenir à « aucun décalage » compris. Le décalage vaut pour le Condensateur, les Capteurs et les Collecteurs à la fois, dans le même sens : vers le froid, plus d'hydrogène et moins d'énergie solaire.
- **[[symbiote_thermal_3:1]]** ne vise que le Condensateur (65 % d'amplitude au plus avec les deux nœuds ci-dessus). **[[symbiote_thermal_3:2]]** vise les Capteurs **et** la part température des Collecteurs.
- **[[symbiote_thermal_4]]** ne touche que la part température d'un Collecteur (température maximale / 4), jamais ses 20 d'énergie de base.
- **[[symbiote_thermal_5]]** : la température d'une planète suit le mois, de sa minimale le 1er à sa maximale au milieu du mois. Avec ce nœud, les Capteurs lisent toujours la maximale.
- **[[symbiote_thermal_6:1]]** relève le Condensateur à ×1 là où il tombe sous 1 (température maximale lue au-dessus de 110 °C). **[[symbiote_thermal_6:2]]** relève les Capteurs à ×1,25 partout où leur facteur est plus bas.
- **[[symbiote_thermal_8]]** s'ajoute au décalage du Climatiseur.
- **[[symbiote_thermal_9]]** lit la température minimale, soit 40 °C sous la maximale, décalage compris.""",
        'growth': """- **[[symbiote_growth_1]]**, **[[symbiote_growth_5]]** et **[[symbiote_growth_3:1]]** ou **[[symbiote_growth_3:2]]** s'additionnent puis multiplient le bonus de position : +65 % au plus sur une mine. Rien là où la position ne donne rien.
- **[[symbiote_growth_2]]** : la planète mère n'a jamais de bonus de position sans ce nœud. La part s'applique au bonus déjà élargi par les nœuds ci-dessus.
- **[[symbiote_growth_4]]** : chaque niveau de Base lunaire donne 6 cases au rang 3, toujours dans la limite du diamètre de la lune, sauf avec [[symbiote_growth_6:2]].
- **[[symbiote_growth_6:1]]** ne vaut que pour les planètes, pas les lunes.
- **[[symbiote_growth_7]]** ne vise que le Modulateur planétaire et la Base lunaire ; la réduction s'ajoute aux autres réductions de prix des bâtiments, au-delà de leur plafond commun.
- **[[symbiote_growth_8]]** : 6 cases par niveau de Modulateur au lieu de 5, et la case de plus des niveaux pairs reste (Modulateur 6 : 33 → 39 cases).
- **[[symbiote_growth_9]]** : une fois tous les 7 jours pour **tout l'empire**, jamais la planète mère. La position visée doit être libre, sans lune et hors espace lointain. Refusée si une flotte d'un autre joueur se dirige vers la colonie, si l'une de vos flottes vole vers elle ou depuis elle, ou en mode vacances. La colonie garde sa taille et ses bâtiments, mais prend la température et le bonus de position de sa nouvelle place.""",
        'host': """- **[[symbiote_host_1]]** compte dans l'accent de vitesse des bâtiments. Une vitesse divise la durée : +10 % = durée ÷ 1,1.
- **[[symbiote_host_3:1]]** et **[[symbiote_host_3:2]]** lisent le **total** de cases de la planète, qui grandit avec le Modulateur planétaire et les cases bonus. La planète mère démarre à 163 cases : ni petite, ni géante. [[symbiote_host_3:1]] s'ajoute aux autres réductions de prix des bâtiments.
- **[[symbiote_host_4]]** porte le seuil de friche à 60, 70 puis 80 % des cases bâties.
- **[[symbiote_host_5]]** compte toute planète d'un autre joueur dans le système, alliés et bots compris ; les lunes ne comptent pas. Le décompte est refait régulièrement, avec un court retard.
- **[[symbiote_host_6:1]]** **remplace** le taux de [[symbiote_host_5]] (2 % par voisin au lieu de 1 %, 15 % au plus au lieu de 8 %) : ils ne s'additionnent pas. **[[symbiote_host_6:2]]** vaut quand aucun autre joueur n'a de planète dans le système ; vos propres planètes n'empêchent rien.
- **[[symbiote_host_7]]** : il suffit d'une autre de vos planètes dans le système. Le bonus ne grandit pas avec leur nombre, et il s'ajoute à [[symbiote_host_5]], [[symbiote_host_6:1]] ou [[symbiote_host_6:2]].
- **[[symbiote_host_8]]** ne se déclenche que si le raid a emporté des ressources. Un nouveau raid relance les 6 h.
- **[[symbiote_host_9]]** : jamais une lune. La première planète désignée l'est tout de suite. En désigner une autre retire aussitôt le statut à l'ancienne, et la nouvelle ne l'obtient que 7 jours plus tard.
- Au plus, l'Hôte ajoute +47 % aux mines d'une planète (15 + 8 + 15 + 9), et +20 % de plus pendant 6 h après un raid.""",
    },
    'caps_note': "La ligne des cases se complète avec [[common_exploration_5]] de l'arbre commun (+2) : l'arbre de classe n'en donne que 2 sur les 4. Les bonus de l'Hôte, le Climatiseur, les planchers de rendement, les cases de la Base lunaire et du Modulateur sont des mécaniques bornées à ce que l'arbre donne : aucun point n'y est perdu.",
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Climatologue | Thermie 15 · Hôte 10 | [[symbiote_thermal_9]], bonus de température +40 % sur les deux facteurs et +25 % de plus sur l'un, Climatiseur de 30 °C, [[symbiote_thermal_4]], [[symbiote_thermal_5]], [[symbiote_thermal_8]] ; [[symbiote_host_1]], planètes en friche +15 %, petits mondes ou géants, friche jusqu'à 80 % des cases, [[symbiote_host_5]], [[symbiote_host_6:1]] ou [[symbiote_host_6:2]] |
| Colon | Croissance 15 · Thermie 10 | [[symbiote_growth_9]], bonus de position +45 % (+65 % sur une mine), planète mère à la moitié de son bonus, [[symbiote_growth_4]], [[symbiote_growth_7]], [[symbiote_growth_8]] ; bonus de température **+10 %** seulement (+35 % sur un bâtiment avec le pôle), Climatiseur de 30 °C, [[symbiote_thermal_4]], [[symbiote_thermal_5]] |
| Jardinier | Hôte 15 · Croissance 10 | [[symbiote_host_9]], planètes en friche +15 %, [[symbiote_host_5]], [[symbiote_host_7]], [[symbiote_host_8]] ; bonus de position +45 % (+65 % sur une mine), [[symbiote_growth_2]], [[symbiote_growth_4]], +2 cases ou [[symbiote_growth_6:2]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Un bonus de température ne change jamais de signe** : sur une planète trop chaude pour le Condensateur d'hydrogène (facteur sous 1), [[symbiote_thermal_1]] n'ajoute rien, c'est [[symbiote_thermal_6:1]] qui relève le plancher. De même, sous 0 °C, les Capteurs photovoltaïques n'ont pas de bonus à élargir : seul [[symbiote_thermal_6:2]] les aide.",
        "**[[symbiote_thermal_2]] tire dans les deux sens** : vers le froid, la planète gagne de l'hydrogène mais perd de l'énergie solaire ; vers le chaud, l'inverse.",
        "**10 points en Thermie ne donnent pas les +40 %** : [[symbiote_thermal_7]] est en rangée 7. Sans elle, l'amplitude générale reste à 10 %.",
        "**Le bonus de position ne concerne que deux mines**, et ses positions dépendent du nombre de positions du système : positions 1 à 3 et 6 à 10 dans un système à 15 positions (Redline). Sur les autres positions, [[symbiote_growth_1]] et [[symbiote_growth_5]] n'apportent rien.",
        "**« En friche » n'est pas « jeune »** : une colonie est jeune pendant ses premiers jours (arbre commun) ; une planète est en friche tant que ses cases ne sont pas assez bâties. Chaque niveau construit la rapproche du seuil.",
        "**[[symbiote_host_6:1]] remplace [[symbiote_host_5]]**, elle ne s'y ajoute pas.",
        "**Le total de cases bouge** : un niveau de Modulateur planétaire ou [[symbiote_growth_6:1]] peut faire perdre [[symbiote_host_3:1]] (passer de 149 à 151 cases) ou gagner [[symbiote_host_3:2]].",
        "**[[symbiote_host_8]] veut un vrai butin** : un raid gagnant sur un stock vide ne déclenche rien.",
        "**[[symbiote_growth_9]] ne sert qu'une fois par semaine pour tout l'empire**, et la colonie déplacée change de température : son Condensateur et ses Capteurs produisent autrement.",
        "**[[symbiote_host_9]] n'a pas de recouvrement** : en changeant de planète, l'ancienne perd le statut tout de suite et la nouvelle l'obtient 7 jours plus tard.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Classes](/fr/dynasty/classes)", "[Arbre commun](/fr/dynasty/common-tree)",
        "[Dynasties](/fr/dynasty/dynasties)", "[Planètes : taille, température, type](/fr/universe/planets)",
        "[L'énergie](/fr/economy/energy)", "[L'Énergéticien](/fr/dynasty/classes/energist)",
    ],
}

EN = {
    'brief': "the Symbiote plays what others endure: the planet's temperature, its place in the system, its size, its moon and its neighbours. Thermal turns temperature into an asset, Growth makes the most of position and fields, Host makes fallow planets and planets with neighbours produce.",
    'rules': [
        "Generic mine production, young colonies and generic fields come from the [common tree](/en/dynasty/common-tree). Fusion, the Solar Collectors' own output and energy shortage belong to the [Energetician](/en/dynasty/classes/energist). The Symbiote has a single **accent**: 2 more fields per planet ([[symbiote_growth_6:1]]), 4 at most with [[common_exploration_5]] (common tree).",
        "The Host's mine bonuses are mechanics of their own: they add to each other and to the other bonuses, all computed on the **gross output** of the three mines (Mineral Excavator, Crystal Extractor, Hydrogen Condenser), and they stay **outside** the talents' production cap. Never on a moon.",
        "Temperature talents only widen a factor's **bonus share**, never its sign. Hydrogen Condenser: factor 1.44 − 0.004 × maximum temperature, widened only above 1. Photovoltaic Sensors: factor 1 + the day's temperature / 100, widened only above 0 °C. Solar Collector: maximum temperature / 4 + 20 energy, only the temperature share is widened, rounded down. Temperatures are detailed on [Planets: size, temperature, type](/en/universe/planets).",
        "The position bonus **depends on the number of positions in the system**, a universe setting (15 on Redline). In a 15-position system, the Crystal Extractor gains +40, +30 and +20% in positions 1 to 3, the Mineral Excavator +17, +23, +35, +23 and +17% in positions 6 to 10. Elsewhere, the position is brought onto a 15-position scale and the bonus is computed between the two neighbouring positions: in a 9-position system, position 2 gives +22.5% crystal. The Hydrogen Condenser never gets a position bonus.",
        "A planet is **fallow** while its built fields are strictly under 50% of its total fields (Planetary Modulator and bonus fields included). This only exists for a Symbiote holding [[symbiote_host_1]] or [[symbiote_host_2]], and never applies to a moon. It has nothing to do with the common tree's young colony.",
    ],
    'example': """**Hydrogen Condenser in position 15 of a 15-position system** (−85 to −45 °C)
- No talent: 1.44 − 0.004 × (−45) = **1.62**. The bonus share is 0.62.
- With [[symbiote_thermal_1]] (+10%): 1 + 0.62 × 1.10 = **1.68**.
- Adding [[symbiote_thermal_7]] at rank 3 (+40% in all): 1 + 0.62 × 1.40 = **1.87**.
- Adding [[symbiote_thermal_3:1]] (+65% in all): 1 + 0.62 × 1.65 = **2.02**.
- Full branch, with [[symbiote_thermal_9]] and [[symbiote_thermal_2]] set toward the cold: the Condenser reads −85 − 30 = −115 °C, factor 1.44 + 0.46 = 1.90, then 1 + 0.90 × 1.65 = **2.485**.
- At level 20, economy speed ×1 (Redline): 10 × 20 × 1.1²⁰ = 1,345.5 hydrogen per hour before the factor, that is **2,179** with no talent and **3,343** with the full branch (+53%).

**[[symbiote_thermal_9]] on a colony in position 8 of a 15-position system** (20 to 60 °C)
- No talent, the Condenser reads the maximum temperature: 1.44 − 0.004 × 60 = **1.20**.
- With the ultimate, it reads the minimum: 1.44 − 0.004 × 20 = **1.36**, that is 13% more hydrogen.

**Mineral Excavator position bonus in position 8 of a 15-position system** (+35% with no talent)
- [[symbiote_growth_1]]: 35 × 1.15 = **+40.25%**.
- [[symbiote_growth_1]] and [[symbiote_growth_5]]: 35 × 1.45 = **+50.75%**.
- Adding [[symbiote_growth_3:1]]: 35 × 1.65 = **+57.75%**.
- A homeworld at the same spot, with [[symbiote_growth_1]], [[symbiote_growth_5]] and [[symbiote_growth_2]] at rank 3: 35 × 1.45 × ½ = **+25.375%**.

**Solar Collector in position 8 of a 15-position system** (maximum temperature 60 °C)
- No talent: 60 / 4 + 20 = **35** energy per Collector.
- [[symbiote_thermal_4]] at rank 3: 15 × 1.45 + 20 = 41.75, rounded down to **41**.
- [[symbiote_thermal_8]]: the planet is read at 100 °C, 100 / 4 + 20 = **45**.
- [[symbiote_thermal_4]] at rank 3, [[symbiote_thermal_3:2]], [[symbiote_thermal_8]] and [[symbiote_thermal_2]] set toward the heat: (60 + 30 + 40) / 4 = 32.5, × 1.70 (45 + 25% amplitude) = 55.25, + 20 = **75**.

**Host on a 210-field colony with 100 fields built, Mineral Excavator level 20** (4,036 metal per hour gross, speed ×1)
- Fallow (100 / 210 = 47.6%) with [[symbiote_host_2]] at rank 3: +15%. [[symbiote_host_3:2]] (over 200 fields): +8%. Three planets of other players in the system with [[symbiote_host_6:1]]: 3 × 2 = +6%. Another of your planets in the system with [[symbiote_host_7]] at rank 3: +9%.
- Total **+38%**: 4,036 × 0.38 = **1,533** more metal per hour.
- For 6 h after a raid that took resources, [[symbiote_host_8]] adds 20%: +58%, that is **2,340**.""",
    'branch_notes': {
        'thermal': """- **[[symbiote_thermal_1]]** and **[[symbiote_thermal_7]]** add up (40% at most) and work on the Hydrogen Condenser and the Photovoltaic Sensors, not on Solar Collectors.
- **[[symbiote_thermal_2]]**: never on a moon. The first setting is immediate; after that each planet waits 7 days between two settings, going back to "no shift" included. The shift applies to the Condenser, the Sensors and the Collectors at once, in the same direction: toward the cold, more hydrogen and less solar energy.
- **[[symbiote_thermal_3:1]]** only targets the Condenser (65% amplitude at most with the two nodes above). **[[symbiote_thermal_3:2]]** targets the Sensors **and** the Collectors' temperature share.
- **[[symbiote_thermal_4]]** only touches a Collector's temperature share (maximum temperature / 4), never its 20 base energy.
- **[[symbiote_thermal_5]]**: a planet's temperature follows the month, from its minimum on the 1st to its maximum mid-month. With this node, the Sensors always read the maximum.
- **[[symbiote_thermal_6:1]]** raises the Condenser to ×1 wherever it falls under 1 (maximum temperature read above 110 °C). **[[symbiote_thermal_6:2]]** raises the Sensors to ×1.25 wherever their factor is lower.
- **[[symbiote_thermal_8]]** adds to the Climate Control's shift.
- **[[symbiote_thermal_9]]** reads the minimum temperature, 40 °C under the maximum, shift included.""",
        'growth': """- **[[symbiote_growth_1]]**, **[[symbiote_growth_5]]** and **[[symbiote_growth_3:1]]** or **[[symbiote_growth_3:2]]** add up, then multiply the position bonus: +65% at most on one mine. Nothing where the position gives nothing.
- **[[symbiote_growth_2]]**: the homeworld never gets a position bonus without this node. The share applies to the bonus already widened by the nodes above.
- **[[symbiote_growth_4]]**: each Lunar base level gives 6 fields at rank 3, always within the moon's diameter, except with [[symbiote_growth_6:2]].
- **[[symbiote_growth_6:1]]** only applies to planets, not moons.
- **[[symbiote_growth_7]]** only targets the Planetary Modulator and the Lunar base; the reduction adds to the other building price reductions, past their common cap.
- **[[symbiote_growth_8]]**: 6 fields per Modulator level instead of 5, and the extra field of even levels stays (Modulator 6: 33 → 39 fields).
- **[[symbiote_growth_9]]**: once every 7 days for **the whole empire**, never the homeworld. The target position must be free, moonless and outside deep space. Refused while another player's fleet is heading for the colony, while one of your fleets flies to or from it, or in vacation mode. The colony keeps its size and buildings, but takes the temperature and position bonus of its new spot.""",
        'host': """- **[[symbiote_host_1]]** counts in the buildings' speed accent. A speed divides the duration: +10% = duration ÷ 1.1.
- **[[symbiote_host_3:1]]** and **[[symbiote_host_3:2]]** read the planet's **total** fields, which grow with the Planetary Modulator and bonus fields. The homeworld starts at 163 fields: neither small nor giant. [[symbiote_host_3:1]] adds to the other building price reductions.
- **[[symbiote_host_4]]** brings the fallow threshold to 60, 70 then 80% of fields built.
- **[[symbiote_host_5]]** counts every planet of another player in the system, allies and bots included; moons do not count. The count is refreshed regularly, with a short delay.
- **[[symbiote_host_6:1]]** **replaces** the rate of [[symbiote_host_5]] (2% per neighbour instead of 1%, 15% at most instead of 8%): they do not add up. **[[symbiote_host_6:2]]** applies when no other player has a planet in the system; your own planets do not prevent it.
- **[[symbiote_host_7]]**: one other planet of yours in the system is enough. The bonus does not grow with their number, and it adds to [[symbiote_host_5]], [[symbiote_host_6:1]] or [[symbiote_host_6:2]].
- **[[symbiote_host_8]]** only triggers if the raid took resources. A new raid restarts the 6 h.
- **[[symbiote_host_9]]**: never a moon. The first planet named is fallow at once. Naming another removes the status from the old one at once, and the new one only gets it 7 days later.
- At most, the Host adds +47% to a planet's mines (15 + 8 + 15 + 9), and +20% more for 6 h after a raid.""",
    },
    'caps_note': "The fields row is completed by the common tree's [[common_exploration_5]] (+2): the class tree only gives 2 of the 4. The Host's bonuses, the Climate Control, the yield floors, the Lunar base and Modulator fields are mechanics bounded to what the tree gives: no point is lost there.",
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Climatologist | Thermal 15 · Host 10 | [[symbiote_thermal_9]], temperature bonus +40% on both factors and +25% more on one, 30 °C Climate Control, [[symbiote_thermal_4]], [[symbiote_thermal_5]], [[symbiote_thermal_8]]; [[symbiote_host_1]], fallow planets +15%, small worlds or giants, fallow up to 80% of fields, [[symbiote_host_5]], [[symbiote_host_6:1]] or [[symbiote_host_6:2]] |
| Settler | Growth 15 · Thermal 10 | [[symbiote_growth_9]], position bonus +45% (+65% on one mine), homeworld at half its bonus, [[symbiote_growth_4]], [[symbiote_growth_7]], [[symbiote_growth_8]]; temperature bonus **+10%** only (+35% on one building with the pole), 30 °C Climate Control, [[symbiote_thermal_4]], [[symbiote_thermal_5]] |
| Gardener | Host 15 · Growth 10 | [[symbiote_host_9]], fallow planets +15%, [[symbiote_host_5]], [[symbiote_host_7]], [[symbiote_host_8]]; position bonus +45% (+65% on one mine), [[symbiote_growth_2]], [[symbiote_growth_4]], +2 fields or [[symbiote_growth_6:2]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**A temperature bonus never changes sign**: on a planet too hot for the Hydrogen Condenser (factor under 1), [[symbiote_thermal_1]] adds nothing, [[symbiote_thermal_6:1]] is what raises the floor. Likewise, under 0 °C the Photovoltaic Sensors have no bonus to widen: only [[symbiote_thermal_6:2]] helps them.",
        "**[[symbiote_thermal_2]] cuts both ways**: toward the cold, the planet gains hydrogen but loses solar energy; toward the heat, the reverse.",
        "**10 points in Thermal do not give the +40%**: [[symbiote_thermal_7]] is in row 7. Without it, the general amplitude stays at 10%.",
        "**The position bonus only concerns two mines**, and its positions depend on the number of positions in the system: positions 1 to 3 and 6 to 10 in a 15-position system (Redline). On other positions, [[symbiote_growth_1]] and [[symbiote_growth_5]] bring nothing.",
        "**\"Fallow\" is not \"young\"**: a colony is young for its first days (common tree); a planet is fallow while its fields are not built enough. Every level built brings it closer to the threshold.",
        "**[[symbiote_host_6:1]] replaces [[symbiote_host_5]]**, it does not add to it.",
        "**The total of fields moves**: a Planetary Modulator level or [[symbiote_growth_6:1]] can lose you [[symbiote_host_3:1]] (going from 149 to 151 fields) or win you [[symbiote_host_3:2]].",
        "**[[symbiote_host_8]] needs real loot**: a won raid on an empty stock triggers nothing.",
        "**[[symbiote_growth_9]] only works once a week for the whole empire**, and the moved colony changes temperature: its Condenser and Sensors produce differently.",
        "**[[symbiote_host_9]] has no overlap**: when changing planet, the old one loses the status at once and the new one gets it 7 days later.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Classes](/en/dynasty/classes)", "[Common tree](/en/dynasty/common-tree)",
        "[Dynasties](/en/dynasty/dynasties)", "[Planets: size, temperature, type](/en/universe/planets)",
        "[Energy](/en/economy/energy)", "[The Energetician](/en/dynasty/classes/energist)",
    ],
}
