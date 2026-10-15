"""Génère l'annexe « bâtiments niveau par niveau » (pages/<langue>/economy/building-levels.md).

Pour chaque bâtiment : coût de chaque niveau, énergie consommée ou produite, production, jusqu'au niveau maximal
(50 au plus). Données et formules relevées dans le code du jeu (DONNEES.md §4, « Relevé dans le code », 15 octobre 2026) :
- coût du niveau N = coût du niveau 1 × facteur^(N − 1), arrondi à l'inférieur par ressource (`Building::getCost()`) ;
- énergie requise : même règle avec `getEnergyMultiplicator()` (le facteur du coût, 2,5 pour la Station de réparation) ;
- production et consommation : `Building::getProduction()`, arrondies vers zéro ; stockage : `Building::getStorage()`.

Si l'équipe rééquilibre un bâtiment, corriger CATALOG puis relancer. Le script remplace le corps de la page et garde
son front matter (wiki_id, dates).
Usage : python3 tools/building_tables.py [--check]
"""
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'pages'
MAX_LEVEL = 50

# code: (coût niv. 1 métal, cristal, hydrogène), facteur, niveau max (None = aucun), énergie requise niv. 1, multiplicateur
CATALOG = {
    'metal_mine': ((60, 15, 0), 1.5, 50, 0, None),
    'crystal_mine': ((48, 24, 0), 1.6, 50, 0, None),
    'hydrogen_synthesizer': ((225, 75, 0), 1.5, 50, 0, None),
    'solar_plant': ((75, 30, 0), 1.5, 50, 0, None),
    'fusion_plant': ((900, 360, 180), 1.8, 50, 0, None),
    'metal_storage': ((1000, 0, 0), 2, 20, 0, None),
    'crystal_storage': ((1000, 500, 0), 2, 20, 0, None),
    'hydrogen_storage': ((1000, 1000, 0), 2, 20, 0, None),
    'research_lab': ((200, 400, 200), 2, 12, 0, None),
    'robotic_factory': ((400, 120, 200), 2, 10, 0, None),
    'shipyard': ((400, 200, 100), 2, 12, 0, None),
    'nanite_factory': ((1000000, 500000, 100000), 2, 10, 0, None),
    'repair_dock': ((200, 0, 50), 5, 10, 50, 2.5),
    'terraformer': ((0, 50000, 100000), 2, 10, 1000, 2),
    'missile_silo': ((20000, 20000, 1000), 2, 10, 0, None),
    'logistics_center': ((20000, 40000, 0), 2, 10, 0, None),
    'lunar_base': ((20000, 40000, 20000), 2, None, 0, None),
    'sensor_phalanx': ((20000, 40000, 20000), 2, None, 0, None),
    'jump_gate': ((2000000, 4000000, 2000000), 2, None, 0, None),
}

NAMES = {
    'metal_mine': ('Excavateur minéral', 'Mineral Excavator'),
    'crystal_mine': ('Extracteur cristallin', 'Crystal Extractor'),
    'hydrogen_synthesizer': ("Condensateur d'hydrogène", 'Hydrogen Condenser'),
    'solar_plant': ('Capteurs photovoltaïques', 'Photovoltaic Sensors'),
    'fusion_plant': ('Réacteur thermonucléaire', 'Thermonuclear Reactor'),
    'metal_storage': ("Dépôt d'alliages", 'Alloy Depot'),
    'crystal_storage': ('Chambre cristalline', 'Crystal Chamber'),
    'hydrogen_storage': ("Citerne d'hydrogène", 'Hydrogen Tank'),
    'research_lab': ("Centre d'innovation", 'Innovation Center'),
    'robotic_factory': ("Fabrique d'automates", 'Automaton Factory'),
    'shipyard': ('Dock orbital', 'Orbital Dock'),
    'nanite_factory': ('Assembleur moléculaire', 'Molecular Assembler'),
    'repair_dock': ('Station de réparation', 'Repair Station'),
    'terraformer': ('Modulateur planétaire', 'Planetary Modulator'),
    'missile_silo': ('Arsenal balistique', 'Ballistic Arsenal'),
    'logistics_center': ('Centre logistique', 'Logistics Center'),
    'lunar_base': ('Base lunaire', 'Lunar base'),
    'sensor_phalanx': ('Phalange de capteur', 'Sensor phalanx'),
    'jump_gate': ('Porte de saut', 'Jump gate'),
}

