"""Valeurs et formules de la rubrique Combat, reprises du code du jeu (astro-nova-backend main 7b255c83, 15 octobre 2026 ; sources dans DONNEES, section « Combat (code, 15 octobre 2026) »).

Régénérer : python3 tools/combat_pages/p_all.py tools/combat_pages
Le script réécrit le corps des huit pages FR et EN sans toucher au front matter. Mettre à jour SHIPS, DEFENSES, RAPID et les constantes ici après un rééquilibrage.
"""
import math
fl = math.floor

def n(x, lang):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s

def d1(x, lang):
    """Un nombre à une décimale (pourcentages de probabilité)."""
    s = f'{x:,.1f}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s

def pct(x, lang, dec=None):
    s = d1(x, lang) if dec == 1 else n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'

# --- Moteur (BattleRules::default(), HitChanceParameters::alwaysHit()) ---
ROUNDS = 6
BOUNCE = 0.01          # règle du 1 %
EXPLOSION = 0.70       # seuil d'explosion
HULL_DIVISOR = 10      # coque de combat = structure / 10
BONUS_PER_LEVEL = 0.1  # Systèmes Offensifs, Champs de Protection, Métallurgie Avancée
DOCTRINE = 5           # Doctrine d'armement, Doctrine de protection (alliance, niveau max 1)
CARGO_PER_LEVEL = 0.05 # Pliage Spatial

# --- Pillage (LootRate, PlayerBonuses) ---
LOOT = 50
LOOT_FLOOR = 30

# --- Reconstruction (DefenseRepairRate, DynastyTraits) ---
REPAIR = 70
REPAIR_HERITAGE = 5
REPAIR_TALENT_CEILING = 15
REPAIR_CEILING = 85

# --- Débris et lunes (DebrisRule, MoonFormation, MoonDiameter) ---
DEBRIS_SHIPS = 30
DEBRIS_DEFENSES = 0
DEBRIS_EXPEDITION = 10
MOON_MAX = 20
MOON_DEBRIS_FOR_MAX = 2_000_000

# --- Simulateur (SimulationLimits, config/services.yaml ; SimulatorPage.tsx) ---
SIM_UNITS = 5_000_000
SIM_ITER = 50
SIM_DEPLOY = 10_000_000
SIM_FRONT_ITER = 50

# code, fr, en (provisoire, PLAN §8), coût (M, C, H), structure, bouclier, arme, fret
SHIPS = [
    ('small_cargo', 'Navette de fret', 'Cargo Shuttle', (2000, 2000, 0), 4000, 10, 5, 5000),
    ('large_cargo', 'Cargo stellaire', 'Stellar Freighter', (6000, 6000, 0), 12000, 25, 5, 25000),
    ('colony_ship', 'Pionnier spatial', 'Space Pioneer', (10000, 20000, 10000), 30000, 100, 50, 7500),
    ('recycler', 'Récupérateur', 'Salvager', (10000, 6000, 2000), 16000, 10, 1, 20000),
    ('espionage_probe', 'Éclaireur', 'Scout', (0, 1000, 0), 1000, 0, 0, 5),
    ('solar_satellite', 'Collecteur solaire', 'Solar Collector', (0, 2000, 500), 2000, 1, 1, 0),
    ('light_fighter', 'Intercepteur', 'Interceptor', (3000, 1000, 0), 4000, 10, 50, 50),
    ('heavy_fighter', 'Assaillant', 'Assailant', (6000, 4000, 0), 10000, 25, 150, 100),
    ('cruiser', 'Corvette', 'Corvette', (20000, 7000, 2000), 27000, 50, 400, 800),
    ('battleship', 'Cuirassé', 'Battleship', (45000, 15000, 0), 60000, 200, 1000, 1500),
    ('bomber', 'Frappe-orbital', 'Orbital Striker', (50000, 25000, 15000), 75000, 500, 1000, 500),
    ('predator', 'Prédateur', 'Predator', (30000, 40000, 15000), 70000, 400, 700, 750),
    ('destroyer', 'Annihilateur', 'Annihilator', (60000, 50000, 15000), 110000, 500, 2000, 2000),
    ('battle_cruiser', 'Colossus stellaire', 'Stellar Colossus', (5000000, 4000000, 1000000), 9000000, 50000, 200000, 1000000),
]
# code, fr, en, coût, structure, bouclier, arme, unique
DEFENSES = [
    ('ballistic_projector', 'Projecteur balistique', 'Ballistic Projector', (2000, 0, 0), 2000, 20, 80, False),
    ('photonic_cannon', 'Canon photonique', 'Photonic Cannon', (1500, 500, 0), 2000, 25, 100, False),
    ('high_energy_emitter', 'Émetteur à haute énergie', 'High-Energy Emitter', (6000, 2000, 0), 8000, 100, 250, False),
    ('ion_battery', 'Batterie ionique', 'Ion Battery', (2000, 6000, 0), 8000, 500, 150, False),
    ('magnetic_accelerator', 'Accélérateur magnétique', 'Magnetic Accelerator', (20000, 15000, 2000), 35000, 200, 1100, False),
    ('plasma_ejector', 'Éjecteur à plasma', 'Plasma Ejector', (50000, 50000, 30000), 100000, 300, 3000, False),
    ('defensive_barrier', 'Barrière défensive', 'Defensive Barrier', (10000, 10000, 0), 20000, 2000, 1, True),
    ('protective_dome', 'Dôme protecteur', 'Protective Dome', (50000, 50000, 0), 100000, 10000, 1, True),
]
SHIP = {s[0]: s for s in SHIPS}
DEF = {d[0]: d for d in DEFENSES}

