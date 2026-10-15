"""Données et rendu de la rubrique Dynastie et talents, reprises du code du jeu (sources dans DONNEES §18).

- talents.json : export du catalogue du serveur (arbres, rangs, portes, effets, plafonds, dynasties, règles),
  produit par export_talents.php sur le dépôt du backend :
      php tools/dynasty_pages/export_talents.php <chemin du backend> > tools/dynasty_pages/talents.json
- labels.json : textes du client (talents.json, dynasties.json, classes.json, pages/talents.json, FR et EN).

Le texte d'un nœud est celui que le jeu affiche (port de talentText.ts du client) : la description du nœud,
avec ses valeurs au rang maximal. Régénérer : python3 tools/dynasty_pages/<script>.py (voir README de la rubrique
dans write.py). Après un rééquilibrage, refaire l'export puis relancer les scripts.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE / 'talents.json').read_text())
LABELS = json.loads((HERE / 'labels.json').read_text())
CLASSES = ['admiral', 'builder', 'energist', 'theorist', 'navigator', 'shadow', 'archivist', 'veteran', 'symbiote', 'oracle']
RULES = DATA['rules']
CEIL = DATA['ceilings']


def n(x, lang, digits=2):
    """Nombre au format du wiki : 2 décimales au plus, espace (FR) ou virgule (EN) des milliers."""
    x = round(float(x), digits)
    if x.is_integer():
        s = f'{int(x):,}'
    else:
        s = f'{x:,.{digits}f}'.rstrip('0').rstrip('.')
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s


def pct(x, lang):
    return f'{n(x, lang)} %' if lang == 'fr' else f'{n(x, lang)}%'


def T(lang):
    return LABELS[lang]['talents']


def fill(template, params):
    return re.sub(r'\{\{(\w+)\}\}', lambda m: str(params.get(m.group(1), m.group(0))), template)


def clean(text):
    """Typographie du wiki : pas de tiret cadratin ni demi-cadratin dans les textes repris du jeu."""
    text = re.sub(r'\s[—–]\s(.+?)\s[—–](,?)', r' (\1)\2', text)  # incise entre deux tirets : parenthèses
    text = re.sub(r'\s+[—–]\s+', ', ', text)
    return text.replace('—', ', ').replace('–', '-')


def amount(unit, value, lang):
    tmpl = T(lang)['units'].get(unit)
    return fill(tmpl, {'value': n(value, lang)}) if tmpl else n(value, lang)


HOURS_IN = {'seconds': 1 / 3600, 'minutes': 1 / 60, 'hours': 1, 'days': 24}


def natural_duration(unit, value, lang):
    hours = value * HOURS_IN.get(unit, 0)
    if hours >= 48 and hours % 24 == 0:
        return fill(T(lang)['natural']['days'], {'value': n(hours / 24, lang)})
    return amount(unit, value, lang)


def natural_every(unit, value, lang):
    nat = T(lang)['natural']
    hours = value * HOURS_IN.get(unit, 0)
    if hours == 24:
        return nat['everyDay']
    if hours == 168:
        return nat['everyWeek']
    if hours > 0 and hours % 168 == 0:
        return fill(nat['everyWeeks'], {'value': n(hours / 168, lang)})
    if hours > 0 and hours % 24 == 0:
        return fill(nat['everyDays'], {'value': n(hours / 24, lang)})
    return fill(nat['every'], {'value': amount(unit, value, lang)})


def times(value, lang):
    t = T(lang)['natural']['times']
    key = str(value).replace('.0', '') if float(value).is_integer() else str(value).replace('.', '_')
    return t.get(key, fill(t['other'], {'value': n(value, lang)}))


def plural(entry, base, count, lang):
    """Choisit base, base_one ou base_other comme i18next (FR : 0 et 1 au singulier)."""
    if base in entry:
        return entry[base]
    one = count in (0, 1) if lang == 'fr' else count == 1
    return entry.get(f'{base}_one' if one else f'{base}_other')


def value_at(effect, ranks):
    """TalentEffect::valueAt : la valeur une fois, ou une fois par rang ; une valeur fixe ne bouge pas."""
    if ranks <= 0:
        return 0.0
    return round(effect['value'] * ranks if effect['per_rank'] and not effect['fixed'] else effect['value'], 6)


def node_entry(lang, key, option=None):
    e = T(lang)['nodes'][key]
    return e[f'option{option}'] if option else e


def node_name(lang, key, option=None):
    return clean(node_entry(lang, key, option)['name'])


def effects_of(node, option=None):
    return [e for e in node['effects'] if (e['option'] is None) == (option is None) and (option is None or e['option'] == option)]


def describe(lang, node, option=None, ranks=None):
    """La phrase que le jeu affiche pour ce nœud (ou cette option) à `ranks` rangs (par défaut : nœud plein)."""
    ranks = node['ranks'] if ranks is None else ranks
    effects = effects_of(node, option)
    params, count = {}, None
    for i, e in enumerate(effects):
        s = '' if i == 0 else str(i + 1)
        v = value_at(e, ranks)
        if i == 0:
            count = v
        params[f'value{s}'] = amount(e['unit'], v, lang)
        params[f'number{s}'] = n(v, lang)
        params[f'duration{s}'] = natural_duration(e['unit'], v, lang)
        params[f'every{s}'] = natural_every(e['unit'], v, lang)
        params[f'times{s}'] = times(v, lang)
    entry = node_entry(lang, node['key'], option)
    tmpl = plural(entry, 'description', count if count is not None else 1, lang)
    if tmpl:
        return clean(fill(tmpl, params))
    texts = []
    for e in effects:  # pas de phrase propre : une phrase par levier, comme le client
        v = value_at(e, ranks)
        lever = T(lang)['levers'].get(e['lever'], e['lever'])
        texts.append(clean(lever if e['unit'] == 'unlock' else fill(lever, {'value': amount(e['unit'], v, lang), 'count': n(v, lang)})))
    return ' ; '.join(texts)


def per_rank(lang, node):
    """Colonne « par rang » : la valeur d'un rang du premier effet qui grandit avec les rangs."""
    grow = [e for e in node['effects'] if e['per_rank'] and not e['fixed']]
    if node['type'] != 'ranks' or not grow:
        return ''
    e = grow[0]
    return f"{node['ranks']} × {amount(e['unit'], e['value'], lang)}"


