"""L'Ombre : textes vérifiés sur le code (note du 15 octobre 2026, SpyMechanics, SpyMissionResolver, CounterEspionageCalculator)."""

FR = {
    'brief': "l'Ombre joue les deux sens du renseignement : lire chez les autres sans se faire prendre, et rendre son propre territoire illisible. Ses talents sont des règles, pas des pourcentages génériques, et elle n'a aucun accent.",
    'rules': [
        "Les talents de l'Ombre s'appuient sur les règles de l'[espionnage](/fr/espionage/spying) : niveau effectif = écart de Renseignement Tactique + 1 par paire d'Éclaireurs (+5 au plus) ; paliers du rapport : ressources dès 1, flotte dès 3, défenses et missiles dès 5, bâtiments dès 7, recherches dès 9 ; chance de détection bornée entre 5 % et 25 %, nulle si votre Renseignement Tactique vaut au moins le double de celui de la cible ou si l'orbite est vide.",
        "Les points de détection ([[shadow_stealth_2]] pour l'espion, [[shadow_counterlight_2]] pour la cible) s'appliquent **avant** la borne de 5 % à 25 % : ils ne font jamais descendre la chance sous 5 % ni monter au-delà de 25 %, et ne créent pas de chance là où elle est nulle.",
        "La **profondeur** ([[shadow_infiltration_2]], [[shadow_infiltration_8]], [[shadow_counterlight_8]]) ne change jamais la chance de détection.",
        "Une vague **prise** est identifiée (le défenseur apprend votre pseudo) ; un second tirage peut la **tracer** (il apprend aussi la planète d'origine). Le défenseur reçoit une alerte d'intrusion à chaque vague, même non détectée.",
    ],
    'example': """**Le risque d'une vague, des deux côtés**
- Cible : Renseignement Tactique 8, 40 vaisseaux en orbite. Espion : Renseignement Tactique 8. Chance : (2 × 8 − 8) × 40 × 0,05 = **16 %**.
- L'espion a [[shadow_stealth_2]] au rang 3 : 16 − 6 = **10 %**. Sa [[shadow_stealth_5]] (15 %) ne le fait pas renoncer.
- Si la cible a [[shadow_counterlight_2]] au rang 3 : 16 + 6 − 6 = **16 %** : la vague fait demi-tour.
- Contre une cible à 8 % : 8 − 6 = 2, relevé à la borne : **5 %**.

**Lire les défenses avec 4 Éclaireurs, à Renseignement Tactique égal**
- Sans talent : 4 Éclaireurs donnent +2 ; niveau effectif 2 : seules les ressources se lisent.
- [[shadow_infiltration_2]] au rang 3 : la vague compte pour 4 + 6 = 10 Éclaireurs, soit +5 ; niveau 5 : ressources, flotte, défenses et missiles.
- Si la cible a [[shadow_counterlight_8]] : niveau 4, les défenses restent fermées. Avec [[shadow_infiltration_8]] en plus : 5 à nouveau.

**Une vague de 9 Éclaireurs prise**
- [[shadow_stealth_3:1]] seule : 9 × 20 % = 1,8, arrondi à l'inférieur : **1** rentre, 8 sont perdus.
- Avec [[shadow_stealth_4]] au rang 3 : 9 × 41 % = 3,69 : **3** rentrent.
- [[shadow_stealth_3:2]] et [[shadow_stealth_4]] au rang 3 : 9 × 21 % = 1,89 : **1** rentre.

**[[shadow_counterlight_6:2]]** : 117 Corvettes sont lues 120 ; 1 234 Intercepteurs, 1 200 ; 19 Cuirassés, 19.""",
    'branch_notes': {
        'infiltration': """- **[[shadow_infiltration_1]]** : quand la section ressources se lit, le rapport donne aussi la production horaire et les entrepôts de la cible, pour projeter le stock à l'arrivée de votre raid.
- **[[shadow_infiltration_2]]** : il faut au moins 1 Éclaireur dans la vague ; le bonus tiré des Éclaireurs reste plafonné à +5.
- **[[shadow_infiltration_3:1]]** : les ressources se lisent toujours, même avec un écart négatif et un seul Éclaireur. **[[shadow_infiltration_3:2]]** : la flotte se lit dès le niveau effectif 2 ; avec Écouter loin de [L'Accord](/fr/dynasty/dynasties), dès 1.
- **[[shadow_infiltration_4]]** : seules les sections du même corps (la planète ou sa lune) sont reprises ; le jeu garde les 10 derniers rapports par case.
- **[[shadow_infiltration_5]]** : le second rapport a le même résultat de détection que la vague.
- **[[shadow_infiltration_6:1]]** : seules les planètes sont listées, avec le pseudo, le statut (actif, inactif, abandonnée, en vacances) et une fourchette du stock total : moins de 10 000, 10 000, 50 000, 100 000, 250 000, 500 000, 1 000 000, 2 500 000, 5 000 000 et plus. Pas de stock pour un joueur en vacances.
- **[[shadow_infiltration_6:2]]** donne Systèmes Offensifs, Champs de Protection et Métallurgie Avancée tant que la flotte se lit et pas les recherches ; le palier de la flotte suit [[shadow_infiltration_3:2]].
- **[[shadow_infiltration_7]]** : présent même dans un rapport qui ne lit rien d'autre (pas sur une base abandonnée). Au rang 2, l'heure est arrondie au quart d'heure inférieur ; au rang 3, la base que le joueur a sélectionnée en dernier.
- **[[shadow_infiltration_9]]** : se demande à l'envoi. L'Éclaireur laissé en orbite est perdu pour votre flotte. Il fait un rapport à chaque départ ou arrivée de flotte sur la base. Pris, il est détruit et l'alerte du défenseur vous nomme, sans donner votre planète. Un seul par base visée : en reposer un relance les 6 h.""",
        'stealth': """- **[[shadow_stealth_1]]** : l'écran d'envoi calcule la chance au moment de l'envoi ; le tirage se fait à l'arrivée des Éclaireurs.
- **[[shadow_stealth_3:1]]** et **[[shadow_stealth_4]]** s'additionnent ; le nombre d'Éclaireurs sauvés est arrondi à l'inférieur, un Éclaireur seul ne rentre jamais. [[shadow_stealth_3:2]] étant l'autre choix, la survie est alors de 21 % au plus.
- **[[shadow_stealth_5]]** : compare la chance bornes comprises. La vague a fait le vol aller-retour et payé son hydrogène. Vous recevez une notification.
- **[[shadow_stealth_6:1]]** : vaut pour tout balayage de Phalange de capteur, y compris ceux partagés en alliance.
- **[[shadow_stealth_6:2]]** : seulement les Attaques à l'aller, pour tout autre joueur (cible et Phalanges).
- **[[shadow_stealth_7]]** : la fausse origine est une planète d'un joueur inactif de votre galaxie ; s'il n'y en a aucune, la vraie origine est donnée. Inutile avec [[shadow_stealth_3:2]], puisque la vague n'est jamais tracée.
- **[[shadow_stealth_8]]** : « aucun risque » veut dire une chance de 0 % ; une cible qui a [[shadow_counterlight_1]] garde ses orbites vides à 5 %. Le défenseur reçoit « activité repérée » dans son système, à l'heure près, au lieu de l'alerte.
- **[[shadow_stealth_9]]** : se déclenche seul sur la **première** vague prise du cycle. Elle reste prise : le défenseur reçoit son alerte et peut la tracer.""",
        'counterlight': """- **[[shadow_counterlight_1]]** : l'écart de Renseignement Tactique doit rester en votre faveur. Avec [[shadow_counterlight_2]] au rang 3, une orbite vide est gardée à 6 %.
- **[[shadow_counterlight_3:1]]** : chaque alerte d'intrusion reçue est copiée en notification aux autres membres de votre alliance.
- **[[shadow_counterlight_4]]** : chaque ressource est lue à 70 % au rang 3 (arrondi à l'inférieur), dans tout rapport d'un autre joueur sur vos bases : vague, Mouchard, Retour de sonde, Repérage de système.
- **[[shadow_counterlight_5]]** : vous apprenez le pseudo et la lune du joueur. Rien contre un Oracle qui a [[oracle_watch_6:1]].
- **[[shadow_counterlight_6:1]]** : seulement si vous possédez aussi l'autre corps de la case.
- **[[shadow_counterlight_6:2]]** : chaque nombre de vaisseaux est arrondi par pas de 1, 10, 100… selon sa taille ; sous 20 vaisseaux d'un type, le nombre reste exact.
- **[[shadow_counterlight_8]]** ne joue pas sur un Mouchard, qui lit toujours au palier 3.
- **[[shadow_counterlight_9]]** : seulement sur une vague tracée. Le rapport lit la planète d'origine, ou la fausse origine si [[shadow_stealth_7]] a joué. L'espion reçoit « activité repérée » dans son système, à l'heure près.""",
    },
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chasseur | Pénétration 15 · Discrétion 10 | [[shadow_infiltration_9]], [[shadow_infiltration_6:2]] ou [[shadow_infiltration_6:1]], [[shadow_infiltration_8]], activité à la base près, [[shadow_infiltration_4]] de 24 h ; −6 points de détection, [[shadow_stealth_5]], survie 41 % (ou [[shadow_stealth_3:2]]), [[shadow_stealth_6:1]] (Phalanges sans composition) ou [[shadow_stealth_6:2]] |
| Fantôme | Discrétion 15 · Pénétration 10 | [[shadow_stealth_9]], [[shadow_stealth_8]], [[shadow_stealth_7]] à 90 %, survie 41 % ; [[shadow_infiltration_1]], bâtiments lus avec 4 Éclaireurs si votre Renseignement Tactique a 2 niveaux d'avance, [[shadow_infiltration_4]] de 24 h, [[shadow_infiltration_5]] |
| Gardien | Contre-jour 15 · Discrétion 10 | [[shadow_counterlight_9]], [[shadow_counterlight_8]], stock lu à 70 %, [[shadow_counterlight_7]] +15 points, [[shadow_counterlight_1]] ; ses propres vagues à −6 points avec [[shadow_stealth_5]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Écouter loin et [[shadow_infiltration_3:2]] se cumulent** : une Ombre de L'Accord qui prend [[shadow_infiltration_3:2]] lit la flotte **deux paliers** plus tôt.",
        "**[[shadow_infiltration_8]] ne réduit pas le risque** : il ajoute de la profondeur, jamais de discrétion.",
        "**[[shadow_stealth_2]] bute sur la borne de 5 %** : contre une cible peu gardée, une partie des 6 points ne sert à rien.",
        "**Plus de « toutes ou aucune »** : avec [[shadow_stealth_3:1]] et [[shadow_stealth_4]], une partie des Éclaireurs d'une vague prise rentre. Sans ces talents, toute la vague tombe ; un Éclaireur seul ne rentre jamais.",
        "**[[shadow_stealth_3:2]] et [[shadow_stealth_7]] ne vont pas ensemble** : une vague jamais tracée n'a pas d'origine à fausser.",
        "**[[shadow_stealth_9]] part tout seul** sur la première vague prise du cycle, même une vague d'un seul Éclaireur.",
        "**[[shadow_infiltration_9]] coûte un Éclaireur** à chaque pose.",
        "**[[shadow_counterlight_4]] ne protège rien** : il fausse le rapport ennemi, le stock reste entièrement pillable.",
        "**[[shadow_counterlight_8]] annule [[shadow_infiltration_8]]** : contre une Ombre qui a pris Contre-jour jusqu'à la rangée 8, votre niveau effectif en plus disparaît.",
        "**[[shadow_counterlight_9]] se remarque** : l'espion apprend qu'il y a eu de l'activité dans son système.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Arbre commun](/fr/dynasty/common-tree)", "[Classes](/fr/dynasty/classes)",
        "[Dynasties](/fr/dynasty/dynasties)", "[Espionner](/fr/espionage/spying)",
        "[Lire un rapport d'espionnage](/fr/espionage/spy-report)", "[Phalange de capteur](/fr/espionage/sensor-phalanx)",
    ],
}

