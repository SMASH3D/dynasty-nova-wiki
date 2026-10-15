"""Page dynasty/common-tree, FR et EN, d'après le code (DONNEES §18). Puis : python3 tools/talent_diagrams.py

Usage : python3 tools/dynasty_pages/p_common.py
"""
import math
import sys
from pathlib import Path

from dyn_lib import RULES, CEIL, n, pct, tree, branch_name, branch_motto, branch_table
from write import write, table

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import talent_diagrams  # noqa: E402

WARN_EN = '''> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}
'''
B = {b['key']: b for b in tree('common')}
CR = {int(k): int(v) for k, v in RULES['COMMON_ROW_RANKS'].items()}
CG = {int(k): int(v) for k, v in RULES['COMMON_ROW_GATES'].items()}
BRANCH = sum(CR.values())
ROWS6, ROWS8 = sum(CR[r] for r in range(1, 7)), sum(CR[r] for r in range(1, 9))
CMAX, ULT = RULES['COMMON_MAX_POINTS'], RULES['ULTIMATE_LEVEL']


def hms(seconds, lang):
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    parts = []
    if h:
        parts.append(f'{h} h')
    if m:
        parts.append(f'{m} min')
    if s:
        parts.append(f'{s} s')
    return ' '.join(parts)


def hasten(seconds, percent):
    """AllianceBonuses::hasten : durée divisée par 1 + bonus, arrondie à la seconde supérieure."""
    return math.ceil(seconds / (1 + percent / 100))


def fly(seconds, factor):
    """Vol : durée divisée par le facteur de vitesse, arrondie à la seconde la plus proche."""
    return round(seconds / factor)


# Valeurs d'exemple recalculées
MINE = 10000
PLASMA = 10
MINE_FULL = MINE * (1 + 25 / 100) + MINE * PLASMA * 1.5 / 100  # Prospérité pleine + Plasma 10 avec Fonderie
MINE_NOFOUNDRY = MINE * (1 + 25 / 100) + MINE * PLASMA / 100
BUILD8 = hasten(8 * 3600, 25)
RESEARCH10 = hasten(10 * 3600, 15)
RESEARCH10_ASTRO = hasten(10 * 3600, 25)
FLIGHT_B = fly(3600, 1.4)
RETURN_TAIL = fly(FLIGHT_B, 1.25)
FUEL = 10000 * (1 - 0.2)
CARGO = 25000 * 1.15
YOUTH_MAX = (168 + 72 + 120) // 24
YOUTH_NO_YW = (168 + 120) // 24
STOCK = 100000
LOOT_BASE, LOOT_FULL = STOCK * 0.5, STOCK * 0.7


def box(lang):
    if lang == 'fr':
        return '''> **Paramètre d'univers** : un joueur compte comme inactif (cible abandonnée) après un nombre de jours sans activité qui dépend de l'univers.
> Par défaut : **14 jours** · Redline : **7 jours**
{.is-info}'''
    return '''> **Universe setting**: a player counts as inactive (abandoned target) after a number of days without activity that depends on the universe.
> Default: **14 days** · Redline: **7 days**
{.is-info}'''


