import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
cap = storage(2) + 10000
hours = cap / 1366
def body(lang):
    N = lambda x: n(x, lang)
    rows = [[l, N(storage(l)), N(1000*2**(l-1)), f'{N(1000*2**(l-1))} / {N(500*2**(l-1))}', f'{N(1000*2**(l-1))} / {N(1000*2**(l-1))}'] for l in range(1,21)]
    H = f'{hours:.1f}'.replace('.', ',') if lang=='fr' else f'{hours:.1f}'
    if lang == 'fr':
        return f'''# Le stockage

> **En bref** : chaque planète stocke ses propres ressources, dans la limite de ses entrepôts. La production remplit les entrepôts jusqu'à leur capacité, jamais au-delà, puis s'arrête jusqu'à ce que vous dépensiez. Ce qui dépasse déjà la capacité reste utilisable.
{{.is-info}}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Dépôt d'alliages"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Chambre cristalline"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Citerne d'hydrogène">

## Règles

1. Chaque planète a une **capacité par ressource** : métal, cristal, hydrogène.
2. La **Base planetaire** fournit **10 000** de capacité pour chaque ressource. Une **lune**, qui n'a ni Base planetaire ni entrepôts, stocke elle aussi 10 000 de chaque ressource.
3. Chaque entrepôt ajoute sa capacité à une ressource : **Dépôt d'alliages** (métal), **Chambre cristalline** (cristal), **Citerne d'hydrogène** (hydrogène). Au niveau N, il contient 5 000 × partie entière(2,5 × e^(20 × N / 33)), jusqu'au niveau 20.
4. La production remplit l'entrepôt **jusqu'à sa capacité, jamais au-delà**. Quand le stock **atteint** la capacité, la **production de cette ressource s'arrête** ; elle reprend dès que le stock repasse en dessous.
5. Un stock **au-dessus** de la capacité reste entièrement utilisable : construction, recherche, chantier, transport.
6. Le **Centre logistique** agrandit la capacité de **10 % par niveau**, jusqu'à +100 % au niveau 10 (voir [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)).
7. Le talent d'alliance **Entrepôts fédérés** ajoute **10 %** de capacité par niveau (2 niveaux), et certains talents de dynastie en ajoutent aussi.
8. Ces bonus **s'additionnent** : ils ne se multiplient pas entre eux. Ils s'appliquent à toute la capacité de la planète, **les 10 000 de la Base planetaire compris**.

## Exemple chiffré

Dépôt d'alliages niveau 2 : 40 000, plus 10 000 de la Base planetaire, soit **{N(cap)} métal**. Avec une production de 1 366 métal par heure, un stock vide est plein en {N(cap)} / 1 366 = **{H} heures**.

Ajoutez un Centre logistique niveau 3 (+30 %) et Entrepôts fédérés niveau 2 (+20 %) :
- Bonus total : 30 % + 20 % = **+50 %** (et non 1,3 × 1,2).
- Capacité en métal : {N(cap)} × 1,5 = **{N(cap*1.5)}**.

## Données détaillées

Capacité d'un entrepôt au niveau N, sans la Base planetaire ni les bonus, et coût pour atteindre ce niveau (métal / cristal) :

{table(['Niveau', 'Capacité', "Dépôt d'alliages (métal)", 'Chambre cristalline', "Citerne d'hydrogène"], rows)}

## Pièges fréquents

- **Un entrepôt plein, c'est de la production perdue** : surveillez la barre de ressources, surtout avant une absence.
- **Un stock important attire les pillards** : voir [Pillage](/fr/combat/plunder).
- **Chaque planète compte à part** : les entrepôts d'une colonie ne servent qu'à elle.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [Liste des bâtiments](/fr/economy/buildings)
- [Formules de l'économie](/fr/economy/formulas)
- [Pillage](/fr/combat/plunder)
'''
    return f'''# Storage

> **In short**: each planet stores its own resources, within the limit of its storage buildings. Production fills storage up to its capacity, never beyond, then stops until you spend some. Whatever is already above capacity stays usable.
{{.is-info}}

<img src="/images/illustrations/buildings/depot-alliages.jpg" width="180" alt="Alloy Depot"> <img src="/images/illustrations/buildings/chambre-cristalline.jpg" width="180" alt="Crystal Chamber"> <img src="/images/illustrations/buildings/citerne-hydrogene.jpg" width="180" alt="Hydrogen Tank">

## Rules

1. Each planet has a **capacity per resource**: metal, crystal, hydrogen.
2. The **Planetary Base** provides **10,000** capacity for each resource. A **moon**, which has neither a Planetary Base nor storage buildings, also holds 10,000 of each resource.
3. Each storage building adds its capacity to one resource: **Alloy Depot** (metal), **Crystal Chamber** (crystal), **Hydrogen Tank** (hydrogen). At level N it holds 5,000 × integer part(2.5 × e^(20 × N / 33)), up to level 20.
4. Production fills storage **up to its capacity, never beyond**. When the stock **reaches** capacity, **production of that resource stops**; it resumes as soon as the stock drops below it.
5. A stock **above** capacity stays fully usable: construction, research, shipyard, transport.
6. The **Logistics Center** enlarges capacity by **10% per level**, up to +100% at level 10 (see [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)).
7. The **Federated warehouses** alliance talent adds **10%** capacity per level (2 levels), and some dynasty talents add more.
8. These bonuses **add up**: they do not multiply each other. They apply to the planet's whole capacity, **the Planetary Base's 10,000 included**.

## Worked example

Alloy Depot level 2: 40,000, plus 10,000 from the Planetary Base, so **{N(cap)} metal**. With an output of 1,366 metal per hour, an empty stock is full in {N(cap)} / 1,366 = **{H} hours**.

Add a level 3 Logistics Center (+30%) and Federated warehouses level 2 (+20%):
- Total bonus: 30% + 20% = **+50%** (not 1.3 × 1.2).
- Metal capacity: {N(cap)} × 1.5 = **{N(cap*1.5)}**.

## Detailed data

Capacity of one storage building at level N, without the Planetary Base or bonuses, and cost to reach that level (metal / crystal):

{table(['Level', 'Capacity', 'Alloy Depot (metal)', 'Crystal Chamber', 'Hydrogen Tank'], rows)}

## Common pitfalls

- **Full storage is lost production**: watch the resource bar, especially before going away.
- **A large stock draws raiders**: see [Plunder](/en/combat/plunder).
- **Each planet counts on its own**: a colony's storage only serves that colony.

## Related pages

- [Resources](/en/economy/resources)
- [Buildings list](/en/economy/buildings)
- [Economy formulas](/en/economy/formulas)
- [Plunder](/en/combat/plunder)
'''
for lang in ('fr','en'): write(lang, 'economy/storage', body(lang))
