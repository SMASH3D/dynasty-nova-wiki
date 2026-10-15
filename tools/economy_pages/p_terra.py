import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
def fields(L): return 5*L + L//2
def body(l):
    N = lambda x: n(x, l); fr = l=='fr'
    trows = []
    for L in range(1,11):
        m,c,h,e = cost((0,50000,100000,1000),2,L)
        add = fields(L)-fields(L-1)
        trows.append([L, N(c), N(h), N(e), f'+{add}', f'+{add-1}', N(fields(L))])
    lrows = []
    for L in range(1,11):
        m,c = cost((20000,40000),2,L)
        lrows.append([L, N(m), N(c), (f'+{L*10} %' if fr else f'+{L*10}%')])
    c4 = sum(cost((0,50000,100000,1000),2,L)[1] for L in range(1,5)); h4 = sum(cost((0,50000,100000,1000),2,L)[2] for L in range(1,5))
    T = table(['Niveau','Cristal','Hydrogène','Énergie requise','Cases ajoutées','Gain net','Cases ajoutées au total'] if fr else ['Level','Crystal','Hydrogen','Required energy','Fields added','Net gain','Total fields added'], trows)
    LT = table(['Niveau','Métal','Cristal','Bonus de stockage'] if fr else ['Level','Metal','Crystal','Storage bonus'], lrows)
    if fr: return f'''# Modulateur planétaire et Centre logistique

> **En bref** : deux bâtiments pour aller plus loin sur une planète. Le **Modulateur planétaire** ajoute des cases quand la planète est pleine. Le **Centre logistique** agrandit toute la capacité de stockage de 10 % par niveau.
{{.is-info}}

<img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="180" alt="Modulateur planétaire"> <img src="/images/illustrations/facilities/centre-logistique.jpg" width="180" alt="Centre logistique">

## Règles

### Modulateur planétaire
1. Prérequis : **Assembleur moléculaire 1** et **Science Énergétique 12**. Niveau maximum : 10. Planètes seulement.
2. Chaque niveau ajoute **5 cases**, plus **1 case aux niveaux pairs**. Le Modulateur occupe lui-même une case par niveau : le gain net est de 4 cases aux niveaux impairs et de 5 aux niveaux pairs. Certains talents ajoutent une case de plus par niveau.
3. Coût du niveau 1 : **50 000 cristal et 100 000 hydrogène**, sans métal. Le coût double à chaque niveau.
4. Il demande aussi une **énergie requise** : 1 000 au niveau 1, doublée à chaque niveau. Elle n'est pas consommée : la production d'énergie de la planète doit simplement atteindre ce seuil au lancement.
5. Une planète **pleine** accepte toujours une montée de niveau du Modulateur, puisque c'est le seul moyen de libérer de la place.

### Centre logistique
6. Prérequis : **Calcul Quantique 2**. Niveau maximum : 10. Planètes seulement.
7. Chaque niveau agrandit la capacité de stockage de la planète de **10 %**, Base planetaire comprise : +100 % au niveau 10. Ce bonus s'additionne à ceux d'alliance et de talents (voir [Le stockage](/fr/economy/storage)).
8. Coût du niveau 1 : **20 000 métal et 40 000 cristal**. Le coût double à chaque niveau.

## Exemple chiffré

**Modulateur planétaire niveau 4** sur une planète de 163 cases
- Cases ajoutées : 5 + 6 + 5 + 6 = **22**. Le Modulateur en occupe 4 : **18 cases** de plus pour vos autres bâtiments, soit 185 cases au total.
- Coût total des 4 niveaux : {N(c4)} cristal et {N(h4)} hydrogène. Énergie requise pour lancer le niveau 4 : 8 000.

**Centre logistique niveau 3** avec un Dépôt d'alliages niveau 2 (40 000) et la Base planetaire (10 000)
- Bonus : +30 % sur 50 000, soit **65 000 métal**.

## Données détaillées

### Modulateur planétaire

{T}

### Centre logistique

{LT}

## Pièges fréquents

- **Le Modulateur coûte surtout de l'hydrogène** : 100 000 dès le niveau 1, puis le double à chaque niveau. Une planète froide le finance plus facilement.
- **L'énergie requise grimpe vite** : 512 000 au niveau 10. Prévoyez vos centrales.
- **Le Modulateur prend aussi de la place** : comptez le gain net, pas les cases ajoutées.

## Pages liées

- [Planètes : taille, température, type](/fr/universe/planets)
- [Le stockage](/fr/economy/storage)
- [Liste des bâtiments](/fr/economy/buildings)
- [L'énergie](/fr/economy/energy)
'''
    return f'''# Planetary Modulator and Logistics Center

> **In short**: two buildings to go further on a planet. The **Planetary Modulator** adds fields once the planet is full. The **Logistics Center** enlarges the whole storage capacity by 10% per level.
{{.is-info}}

<img src="/images/illustrations/facilities/modulateur-planetaire.jpg" width="180" alt="Planetary Modulator"> <img src="/images/illustrations/facilities/centre-logistique.jpg" width="180" alt="Logistics Center">

## Rules

### Planetary Modulator
1. Requirements: **Molecular Assembler 1** and **Energy Science 12**. Maximum level: 10. Planets only.
2. Each level adds **5 fields**, plus **1 field at even levels**. The Modulator itself takes one field per level: the net gain is 4 fields at odd levels and 5 at even levels. Some talents add one more field per level.
3. Level 1 cost: **50,000 crystal and 100,000 hydrogen**, no metal. The cost doubles at each level.
4. It also needs a **required energy**: 1,000 at level 1, doubled at each level. It is not used up: the planet's energy production simply has to reach that threshold when the construction starts.
5. A **full** planet always accepts a Modulator upgrade, since it is the only way to free up room.

### Logistics Center
6. Requirement: **Quantum Computing 2**. Maximum level: 10. Planets only.
7. Each level enlarges the planet's storage capacity by **10%**, Planetary Base included: +100% at level 10. This bonus adds to the alliance and talent bonuses (see [Storage](/en/economy/storage)).
8. Level 1 cost: **20,000 metal and 40,000 crystal**. The cost doubles at each level.

## Worked example

**Planetary Modulator level 4** on a 163-field planet
- Fields added: 5 + 6 + 5 + 6 = **22**. The Modulator takes 4: **18 more fields** for your other buildings, 185 fields in all.
- Total cost of the 4 levels: {N(c4)} crystal and {N(h4)} hydrogen. Required energy to start level 4: 8,000.

**Logistics Center level 3** with an Alloy Depot level 2 (40,000) and the Planetary Base (10,000)
- Bonus: +30% on 50,000, so **65,000 metal**.

## Detailed data

### Planetary Modulator

{T}

### Logistics Center

{LT}

## Common pitfalls

- **The Modulator costs mostly hydrogen**: 100,000 from level 1, then twice as much at each level. A cold planet pays for it more easily.
- **Required energy climbs fast**: 512,000 at level 10. Plan your power plants.
- **The Modulator takes room too**: count the net gain, not the fields added.

## Related pages

- [Planets: size, temperature, type](/en/universe/planets)
- [Storage](/en/economy/storage)
- [Buildings list](/en/economy/buildings)
- [Energy](/en/economy/energy)
'''
for l in ('fr','en'): write(l, 'economy/terraformer-and-logistics', body(l))