NOTES = {
    'fr': {
        'prosperity': [
            "Les bonus de production s'appliquent à la production brute des trois mines, avant le rapport d'énergie. Ils s'additionnent entre eux, puis sont plafonnés.",
            "**Entrepôts** s'ajoute au Centre logistique et à toute la capacité de la planète, Base planetaire comprise. **Coffres enterrés** retire 5 points au taux de pillage que vous subissez (50 % → 45 %), jamais sous 30 %.",
            "**Fonderie à plasma** : votre niveau de Maîtrise du Plasma compte une fois et demie pour la production. Ce bonus se calcule à part du plafond de production.",
            "**Réseau optimisé** augmente l'énergie produite par les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires. **Colonies prospères** touche chaque planète qui n'est ni votre planète mère ni une lune (colonies et mondes conquis), au-delà du plafond de 45 %.",
            "**Pont de ressources** : une fois par 24 heures glissantes pour tout votre empire, vers n'importe quelle autre de vos planètes ou lunes. La limite est de 2 heures de la production actuelle de la planète de départ, les trois ressources additionnées et réparties comme vous le voulez, sans dépasser son stock. La planète d'arrivée peut dépasser ses entrepôts.",
            "**Stock de sécurité** : quand un entrepôt est plein, 25 % de ce que la mine aurait produit est quand même versé, au-dessus de la capacité.",
        ],
        'exploration': [
            "**Méthode** et **Astrométrie** partagent le même plafond de 25 % : avec Méthode pleine, Renseignement Tactique et Cosmologie Appliquée vont 25 % plus vite, pas 30 %.",
            "**Cartographes** raccourcit le séjour d'exploration que vous choisissez. Le trajet ne change pas, et l'hydrogène du séjour, le risque de retard et les gains restent ceux de la durée choisie.",
            "**Arche** a trois effets sur le Pionnier spatial et la colonisation. La vitesse des colonisations reste sous le plafond total de vitesse de flotte (60 %).",
            "Une colonie est **jeune** pendant 7 jours après sa fondation par un Pionnier spatial (jamais la planète mère, une lune ou un monde conquis). Seul **Comptoirs pionniers** profite de cet état : **Jeunes mondes** n'a d'effet qu'avec lui. Avec les deux : 15 jours de jeunesse.",
            "Une **cible abandonnée** est un monde en ruine, un adversaire contrôlé par le jeu, ou un joueur inactif dans l'univers. Le taux de pillage de base est 50 % ; Pillards d'abandonnés et Pillage organisé ajoutent des points à ce taux.",
            "**Archives volées** ne compte que les pillages qui rapportent au moins une heure de production de votre planète mère (les trois ressources additionnées). Elle avance la recherche en cours (la première si deux tournent), jamais jusqu'à la fin ; les 10 charges se comptent sur 24 heures à partir de la première.",
            "**Flair de prospecteur** : 33 % des chances de ne rien trouver passent du côté des ressources. Sur une case d'espace lointain encore jamais explorée, « rien » passe de 33 % à 22,11 %, « ressources » de 33 % à 43,89 %.",
            "**Second centre d'innovation** : la seconde recherche doit être différente de la première et ne démarre que si une recherche tourne déjà. À mi-vitesse, une recherche de 4 h en dure 8.",
        ],
        'logistics': [
            "Les bonus de vitesse **divisent** la durée du vol : +40 % = un vol 1,4 fois plus court. Ils sont lus au départ de la flotte.",
            "Les réductions d'hydrogène touchent le carburant du vol, pas celui d'un séjour d'expédition. Le fret s'ajoute à la capacité déjà augmentée par la Technologie hyperespace.",
            "**Vent arrière** accélère tous les retours, rappels compris. **Liaisons internes** accélère les transports et stationnements qui arrivent sur l'une de vos planètes. Les deux multiplient la vitesse en plus du plafond de vitesse.",
            "**Chargement prioritaire** : au départ, vous fixez l'ordre dans lequel butin et débris remplissent vos soutes quand tout ne tient pas. Sans lui, chaque ressource est chargée en proportion.",
        ],
    },
    'en': {
        'prosperity': [
            "Production bonuses apply to the raw production of the three mines, before the energy ratio. They add up, then are capped.",
            "**Warehouses** adds up with the Logistics Center and applies to the planet's whole capacity, Planetary Base included. **Buried Vaults** takes 5 points off the plunder rate you suffer (50% → 45%), never below 30%.",
            "**Plasma Foundry**: your Plasma Mastery level counts one and a half times for production. This bonus is computed apart from the production cap.",
            "**Optimised Grid** raises the energy produced by Photovoltaic Sensors, the Thermonuclear Reactor and Solar Collectors. **Thriving Colonies** applies to every planet that is neither your home planet nor a moon (colonies and conquered worlds), past the 45% cap.",
            "**Resource Bridge**: once per rolling 24 hours for your whole empire, to any other of your planets or moons. The limit is 2 hours of the departure planet's current production, the three resources added together and split as you wish, never more than its stock. The arrival planet may go past its storage.",
            "**Safety Stock**: when a storage building is full, 25% of what the mine would have produced is still credited, above capacity.",
        ],
        'exploration': [
            "**Method** and **Astrometry** share the same 25% cap: with Method full, Tactical Intelligence and Applied Cosmology go 25% faster, not 30%.",
            "**Cartographers** shortens the exploration stay you choose. The trip does not change, and the stay's hydrogen, the delay risk and the gains remain those of the chosen duration.",
            "**Ark** has three effects on the Space Pioneer and colonisation. Colonisation speed stays under the fleet speed total cap (60%).",
            "A colony is **young** for 7 days after being founded by a Space Pioneer (never the home planet, a moon or a conquered world). Only **Pioneer Outposts** uses that state: **Young Worlds** only works with it. With both: 15 days of youth.",
            "An **abandoned target** is a ruined world, an opponent controlled by the game, or a player inactive in the universe. The base plunder rate is 50%; Derelict Raiders and Organised Plunder add points to that rate.",
            "**Stolen Archives** only counts plunders that bring back at least one hour of your home planet's production (the three resources added together). It advances the current study (the first one if two are running), never to completion; the 10 charges are counted over 24 hours from the first one.",
            "**Prospector's Nose**: 33% of the chance of finding nothing moves to resources. On a deep-space cell never explored before, \"nothing\" goes from 33% to 22.11%, \"resources\" from 33% to 43.89%.",
            "**Second Innovation Center**: the second study must differ from the first and only starts while a study is already running. At half speed, a 4 h study takes 8 h.",
        ],
        'logistics': [
            "Speed bonuses **divide** the flight duration: +40% = a flight 1.4 times shorter. They are read when the fleet leaves.",
            "Hydrogen reductions apply to the flight's fuel, not to an expedition stay's. Cargo adds to the capacity already raised by Hyperspace Technology.",
            "**Tailwind** speeds up every way home, recalls included. **Inner Lanes** speeds up transports and deployments arriving at one of your planets. Both multiply the speed on top of the speed cap.",
            "**Priority Loading**: when leaving, you set the order in which plunder and debris fill your holds when everything does not fit. Without it, each resource is loaded in proportion.",
        ],
    },
}

