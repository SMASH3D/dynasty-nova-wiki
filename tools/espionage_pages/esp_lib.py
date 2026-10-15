"""Valeurs et formules de la rubrique Espionnage, reprises du code du jeu (astro-nova-backend main 7b255c83, 15 octobre 2026 ; sources dans DONNEES, section « Espionnage (code, 15 octobre 2026) »).

Régénérer les pages : python3 tools/espionage_pages/p_index.py tools/espionage_pages  (idem p_spying, p_report, p_phalanx).
Chaque script réécrit le corps des pages FR et EN sans toucher au front matter. Mettre à jour les constantes ici après un rééquilibrage.
"""
import math

fl = math.floor

# EffectiveEspionageLevelCalculator
MAX_PROBE_BONUS = 5
PROBES_PER_BONUS = 2
# EspionageTier
TIERS = [  # seuil, fr, en
    (1, 'ressources', 'resources'),
    (3, 'flotte', 'fleet'),
    (5, 'défenses et missiles', 'defenses and missiles'),
    (7, 'bâtiments', 'buildings'),
    (9, 'recherches', 'research'),
]
# CounterEspionageCalculator
RISK_PER_SHIP = 0.05
MIN_CHANCE, MAX_CHANCE = 5.0, 25.0
# SendFleetHandler : 5 % par niveau de Renseignement Tactique, plancher 50 %
SPY_FUEL_STEP, SPY_FUEL_FLOOR = 0.05, 0.5
# SpyMissionResolver
SPY_HISTORY_KEPT = 10
# Talents d'alliance (table alliance_talent, migration Version20261010090000)
ALLIANCE_TALENT_MAX = 3
ALLIANCE_TALENT_EFFECT = 1
ALLIANCE_QUARANTINE_HOURS = 24  # config/services.yaml alliance_quarantine_hours
# Research espionage (table research)
ESPIONAGE_MAX = 15
# Base::PHALANX_SCAN_COST, building sensor_phalanx (migration Version20260918090000)
PHALANX_SCAN_COST = 5000
PHALANX_BASE_COST = (20000, 40000, 20000)
PHALANX_FACTOR = 2
REDLINE_SYSTEMS = 99


def n(x, lang):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s


def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'


def probe_bonus(probes):
    return 0 if probes <= 0 else min(MAX_PROBE_BONUS, probes // PROBES_PER_BONUS)


def effective(att, dfn, probes, depth=0, muffling=0):
    return max(0, att - dfn + probe_bonus(probes) + depth - muffling)


def sections(level, lang):
    i = 1 if lang == 'fr' else 2
    return [t[i] for t in TIERS if level >= t[0]]


def chance(dfn, att, ships):
    if ships <= 0:
        return 0.0
    edge = 2 * dfn - att
    if edge <= 0:
        return 0.0
    return max(MIN_CHANCE, min(MAX_CHANCE, edge * ships * RISK_PER_SHIP))


def raw_chance(dfn, att, ships):
    return (2 * dfn - att) * ships * RISK_PER_SHIP


def fuel_factor(level):
    return max(SPY_FUEL_FLOOR, 1.0 - level * SPY_FUEL_STEP)


def phalanx_range(level):
    return max(1, level ** 2 - 1) if level > 0 else -1


def phalanx_cost(level):
    return [fl(c * PHALANX_FACTOR ** (level - 1)) for c in PHALANX_BASE_COST]


def ring(a, b, size):
    straight = abs(a - b)
    other = size - straight
    return min(straight, other) if other > 0 else straight


def covered_systems(origin, level, size=REDLINE_SYSTEMS):
    r = phalanx_range(level)
    return [s for s in range(1, size + 1) if ring(origin, s, size) <= r]


def spans(systems):
    """[1,2,3,7,8] -> [(1,3),(7,8)]"""
    out = []
    for s in systems:
        if out and s == out[-1][1] + 1:
            out[-1][1] = s
        else:
            out.append([s, s])
    return [tuple(x) for x in out]


def probes_for(tier, edge):
    """Plus petite vague dont le bonus atteint le palier, ou None hors de portée."""
    for p in range(1, MAX_PROBE_BONUS * PROBES_PER_BONUS + 1):
        if edge + probe_bonus(p) >= tier:
            return p
    return None
