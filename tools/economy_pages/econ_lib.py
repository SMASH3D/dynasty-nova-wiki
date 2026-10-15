"""Valeurs et formules de la rubrique Économie, reprises du code du jeu (astro-nova-backend main, 15 octobre 2026 ; sources dans DONNEES §4).

Régénérer une page : python3 tools/economy_pages/p_resources.py tools/economy_pages  (idem p_energy, p_storage, p_buildings, p_formulas, p_rest, p_terra).
Chaque script réécrit le corps des pages FR et EN sans toucher au front matter. Mettre à jour CAT et les formules ici après un rééquilibrage.
"""
import math
fl = math.floor
def tr(v): return int(fl(abs(v))) * (1 if v >= 0 else -1)
def n(x, lang):
    if isinstance(x, float) and not x.is_integer():
        s = f'{x:,.2f}'.rstrip('0').rstrip('.')
    else:
        s = f'{int(x):,}'
    return s.replace(',', ' ').replace('.', ',') if lang == 'fr' else s
def pct(x, lang):
    s = n(x, lang)
    return f'{s} %' if lang == 'fr' else f'{s}%'
# production (speed 1)
def mine(base, L): return tr(base * L * 1.1 ** L)
def h2factor(tmax): return max(0.0, round(1.44 - 0.004 * tmax, 3))
def solar(L, t): return tr(20 * L * 1.1 ** L * (1 + max(0.0, t / 100)))
def fusion(L, es): return tr(30 * L * (1.05 + es * 0.01) ** L)
def satellite(tmax): return max(0, fl(tmax / 4 + 20))
def cost(base, m, L): return [fl(x * m ** (L - 1)) for x in base]
def storage(L): return 5000 * fl(2.5 * math.exp(20 * L / 33))
def btime(total, robo=0, nanite=0, speed=1): return round(total / (2500 * (1 + robo) * 2 ** nanite) * 3600 / speed)
CAT = [  # code, fr, en, cat_fr, cat_en, base(M,C,H,E), factor, max, prereq_fr, prereq_en, scope
 ('planetary_base','Base planetaire / Base Coloniale','Planetary Base / Colonial Base','base','base',(0,0,0,0),None,1,'aucun','none','planète'),
 ('metal_mine','Excavateur minéral','Mineral Excavator','production','production',(60,15,0,0),1.5,50,'aucun','none','planète'),
 ('crystal_mine','Extracteur cristallin','Crystal Extractor','production','production',(48,24,0,0),1.6,50,'aucun','none','planète'),
 ('hydrogen_synthesizer',"Condensateur d'hydrogène",'Hydrogen Condenser','production','production',(225,75,0,0),1.5,50,'aucun','none','planète'),
 ('solar_plant','Capteurs photovoltaïques','Photovoltaic Sensors','énergie','energy',(75,30,0,0),1.5,50,'aucun','none','planète'),
 ('fusion_plant','Réacteur thermonucléaire','Thermonuclear Reactor','énergie','energy',(900,360,180,0),1.8,50,"Condensateur d'hydrogène 5, Science Énergétique 3",'Hydrogen Condenser 5, Energy Science 3','planète'),
 ('metal_storage',"Dépôt d'alliages",'Alloy Depot','stockage','storage',(1000,0,0,0),2,20,'aucun','none','planète'),
 ('crystal_storage','Chambre cristalline','Crystal Chamber','stockage','storage',(1000,500,0,0),2,20,'aucun','none','planète'),
 ('hydrogen_storage',"Citerne d'hydrogène",'Hydrogen Tank','stockage','storage',(1000,1000,0,0),2,20,'aucun','none','planète'),
 ('research_lab',"Centre d'innovation",'Innovation Center','recherche','research',(200,400,200,0),2,12,'aucun','none','planète'),
 ('robotic_factory',"Fabrique d'automates",'Automaton Factory','installation','facility',(400,120,200,0),2,10,'aucun','none','planète et lune'),
 ('shipyard','Dock orbital','Orbital Dock','installation','facility',(400,200,100,0),2,12,"Fabrique d'automates 2",'Automaton Factory 2','planète et lune'),
 ('nanite_factory','Assembleur moléculaire','Molecular Assembler','installation','facility',(1000000,500000,100000,0),2,10,"Fabrique d'automates 10, Calcul Quantique 10",'Automaton Factory 10, Quantum Computing 10','planète'),
 ('repair_dock','Station de réparation','Repair Station','chantier','shipyard',(200,0,50,50),5,10,'Dock orbital 2','Orbital Dock 2','planète'),
 ('terraformer','Modulateur planétaire','Planetary Modulator','ressource','resource',(0,50000,100000,1000),2,10,'Assembleur moléculaire 1, Science Énergétique 12','Molecular Assembler 1, Energy Science 12','planète'),
 ('missile_silo','Arsenal balistique','Ballistic Arsenal','ressource','resource',(20000,20000,1000,0),2,10,'Dock orbital 1','Orbital Dock 1','planète'),
 ('logistics_center','Centre logistique','Logistics Center','ressource','resource',(20000,40000,0,0),2,10,'Calcul Quantique 2','Quantum Computing 2','planète'),
 ('lunar_base','Base lunaire','Lunar base','installation','facility',(20000,40000,20000,0),2,None,'aucun','none','lune'),
 ('sensor_phalanx','Phalange de capteur','Sensor phalanx','installation','facility',(20000,40000,20000,0),2,None,'Base lunaire 1','Lunar base 1','lune'),
 ('jump_gate','Porte de saut','Jump gate','installation','facility',(2000000,4000000,2000000,0),2,None,'Base lunaire 1, Pliage Spatial 7','Lunar base 1, Hyperspace Technology 7','lune'),
]
REPAIR = [0.45,0.48,0.49,0.50,0.51,0.52,0.53,0.53,0.54,0.54]
