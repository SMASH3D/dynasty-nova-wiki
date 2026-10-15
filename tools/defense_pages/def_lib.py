"""Valeurs et formules de la rubrique Défense, reprises du code du jeu (astro-nova-backend main 7b255c83, 15 octobre 2026 ; sources dans DONNEES §7).

Régénérer les pages : python3 tools/defense_pages/p_defense.py
Le script réécrit le corps des pages FR et EN (defense, defense/defenses, defense/shield-domes,
defense/missiles) sans toucher au front matter. Après un rééquilibrage, mettre à jour CAT, RF,
SILO et les constantes ici, puis relancer.
"""
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / 'pages'
fl = math.floor


def rnd(x):
    """round() de PHP : demi vers l'extérieur."""
    return int(math.floor(x + 0.5)) if x >= 0 else -int(math.floor(-x + 0.5))


def n(x, lang):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s


def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'


def dur(sec, lang):
    """Durée lisible : 3 h 12 min, 9 min 36 s, 45 s."""
    sec = int(sec)
    d, r = divmod(sec, 86400)
    h, r = divmod(r, 3600)
    m, s = divmod(r, 60)
    parts = []
    if d: parts.append(f'{d} j' if lang == 'fr' else f'{d} d')
    if h: parts.append(f'{h} h')
    if m: parts.append(f'{m} min')
    if s or not parts: parts.append(f'{s} s')
    return ' '.join(parts[:2]) if d else ' '.join(parts)


# --- Catalogue (table `defense`, semée par les migrations, relevée en base migrée le 15 octobre 2026)
# code, nom FR, nom EN (wiki), image, (métal, cristal, hydrogène), structure, bouclier, arme, build_time (s),
# unique, missile, cases d'Arsenal, prérequis [(type, code, niveau)]
CAT = [
    ('ballistic_projector', 'Projecteur balistique', 'Ballistic Projector', 'projecteur-balistique', (2000, 0, 0), 2000, 20, 80, 2880, False, False, 0,
     [('b', 'shipyard', 1)]),
    ('photonic_cannon', 'Canon photonique', 'Photonic Cannon', 'canon-photonique', (1500, 500, 0), 2000, 25, 100, 2880, False, False, 0,
     [('b', 'shipyard', 2), ('r', 'laser', 3)]),
    ('high_energy_emitter', 'Émetteur à haute énergie', 'High-Energy Emitter', 'emetteur-a-haute-energie', (6000, 2000, 0), 8000, 100, 250, 11520, False, False, 0,
     [('b', 'shipyard', 4), ('r', 'laser', 6), ('r', 'energy_science', 3)]),
    ('ion_battery', 'Batterie ionique', 'Ion Battery', 'batterie-ionique', (2000, 6000, 0), 8000, 500, 150, 11520, False, False, 0,
     [('b', 'shipyard', 4), ('r', 'ion', 4)]),
    ('magnetic_accelerator', 'Accélérateur magnétique', 'Magnetic Accelerator', 'accelerateur-magnetique', (20000, 15000, 2000), 35000, 200, 1100, 50400, False, False, 0,
     [('b', 'shipyard', 6), ('r', 'weapons', 3), ('r', 'shielding', 1), ('r', 'energy_science', 6)]),
    ('plasma_ejector', 'Éjecteur à plasma', 'Plasma Ejector', 'ejecteur-a-plasma', (50000, 50000, 30000), 100000, 300, 3000, 100800, False, False, 0,
     [('b', 'shipyard', 8), ('r', 'plasma', 7)]),
    ('defensive_barrier', 'Barrière défensive', 'Defensive Barrier', 'barriere-defensive', (10000, 10000, 0), 20000, 2000, 1, 28800, True, False, 0,
     [('b', 'shipyard', 1), ('r', 'shielding', 2)]),
    ('protective_dome', 'Dôme protecteur', 'Protective Dome', 'dome-protecteur', (50000, 50000, 0), 100000, 10000, 1, 144000, True, False, 0,
     [('b', 'shipyard', 6), ('r', 'shielding', 6)]),
    ('interceptors', 'Intercepteurs', 'Interception Missile', 'intercepteurs', (8000, 2000, 0), 8000, 1, 1, 11520, False, True, 1,
     [('b', 'shipyard', 1), ('b', 'missile_silo', 2)]),
    ('long_range_warheads', 'Ogives longue portée', 'Long-Range Warheads', 'ogives-longue-portee', (12500, 2500, 10000), 15000, 1, 12000, 21600, False, True, 2,
     [('b', 'shipyard', 1), ('b', 'missile_silo', 4), ('r', 'impulse_drive', 1)]),
]
BY = {c[0]: c for c in CAT}
DEFENSES = [c for c in CAT if not c[10]]
MISSILES = [c for c in CAT if c[10]]

