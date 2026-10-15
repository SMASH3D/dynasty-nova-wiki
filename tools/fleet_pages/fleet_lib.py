"""Valeurs et formules de la rubrique Flotte, reprises du code du jeu (astro-nova-backend main 7b255c83,
15 octobre 2026 ; catalogue : table `ship` et `rapid_fire` d'une base migrée ; sources dans DONNEES.md,
section « Flotte (code, 15 octobre 2026) »).

Régénérer : python3 tools/fleet_pages/p_<page>.py tools/fleet_pages  (p_ships, p_rapid, p_movement,
p_missions, p_expeditions, p_jump, p_dock, p_index). Chaque script réécrit le corps des pages FR et EN
sans toucher au front matter. Mettre à jour SHIPS, RF et les formules ici après un rééquilibrage.
"""
import math

fl = math.floor


def n(x, lang):
    """Nombre au format de la langue : espace des milliers et virgule décimale en FR, virgule des milliers en EN."""
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s


def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'


def hms(sec, lang):
    """Durée lisible : heures (milliers à la manière de la langue), minutes, secondes."""
    h, r = divmod(int(sec), 3600)
    m, s = divmod(r, 60)
    out = []
    if h: out.append(f'{n(h, lang)} h')
    if m: out.append(f'{m} min')
    if s or not out: out.append(f'{s} s')
    return ' '.join(out)


# Recherches (noms affichés par le jeu, src/i18n/locales/{fr,en}/researches.json)
RES = {
    'combustion_drive': ('Propulseur Chimique', 'Combustion Drive'),
    'impulse_drive': ('Moteur Magnétique', 'Impulse Drive'),
    'hyperspace_drive': ('Navigation Transdimensionnelle', 'Hyperspace Drive'),
    'hyperspace': ('Pliage Spatial', 'Hyperspace Technology'),
    'astrophysics': ('Cosmologie Appliquée', 'Astrophysics'),
    'shielding': ('Champs de Protection', 'Shielding Technology'),
    'armor': ('Métallurgie Avancée', 'Armor Technology'),
    'weapons': ('Systèmes Offensifs', 'Weapon Systems'),
    'espionage': ('Renseignement Tactique', 'Espionage Technology'),
    'ion': ('Manipulation Ionique', 'Ion Technology'),
    'plasma': ('Maîtrise du Plasma', 'Plasma Technology'),
    'laser': ('Systèmes Photoniques', 'Laser Technology'),
    'graviton': ('Manipulation Gravitationnelle', 'Graviton Technology'),
    'quantum_computing': ('Calcul Quantique', 'Quantum Computing'),
}
# Moteurs : ReactorType::getBonusPerLevel()
DRIVE = {'combustion': ('combustion_drive', 0.1), 'impulse': ('impulse_drive', 0.2), 'hyperspace': ('hyperspace_drive', 0.3)}

# Défenses (noms du jeu, defenses.json)
DEF = {
    'ballistic_projector': ('Projecteur balistique', 'Ballistic Projector'),
    'photonic_cannon': ('Canon photonique', 'Photonic Cannon'),
    'high_energy_emitter': ('Émetteur à haute énergie', 'High-Energy Emitter'),
    'magnetic_accelerator': ('Accélérateur magnétique', 'Magnetic Accelerator'),
    'ion_battery': ('Batterie ionique', 'Ion Battery'),
    'plasma_ejector': ('Éjecteur à plasma', 'Plasma Ejector'),
    'defensive_barrier': ('Barrière défensive', 'Defensive Barrier'),
    'protective_dome': ('Dôme protecteur', 'Protective Dome'),
}

