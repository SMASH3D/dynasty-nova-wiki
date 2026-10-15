"""Réécrit les quatre pages de la rubrique Défense (FR et EN) depuis def_lib.

python3 tools/defense_pages/p_defense.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from def_lib import *  # noqa: E402,F403

FR, EN = 'fr', 'en'


def nm(c, lang):
    return c[1] if lang == FR else c[2]


def img(c, lang, w=48):
    return f'<img src="/images/illustrations/defense/{c[3]}.jpg" width="{w}" alt="{nm(c, lang)}">'


def req(c, lang):
    i = 0 if lang == FR else 1
    return ', '.join(f'{NAMES[code][i]} {lvl}' for _, code, lvl in c[12])


def cost3(c, lang):
    return [n(x, lang) for x in c[4]]


def box(lang, fr_text, en_text, default, redline):
    if lang == FR:
        return f'> **Paramètre d\'univers** : {fr_text}\n> Par défaut : **{default[0]}** · Redline : **{redline[0]}**\n{{.is-info}}'
    return f'> **Universe setting**: {en_text}\n> Default: **{default[1]}** · Redline: **{redline[1]}**\n{{.is-info}}'


def link(lang, path, fr, en):
    return f'[{fr if lang == FR else en}](/{lang}/{path})'


# ---------------------------------------------------------------- index
def index(lang):
    if lang == FR:
        return '''# Défense

> **En bref** : les défenses restent sur leur planète et prennent part à chaque combat qui s'y livre. Elles se construisent au Dock orbital, ne se déplacent pas et ne sont jamais pillées. Les missiles se stockent à part, dans l'Arsenal balistique : les Ogives longue portée détruisent les défenses d'une planète ennemie sans engager de flotte, les Intercepteurs abattent celles qui visent la vôtre.
{.is-info}

## Pages de cette rubrique

- [Liste des défenses](/fr/defense/defenses) : coûts, statistiques, prérequis et durées des 8 défenses.
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes) : les deux défenses uniques à gros bouclier.
- [Missiles](/fr/defense/missiles) : Arsenal balistique, portée, interception et dégâts des salves.

## Voir aussi

- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Déroulement d'un combat](/fr/combat/how-combat-works)'''
    return '''# Defense

> **In short**: defenses stay on their planet and take part in every battle fought there. They are built at the Orbital Dock, never move and are never plundered. Missiles are stored apart, in the Ballistic Arsenal: Long-Range Warheads destroy an enemy planet's defenses without sending a fleet, Interception Missiles shoot down the ones aimed at yours.
{.is-info}

## Pages in this section

- [Defenses list](/en/defense/defenses): costs, stats, requirements and build times of the 8 defenses.
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes): the two unique, heavily shielded defenses.
- [Missiles](/en/defense/missiles): Ballistic Arsenal, range, interception and salvo damage.

## See also

- [Defense rebuild](/en/combat/defense-rebuild)
- [How combat works](/en/combat/how-combat-works)'''


# ---------------------------------------------------------------- defenses
def defenses(lang):
    N = lambda x: n(x, lang)
    fr = lang == FR
    bp, ion = BY['ballistic_projector'], BY['ion_battery']
    q, dock = 20, 4
    t1 = unit_time(bp, dock)
    tot = t1 * q
    w, s, h = combat_stats(ion, 5, 4, 6)

    stats_rows = []
    for c in DEFENSES:
        _, _, hull = combat_stats(c)
        stats_rows.append([img(c, lang) + ' ' + nm(c, lang), *cost3(c, lang), N(points(c)), N(c[5]), N(hull), N(c[6]), N(c[7]), dur(c[8], lang)])
    hdr = (['Défense', 'Métal', 'Cristal', 'Hydrogène', 'Points', 'Structure', 'Coque en combat', 'Bouclier', 'Attaque', 'Durée de base'] if fr
           else ['Defense', 'Metal', 'Crystal', 'Hydrogen', 'Points', 'Structure', 'Combat hull', 'Shield', 'Attack', 'Base time'])
    T1 = table(hdr, stats_rows)

    T2 = table(['Défense', 'Prérequis', 'Exemplaires par planète'] if fr else ['Defense', 'Requirements', 'Copies per planet'],
               [[nm(c, lang), req(c, lang), '1' if c[9] else ('illimité' if fr else 'unlimited')] for c in DEFENSES])

    docks = [2, 4, 6, 8, 10, 12]
    rows = []
    for c in DEFENSES:
        need = c[12][0][2]
        rows.append([nm(c, lang)] + [(dur(unit_time(c, d), lang) if d >= need else ('non' if fr else 'no')) for d in docks])
    T3 = table([('Défense' if fr else 'Defense')] + [(f'Dock {d}' if fr else f'Dock {d}') for d in docks], rows)

    rf_rows = []
    for c in DEFENSES:
        lst = RF[c[0]]
        txt = ', '.join(f'{SHIPS[s_][0 if fr else 1]} {v}' for s_, v in lst) if lst else ('aucun' if fr else 'none')
        rf_rows.append([nm(c, lang), txt])
    T4 = table(['Défense', 'Tirs rapides subis'] if fr else ['Defense', 'Rapid fire taken'], rf_rows)

    if fr:
        return f'''# Liste des défenses

> **En bref** : les défenses protègent votre planète en permanence. Elles ne se déplacent pas, ne peuvent pas être pillées et prennent part à chaque combat livré sur leur planète. Le jeu en compte 8, dont deux uniques (Barrière défensive et Dôme protecteur). Les missiles se construisent au même endroit mais ne combattent pas : voir [Missiles](/fr/defense/missiles).
{{.is-info}}

{box(lang, "la part des défenses détruites qui part en champ de ruines peut être différente selon l'univers.", '', ('0 %', ''), ('0 %', ''))}

{box(lang, "la vitesse de chantier divise la durée de construction des défenses.", '', ('×1', ''), ('×1', ''))}

## Règles

### Construction
1. Les défenses se construisent au **Dock orbital**, sur une planète ou sur une lune qui en possède un.
2. Pendant l'agrandissement du Dock orbital, **aucune commande** de défense n'est acceptée.
3. Les défenses ont **leur propre file**, distincte de celle des vaisseaux : les deux avancent en même temps. La file accepte **{QUEUE_FREE} commandes** (**{QUEUE_PREMIUM}** avec le Premium), celle en cours comprise (voir [Files de construction](/fr/economy/build-queue)).
4. À la commande, la planète doit avoir les ressources de **toute la quantité**. Chaque unité est ensuite payée au moment où elle entre en production ; si l'unité suivante ne peut plus être payée, la commande s'arrête là.
5. Commander une défense déjà en attente dans la file l'ajoute à cette commande, sans prendre de place supplémentaire.
6. **Durée d'une unité**, en secondes, jamais moins d'une seconde :
$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v$$
   - $T$ : durée de base de la défense (tableau ci-dessous) ; $D$ : niveau du Dock orbital ; $A$ : niveau de l'Assembleur moléculaire ; $v$ : vitesse de chantier de l'univers.
   - Les bonus de vitesse de chantier (talents de dynastie, alliance) divisent ensuite cette durée.

### En combat
7. Chaque défense tire **une fois par round** et ne combat que là où elle est construite (planète ou lune).
8. Attaque, bouclier et structure augmentent de **10 % par niveau** de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. En combat, la **coque** vaut la structure divisée par 10.
9. Les défenses n'ont **aucun tir rapide**. Certains vaisseaux en ont contre elles (tableau ci-dessous).
10. Après un combat, une partie des défenses détruites est reconstruite gratuitement : voir [Reconstruction des défenses](/fr/combat/defense-rebuild). Une défense détruite par un missile est perdue (voir [Missiles](/fr/defense/missiles)).
11. Les défenses détruites ne laissent **aucun champ de ruines**, sauf réglage contraire de l'univers.

### Unicité et points
12. **Barrière défensive et Dôme protecteur** : un seul exemplaire de chacun par planète. Impossible d'en commander plus d'un à la fois, ni d'en commander un tant qu'il en existe un sur la planète ou dans la file.
13. **Points** : chaque défense rapporte 1 point par tranche de 1 000 ressources de son coût (métal, cristal et hydrogène), comptés dans les points militaires.

## Exemple chiffré

**Commander {q} Projecteurs balistiques avec un Dock orbital niveau {dock}** (Assembleur moléculaire 0, vitesse ×1)
- Coût : {q} × {N(bp[4][0])} = **{N(q * bp[4][0])} métal**, à avoir sur la planète au moment de la commande ; **{N(q * points(bp))} points** militaires une fois construits.
- Une unité : {N(bp[8])} / (1 + {dock}) = **{N(t1)} secondes**.
- La commande entière : {q} × {N(t1)} = {N(tot)} secondes, soit **{dur(tot, lang)}**.

**Une Batterie ionique en combat** avec Systèmes Offensifs 5, Champs de Protection 4 et Métallurgie Avancée 6
- Attaque : {N(ion[7])} × 1,5 = **{N(w)}**.
- Bouclier : {N(ion[6])} × 1,4 = **{N(s)}**.
- Coque : {N(ion[5])} × 1,6 / 10 = **{N(h)}**.

## Données détaillées

### Coûts et statistiques de base (sans recherche)

{T1}

La durée de base est celle d'une unité avec un Dock orbital niveau 0 ; le Dock la divise ensuite (règle 6).

### Prérequis

{T2}

### Durée d'une unité selon le Dock orbital

Assembleur moléculaire 0, vitesse de chantier ×1, sans bonus. « non » : niveau de Dock insuffisant.

{T3}

Chaque niveau d'Assembleur moléculaire divise encore ces durées par deux.

### Vaisseaux qui ont un tir rapide contre les défenses

{T4}

## Pièges fréquents

- **Le Dock orbital bloque les commandes pendant son agrandissement** : lancez vos défenses avant de l'agrandir.
- **Une grosse commande peut s'arrêter en route** : chaque unité est payée à son tour. Si vous dépensez les ressources ailleurs entre-temps, la commande s'arrête à la dernière unité payée.
- **Le Frappe-orbital est l'ennemi des défenses** : il a un tir rapide contre presque toutes. Face à lui, l'Éjecteur à plasma et les deux boucliers résistent le mieux.
- **Les défenses ne rapportent rien à l'attaquant** : elles ne laissent pas de champ de ruines par défaut. Une planète très défendue coûte cher à attaquer sans rien rendre en débris.

## Pages liées

- [Missiles](/fr/defense/missiles)
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Tirs rapides](/fr/fleet/rapid-fire)
- [Files de construction](/fr/economy/build-queue)'''
    return f'''# Defenses list

> **In short**: defenses protect your planet around the clock. They never move, cannot be plundered and take part in every battle fought on their planet. The game has 8 of them, two of which are unique (Defensive Barrier and Protective Dome). Missiles are built at the same place but never fight: see [Missiles](/en/defense/missiles).
{{.is-info}}

{box(lang, '', 'the share of destroyed defenses that turns into a debris field may differ from one universe to another.', ('', '0%'), ('', '0%'))}

{box(lang, '', 'the shipyard speed divides the build time of defenses.', ('', '×1'), ('', '×1'))}

## Rules

### Building
1. Defenses are built at the **Orbital Dock**, on a planet or on a moon that has one.
2. While the Orbital Dock is being upgraded, **no defense order** is accepted.
3. Defenses have **their own queue**, separate from the ships' queue: both run at the same time. The queue holds **{QUEUE_FREE} orders** (**{QUEUE_PREMIUM}** with Premium), the running one included (see [Build queues](/en/economy/build-queue)).
4. When you order, the planet must hold the resources for **the whole quantity**. Each unit is then paid when it enters production; if the next unit can no longer be paid, the order stops there.
5. Ordering a defense that is already waiting in the queue adds to that order, without taking another queue slot.
6. **Time per unit**, in seconds, never less than one second:
$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v$$
   - $T$: the defense's base time (table below); $D$: Orbital Dock level; $A$: Molecular Assembler level; $v$: the universe's shipyard speed.
   - Shipyard speed bonuses (dynasty talents, alliance) then divide this time.

### In battle
7. Each defense fires **once per round** and only fights where it is built (planet or moon).
8. Attack, shield and structure grow by **10% per level** of Weapon Systems, Shielding Technology and Armor Technology. In battle, the **hull** is the structure divided by 10.
9. Defenses have **no rapid fire**. Some ships have rapid fire against them (table below).
10. After a battle, part of the destroyed defenses is rebuilt for free: see [Defense rebuild](/en/combat/defense-rebuild). A defense destroyed by a missile is lost (see [Missiles](/en/defense/missiles)).
11. Destroyed defenses leave **no debris field**, unless the universe says otherwise.

### Uniqueness and points
12. **Defensive Barrier and Protective Dome**: one of each per planet. You cannot order more than one at a time, nor order one while there is one on the planet or in the queue.
13. **Points**: each defense earns 1 point per 1,000 resources of its cost (metal, crystal and hydrogen), counted in military points.

## Worked example

**Ordering {q} Ballistic Projectors with an Orbital Dock at level {dock}** (Molecular Assembler 0, speed ×1)
- Cost: {q} × {N(bp[4][0])} = **{N(q * bp[4][0])} metal**, to be on the planet when you order; **{N(q * points(bp))} military points** once built.
- One unit: {N(bp[8])} / (1 + {dock}) = **{N(t1)} seconds**.
- The whole order: {q} × {N(t1)} = {N(tot)} seconds, that is **{dur(tot, lang)}**.

**An Ion Battery in battle** with Weapon Systems 5, Shielding Technology 4 and Armor Technology 6
- Attack: {N(ion[7])} × 1.5 = **{N(w)}**.
- Shield: {N(ion[6])} × 1.4 = **{N(s)}**.
- Hull: {N(ion[5])} × 1.6 / 10 = **{N(h)}**.

## Detailed data

### Costs and base stats (no research)

{T1}

The base time is that of one unit with an Orbital Dock at level 0; the Dock then divides it (rule 6).

### Requirements

{T2}

### Time per unit by Orbital Dock level

Molecular Assembler 0, shipyard speed ×1, no bonus. "no": Dock level too low.

{T3}

Each Molecular Assembler level halves these times again.

### Ships with rapid fire against defenses

{T4}

Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).

## Common pitfalls

- **The Orbital Dock blocks orders while it is upgraded**: queue your defenses before upgrading it.
- **A large order can stop halfway**: each unit is paid in turn. If you spend the resources elsewhere meanwhile, the order stops at the last unit paid.
- **The Orbital Striker is the bane of defenses**: it has rapid fire against almost all of them. Against it, the Plasma Ejector and the two shields hold best.
- **Defenses give the attacker nothing**: by default they leave no debris field. A heavily defended planet is costly to attack and gives nothing back in debris.

## Related pages

- [Missiles](/en/defense/missiles)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Defense rebuild](/en/combat/defense-rebuild)
- [How combat works](/en/combat/how-combat-works)
- [Rapid fire](/en/fleet/rapid-fire)
- [Build queues](/en/economy/build-queue)'''


# ---------------------------------------------------------------- shield domes
def domes(lang):
    N = lambda x: n(x, lang)
    fr = lang == FR
    b, d = BY['defensive_barrier'], BY['protective_dome']
    rows = []
    lab = (['Coût (métal / cristal)', 'Points', 'Structure', 'Coque en combat', 'Bouclier', 'Attaque', 'Durée de base', 'Prérequis', 'Exemplaires',
            'Résistance face aux Ogives (sans recherche)'] if fr else
           ['Cost (metal / crystal)', 'Points', 'Structure', 'Combat hull', 'Shield', 'Attack', 'Base time', 'Requirements', 'Copies',
            'Toughness against Warheads (no research)'])
    vals = []
    for c in (b, d):
        _, _, hull = combat_stats(c)
        vals.append([f'{N(c[4][0])} / {N(c[4][1])}', N(points(c)), N(c[5]), N(hull), N(c[6]), N(c[7]), dur(c[8], lang), req(c, lang), '1', N(resilience(c))])
    for i, l in enumerate(lab):
        rows.append([l, vals[0][i], vals[1][i]])
    T = table(['', nm(b, lang), nm(d, lang)], rows)
    # exemple
    _, ds, dh = combat_stats(d)
    thr = ds // 100
    lf = 50  # attaque de l'Intercepteur (vaisseau light_fighter), table `ship`
    bs = 1000  # attaque du Cuirassé (battleship), table `ship`
    shots = ds // bs
    wh = BY['long_range_warheads'][7]
    need = -(-resilience(d) // wh)
    sh4, sh6 = resilience(d, 6, 6), None
    need6 = -(-sh4 // warhead_damage(4, 1))
    need0 = -(-sh4 // wh)
    if fr:
        return f'''# Barrière défensive et Dôme protecteur

> **En bref** : la Barrière défensive et le Dôme protecteur sont des défenses à très gros bouclier, limitées à un exemplaire chacune par planète. Elles encaissent les tirs pour elles-mêmes : elles ne protègent pas les autres unités.
{{.is-info}}

{img(b, lang, 180)} {img(d, lang, 180)}

## Règles

1. **Un seul exemplaire de chaque** par planète. Une commande ne peut porter que sur une unité, et elle est refusée s'il en existe déjà une sur la planète ou dans la file.
2. En combat, ce sont des **cibles ordinaires** dotées d'un gros bouclier individuel. Elles **ne créent pas de bouclier global** autour de la planète.
3. Elles tirent très peu (attaque {N(b[7])}) : leur rôle est d'absorber des tirs.
4. Un tir inférieur à 1 % de leur bouclier rebondit sans effet (voir [Déroulement d'un combat](/fr/combat/how-combat-works)).
5. Comme toute défense, elles peuvent être reconstruites gratuitement après un combat (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)). Si elles sont perdues, vous pouvez en reconstruire une.
6. Face aux missiles, elles comptent bouclier + coque comme les autres défenses. Sans cible désignée, les Ogives frappent d'abord la défense la plus résistante : souvent le Dôme. Détruites par des Ogives, elles sont perdues (voir [Missiles](/fr/defense/missiles)).

## Exemple chiffré

**Un Dôme protecteur sans recherche** (bouclier {N(ds)}, coque {N(dh)})
- Seuil du 1 % : {N(thr)}. Un Intercepteur (vaisseau, attaque {N(lf)}) est en dessous : **chacun de ses tirs rebondit**, le Dôme ne perd rien.
- Un Cuirassé (attaque {N(bs)}) passe le seuil : {N(shots)} tirs vident le bouclier, les suivants entament la coque.

**Le même Dôme face aux Ogives longue portée**
- Résistance : {N(ds)} + {N(dh)} = **{N(resilience(d))}**. Une Ogive fait {N(wh)} dégâts sans recherche : il en faut **{need}** qui passent les Intercepteurs.
- Avec Champs de Protection 6 et Métallurgie Avancée 6 chez le défenseur, la résistance monte à {N(sh4)} : il faut **{need0}** Ogives à un tireur sans recherche, mais **{need6}** à un tireur à Systèmes Offensifs 4 ({N(warhead_damage(4, 1))} par Ogive).

## Données détaillées

{T}

La durée de base est divisée par (1 + niveau du Dock orbital) et par 2 à chaque niveau d'Assembleur moléculaire (voir [Liste des défenses](/fr/defense/defenses)).

## Pièges fréquents

- **Pas de bulle protectrice** : vos autres défenses et vaisseaux restent exposés.
- **Le Dôme attire les Ogives** : c'est souvent la défense la plus résistante, donc la première visée par une salve sans cible désignée.
- **Pas de deuxième commande en attente** : tant qu'un Dôme est dans la file, un second est refusé.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Missiles](/fr/defense/missiles)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)'''
    return f'''# Defensive Barrier and Protective Dome

> **In short**: the Defensive Barrier and the Protective Dome are defenses with a very large shield, limited to one of each per planet. They soak up shots for themselves only: they do not protect other units.
{{.is-info}}

{img(b, lang, 180)} {img(d, lang, 180)}

## Rules

1. **Only one of each** per planet. An order can only be for one unit, and it is refused if there is already one on the planet or in the queue.
2. In battle they are **ordinary targets** with a large individual shield. They **do not create a global shield** around the planet.
3. They barely fire (attack {N(b[7])}): their job is to absorb shots.
4. A shot below 1% of their shield bounces off with no effect (see [How combat works](/en/combat/how-combat-works)).
5. Like any defense, they can be rebuilt for free after a battle (see [Defense rebuild](/en/combat/defense-rebuild)). If they are lost, you may build another one.
6. Against missiles, they count shield + hull like every other defense. Without a designated target, Warheads hit the toughest defense first: often the Dome. Destroyed by Warheads, they are lost (see [Missiles](/en/defense/missiles)).

## Worked example

**A Protective Dome with no research** (shield {N(ds)}, hull {N(dh)})
- 1% threshold: {N(thr)}. An Interceptor (ship, attack {N(lf)}) falls below it: **every one of its shots bounces**, the Dome loses nothing.
- A Battleship (attack {N(bs)}) clears the threshold: {N(shots)} shots empty the shield, the next ones hit the hull.

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).

**The same Dome against Long-Range Warheads**
- Toughness: {N(ds)} + {N(dh)} = **{N(resilience(d))}**. A Warhead deals {N(wh)} damage with no research: it takes **{need}** that get past the Interception Missiles.
- With Shielding Technology 6 and Armor Technology 6 on the defender's side, toughness rises to {N(sh4)}: a shooter with no research needs **{need0}** Warheads, but one at Weapon Systems 4 ({N(warhead_damage(4, 1))} per Warhead) needs **{need6}**.

## Detailed data

{T}

The base time is divided by (1 + Orbital Dock level) and by 2 for each Molecular Assembler level (see [Defenses list](/en/defense/defenses)).

## Common pitfalls

- **No protective bubble**: your other defenses and ships remain exposed.
- **The Dome draws Warheads**: it is often the toughest defense, hence the first one hit by a salvo with no designated target.
- **No second order in the queue**: while a Dome is in the queue, a second one is refused.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
- [How combat works](/en/combat/how-combat-works)
- [Defense rebuild](/en/combat/defense-rebuild)'''


# ---------------------------------------------------------------- missiles
def missiles(lang):
    N = lambda x: n(x, lang)
    fr = lang == FR
    ic, wh = BY['interceptors'], BY['long_range_warheads']
    # Arsenal
    lvl = 3
    nwh = 10
    # portée et vol
    drive, so = 4, 6
    o, t = (3, 40, 8), (3, 55, 4)
    dist = ring(o[1], t[1], 99)
    rng = missile_range(drive)
    fl_s = flight(dist)
    o2, t2 = (5, 97, 6), (5, 3, 10)
    dist2 = ring(o2[1], t2[1], 99)
    # salve
    fired, icp = 5, 3
    impacting = max(0, fired - icp)
    per = warhead_damage(so, 1)
    pool = warhead_damage(so, impacting)
    shd, arm = 4, 5
    gq = [('protective_dome', 1), ('plasma_ejector', 2), ('ballistic_projector', 40)]
    grid = [(c, resilience(BY[c], shd, arm), q) for c, q in gq]
    res = {c: r for c, r, _ in grid}
    k1, left1 = shatter(pool, grid)
    k2, left2 = shatter(pool, grid, 'plasma_ejector')
    PL = {'protective_dome': ('Dômes protecteurs', 'Protective Domes'), 'plasma_ejector': ('Éjecteurs à plasma', 'Plasma Ejectors'),
          'ballistic_projector': ('Projecteurs balistiques', 'Ballistic Projectors')}
    nm_ = lambda code, k=1: nm(BY[code], lang) if k == 1 else PL[code][0 if fr else 1]

    def steps(kills, start):
        out, p = [], start
        order = [g for g in grid]
        for code, k in kills:
            p2 = p - k * res[code]
            out.append(f'{k} {nm_(code, k)} ({N(k)} × {N(res[code])}) : {N(p)} → {N(p2)}' if fr else f'{k} {nm_(code, k)} ({N(k)} × {N(res[code])}): {N(p)} → {N(p2)}')
            p = p2
        return out

    s1, s2 = steps(k1, pool), steps(k2, pool)
    # tables
    mt = table(['Missile', 'Métal', 'Cristal', 'Hydrogène', 'Points', 'Cases d\'Arsenal', 'Dégâts', 'Durée de base', 'Prérequis'] if fr else
               ['Missile', 'Metal', 'Crystal', 'Hydrogen', 'Points', 'Arsenal slots', 'Damage', 'Base time', 'Requirements'],
               [[img(c, lang) + ' ' + nm(c, lang), *cost3(c, lang), N(points(c)), N(c[11]),
                 (N(c[7]) if c[0] == 'long_range_warheads' else ('aucun' if fr else 'none')), dur(c[8], lang), req(c, lang)] for c in MISSILES])
    st_rows = []
    cum = [0, 0, 0]
    for L in range(1, SILO_MAX + 1):
        cc = silo_cost(L)
        cum = [a + b for a, b in zip(cum, cc)]
        st_rows.append([L, *[N(x) for x in cc], N(silo_slots(L)), N(silo_slots(L) // 2), N(silo_slots(L))])
    stt = table(['Niveau', 'Métal', 'Cristal', 'Hydrogène', 'Cases', 'Ogives au plus', 'Intercepteurs au plus'] if fr else
                ['Level', 'Metal', 'Crystal', 'Hydrogen', 'Slots', 'Warheads at most', 'Interception Missiles at most'], st_rows)
    rg_rows = [[d, N(missile_range(d)), dur(flight(missile_range(d)), lang)] for d in range(1, 11)]
    rgt = table(['Moteur Magnétique', 'Portée (systèmes)', 'Vol jusqu\'à la limite'] if fr else
                ['Impulse Drive', 'Range (systems)', 'Flight to the limit'], rg_rows)
    rs_rows = [[nm(c, lang), N(resilience(c)), N(-(-resilience(c) // wh[7]))] for c in sorted(DEFENSES, key=lambda c: -resilience(c))]
    rst = table(['Défense', 'Résistance (bouclier + coque)', 'Ogives pour une unité'] if fr else
                ['Defense', 'Toughness (shield + hull)', 'Warheads for one unit'], rs_rows)
    killed_txt = lambda kills: ', '.join(f'{k} {nm_(c, k)}' for c, k in kills)

    if fr:
        return f'''# Missiles

> **En bref** : les missiles se stockent dans l'Arsenal balistique. Les **Ogives longue portée** détruisent les défenses d'une planète ennemie de la même galaxie sans engager de flotte ; leur portée dépend du Moteur Magnétique. Les **Intercepteurs** abattent automatiquement, une pour une, les Ogives qui visent votre planète. Les missiles ne prennent jamais part aux combats de flottes.
{{.is-info}}

{box(lang, "la limite d'attaques, qui compte aussi les salves de missiles, peut être différente selon l'univers.", '', (f'{ATTACKS} attaques par {WINDOW_H} h', ''), (f'{ATTACKS} attaques par {WINDOW_H} h', ''))}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Arsenal balistique"> {img(ic, lang, 180)} {img(wh, lang, 180)}

## Règles

### L'Arsenal balistique
1. Les missiles sont stockés dans l'**Arsenal balistique**, qui offre **{SLOTS_PER_LEVEL} cases par niveau** (niveau {SILO_MAX} au plus). Il ne se construit que sur une planète.
2. Un **Intercepteur** occupe **{ic[11]} case**, une **Ogive longue portée** en occupe **{wh[11]}**.
3. Les missiles en file d'attente ou en construction comptent déjà : une commande qui ne tiendrait pas dans les cases libres est refusée avant toute dépense.
4. Les missiles n'occupent aucune case de la planète. Seul l'Arsenal lui-même occupe une case par niveau.
5. Démolir un niveau d'Arsenal alors qu'il est plein ne détruit aucun missile ; vous ne pouvez simplement plus en commander.
6. Les missiles ne tirent jamais pendant un combat, ne comptent pas dans la puissance défensive de la planète et ne peuvent pas être détruits par une salve.
7. **Points** : comme les défenses, 1 point par tranche de 1 000 ressources, dans les points militaires, tant qu'ils sont au silo. Un missile tiré, ou un Intercepteur consommé, sort de vos points.

### Portée et vol
8. **Portée** : avec le Moteur Magnétique au niveau $N$, une Ogive atteint toute planète située à au plus $5 \\times N - 1$ systèmes, **dans la même galaxie** seulement.
   - $N$ : votre niveau de Moteur Magnétique. Une autre galaxie est toujours hors de portée, quel que soit le niveau.
9. Les systèmes d'une galaxie forment un anneau : le système 99 est voisin du système 1. La distance se compte par le plus court côté. La position dans le système ne compte pas.
10. **Durée du vol** : 30 secondes par système de distance, et 30 secondes au moins (même système). La cible n'est **pas prévenue** avant l'impact.
11. Une salve **ne peut pas être rappelée**. Les Ogives quittent le silo au lancement et ne reviennent jamais, même si la planète visée est abandonnée entre-temps.

### Cibles et restrictions
12. Une salve part d'une planète et vise une **planète** : jamais une lune, ni une case vide, ni l'une de vos planètes.
13. Interdit sur un membre de votre alliance, sur un joueur **en mode vacances** et sur un joueur protégé ([Protection des débutants](/fr/players/beginner-protection)). Vous ne pouvez pas tirer pendant vos propres vacances.
14. Une salve **compte comme une attaque** dans la [limite d'attaques](/fr/players/attack-limit) sur le joueur visé. Comme elle ne se rappelle pas, le créneau est consommé.
15. Tirer **met fin à votre propre protection de nouveau joueur**, définitivement.
16. Une planète abandonnée peut être visée : personne ne la défend, la limite d'attaques ne s'applique pas.
17. Pendant une **maintenance**, aucun tir n'est accepté ; une salve déjà en vol arrive normalement.

### À l'impact
18. **Interception** : chaque Intercepteur de la planète visée abat **une Ogive**, automatiquement, avant tout dégât. Il est consommé.
19. **Dégâts** : chaque Ogive qui passe apporte $12\\,000 \\times (1 + 0{{,}}1 \\times S)$ dégâts, mis en commun pour toute la salve (arrondi à l'inférieur).
   - $S$ : niveau de Systèmes Offensifs du tireur.
20. **Résistance** d'une défense : son bouclier + sa coque de combat, avec les recherches et bonus du défenseur (voir [Liste des défenses](/fr/defense/defenses), règle 8).
21. **Ordre des cibles** : la cible désignée d'abord (si la planète en a), puis les défenses par résistance décroissante. Sans cible désignée, la plus résistante d'abord.
22. Une défense n'est détruite qu'**entière**. Sur chaque ligne, la salve détruit autant d'unités que ses dégâts restants en paient ; si elle ne peut plus en payer une seule, elle passe à la ligne suivante, moins résistante. Ce qui reste à la fin est perdu.
23. Une salve **ne détruit que des défenses** : jamais les bâtiments, la flotte en orbite, les ressources ni les missiles du silo.
24. Les défenses détruites par une Ogive sont **perdues définitivement** : pas de reconstruction gratuite. Leurs points sont retirés.
25. Le tireur et le défenseur reçoivent un rapport : Ogives tirées, interceptées, arrivées, défenses touchées et planète d'origine.
26. Certains talents de dynastie modifient la portée, la capacité de l'Arsenal, les dégâts et l'interception (voir [Dynastie et talents](/fr/dynasty)).

## Exemple chiffré

**Remplir un Arsenal balistique niveau {lvl}**
- Capacité : {lvl} × {SLOTS_PER_LEVEL} = **{N(silo_slots(lvl))} cases**.
- {nwh} Intercepteurs ({nwh} cases) + {nwh} Ogives longue portée ({nwh * wh[11]} cases) = {nwh + nwh * wh[11]} : l'Arsenal est plein.
- Coût des {nwh} Ogives : {N(nwh * wh[4][0])} métal, {N(nwh * wh[4][1])} cristal, {N(nwh * wh[4][2])} hydrogène, soit {N(nwh * points(wh))} points militaires, retirés quand elles partent.

**Portée et vol** (Moteur Magnétique {drive})
- Portée : 5 × {drive} − 1 = **{rng} systèmes**.
- De [{o[0]}:{o[1]}:{o[2]}] vers [{t[0]}:{t[1]}:{t[2]}] : {dist} systèmes, à portée. Vol : {dist} × 30 = {N(fl_s)} secondes, soit **{dur(fl_s, lang)}**.
- De [{o2[0]}:{o2[1]}:{o2[2]}] vers [{o2[0]}:{t2[1]}:{t2[2]}] : l'anneau passe par 98, 99, 1, 2, 3, soit **{dist2} systèmes**, à portée dès le Moteur Magnétique 2 ; vol de {dur(flight(dist2), lang)}.
- Vers [4:40:8] : autre galaxie, **hors de portée**.

**Une salve de {fired} Ogives** tirée avec Systèmes Offensifs {so}, sur une planète qui a {icp} Intercepteurs, 1 Dôme protecteur, 2 Éjecteurs à plasma et 40 Projecteurs balistiques (défenseur à Champs de Protection {shd} et Métallurgie Avancée {arm})
- Interception : {icp} Ogives abattues, **{impacting} arrivent**. Les {icp} Intercepteurs sont consommés.
- Dégâts : {impacting} × 12 000 × {n(1 + 0.1 * so, lang)} = **{N(pool)}**.
- Résistances : Dôme {N(res['protective_dome'])}, Éjecteur à plasma {N(res['plasma_ejector'])}, Projecteur balistique {N(res['ballistic_projector'])}.
- Sans cible désignée : {('; ' if not fr else ' ; ').join(s1)}. Les Éjecteurs (il faudrait {N(res['plasma_ejector'])}) sont sautés. Bilan : **{killed_txt(k1)}**, {N(left1)} dégâts perdus.
- Cible désignée « Éjecteur à plasma » : {('; ' if not fr else ' ; ').join(s2)}. Le Dôme est sauté. Bilan : **{killed_txt(k2)}**, {N(left2)} dégâts perdus.

## Données détaillées

### Missiles

{mt}

Les dégâts sont ceux d'une Ogive sans recherche (règle 19). Un Intercepteur ne fait aucun dégât : il ne sert qu'à abattre une Ogive. Le Moteur Magnétique 1 requis pour les Ogives donne déjà une portée de {missile_range(1)} systèmes.

### Arsenal balistique

Prérequis : Dock orbital 1. Le coût double à chaque niveau.

{stt}

### Portée selon le Moteur Magnétique

{rgt}

Sur Redline, une galaxie compte 99 systèmes : par le plus court côté de l'anneau, aucun n'est à plus de 49 systèmes. Le niveau 10 couvre donc toute votre galaxie.

### Résistance des défenses face aux Ogives (sans recherche du défenseur)

{rst}

« Ogives pour une unité » : Ogives arrivées nécessaires, sans recherche chez le tireur, pour détruire une unité seule.

## Pièges fréquents

- **« Intercepteurs » n'est pas l'« Intercepteur »** : le missile (pluriel) et le vaisseau de combat (singulier) n'ont rien à voir.
- **Pas de missile entre galaxies** : la portée ne compte que les systèmes de votre galaxie.
- **Le Dôme part en premier** : sans cible désignée, la défense la plus résistante est frappée d'abord. Désignez une cible si vous visez autre chose.
- **Une salve trop faible passe à côté** : une Ogive seule ne détruit pas un Dôme sans recherche ; ses dégâts vont aux défenses suivantes.
- **Une salve coûte un créneau d'attaque** : elle compte dans la limite d'attaques sur le joueur, même si elle ne détruit rien.
- **Fin de la protection de nouveau joueur** : votre première salve y met fin, comme une attaque de flotte.
- **Les missiles ne défendent pas contre les flottes** : seuls les Intercepteurs servent en défense, et uniquement contre les Ogives.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Barrière défensive et Dôme protecteur](/fr/defense/shield-domes)
- [Limite d'attaques](/fr/players/attack-limit)
- [Protection des débutants](/fr/players/beginner-protection)
- [Mode vacances](/fr/players/vacation-mode)
- [Maintenance](/fr/misc/maintenance)'''
    return f'''# Missiles

> **In short**: missiles are stored in the Ballistic Arsenal. **Long-Range Warheads** destroy the defenses of an enemy planet in the same galaxy without sending a fleet; their range depends on the Impulse Drive. **Interception Missiles** automatically shoot down, one for one, the Warheads aimed at your planet. Missiles never take part in fleet battles.
{{.is-info}}

{box(lang, '', 'the attack limit, which also counts missile salvos, may differ from one universe to another.', ('', f'{ATTACKS} attacks per {WINDOW_H} h'), ('', f'{ATTACKS} attacks per {WINDOW_H} h'))}

<img src="/images/illustrations/facilities/arsenal-balistique.jpg" width="180" alt="Ballistic Arsenal"> {img(ic, lang, 180)} {img(wh, lang, 180)}

## Rules

### The Ballistic Arsenal
1. Missiles are stored in the **Ballistic Arsenal**, which offers **{SLOTS_PER_LEVEL} slots per level** (level {SILO_MAX} at most). It can only be built on a planet.
2. An **Interception Missile** takes **{ic[11]} slot**, a **Long-Range Warhead** takes **{wh[11]}**.
3. Missiles in the queue or under construction already count: an order that would not fit in the free slots is refused before anything is spent.
4. Missiles take no planet fields. Only the Arsenal itself takes one field per level.
5. Demolishing an Arsenal level while it is full destroys no missile; you just cannot order more.
6. Missiles never fire during a battle, do not count towards the planet's defensive power and cannot be destroyed by a salvo.
7. **Points**: like defenses, 1 point per 1,000 resources, in military points, while they sit in the silo. A missile fired, or an Interception Missile spent, leaves your points.

### Range and flight
8. **Range**: with the Impulse Drive at level $N$, a Warhead reaches any planet at most $5 \\times N - 1$ systems away, **in the same galaxy** only.
   - $N$: your Impulse Drive level. Another galaxy is always out of range, whatever the level.
9. The systems of a galaxy form a ring: system 99 is next to system 1. The distance is counted the short way round. The position within the system does not matter.
10. **Flight time**: 30 seconds per system of distance, and 30 seconds at least (same system). The target gets **no warning** before impact.
11. A salvo **cannot be recalled**. Warheads leave the silo at launch and never come back, even if the target planet is abandoned in the meantime.

### Targets and restrictions
12. A salvo leaves from a planet and targets a **planet**: never a moon, an empty slot or one of your own planets.
13. Forbidden against a member of your alliance, a player **in vacation mode** and a protected player ([Beginner protection](/en/players/beginner-protection)). You cannot fire during your own vacation.
14. A salvo **counts as an attack** in the [attack limit](/en/players/attack-limit) on the targeted player. Since it cannot be recalled, the slot is spent.
15. Firing **ends your own new-player protection**, for good.
16. An abandoned planet can be targeted: nobody defends it, and the attack limit does not apply.
17. During **maintenance**, no launch is accepted; a salvo already in flight lands normally.

### On impact
18. **Interception**: each Interception Missile on the target planet shoots down **one Warhead**, automatically, before any damage. It is spent.
19. **Damage**: each Warhead that gets through brings $12{{,}}000 \\times (1 + 0.1 \\times S)$ damage, pooled for the whole salvo (rounded down).
   - $S$: the shooter's Weapon Systems level.
20. **Toughness** of a defense: its shield + its combat hull, with the defender's research and bonuses (see [Defenses list](/en/defense/defenses), rule 8).
21. **Target order**: the designated target first (if the planet has any), then defenses by decreasing toughness. Without a designated target, the toughest first.
22. A defense is only destroyed **whole**. On each line, the salvo destroys as many units as its remaining damage pays for; if it cannot pay for a single one, it moves on to the next, less tough line. Whatever is left at the end is lost.
23. A salvo **only destroys defenses**: never buildings, the fleet in orbit, resources or the missiles in the silo.
24. Defenses destroyed by a Warhead are **lost for good**: no free rebuild. Their points are removed.
25. Both the shooter and the defender get a report: Warheads fired, intercepted, landed, defenses hit and planet of origin.
26. Some dynasty talents change the range, the Arsenal capacity, the damage and the interception (see [Dynasty and talents](/en/dynasty)).

## Worked example

**Filling a level {lvl} Ballistic Arsenal**
- Capacity: {lvl} × {SLOTS_PER_LEVEL} = **{N(silo_slots(lvl))} slots**.
- {nwh} Interception Missiles ({nwh} slots) + {nwh} Long-Range Warheads ({nwh * wh[11]} slots) = {nwh + nwh * wh[11]}: the Arsenal is full.
- Cost of the {nwh} Warheads: {N(nwh * wh[4][0])} metal, {N(nwh * wh[4][1])} crystal, {N(nwh * wh[4][2])} hydrogen, that is {N(nwh * points(wh))} military points, removed when they leave.

**Range and flight** (Impulse Drive {drive})
- Range: 5 × {drive} − 1 = **{rng} systems**.
- From [{o[0]}:{o[1]}:{o[2]}] to [{t[0]}:{t[1]}:{t[2]}]: {dist} systems, in range. Flight: {dist} × 30 = {N(fl_s)} seconds, that is **{dur(fl_s, lang)}**.
- From [{o2[0]}:{o2[1]}:{o2[2]}] to [{o2[0]}:{t2[1]}:{t2[2]}]: the ring goes through 98, 99, 1, 2, 3, that is **{dist2} systems**, in range from Impulse Drive 2; flight of {dur(flight(dist2), lang)}.
- To [4:40:8]: another galaxy, **out of range**.

**A salvo of {fired} Warheads** fired with Weapon Systems {so}, at a planet holding {icp} Interception Missiles, 1 Protective Dome, 2 Plasma Ejectors and 40 Ballistic Projectors (defender at Shielding Technology {shd} and Armor Technology {arm})
- Interception: {icp} Warheads shot down, **{impacting} land**. The {icp} Interception Missiles are spent.
- Damage: {impacting} × 12,000 × {n(1 + 0.1 * so, lang)} = **{N(pool)}**.
- Toughness: Dome {N(res['protective_dome'])}, Plasma Ejector {N(res['plasma_ejector'])}, Ballistic Projector {N(res['ballistic_projector'])}.
- No designated target: {('; ' if not fr else ' ; ').join(s1)}. The Ejectors (one would take {N(res['plasma_ejector'])}) are skipped. Result: **{killed_txt(k1)}**, {N(left1)} damage lost.
- Designated target "Plasma Ejector": {('; ' if not fr else ' ; ').join(s2)}. The Dome is skipped. Result: **{killed_txt(k2)}**, {N(left2)} damage lost.

## Detailed data

### Missiles

{mt}

Damage is that of one Warhead with no research (rule 19). An Interception Missile deals no damage: it only shoots down a Warhead. The Impulse Drive 1 required for Warheads already gives a range of {missile_range(1)} systems.

### Ballistic Arsenal

Requirement: Orbital Dock 1. The cost doubles at each level.

{stt}

### Range by Impulse Drive level

{rgt}

On Redline a galaxy has 99 systems: the short way round the ring, none is more than 49 systems away. Level 10 therefore covers your whole galaxy.

### Defense toughness against Warheads (no defender research)

{rst}

"Warheads for one unit": Warheads landing, with no shooter research, needed to destroy a single unit.

## Common pitfalls

- **"Interception Missile" is not the "Interceptor"**: the missile and the combat ship have nothing in common. The game shows the missile as "Interceptors".
- **No missile across galaxies**: range only counts systems in your own galaxy.
- **The Dome goes first**: without a designated target, the toughest defense is hit first. Designate a target if you are after something else.
- **A salvo too weak goes past**: a single Warhead does not destroy a Dome with no research; its damage goes to the next defenses.
- **A salvo costs an attack slot**: it counts in the attack limit on the player, even if it destroys nothing.
- **End of new-player protection**: your first salvo ends it, just like a fleet attack.
- **Missiles do not defend against fleets**: only Interception Missiles help in defense, and only against Warheads.

## Related pages

- [Defenses list](/en/defense/defenses)
- [Defensive Barrier and Protective Dome](/en/defense/shield-domes)
- [Attack limit](/en/players/attack-limit)
- [Beginner protection](/en/players/beginner-protection)
- [Vacation mode](/en/players/vacation-mode)
- [Maintenance](/en/misc/maintenance)'''


if __name__ == '__main__':
    for lang in (FR, EN):
        write(lang, 'defense', index(lang))
        write(lang, 'defense/defenses', defenses(lang))
        write(lang, 'defense/shield-domes', domes(lang))
        write(lang, 'defense/missiles', missiles(lang))
