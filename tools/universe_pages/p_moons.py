import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

MAXC, CAP = DEFAULTS['moon']
CHANCES = [1, 2, 5, 10, 15, 20]
DEBRIS_EX = [50_000, 100_000, 500_000, 1_000_000, 2_000_000, 5_000_000]
LB_LEVELS = list(range(1, 16))
EX_CHANCE = 10


def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    fr = lang == 'fr'
    deb_rows = [[N(d), P(moon_chance(d, MAXC, CAP))] for d in DEBRIS_EX]
    size_rows = []
    for c in CHANCES:
        (d0, f0), (d1, f1) = moon_fields_range(c, MAXC)
        size_rows.append([P(c), N(fl(c * CAP / MAXC)), f'{N(d0)} à {N(d1)}' if fr else f'{N(d0)} to {N(d1)}', f'{N(f0)} à {N(f1)}' if fr else f'{N(f0)} to {N(f1)}'])
    lb_rows = []
    cum = [0, 0, 0]
    for L in LB_LEVELS:
        cst = cost(LUNAR_BASE_COST, 2, L)
        cum = [a + b for a, b in zip(cum, cst)]
        lb_rows.append([L, N(cst[0]), N(cst[1]), N(cst[2]), N(MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * L), N(MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * L - L)])
    (ed0, ef0), (ed1, ef1) = moon_fields_range(EX_CHANCE, MAXC)
    ex_debris = fl(EX_CHANCE * CAP / MAXC)
    # niveau de Base lunaire qui atteint le plafond de la plus petite lune de l'exemple
    lvl_cap = next(L for L in range(1, 100) if MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * L >= ef0)
    lb1 = cost(LUNAR_BASE_COST, 2, 1)
    ph1 = PHALANX_COST
    jg1 = JUMP_GATE_COST
    if fr:
        cat = [
            ['Base lunaire', f'{N(lb1[0])} / {N(lb1[1])} / {N(lb1[2])}', '×2', 'aucun', 'aucun (le diamètre plafonne les cases)'],
            ['Phalange de capteur', f'{N(ph1[0])} / {N(ph1[1])} / {N(ph1[2])}', '×2', 'Base lunaire 1', 'aucun'],
            ['Porte de saut', f'{N(jg1[0])} / {N(jg1[1])} / {N(jg1[2])}', '×2', 'Base lunaire 1, Pliage Spatial 7', 'aucun'],
            ["Fabrique d'automates", '400 / 120 / 200', '×2', 'Base lunaire 1', '10'],
            ['Dock orbital', '400 / 200 / 100', '×2', "Base lunaire 1, Fabrique d'automates 2", '12'],
        ]
        return f'''# Les lunes

> **En bref** : une lune peut naître des débris d'un combat livré au-dessus d'une planète. Elle revient toujours au propriétaire de la planète, quel que soit le vainqueur. Elle commence avec une seule case : la Base lunaire en ouvre d'autres, dans la limite fixée par son diamètre. Une lune accueille la Phalange de capteur et la Porte de saut, et ne peut pas être scannée par une phalange.
{{.is-info}}

> **Paramètre d'univers** : la chance maximale de former une lune et la quantité de débris qui l'atteint peuvent être différentes selon l'univers.
> Par défaut : **{P(MAXC)} au plus, pour {N(CAP)} de débris** · Redline : **{P(REDLINE['moon'][0])} au plus, pour {N(REDLINE['moon'][1])} de débris**
{{.is-info}}

## Règles

### Formation
1. À la fin d'un combat au-dessus d'une planète, une lune peut se former. La chance dépend **des débris de ce combat** (métal et cristal) : le champ de ruines déjà en orbite, laissé par des combats précédents, ne compte pas.
2. **Chance** = débris du combat × chance maximale / débris pour la chance maximale, plafonnée à la chance maximale (formule ci-dessous). En dessous d'un point de chance ({N(fl(CAP / MAXC))} débris par défaut), aucune lune ne peut se former.
3. La lune revient **au propriétaire de la planète**, que le combat soit gagné ou perdu. Un attaquant ne gagne jamais de lune en orbite d'une planète qui n'est pas la sienne.
4. Former une lune ne consomme pas les débris : les recycleurs récupèrent tout le champ de ruines.
5. Une position porte **au plus une lune**. Tant que la planète a sa lune, aucun combat n'en forme une autre.
6. Plus la chance était élevée, plus la lune est **grande** : son diamètre fixe le nombre maximal de cases qu'elle offrira (tableau ci-dessous). La notification du combat donne son diamètre.
7. Dans un univers où les **impacts géants** sont activés (événements cosmiques, fermés par défaut), une lune peut aussi naître d'un impact.

### Développement
8. Une lune naît **vide** : ni ressources, ni bâtiments, **une seule case**, et le nom de sa planète (elle peut être renommée).
9. La **Base lunaire** se construit en premier : aucun autre bâtiment ne peut être lancé sur la lune avant elle. Elle ne se démolit pas.
10. Chaque niveau de Base lunaire **ouvre {LUNAR_BASE_FIELDS} cases et en occupe une**, soit 2 cases nettes par niveau.
11. Les cases d'une lune ne dépassent jamais son **plafond** : partie entière((diamètre / 1 000)²). Au-delà, monter la Base lunaire n'ouvre plus rien. Un talent de dynastie lève ce plafond.
12. Bâtiments possibles sur une lune : Base lunaire, Phalange de capteur, Porte de saut, Fabrique d'automates, Dock orbital (tableau ci-dessous).
13. Une lune **ne produit rien** et stocke 10 000 de chaque ressource (voir [Le stockage](/fr/economy/storage)).

### Vivre avec une lune
14. Le vol entre une planète et sa lune a une distance de **5** : un trajet très court, mais un vrai vol.
15. Une lune peut être espionnée, attaquée, détruite par des Colossus stellaires (voir [Destruction de lune](/fr/combat/moon-destruction)), et recevoir des transports. Elle ne se colonise pas, et elle n'occupe pas de place de colonie.
16. Une **Phalange de capteur** ne peut jamais scanner une lune : une flotte qui y stationne reste invisible.
17. Abandonner une planète abandonne aussi sa lune et tout ce qu'elle porte ; recoloniser cette planète la rend avec sa lune.

## Formules

$$ C = \\min\\left(D \\times \\frac{{C_{{max}}}}{{D_{{max}}}},\\ C_{{max}}\\right) \\quad \\text{{si }} D \\geq \\frac{{D_{{max}}}}{{C_{{max}}}},\\ \\text{{sinon }} 0 $$

- $C$ : chance de former une lune, en % ;
- $D$ : débris de métal et de cristal laissés par ce combat ;
- $C_{{max}}$ : chance maximale de l'univers ({P(MAXC)} par défaut) ;
- $D_{{max}}$ : débris qui donnent la chance maximale ({N(CAP)} par défaut).

$$ K = \\left\\lfloor \\left( \\frac{{d}}{{1\\,000}} \\right)^2 \\right\\rfloor $$

- $K$ : plafond de cases de la lune ;
- $d$ : son diamètre, en kilomètres.

## Exemple chiffré

Un combat laisse **{N(ex_debris)}** de débris au-dessus de votre planète, dans un univers réglé par défaut :
- Chance de lune : {N(ex_debris)} × {N(MAXC)} / {N(CAP)} = **{P(EX_CHANCE)}**.
- Si la lune se forme, son diamètre est compris entre **{N(ed0)} et {N(ed1)} km**, soit un plafond de **{N(ef0)} à {N(ef1)} cases**.
- Avec un plafond de {N(ef0)} cases, la Base lunaire atteint ce plafond au niveau **{lvl_cap}** (1 + {LUNAR_BASE_FIELDS} × {lvl_cap} = {N(MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * lvl_cap)} cases ouvertes, ramenées à {N(ef0)}).
- Le champ de ruines reste entier pour vos recycleurs.

## Données détaillées

### Chance selon les débris du combat (réglages par défaut)

{table(['Débris du combat', 'Chance de lune'], deb_rows)}

### Taille de la lune selon la chance (réglages par défaut)

{table(['Chance du combat', 'Débris correspondants', 'Diamètre (km)', 'Plafond de cases'], size_rows)}

### Base lunaire niveau par niveau

Coût du niveau N : coût du niveau 1 × 2^(N − 1). Les cases ouvertes sont plafonnées par le diamètre de la lune.

{table(['Niveau', 'Métal', 'Cristal', 'Hydrogène', 'Cases ouvertes', 'Cases libres (Base lunaire seule)'], lb_rows)}

### Bâtiments d'une lune

{table(['Bâtiment', 'Coût du niveau 1 (métal / cristal / hydrogène)', 'Facteur par niveau', 'Prérequis', 'Niveau max'], cat)}

## Pièges fréquents

- **Un gros champ de ruines déjà en orbite ne sert à rien** : seuls les débris du combat qui vient d'avoir lieu comptent.
- **Les défenses ne laissent pas de débris** dans un univers réglé par défaut : seuls les vaisseaux détruits nourrissent la chance de lune.
- **Une petite lune reste petite** : son plafond est fixé à sa naissance, et la Base lunaire ne le dépasse pas.
- **Une lune n'est pas un abri contre tout** : invisible à la phalange, elle peut quand même être attaquée ou détruite.

## Pages liées

- [Champs de débris](/fr/combat/debris)
- [Destruction de lune](/fr/combat/moon-destruction)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Porte de saut](/fr/fleet/jump-gate)
- [Liste des bâtiments](/fr/economy/buildings)
'''
    cat = [
        ['Lunar base', f'{N(lb1[0])} / {N(lb1[1])} / {N(lb1[2])}', '×2', 'none', 'none (the diameter caps the fields)'],
        ['Sensor phalanx', f'{N(ph1[0])} / {N(ph1[1])} / {N(ph1[2])}', '×2', 'Lunar base 1', 'none'],
        ['Jump gate', f'{N(jg1[0])} / {N(jg1[1])} / {N(jg1[2])}', '×2', 'Lunar base 1, Hyperspace Technology 7', 'none'],
        ['Automaton Factory', '400 / 120 / 200', '×2', 'Lunar base 1', '10'],
        ['Orbital Dock', '400 / 200 / 100', '×2', 'Lunar base 1, Automaton Factory 2', '12'],
    ]
    return f'''# Moons

> **In short**: a moon may be born from the debris of a battle fought above a planet. It always goes to the planet's owner, whoever won. It starts with a single field: the Lunar base opens more, within the limit set by its diameter. A moon hosts the Sensor phalanx and the Jump gate, and cannot be scanned by a phalanx.
{{.is-info}}

> **Universe setting**: the maximum chance of forming a moon and the amount of debris that reaches it may differ from one universe to another.
> Default: **{P(MAXC)} at most, at {N(CAP)} debris** · Redline: **{P(REDLINE['moon'][0])} at most, at {N(REDLINE['moon'][1])} debris**
{{.is-info}}

## Rules

### Formation
1. At the end of a battle above a planet, a moon may form. The chance depends on **that battle's debris** (metal and crystal): a debris field already in orbit, left by earlier battles, does not count.
2. **Chance** = battle debris × maximum chance / debris for the maximum chance, capped at the maximum chance (formula below). Below one point of chance ({N(fl(CAP / MAXC))} debris by default), no moon can form.
3. The moon goes **to the planet's owner**, whether the battle was won or lost. An attacker never gains a moon in orbit of a planet that is not theirs.
4. Forming a moon does not use up the debris: recyclers collect the whole debris field.
5. A position holds **at most one moon**. As long as the planet has its moon, no battle forms another one.
6. The higher the chance was, the **bigger** the moon: its diameter sets the maximum number of fields it will offer (table below). The battle notification gives its diameter.
7. In a universe where **giant impacts** are switched on (cosmic events, closed by default), a moon can also be born from an impact.

### Development
8. A moon is born **empty**: no resources, no buildings, **a single field**, and its planet's name (it can be renamed).
9. The **Lunar base** is built first: no other building can be started on the moon before it. It cannot be demolished.
10. Each Lunar base level **opens {LUNAR_BASE_FIELDS} fields and takes one**, a net 2 fields per level.
11. A moon's fields never go past its **cap**: whole part of ((diameter / 1,000)²). Beyond it, raising the Lunar base opens nothing more. A dynasty talent lifts that cap.
12. Buildings possible on a moon: Lunar base, Sensor phalanx, Jump gate, Automaton Factory, Orbital Dock (table below).
13. A moon **produces nothing** and stores 10,000 of each resource (see [Storage](/en/economy/storage)).

### Living with a moon
14. The flight between a planet and its moon has a distance of **5**: a very short trip, but a real flight.
15. A moon can be spied on, attacked, destroyed by Stellar Colossi (see [Moon destruction](/en/combat/moon-destruction)), and receive transports. It cannot be colonized, and it does not take a colony slot.
16. A **Sensor phalanx** can never scan a moon: a fleet stationed there stays invisible.
17. Abandoning a planet also abandons its moon and everything on it; recolonizing that planet hands it back with its moon.

## Formulas

$$ C = \\min\\left(D \\times \\frac{{C_{{max}}}}{{D_{{max}}}},\\ C_{{max}}\\right) \\quad \\text{{if }} D \\geq \\frac{{D_{{max}}}}{{C_{{max}}}},\\ \\text{{otherwise }} 0 $$

- $C$: chance of forming a moon, in %;
- $D$: metal and crystal debris left by that battle;
- $C_{{max}}$: the universe's maximum chance ({P(MAXC)} by default);
- $D_{{max}}$: debris that gives the maximum chance ({N(CAP)} by default).

$$ K = \\left\\lfloor \\left( \\frac{{d}}{{1{{,}}000}} \\right)^2 \\right\\rfloor $$

- $K$: the moon's field cap;
- $d$: its diameter, in kilometers.

## Worked example

A battle leaves **{N(ex_debris)}** debris above your planet, in a universe with default settings:
- Moon chance: {N(ex_debris)} × {N(MAXC)} / {N(CAP)} = **{P(EX_CHANCE)}**.
- If the moon forms, its diameter is between **{N(ed0)} and {N(ed1)} km**, a cap of **{N(ef0)} to {N(ef1)} fields**.
- With a cap of {N(ef0)} fields, the Lunar base reaches that cap at level **{lvl_cap}** (1 + {LUNAR_BASE_FIELDS} × {lvl_cap} = {N(MOON_INITIAL_FIELDS + LUNAR_BASE_FIELDS * lvl_cap)} fields opened, brought down to {N(ef0)}).
- The debris field stays whole for your recyclers.

## Detailed data

### Chance by battle debris (default settings)

{table(['Battle debris', 'Moon chance'], deb_rows)}

### Moon size by chance (default settings)

{table(['Battle chance', 'Matching debris', 'Diameter (km)', 'Field cap'], size_rows)}

### Lunar base level by level

Cost of level N: level 1 cost × 2^(N − 1). Fields opened are capped by the moon's diameter.

{table(['Level', 'Metal', 'Crystal', 'Hydrogen', 'Fields opened', 'Free fields (Lunar base only)'], lb_rows)}

### Moon buildings

{table(['Building', 'Level 1 cost (metal / crystal / hydrogen)', 'Factor per level', 'Requirements', 'Max level'], cat)}

## Common pitfalls

- **A large debris field already in orbit is no help**: only the debris of the battle that just took place counts.
- **Defenses leave no debris** in a universe with default settings: only destroyed ships feed the moon chance.
- **A small moon stays small**: its cap is set at birth, and the Lunar base never goes past it.
- **A moon is not a shelter from everything**: invisible to the phalanx, it can still be attacked or destroyed.

## Related pages

- [Debris fields](/en/combat/debris)
- [Moon destruction](/en/combat/moon-destruction)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Jump gate](/en/fleet/jump-gate)
- [List of buildings](/en/economy/buildings)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/moons', body(lang), published=False)