SECTIONS = {  # regroupement des bâtiments dans la page
    'fr': [('Production', ['metal_mine', 'crystal_mine', 'hydrogen_synthesizer']),
           ('Énergie', ['solar_plant', 'fusion_plant']),
           ('Stockage', ['metal_storage', 'crystal_storage', 'hydrogen_storage', 'logistics_center']),
           ('Installations', ['research_lab', 'robotic_factory', 'shipyard', 'nanite_factory', 'repair_dock',
                              'terraformer', 'missile_silo']),
           ('Bâtiments lunaires', ['lunar_base', 'sensor_phalanx', 'jump_gate'])],
    'en': [('Production', ['metal_mine', 'crystal_mine', 'hydrogen_synthesizer']),
           ('Energy', ['solar_plant', 'fusion_plant']),
           ('Storage', ['metal_storage', 'crystal_storage', 'hydrogen_storage', 'logistics_center']),
           ('Facilities', ['research_lab', 'robotic_factory', 'shipyard', 'nanite_factory', 'repair_dock',
                           'terraformer', 'missile_silo']),
           ('Moon buildings', ['lunar_base', 'sensor_phalanx', 'jump_gate'])],
}

FUSION_SE = (5, 10, 15)  # niveaux de Science Énergétique montrés pour le Réacteur


def fmt(value, locale):
    text = f'{int(value):,}'
    return text.replace(',', ' ') if locale == 'fr' else text


def cost(code, level):
    (m, c, h), factor, _, energy, mult = CATALOG[code]
    k = factor ** (level - 1)
    e = math.floor(energy * (mult or factor) ** (level - 1)) if energy else 0
    return math.floor(m * k), math.floor(c * k), math.floor(h * k), e


def levels(code):
    return range(1, min(CATALOG[code][2] or MAX_LEVEL, MAX_LEVEL) + 1)


def g(n):
    return n * 1.1 ** n


def table(code, locale):
    fr = locale == 'fr'
    (m1, c1, h1), _, _, e1, _ = CATALOG[code]
    head = ['Niveau' if fr else 'Level'] + [label for label, base in
                                             (('Métal' if fr else 'Metal', m1), ('Cristal' if fr else 'Crystal', c1),
                                              ('Hydrogène' if fr else 'Hydrogen', h1)) if base]
    if e1:
        head.append('Énergie requise' if fr else 'Energy required')
    extra = {
        'metal_mine': [('Métal / h' if fr else 'Metal / h', lambda n: 30 * g(n)),
                       ('Énergie consommée' if fr else 'Energy used', lambda n: 10 * g(n))],
        'crystal_mine': [('Cristal / h' if fr else 'Crystal / h', lambda n: 20 * g(n)),
                         ('Énergie consommée' if fr else 'Energy used', lambda n: 10 * g(n))],
        'hydrogen_synthesizer': [('Hydrogène / h, base' if fr else 'Hydrogen / h, base', lambda n: 10 * g(n)),
                                 ('Énergie consommée' if fr else 'Energy used', lambda n: 10 * g(n))],
        'solar_plant': [('Énergie produite, base' if fr else 'Energy produced, base', lambda n: 20 * g(n))],
        'fusion_plant': [(f'Énergie (Sc. Én. {se})' if fr else f'Energy (En. Sc. {se})',
                          lambda n, se=se: 30 * n * (1.05 + 0.01 * se) ** n) for se in FUSION_SE]
        + [('Hydrogène consommé / h' if fr else 'Hydrogen used / h', lambda n: 10 * g(n))],
        'metal_storage': [('Capacité' if fr else 'Capacity', lambda n: 5000 * math.floor(2.5 * math.exp(20 * n / 33)))],
        'logistics_center': [('Stockage' if fr else 'Storage', lambda n: f'+{10 * n} %' if fr else f'+{10 * n}%')],
        'research_lab': [('Durée des recherches' if fr else 'Research time', lambda n: f'÷ {n + 1}')],
        'robotic_factory': [('Durée des bâtiments' if fr else 'Building time', lambda n: f'÷ {n + 1}')],
        'nanite_factory': [('Durée des bâtiments' if fr else 'Building time', lambda n: f'÷ {fmt(2 ** n, locale)}')],
        'terraformer': [('Cases en plus (total)' if fr else 'Extra fields (total)', lambda n: f'+{5 * n + n // 2}')],
        'lunar_base': [('Cases (plafond : diamètre)' if fr else 'Fields (capped by diameter)', lambda n: 3 * n)],
    }
    extra['crystal_storage'] = extra['hydrogen_storage'] = extra['metal_storage']
    columns = extra.get(code, [])
    lines = ['| ' + ' | '.join(head + [c[0] for c in columns]) + ' |', '|' + '---|' * (len(head) + len(columns))]
    for n in levels(code):
        m, c, h, e = cost(code, n)
        row = [str(n)] + [fmt(v, locale) for v, base in ((m, m1), (c, c1), (h, h1)) if base]
        if e1:
            row.append(fmt(e, locale))
        for _, f in columns:
            v = f(n)
            row.append(v if isinstance(v, str) else fmt(math.trunc(v), locale))
        lines.append('| ' + ' | '.join(row) + ' |')
    return '\n'.join(lines)


