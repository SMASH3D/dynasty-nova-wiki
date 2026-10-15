"""Page research/tech-tree (FR et EN) : chemins complets et déblocages calculés depuis le catalogue."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_lib import *
from write import write, table

SHIP_ORDER = ['small_cargo', 'large_cargo', 'colony_ship', 'recycler', 'espionage_probe', 'solar_satellite',
              'light_fighter', 'heavy_fighter', 'cruiser', 'battleship', 'bomber', 'predator', 'destroyer', 'battle_cruiser']
DEF_ORDER = ['ballistic_projector', 'photonic_cannon', 'high_energy_emitter', 'magnetic_accelerator', 'ion_battery',
             'plasma_ejector', 'defensive_barrier', 'protective_dome', 'interceptors', 'long_range_warheads']
RES_ORDER = [c for _, codes in SECTIONS for c in codes]
BLD_WITH_REQ = [b[0] for b in BUILDINGS if b[3]]
ALL = [b[0] for b in BUILDINGS] + [r[0] for r in RESEARCH] + [s[0] for s in SHIPS] + [d[0] for d in DEFENSES]
UNIT_ORDER = [b[0] for b in BUILDINGS] + RES_ORDER + SHIP_ORDER + DEF_ORDER

def unlocks():
    """Débloque direct : {prérequis: [(niveau, élément)]}."""
    out = {}
    for code in ALL:
        for t, rc, lv in reqs_of(code):
            out.setdefault(rc, []).append((lv, code))
    return out

def fmt_unlocks(items, lang):
    by = {}
    for lv, code in items:
        by.setdefault(lv, []).append(code)
    parts = []
    for lv in sorted(by):
        names = ', '.join(nm(c, lang) for c in sorted(by[lv], key=UNIT_ORDER.index))
        parts.append(f'{names} ({lv})')
    return ' ; '.join(parts) if lang == 'fr' else '; '.join(parts)

def path_rows(codes, lang):
    return [[nm(c, lang), fmt_need(closure(c), lang)] for c in codes]

def mermaid(lang):
    """Prérequis entre technologies, avec le niveau de Centre d'innovation de chacune (Mermaid 8.8.2)."""
    ids = {c: f'R{i}' for i, c in enumerate(RES_ORDER)}
    lab = "Centre" if lang == 'fr' else 'Center'
    lines = ['```mermaid', 'graph TB']
    for c in RES_ORDER:
        lv = [l for t, rc, l in RES[c][6] if rc == 'research_lab'][0]
        lines.append(f'    {ids[c]}["{nm(c, lang)}<br/>{lab} {lv}"]')
    for c in RES_ORDER:
        for t, rc, lv in RES[c][6]:
            if t == 'r':
                lines.append(f'    {ids[rc]} -->|{lv}| {ids[c]}')
    lines.append('```')
    return '\n'.join(lines)