FULL = {
    'fr': {
        'prosperity': "Branche pleine : mines **+25 %**, bâtiments **+25 %**, vaisseaux et défenses **+10 %**, Maîtrise du Plasma comptée **une fois et demie**.",
        'exploration': f"Branche pleine : recherche **+15 %** et une seconde recherche, séjours d'expédition **25 %** plus courts, pillage des cibles abandonnées **70 %**, **+2 cases**, jeunes colonies plus rapides et jeunes jusqu'à **{YOUTH_NO_YW} jours** (**{YOUTH_MAX}** avec Jeunes mondes).",
        'logistics': "Branche pleine : vols **30 %** plus rapides et fret **+25 %** (option A en rangée 3), ou vols **40 %** plus rapides et fret **+15 %** (option B) ; hydrogène **−20 %** ; **+2** flottes ; Chargement prioritaire.",
    },
    'en': {
        'prosperity': "Full branch: mines **+25%**, buildings **+25%**, ships and defences **+10%**, Plasma Mastery counted **one and a half times**.",
        'exploration': f"Full branch: research **+15%** and a second study, expedition stays **25%** shorter, plunder of abandoned targets **70%**, **+2 fields**, young colonies faster and young for up to **{YOUTH_NO_YW} days** (**{YOUTH_MAX}** with Young Worlds).",
        'logistics': "Full branch: flights **30%** faster and cargo **+25%** (option A in row 3), or flights **40%** faster and cargo **+15%** (option B); hydrogen **−20%**; **+2** fleets; Priority Loading.",
    },
}


def branches_md(lang):
    out = []
    for key in ('prosperity', 'exploration', 'logistics'):
        notes = '\n'.join(f'- {x}' for x in NOTES[lang][key])
        out.append(f"## {branch_name(lang, key)}\n\n*{branch_motto(lang, key)}*\n\n{branch_table(lang, B[key])}\n\n{notes}\n\n{FULL[lang][key]}")
    return '\n\n'.join(out)


