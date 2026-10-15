"""Génère le diagramme Mermaid de l'arbre de talents des pages de classe et de l'arbre commun, à partir du code du jeu.

La forme de chaque arbre vient de l'export du serveur (tools/dynasty_pages/talents.json) : rangées, rangs,
nœuds de choix, portes, ultime ; les noms viennent des textes du client (tools/dynasty_pages/labels.json).
Arbre de classe : 3 branches de 9 rangées, 15 points, choix en rangées 3 et 6, portes à 5 et 12 points.
Arbre commun : 3 branches de 10 rangées, 28 points, portes à 8, 20 et 32 points ; choix en rangées 3, 6 et 8
pour Prospérité et Exploration, en rangées 3 et 6 seulement pour Logistique (sa rangée 8 est une clé).
Le diagramme est inséré (ou remplacé) dans une section « Vue d'ensemble de l'arbre » placée en tête des
données détaillées. Le script vérifie aussi que les tableaux de chaque page nomment les nœuds du code, rangée par rangée.

Syntaxe compatible avec Mermaid 8.8.2, la version embarquée par Wiki.js 2 :
- `graph TB` et non `flowchart TB` (le moteur flowchart de cette version inverse les sous-graphes) ;
- pas de `direction` dans un `subgraph` (apparu en 8.12, provoque « Syntax error in graph »).

Usage : python3 tools/talent_diagrams.py [--check | --print fr/energist | --print fr/common-tree]   (--check : pages à régénérer, sans écrire ; --print : un seul diagramme)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / 'pages'
sys.path.insert(0, str(Path(__file__).resolve().parent / 'dynasty_pages'))
import dyn_lib  # noqa: E402  (export du code et textes du client)

TEXT = {
    'fr': {'detail': '## Données détaillées', 'title': "### Vue d'ensemble de l'arbre",
           'intro': "Les trois branches de l'arbre {tree}, de la rangée 1 à l'ultime. Le détail de chaque talent est dans les tableaux{where}.",
           'tree': {'class': 'de classe', 'common': 'commun'}, 'where': {'class': ' ci-dessous', 'common': ' de chaque branche'},
           'gate': "🔒 {n} points dans l'arbre", 'pt': '{n} pt', 'pts': '{n} pts', 'ultimate': 'ultime'},
    'en': {'detail': '## Detailed data', 'title': '### Tree at a glance',
           'intro': 'The three branches of the {tree}, from row 1 to the ultimate. Each talent is detailed in the{where} tables.',
           'tree': {'class': 'class tree', 'common': 'common tree'}, 'where': {'class': '', 'common': ' branch'},
           'gate': '🔒 {n} points in the tree', 'pt': '{n} pt', 'pts': '{n} pts', 'ultimate': 'ultimate'},
}



def shape_of(owner):
    """Forme d'un arbre lue dans le code : nombre de rangées, points par branche, rangées de choix par branche,
    portes (rangée après laquelle elle se place : points placés au-dessus)."""
    branches = dyn_lib.tree(owner)
    nodes = branches[0]['nodes']
    gates = {}
    for previous, node in zip(nodes, nodes[1:]):
        if node['gate'] > previous['gate']:
            gates[previous['row']] = node['gate']
    return {'rows': len(nodes), 'points': sum(x['ranks'] for x in nodes), 'gates': gates,
            'choices': [{x['row'] for x in b['nodes'] if x['type'] == 'choice'} for b in branches]}


def from_code(owner, locale):
    """[(titre, devise, [(rangée, [noms], points)])] pour chaque branche, de gauche à droite, d'après le code."""
    result = []
    for b in dyn_lib.tree(owner):
        rows = []
        for x in b['nodes']:
            names = [dyn_lib.node_name(locale, x['key'], o) for o in (1, 2)] if x['type'] == 'choice' else [dyn_lib.node_name(locale, x['key'])]
            rows.append((x['row'], [quote(nm) for nm in names], x['ranks']))
        result.append((dyn_lib.branch_name(locale, b['key']), dyn_lib.branch_motto(locale, b['key']), rows))
    return result


