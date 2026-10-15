"""Les dix pages dynasty/classes/<classe>, FR et EN, d'après le code (DONNEES §18).

Tableaux des branches, plafonds de la classe et diagramme : générés depuis l'export du code.
Textes propres à chaque classe (en bref, règles, exemples, builds, pièges) : classes_text.py, vérifiés sur le code.

Usage : python3 tools/dynasty_pages/p_classes.py [classe ...]   puis   python3 tools/talent_diagrams.py
"""
import sys
from pathlib import Path

from dyn_lib import DATA, RULES, CLASSES, LABELS, tree, branch_name, branch_motto, branch_table, class_caps_table, class_label, clean
from write import write
from classes_text import PROSE
from p_core import ARTICLE, dyn_name

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import talent_diagrams  # noqa: E402

WARN_EN = '''> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}
'''
BRANCH_K = sum(int(v) for v in RULES['CLASS_ROW_RANKS'].values())
KMAX = RULES['CLASS_MAX_POINTS']
ROWS6 = sum(int(RULES['CLASS_ROW_RANKS'][str(r)]) for r in range(1, 7))


def generic_rules(lang, c):
    d = DATA['classes'][c]['exclusive_to']
    names = [branch_name(lang, b['key']) for b in tree(c)]
    fr = lang == 'fr'
    if fr:
        who = (f"{ARTICLE[lang][c]} est une classe **commune** : toutes les dynasties peuvent la prendre." if d is None
               else f"{ARTICLE[lang][c]} est une classe **exclusive à [{dyn_name(lang, d)}](/fr/dynasty/dynasties)** : seuls les joueurs de cette dynastie peuvent la prendre.")
        return [who,
                f"Son arbre compte **trois branches** : {names[0]}, {names[1]} et {names[2]}.",
                f"Chaque branche a 9 rangées et coûte {BRANCH_K} points. Avec {KMAX} points au maximum, vous complétez une branche et son ultime, plus une seconde branche jusqu'à la rangée 6 ({ROWS6} points). Le fonctionnement des points, des portes et des choix est décrit sur [Les talents](/fr/dynasty/talents)."]
    who = (f"{ARTICLE[lang][c]} is a **common** class: every dynasty can take it." if d is None
           else f"{ARTICLE[lang][c]} is a class **exclusive to [{dyn_name(lang, d)}](/en/dynasty/dynasties)**: only players of that dynasty can take it.")
    return [who,
            f"Its tree has **three branches**: {names[0]}, {names[1]} and {names[2]}.",
            f"Each branch has 9 rows and costs {BRANCH_K} points. With {KMAX} points at most, you complete one branch and its ultimate, plus a second branch down to row 6 ({ROWS6} points). How points, gates and choices work is described on [Talents](/en/dynasty/talents)."]


def body(lang, c):
    P = PROSE[c][lang]
    fr = lang == 'fr'
    rules = generic_rules(lang, c) + P['rules']
    rules_md = '\n'.join(f'{i}. {r}' for i, r in enumerate(rules, 1))
    branches = []
    for b in tree(c):
        note = P.get('branch_notes', {}).get(b['key'], '')
        branches.append(f"### {branch_name(lang, b['key'])}\n\n*{branch_motto(lang, b['key'])}*\n\n{branch_table(lang, b)}" + (f'\n\n{note}' if note else ''))
    diagram = talent_diagrams.section_for(c, lang, 'class').rstrip('\n')
    caps_title = '### Plafonds de la classe' if fr else '### Class caps'
    caps_intro = ("Ce que les talents des deux arbres peuvent apporter au plus à cette classe, levier par levier. Au-delà, un point n'ajoute rien. Le trait de dynastie s'ajoute ensuite."
                  if fr else "The most the talents of both trees can bring this class, lever by lever. Past it, a point adds nothing. The dynasty trait then adds on top.")
    caps_extra = ('\n\n' + P['caps_note']) if P.get('caps_note') else ''
    builds_title = '### Builds à 25 points' if fr else '### 25-point builds'
    head = f"# {ARTICLE[lang][c]}\n\n> **{'En bref' if fr else 'In short'}** : {P['brief']}\n{{.is-info}}\n" if fr else \
        f"# {ARTICLE[lang][c]}\n\n> **In short**: {P['brief']}\n{{.is-info}}\n"
    if not fr and P.get('warn_en', True):
        head += '\n' + WARN_EN
    parts = [head,
             ('## Règles' if fr else '## Rules') + '\n\n' + rules_md,
             ('## Exemple chiffré' if fr else '## Worked example') + '\n\n' + P['example'].strip(),
             ('## Données détaillées' if fr else '## Detailed data') + '\n\n' + diagram,
             '\n\n'.join(branches),
             f'{caps_title}\n\n{caps_intro}\n\n{class_caps_table(lang, c)}{caps_extra}',
             f"{builds_title}\n\n{P['builds'].strip()}",
             ('## Pièges fréquents' if fr else '## Common pitfalls') + '\n\n' + '\n'.join(f'- {x}' for x in P['pitfalls']),
             ('## Pages liées' if fr else '## Related pages') + '\n\n' + '\n'.join(f'- {x}' for x in P['related'])]
    return '\n\n'.join(p.strip('\n') for p in parts) + '\n'


if __name__ == '__main__':
    todo = sys.argv[1:] or CLASSES
    for c in todo:
        for lang in ('fr', 'en'):
            write(lang, f'dynasty/classes/{c}', body(lang, c))