# Vaisseaux : table `ship` (type, reactor_type, base_cost, structural_integrity, shield_power, weapon_power,
# cargo_capacity, speed, fuel_consumption, build_time, reactor_upgrades, requirements). Noms EN provisoires (PLAN §8).
# code, fr, en, image, type, drive, (M, C, H), structure, bouclier, attaque, fret, vitesse, conso, build_time (s),
# changements de moteur [(moteur, niveau, vitesse, conso)], prérequis [(code, niveau)] (Dock orbital en premier)
SHIPS = [
    ('small_cargo', 'Navette de fret', 'Cargo Shuttle', 'navette-de-fret', 'civil', 'combustion', (2000, 2000, 0), 4000, 10, 5, 5000, 5000, 10, 5400,
     [('impulse', 5, 10000, 20)], [('shipyard', 2), ('combustion_drive', 2)]),
    ('large_cargo', 'Cargo stellaire', 'Stellar Freighter', 'cargo-stellaire', 'civil', 'combustion', (6000, 6000, 0), 12000, 25, 5, 25000, 7500, 50, 14400,
     [], [('shipyard', 4), ('combustion_drive', 6)]),
    ('colony_ship', 'Pionnier spatial', 'Space Pioneer', 'pionnier-spatial', 'civil', 'impulse', (10000, 20000, 10000), 30000, 100, 50, 7500, 2500, 1000, 100800,
     [], [('shipyard', 4), ('impulse_drive', 3), ('astrophysics', 1)]),
    ('recycler', 'Récupérateur', 'Salvager', 'recuperateur', 'civil', 'combustion', (10000, 6000, 2000), 16000, 10, 1, 20000, 2000, 300, 25200,
     [('impulse', 17, 4000, 600), ('hyperspace', 15, 6000, 900)], [('shipyard', 4), ('combustion_drive', 6), ('shielding', 2)]),
    ('espionage_probe', 'Éclaireur', 'Scout', 'eclaireur', 'civil', 'combustion', (0, 1000, 0), 1000, 0, 0, 5, 100000000, 1, 600,
     [], [('shipyard', 3), ('combustion_drive', 3), ('espionage', 2)]),
    ('solar_satellite', 'Collecteur solaire', 'Solar Collector', 'collecteur-solaire', 'advanced', None, (0, 2000, 500), 2000, 1, 1, 0, 0, 0, 2880,
     [], [('shipyard', 1)]),
    ('light_fighter', 'Intercepteur', 'Interceptor', 'intercepteur', 'military', 'combustion', (3000, 1000, 0), 4000, 10, 50, 50, 12500, 20, 1800,
     [], [('shipyard', 1)]),
    ('heavy_fighter', 'Assaillant', 'Assailant', 'assaillant', 'military', 'impulse', (6000, 4000, 0), 10000, 25, 150, 100, 10000, 75, 5400,
     [], [('shipyard', 3), ('armor', 2)]),
    ('cruiser', 'Corvette', 'Corvette', 'corvette', 'military', 'impulse', (20000, 7000, 2000), 27000, 50, 400, 800, 15000, 300, 28800,
     [], [('shipyard', 5), ('impulse_drive', 4), ('ion', 2)]),
    ('battleship', 'Cuirassé', 'Battleship', 'cuirasse', 'military', 'hyperspace', (45000, 15000, 0), 60000, 200, 1000, 1500, 10000, 500, 64800,
     [], [('shipyard', 7), ('hyperspace_drive', 4)]),
    ('bomber', 'Frappe-orbital', 'Orbital Striker', 'frappe-orbital', 'advanced', 'impulse', (50000, 25000, 15000), 75000, 500, 1000, 500, 4000, 700, 86400,
     [('hyperspace', 8, 5000, 700)], [('shipyard', 8), ('impulse_drive', 6), ('plasma', 5)]),
    ('predator', 'Prédateur', 'Predator', 'predateur', 'advanced', 'hyperspace', (30000, 40000, 15000), 70000, 400, 700, 750, 10000, 250, 79200,
     [], [('shipyard', 8), ('hyperspace_drive', 5), ('laser', 12), ('ion', 5)]),
    ('destroyer', 'Annihilateur', 'Annihilator', 'annihilateur', 'advanced', 'hyperspace', (60000, 50000, 15000), 110000, 500, 2000, 2000, 5000, 1000, 115200,
     [], [('shipyard', 9), ('hyperspace_drive', 6), ('armor', 6)]),
    ('battle_cruiser', 'Colossus stellaire', 'Stellar Colossus', 'colossus-stellaire', 'advanced', 'hyperspace', (5000000, 4000000, 1000000), 9000000, 50000, 200000, 1000000, 100, 1, 12960000,
     [], [('shipyard', 12), ('hyperspace_drive', 7), ('hyperspace', 6), ('graviton', 1)]),
]
S = {s[0]: s for s in SHIPS}
TYPE = {'civil': ('civil', 'civil'), 'military': ('combat', 'combat'), 'advanced': ('spécial', 'special')}


def sname(code, lang):
    if code in S:
        return S[code][1] if lang == 'fr' else S[code][2]
    return DEF[code][0 if lang == 'fr' else 1]


