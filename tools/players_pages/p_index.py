import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *

PAGES = [
 ('rankings', 'Classements et points', f'1 point pour {n(POINT_DIVISOR, "fr")} ressources, quatre classements de joueurs et deux d\'alliance.',
              'Rankings and points', f'1 point per {n(POINT_DIVISOR, "en")} resources, four player rankings and two alliance rankings.'),
 ('beginner-protection', 'Protection des débutants', f'{NEWCOMER_DAYS} jours de protection nouvel arrivant, puis paliers de points.',
              'Beginner protection', f'{NEWCOMER_DAYS} days of newcomer protection, then point tiers.'),
 ('attack-limit', "Limite d'attaques", f'{BASH_MAX} attaques sur un même joueur par tranche de {BASH_WINDOW_H} h (par défaut).',
              'Attack limit', f'{BASH_MAX} attacks on the same player per {BASH_WINDOW_H}-hour window (default).'),
 ('vacation-mode', 'Mode vacances', f'Mettre son empire en pause, {VACATION_MIN_H} h au moins.',
              'Vacation mode', f'Pausing your empire, {VACATION_MIN_H} h at least.'),
 ('inactivity', 'Inactivité', 'Ce que coûte une absence sans mode vacances.',
              'Inactivity', 'What an absence without vacation mode costs.'),
 ('alliances', 'Alliances', 'Fonder, rejoindre, rangs et sièges.', 'Alliances', 'Founding, joining, ranks and seats.'),
 ('pacts-and-wars', 'Pactes, fair-play et guerres', 'Diplomatie entre alliances.', 'Pacts, fair play and wars', 'Diplomacy between alliances.'),
 ('alliance-missions', "Missions et station d'alliance", "Trésorerie, entraide, station et missions.", 'Alliance missions and station', 'Treasury, mutual aid, station and missions.'),
 ('messages-and-reports', 'Messagerie et rapports', f'Chat, rapports gardés {REPORT_RETENTION_D} jours, partage et réglages.',
              'Messages and reports', f'Chat, reports kept {REPORT_RETENTION_D} days, sharing and settings.'),
 ('game-rules', 'Règlement', '', 'Game rules', ''),
]

def body(lang):
    fr = lang == 'fr'
    lines = []
    for slug, tfr, dfr, ten, den in PAGES:
        t, d = (tfr, dfr) if fr else (ten, den)
        lines.append(f'- [{t}](/{lang}/players/{slug})' + (f' : {d}' if fr and d else (f': {d}' if d else '')))
    items = '\n'.join(lines)
    if fr:
        return f'''# Joueurs et règles

**Classements, protections, alliances et règlement.**

## Pages de cette rubrique

{items}
'''
    return f'''# Players and rules

**Rankings, protections, alliances and rules.**

## Pages in this section

{items}
'''

for lang in ('fr', 'en'):
    write(lang, 'players', body(lang))
