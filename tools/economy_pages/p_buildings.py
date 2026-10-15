import sys, re; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
src = (ROOT/'fr'/'economy'/'buildings.md').read_text()
IMG = {}
for c in CAT:
    name = c[1].split(' / ')[0]
    m = re.search(r'<img src="([^"]+)" width="48" alt="' + re.escape(name), src)
    IMG[c[0]] = m.group(1) if m else None
missing = [k for k,v in IMG.items() if not v]; print('sans image', missing)
ROLE = {
 'planetary_base': ("Cœur de la planète : 10 000 de stockage par ressource, 20 métal et 10 cristal par heure", "Heart of the planet: 10,000 storage per resource, 20 metal and 10 crystal per hour"),
 'metal_mine': ('Produit le métal', 'Produces metal'),
 'crystal_mine': ('Produit le cristal', 'Produces crystal'),
 'hydrogen_synthesizer': ("Produit l'hydrogène, davantage sur une planète froide", 'Produces hydrogen, more on a cold planet'),
 'solar_plant': ("Produit l'énergie, davantage par temps chaud", 'Produces energy, more in hot weather'),
 'fusion_plant': ("Produit de l'énergie en consommant de l'hydrogène", 'Produces energy by burning hydrogen'),
 'metal_storage': ('Stocke le métal', 'Stores metal'),
 'crystal_storage': ('Stocke le cristal', 'Stores crystal'),
 'hydrogen_storage': ("Stocke l'hydrogène", 'Stores hydrogen'),
 'research_lab': ('Permet la recherche et la rend plus rapide', 'Enables research and speeds it up'),
 'robotic_factory': ('Accélère la construction des bâtiments', 'Speeds up building construction'),
 'shipyard': ('Construit vaisseaux et défenses, et les construit plus vite à chaque niveau', 'Builds ships and defenses, faster at each level'),
 'nanite_factory': ('Divise par deux, à chaque niveau, la durée des bâtiments, des vaisseaux et des défenses', 'Halves, at each level, the time of buildings, ships and defenses'),
 'repair_dock': ('Récupère une part des vaisseaux perdus en défense', 'Recovers a share of the ships lost in defense'),
 'terraformer': ('Ajoute des cases à la planète', 'Adds fields to the planet'),
 'missile_silo': ('Stocke les missiles', 'Stores missiles'),
 'logistics_center': ('Agrandit les entrepôts de 10 % par niveau', 'Enlarges storage by 10% per level'),
 'lunar_base': ('Rend la surface de la lune constructible : chaque niveau ouvre 3 cases et en occupe 1', "Makes the moon's surface buildable: each level opens 3 fields and takes 1"),
 'sensor_phalanx': ('Repère les flottes autour d\'une planète', 'Spots fleets around a planet'),
 'jump_gate': ('Saut instantané entre deux lunes', 'Instant jump between two moons'),
}
SCOPE_EN = {'planète':'planet','planète et lune':'planet and moon','lune':'moon'}
c13, c14 = cost((60,15,0),1.5,13), cost((60,15,0),1.5,14)
t14 = btime(sum(c14), robo=4)
def body(lang):
    N = lambda x: n(x, lang)
    fr = lang == 'fr'
    rows = []
    for c in CAT:
        code, nfr, nen, cfr, cen, base, fac, mx, pfr, pen, sc = c
        name = nfr if fr else nen
        img = f'<img src="{IMG[code]}" width="48" alt="{name}"> ' if IMG[code] else ''
        m_, c_, h_, e_ = base
        cost1 = f'{N(m_)} / {N(c_)} / {N(h_)}' + (f' · {N(e_)} {"énergie requise" if fr else "required energy"}' if e_ else '')
        if code == 'planetary_base': cost1 = 'donnée à la fondation' if fr else 'given at founding'
        f = '' if fac is None or code=='planetary_base' else (str(fac).replace('.', ',') if fr else str(fac))
        if code == 'repair_dock': f += (' (énergie requise : 2,5)' if fr else ' (required energy: 2.5)')
        rows.append([img + name, cfr if fr else cen, ROLE[code][0 if fr else 1], cost1, f, (N(mx) if mx else ('aucun' if fr else 'none')), pfr if fr else pen, sc if fr else SCOPE_EN[sc]])
    hdr = ['Bâtiment','Catégorie','Rôle','Coût du niveau 1 (métal / cristal / hydrogène)','Facteur','Niveau max','Prérequis','Où'] if fr else ['Building','Category','Role','Level 1 cost (metal / crystal / hydrogen)','Factor','Max level','Requirements','Where']
    T = table(hdr, rows)
    pts = (sum(c14)) / 1000
    P = f'{pts:.1f}'.replace('.', ',') if fr else f'{pts:.1f}'
    if fr:
        return f'''# Liste des bâtiments

> **En bref** : une planète compte jusqu'à 17 bâtiments. Une lune en accueille 5 : ses 3 bâtiments lunaires, plus la Fabrique d'automates et le Dock orbital. Les mines produisent les ressources, les centrales l'énergie, les entrepôts stockent, et les installations ouvrent la recherche, les vaisseaux, les défenses et les missiles. Chaque niveau de bâtiment occupe une case.
{{.is-info}}

> **Paramètre d'univers** : la vitesse de construction divise la durée de construction des bâtiments.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

## Règles

1. Un bâtiment se construit **niveau par niveau**. Le coût du niveau N vaut le coût du niveau 1 × facteur^(N − 1), arrondi à l'inférieur pour chaque ressource (voir [Formules de l'économie](/fr/economy/formulas)).
2. **Chaque niveau occupe une case** de la planète. Exceptions : la Base planetaire (une case, niveau unique) et la Station de réparation, qui n'en occupe aucune.
3. Un ennemi ne peut **jamais détruire vos bâtiments**. Seul leur propriétaire peut les démolir (voir [Démolir un bâtiment](/fr/economy/demolition)) ; seule la destruction d'une lune emporte les bâtiments de cette lune.
4. Un bâtiment est **payé au lancement** de sa construction, pas à sa mise en file.
5. **Points** : chaque niveau rapporte 1 point par tranche de 1 000 ressources dépensées (métal, cristal et hydrogène), comptés dans les points d'économie.
6. Chaque bâtiment a un **niveau maximum**, sauf les bâtiments lunaires, limités par la place sur la lune.
7. La **Base planetaire** (Base Coloniale sur une colonie) est présente dès la fondation et ne peut pas être démolie.
8. Certains bâtiments demandent une **énergie requise** : la production d'énergie de la planète doit atteindre ce seuil au lancement de la construction, rien n'est consommé.
9. **Sur une lune** : la Base lunaire, la Phalange de capteur et la Porte de saut, plus la Fabrique d'automates et le Dock orbital, aux mêmes coûts et avec les mêmes prérequis que sur une planète. Une lune démarre avec 1 case ; chaque niveau de Base lunaire en ouvre 3 et en occupe 1, sans dépasser ce que permet le diamètre de la lune.

## Exemple chiffré

Faire passer l'Excavateur minéral du niveau 13 au niveau 14 :
- Coût : 60 × 1,5^13 = **{N(c14[0])} métal** et 15 × 1,5^13 = **{N(c14[1])} cristal**, soit {N(sum(c14))} ressources et **{P} points** d'économie.
- La production passe de {N(mine(30,13))} à **{N(mine(30,14))} métal par heure**, la consommation d'énergie de {N(mine(10,13))} à **{N(mine(10,14))}**.
- Durée avec une Fabrique d'automates niveau 4 : {N(sum(c14))} / (2 500 × 5) heures, soit **{N(t14)} secondes** (1 h 10 min).

## Données détaillées

{T}

Le coût du niveau N se calcule avec le facteur : par exemple, le Dock orbital niveau 5 coûte 400 × 2^4 = 6 400 métal, 3 200 cristal et 1 600 hydrogène. Le coût, l'énergie et la production de chaque niveau sont dans l'[annexe : les bâtiments niveau par niveau](/fr/economy/building-levels).

## Pièges fréquents

- **Mines et énergie vont ensemble** : chaque niveau de mine consomme plus d'énergie. Sans centrale suffisante, toute la production ralentit (voir [L'énergie](/fr/economy/energy)).
- **Les cases sont limitées** : chaque niveau en occupe une. Pensez au Modulateur planétaire avant de saturer votre planète.
- **Un ordre en file n'est pas payé** : il ne sera payé qu'au lancement. Si la planète n'a plus les ressources à ce moment-là, l'ordre est abandonné sans frais.
- **Les facteurs ne sont pas tous égaux** : l'Extracteur cristallin (1,6) et le Réacteur (1,8) renchérissent plus vite que les autres mines.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Formules de l'économie](/fr/economy/formulas)
- [Files de construction](/fr/economy/build-queue)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Arbre technologique](/fr/research/tech-tree)
- [Annexe : les bâtiments niveau par niveau](/fr/economy/building-levels)
'''
    return f'''# Buildings list

> **In short**: a planet can hold up to 17 buildings. A moon takes 5: its 3 lunar buildings, plus the Automaton Factory and the Orbital Dock. Mines produce resources, power plants produce energy, storage keeps your stock, and facilities open research, ships, defenses and missiles. Every building level takes one field.
{{.is-info}}

> **Universe setting**: the construction speed divides building times.
> Default: **×1** · Redline: **×1**
{{.is-info}}

## Rules

1. A building goes up **level by level**. Level N costs the level 1 cost × factor^(N − 1), rounded down for each resource (see [Economy formulas](/en/economy/formulas)).
2. **Each level takes one field** on the planet. Exceptions: the Planetary Base (one field, single level) and the Repair Station, which takes none.
3. An enemy can **never destroy your buildings**. Only their owner can demolish them (see [Demolishing a building](/en/economy/demolition)); only the destruction of a moon takes that moon's buildings with it.
4. A building is **paid when its construction starts**, not when it is queued.
5. **Points**: each level earns 1 point per 1,000 resources spent (metal, crystal and hydrogen), counted in economy points.
6. Each building has a **maximum level**, except the lunar buildings, limited by the room on the moon.
7. The **Planetary Base** (Colonial Base on a colony) is there from founding and cannot be demolished.
8. Some buildings need a **required energy**: the planet's energy production must reach that threshold when construction starts; nothing is used up.
9. **On a moon**: the Lunar base, the Sensor phalanx and the Jump gate, plus the Automaton Factory and the Orbital Dock, at the same costs and with the same requirements as on a planet. A moon starts with 1 field; each Lunar base level opens 3 and takes 1, never beyond what the moon's diameter allows.

## Worked example

Raising the Mineral Excavator from level 13 to level 14:
- Cost: 60 × 1.5^13 = **{N(c14[0])} metal** and 15 × 1.5^13 = **{N(c14[1])} crystal**, so {N(sum(c14))} resources and **{P} economy points**.
- Output goes from {N(mine(30,13))} to **{N(mine(30,14))} metal per hour**, energy use from {N(mine(10,13))} to **{N(mine(10,14))}**.
- Time with an Automaton Factory level 4: {N(sum(c14))} / (2,500 × 5) hours, so **{N(t14)} seconds** (1 h 10 min).

## Detailed data

{T}

Level N cost follows from the factor: for instance, Orbital Dock level 5 costs 400 × 2^4 = 6,400 metal, 3,200 crystal and 1,600 hydrogen. The cost, energy and output of every level are in the [appendix: buildings level by level](/en/economy/building-levels).

## Common pitfalls

- **Mines and energy go together**: each mine level uses more energy. Without enough power, all production slows down (see [Energy](/en/economy/energy)).
- **Fields are limited**: each level takes one. Think of the Planetary Modulator before your planet fills up.
- **A queued order is not paid**: it is paid when it starts. If the planet no longer has the resources then, the order is dropped at no cost.
- **Factors are not all equal**: the Crystal Extractor (1.6) and the Reactor (1.8) get pricier faster than the other mines.

## Related pages

- [Resources](/en/economy/resources)
- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Economy formulas](/en/economy/formulas)
- [Build queues](/en/economy/build-queue)
- [Demolishing a building](/en/economy/demolition)
- [Tech tree](/en/research/tech-tree)
- [Appendix: buildings level by level](/en/economy/building-levels)
'''
for lang in ('fr','en'): write(lang, 'economy/buildings', body(lang))
