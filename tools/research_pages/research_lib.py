"""Valeurs et formules de la rubrique Recherche, reprises du code du jeu (astro-nova-backend main 7b255c83,
15 octobre 2026 ; sources dans DONNEES §5). Catalogue relevé dans les tables research, building, ship et defense
d'une base où toutes les migrations ont été rejouées ; noms affichés relevés dans Astro-Nova-React (src/i18n/locales).

Régénérer : python3 tools/research_pages/p_technologies.py (idem p_tech_tree, p_collaboration, p_index).
Chaque script réécrit le corps des pages FR et EN sans toucher au front matter. Après un rééquilibrage,
mettre à jour les listes ci-dessous et relancer les quatre scripts.
"""
import math
fl = math.floor

def n(x, lang):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s

def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'

def dur(seconds):
    s = int(seconds); h, s = divmod(s, 3600); m, s = divmod(s, 60)
    parts = ([f'{h} h'] if h else []) + ([f'{m} min'] if m else []) + ([f'{s} s'] if s or not (h or m) else [])
    return ' '.join(parts)

RESEARCH = [  # code, catégorie serveur, position, max, facteur, (M, C, H, énergie) niv. 1, prérequis
 ('energy_science', 'energy', 1, 25, 2, (0, 800, 400, 0), [('b', 'research_lab', 1)]),
 ('plasma', 'energy', 2, 20, 2, (2000, 4000, 1000, 0), [('b', 'research_lab', 4), ('r', 'energy_science', 8), ('r', 'laser', 10), ('r', 'ion', 5)]),
 ('quantum_computing', 'computer', 3, 20, 2, (0, 400, 600, 0), [('b', 'research_lab', 1)]),
 ('research_network', 'computer', 4, 10, 2, (240000, 400000, 160000, 0), [('b', 'research_lab', 10), ('r', 'quantum_computing', 8), ('r', 'hyperspace', 8)]),
 ('combustion_drive', 'drive', 5, 15, 2, (400, 0, 600, 0), [('b', 'research_lab', 1), ('r', 'energy_science', 1)]),
 ('impulse_drive', 'drive', 6, 15, 2, (2000, 4000, 600, 0), [('b', 'research_lab', 2), ('r', 'energy_science', 1), ('r', 'combustion_drive', 3)]),
 ('hyperspace_drive', 'drive', 7, 15, 2, (10000, 20000, 6000, 0), [('b', 'research_lab', 7), ('r', 'energy_science', 1), ('r', 'hyperspace', 3)]),
 ('laser', 'weapons', 8, 20, 2, (200, 100, 0, 0), [('b', 'research_lab', 1), ('r', 'energy_science', 2)]),
 ('ion', 'weapons', 9, 15, 2, (1000, 300, 100, 0), [('b', 'research_lab', 4), ('r', 'energy_science', 4), ('r', 'laser', 5)]),
 ('hyperspace', 'weapons', 10, 15, 2, (0, 4000, 2000, 0), [('b', 'research_lab', 7), ('r', 'energy_science', 5), ('r', 'laser', 7), ('r', 'ion', 5)]),
 ('shielding', 'defense', 11, 20, 2, (200, 600, 0, 0), [('b', 'research_lab', 6), ('r', 'energy_science', 3)]),
 ('armor', 'defense', 12, 20, 2, (1000, 0, 0, 0), [('b', 'research_lab', 2)]),
 ('weapons', 'weapons', 13, 20, 2, (800, 200, 0, 0), [('b', 'research_lab', 4)]),
 ('espionage', 'exploration', 14, 15, 2, (200, 1000, 200, 0), [('b', 'research_lab', 3)]),
 ('astrophysics', 'exploration', 15, 20, 1.75, (4000, 8000, 4000, 0), [('b', 'research_lab', 3), ('r', 'espionage', 4), ('r', 'impulse_drive', 3)]),
 ('graviton', 'weapons', 16, 10, 3, (0, 0, 0, 300000), [('b', 'research_lab', 12), ('r', 'energy_science', 12), ('r', 'laser', 12), ('r', 'ion', 8)]),
 ('interstellar_diplomacy', 'computer', 17, 8, 2, (5000, 10000, 5000, 0), [('b', 'research_lab', 5), ('r', 'quantum_computing', 4)]),
]
BUILDINGS = [  # code, max, portée, prérequis
 ('planetary_base', 1, 'planet', []),
 ('metal_mine', 50, 'planet', []),
 ('crystal_mine', 50, 'planet', []),
 ('hydrogen_synthesizer', 50, 'planet', []),
 ('solar_plant', 50, 'planet', []),
 ('fusion_plant', 50, 'planet', [('b', 'hydrogen_synthesizer', 5), ('r', 'energy_science', 3)]),
 ('metal_storage', 20, 'planet', []),
 ('crystal_storage', 20, 'planet', []),
 ('hydrogen_storage', 20, 'planet', []),
 ('research_lab', 12, 'planet', []),
 ('robotic_factory', 10, 'both', []),
 ('shipyard', 12, 'both', [('b', 'robotic_factory', 2)]),
 ('nanite_factory', 10, 'planet', [('b', 'robotic_factory', 10), ('r', 'quantum_computing', 10)]),
 ('terraformer', 10, 'planet', [('b', 'nanite_factory', 1), ('r', 'energy_science', 12)]),
 ('repair_dock', 10, 'planet', [('b', 'shipyard', 2)]),
 ('missile_silo', 10, 'planet', [('b', 'shipyard', 1)]),
 ('logistics_center', 10, 'planet', [('r', 'quantum_computing', 2)]),
 ('lunar_base', None, 'moon', []),
 ('sensor_phalanx', None, 'moon', [('b', 'lunar_base', 1)]),
 ('jump_gate', None, 'moon', [('b', 'lunar_base', 1), ('r', 'hyperspace', 7)]),
]
SHIPS = [  # code, type, prérequis, moteur, changements de moteur (niveau de recherche, moteur, vitesse, consommation)
 ('battle_cruiser', 'advanced', [('b', 'shipyard', 12), ('r', 'hyperspace_drive', 7), ('r', 'hyperspace', 6), ('r', 'graviton', 1)], 'hyperspace', []),
 ('battleship', 'military', [('b', 'shipyard', 7), ('r', 'hyperspace_drive', 4)], 'hyperspace', []),
 ('bomber', 'advanced', [('b', 'shipyard', 8), ('r', 'impulse_drive', 6), ('r', 'plasma', 5)], 'impulse', [(8, 'hyperspace', 5000, 700)]),
 ('colony_ship', 'civil', [('b', 'shipyard', 4), ('r', 'impulse_drive', 3), ('r', 'astrophysics', 1)], 'impulse', []),
 ('cruiser', 'military', [('b', 'shipyard', 5), ('r', 'impulse_drive', 4), ('r', 'ion', 2)], 'impulse', []),
 ('destroyer', 'advanced', [('b', 'shipyard', 9), ('r', 'hyperspace_drive', 6), ('r', 'armor', 6)], 'hyperspace', []),
 ('espionage_probe', 'civil', [('b', 'shipyard', 3), ('r', 'combustion_drive', 3), ('r', 'espionage', 2)], 'combustion', []),
 ('heavy_fighter', 'military', [('b', 'shipyard', 3), ('r', 'armor', 2)], 'impulse', []),
 ('large_cargo', 'civil', [('b', 'shipyard', 4), ('r', 'combustion_drive', 6)], 'combustion', []),
 ('light_fighter', 'military', [('b', 'shipyard', 1)], 'combustion', []),
 ('predator', 'advanced', [('b', 'shipyard', 8), ('r', 'hyperspace_drive', 5), ('r', 'laser', 12), ('r', 'ion', 5)], 'hyperspace', []),
 ('recycler', 'civil', [('b', 'shipyard', 4), ('r', 'combustion_drive', 6), ('r', 'shielding', 2)], 'combustion', [(17, 'impulse', 4000, 600), (15, 'hyperspace', 6000, 900)]),
 ('small_cargo', 'civil', [('b', 'shipyard', 2), ('r', 'combustion_drive', 2)], 'combustion', [(5, 'impulse', 10000, 20)]),
 ('solar_satellite', 'advanced', [('b', 'shipyard', 1)], 'combustion', []),
]
DEFENSES = [  # code, type, prérequis
 ('ballistic_projector', 'standard', [('b', 'shipyard', 1)]),
 ('defensive_barrier', 'advanced', [('b', 'shipyard', 1), ('r', 'shielding', 2)]),
 ('high_energy_emitter', 'standard', [('b', 'shipyard', 4), ('r', 'laser', 6), ('r', 'energy_science', 3)]),
 ('interceptors', 'advanced', [('b', 'shipyard', 1), ('b', 'missile_silo', 2)]),
 ('ion_battery', 'standard', [('b', 'shipyard', 4), ('r', 'ion', 4)]),
 ('long_range_warheads', 'advanced', [('b', 'shipyard', 1), ('b', 'missile_silo', 4), ('r', 'impulse_drive', 1)]),
 ('magnetic_accelerator', 'standard', [('b', 'shipyard', 6), ('r', 'weapons', 3), ('r', 'shielding', 1), ('r', 'energy_science', 6)]),
 ('photonic_cannon', 'standard', [('b', 'shipyard', 2), ('r', 'laser', 3)]),
 ('plasma_ejector', 'advanced', [('b', 'shipyard', 8), ('r', 'plasma', 7)]),
 ('protective_dome', 'advanced', [('b', 'shipyard', 6), ('r', 'shielding', 6)]),
]