# Palette reprise de l'interface du jeu : fond bleu nuit, or pour les clés et les portes, bleu pour les rangs.
# Ces couleurs suffisent à un rendu correct ; la feuille assets/talent-tree.css ajoute arrondis, halos et police.
STYLES = """    classDef head fill:#111b2e,stroke:#2a3852,color:#e6ecf7,stroke-width:1px;
    classDef key fill:#1c1606,stroke:#f5c542,color:#fde9a8,stroke-width:2px;
    classDef rank fill:#0e1a30,stroke:#4f8cff,color:#e6ecf7,stroke-width:2px;
    classDef option fill:#101827,stroke:#46546e,color:#cfd8e6,stroke-width:1px;
    classDef gate fill:#241b06,stroke:#c99a2e,color:#f5c542,stroke-width:1px;
    classDef ultimate fill:#1a1630,stroke:#e2c068,color:#fff6d8,stroke-width:3px;
    linkStyle default stroke:#33415c,stroke-width:2px,fill:none;"""


def clean(name):
    """Retire le préfixe d'option (« A : », « B · », « A: ») et protège les guillemets pour Mermaid."""
    name = re.sub(r'^[AB]\s*[:·]\s*', '', name.strip())
    return name.replace('"', '#quot;')


def parse(text, shape):
    """Renvoie [(titre, devise, [(rangée, [noms], points)])] pour chaque branche (titre ## ou ### suivi d'un tableau)."""
    branches, current = [], None
    for line in text.split('\n'):
        if line.startswith('## ') or line.startswith('### '):
            current = {'title': line.lstrip('#').strip(), 'motto': '', 'rows': []}
            branches.append(current)
            continue
        if current and not current['rows'] and re.fullmatch(r'\*[^*].*\*', line.strip()):
            current['motto'] = line.strip().strip('*')  # devise en italique sous le titre
            continue
        if not current or not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 3:
            continue
        name_cell = next((c for c in cells[1:3] if '**' in c), None)
        if name_cell is None:
            continue
        names = [clean(n) for n in re.findall(r'\*\*(.+?)\*\*', name_cell)]
        if cells[0].isdigit():
            # Nombre de rangs : cellule qui commence par « 3 rangs », « 5 ranks » ou « 3 × » ; sinon 1 point.
            ranks = next((int(m.group(1)) for c in cells[1:] if c is not name_cell
                          for m in [re.match(r'(\d+)\s*(rangs|ranks|×)', c)] if m), 1)
            current['rows'].append([int(cells[0]), names, ranks])
        elif cells[0] == '' and current['rows']:
            current['rows'][-1][1] += names  # option B sur une ligne de continuation
    result = []
    for b in branches:
        if not b['rows']:
            continue
        rows = b['rows']
        if [r[0] for r in rows] != list(range(1, shape['rows'] + 1)) or any(len(r[1]) not in (1, 2) for r in rows):
            raise ValueError(f'branche inattendue : {b["title"]} {rows}')
        match = re.match(r'(.+?)\s*:\s*[«"](.+?)[»"]\s*$', b['title'])
        title, motto = (match.group(1), match.group(2)) if match else (b['title'], b['motto'])
        result.append((title.strip(), motto.strip(), rows))
    if len(result) != 3:
        raise ValueError(f'{len(result)} branches au lieu de 3')
    return result


def quote(text):
    return text.replace('"', '#quot;')


def check_tables(body, owner, locale, shape):
    """Les tableaux de la page doivent nommer, rangée par rangée, les nœuds du code (choix compris)."""
    tables = parse(body, shape)
    for (title, _, rows), (code_title, _, code_rows) in zip(tables, from_code(owner, locale)):
        for (number, names, _), (_, code_names, _) in zip(rows, code_rows):
            if [quote(nm) for nm in names] != code_names:
                raise ValueError(f'{locale}/{owner}, {title}, rangée {number} : {names} au lieu de {code_names}')