NOTES = {
    'fr': {
        'hydrogen_synthesizer': "Production de base : à multiplier par le facteur de température (1,44 − 0,004 × température maximale), par exemple ×1,28 à 40 °C ou ×1,56 à −30 °C.",
        'solar_plant': "Production de base, valable quand la température actuelle est nulle ou négative ; au-dessus, multipliez par (1 + température actuelle / 100), par exemple ×1,23 à 23 °C.",
        'fusion_plant': "La production dépend du niveau de Science Énergétique ; trois niveaux sont montrés. Le Réacteur demande Condensateur d'hydrogène 5 et Science Énergétique 3.",
        'metal_storage': "Capacité du bâtiment seul, avant les 10 000 par niveau de Base planetaire et le bonus du Centre logistique.",
        'logistics_center': "Le bonus s'ajoute à ceux des talents et s'applique à toute la capacité de stockage de la base, Base planetaire comprise.",
        'research_lab': "Durée de base des recherches, hors réseau de laboratoires (Collaboration Stellaire).",
        'robotic_factory': "Se combine avec l'Assembleur moléculaire : la durée est divisée par (1 + niveau de la Fabrique) × 2^niveau de l'Assembleur.",
        'nanite_factory': "Se combine avec la Fabrique d'automates : la durée est divisée par (1 + niveau de la Fabrique) × 2^niveau de l'Assembleur.",
        'terraformer': "5 cases par niveau, plus une case tous les deux niveaux (total cumulé). L'énergie requise est un seuil à atteindre pour construire le niveau, elle n'est pas consommée.",
        'lunar_base': "3 cases par niveau, sans dépasser ce que permet le diamètre de la lune.",
        'repair_dock': "L'énergie requise est un seuil à atteindre pour construire le niveau ; la Station n'en consomme pas en fonctionnement.",
    },
    'en': {
        'hydrogen_synthesizer': 'Base output: multiply by the temperature factor (1.44 − 0.004 × maximum temperature), e.g. ×1.28 at 40 °C or ×1.56 at −30 °C.',
        'solar_plant': 'Base output, valid when the current temperature is zero or below; above that, multiply by (1 + current temperature / 100), e.g. ×1.23 at 23 °C.',
        'fusion_plant': 'Output depends on the Energy Science level; three levels are shown. The Reactor requires Hydrogen Condenser 5 and Energy Science 3.',
        'metal_storage': 'Capacity of the building alone, before the 10,000 per Planetary Base level and the Logistics Center bonus.',
        'logistics_center': "The bonus adds up with talent bonuses and applies to the base's whole storage capacity, Planetary Base included.",
        'research_lab': 'Base research time, without the laboratory network (Stellar Collaboration).',
        'robotic_factory': 'Combines with the Molecular Assembler: time is divided by (1 + Factory level) × 2^Assembler level.',
        'nanite_factory': 'Combines with the Automaton Factory: time is divided by (1 + Factory level) × 2^Assembler level.',
        'terraformer': '5 fields per level, plus one field every two levels (running total). The energy required is a threshold to build the level, it is not used up.',
        'lunar_base': "3 fields per level, never beyond what the moon's diameter allows.",
        'repair_dock': 'The energy required is a threshold to build the level; the Station uses none while running.',
    },
}
for _l in NOTES:
    NOTES[_l]['crystal_storage'] = NOTES[_l]['hydrogen_storage'] = NOTES[_l]['metal_storage']


