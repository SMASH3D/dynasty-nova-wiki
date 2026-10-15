"""Valeurs et formules de la rubrique Univers, reprises du code du jeu (astro-nova-backend main 7b255c83, 15 octobre 2026 ; sources dans DONNEES, section « Univers (code, 15 octobre 2026) »).

Régénérer les pages : python3 tools/universe_pages/p_all.py
Chaque script réécrit le corps des pages FR et EN sans toucher au front matter (sauf `published` quand il le précise).
Mettre à jour les constantes ici après un changement du code.
"""
import math
fl = math.floor


def n(x, lang):
    """Nombre au format de la langue : espace (FR) ou virgule (EN) des milliers, virgule (FR) ou point (EN) décimal, signe moins typographique."""
    neg = x < 0
    x = abs(x)
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    s = s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s
    return ('−' if neg else '') + s


def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'


# --- Réglages d'univers (src/Shared/Domain/ValueObject/*::default(), UniverseDefaultsReadModel) ---
DEFAULTS = {
    'speeds': 1,                      # UniverseSpeeds::default() : les cinq vitesses à 1
    'bashing': (6, 24),               # BashingRule::default() : 6 attaques par fenêtre de 24 h
    'beginner_tiers': [(500, 3), (5000, 5), (500000, 10)],
    'beginner_inactivity_days': 14,
    'debris': (30, 0),                # DebrisRule : vaisseaux, défenses (%)
    'moon': (20, 2_000_000),          # MoonFormation : chance max (%), débris pour la chance max
    'abandon': dict(life=60, b_init=1, b_int=2, b_loss=1, f_init=30, f_int=2, f_loss=5,
                    d_init=35, d_int=3, d_loss=5, sat_init=100, lock=30),
    'queue': (2, 5),                  # ConstructionQueueCapacity : ordres par file, gratuit / Premium
    'bookmarks': (10, 200),           # BookmarkCapacity
    'expeditions': True,              # ExpeditionRule
    'cosmic_events': False,           # CosmicEventRule : chaque événement fermé par défaut
}
# Redline : DONNEES §2 (relevé du 2 octobre 2026) et players-10
REDLINE = {
    'map': (9, 99, 15), 'max_players': 1000, 'speeds': 1, 'start': (500, 500),
    'bashing': (6, 24), 'beginner_tiers': [(500, 3), (5000, 5), (500000, 10)],
    'beginner_inactivity_days': 7, 'debris': (30, 0), 'moon': (20, 2_000_000),
    'abandon': DEFAULTS['abandon'], 'queue': (2, 5), 'bookmarks': (10, 200),
}
POSITIONS_MIN, POSITIONS_MAX = 9, 20   # CreateUniverseRequestPayload : Range(min: 9, max: 20)
GALAXIES_MAX = 100                     # LessThanOrEqual(100)
NEWCOMER_DAYS = 7                      # NewcomerProtection::DURATION_DAYS (fixe, pas un réglage)

# --- Planètes (PlanetGeneratorService) ---
TYPES = {  # position sur 15 : (taille moyenne, types)
    1: (145, ['desert', 'dry']), 2: (150, ['desert', 'dry']), 3: (155, ['desert', 'dry', 'normal']),
    4: (160, ['dry', 'normal']), 5: (163, ['normal', 'water']), 6: (185, ['normal', 'water', 'jungle']),
    7: (190, ['normal', 'water', 'jungle']), 8: (195, ['water', 'jungle']), 9: (200, ['water', 'jungle', 'normal']),
    10: (205, ['jungle', 'normal']), 11: (225, ['ice', 'normal']), 12: (230, ['ice', 'gas']),
    13: (235, ['ice', 'gas']), 14: (242, ['ice', 'gas']), 15: (245, ['ice', 'gas']),
}
TYPE_NAMES = {
    'fr': {'desert': 'désert', 'dry': 'aride', 'normal': 'normal', 'jungle': 'jungle', 'water': 'eau', 'ice': 'glace', 'gas': 'gaz'},
    'en': {'desert': 'desert', 'dry': 'dry', 'normal': 'normal', 'jungle': 'jungle', 'water': 'water', 'ice': 'ice', 'gas': 'gas'},
}
SIZE_SPREAD = 15
MOTHER_SIZE = 163                      # Base::DEFAULT_MOTHER_BASE_SIZE