# Tirs rapides : table `rapid_fire` (attacker_code, target_code, value)
RF = {
    'battle_cruiser': {'solar_satellite': 1250, 'espionage_probe': 1250, 'small_cargo': 250, 'colony_ship': 250, 'large_cargo': 250, 'recycler': 250,
                       'ballistic_projector': 200, 'light_fighter': 200, 'photonic_cannon': 200, 'heavy_fighter': 100, 'high_energy_emitter': 100,
                       'ion_battery': 100, 'magnetic_accelerator': 50, 'cruiser': 33, 'battleship': 30, 'bomber': 25, 'predator': 15, 'destroyer': 5},
    'battleship': {'espionage_probe': 5, 'solar_satellite': 5},
    'bomber': {'ballistic_projector': 20, 'photonic_cannon': 20, 'high_energy_emitter': 10, 'ion_battery': 10, 'magnetic_accelerator': 5,
               'plasma_ejector': 5, 'espionage_probe': 5, 'solar_satellite': 5},
    'colony_ship': {'espionage_probe': 5, 'solar_satellite': 5},
    'cruiser': {'ballistic_projector': 10, 'light_fighter': 6, 'espionage_probe': 5, 'solar_satellite': 5},
    'destroyer': {'photonic_cannon': 10, 'predator': 2, 'espionage_probe': 5, 'solar_satellite': 5},
    'heavy_fighter': {'small_cargo': 3, 'espionage_probe': 5, 'solar_satellite': 5},
    'large_cargo': {'espionage_probe': 5, 'solar_satellite': 5},
    'light_fighter': {'espionage_probe': 5, 'solar_satellite': 5},
    'predator': {'battleship': 7, 'cruiser': 4, 'heavy_fighter': 4, 'large_cargo': 3, 'small_cargo': 3, 'espionage_probe': 5, 'solar_satellite': 5},
    'recycler': {'espionage_probe': 5, 'solar_satellite': 5},
    'small_cargo': {'espionage_probe': 5, 'solar_satellite': 5},
}


# ---- Vol (FlightPlan, FleetFlight, Distance, Ship) ----
def propulsion(code, levels):
    """(moteur, vitesse de base, conso) selon les recherches de moteur : Ship::propulsionFor(), ReactorUpgrades::bestReachedWith()."""
    s = S[code]
    best = None
    for (drv, lvl, spd, fuel) in s[14]:
        if levels.get(DRIVE[drv][0], 0) >= lvl and (best is None or ['combustion', 'impulse', 'hyperspace'].index(drv) > ['combustion', 'impulse', 'hyperspace'].index(best[0])):
            best = (drv, spd, fuel)
    return best or (s[5], s[11], s[12])


def speed(code, levels):
    drv, base, _ = propulsion(code, levels)
    return base * (1 + DRIVE[drv][1] * levels.get(DRIVE[drv][0], 0))


def cargo(code, hyper):
    return round(S[code][10] * (1 + 0.05 * hyper))


def distance(dg, ds, dp):
    """Distance::units() ; dg, ds, dp = écarts (déjà ramenés par le plus court chemin autour de l'univers)."""
    if dg: return 20000 * dg
    if ds: return 2700 + 95 * ds
    if dp: return 1000 + 5 * dp
    return 5


def ring(a, b, size):
    """Distance::roundTheRing() : écart le plus court, en passant au besoin par le bord."""
    straight = abs(a - b)
    other = size - straight
    return min(straight, other) if other > 0 else straight


def duration(d, pct_, v, fleet_speed=1, pace=1.0):
    """FleetFlight::over() : (10 + 3500 / s × √(10 d / V)) / vitesse flotte / bonus, arrondi, au moins 1 s."""
    s = max(1, pct_) / 100
    return max(1, round((10 + 3500 / s * math.sqrt(10 * d / max(1.0, v))) / max(1, fleet_speed) / pace))


def leg_fuel(d, pct_, fleet, levels):
    """FlightPlan::legBurn() + computeLegConsumption() : arrondi à l'inférieur, au moins 1 si un vaisseau consomme."""
    vmin = min(speed(c, levels) for c, q in fleet)
    burn = 0.0
    total = 0
    for c, q in fleet:
        f = propulsion(c, levels)[2] * q
        total += f
        if not f: continue
        burn += f * d / 35000 * (pct_ / 100 * math.sqrt(vmin / speed(c, levels)) + 1) ** 2
    return 0 if total == 0 else max(1, fl(burn))


def hold_fuel(hours, fleet, levels):
    """HoldDuration::fuelFor() : plafond(heures × somme des consommations / 10), avec la consommation du moteur
    d'origine (FleetComposition::totalFuelConsumption() lit getFuelConsumption(), pas le moteur changé)."""
    return math.ceil(hours * sum(S[c][12] * q for c, q in fleet) / 10)


def build_time(code, dock, nanite=0, speed_=1):
    """Ship::getConstructionTime() : build_time / ((1 + Dock) × 2^Assembleur) / vitesse chantier, arrondi, au moins 1 s."""
    return max(1, round(S[code][13] / ((1 + dock) * 2 ** nanite) / speed_))


def points(code):
    return sum(S[code][6]) / 1000