def example(locale):
    """Exemple chiffré : passer l'Excavateur minéral du niveau 20 au niveau 21."""
    m, c, _, _ = cost('metal_mine', 21)
    gain = math.trunc(30 * g(21)) - math.trunc(30 * g(20))
    energy = math.trunc(10 * g(21)) - math.trunc(10 * g(20))
    f = lambda v: fmt(v, locale)
    if locale == 'fr':
        return (f"**Excavateur minéral, du niveau 20 au niveau 21** (Redline, vitesse ×1)\n"
                f"- Coût du niveau 21 : 60 × 1,5^20 = **{f(m)}** métal et 15 × 1,5^20 = **{f(c)}** cristal.\n"
                f"- Production : de {f(math.trunc(30 * g(20)))} à {f(math.trunc(30 * g(21)))} métal par heure, soit **+{f(gain)}**.\n"
                f"- Énergie : **{f(energy)}** de plus à fournir, de {f(math.trunc(10 * g(20)))} à {f(math.trunc(10 * g(21)))}.\n"
                f"- Le niveau est amorti en {f(m // gain)} heures environ de la seule production ajoutée, sans compter le cristal ni l'énergie.")
    return (f"**Mineral Excavator, from level 20 to level 21** (Redline, speed ×1)\n"
            f"- Level 21 cost: 60 × 1.5^20 = **{f(m)}** metal and 15 × 1.5^20 = **{f(c)}** crystal.\n"
            f"- Output: from {f(math.trunc(30 * g(20)))} to {f(math.trunc(30 * g(21)))} metal per hour, so **+{f(gain)}**.\n"
            f"- Energy: **{f(energy)}** more to supply, from {f(math.trunc(10 * g(20)))} to {f(math.trunc(10 * g(21)))}.\n"
            f"- The level pays for itself in about {f(m // gain)} hours of the added output alone, leaving out crystal and energy.")