EN = {
    'brief': "the Shadow plays intelligence both ways: reading others without getting caught, and making its own territory unreadable. Its talents are rules, not generic percentages, and it has no accent.",
    'rules': [
        "The Shadow's talents build on the rules of [espionage](/en/espionage/spying): effective level = Espionage Technology gap + 1 per pair of Scouts (+5 at most); report tiers: resources from 1, fleet from 3, defences and missiles from 5, buildings from 7, research from 9; detection chance bounded between 5% and 25%, zero if your Espionage Technology is at least double the target's or if the orbit is empty.",
        "Detection points ([[shadow_stealth_2]] for the spy, [[shadow_counterlight_2]] for the target) apply **before** the 5% to 25% band: they never take the chance below 5% or above 25%, and never create a chance where it is zero.",
        "**Depth** ([[shadow_infiltration_2]], [[shadow_infiltration_8]], [[shadow_counterlight_8]]) never changes the detection chance.",
        "A **caught** wave is identified (the defender learns your name); a second roll may **trace** it (they also learn the planet of origin). The defender gets an intrusion alert for every wave, even an undetected one.",
    ],
    'example': """**A wave's risk, from both sides**
- Target: Espionage Technology 8, 40 ships in orbit. Spy: Espionage Technology 8. Chance: (2 × 8 − 8) × 40 × 0.05 = **16%**.
- The spy has [[shadow_stealth_2]] at rank 3: 16 − 6 = **10%**. Their [[shadow_stealth_5]] (15%) does not turn them back.
- If the target has [[shadow_counterlight_2]] at rank 3: 16 + 6 − 6 = **16%**: the wave turns back.
- Against an 8% target: 8 − 6 = 2, raised to the band: **5%**.

**Reading defences with 4 Scouts, at equal Espionage Technology**
- With no talent: 4 Scouts give +2; effective level 2: only resources are read.
- [[shadow_infiltration_2]] at rank 3: the wave counts as 4 + 6 = 10 Scouts, that is +5; level 5: resources, fleet, defences and missiles.
- If the target has [[shadow_counterlight_8]]: level 4, defences stay closed. With [[shadow_infiltration_8]] as well: 5 again.

**A caught wave of 9 Scouts**
- [[shadow_stealth_3:1]] alone: 9 × 20% = 1.8, rounded down: **1** comes home, 8 are lost.
- With [[shadow_stealth_4]] at rank 3: 9 × 41% = 3.69: **3** come home.
- [[shadow_stealth_3:2]] and [[shadow_stealth_4]] at rank 3: 9 × 21% = 1.89: **1** comes home.

**[[shadow_counterlight_6:2]]**: 117 Corvettes read as 120; 1,234 Interceptors, 1,200; 19 Battleships, 19.""",
    'branch_notes': {
        'infiltration': """- **[[shadow_infiltration_1]]**: when the resources section is read, the report also gives the target's hourly production and storage, to project the stock at your raid's arrival.
- **[[shadow_infiltration_2]]**: the wave needs at least 1 Scout; the bonus from Scouts stays capped at +5.
- **[[shadow_infiltration_3:1]]**: resources are always read, even with a negative gap and a single Scout. **[[shadow_infiltration_3:2]]**: the fleet is read from effective level 2; with Listening Far from [The Accord](/en/dynasty/dynasties), from 1.
- **[[shadow_infiltration_4]]**: only sections of the same body (the planet or its moon) are carried over; the game keeps the last 10 reports per cell.
- **[[shadow_infiltration_5]]**: the second report has the same detection result as the wave.
- **[[shadow_infiltration_6:1]]**: only planets are listed, with the player name, the status (active, inactive, abandoned, on vacation) and a bracket of the total stock: under 10,000, 10,000, 50,000, 100,000, 250,000, 500,000, 1,000,000, 2,500,000, 5,000,000 and more. No stock for a player on vacation.
- **[[shadow_infiltration_6:2]]** gives Weapon Systems, Shielding Technology and Armor Technology while the fleet is read but not the research; the fleet tier follows [[shadow_infiltration_3:2]].
- **[[shadow_infiltration_7]]**: present even in a report that reads nothing else (not on an abandoned base). At rank 2, the time is rounded down to the quarter hour; at rank 3, the base the player last selected.
- **[[shadow_infiltration_9]]**: requested when sending. The Scout left in orbit is lost to your fleet. It reports at every fleet departure or arrival on the base. Caught, it is destroyed and the defender's alert names you, without giving your planet. Only one per targeted base: placing another restarts the 6 h.""",
        'stealth': """- **[[shadow_stealth_1]]**: the sending screen computes the chance at sending time; the roll happens when the Scouts arrive.
- **[[shadow_stealth_3:1]]** and **[[shadow_stealth_4]]** add up; the number of Scouts saved is rounded down, a lone Scout never comes home. [[shadow_stealth_3:2]] being the other choice, survival is then 21% at most.
- **[[shadow_stealth_5]]**: compares the chance with the band applied. The wave has flown the round trip and paid its hydrogen. You get a notification.
- **[[shadow_stealth_6:1]]**: applies to every Sensor phalanx sweep, including those shared in an alliance.
- **[[shadow_stealth_6:2]]**: only Attacks on their way out, for every other player (target and phalanxes).
- **[[shadow_stealth_7]]**: the false origin is a planet of an inactive player in your galaxy; if there is none, the real origin is given. Useless with [[shadow_stealth_3:2]], since the wave is never traced.
- **[[shadow_stealth_8]]**: "no risk" means a 0% chance; a target with [[shadow_counterlight_1]] keeps its empty orbits at 5%. The defender gets "activity spotted" in their system, to the hour, instead of the alert.
- **[[shadow_stealth_9]]**: fires on its own on the **first** caught wave of the cycle. It is still caught: the defender gets their alert and may trace it.""",
        'counterlight': """- **[[shadow_counterlight_1]]**: the Espionage Technology gap must still be in your favour. With [[shadow_counterlight_2]] at rank 3, an empty orbit is guarded at 6%.
- **[[shadow_counterlight_3:1]]**: every intrusion alert you receive is copied as a notification to the other members of your alliance.
- **[[shadow_counterlight_4]]**: each resource is read at 70% at rank 3 (rounded down), in any report by another player on your bases: wave, Bug, Return to Sender, System Survey.
- **[[shadow_counterlight_5]]**: you learn the player's name and moon. Nothing against an Oracle with [[oracle_watch_6:1]].
- **[[shadow_counterlight_6:1]]**: only if you also own the other body of the cell.
- **[[shadow_counterlight_6:2]]**: each ship count is rounded by steps of 1, 10, 100… depending on its size; under 20 ships of a type, the count stays exact.
- **[[shadow_counterlight_8]]** does not affect a Bug, which always reads at tier 3.
- **[[shadow_counterlight_9]]**: only on a traced wave. The report reads the planet of origin, or the false origin if [[shadow_stealth_7]] worked. The spy gets "activity spotted" in their system, to the hour.""",
    },
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Hunter | Infiltration 15 · Stealth 10 | [[shadow_infiltration_9]], [[shadow_infiltration_6:2]] or [[shadow_infiltration_6:1]], [[shadow_infiltration_8]], activity down to the base, a 24 h [[shadow_infiltration_4]]; −6 detection points, [[shadow_stealth_5]], 41% survival (or [[shadow_stealth_3:2]]), [[shadow_stealth_6:1]] (phalanxes without composition) or [[shadow_stealth_6:2]] |
| Ghost | Stealth 15 · Infiltration 10 | [[shadow_stealth_9]], [[shadow_stealth_8]], [[shadow_stealth_7]] at 90%, 41% survival; [[shadow_infiltration_1]], buildings read with 4 Scouts if your Espionage Technology is 2 levels ahead, a 24 h [[shadow_infiltration_4]], [[shadow_infiltration_5]] |
| Warden | Backlight 15 · Stealth 10 | [[shadow_counterlight_9]], [[shadow_counterlight_8]], stock read at 70%, [[shadow_counterlight_7]] +15 points, [[shadow_counterlight_1]]; its own waves at −6 points with [[shadow_stealth_5]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**Listening Far and [[shadow_infiltration_3:2]] stack**: an Accord Shadow taking [[shadow_infiltration_3:2]] reads the fleet **two tiers** earlier.",
        "**[[shadow_infiltration_8]] does not lower the risk**: it adds depth, never stealth.",
        "**[[shadow_stealth_2]] hits the 5% floor**: against a lightly guarded target, part of the 6 points is wasted.",
        "**No more \"all or nothing\"**: with [[shadow_stealth_3:1]] and [[shadow_stealth_4]], part of a caught wave's Scouts comes home. Without these talents, the whole wave falls; a lone Scout never comes home.",
        "**[[shadow_stealth_3:2]] and [[shadow_stealth_7]] do not go together**: a wave that is never traced has no origin to fake.",
        "**[[shadow_stealth_9]] fires on its own** on the first caught wave of the cycle, even a single-Scout wave.",
        "**[[shadow_infiltration_9]] costs a Scout** each time it is placed.",
        "**[[shadow_counterlight_4]] protects nothing**: it skews the enemy report, the stock stays fully lootable.",
        "**[[shadow_counterlight_8]] cancels [[shadow_infiltration_8]]**: against a Shadow that took Backlight down to row 8, your extra effective level disappears.",
        "**[[shadow_counterlight_9]] gets noticed**: the spy learns there was activity in their system.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Common tree](/en/dynasty/common-tree)", "[Classes](/en/dynasty/classes)",
        "[Dynasties](/en/dynasty/dynasties)", "[Spying](/en/espionage/spying)",
        "[Reading a spy report](/en/espionage/spy-report)", "[Sensor phalanx](/en/espionage/sensor-phalanx)",
    ],
}