def builds(lang):
    fr = lang == 'fr'
    P = branch_name
    rows = [
        ['**Industriel**' if fr else '**Industrialist**', f"{P(lang,'prosperity')} 28, {P(lang,'exploration')} 22 ({'jusqu’à la rangée 8' if fr else 'down to row 8'})".replace('’', "'"),
         ("mines +25 %, bâtiments +25 %, vaisseaux +10 %, Plasma ×1,5 ; recherche +15 %, séjours 25 % plus courts, pillage des cibles abandonnées 60 %, +2 cases, jeunes colonies plus rapides" if fr
          else "mines +25%, buildings +25%, ships +10%, Plasma ×1.5; research +15%, stays 25% shorter, plunder of abandoned targets 60%, +2 fields, faster young colonies")],
        ['**Raideur**' if fr else '**Raider**', f"{P(lang,'logistics')} 28, {P(lang,'exploration')} 22",
         ("vols 30 à 40 % plus rapides, hydrogène −20 %, fret +15 à 25 %, +2 flottes ; recherche +15 %, séjours 25 % plus courts, pillage des cibles abandonnées 60 %" if fr
          else "flights 30 to 40% faster, hydrogen −20%, cargo +15 to 25%, +2 fleets; research +15%, stays 25% shorter, plunder of abandoned targets 60%")],
        ['**Savant**' if fr else '**Scholar**', f"{P(lang,'exploration')} 28, {P(lang,'prosperity')} 22",
         ("recherche +15 % et seconde recherche, séjours 25 % plus courts, pillage des cibles abandonnées 70 % ; mines +24 %, bâtiments +10 %, vaisseaux +10 %, Plasma ×1,5" if fr
          else "research +15% and a second study, stays 25% shorter, plunder of abandoned targets 70%; mines +24%, buildings +10%, ships +10%, Plasma ×1.5")],
        ['**Généraliste**' if fr else '**Generalist**', ("rangées 1 à 6 des trois branches (48 points) et 2 points en rangée 7" if fr else "rows 1 to 6 of the three branches (48 points) and 2 points in row 7"),
         ("mines +24 %, bâtiments +10 %, Plasma ×1,5 ; recherche +15 %, séjours 25 % plus courts, pillage des cibles abandonnées 60 %, +2 cases ; vols 15 à 25 % plus rapides, hydrogène −10 %, +1 flotte" if fr
          else "mines +24%, buildings +10%, Plasma ×1.5; research +15%, stays 25% shorter, plunder of abandoned targets 60%, +2 fields; flights 15 to 25% faster, hydrogen −10%, +1 fleet")],
    ]
    return table(['Build', 'Répartition', "Ce qu'il obtient"] if fr else ['Build', 'Split', 'What it gets'], rows)