def branch_name(lang, key):
    return clean(T(lang)['branches'][key]['name'])


def branch_motto(lang, key):
    return clean(T(lang)['branches'][key]['motto'])


def tree(owner):
    return DATA['trees'][owner]


def class_label(lang, key, field='name'):
    return clean(LABELS[lang]['classes'][key][field])


WORD = {
    'fr': {'row': 'Rangée', 'node': 'Nœud', 'effect': 'Effet (nœud plein)', 'per': 'Par rang', 'type': 'Type',
           'ranks': 'rangs', 'key': 'clé', 'choice': 'choix', 'capstone': 'ultime', 'or': 'ou',
           'gate': '{n} points placés au-dessus', 'open': 'ouverte', 'ultimate': '*(ultime)*'},
    'en': {'row': 'Row', 'node': 'Node', 'effect': 'Effect (full node)', 'per': 'Per rank', 'type': 'Type',
           'ranks': 'ranks', 'key': 'key', 'choice': 'choice', 'capstone': 'ultimate', 'or': 'or',
           'gate': '{n} points placed above', 'open': 'open', 'ultimate': '*(ultimate)*'},
}


def node_type(lang, node):
    w = WORD[lang]
    if node['type'] == 'ranks':
        return f"{node['ranks']} {w['ranks']}"
    return w[node['type']]


def branch_table(lang, branch):
    """Tableau d'une branche : rangée, nœud, type, effet au rang maximal, valeur par rang. Une ligne par option d'un choix."""
    w = WORD[lang]
    out = [f"| {w['row']} | {w['node']} | {w['type']} | {w['effect']} | {w['per']} |", '|---|---|---|---|---|']
    for node in branch['nodes']:
        if node['type'] == 'choice':
            for opt, letter in ((1, 'A'), (2, 'B')):
                row = str(node['row']) if opt == 1 else ''
                typ = node_type(lang, node) if opt == 1 else ''
                out.append(f"| {row} | **{letter} · {node_name(lang, node['key'], opt)}** | {typ} | {describe(lang, node, opt)} | |")
        else:
            name = f"**{node_name(lang, node['key'])}**"
            out.append(f"| {node['row']} | {name} | {node_type(lang, node)} | {describe(lang, node)} | {per_rank(lang, node)} |")
    return '\n'.join(out)


def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    out += ['| ' + ' | '.join(str(c) for c in r) + ' |' for r in rows]
    return '\n'.join(out)


def lever_text(lang, lever, value):
    """Le libellé d'un levier (textes du client), à la valeur donnée."""
    unit = DATA['lever_units'][lever]
    tmpl = plural(T(lang)['levers'], lever, value, lang)
    if not tmpl:
        return f'{lever} : {amount(unit, value, lang)}'
    return clean(fill(tmpl, {'value': amount(unit, value, lang), 'count': n(value, lang)}))


def tree_reach(owner):
    """Ce que l'arbre atteint au plus, levier par levier : somme des nœuds pleins, la meilleure option d'un choix."""
    reach = {}
    for b in tree(owner):
        for node in b['nodes']:
            best = {}
            for e in node['effects']:
                if e['fixed'] or e['unit'] == 'unlock':
                    continue
                v = value_at(e, node['ranks'])
                best[e['lever']] = max(best.get(e['lever'], 0.0), v)
            for lever, v in best.items():
                reach[lever] = round(reach.get(lever, 0.0) + v, 6)
    return reach


def class_caps_table(lang, owner):
    """Plafonds propres à la classe : les leviers de son arbre que le code borne pour elle."""
    caps, reach = DATA['class_caps'][owner], tree_reach(owner)
    fr = lang == 'fr'
    rows = []
    for lever, r in reach.items():
        cap = caps.get(lever)
        if cap is None:
            continue
        unit = DATA['lever_units'][lever]
        note = ''
        if r > cap + 1e-9:
            note = ' (plafonné)' if fr else ' (capped)'
        rows.append([lever_text(lang, lever, cap), amount(unit, r, lang) + note])
    head = ['Plafond de la classe (talents des deux arbres)', "Ce que l'arbre de classe atteint"] if fr else \
           ['Class cap (talents of both trees)', 'What the class tree reaches']
    return table(head, rows)
