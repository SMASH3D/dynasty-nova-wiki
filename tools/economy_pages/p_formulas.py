import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
# Exemple : Dock orbital 6 -> 7 avec Fabrique 6, Assembleur 1, vitesse 1, Bâtisseurs associés 2 (+20 %)
c7 = cost((400,200,100),2,7); tot = sum(c7)
raw = btime(tot, robo=6, nanite=1)
fast = max(1, math.ceil(round(raw*100/120, 6)))
ship = max(1, round(5400/((1+7)*2**1)/1))
def hm(s, lang):
    h, r = divmod(s, 3600); m = round(r/60)
    return f'{h} h {m:02d} min' if h else f'{m} min'
def body(lang):
    N = lambda x: n(x, lang); fr = lang=='fr'
    if fr:
        return f'''# Formules de l'économie

> **En bref** : toutes les formules de l'économie, telles que le jeu les calcule : coût et points d'un niveau, durée des bâtiments, des vaisseaux, des défenses et des recherches, production, énergie et stockage. Chaque bonus de vitesse divise une durée, chaque bonus de production s'ajoute à la production brute des mines.
{{.is-info}}

> **Paramètre d'univers** : les vitesses d'économie, de construction, de recherche et de chantier peuvent être différentes selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

## Règles

### Coût et points
1. Coût du niveau $N$ d'un bâtiment ou d'une recherche, pour chaque ressource :
$$C_N = \\left\\lfloor C_1 \\times f^{{N-1}} \\right\\rfloor$$
   - $C_1$ : coût du niveau 1 ; $f$ : facteur du bâtiment ou de la recherche (voir [Liste des bâtiments](/fr/economy/buildings)).
   - L'énergie requise suit la même formule ; seule la Station de réparation a un facteur d'énergie différent (2,5 au lieu de 5).
2. Un vaisseau ou une défense coûte toujours le même prix à l'unité.
3. **Points** : $P = (M + C + H) / 1\\,000$, où $M$, $C$ et $H$ sont le métal, le cristal et l'hydrogène dépensés. L'énergie requise ne compte pas.

### Durées
4. **Bâtiment**, en heures :
$$t = \\frac{{M + C + H}}{{2\\,500 \\times (1 + F) \\times 2^{{A}}}} \\div v_c \\div \\left(1 + \\frac{{b}}{{100}}\\right)$$
   - $M + C + H$ : coût du niveau ; $F$ : niveau de la Fabrique d'automates ; $A$ : niveau de l'Assembleur moléculaire ; $v_c$ : vitesse de construction de l'univers ; $b$ : bonus de vitesse en %, additionnés (talent d'alliance Bâtisseurs associés, talents de dynastie).
   - Le résultat est arrondi à la seconde. Une démolition dure la moitié de la construction du niveau retiré, sans les bonus de vitesse.
5. **Vaisseau ou défense**, en secondes par unité, jamais moins d'une seconde :
$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v_{{ch}}$$
   - $T$ : durée de base de l'unité (par exemple 5 400 s pour une Navette de fret, 2 880 s pour un Collecteur solaire) ; $D$ : niveau du Dock orbital ; $A$ : niveau de l'Assembleur moléculaire ; $v_{{ch}}$ : vitesse de chantier de l'univers. Les bonus de vitesse du chantier (talents) divisent ensuite la durée comme pour les bâtiments.
6. **Recherche**, en heures :
$$t = \\frac{{M + C}}{{1\\,000 \\times (1 + L)}} \\div v_r$$
   - $M + C$ : métal et cristal du niveau, sans l'hydrogène ; $L$ : niveau effectif du Centre d'innovation, réseau de laboratoires compris (voir [Recherche](/fr/research)) ; $v_r$ : vitesse de recherche de l'univers. Les bonus de vitesse (Centres d'innovation en réseau, talents) divisent la durée comme pour les bâtiments.

### Production et énergie (par heure, au niveau $N$)
7. Excavateur minéral : $30 \\times N \\times 1{{,}}1^N$ métal ; Extracteur cristallin : $20 \\times N \\times 1{{,}}1^N$ cristal ; Condensateur d'hydrogène : $10 \\times N \\times 1{{,}}1^N \\times k_H$ hydrogène, avec $k_H = 1{{,}}44 - 0{{,}}004 \\times T_{{max}}$ (jamais négatif). Le tout multiplié par la vitesse d'économie.
8. Consommation d'énergie de chaque mine : $10 \\times N \\times 1{{,}}1^N$, sans la vitesse d'économie.
9. Capteurs photovoltaïques : $20 \\times N \\times 1{{,}}1^N \\times (1 + T / 100)$, avec $T$ la température actuelle, comptée 0 si elle est négative.
10. Réacteur thermonucléaire : $30 \\times N \\times (1{{,}}05 + 0{{,}}01 \\times S)^N$ énergie, $S$ étant le niveau de Science Énergétique ; il consomme $10 \\times N \\times 1{{,}}1^N$ hydrogène, multiplié par la vitesse d'économie.
11. Collecteur solaire : $\\lfloor T_{{max}} / 4 + 20 \\rfloor$ énergie par unité, jamais négatif.
12. Bonus de production : Maîtrise du Plasma (+1 % de métal, +0,66 % de cristal, +0,33 % d'hydrogène par niveau), Extraction coordonnée (+5 % par niveau), bonus de position des colonies, dynastie et talents. Chacun se calcule sur la production brute des mines, s'arrondit à l'inférieur, et ils s'additionnent.
13. Déficit d'énergie : la production des mines, bonus compris, est multipliée par $\\min(1, \\text{{production}} / \\text{{consommation}})$. Puis s'ajoutent 20 métal et 10 cristal de la Base planetaire, multipliés par la vitesse d'économie.

### Stockage
14. Capacité d'un entrepôt au niveau $N$ : $5\\,000 \\times \\lfloor 2{{,}}5 \\times e^{{20N/33}} \\rfloor$. Base planetaire : 10 000 par ressource. Bonus (Centre logistique +10 % par niveau, Entrepôts fédérés +10 % par niveau, talents) additionnés et appliqués à toute la capacité.

$T_{{max}}$ : température maximale de la planète, en °C.

## Exemple chiffré

Monter le Dock orbital du niveau 6 au niveau 7 avec une Fabrique d'automates niveau 6, un Assembleur moléculaire niveau 1, le talent Bâtisseurs associés niveau 2 (+20 %), vitesse ×1 :
- Coût du niveau 7 : 400 × 2^6 = {N(c7[0])} métal, {N(c7[1])} cristal, {N(c7[2])} hydrogène, soit {N(tot)} ressources et {N(tot/1000)} points.
- Durée de base : {N(tot)} / (2 500 × 7 × 2) heures = **{N(raw)} secondes**.
- Avec +20 % de vitesse : {N(raw)} / 1,2 = **{N(fast)} secondes** ({hm(fast,'fr')}).

Une Navette de fret construite ensuite au Dock orbital 7 avec l'Assembleur 1 : 5 400 / (8 × 2) = **{N(ship)} secondes** par unité.

## Données détaillées

### Ce que change chaque vitesse d'univers

| Vitesse | Effet |
|---|---|
| Économie | Multiplie la production des mines, de la Base planetaire et la consommation d'hydrogène du Réacteur ; ne change ni l'énergie ni la consommation d'énergie |
| Construction | Divise la durée des bâtiments et des démolitions |
| Recherche | Divise la durée des recherches |
| Chantier | Divise la durée des vaisseaux et des défenses, accélère la Station de réparation |
| Flotte | Voir [Déplacements](/fr/fleet/movement) |

## Pièges fréquents

- **L'hydrogène compte dans la durée d'un bâtiment** : un bâtiment qui coûte de l'hydrogène dure plus longtemps qu'une mine au même total de métal et de cristal. En recherche, il ne compte pas.
- **Les bonus de vitesse ne réduisent pas de leur pourcentage** : +20 % de vitesse divise la durée par 1,2, soit environ 17 % de moins.
- **L'Assembleur moléculaire divise par deux à chaque niveau** : bâtiments, vaisseaux et défenses.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Liste des bâtiments](/fr/economy/buildings)
- [Files de construction](/fr/economy/build-queue)
'''
    return f'''# Economy formulas

> **In short**: every economy formula, as the game computes it: cost and points of a level, time for buildings, ships, defenses and research, production, energy and storage. Every speed bonus divides a time, every production bonus adds to the mines' gross output.
{{.is-info}}

> **Universe setting**: the economy, construction, research and shipyard speeds may differ from one universe to another.
> Default: **×1** · Redline: **×1**
{{.is-info}}

## Rules

### Cost and points
1. Cost of level $N$ of a building or a research, for each resource:
$$C_N = \\left\\lfloor C_1 \\times f^{{N-1}} \\right\\rfloor$$
   - $C_1$: level 1 cost; $f$: the building's or research's factor (see [Buildings list](/en/economy/buildings)).
   - Required energy follows the same formula; only the Repair Station has a different energy factor (2.5 instead of 5).
2. A ship or a defense always costs the same per unit.
3. **Points**: $P = (M + C + H) / 1{{,}}000$, where $M$, $C$ and $H$ are the metal, crystal and hydrogen spent. Required energy does not count.

### Times
4. **Building**, in hours:
$$t = \\frac{{M + C + H}}{{2{{,}}500 \\times (1 + F) \\times 2^{{A}}}} \\div v_c \\div \\left(1 + \\frac{{b}}{{100}}\\right)$$
   - $M + C + H$: the level's cost; $F$: Automaton Factory level; $A$: Molecular Assembler level; $v_c$: the universe's construction speed; $b$: speed bonuses in %, added up (Associated builders alliance talent, dynasty talents).
   - The result is rounded to the second. A demolition takes half the construction time of the level removed, without speed bonuses.
5. **Ship or defense**, in seconds per unit, never under one second:
$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v_{{sh}}$$
   - $T$: the unit's base time (for instance 5,400 s for a Cargo Shuttle, 2,880 s for a Solar Collector); $D$: Orbital Dock level; $A$: Molecular Assembler level; $v_{{sh}}$: the universe's shipyard speed. Shipyard speed bonuses (talents) then divide the time as for buildings.
6. **Research**, in hours:
$$t = \\frac{{M + C}}{{1{{,}}000 \\times (1 + L)}} \\div v_r$$
   - $M + C$: the level's metal and crystal, without hydrogen; $L$: effective Innovation Center level, laboratory network included (see [Research](/en/research)); $v_r$: the universe's research speed. Speed bonuses (Networked innovation centers, talents) divide the time as for buildings.

### Production and energy (per hour, at level $N$)
7. Mineral Excavator: $30 \\times N \\times 1.1^N$ metal; Crystal Extractor: $20 \\times N \\times 1.1^N$ crystal; Hydrogen Condenser: $10 \\times N \\times 1.1^N \\times k_H$ hydrogen, with $k_H = 1.44 - 0.004 \\times T_{{max}}$ (never negative). All multiplied by the economy speed.
8. Energy use of each mine: $10 \\times N \\times 1.1^N$, without the economy speed.
9. Photovoltaic Sensors: $20 \\times N \\times 1.1^N \\times (1 + T / 100)$, with $T$ the current temperature, counted as 0 when negative.
10. Thermonuclear Reactor: $30 \\times N \\times (1.05 + 0.01 \\times S)^N$ energy, $S$ being the Energy Science level; it burns $10 \\times N \\times 1.1^N$ hydrogen, multiplied by the economy speed.
11. Solar Collector: $\\lfloor T_{{max}} / 4 + 20 \\rfloor$ energy per unit, never negative.
12. Production bonuses: Plasma Technology (+1% metal, +0.66% crystal, +0.33% hydrogen per level), Coordinated extraction (+5% per level), the colonies' position bonus, dynasty and talents. Each is computed on the mines' gross output and rounded down, and they add up.
13. Energy deficit: the mines' output, bonuses included, is multiplied by $\\min(1, \\text{{production}} / \\text{{consumption}})$. Then come the Planetary Base's 20 metal and 10 crystal, multiplied by the economy speed.

### Storage
14. Capacity of a storage building at level $N$: $5{{,}}000 \\times \\lfloor 2.5 \\times e^{{20N/33}} \\rfloor$. Planetary Base: 10,000 per resource. Bonuses (Logistics Center +10% per level, Federated warehouses +10% per level, talents) added up and applied to the whole capacity.

$T_{{max}}$: the planet's maximum temperature, in °C.

## Worked example

Raising the Orbital Dock from level 6 to level 7 with an Automaton Factory level 6, a Molecular Assembler level 1, the Associated builders talent at level 2 (+20%), speed ×1:
- Level 7 cost: 400 × 2^6 = {N(c7[0])} metal, {N(c7[1])} crystal, {N(c7[2])} hydrogen, so {N(tot)} resources and {N(tot/1000)} points.
- Base time: {N(tot)} / (2,500 × 7 × 2) hours = **{N(raw)} seconds**.
- With +20% speed: {N(raw)} / 1.2 = **{N(fast)} seconds** ({hm(fast,'en')}).

A Cargo Shuttle then built at Orbital Dock 7 with Assembler 1: 5,400 / (8 × 2) = **{N(ship)} seconds** per unit.

## Detailed data

### What each universe speed changes

| Speed | Effect |
|---|---|
| Economy | Multiplies the output of the mines, of the Planetary Base and the Reactor's hydrogen use; changes neither energy nor energy use |
| Construction | Divides building and demolition times |
| Research | Divides research times |
| Shipyard | Divides ship and defense times, speeds up the Repair Station |
| Fleet | See [Movement](/en/fleet/movement) |

## Common pitfalls

- **Hydrogen counts in a building's time**: a building that costs hydrogen takes longer than a mine with the same metal and crystal total. In research, it does not count.
- **Speed bonuses do not cut by their percentage**: +20% speed divides the time by 1.2, so about 17% less.
- **The Molecular Assembler halves at every level**: buildings, ships and defenses.

## Related pages

- [Resources](/en/economy/resources)
- [Energy](/en/economy/energy)
- [Storage](/en/economy/storage)
- [Buildings list](/en/economy/buildings)
- [Build queues](/en/economy/build-queue)
'''
for lang in ('fr','en'): write(lang, 'economy/formulas', body(lang))
print(c7, tot, raw, fast, ship)