TEXT = {
    'fr': {
        'title': 'Annexe : les bâtiments niveau par niveau',
        'brief': "> **En bref** : pour chaque bâtiment, le coût de chaque niveau, l'énergie qu'il consomme ou produit et sa production, jusqu'à son niveau maximal (50 au plus). La durée de construction n'est pas indiquée : elle dépend trop de la Fabrique d'automates, de l'Assembleur moléculaire, de la vitesse de l'univers et des talents.\n{.is-info}",
        'universe': "> **Paramètre d'univers** : la production est multipliée par la vitesse d'économie de l'univers ; la consommation d'énergie ne l'est pas.\n> Par défaut : **×1** · Redline : **×1**\n{.is-info}",
        'rules': ["Le coût du niveau N vaut le coût du niveau 1 multiplié par le **facteur** du bâtiment, N − 1 fois, arrondi à l'inférieur pour chaque ressource.",
                  "La **production** est donnée à la vitesse ×1, avant les bonus (bonus de position des colonies, Maîtrise du Plasma, talents) et avant un éventuel déficit d'énergie.",
                  "L'**énergie consommée** par une mine ne dépend pas de la vitesse de l'univers. Si la production d'énergie ne suffit pas, les trois mines ralentissent dans la même proportion (voir [L'énergie](/fr/economy/energy)).",
                  "Un bâtiment sans niveau maximal est montré jusqu'au niveau 50.",
                  "Chaque niveau rapporte des **points** : 1 point par 1 000 ressources de son coût (métal + cristal + hydrogène)."],
        'example': '## Exemple chiffré', 'rules_h': '## Règles', 'data': '## Données détaillées',
        'factor': 'Facteur {f}, niveau maximal {m}.', 'nomax': 'Facteur {f}, pas de niveau maximal.',
        'related': "## Pages liées\n\n- [Liste des bâtiments](/fr/economy/buildings)\n- [Les ressources](/fr/economy/resources)\n- [L'énergie](/fr/economy/energy)\n- [Le stockage](/fr/economy/storage)\n- [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)",
        'description': "Coût, énergie et production de chaque bâtiment, niveau par niveau.",
    },
    'en': {
        'title': 'Appendix: buildings level by level',
        'brief': "> **In short**: for each building, the cost of every level, the energy it uses or produces and its output, up to its maximum level (50 at most). Build time is not shown: it depends too much on the Automaton Factory, the Molecular Assembler, the universe speed and talents.\n{.is-info}",
        'universe': '> **Universe setting**: output is multiplied by the universe economy speed; energy use is not.\n> Default: **×1** · Redline: **×1**\n{.is-info}',
        'rules': ["The cost of level N is the level 1 cost multiplied by the building's **factor**, N − 1 times, rounded down for each resource.",
                  'The **output** is given at speed ×1, before bonuses (colony position bonus, Plasma Technology, talents) and before any energy shortage.',
                  'The **energy used** by a mine does not depend on the universe speed. If energy output falls short, all three mines slow down in the same proportion (see [Energy](/en/economy/energy)).',
                  'A building with no maximum level is shown up to level 50.',
                  'Each level is worth **points**: 1 point per 1,000 resources of its cost (metal + crystal + hydrogen).'],
        'example': '## Worked example', 'rules_h': '## Rules', 'data': '## Detailed data',
        'factor': 'Factor {f}, maximum level {m}.', 'nomax': 'Factor {f}, no maximum level.',
        'related': '## Related pages\n\n- [Buildings list](/en/economy/buildings)\n- [Resources](/en/economy/resources)\n- [Energy](/en/economy/energy)\n- [Storage](/en/economy/storage)\n- [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)',
        'description': 'Cost, energy and output of every building, level by level.',
    },
}


def body(locale):
    t = TEXT[locale]
    out = [f'# {t["title"]}', '', t['brief'], '', t['universe'], '', t['rules_h'], '']
    out += [f'{i}. {r}' for i, r in enumerate(t['rules'], 1)]
    out += ['', t['example'], '', example(locale), '', t['data'], '']
    for section, codes in SECTIONS[locale]:
        out += [f'### {section}', '']
        for code in codes:
            name = NAMES[code][0 if locale == 'fr' else 1]
            _, factor, maxi, _, _ = CATALOG[code]
            f = str(factor).replace('.', ',') if locale == 'fr' else str(factor)
            out += [f'#### {name}', '', (t['factor'].format(f=f, m=maxi) if maxi else t['nomax'].format(f=f))
                    + (' ' + NOTES[locale][code] if code in NOTES[locale] else ''), '', table(code, locale), '']
    out += [t['related'], '']
    return '\n'.join(out)


def write(locale, check):
    path = ROOT / locale / 'economy' / 'building-levels.md'
    new = body(locale)
    if path.exists():
        head, old = path.read_text(encoding='utf-8').split('\n---\n\n', 1)
    else:
        t = TEXT[locale]
        meta = {'locale': locale, 'path': 'economy/building-levels',
                'url': f'https://wiki.dynastynova.com/{locale}/economy/building-levels', 'title': t['title'],
                'description': t['description'], 'tags': ['economy'], 'published': False}
        head, old = '---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in meta.items()), None
    if new != old and not check:
        path.write_text(head + '\n---\n\n' + new, encoding='utf-8')
    print(f'{"à régénérer" if check and new != old else "écrite" if new != old else "à jour"} {path.relative_to(ROOT)}')


if __name__ == '__main__':
    for loc in ('fr', 'en'):
        write(loc, '--check' in sys.argv)