def name(code, lang):
    u = SHIP.get(code) or DEF.get(code)
    return u[1] if lang == 'fr' else u[2]

# --- Statistiques effectives (Ship/Defense::combatStats(), CombatResearch::withBonuses(), AllianceBonuses::boost()) ---
def boosted(base, level):
    return int(round(base * (1.0 + BONUS_PER_LEVEL * max(0, level))))

def boost(value, percent):
    return value if percent == 0 else fl(round(value * (100 + percent) / 100, 6))

def stats(code, weapons=0, shielding=0, armor=0, doctrine_weapons=0, doctrine_protection=0):
    u = SHIP.get(code) or DEF.get(code)
    structure, shield, weapon = (u[4], u[5], u[6])
    hull = int(round(boosted(structure, armor) / HULL_DIVISOR))
    return {
        'weapon': boost(boosted(weapon, weapons), doctrine_weapons),
        'shield': boost(boosted(shield, shielding), doctrine_protection),
        'hull': boost(hull, doctrine_protection),
    }

# --- Débris (DebrisFieldCalculator::fromLosses()) ---
def debris(losses, ship_rate=DEBRIS_SHIPS, defense_rate=DEBRIS_DEFENSES):
    m = c = 0.0
    for code, qty in losses.items():
        if code in SHIP:
            cost, rate = SHIP[code][3], ship_rate
        else:
            cost, rate = DEF[code][3], defense_rate
        m += cost[0] * qty * rate / 100
        c += cost[1] * qty * rate / 100
    return fl(m), fl(c)

# --- Lune (MoonFormation::chanceFor(), MoonDiameter::roll(), maxFields()) ---
def moon_chance(units, max_chance=MOON_MAX, for_max=MOON_DEBRIS_FOR_MAX):
    if units < for_max / max_chance:
        return 0.0
    return min(units * max_chance / for_max, max_chance)

def moon_diameters(chance, max_chance=MOON_MAX):
    p = max(0.01, min(1.0, chance / max_chance) * 0.20)
    return [fl(1000 * math.sqrt(10 + x + 300 * p)) for x in range(11)]

def moon_fields(diameter):
    return fl((diameter / 1000) ** 2)

# --- Destruction de lune (MoonDestructionOdds) ---
def moon_destroy(diameter, colossi):
    return min(100.0, max(0.0, 100.0 - math.sqrt(diameter)) * math.sqrt(colossi)) if colossi > 0 else 0.0

def fleet_loss(diameter):
    return math.sqrt(diameter) / 2.0

# --- Reconstruction (tirage indépendant par unité) ---
def binom(k, n_, p):
    return math.comb(n_, k) * p ** k * (1 - p) ** (n_ - k)

# --- Pillage (LootRate::of(), Fleet::fit(), Ship::effectiveCargoCapacity()) ---
def loot(stock, rate=LOOT):
    return tuple(fl(round(r * rate / 100, 6)) for r in stock)

def fit(load, room):
    total = sum(load)
    if total <= room:
        return tuple(load)
    return tuple(fl(room * r / total) for r in load)

def cargo(code, qty, hyperspace=0):
    return int(round(SHIP[code][7] * (1.0 + CARGO_PER_LEVEL * max(0, hyperspace)))) * qty
