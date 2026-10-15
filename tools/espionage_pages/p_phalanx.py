import sys; sys.path.insert(0, sys.argv[1])
from esp_lib import *; from write import *

LV = 4
R = phalanx_range(LV)
mid = spans(covered_systems(50, LV))
edge = spans(covered_systems(5, LV))
assert R == 15 and mid == [(35, 65)] and edge == [(1, 20), (89, 99)]
assert 60 in covered_systems(50, LV) and 70 not in covered_systems(50, LV)
LEVELS = range(1, 11)


def body(lang):
    N = lambda x: n(x, lang)
    sp = lambda s: (f'{s[0]} à {s[1]}' if lang == 'fr' else f'{s[0]} to {s[1]}')
    rows = [[l, N(phalanx_range(l)), *[N(c) for c in phalanx_cost(l)]] for l in LEVELS]
    if lang == 'fr':
        return f'''# Phalange de capteur

> **En bref** : la Phalange de capteur se construit sur une lune. Elle balaie une planète de la même galaxie et montre toutes les flottes en route qui en partent ou s'y dirigent : composition, mission et horaires. Chaque balayage coûte {N(PHALANX_SCAN_COST)} hydrogène, pris sur la lune.
{{.is-info}}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Phalange de capteur">

> **Paramètre d'univers** : le nombre de systèmes par galaxie peut être différent selon l'univers.
> Par défaut : **fixé à la création de l'univers** · Redline : **{REDLINE_SYSTEMS} systèmes**
{{.is-info}}

## Règles

### Construire

1. La Phalange se construit **uniquement sur une lune**, après la **Base lunaire niveau 1**.
2. Le niveau N coûte {N(PHALANX_BASE_COST[0])} métal, {N(PHALANX_BASE_COST[1])} cristal et {N(PHALANX_BASE_COST[2])} hydrogène, multipliés par 2 à chaque niveau (× 2^(N − 1)). Elle n'a pas de niveau maximum : seules les cases de la lune la limitent.

### Balayer

3. La Phalange balaie une **planète** de la **même galaxie**, à portée. Elle ne peut **jamais viser une lune**.
4. **Portée** = niveau² − 1 systèmes de part et d'autre de la lune, au minimum 1.
5. La galaxie **boucle** sur ses systèmes : le dernier système est voisin du premier. Une lune proche d'un bord voit donc aussi les systèmes de l'autre bout.
6. Chaque balayage coûte **{N(PHALANX_SCAN_COST)} hydrogène**, pris sur la lune, même si aucune flotte n'est trouvée.
7. Un balayage refusé (hors de portée, autre galaxie, lune visée, hydrogène insuffisant) ne coûte rien.
8. Vous ne pouvez pas balayer si vous êtes en mode vacances.

### Ce que montre le balayage

9. Toutes les flottes **en route** qui ont la planète pour **départ ou destination**, à l'aller comme au retour, y compris les flottes ennemies : leurs **vaisseaux**, leur **mission**, leur départ et leur destination, et leurs **heures de départ et d'arrivée**.
10. La **cargaison** reste invisible.
11. Les missions **Espionnage** et **Recyclage** n'apparaissent pas.
12. Les flottes qui partent de la **lune** de cette planète ou s'y rendent n'apparaissent pas non plus.
13. Le joueur balayé **n'est pas prévenu**.
14. Certains talents de dynastie modifient la Phalange (portée, coût, balayage prolongé, mémoire) ou la trompent : voir l'[Oracle](/fr/dynasty/classes/oracle) et l'[Ombre](/fr/dynasty/classes/shadow).

## Exemple chiffré

Votre lune est en [3:50:8] avec une Phalange niveau {LV}, dans une galaxie de {REDLINE_SYSTEMS} systèmes.
- Portée : {LV}² − 1 = **{R} systèmes** de part et d'autre, soit les systèmes **{sp(mid[0])}** de la galaxie 3.
- Vous pouvez balayer une planète en [3:60:5] pour {N(PHALANX_SCAN_COST)} hydrogène.
- Une planète en [3:70:5] est hors de portée. Une planète en [4:50:5] est dans une autre galaxie : impossible.
- Près du bord, la portée continue de l'autre côté : depuis [3:5:8], la même Phalange couvre les systèmes **{sp(edge[0])}** et **{sp(edge[1])}**.

## Données détaillées

{table(['Niveau', 'Portée (systèmes de chaque côté)', 'Métal', 'Cristal', 'Hydrogène'], rows)}

## Pièges fréquents

- **Une flotte stationnée sur une lune échappe à la Phalange** : une lune ne se balaie pas, et le trafic de la lune n'apparaît pas sur le balayage de sa planète.
- **Le balayage est payé même vide** : {N(PHALANX_SCAN_COST)} hydrogène à chaque fois.
- **Prévoir l'hydrogène sur la lune** : le coût est prélevé sur la lune, qui ne produit rien. Apportez-y l'hydrogène par transport.
- **Pas de balayage d'une autre galaxie**, quel que soit le niveau.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Porte de saut](/fr/fleet/jump-gate)
- [Espionner](/fr/espionage/spying)
- [Coordonnées](/fr/universe/coordinates)
'''
    return f'''# Sensor phalanx

> **In short**: the Sensor phalanx is built on a moon. It sweeps a planet of the same galaxy and shows every fleet under way leaving it or heading for it: composition, mission and times. Each sweep costs {N(PHALANX_SCAN_COST)} hydrogen, taken from the moon.
{{.is-info}}

<img src="/images/illustrations/facilities/phalange-de-capteur.jpg" width="180" alt="Sensor phalanx">

> **Universe setting**: the number of systems per galaxy may differ from one universe to another.
> Default: **set when the universe is created** · Redline: **{REDLINE_SYSTEMS} systems**
{{.is-info}}

## Rules

### Building

1. The Phalanx can be built **only on a moon**, after **Lunar base level 1**.
2. Level N costs {N(PHALANX_BASE_COST[0])} metal, {N(PHALANX_BASE_COST[1])} crystal and {N(PHALANX_BASE_COST[2])} hydrogen, doubled at each level (× 2^(N − 1)). It has no maximum level: only the moon's fields limit it.

### Sweeping

3. The Phalanx sweeps a **planet** in the **same galaxy**, within range. It can **never target a moon**.
4. **Range** = level² − 1 systems on each side of the moon, at least 1.
5. The galaxy **wraps around** its systems: the last system is next to the first. A moon near one end therefore also sees the systems at the other end.
6. Each sweep costs **{N(PHALANX_SCAN_COST)} hydrogen**, taken from the moon, even if no fleet is found.
7. A refused sweep (out of range, other galaxy, moon targeted, not enough hydrogen) costs nothing.
8. You cannot sweep while you are on vacation.

### What the sweep shows

9. Every fleet **under way** whose **departure or destination** is the planet, outbound or returning, enemy fleets included: their **ships**, their **mission**, where they leave from and where they go, and their **departure and arrival times**.
10. The **cargo** stays hidden.
11. **Espionage** and **Recycling** missions do not show.
12. Fleets leaving the planet's **moon** or heading for it do not show either.
13. The swept player **is not warned**.
14. Some dynasty talents change the Phalanx (range, cost, extended sweep, memory) or fool it: see the [Oracle](/en/dynasty/classes/oracle) and the [Shadow](/en/dynasty/classes/shadow).

## Worked example

Your moon is at [3:50:8] with a level {LV} Phalanx, in a galaxy of {REDLINE_SYSTEMS} systems.
- Range: {LV}² − 1 = **{R} systems** on each side, i.e. systems **{sp(mid[0])}** of galaxy 3.
- You can sweep a planet at [3:60:5] for {N(PHALANX_SCAN_COST)} hydrogen.
- A planet at [3:70:5] is out of range. A planet at [4:50:5] is in another galaxy: impossible.
- Near the edge, the range carries on from the other end: from [3:5:8], the same Phalanx covers systems **{sp(edge[0])}** and **{sp(edge[1])}**.

## Detailed data

{table(['Level', 'Range (systems on each side)', 'Metal', 'Crystal', 'Hydrogen'], rows)}

## Common pitfalls

- **A fleet stationed on a moon escapes the Phalanx**: a moon cannot be swept, and the moon's traffic does not show on its planet's sweep.
- **The sweep is paid even when empty**: {N(PHALANX_SCAN_COST)} hydrogen every time.
- **Keep hydrogen on the moon**: the cost is taken from the moon, which produces nothing. Bring hydrogen there by transport.
- **No sweeping another galaxy**, whatever the level.

## Related pages

- [Moons](/en/universe/moons)
- [Jump gate](/en/fleet/jump-gate)
- [Spying](/en/espionage/spying)
- [Coordinates](/en/universe/coordinates)
'''


for lang in ('fr', 'en'):
    write(lang, 'espionage/sensor-phalanx', body(lang),
          description='Observer les flottes depuis une lune : portée, coût, ce qui est vu.' if lang == 'fr'
          else 'Watching fleets from a moon: range, cost, what is seen.')