def body(lang):
    fr = lang == 'fr'
    diagram = talent_diagrams.section_for('common', lang, 'common').rstrip('\n')
    N = lambda x: n(x, lang)
    if fr:
        head = f'''# L'arbre commun

> **En bref** : l'arbre commun est le même pour toutes les dynasties et toutes les classes. Il reçoit 1 point par niveau, {CMAX} au maximum, et règle votre propre vitesse de jeu : **Prospérité** pour produire et construire, **Exploration** pour chercher et s'étendre, **Logistique** pour vos flottes. {CMAX} points suffisent pour une branche pleine et l'essentiel d'une deuxième.
{{.is-info}}

{box(lang)}

## Règles

1. 3 branches de 10 rangées, {BRANCH} points par branche, {3 * BRANCH} au total. Vous en placez **{CMAX} au maximum**.
2. Un nœud ne s'ouvre que lorsque le nœud au-dessus de lui est plein. Les rangées s'ouvrent à {CG[4]}, {CG[7]} et {CG[9]} points placés au-dessus, toutes branches confondues : une branche seule contient {ROWS6} points dans ses rangées 1 à 6 et {ROWS8} dans ses rangées 1 à 8, il faut donc **{CG[7] - ROWS6} points ailleurs** avant sa rangée 7 et **{CG[9] - ROWS8}** avant sa rangée 9. L'ultime (rangée 10) demande en plus le niveau {ULT} et la branche pleine. Voir [Les talents](/fr/dynasty/talents).
3. Les rangées 3 et 6 sont des **choix** dans les trois branches : un point, option A ou B. La rangée 8 est un choix en Prospérité et en Exploration ; en Logistique, c'est une clé (Chargement prioritaire).
4. L'arbre commun **ne change pas** quand vous changez de classe.
5. Les bonus qui ne servent que vous (production, recherche, construction) montent haut. Ceux qui touchent les autres joueurs (vitesse de flotte, pillage) restent modérés.
6. Les bonus de vitesse de flotte **divisent la durée du vol** : +50 % = un vol 1,5 fois plus court.'''
        example = f'''## Exemple chiffré

**Prospérité pleine, Maîtrise du Plasma niveau {PLASMA}**
- Une mine de métal qui produit {N(MINE)} par heure (production brute) gagne +25 % de talents, soit {N(MINE * 0.25)}.
- Le Plasma {PLASMA} donne +{PLASMA} % ; avec Fonderie à plasma, il compte pour {N(PLASMA * 1.5)} niveaux : +{N(PLASMA * 1.5)} %, soit {N(MINE * PLASMA * 1.5 / 100)}.
- Total : **{N(MINE_FULL)}** par heure (sans Fonderie : {N(MINE_NOFOUNDRY)}), avant le rapport d'énergie. Avec La rotation Halden : {N(MINE_FULL + MINE * 0.02)}.
- Un bâtiment de 8 h se construit en 8 / 1,25 = **{hms(BUILD8, lang)}**.

**Exploration jusqu'à Astrométrie**
- Une recherche de 10 h se termine en 10 / 1,15 = **{hms(RESEARCH10, lang)}**.
- Cosmologie Appliquée, 10 h avec Méthode pleine et Astrométrie : le plafond de 25 % s'applique, **{hms(RESEARCH10_ASTRO, lang)}**.
- Une expédition qui explore 4 h n'explore plus que **3 h** (Cartographes au rang 5). Le trajet ne change pas.

**Pillage d'un joueur inactif** (taux de pillage de base 50 %, voir [Pillage](/fr/combat/plunder))
- Il a {N(STOCK)} métal en stock : vous emportez {N(LOOT_BASE)} sans talent, **{N(LOOT_FULL)}** avec Pillards d'abandonnés et Pillage organisé pleins (+20 points), dans la limite de vos soutes.

**Logistique pleine, option B**
- Un vol de 1 h dure 60 / 1,4 = **{hms(FLIGHT_B, lang)}**. Avec Vent arrière au lieu de Liaisons internes, le retour dure {hms(FLIGHT_B, lang)} / 1,25 = **{hms(RETURN_TAIL, lang)}**.
- Un vol qui brûle 10 000 hydrogène n'en brûle plus que **{N(FUEL)}**.
- Un Cargo stellaire de 25 000 de fret emporte 25 000 × 1,15 = **{N(CARGO)}** ressources (sans la Technologie hyperespace).'''
        pit = f'''## Pièges fréquents

- **Lire « +40 % de vitesse » comme un vol 40 % plus court** : la vitesse divise la durée. Un vol de 1 h passe à {hms(FLIGHT_B, lang)}, pas à 36 min.
- **Prendre Jeunes mondes seul** : sans Comptoirs pionniers, une colonie jeune n'a aucun bonus, et la prolonger ne sert à rien.
- **Additionner Méthode et Astrométrie** : les deux tiennent dans le même plafond de 25 %.
- **Cartographes et les gains** : le talent raccourcit l'exploration, mais l'expédition rapporte comme si elle avait exploré la durée choisie.
- **Pillards d'abandonnés contre un joueur actif** : le bonus ne joue que contre les joueurs inactifs, les mondes en ruine et les adversaires contrôlés par le jeu.
- **Archives volées et les petits pillages** : un pillage qui rapporte moins d'une heure de production de votre planète mère ne compte pas.
- **Deux ultimes** : deux branches pleines demandent {2 * BRANCH} points, au-delà des {CMAX} du budget.

## Pages liées

- [Les talents](/fr/dynasty/talents)
- [Les classes](/fr/dynasty/classes)
- [Déplacements](/fr/fleet/movement)
- [Expéditions](/fr/fleet/expeditions)
- [Pillage](/fr/combat/plunder)
- [Coloniser](/fr/universe/colonization)
- [Le stockage](/fr/economy/storage)'''
        data = f'''## Données détaillées

{diagram}

### Ce que {CMAX} points achètent

Aucun build ne prend tout : chacun choisit où va sa vitesse. Les quatre répartitions ci-dessous respectent les portes.

{builds(lang)}

Les plafonds de chaque bonus, avec les talents d'alliance, sont sur la page [Les talents](/fr/dynasty/talents#plafonds-des-bonus-partagés).'''
    else:
        head = f'''# The common tree

> **In short**: the common tree is the same for every dynasty and every class. It gets 1 point per level, {CMAX} at most, and sets your own pace: **Prosperity** to produce and build, **Exploration** to research and expand, **Logistics** for your fleets. {CMAX} points are enough for a full branch and most of a second one.
{{.is-info}}

{WARN_EN}
{box(lang)}

## Rules

1. 3 branches of 10 rows, {BRANCH} points per branch, {3 * BRANCH} in total. You place **{CMAX} at most**.
2. A node only opens once the node above it is full. Rows open at {CG[4]}, {CG[7]} and {CG[9]} points placed above, every branch together: a branch alone holds {ROWS6} points in its rows 1 to 6 and {ROWS8} in its rows 1 to 8, so you need **{CG[7] - ROWS6} points elsewhere** before its row 7 and **{CG[9] - ROWS8}** before its row 9. The ultimate (row 10) also requires level {ULT} and the full branch. See [Talents](/en/dynasty/talents).
3. Rows 3 and 6 are **choices** in all three branches: one point, option A or B. Row 8 is a choice in Prosperity and Exploration; in Logistics, it is a key (Priority Loading).
4. The common tree **does not change** when you change class.
5. Bonuses that only serve you (production, research, construction) go high. Those that affect other players (fleet speed, plunder) stay moderate.
6. Fleet speed bonuses **divide the flight duration**: +50% = a flight 1.5 times shorter.'''
        example = f'''## Worked example

**Full Prosperity, Plasma Mastery level {PLASMA}**
- A metal mine producing {N(MINE)} per hour (raw production) gains +25% from talents, that is {N(MINE * 0.25)}.
- Plasma {PLASMA} gives +{PLASMA}%; with Plasma Foundry, it counts as {N(PLASMA * 1.5)} levels: +{N(PLASMA * 1.5)}%, that is {N(MINE * PLASMA * 1.5 / 100)}.
- Total: **{N(MINE_FULL)}** per hour (without the Foundry: {N(MINE_NOFOUNDRY)}), before the energy ratio. With The Halden Rotation: {N(MINE_FULL + MINE * 0.02)}.
- An 8 h building is built in 8 / 1.25 = **{hms(BUILD8, lang)}**.

**Exploration down to Astrometry**
- A 10 h study completes in 10 / 1.15 = **{hms(RESEARCH10, lang)}**.
- Applied Cosmology, 10 h with full Method and Astrometry: the 25% cap applies, **{hms(RESEARCH10_ASTRO, lang)}**.
- An expedition exploring for 4 h now only explores for **3 h** (Cartographers at rank 5). The trip does not change.

**Plundering an inactive player** (base plunder rate 50%, see [Plunder](/en/combat/plunder))
- They have {N(STOCK)} metal in stock: you take {N(LOOT_BASE)} without talents, **{N(LOOT_FULL)}** with full Derelict Raiders and Organised Plunder (+20 points), within your holds' limit.

**Full Logistics, option B**
- A 1 h flight takes 60 / 1.4 = **{hms(FLIGHT_B, lang)}**. With Tailwind instead of Inner Lanes, the way home takes {hms(FLIGHT_B, lang)} / 1.25 = **{hms(RETURN_TAIL, lang)}**.
- A flight burning 10,000 hydrogen only burns **{N(FUEL)}**.
- A Stellar Freighter with 25,000 cargo carries 25,000 × 1.15 = **{N(CARGO)}** resources (without Hyperspace Technology).'''
        pit = f'''## Common pitfalls

- **Reading "+40% speed" as a flight 40% shorter**: speed divides the duration. A 1 h flight becomes {hms(FLIGHT_B, lang)}, not 36 min.
- **Taking Young Worlds alone**: without Pioneer Outposts, a young colony has no bonus, and extending it does nothing.
- **Adding up Method and Astrometry**: both fit within the same 25% cap.
- **Cartographers and the gains**: the talent shortens the exploration, but the expedition brings back as if it had explored for the chosen duration.
- **Derelict Raiders against an active player**: the bonus only works against inactive players, ruined worlds and opponents controlled by the game.
- **Stolen Archives and small plunders**: a plunder bringing back less than one hour of your home planet's production does not count.
- **Two ultimates**: two full branches require {2 * BRANCH} points, beyond the {CMAX} of the budget.

## Related pages

- [Talents](/en/dynasty/talents)
- [The classes](/en/dynasty/classes)
- [Movement](/en/fleet/movement)
- [Expeditions](/en/fleet/expeditions)
- [Plunder](/en/combat/plunder)
- [Colonisation](/en/universe/colonization)
- [Storage](/en/economy/storage)'''
        data = f'''## Detailed data

{diagram}

### What {CMAX} points buy

No build takes everything: each one chooses where its speed goes. The four splits below respect the gates.

{builds(lang)}

The caps of each bonus, with alliance talents, are on the [Talents](/en/dynasty/talents#caps-of-the-shared-bonuses) page.'''
    return '\n\n'.join([head, branches_md(lang), example, data, pit]) + '\n'


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'dynasty/common-tree', body(lang))
