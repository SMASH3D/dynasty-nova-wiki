import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    lv = {'combustion_drive': 6}
    fleet = [('light_fighter', 10)]
    d = distance(0, ring(40, 50, 99), 0)
    v = speed('light_fighter', lv)
    rows = []
    res = {}
    for p in (100, 50, 10):
        t = duration(d, p, v); f = leg_fuel(d, p, fleet, lv)
        res[p] = (t, f)
        rows.append([pct(p, lang), f'{N(t)} s ({hms(t, lang)})', N(f), N(2 * f)])
    T1 = table(['Vitesse', "Durée d'un trajet", "Hydrogène d'un trajet", 'Payé au départ (aller-retour)'] if fr
               else ['Speed', 'One-way time', 'One-way hydrogen', 'Paid at departure (round trip)'], rows)
    save = round(100 * (1 - res[50][1] / res[100][1]))
    # Carte circulaire
    g = ring(1, 9, 9); s_ = ring(3, 97, 99)
    dg, ds = distance(g, 0, 0), distance(0, s_, 0)
    # Moteurs
    drv = {}
    for s in SHIPS:
        if s[5]:
            drv.setdefault(s[5], []).append(s[1] if fr else f'*{s[2]}*')
    names = {'combustion': RES['combustion_drive'], 'impulse': RES['impulse_drive'], 'hyperspace': RES['hyperspace_drive']}
    T2 = table(['Moteur', 'Bonus par niveau', "Vaisseaux (moteur d'origine)"] if fr else ['Drive', 'Bonus per level', 'Ships (built-in drive)'],
               [[names[k][0 if fr else 1], '+' + pct(int(DRIVE[k][1] * 100), lang), ', '.join(drv[k])] for k in ('combustion', 'impulse', 'hyperspace')])
    if fr:
        return f'''# Déplacements

> **En bref** : la durée d'un vol dépend de la distance, de la vitesse du vaisseau le plus lent et de la vitesse choisie, de 1 à 100 %. Sa consommation d'hydrogène dépend de la distance, des vaisseaux envoyés et de la vitesse. Voler moins vite coûte beaucoup moins cher. L'hydrogène du voyage voyage dans les soutes, avec la cargaison.
{{.is-info}}

> **Paramètre d'univers** : la vitesse des flottes divise la durée des vols. Elle ne change pas la consommation.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

## Règles

### Emplacements de flotte
1. Le nombre de flottes en vol en même temps est limité : **emplacements de flotte = 1 + niveau de Calcul Quantique**, plus jusqu'à 3 emplacements de talents (dont un réservé aux attaques pour l'Amiral). Voir [Les talents](/fr/dynasty/talents).
2. Une flotte occupe son emplacement de son départ à son retour. Les expéditions, y compris pendant leur maintien, et les dépôts à la Station stellaire en occupent un. Les missiles et les sauts par [Porte de saut](/fr/fleet/jump-gate) n'en occupent pas. Le Navigateur dispose en plus de navettes, hors emplacements, pour les transports et stationnements entre ses propres bases.

### Vitesse
3. Vitesse d'un vaisseau = vitesse de base de son moteur × (1 + bonus × niveau de la recherche de ce moteur) : **+10 %** par niveau de Propulseur Chimique, **+20 %** de Moteur Magnétique, **+30 %** de Navigation Transdimensionnelle. Certains vaisseaux changent de moteur avec la recherche (voir [Liste des vaisseaux](/fr/fleet/ships)).
4. Une flotte avance à la vitesse de son **vaisseau le plus lent**.
5. Vous choisissez une **vitesse de 1 à 100 %**, par pas de 1 %. Dans les formules, elle devient la fraction $s$ : $s = 1$ à 100 %, $s = 0,5$ à 50 %.

### Distance
6. La distance dépend de ce qui diffère entre le départ et l'arrivée :

| Trajet | Distance |
|---|---|
| Vers une autre galaxie | 20 000 × écart entre les galaxies |
| Même galaxie, autre système | 2 700 + 95 × écart entre les systèmes |
| Même système, autre position | 1 000 + 5 × écart entre les positions |
| Entre une planète et sa lune | 5 |

7. **La carte est circulaire** pour les galaxies et pour les systèmes : l'écart se compte par le plus court chemin, en passant au besoin par le bord. Sur Redline, la galaxie 9 est voisine de la galaxie 1, et le système 99 du système 1. Les positions, elles, ne bouclent pas.

### Durée
8. Durée d'un trajet, en secondes, arrondie, au moins 1 :

$$
T = \\frac{{10 + \\frac{{3\\,500}}{{s}}\\sqrt{{\\frac{{10 \\times D}}{{V}}}}}}{{A \\times B}}
$$

- $T$ : durée du trajet, en secondes ;
- $s$ : vitesse choisie, en fraction (de 0,01 pour 1 % à 1 pour 100 %) ;
- $D$ : distance du trajet (règle 6) ;
- $V$ : vitesse du vaisseau le plus lent de la flotte ;
- $A$ : vitesse des flottes de l'univers ;
- $B$ : bonus de vitesse, 1 sans bonus (règle 13).

### Consommation d'hydrogène
9. Consommation d'un trajet, arrondie à l'inférieur, au moins 1 dès qu'un vaisseau consomme :

$$
U = \\sum_i \\frac{{F_i \\times N_i \\times D}}{{35\\,000}} \\left( s \\sqrt{{\\frac{{V}}{{V_i}}}} + 1 \\right)^2
$$

- $U$ : hydrogène du trajet ;
- $F_i$ : consommation d'un vaisseau du type $i$, celle de son moteur actuel ;
- $N_i$ : nombre de vaisseaux du type $i$ ;
- $D$ : distance du trajet ;
- $s$ : vitesse choisie, en fraction ;
- $V$ : vitesse du vaisseau le plus lent de la flotte ;
- $V_i$ : vitesse du type de vaisseau $i$.

10. Un vaisseau plus rapide que le reste de sa flotte consomme moins. Aucune recherche ne réduit la consommation ; un meilleur moteur l'augmente.
11. **Le retour est payé au départ** : chaque trajet est compté séparément, aller puis retour, pour toutes les missions sauf **Colonisation** et **Stationnement**, qui sont des allers simples. Les dépôts à la Station stellaire ne consomment rien.
12. **L'hydrogène du voyage voyage dans les soutes** : cargaison + hydrogène du voyage ne doivent pas dépasser le fret de la flotte. Un talent du Navigateur allège ce carburant.

### Bonus
13. Les bonus de vitesse (talents personnels et talent d'alliance Propulsion coordonnée, +5 % par niveau) **divisent la durée** : +50 % = un trajet 1,5 fois plus court. Ensemble, ils plafonnent à **+60 %** ; quelques talents de trajet s'ajoutent hors plafond (retour, trajets entre vos bases, rappel).
14. Les baisses de consommation (talents personnels et talent d'alliance Ravitaillement optimisé, 5 % par niveau) plafonnent ensemble à **45 %**, sans jamais descendre sous 1 par trajet.

### Rappel et retour
15. Une flotte peut être **rappelée** tant qu'elle est à l'aller ou en maintien d'expédition, pas sur le chemin du retour. Les dépôts à la Station stellaire ne se rappellent pas.
16. Une flotte rappelée rentre en autant de temps qu'elle en a déjà passé à l'aller ; une expédition rappelée pendant son maintien refait tout le trajet. Le rappel **ne rembourse pas** l'hydrogène (sauf talent du Navigateur). Une attaque rappelée ne compte plus dans la [limite d'attaques](/fr/players/attack-limit).
17. Au retour, la flotte se pose sur sa base de départ, avec sa cargaison, même au-delà de la capacité des entrepôts. **Il faut que cette base vous appartienne encore et ait un Dock orbital** : sinon, la flotte est perdue.

## Exemple chiffré

10 Intercepteurs (vitesse 12 500 × 1,6 = {N(v)} avec Propulseur Chimique 6, consommation 20 chacun) attaquent de [2:40:8] vers [2:50:3]. Distance : 2 700 + 95 × 10 = **{N(d)}**.

{T1}

Par exemple à 100 % : 10 + 3 500 / 1 × √(10 × {N(d)} / {N(v)}) ≈ {N(res[100][0])} s, et 20 × 10 × {N(d)} / 35 000 × (1 + 1)² ≈ {N(res[100][1])} hydrogène. À mi-vitesse, le vol dure deux fois plus longtemps mais coûte **{save} % d'hydrogène en moins**.

**Carte circulaire** : de la galaxie 1 à la galaxie 9 sur Redline, l'écart est de {g} galaxie, soit une distance de {N(dg)}, et non 8 × 20 000. Du système 3 au système 97 d'une même galaxie, l'écart est de {s_} systèmes : distance {N(ds)}.

## Données détaillées

### Moteurs

{T2}

Les vitesses, consommations et changements de moteur sont sur la page [Liste des vaisseaux](/fr/fleet/ships).

### Ordres de vol des talents

Des talents ajoutent des ordres de vol : changer de vitesse en vol (Relance à 100 %, Mise en attente jusqu'à 10 %), Port d'attache, Fret retour, Livraison groupée, Ordre de chargement, Postcombustion, Redirection, Saut de retour. Ils sont décrits sur [Les talents](/fr/dynasty/talents) et l'arbre du [Navigateur](/fr/dynasty/classes/navigator).

## Pièges fréquents

- **Le plus lent impose son rythme** : un seul Récupérateur (vitesse 2 000) ralentit toute une flotte d'Intercepteurs.
- **Le retour se paie au départ** : prévoyez l'hydrogène de l'aller-retour avant d'attaquer, et la place dans les soutes pour le transporter.
- **Rappeler ne rembourse rien** : l'hydrogène dépensé est perdu.
- **Ne retirez pas le Dock orbital d'une base qui attend une flotte** : sans Dock à l'arrivée, la flotte qui rentre est perdue.
- **Pensez au bord de la carte** : la galaxie la plus proche n'est pas toujours celle qu'on croit.
- **Calcul Quantique limite vos flottes** : au niveau 2, seulement 3 flottes en vol, expéditions et dépôts compris.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Les missions](/fr/fleet/missions)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Expéditions](/fr/fleet/expeditions)
- [Porte de saut](/fr/fleet/jump-gate)
- [Missions et station d'alliance](/fr/players/alliance-missions)
'''
    return f'''# Fleet movement

> **In short**: a flight's duration depends on the distance, the speed of the slowest ship and the speed you choose, from 1 to 100%. Its hydrogen use depends on the distance, the ships sent and the speed. Flying slower costs much less. The trip's hydrogen travels in the holds, with the cargo.
{{.is-info}}

> **Universe setting**: the fleet speed divides flight durations. It does not change consumption.
> Default: **×1** · Redline: **×1**
{{.is-info}}

## Rules

### Fleet slots
1. The number of fleets flying at once is capped: **fleet slots = 1 + Quantum Computing level**, plus up to 3 talent slots (one of them for attacks only, for the Admiral). See [Talents](/en/dynasty/talents).
2. A fleet takes its slot from departure to return. Expeditions, including during their hold, and Stellar Station deposits take one. Missiles and [Jump gate](/en/fleet/jump-gate) jumps do not. The Navigator also gets shuttles, outside the slots, for transports and stationing between their own bases.

### Speed
3. A ship's speed = its drive's base speed × (1 + bonus × level of that drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive. Some ships switch drives with research (see [Ships list](/en/fleet/ships)).
4. A fleet flies at the speed of its **slowest ship**.
5. You choose a **speed from 1 to 100%**, in steps of 1%. In the formulas it becomes the fraction $s$: $s = 1$ at 100%, $s = 0.5$ at 50%.

### Distance
6. The distance depends on what differs between departure and arrival:

| Trip | Distance |
|---|---|
| To another galaxy | 20,000 × galaxy gap |
| Same galaxy, other system | 2,700 + 95 × system gap |
| Same system, other position | 1,000 + 5 × position gap |
| Between a planet and its moon | 5 |

7. **The map wraps around** for galaxies and for systems: the gap is counted the shortest way, across the edge if need be. On Redline, galaxy 9 neighbours galaxy 1, and system 99 neighbours system 1. Positions do not wrap.

### Duration
8. One-way duration, in seconds, rounded, at least 1:

$$
T = \\frac{{10 + \\frac{{3{{,}}500}}{{s}}\\sqrt{{\\frac{{10 \\times D}}{{V}}}}}}{{A \\times B}}
$$

- $T$: trip duration, in seconds;
- $s$: chosen speed, as a fraction (from 0.01 for 1% to 1 for 100%);
- $D$: trip distance (rule 6);
- $V$: speed of the slowest ship in the fleet;
- $A$: the universe's fleet speed;
- $B$: speed bonus, 1 without a bonus (rule 13).

### Hydrogen consumption
9. One-way consumption, rounded down, at least 1 as soon as a ship burns fuel:

$$
U = \\sum_i \\frac{{F_i \\times N_i \\times D}}{{35{{,}}000}} \\left( s \\sqrt{{\\frac{{V}}{{V_i}}}} + 1 \\right)^2
$$

- $U$: hydrogen for the trip;
- $F_i$: consumption of one ship of type $i$, that of its current drive;
- $N_i$: number of ships of type $i$;
- $D$: trip distance;
- $s$: chosen speed, as a fraction;
- $V$: speed of the slowest ship in the fleet;
- $V_i$: speed of ship type $i$.

10. A ship faster than the rest of its fleet burns less. No research lowers consumption; a better drive raises it.
11. **The way back is paid at departure**: each leg is counted on its own, out then back, for every mission except **Colonization** and **Stationing**, which are one-way. Stellar Station deposits burn nothing.
12. **The trip's hydrogen travels in the holds**: cargo + trip hydrogen must not exceed the fleet's cargo capacity. A Navigator talent lightens that fuel.

### Bonuses
13. Speed bonuses (personal talents and the alliance talent Coordinated propulsion, +5% per level) **divide the duration**: +50% = a trip 1.5 times shorter. Together they cap at **+60%**; a few trip talents add on top of the cap (return, trips between your bases, recall).
14. Consumption cuts (personal talents and the alliance talent Optimised supply, 5% per level) cap together at **45%**, never below 1 per leg.

### Recall and return
15. A fleet can be **recalled** while it is flying out or holding on an expedition, not on its way back. Stellar Station deposits cannot be recalled.
16. A recalled fleet flies home in as much time as it already spent flying out; an expedition recalled during its hold flies the whole way. A recall **does not refund** hydrogen (except with a Navigator talent). A recalled attack no longer counts towards the [attack limit](/en/players/attack-limit).
17. On return, the fleet lands at its home base with its cargo, even beyond storage capacity. **That base must still be yours and have an Orbital Dock**: otherwise the fleet is lost.

## Worked example

10 Interceptors (speed 12,500 × 1.6 = {N(v)} with Combustion Drive 6, consumption 20 each) attack from [2:40:8] to [2:50:3]. Distance: 2,700 + 95 × 10 = **{N(d)}**.

{T1}

For instance at 100%: 10 + 3,500 / 1 × √(10 × {N(d)} / {N(v)}) ≈ {N(res[100][0])} s, and 20 × 10 × {N(d)} / 35,000 × (1 + 1)² ≈ {N(res[100][1])} hydrogen. At half speed the flight takes twice as long but costs **{save}% less hydrogen**.

**Wrapping map**: from galaxy 1 to galaxy 9 on Redline, the gap is {g} galaxy, so a distance of {N(dg)}, not 8 × 20,000. From system 3 to system 97 of the same galaxy, the gap is {s_} systems: distance {N(ds)}.

## Detailed data

### Drives

{T2}

Speeds, consumption and drive switches are on the [Ships list](/en/fleet/ships) page.

### Talent flight orders

Talents add flight orders: changing speed in flight (Relaunch at 100%, Holding pattern down to 10%), Home port, Return freight, Grouped delivery, Loading order, Afterburner, Redirection, Return jump. They are described in [Talents](/en/dynasty/talents) and the [Navigator](/en/dynasty/classes/navigator) tree.

## Common pitfalls

- **The slowest ship sets the pace**: a single Salvager (speed 2,000) slows a whole fleet of Interceptors.
- **The way back is paid at departure**: plan the round-trip hydrogen before attacking, and the hold space to carry it.
- **A recall refunds nothing**: the hydrogen spent is gone.
- **Do not remove the Orbital Dock of a base expecting a fleet**: with no Dock on arrival, the returning fleet is lost.
- **Mind the edge of the map**: the nearest galaxy is not always the one you think.
- **Quantum Computing caps your fleets**: at level 2, only 3 fleets in flight, expeditions and deposits included.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Missions](/en/fleet/missions)
- [Ships list](/en/fleet/ships)
- [Expeditions](/en/fleet/expeditions)
- [Jump gate](/en/fleet/jump-gate)
- [Alliance missions and station](/en/players/alliance-missions)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/movement', body(lang))