RES = {r[0]: r for r in RESEARCH}
BLD = {b[0]: b for b in BUILDINGS}

NAMES = {  # code: (FR, EN), noms affichés par le jeu ; vaisseaux : EN provisoire (PLAN §8)
 'energy_science': ('Science Énergétique', 'Energy Science'),
 'plasma': ('Maîtrise du Plasma', 'Plasma Technology'),
 'quantum_computing': ('Calcul Quantique', 'Quantum Computing'),
 'research_network': ('Collaboration Stellaire', 'Stellar Collaboration'),
 'combustion_drive': ('Propulseur Chimique', 'Combustion Drive'),
 'impulse_drive': ('Moteur Magnétique', 'Impulse Drive'),
 'hyperspace_drive': ('Navigation Transdimensionnelle', 'Hyperspace Drive'),
 'laser': ('Systèmes Photoniques', 'Laser Technology'),
 'ion': ('Manipulation Ionique', 'Ion Technology'),
 'hyperspace': ('Pliage Spatial', 'Hyperspace Technology'),
 'shielding': ('Champs de Protection', 'Shielding Technology'),
 'armor': ('Métallurgie Avancée', 'Armor Technology'),
 'weapons': ('Systèmes Offensifs', 'Weapon Systems'),
 'espionage': ('Renseignement Tactique', 'Espionage Technology'),
 'astrophysics': ('Cosmologie Appliquée', 'Astrophysics'),
 'graviton': ('Manipulation Gravitationnelle', 'Graviton Technology'),
 'interstellar_diplomacy': ('Diplomatie Stellaire', 'Stellar Diplomacy'),
 'planetary_base': ('Base planetaire', 'Planetary Base'),
 'metal_mine': ('Excavateur minéral', 'Mineral Excavator'),
 'crystal_mine': ('Extracteur cristallin', 'Crystal Extractor'),
 'hydrogen_synthesizer': ("Condensateur d'hydrogène", 'Hydrogen Condenser'),
 'solar_plant': ('Capteurs photovoltaïques', 'Photovoltaic Sensors'),
 'fusion_plant': ('Réacteur thermonucléaire', 'Thermonuclear Reactor'),
 'metal_storage': ("Dépôt d'alliages", 'Alloy Depot'),
 'crystal_storage': ('Chambre cristalline', 'Crystal Chamber'),
 'hydrogen_storage': ("Citerne d'hydrogène", 'Hydrogen Tank'),
 'shipyard': ('Dock orbital', 'Orbital Dock'),
 'logistics_center': ('Centre logistique', 'Logistics Center'),
 'repair_dock': ('Station de réparation', 'Repair Station'),
 'research_lab': ("Centre d'innovation", 'Innovation Center'),
 'missile_silo': ('Arsenal balistique', 'Ballistic Arsenal'),
 'terraformer': ('Modulateur planétaire', 'Planetary Modulator'),
 'nanite_factory': ('Assembleur moléculaire', 'Molecular Assembler'),
 'robotic_factory': ("Fabrique d'automates", 'Automaton Factory'),
 'lunar_base': ('Base lunaire', 'Lunar base'),
 'sensor_phalanx': ('Phalange de capteur', 'Sensor phalanx'),
 'jump_gate': ('Porte de saut', 'Jump gate'),
 'small_cargo': ('Navette de fret', 'Cargo Shuttle'),
 'large_cargo': ('Cargo stellaire', 'Stellar Freighter'),
 'colony_ship': ('Pionnier spatial', 'Space Pioneer'),
 'recycler': ('Récupérateur', 'Salvager'),
 'espionage_probe': ('Éclaireur', 'Scout'),
 'solar_satellite': ('Collecteur solaire', 'Solar Collector'),
 'light_fighter': ('Intercepteur', 'Interceptor'),
 'heavy_fighter': ('Assaillant', 'Assailant'),
 'cruiser': ('Corvette', 'Corvette'),
 'battleship': ('Cuirassé', 'Battleship'),
 'bomber': ('Frappe-orbital', 'Orbital Striker'),
 'predator': ('Prédateur', 'Predator'),
 'destroyer': ('Annihilateur', 'Annihilator'),
 'battle_cruiser': ('Colossus stellaire', 'Stellar Colossus'),
 'ballistic_projector': ('Projecteur balistique', 'Ballistic Projector'),
 'photonic_cannon': ('Canon photonique', 'Photonic Cannon'),
 'high_energy_emitter': ('Émetteur à haute énergie', 'High-Energy Emitter'),
 'magnetic_accelerator': ('Accélérateur magnétique', 'Magnetic Accelerator'),
 'ion_battery': ('Batterie ionique', 'Ion Battery'),
 'plasma_ejector': ('Éjecteur à plasma', 'Plasma Ejector'),
 'defensive_barrier': ('Barrière défensive', 'Defensive Barrier'),
 'protective_dome': ('Dôme protecteur', 'Protective Dome'),
 'interceptors': ('Intercepteurs', 'Interception Missile'),
 'long_range_warheads': ('Ogives longue portée', 'Long-Range Warheads'),
}
def nm(code, lang): return NAMES[code][0 if lang == 'fr' else 1]
DRIVE_OF = {'combustion': 'combustion_drive', 'impulse': 'impulse_drive', 'hyperspace': 'hyperspace_drive'}
DRIVE_BONUS = {'combustion_drive': 10, 'impulse_drive': 20, 'hyperspace_drive': 30}  # % par niveau, ReactorType::getBonusPerLevel()

