"""Valeurs et règles de la rubrique Joueurs, reprises du code du jeu (astro-nova-backend main 7b255c83, 15 octobre 2026 ; sources dans DONNEES, section « Joueurs (code, 15 octobre 2026) »).

Régénérer une page : python3 tools/players_pages/p_rankings.py tools/players_pages  (idem p_index, p_beginner, p_attack, p_vacation, p_inactivity, p_messages).
Chaque script réécrit le corps des pages FR et EN sans toucher au front matter (sauf titre ou description passés à write()).
Mettre à jour les constantes ici après un changement de règle.
"""
import math

# Classements (Constructable::getPoints, RankingCategory, Point::rounded)
POINT_DIVISOR = 1000                       # 1 point = 1 000 ressources du coût catalogue
# Protection des débutants (BeginnerProtection::default)
TIERS = [(500, 3), (5_000, 5), (500_000, 10)]
INACTIVITY_DEFAULT, INACTIVITY_REDLINE = 14, 7
# Protection nouvel arrivant (NewcomerProtection::DURATION_DAYS), constante, pas un paramètre d'univers
NEWCOMER_DAYS = 7
# Limite d'attaques (BashingRule::default, AttackTally : tranche fixe)
BASH_MAX, BASH_WINDOW_H = 6, 24
BASH_REDLINE = (6, 24)
# Mode vacances (VacationMode::MINIMUM_HOURS)
VACATION_MIN_H = 48
# Succession du fondateur (config/services.yaml alliance_succession_*)
FOUNDER_ALERTS, FOUNDER_LOSS_DAYS = (7, 12), 14
# Messagerie et rapports (config/services.yaml, MessageBody, SpamPolicy)
REPORT_RETENTION_D = 7
ALLIANCE_CHAT_D = 30
SHARED_GRACE_D = 7
CHAT_MAX_CHARS = 500
SPAM_MAX, SPAM_WINDOW_S = 5, 60
PINS_MAX = 3

def n(x, lang, dec=2):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.{dec}f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s

def cost(base, factor, level):
    """Coût d'un niveau de bâtiment ou de recherche : base × facteur^(niveau − 1), arrondi par défaut."""
    return [math.floor(b * factor ** (level - 1)) for b in base]

def points(m, c, h):
    return (m + c + h) / POINT_DIVISOR

def tier_of(p, tiers=TIERS):
    for up, ratio in tiers:
        if p < up:
            return (up, ratio)
    return None

def blocks(a, b, inactive_defender=False, tiers=TIERS):
    """BeginnerProtection::blocksAttack, points arrondis à l'entier inférieur."""
    if inactive_defender:
        return False
    weak, strong = min(a, b), max(a, b)
    t = tier_of(weak, tiers)
    if t is None:
        return False
    if weak <= 0:
        return strong > 0
    return strong >= weak * t[1]

class Tally:
    """AttackTally : une ligne par couple attaquant/défenseur, tranche fixe ouverte par la première attaque."""
    def __init__(self):
        self.count, self.start = 0, None
    def attack(self, t):
        if self.start is None or t >= self.start + BASH_WINDOW_H:
            self.start, self.count = t, 0
        if self.count >= BASH_MAX:
            return False
        self.count += 1
        return True
    def refund(self):
        self.count = max(0, self.count - 1)
    def remaining(self, t):
        if self.start is None or t >= self.start + BASH_WINDOW_H:
            return BASH_MAX
        return BASH_MAX - self.count

# Coûts catalogue (MySQL de dev migré, tables ship et defense, colonne base_cost, 15 octobre 2026)
SHIPS = [  # code, FR (jeu), EN (provisoire, PLAN §8), métal, cristal, hydrogène
 ('small_cargo', 'Navette de fret', 'Cargo Shuttle', 2000, 2000, 0),
 ('large_cargo', 'Cargo stellaire', 'Stellar Freighter', 6000, 6000, 0),
 ('colony_ship', 'Pionnier spatial', 'Space Pioneer', 10000, 20000, 10000),
 ('recycler', 'Récupérateur', 'Salvager', 10000, 6000, 2000),
 ('espionage_probe', 'Éclaireur', 'Scout', 0, 1000, 0),
 ('solar_satellite', 'Collecteur solaire', 'Solar Collector', 0, 2000, 500),
 ('light_fighter', 'Intercepteur', 'Interceptor', 3000, 1000, 0),
 ('heavy_fighter', 'Assaillant', 'Assailant', 6000, 4000, 0),
 ('cruiser', 'Corvette', 'Corvette', 20000, 7000, 2000),
 ('battleship', 'Cuirassé', 'Battleship', 45000, 15000, 0),
 ('bomber', 'Frappe-orbital', 'Orbital Striker', 50000, 25000, 15000),
 ('predator', 'Prédateur', 'Predator', 30000, 40000, 15000),
 ('destroyer', 'Annihilateur', 'Annihilator', 60000, 50000, 15000),
 ('battle_cruiser', 'Colossus stellaire', 'Stellar Colossus', 5000000, 4000000, 1000000),
]
DEFENSES = [
 ('ballistic_projector', 'Projecteur balistique', 'Ballistic Projector', 2000, 0, 0),
 ('photonic_cannon', 'Canon photonique', 'Photonic Cannon', 1500, 500, 0),
 ('high_energy_emitter', 'Émetteur à haute énergie', 'High-Energy Emitter', 6000, 2000, 0),
 ('ion_battery', 'Batterie ionique', 'Ion Battery', 2000, 6000, 0),
 ('magnetic_accelerator', 'Accélérateur magnétique', 'Magnetic Accelerator', 20000, 15000, 2000),
 ('plasma_ejector', 'Éjecteur à plasma', 'Plasma Ejector', 50000, 50000, 30000),
 ('defensive_barrier', 'Barrière défensive', 'Defensive Barrier', 10000, 10000, 0),
 ('protective_dome', 'Dôme protecteur', 'Protective Dome', 50000, 50000, 0),
 ('interceptors', 'Intercepteurs', 'Interception Missile', 8000, 2000, 0),
 ('long_range_warheads', 'Ogives longue portée', 'Long-Range Warheads', 12500, 2500, 10000),
]
METAL_MINE = ((60, 15, 0), 1.5)  # Excavateur minéral, table building

def setting_box(lang, what, default, redline):
    if lang == 'fr':
        return f'> **Paramètre d\'univers** : {what}\n> Par défaut : {default} · Redline : {redline}\n{{.is-info}}'
    return f'> **Universe setting**: {what}\n> Default: {default} · Redline: {redline}\n{{.is-info}}'
