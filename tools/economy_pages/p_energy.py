import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
sp = solar(13, 10); cons = mine(10,13)*2 + mine(10,10)
ratio = min(100.0, sp / cons * 100)
m = mine(30, 13); mr = fl(m * ratio / 100)
ex = dict(sp=sp, cons=cons, ratio=ratio, m=m, mr=mr)
def body(lang):
    N = lambda x: n(x, lang)
    deg = (lambda t: f'{t} °C') if lang=='fr' else (lambda t: f'{t}°C')
    rows = [[l, N(mine(10,l)), N(solar(l,0))] for l in range(1,31)]
    frows = [[l] + [N(fusion(l, es)) for es in (3,6,9,12)] + [N(mine(10,l))] for l in range(1,21)]
    srows = [[deg(t), N(satellite(t))] for t in range(-120, 161, 20)]
    R = f'{ratio:.1f}'.replace('.', ',') if lang=='fr' else f'{ratio:.1f}'
    if lang == 'fr':
        return f'''# L'énergie

> **En bref** : vos mines consomment de l'énergie, vos centrales en produisent. Tant que la production couvre la consommation, tout tourne à plein régime. Dès qu'elle ne suffit plus, **les trois mines** ralentissent dans la même proportion. L'énergie ne se stocke pas.
{{.is-info}}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Capteurs photovoltaïques"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Réacteur thermonucléaire"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Collecteur solaire">

## Règles

1. **Capteurs photovoltaïques** : 20 × N × 1,1^N énergie au niveau N, multipliés par 1 + température actuelle / 100 quand la température actuelle de la planète est positive. La température actuelle suit le mois du calendrier (voir [Planètes](/fr/universe/planets)).
2. **Réacteur thermonucléaire** : 30 × N × (1,05 + 0,01 × Science Énergétique)^N énergie, en **consommant de l'hydrogène** : 10 × N × 1,1^N par heure, multipliés par la vitesse d'économie de l'univers.
3. **Collecteur solaire** : vaisseau qui reste en orbite et produit, chacun, température maximale / 4 + 20 énergie, arrondi à l'inférieur et jamais négatif. Il peut être détruit en combat.
4. **Consommation** : l'Excavateur minéral, l'Extracteur cristallin et le Condensateur d'hydrogène consomment chacun 10 × N × 1,1^N énergie. La vitesse d'économie ne change pas la consommation.
5. **Déficit** : si la consommation dépasse la production, la production des trois mines, bonus compris, est multipliée par production / consommation. Le détail de production affiche une ligne « Déficit d'énergie ». Le revenu de la Base planetaire n'est pas touché.
6. **Taux de fonctionnement** : chaque mine se règle par pas de 10 % ; production et consommation baissent ensemble. Le Réacteur, lui, tourne toujours à plein, sauf talent qui le permet.
7. L'énergie **ne se stocke pas** : elle se calcule à chaque instant.
8. Certains bâtiments et recherches demandent une **énergie requise** pour être lancés (Station de réparation, Modulateur planétaire, Manipulation Gravitationnelle) : c'est un seuil de production, pas une dépense.

## Exemple chiffré

Capteurs photovoltaïques 13 un jour à 10 °C, Excavateur minéral 13, Extracteur cristallin 13, Condensateur d'hydrogène 10 :
- Production : 20 × 13 × 1,1^13 × 1,1 = **{N(sp)}** énergie.
- Consommation : {N(mine(10,13))} + {N(mine(10,13))} + {N(mine(10,10))} = **{N(cons)}**.
- Couverture : {N(sp)} / {N(cons)} = **{R} %**. L'Excavateur, qui devrait produire {N(m)} métal par heure, n'en produit plus que **{N(mr)}**.
- Monter une mine d'un niveau aggraverait le déficit : il vaut mieux monter les Capteurs.

**Collecteurs solaires** : sur une planète dont la température maximale est de 60 °C, chacun produit 60 / 4 + 20 = **35** énergie ; 10 Collecteurs en produisent **350**.

## Données détaillées

### Consommation des mines et production des Capteurs

Les Capteurs sont donnés à 0 °C ou moins ; à une température actuelle T positive, multipliez par 1 + T / 100.

{table(['Niveau', 'Consommation de chaque mine', 'Capteurs photovoltaïques (0 °C)'], rows)}

### Réacteur thermonucléaire

{table(['Niveau', 'Énergie (Science Énergétique 3)', 'Énergie (6)', 'Énergie (9)', 'Énergie (12)', 'Hydrogène consommé par heure (vitesse ×1)'], frows)}

### Collecteur solaire

{table(['Température maximale', 'Énergie par Collecteur'], srows)}

## Pièges fréquents

- **Une mine de plus peut faire baisser la production totale** : sans centrale correspondante, le déficit ralentit les trois mines.
- **La production solaire bouge dans le mois** : la température actuelle varie, et avec elle les Capteurs. Gardez une marge.
- **Les Collecteurs solaires sont vulnérables** : ils peuvent être détruits en combat.
- **Le Réacteur coûte de l'hydrogène** : sa consommation est retirée de votre production d'hydrogène.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Formules de l'économie](/fr/economy/formulas)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Liste des vaisseaux](/fr/fleet/ships)
'''
    return f'''# Energy

> **In short**: your mines use energy, your power plants produce it. As long as production covers consumption, everything runs at full speed. As soon as it falls short, **all three mines** slow down in the same proportion. Energy is not stored.
{{.is-info}}

<img src="/images/illustrations/buildings/capteurs-photovoltaiques.jpg" width="180" alt="Photovoltaic Sensors"> <img src="/images/illustrations/buildings/reacteur-thermonucleaire.jpg" width="180" alt="Thermonuclear Reactor"> <img src="/images/illustrations/ships/collecteur-solaire.jpg" width="180" alt="Solar Collector">

## Rules

1. **Photovoltaic Sensors**: 20 × N × 1.1^N energy at level N, multiplied by 1 + current temperature / 100 when the planet's current temperature is positive. The current temperature follows the calendar month (see [Planets](/en/universe/planets)).
2. **Thermonuclear Reactor**: 30 × N × (1.05 + 0.01 × Energy Science)^N energy, **burning hydrogen**: 10 × N × 1.1^N per hour, multiplied by the universe's economy speed.
3. **Solar Collector**: a ship that stays in orbit and produces, each, maximum temperature / 4 + 20 energy, rounded down and never negative. It can be destroyed in combat.
4. **Consumption**: the Mineral Excavator, the Crystal Extractor and the Hydrogen Condenser each use 10 × N × 1.1^N energy. The economy speed does not change consumption.
5. **Deficit**: when consumption exceeds production, the three mines' output, bonuses included, is multiplied by production / consumption. The production breakdown shows an "Energy deficit" line. The Planetary Base's income is not affected.
6. **Operating rate**: each mine is set in steps of 10%; output and consumption drop together. The Reactor always runs at full power, unless a talent allows otherwise.
7. Energy is **never stored**: it is computed at every moment.
8. Some buildings and research need a **required energy** to be started (Repair Station, Planetary Modulator, Graviton Technology): it is a production threshold, not a cost.

## Worked example

Photovoltaic Sensors 13 on a 10°C day, Mineral Excavator 13, Crystal Extractor 13, Hydrogen Condenser 10:
- Production: 20 × 13 × 1.1^13 × 1.1 = **{N(sp)}** energy.
- Consumption: {N(mine(10,13))} + {N(mine(10,13))} + {N(mine(10,10))} = **{N(cons)}**.
- Coverage: {N(sp)} / {N(cons)} = **{R}%**. The Excavator, which should produce {N(m)} metal per hour, only produces **{N(mr)}**.
- Raising a mine one level would deepen the deficit: better raise the Sensors.

**Solar Collectors**: on a planet with a maximum temperature of 60°C, each produces 60 / 4 + 20 = **35** energy; 10 Collectors produce **350**.

## Detailed data

### Mine consumption and Sensors output

Sensors are given at 0°C or below; at a positive current temperature T, multiply by 1 + T / 100.

{table(['Level', 'Consumption of each mine', 'Photovoltaic Sensors (0°C)'], rows)}

### Thermonuclear Reactor

{table(['Level', 'Energy (Energy Science 3)', 'Energy (6)', 'Energy (9)', 'Energy (12)', 'Hydrogen burned per hour (speed ×1)'], frows)}

### Solar Collector

{table(['Maximum temperature', 'Energy per Collector'], srows)}

## Common pitfalls

- **One more mine level can lower total output**: without a matching power plant, the deficit slows all three mines.
- **Solar output moves during the month**: the current temperature varies, and the Sensors with it. Keep a margin.
- **Solar Collectors are vulnerable**: they can be destroyed in combat.
- **The Reactor costs hydrogen**: what it burns is taken off your hydrogen output.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Economy formulas](/en/economy/formulas)
- [Planets: size, temperature, type](/en/universe/planets)
- [Ships list](/en/fleet/ships)
'''
for lang in ('fr','en'): write(lang, 'economy/energy', body(lang))
print(ex)