def php_round(x):
    """round() de PHP : moitié loin de zéro."""
    return int(math.floor(x + 0.5)) if x >= 0 else -int(math.floor(-x + 0.5))


def eff_pos(p, total):
    """Position ramenée sur 15 pour la taille, les types et la température : arrondie."""
    return php_round((p - 1) * (14.0 / max(1, total - 1))) + 1


def temps(ep):
    base = 160 - 15 * ep
    return base - 20, base + 20


def temp_at(tmin, tmax, day, days_in_month):
    """Map::getTemperatureAt()."""
    peak = fl(days_in_month / 2)
    f = (day - 1) / max(1, peak - 1) if day <= peak else (days_in_month - day) / max(1, days_in_month - peak)
    return php_round(tmin + (tmax - tmin) * f)


def h2factor(tmax): return max(0.0, round(1.44 - 0.004 * tmax, 3))
def satellite(tmax): return max(0, fl(tmax / 4 + 20))


# --- Bonus de position (SystemPosition) ---
METAL = [0, 0, 0, 0, 0, 17, 23, 35, 23, 17, 0, 0, 0, 0, 0]
CRYSTAL = [40, 30, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def ref_pos(p, total):
    """Position lue sur l'échelle de 15, sans arrondi."""
    return min(15.0, max(1.0, 1 + (p - 1) * 14 / max(1, total - 1)))


def interp(table, p, total):
    r = ref_pos(p, total) - 1
    below = max(0, fl(r))
    above = min(14, below + 1)
    w = r - below
    return round(table[below] + (table[above] - table[below]) * w, 2)


def metal_bonus(p, total): return interp(METAL, p, total)
def crystal_bonus(p, total): return interp(CRYSTAL, p, total)


# --- Colonisation (UserUniverse::maxBasesForAstrophysics) ---
def max_bases(level): return 1 + fl((level + 1) / 2)


# --- Distances (Distance::units, anneaux depuis le 9 octobre 2026) ---
def ring(a, b, size):
    s = abs(a - b)
    r = size - s
    return min(s, r) if r > 0 else s


def distance(o, t, galaxies, systems):
    g = ring(o[0], t[0], galaxies)
    s = ring(o[1], t[1], systems)
    p = abs(o[2] - t[2])
    if g: return 20000 * g
    if s: return 2700 + 95 * s
    if p: return 1000 + 5 * p
    return 5


# --- Lunes (MoonFormation, MoonDiameter, Base) ---
def moon_chance(debris, max_chance=20.0, cap=2_000_000):
    per_point = cap / max_chance
    if debris < per_point: return 0.0
    return min(debris * max_chance / cap, max_chance)


def moon_fields_range(chance, max_chance=20.0):
    """Cases au plafond (min, max) et diamètres (min, max) pour une chance donnée."""
    progress = max(0.01, min(1.0, chance / max_chance) * 0.20)
    out = []
    for step in (0, 10):
        fields = 10 + step + 300 * progress
        d = fl(1000 * math.sqrt(fields))
        out.append((d, fl((d / 1000) ** 2)))
    return out  # [(diam_min, cases_min), (diam_max, cases_max)]


MOON_INITIAL_FIELDS = 1
LUNAR_BASE_FIELDS = 3
LUNAR_BASE_COST = (20000, 40000, 20000)   # MySQL `building` (migrations), multiplicateur 2, pas de niveau max
PHALANX_COST = (20000, 40000, 20000)      # idem, prérequis Base lunaire 1
JUMP_GATE_COST = (2000000, 4000000, 2000000)


def cost(base, m, L): return [fl(x * m ** (L - 1)) for x in base]


def moon_fields(lunar_level, cap):
    return min(MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * lunar_level, cap)


# --- Abandon (Base::applyAbandonmentShock, settleAbandonmentDecay) ---
def share_of(q, rate): return fl(q * rate / 100)


def wasted(q, rate, steps):
    rem = q
    for _ in range(steps):
        if rem <= 0: break
        rem -= max(1, fl(rem * rate / 100))
    return max(0, rem)