# Rubriques de la page Recherche du jeu (front : researchSections.ts, pages/research.json)
SECTIONS = [
 (('Recherche Fondamentale', 'Fundamental Research'), ['energy_science', 'laser', 'ion', 'hyperspace', 'plasma']),
 (('Recherche en Propulsion', 'Propulsion Research'), ['combustion_drive', 'impulse_drive', 'hyperspace_drive']),
 (('Recherche de Combat', 'Combat Research'), ['weapons', 'shielding', 'armor']),
 (('Recherche Stratégique', 'Strategic Research'), ['espionage', 'quantum_computing', 'astrophysics', 'research_network', 'graviton', 'interstellar_diplomacy']),
]

# --- formules (code) ---
def cost(code, L):
    """Research::getCost() : coût niv. 1 × facteur^(N − 1), arrondi à l'inférieur par ressource (énergie comprise)."""
    r = RES[code]
    return tuple(fl(x * r[4] ** (L - 1)) for x in r[5])

def research_seconds(code, L, lab, speed=1):
    """Research::getResearchTime() : (métal + cristal) / (1 000 × (1 + niveau effectif)) h ÷ vitesse, arrondi à la seconde."""
    m, c, h, e = cost(code, L)
    return round((m + c) / (1000 * (1 + lab)) * 3600 / speed)

