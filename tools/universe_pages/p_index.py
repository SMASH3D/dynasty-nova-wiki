import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

PAGES = [
    ('universes', 'Les univers', 'parties indépendantes, réglages, vitesses, arrivée dans un univers', 'Universes', 'separate games, settings, speeds, joining a universe'),
    ('coordinates', 'Coordonnées', 'galaxie, système, position, carte qui boucle, distances', 'Coordinates', 'galaxy, system, position, wrap-around map, distances'),
    ('galaxy-view', 'La vue galaxie', 'cases inexplorées, badges, espace lointain, Station stellaire', 'The galaxy view', 'unexplored cells, badges, deep space, Stellar Station'),
    ('planets', 'Planètes : taille, température, type', 'cases, température, bonus de position', 'Planets: size, temperature, type', 'fields, temperature, position bonus'),
    ('colonization', 'Coloniser', 'Pionnier spatial, Cosmologie Appliquée, planètes abandonnées', 'Colonization', 'Space Pioneer, Astrophysics, abandoned planets'),
    ('abandoning-a-planet', 'Abandonner une colonie', 'conditions, premier choc, dégradation', 'Abandoning a colony', 'conditions, first shock, decay'),
    ('moons', 'Les lunes', 'formation, diamètre, cases, Base lunaire', 'Moons', 'formation, diameter, fields, Lunar base'),
]


def body(lang):
    if lang == 'fr':
        items = '\n'.join(f'- [{t}](/fr/universe/{p}) : {d}' for p, t, d, _, _ in PAGES)
        return f'''# Univers et planètes

**Univers, coordonnées, planètes et lunes.**

## Pages de cette rubrique

{items}
'''
    items = '\n'.join(f'- [{t}](/en/universe/{p}): {d}' for p, _, _, t, d in PAGES)
    return f'''# Universe and planets

**Universes, coordinates, planets and moons.**

## Pages in this section

{items}
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe', body(lang))