NAMES = {  # libellés du jeu (front, src/i18n/locales/{fr,en})
    'shipyard': ('Dock orbital', 'Orbital Dock'),
    'missile_silo': ('Arsenal balistique', 'Ballistic Arsenal'),
    'laser': ('Systèmes Photoniques', 'Laser Technology'),
    'energy_science': ('Science Énergétique', 'Energy Science'),
    'ion': ('Manipulation Ionique', 'Ion Technology'),
    'weapons': ('Systèmes Offensifs', 'Weapon Systems'),
    'shielding': ('Champs de Protection', 'Shielding Technology'),
    'armor': ('Métallurgie Avancée', 'Armor Technology'),
    'plasma': ('Maîtrise du Plasma', 'Plasma Technology'),
    'impulse_drive': ('Moteur Magnétique', 'Impulse Drive'),
}
SHIPS = {  # noms FR du jeu, EN provisoires (PLAN §8)
    'battle_cruiser': ('Colossus stellaire', 'Stellar Colossus'),
    'bomber': ('Frappe-orbital', 'Orbital Striker'),
    'cruiser': ('Corvette', 'Corvette'),
    'destroyer': ('Annihilateur', 'Annihilator'),
}
# Tirs rapides contre les défenses (table `rapid_fire`) ; aucune défense n'en a
RF = {
    'ballistic_projector': [('bomber', 20), ('cruiser', 10), ('battle_cruiser', 200)],
    'photonic_cannon': [('bomber', 20), ('destroyer', 10), ('battle_cruiser', 200)],
    'high_energy_emitter': [('bomber', 10), ('battle_cruiser', 100)],
    'ion_battery': [('bomber', 10), ('battle_cruiser', 100)],
    'magnetic_accelerator': [('bomber', 5), ('battle_cruiser', 50)],
    'plasma_ejector': [('bomber', 5)],
    'defensive_barrier': [],
    'protective_dome': [],
}

# --- Arsenal balistique (table `building`) : coût du niveau 1, facteur 2, niveau max 10, planète seulement
SILO_BASE = (20000, 20000, 1000)
SILO_FACTOR = 2
SILO_MAX = 10
SLOTS_PER_LEVEL = 10          # SiloCapacity::SLOTS_PER_LEVEL
SYSTEMS_PER_DRIVE_LEVEL = 5   # MissileRange
SECONDS_PER_SYSTEM = 30       # MissileFlight
STAT_BONUS = 0.1              # Defense::COMBAT_STAT_BONUS_PER_LEVEL, MissileBarrage::WEAPONS_BONUS_PER_LEVEL
HULL_DIVISOR = 10             # Defense::COMBAT_HULL_DIVISOR
DOCK_MAX = 12
ATTACKS, WINDOW_H = 6, 24     # BashingRule::default() ; Redline identique (DONNEES §2)
QUEUE_FREE, QUEUE_PREMIUM = 2, 5  # ConstructionQueueCapacity::default() ; Redline identique


def silo_cost(level):
    return tuple(fl(x * SILO_FACTOR ** (level - 1)) for x in SILO_BASE)


def silo_slots(level):
    return max(0, level) * SLOTS_PER_LEVEL


def points(c):
    return sum(c[4]) / 1000


def unit_time(c, dock, nanite=0, speed=1):
    """Defense::getConstructionTime() : au moins 1 s."""
    return max(1, rnd(c[8] / ((1 + dock) * 2 ** nanite) / speed))


def boosted(base, level):
    return rnd(base * (1 + STAT_BONUS * max(0, level)))


def combat_stats(c, weapons=0, shielding=0, armor=0):
    """Defense::combatStats() : (arme, bouclier, coque)."""
    return boosted(c[7], weapons), boosted(c[6], shielding), rnd(boosted(c[5], armor) / HULL_DIVISOR)


def resilience(c, shielding=0, armor=0):
    """DefenseGridEntry : bouclier + coque de combat."""
    _, s, h = combat_stats(c, 0, shielding, armor)
    return s + h


def missile_range(drive):
    """MissileRange::forImpulseDrive() : -1 = rien n'est à portée."""
    return max(-1, drive * SYSTEMS_PER_DRIVE_LEVEL - 1)


def ring(a, b, size):
    straight = abs(a - b)
    other = size - straight
    return min(straight, other) if other > 0 else straight


def flight(systems):
    return max(1, systems) * SECONDS_PER_SYSTEM


def warhead_damage(weapons, count):
    return fl(BY['long_range_warheads'][7] * (1 + STAT_BONUS * max(0, weapons)) * max(0, count))


def shatter(pool, grid, designated=None):
    """MissileBarrage::shatter() : grid = [(code, résistance, quantité)]."""
    order = sorted([g for g in grid if g[2] > 0], key=lambda g: -g[1])
    if designated:
        order = [g for g in order if g[0] == designated] + [g for g in order if g[0] != designated]
    out = []
    for code, res, qty in order:
        if res <= 0:
            continue
        k = min(qty, pool // res)
        if k <= 0:
            continue
        pool -= k * res
        out.append((code, k))
    return out, pool


def write(lang, path, body):
    p = ROOT / lang / f'{path}.md'
    head, _ = p.read_text().split('\n---\n\n', 1)
    p.write_text(head + '\n---\n\n' + body.strip('\n') + '\n')
    print('écrit', lang, path)


def table(header, rows):
    out = ['| ' + ' | '.join(header) + ' |', '|' + '---|' * len(header)]
    out += ['| ' + ' | '.join(str(x) for x in r) + ' |' for r in rows]
    return '\n'.join(out)
