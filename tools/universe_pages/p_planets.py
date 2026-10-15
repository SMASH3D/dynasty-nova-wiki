import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

DAYS = [1, 5, 10, 15, 16, 20, 25, 31]


def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    fr = lang == 'fr'
    F2 = lambda x: (f'{x:.2f}'.replace('.', ',') if fr else f'{x:.2f}')
    T = TYPE_NAMES[lang]
    rows15 = []
    for p in range(1, 16):
        size, types = TYPES[p]
        lo, hi = temps(p)
        rows15.append([p, N(size), f'{N(size - SIZE_SPREAD)} à {N(size + SIZE_SPREAD)}' if fr else f'{N(size - SIZE_SPREAD)} to {N(size + SIZE_SPREAD)}',
                       ', '.join(T[t] for t in types), f'{N(lo)} / {N(hi)}', F2(h2factor(hi)), N(satellite(hi))])
    mapping = '\n'.join(f'- {k} positions : ' + ', '.join(str(eff_pos(p, k)) for p in range(1, k + 1)) if fr else
                        f'- {k} positions: ' + ', '.join(str(eff_pos(p, k)) for p in range(1, k + 1))
                        for k in range(POSITIONS_MIN, POSITIONS_MAX + 1))

    def bonus_rows(k):
        out = []
        for p in range(1, k + 1):
            m, c = metal_bonus(p, k), crystal_bonus(p, k)
            if m or c:
                out.append([p, N(round(ref_pos(p, k), 2)), P(m) if m else '', P(c) if c else ''])
        return out
    hdr_b = ['Position', 'Lue sur 15', 'Métal', 'Cristal'] if fr else ['Position', 'Read on 15', 'Metal', 'Crystal']
    lo8, hi8 = temps(8)
    trow = [[d, N(temp_at(lo8, hi8, d, 31)), P(max(0, temp_at(lo8, hi8, d, 31)))] for d in DAYS]
    f3, f12 = h2factor(temps(3)[1]), h2factor(temps(12)[1])
    gain = round((f12 / f3 - 1) * 100)
    # exemple bonus : colonie en position 8 sur 15, mine produisant 1 000 métal/h
    ex_m = fl(1000 * metal_bonus(8, 15) / 100)
    ex9 = metal_bonus(4, 9)
    ex9_out = fl(1000 * ex9 / 100)
    if fr:
        return f'''# Planètes : taille, température, type

> **En bref** : la position d'une planète dans son système fixe sa taille moyenne et sa température. Les planètes proches de l'étoile sont plus petites et plus chaudes, idéales pour l'énergie solaire ; les planètes lointaines sont plus grandes et plus froides, idéales pour l'hydrogène. Le type de planète (désert, jungle, glace…) ne change que l'apparence. Les colonies ont en plus un bonus de production de métal ou de cristal selon leur position ; la planète mère n'en a pas.
{{.is-info}}

> **Paramètre d'univers** : le nombre de positions par système (de {POSITIONS_MIN} à {POSITIONS_MAX}) dépend de l'univers. Dans un univers qui n'en a pas 15, chaque position est lue sur une échelle de 15 (règles 2 et 9).
> Par défaut : **aucun, chaque univers a le sien** · Redline : **15 positions**
{{.is-info}}

![Un système en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*Un système en affichage orbites : chaque planète a l'aspect de son type et de son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

### Taille
1. Le nombre de cases d'une planète vaut la **taille moyenne de sa position, plus ou moins {SIZE_SPREAD}**. Il est fixé une fois pour toutes à la création de l'univers, case par case.
2. Dans un système qui n'a pas 15 positions, la position est d'abord **ramenée sur 15 et arrondie** (liste dans les données détaillées) : la taille, les types et la température sont ceux de cette position ramenée.
3. La **planète mère** a toujours **{MOTHER_SIZE} cases**, quelle que soit sa position.
4. Chaque niveau de bâtiment occupe **une case**, sauf la Station de réparation. Le [Modulateur planétaire](/fr/economy/terraformer-and-logistics) ajoute des cases, et certains talents de dynastie aussi.

### Température
5. Chaque position a une température **minimale** et **maximale**, écartées de 40 °C : $T_{{max}} = 180 - 15 \\times p$ et $T_{{min}} = T_{{max}} - 40$, avec $p$ la position ramenée sur 15.
6. La température **actuelle** suit le mois du calendrier : à sa minimale le 1er, elle monte chaque jour jusqu'à sa maximale le jour du milieu du mois (le 15, le 14 en février), puis redescend jusqu'à sa minimale le dernier jour. Elle est arrondie au degré.
7. La température agit sur trois productions (détail dans [L'énergie](/fr/economy/energy)) :
   - **Condensateur d'hydrogène** : production × (1,44 − 0,004 × $T_{{max}}$), jamais en dessous de 0. Plus il fait froid, plus il produit.
   - **Collecteur solaire** : $T_{{max}}$ / 4 + 20 énergie chacun, arrondi à l'inférieur.
   - **Capteurs photovoltaïques** : production × (1 + température actuelle / 100), quand la température actuelle est positive.

### Type et apparence
8. Chaque planète a un **type** (désert, aride, normal, jungle, eau, glace, gaz), tiré parmi ceux de sa position, et un **biome**, une variante visuelle. Ils ne changent que le nom généré et les images, pas la production. Un **skin de planète**, obtenu en boutique ou dans le lot mensuel Premium, remplace l'apparence de votre planète.

### Bonus de position
9. **Bonus de position** : l'Extracteur cristallin produit davantage près de l'étoile, l'Excavateur minéral au milieu du système (tableau ci-dessous). Le bonus a sa propre ligne dans le détail de production. Il ne touche pas l'hydrogène, qui dépend de la température.
10. La **planète mère n'a pas de bonus de position** : son emplacement est tiré au hasard, et le bonus donnerait à chacun une avance différente par chance. Seul un talent de dynastie peut lui en accorder une part.
11. Dans un système qui n'a pas 15 positions, la position est lue sur l'échelle de 15 **sans arrondi**, et le bonus est **interpolé** entre les deux positions qui l'encadrent. Le pic (+40 % de cristal, +35 % de métal) reste le même, aucune position n'est doublée ni sautée.
12. Le bonus s'applique à la production de la mine, arrondi à l'inférieur.

## Exemple chiffré

**Hydrogène : position 3 contre position 12**
- Position 3 (température max {temps(3)[1]} °C) : facteur 1,44 − 0,004 × {temps(3)[1]} = **{F2(f3)}**.
- Position 12 (température max {temps(12)[1]} °C) : facteur **{F2(f12)}**.
- À niveau égal, le Condensateur de la position 12 produit {F2(f12)} / {F2(f3)} = **{gain} % de plus**.

**Bonus de position d'une colonie**
- Colonie en position 8 d'un système de 15, Excavateur minéral produisant 1 000 métal par heure : bonus {P(metal_bonus(8, 15))}, soit **+{N(ex_m)} métal par heure**.
- Même mine sur une colonie en position 4 d'un système de 9 : la position est lue à {N(ref_pos(4, 9))} sur 15, entre 6 (+17 %) et 7 (+23 %), soit un bonus de **{P(ex9)}** : **+{N(ex9_out)} métal par heure**.
- La même mine sur votre planète mère : **aucun bonus**.

**La température du mois en position 8** ({lo8} à {hi8} °C, mois de 31 jours) et le bonus des Capteurs photovoltaïques :

{table(['Jour', 'Température actuelle (°C)', 'Bonus des Capteurs'], trow)}

## Données détaillées

### Selon la position (sur 15)

{table(['Position', 'Taille moyenne', 'Taille possible', 'Types possibles', 'Temp. min / max (°C)', 'Facteur du Condensateur', 'Énergie par Collecteur'], rows15)}

### Positions ramenées sur 15 (taille, types, température)

Position ramenée de chaque position du système, de la 1re à la dernière :

{mapping}

### Bonus de position (colonies uniquement)

Système de 15 positions (Redline) ; les positions absentes n'ont pas de bonus :

{table(hdr_b, bonus_rows(15))}

Système de 9 positions :

{table(hdr_b, bonus_rows(9))}

Système de 20 positions :

{table(hdr_b, bonus_rows(20))}

La position lue sur 15 vaut $1 + (p - 1) \\times 14 / (n - 1)$, avec $p$ la position et $n$ le nombre de positions du système.

## Pièges fréquents

- **La planète mère ne suit pas la table** : elle a toujours {MOTHER_SIZE} cases et n'a pas de bonus de position.
- **Pour une colonie, la position compte double** : cristal près de l'étoile, métal au milieu du système (+35 % en position 8 sur 15).
- **Taille et bonus ne se lisent pas pareil** dans un univers qui n'a pas 15 positions : la taille et la température suivent la position arrondie, le bonus la position exacte.
- **Le bonus solaire varie dans le mois** : une planète froide n'en profite presque jamais.
- **Le type ne compte pas** : une planète « glace » et une planète « gaz » à la même position produisent pareil.

## Pages liées

- [Coloniser](/fr/universe/colonization)
- [Liste des bâtiments](/fr/economy/buildings)
- [L'énergie](/fr/economy/energy)
- [Modulateur planétaire et Centre logistique](/fr/economy/terraformer-and-logistics)
- [Coordonnées](/fr/universe/coordinates)
'''
    return f'''# Planets: size, temperature, type

> **In short**: a planet's position in its system sets its average size and its temperature. Planets close to the star are smaller and hotter, ideal for solar energy; distant planets are larger and colder, ideal for hydrogen. The planet type (desert, jungle, ice…) only changes its look. Colonies also get a metal or crystal output bonus depending on their position; the mother planet gets none.
{{.is-info}}

> **Universe setting**: the number of positions per system ({POSITIONS_MIN} to {POSITIONS_MAX}) depends on the universe. In a universe without 15 positions, each position is read on a 15-position scale (rules 2 and 11).
> Default: **none, each universe has its own** · Redline: **15 positions**
{{.is-info}}

![A system in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*A system in orbit layout: each planet looks like its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

### Size
1. A planet's number of fields is the **average size of its position, plus or minus {SIZE_SPREAD}**. It is fixed once and for all when the universe is created, cell by cell.
2. In a system without 15 positions, the position is first **scaled to 15 and rounded** (list in the detailed data): size, types and temperature are those of that scaled position.
3. The **mother planet** always has **{MOTHER_SIZE} fields**, whatever its position.
4. Each building level takes **one field**, except the Repair Station. The [Planetary Modulator](/en/economy/terraformer-and-logistics) adds fields, and so do some dynasty talents.

### Temperature
5. Each position has a **minimum** and a **maximum** temperature, 40 °C apart: $T_{{max}} = 180 - 15 \\times p$ and $T_{{min}} = T_{{max}} - 40$, with $p$ the position scaled to 15.
6. The **current** temperature follows the calendar month: at its minimum on the 1st, it rises each day to its maximum on the middle day of the month (the 15th, the 14th in February), then falls back to its minimum on the last day. It is rounded to the degree.
7. Temperature affects three outputs (details in [Energy](/en/economy/energy)):
   - **Hydrogen Condenser**: output × (1.44 − 0.004 × $T_{{max}}$), never below 0. The colder, the more it produces.
   - **Solar Collector**: $T_{{max}}$ / 4 + 20 energy each, rounded down.
   - **Photovoltaic Sensors**: output × (1 + current temperature / 100), when the current temperature is positive.

### Type and look
8. Each planet has a **type** (desert, dry, normal, jungle, water, ice, gas), drawn among those of its position, and a **biome**, a visual variant. They only change the generated name and the pictures, not output. A **planet skin**, from the shop or the Premium monthly set, replaces your planet's look.

### Position bonus
9. **Position bonus**: the Crystal Extractor produces more close to the star, the Mineral Excavator in the middle of the system (table below). The bonus has its own line in the production breakdown. It does not affect hydrogen, which depends on temperature.
10. The **mother planet has no position bonus**: its slot is drawn at random, and the bonus would hand everyone a different head start by luck. Only a dynasty talent can grant it a share.
11. In a system without 15 positions, the position is read on the 15-position scale **without rounding**, and the bonus is **interpolated** between the two positions around it. The peak (+40% crystal, +35% metal) stays the same, and no position is doubled or skipped.
12. The bonus applies to the mine's output, rounded down.

## Worked example

**Hydrogen: position 3 versus position 12**
- Position 3 (max temperature {temps(3)[1]} °C): factor 1.44 − 0.004 × {temps(3)[1]} = **{F2(f3)}**.
- Position 12 (max temperature {temps(12)[1]} °C): factor **{F2(f12)}**.
- At the same level, the position 12 Condenser produces {F2(f12)} / {F2(f3)} = **{gain}% more**.

**A colony's position bonus**
- Colony at position 8 of a 15-position system, Mineral Excavator producing 1,000 metal per hour: bonus {P(metal_bonus(8, 15))}, so **+{N(ex_m)} metal per hour**.
- Same mine on a colony at position 4 of a 9-position system: the position is read as {N(ref_pos(4, 9))} on the 15 scale, between 6 (+17%) and 7 (+23%), so a bonus of **{P(ex9)}**: **+{N(ex9_out)} metal per hour**.
- The same mine on your mother planet: **no bonus**.

**The month's temperature at position 8** ({lo8} to {hi8} °C, 31-day month) and the Photovoltaic Sensors bonus:

{table(['Day', 'Current temperature (°C)', 'Sensors bonus'], trow)}

## Detailed data

### By position (out of 15)

{table(['Position', 'Average size', 'Possible size', 'Possible types', 'Min / max temp. (°C)', 'Condenser factor', 'Energy per Collector'], rows15)}

### Positions scaled to 15 (size, types, temperature)

Scaled position of each position of the system, from the 1st to the last:

{mapping}

### Position bonus (colonies only)

15-position system (Redline); positions not listed have no bonus:

{table(hdr_b, bonus_rows(15))}

9-position system:

{table(hdr_b, bonus_rows(9))}

20-position system:

{table(hdr_b, bonus_rows(20))}

The position read on 15 is $1 + (p - 1) \\times 14 / (n - 1)$, with $p$ the position and $n$ the system's number of positions.

## Common pitfalls

- **The mother planet does not follow the table**: it always has {MOTHER_SIZE} fields and no position bonus.
- **For a colony, position counts twice**: crystal close to the star, metal in the middle of the system (+35% at position 8 out of 15).
- **Size and bonus are not read the same way** in a universe without 15 positions: size and temperature follow the rounded position, the bonus the exact one.
- **The solar bonus varies over the month**: a cold planet hardly ever benefits.
- **Type does not matter**: an "ice" planet and a "gas" planet at the same position produce the same.

## Related pages

- [Colonization](/en/universe/colonization)
- [List of buildings](/en/economy/buildings)
- [Energy](/en/economy/energy)
- [Planetary Modulator and Logistics Center](/en/economy/terraformer-and-logistics)
- [Coordinates](/en/universe/coordinates)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/planets', body(lang))
