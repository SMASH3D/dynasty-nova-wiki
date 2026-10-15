import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
L = range(1, 31)
# exemple
m, c = mine(30, 13), mine(20, 13)
pm, pc = fl(m*2*1.00/100), fl(c*2*0.66/100)
am, ac = fl(m*10/100), fl(c*10/100)
posm = fl(m*35/100)
tm, tc = m+pm+am+posm+20, c+pc+ac+10
ex = dict(m=m, c=c, pm=pm, pc=pc, am=am, ac=ac, posm=posm, tm=tm, tc=tc)
def body(lang):
    N = lambda x: n(x, lang)
    rows = [[l, N(mine(30,l)), N(mine(20,l)), N(mine(10,l))] for l in L]
    hrows = [[f'{t} °C' if lang=='fr' else f'{t}°C', (f'{h2factor(t):.2f}'.replace('.', ',') if lang=='fr' else f'{h2factor(t):.2f}')] for t in range(-120, 161, 20)]
    if lang == 'fr':
        return f'''# Les ressources

> **En bref** : trois ressources se stockent, le métal, le cristal et l'hydrogène. Vos mines les produisent en continu, même quand vous n'êtes pas connecté, et chaque planète a son propre stock. L'énergie, quatrième ressource, ne se stocke pas : elle fait tourner les mines.
{{.is-info}}

> **Paramètre d'univers** : la vitesse d'économie multiplie la production des mines et de la Base planetaire.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Métal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Cristal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogène"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Énergie">

## Règles

1. **Métal** : produit par l'Excavateur minéral, 30 × N × 1,1^N par heure au niveau N.
2. **Cristal** : produit par l'Extracteur cristallin, 20 × N × 1,1^N par heure.
3. **Hydrogène** : produit par le Condensateur d'hydrogène, 10 × N × 1,1^N par heure, multiplié par un **facteur de température** qui vaut 1,44 − 0,004 × la température maximale de la planète. Une planète froide produit davantage ; au-delà de 360 °C, plus rien.
4. **Énergie** : produite par les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires, consommée par les trois mines. Elle ne se stocke pas (voir [L'énergie](/fr/economy/energy)).
5. La **Base planetaire** (Base Coloniale sur une colonie) ajoute **20 métal et 10 cristal par heure**, multipliés par la vitesse d'économie.
6. La production est **continue**, calculée à l'heure et arrondie à l'inférieur. Chaque planète a **son propre stock**, limité par ses entrepôts (voir [Le stockage](/fr/economy/storage)).
7. **Bonus** : ils s'appliquent à la production brute des trois mines et **s'additionnent**, sans se multiplier entre eux :
   - **Maîtrise du Plasma** : +1 % de métal, +0,66 % de cristal et +0,33 % d'hydrogène par niveau ;
   - talent d'alliance **Extraction coordonnée** : +5 % des trois ressources par niveau ;
   - **bonus de position**, sur les colonies seulement : jusqu'à +40 % de cristal en positions 1 à 3, jusqu'à +35 % de métal en positions 6 à 10 (voir [Planètes](/fr/universe/planets)) ;
   - les traits de dynastie et les talents (voir [Dynastie et talents](/fr/dynasty)).
8. Si l'énergie manque, la production des mines, bonus compris, baisse dans la proportion du déficit. Le revenu de la Base planetaire n'est pas touché.
9. **Taux de fonctionnement** : chaque mine se règle par pas de 10 %, de 0 à 100 %. Sa production et sa consommation d'énergie baissent dans la même proportion.
10. La production s'arrête quand le stock d'une ressource atteint sa capacité, pendant le [mode vacances](/fr/players/vacation-mode), sur une planète abandonnée, et quand un univers privé est gelé ou terminé.

## Exemple chiffré

Une colonie en position 8, avec Excavateur minéral 13, Extracteur cristallin 13, Maîtrise du Plasma 2, Extraction coordonnée 2 (+10 %) et assez d'énergie :
- Métal : {N(m)} (Excavateur) + {N(pm)} (Plasma : 2 %) + {N(am)} (alliance : 10 %) + {N(posm)} (position 8 : 35 %) + 20 (Base) = **{N(tm)} par heure**.
- Cristal : {N(c)} (Extracteur) + {N(pc)} (Plasma : 1,32 %) + {N(ac)} (alliance) + 10 (Base) = **{N(tc)} par heure**. La position 8 n'a pas de bonus de cristal.
- Chaque bonus est calculé sur la production brute de la mine et arrondi à l'inférieur.

## Données détaillées

### Production des mines par niveau (par heure, vitesse ×1, sans bonus)

L'hydrogène est donné pour un facteur de température de 1 ; multipliez-le par le facteur de votre planète.

{table(['Niveau', 'Excavateur minéral (métal)', 'Extracteur cristallin (cristal)', "Condensateur d'hydrogène (hydrogène, facteur 1)"], rows)}

### Facteur de température du Condensateur d'hydrogène

{table(['Température maximale', 'Facteur'], hrows)}

## Pièges fréquents

- **L'hydrogène part en fumée** : chaque vol en consomme, aller et retour payés au départ pour la plupart des missions.
- **Un stock plein ne produit plus** : dépensez ou agrandissez vos entrepôts.
- **Le stock est local** : les ressources d'une colonie ne servent pas sur la planète mère, il faut les transporter.
- **La planète mère n'a pas de bonus de position** : pensez-y en choisissant l'emplacement de vos colonies.

## Pages liées

- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Formules de l'économie](/fr/economy/formulas)
- [Planètes : taille, température, type](/fr/universe/planets)
'''
    return f'''# Resources

> **In short**: three resources are stored: metal, crystal and hydrogen. Your mines produce them continuously, even while you are offline, and each planet has its own stock. Energy, the fourth resource, is not stored: it runs the mines.
{{.is-info}}

> **Universe setting**: the economy speed multiplies the output of the mines and of the Planetary Base.
> Default: **×1** · Redline: **×1**
{{.is-info}}

<img src="/images/illustrations/resources/metal.jpg" width="180" alt="Metal"> <img src="/images/illustrations/resources/crystal.jpg" width="180" alt="Crystal"> <img src="/images/illustrations/resources/hydrogene.jpg" width="180" alt="Hydrogen"> <img src="/images/illustrations/resources/energy.jpg" width="180" alt="Energy">

## Rules

1. **Metal**: produced by the Mineral Excavator, 30 × N × 1.1^N per hour at level N.
2. **Crystal**: produced by the Crystal Extractor, 20 × N × 1.1^N per hour.
3. **Hydrogen**: produced by the Hydrogen Condenser, 10 × N × 1.1^N per hour, multiplied by a **temperature factor** of 1.44 − 0.004 × the planet's maximum temperature. A cold planet produces more; above 360°C, nothing at all.
4. **Energy**: produced by the Photovoltaic Sensors, the Thermonuclear Reactor and Solar Collectors, used by the three mines. It is not stored (see [Energy](/en/economy/energy)).
5. The **Planetary Base** (Colonial Base on a colony) adds **20 metal and 10 crystal per hour**, multiplied by the economy speed.
6. Production is **continuous**, computed per hour and rounded down. Each planet has **its own stock**, limited by its storage (see [Storage](/en/economy/storage)).
7. **Bonuses**: they apply to the gross output of the three mines and **add up**, without multiplying each other:
   - **Plasma Technology**: +1% metal, +0.66% crystal and +0.33% hydrogen per level;
   - **Coordinated extraction** alliance talent: +5% of all three resources per level;
   - **position bonus**, on colonies only: up to +40% crystal at positions 1 to 3, up to +35% metal at positions 6 to 10 (see [Planets](/en/universe/planets));
   - dynasty traits and talents (see [Dynasty and talents](/en/dynasty)).
8. When energy runs short, the mines' output, bonuses included, drops in proportion to the deficit. The Planetary Base's income is not affected.
9. **Operating rate**: each mine is set in steps of 10%, from 0 to 100%. Its output and its energy use drop in the same proportion.
10. Production stops when a resource's stock reaches its capacity, during [vacation mode](/en/players/vacation-mode), on an abandoned planet, and while a private universe is frozen or finished.

## Worked example

A colony at position 8, with Mineral Excavator 13, Crystal Extractor 13, Plasma Technology 2, Coordinated extraction 2 (+10%) and enough energy:
- Metal: {N(m)} (Excavator) + {N(pm)} (Plasma: 2%) + {N(am)} (alliance: 10%) + {N(posm)} (position 8: 35%) + 20 (Base) = **{N(tm)} per hour**.
- Crystal: {N(c)} (Extractor) + {N(pc)} (Plasma: 1.32%) + {N(ac)} (alliance) + 10 (Base) = **{N(tc)} per hour**. Position 8 has no crystal bonus.
- Each bonus is computed on the mine's gross output and rounded down.

## Detailed data

### Mine output per level (per hour, speed ×1, no bonus)

Hydrogen is given for a temperature factor of 1; multiply it by your planet's factor.

{table(['Level', 'Mineral Excavator (metal)', 'Crystal Extractor (crystal)', 'Hydrogen Condenser (hydrogen, factor 1)'], rows)}

### Hydrogen Condenser temperature factor

{table(['Maximum temperature', 'Factor'], hrows)}

## Common pitfalls

- **Hydrogen goes up in smoke**: every flight burns some, with the return trip paid at departure for most missions.
- **A full stock stops producing**: spend it or enlarge your storage.
- **Stock is local**: a colony's resources cannot be used on the home planet; they have to be transported.
- **The home planet has no position bonus**: keep it in mind when picking where to settle your colonies.

## Related pages

- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Economy formulas](/en/economy/formulas)
- [Planets: size, temperature, type](/en/universe/planets)
'''
for lang in ('fr', 'en'): write(lang, 'economy/resources', body(lang))
print(ex)