def diagram(branches, t, shape):
    lines = ['```mermaid', 'graph TB']
    # Mermaid 8.8.2 place le dernier sous-graphe défini à gauche : on les écrit dans l'ordre inverse.
    for index in range(len(branches), 0, -1):
        title, motto, rows = branches[index - 1]
        p = f'B{index}'
        # En-tête de branche dans un nœud : en 8.8.2, le titre d'un sous-graphe chevauche son premier nœud.
        # Mermaid 8.8.2 échappe les balises des libellés, sauf <br/> : pas de gras ni d'italique.
        header = quote(title.upper()) + (f'<br/>{quote(motto)}' if motto else '')
        lines.append(f'    subgraph {p}[" "]')
        lines.append(f'        {p}H["{header}"]:::head')
        previous = [f'{p}H']
        for number, names, points in rows:
            pts = t['pts' if points > 1 else 'pt'].format(n=points)
            if len(names) == 2:
                # Choix exclusif : les deux options côte à côte, comme les cases 1 | 2 du jeu.
                current = [f'{p}R{number}A', f'{p}R{number}B']
                lines.append(f'        {current[0]}["① {names[0]}<br/>{pts}"]:::option')
                lines.append(f'        {current[1]}["② {names[1]}<br/>{pts}"]:::option')
            elif number == shape['rows']:
                current = [f'{p}R{number}']
                lines.append(f'        {current[0]}[["✦ {names[0]}<br/>{t["ultimate"]}"]]:::ultimate')
            elif points == 1:
                current = [f'{p}R{number}']
                lines.append(f'        {current[0]}{{{{"{names[0]}<br/>{pts}"}}}}:::key')
            else:
                current = [f'{p}R{number}']
                lines.append(f'        {current[0]}("{names[0]}<br/>{pts}"):::rank')
            for a in previous:
                for b in current:
                    lines.append(f'        {a} --- {b}')
            previous = current
            if number in shape['gates']:
                gate = f'{p}G{number}'
                lines.append(f'        {gate}(["{t["gate"].format(n=shape["gates"][number])}"]):::gate')
                for a in previous:
                    lines.append(f'        {a} --- {gate}')
                previous = [gate]
        lines.append('    end')
    lines.append(STYLES)
    # Cartes de branche : fond bleu nuit, comme les panneaux du jeu (sinon gris du thème de Wiki.js).
    for index in range(1, len(branches) + 1):
        lines.append(f'    style B{index} fill:#0b1322,stroke:#1e2a40,stroke-width:1px;')
    lines.append('```')
    return '\n'.join(lines)


def pages():
    """(chemin, langue, forme) des pages à diagramme : les dix classes et l'arbre commun, en FR et en EN."""
    for locale in TEXT:
        for path in sorted((ROOT / locale / 'dynasty' / 'classes').glob('*.md')):
            if path.stem != 'diagrams':  # page de test, hors dépôt
                yield path, locale, 'class'
        yield ROOT / locale / 'dynasty' / 'common-tree.md', locale, 'common'


def owner_of(path, kind):
    return 'common' if kind == 'common' else path.stem


def section_for(owner, locale, kind):
    t, shape = TEXT[locale], shape_of(owner)
    intro = t['intro'].format(tree=t['tree'][kind], where=t['where'][kind])
    return f'{t["title"]}\n\n{intro}\n\n{diagram(from_code(owner, locale), t, shape)}\n\n'


def update(path, locale, kind):
    t, owner = TEXT[locale], owner_of(path, kind)
    text = path.read_text(encoding='utf-8')
    head, body = text.split('\n---\n\n', 1)
    check_tables(body, owner, locale, shape_of(owner))
    section = section_for(owner, locale, kind)
    if t['title'] in body:
        start = body.index(t['title'])
        end = body.index('\n```\n', body.index('```mermaid', start)) + len('\n```\n\n')
        new_body = body[:start] + section + body[end:]
    else:
        marker = t['detail'] + '\n\n'
        if marker not in body:
            raise ValueError(f'{path} : section « {t["detail"]} » absente')
        new_body = body.replace(marker, marker + section, 1)
    return head + '\n---\n\n' + new_body, new_body != body


if __name__ == '__main__':
    if '--print' in sys.argv:  # --print fr/energist ou fr/common-tree : affiche le bloc Mermaid d'une seule page
        locale, name = sys.argv[sys.argv.index('--print') + 1].split('/')
        kind = 'common' if name == 'common-tree' else 'class'
        owner = 'common' if kind == 'common' else name
        print(diagram(from_code(owner, locale), TEXT[locale], shape_of(owner)))
        sys.exit()
    check = '--check' in sys.argv
    for path, locale, kind in pages():
        text, changed = update(path, locale, kind)
        if changed and not check:
            path.write_text(text, encoding='utf-8')
        print(f'{"à régénérer" if check and changed else "modifiée" if changed else "à jour"} {path.relative_to(ROOT)}')