def hasten(seconds, percent):
    """AllianceBonuses::hasten() : durée × 100 / (100 + bonus), arrondie au supérieur, au moins 1 s."""
    return seconds if percent == 0 else max(1, math.ceil(round(seconds * 100 / (100 + percent), 6)))

def points(code, L):
    m, c, h, e = cost(code, L)
    return (m + c + h) / 1000  # Constructable::getPoints(), énergie exclue

def network_effective(local, others, network_level, tolerance=0, extra=0):
    """ResearchLabContributions::eligible() + ResearchNetwork::effectiveLabLevel(), sans talent de bonus de niveaux."""
    if network_level <= 0 or local <= 0:
        return local, []
    lowest = max(1, local - tolerance)
    kept = sorted([o for o in others if o >= lowest], reverse=True)[: network_level + extra]
    return local + sum(kept), kept

def max_bases(astro): return 1 + (astro + 1) // 2           # UserUniverse::maxBasesForAstrophysics()
def expeditions(astro): return int(math.isqrt(max(0, astro)))  # ExpeditionSlots::forAstrophysics() (hors Premium)
def hold_hours(astro): return max(0, astro)                   # HoldDuration::maxHoursFor()
def fleet_slots(qc): return 1 + qc                            # UserUniverse::getMaxFleets() (hors talents)
ALLIANCE_CAPACITY = {1: 10, 2: 15, 3: 20, 4: 25, 5: 30, 6: 35, 7: 40, 8: 50}  # AllianceCapacity
def missile_range(impulse): return max(-1, impulse * 5 - 1)   # MissileRange::forImpulseDrive()
def spy_fuel_factor(esp): return max(0.5, 1 - esp * 0.05)     # SendFleetHandler (mission espionnage)
PLASMA = (1.00, 0.66, 0.33)  # % par niveau sur la production brute des mines : Base::PLASMA_BONUS_*
def fusion(L, es): return int(30 * L * (1.05 + es * 0.01) ** L)  # Building::getProduction(), Réacteur

# --- prérequis ---
def reqs_of(code):
    if code in RES: return RES[code][6]
    if code in BLD: return BLD[code][3]
    for s in SHIPS:
        if s[0] == code: return s[2]
    for d in DEFENSES:
        if d[0] == code: return d[2]
    raise KeyError(code)

def closure(code):
    """Tout ce qu'il faut atteindre pour débloquer code : {code: niveau}, chaînes comprises."""
    need = {}
    def visit(c):
        for t, rc, lv in reqs_of(c):
            if need.get(rc, 0) < lv:
                need[rc] = lv
            visit(rc)
    visit(code)
    return need

ORDER = [b[0] for b in BUILDINGS] + [r[0] for r in RESEARCH]
def fmt_need(need, lang):
    keys = sorted(need, key=lambda k: (0 if k in BLD else 1, ORDER.index(k)))
    return ', '.join(f'{nm(k, lang)} {need[k]}' for k in keys)