def body(lang):
    fr = lang == 'fr'
    U = unlocks()
    hdr_path = ['Objectif', "Tout ce qu'il faut atteindre"] if fr else ['Goal', 'Everything you need to reach']
    t_ships = table(hdr_path, path_rows(SHIP_ORDER, lang))
    t_defs = table(hdr_path, path_rows(DEF_ORDER, lang))
    t_blds = table(hdr_path, path_rows(BLD_WITH_REQ, lang))
    t_res = table(hdr_path, path_rows(RES_ORDER, lang))
    t_ub = table(['Bâtiment', 'Débloque (niveau requis)'] if fr else ['Building', 'Unlocks (level required)'],
                 [[nm(b[0], lang), fmt_unlocks(U[b[0]], lang)] for b in BUILDINGS if b[0] in U])
    t_ur = table(['Technologie', 'Débloque (niveau requis)'] if fr else ['Technology', 'Unlocks (level required)'],
                 [[nm(c, lang), fmt_unlocks(U[c], lang)] for c in RES_ORDER if c in U])
    pion = closure('colony_ship')
    pb = fmt_need({k: v for k, v in pion.items() if k in BLD}, lang)
    pr = fmt_need({k: v for k, v in pion.items() if k in RES}, lang)
    col = closure('battle_cruiser')
    lab12 = [c for c in RES_ORDER if [l for t, rc, l in RES[c][6] if rc == 'research_lab'][0] >= 10]
    no_unlock = [c for c in RES_ORDER if c not in U]
    if fr:
        return f'''# Arbre technologique

> **En bref** : la plupart des bâtiments, technologies, vaisseaux et défenses exigent d'avoir atteint certains niveaux ailleurs. Cette page donne, pour chaque élément, la liste complète de ce qu'il faut atteindre, puis ce que débloque chaque bâtiment et chaque technologie. Toutes les valeurs viennent du catalogue du jeu.
{{.is-info}}

## Règles

1. Un prérequis s'exprime en **niveau minimum** d'un bâtiment ou d'une technologie.
2. Tant qu'un prérequis manque, l'élément reste verrouillé dans le jeu.
3. Un prérequis de **bâtiment** se lit sur la planète (ou la lune) où l'on construit ou d'où l'on lance la recherche. Un prérequis de **technologie** vaut pour tout l'empire. Dans les chemins complets, le Centre d'innovation est celui de la planète qui lance chaque recherche : pour la Porte de saut, bâtie sur une lune, il se trouve sur l'une de vos planètes.
4. Les prérequis s'enchaînent : une technologie demandée a elle-même ses prérequis. Les tableaux de chemins donnent la **liste complète**, chaînes comprises, en gardant pour chaque élément le niveau le plus élevé demandé.
5. Les prérequis d'un **bâtiment** ne se vérifient qu'à son premier niveau sur une planète. Ceux d'une **technologie** se vérifient à chaque niveau, sur la planète qui la lance ; ceux d'un **vaisseau** ou d'une **défense**, à chaque commande.
6. Les bâtiments lunaires (Phalange de capteur, Porte de saut) demandent une Base lunaire sur la même lune.
7. **Mise en file** : un prérequis compte déjà s'il sera atteint par un ordre placé avant (un bâtiment de la même planète, une étude de l'empire). Il est vérifié de nouveau quand l'ordre démarre ; s'il manque alors, l'ordre est abandonné sans frais.

## Exemple chiffré

Pour construire votre premier **Pionnier spatial** et coloniser, il faut au total :
- Bâtiments, sur la planète qui le construit : {pb}.
- Technologies : {pr}.

Le Colossus stellaire, le vaisseau le plus exigeant, demande {len(col)} prérequis en tout, dont le Centre d'innovation et le Dock orbital au niveau 12, leur maximum.

## Données détaillées

### Prérequis entre technologies

Chaque flèche porte le niveau demandé ; sous chaque nom, le niveau de Centre d'innovation requis.

{mermaid(lang)}

### Chemins complets : vaisseaux

{t_ships}

### Chemins complets : défenses et missiles

{t_defs}

### Chemins complets : bâtiments

Seuls figurent les bâtiments qui ont des prérequis.

{t_blds}

### Chemins complets : technologies

{t_res}

### Ce que débloque chaque bâtiment

{t_ub}

### Ce que débloque chaque technologie

{t_ur}

{' et '.join(nm(c, lang) for c in no_unlock)} ne {'débloquent' if len(no_unlock) > 1 else 'débloque'} rien : {'leur' if len(no_unlock) > 1 else 'son'} intérêt tient à {'leur' if len(no_unlock) > 1 else 'son'} effet (voir [Liste des technologies](/fr/research/technologies)).

## Pièges fréquents

- **Renseignement Tactique mène à la colonisation** : son niveau 4 est requis pour la Cosmologie Appliquée, donc pour le Pionnier spatial.
- **Le Centre d'innovation est le vrai verrou** : {', '.join(nm(c, lang) for c in lab12)} demandent un Centre de niveau 10 ou plus sur la planète qui lance la recherche. Le niveau 12 est aussi le maximum du Centre.
- **Pliage Spatial ouvre la propulsion lourde** : sans Pliage Spatial 3, pas de Navigation Transdimensionnelle, donc pas de Cuirassé.
- **Calcul Quantique mène à l'alliance** : son niveau 4 est requis pour la Diplomatie Stellaire, elle-même requise pour fonder une alliance.
- **Le Dock orbital se monte sur chaque planète** : ses prérequis (Fabrique d'automates 2) et les niveaux de Dock demandés par les vaisseaux se lisent sur la planète qui construit.

## Pages liées

- [Liste des technologies](/fr/research/technologies)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Missiles](/fr/defense/missiles)
'''
    return f'''# Tech tree

> **In short**: most buildings, technologies, ships and defenses require certain levels elsewhere first. For each item, this page lists everything you need to reach, then what each building and technology unlocks. Every value comes from the game catalogue.
{{.is-info}}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{{.is-warning}}

## Rules

1. A requirement is a **minimum level** of a building or a technology.
2. Until a requirement is met, the item stays locked in the game.
3. A **building** requirement is read on the planet (or moon) where you build or start the research. A **technology** requirement applies to the whole empire. In the full paths, the Innovation Center is that of the planet starting each research: for the Jump gate, built on a moon, it stands on one of your planets.
4. Requirements chain: a required technology has its own requirements. The path tables give the **full list**, chains included, keeping the highest level asked for each item.
5. A **building**'s requirements are only checked for its first level on a planet. A **technology**'s are checked at every level, on the planet starting it; a **ship**'s or a **defense**'s, at every order.
6. Lunar buildings (Sensor phalanx, Jump gate) need a Lunar base on the same moon.
7. **Queueing**: a requirement already counts if an order placed earlier will reach it (a building on the same planet, a study anywhere in the empire). It is checked again when the order starts; if it is missing then, the order is dropped at no cost.

## Worked example

To build your first **Space Pioneer** and colonize, you need in total:
- Buildings, on the planet building it: {pb}.
- Technologies: {pr}.

The Stellar Colossus, the most demanding ship, has {len(col)} requirements in all, including the Innovation Center and the Orbital Dock at level 12, their maximum.

## Detailed data

### Requirements between technologies

Each arrow shows the level required; under each name, the Innovation Center level required.

{mermaid(lang)}

### Full paths: ships

{t_ships}

### Full paths: defenses and missiles

{t_defs}

### Full paths: buildings

Only buildings with requirements are listed.

{t_blds}

### Full paths: technologies

{t_res}

### What each building unlocks

{t_ub}

### What each technology unlocks

{t_ur}

{' and '.join(nm(c, lang) for c in no_unlock)} unlock{'' if len(no_unlock) > 1 else 's'} nothing: {'their' if len(no_unlock) > 1 else 'its'} value lies in {'their' if len(no_unlock) > 1 else 'its'} effect (see [Technologies list](/en/research/technologies)).

## Common pitfalls

- **Espionage Technology leads to colonization**: its level 4 is needed for Astrophysics, hence for the Space Pioneer.
- **The Innovation Center is the real lock**: {', '.join(nm(c, lang) for c in lab12)} need a level 10 Center or higher on the planet starting the research. Level 12 is also the Center's maximum.
- **Hyperspace Technology opens heavy propulsion**: without Hyperspace Technology 3, no Hyperspace Drive, hence no Battleship.
- **Quantum Computing leads to alliances**: its level 4 is needed for Stellar Diplomacy, itself needed to found an alliance.
- **The Orbital Dock is built on each planet**: its requirements (Automaton Factory 2) and the Dock levels ships ask for are read on the planet building them.

## Related pages

- [Technologies list](/en/research/technologies)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Buildings list](/en/economy/buildings)
- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
'''

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'research/tech-tree', body(lang))
