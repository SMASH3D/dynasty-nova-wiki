import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *

ORDER = [s[0] for s in SHIPS]


def nm(code, lang):
    if lang == 'en' and code in S:
        return f'*{S[code][2]}*'
    return sname(code, lang)


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    rows = []
    for a in ORDER:
        t = RF.get(a)
        if not t:
            continue
        cells = ', '.join(f'{nm(c, lang)} {N(v)}' for c, v in sorted(t.items(), key=lambda kv: -kv[1]))
        rows.append([nm(a, lang), cells])
    none = [nm(c, lang) for c in ORDER if c not in RF]
    rows.append([', '.join(none), 'aucun' if fr else 'none'])
    rows.append(['Toutes les défenses' if fr else 'All defenses', 'aucun' if fr else 'none'])
    hdr = ['Tireur', 'Cibles (facteur)'] if fr else ['Shooter', 'Targets (factor)']
    T1 = table(hdr, rows)
    targets = {}
    for a, t in RF.items():
        for c, v in t.items():
            targets.setdefault(c, []).append((a, v))
    rows2 = []
    for c in ORDER + list(DEF):
        lst = sorted(targets.get(c, []), key=lambda kv: -kv[1])
        rows2.append([nm(c, lang), ', '.join(f'{nm(a, lang)} {N(v)}' for a, v in lst) or ('personne' if fr else 'nobody')])
    T2 = table(['Cible', 'Vaisseaux qui ont un tir rapide contre elle'] if fr else ['Target', 'Ships with rapid fire against it'], rows2)
    p6 = round(100 * 5 / 6, 1)
    p6s = (f'{p6}'.replace('.', ',') + ' %') if fr else f'{p6}%'
    if fr:
        return f'''# Tirs rapides

> **En bref** : certains vaisseaux ont un **tir rapide** contre certaines unités. Après chaque tir sur l'une d'elles, ils ont une chance de tirer à nouveau dans le même round, sur une nouvelle cible tirée au hasard. Le facteur affiché est le nombre moyen de tirs enchaînés contre ce type d'unité. Les défenses n'ont pas de tir rapide.
{{.is-info}}

## Règles

1. À chaque round, chaque unité tire au moins une fois (une fois par tir de base) sur une unité adverse **tirée au hasard** parmi celles encore en vie. Le tir rapide ne guide jamais le tir vers les unités qu'il contre.
2. Après chaque tir, touché ou manqué, si le tireur a un tir rapide de facteur $f$ contre l'unité qu'il vient de viser, il tire à nouveau avec la probabilité $(f - 1) / f$, sur une **nouvelle cible tirée au hasard**.
3. La chaîne continue tant que le tirage réussit **et** que la dernière cible visée fait partie de ses tirs rapides. Dès qu'elle tombe sur une unité qui n'en fait pas partie, elle s'arrête après ce tir.
4. Contre une flotte composée uniquement de la cible, le tireur tire donc $f$ fois en moyenne par round.
5. Un tir enchaîné suit les règles d'un tir normal : un tir inférieur à 1 % du bouclier de la cible rebondit.
6. Certains talents renforcent les tirs rapides (voir [Les talents](/fr/dynasty/talents)) : le tableau ci-dessous donne les facteurs de base.

## Exemple chiffré

Une Corvette a un tir rapide de **6** contre l'Intercepteur.
- Après un tir sur un Intercepteur, elle retire avec une probabilité de 5 / 6 = **{p6s}**.
- Face à une flotte composée uniquement d'Intercepteurs, elle tire **6 fois en moyenne** par round, au lieu d'une.
- Face à une flotte moitié Intercepteurs, moitié Cuirassés, la chaîne s'arrête dès qu'elle tombe sur un Cuirassé : elle tire nettement moins.

## Données détaillées

### Qui tire rapidement sur qui

{T1}

### Qui est visé par quoi

{T2}

## Pièges fréquents

- **Les Éclaireurs et Collecteurs relancent les tirs adverses** : presque tous les vaisseaux ont un tir rapide de 5 contre eux. Laisser beaucoup d'Éclaireurs ou de Collecteurs en orbite pendant une attaque donne à l'attaquant des tirs supplémentaires.
- **Les tirs rapides ne garantissent rien** : la cible suivante est tirée au hasard. Dans une flotte variée, les chaînes sont plus courtes que le facteur affiché.
- **Le Colossus stellaire n'est visé par aucun tir rapide** : il ne peut être abattu qu'à la force des tirs normaux.
- **Un tir rapide ne contourne pas la règle du 1 %** : un tir trop faible contre un gros bouclier rebondit, même s'il fait partie d'une chaîne.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Simulateur de combat](/fr/combat/simulator)
'''
    return f'''# Rapid fire

> **In short**: some ships have **rapid fire** against some units. After each shot at one of them, they have a chance to fire again in the same round, at a new randomly drawn target. The factor shown is the average number of chained shots against that unit type. Defenses have no rapid fire.
{{.is-info}}

> Ships are not translated in the game yet: it shows their French name in every language. The English names used here are provisional (see [Ships list](/en/fleet/ships)).
{{.is-warning}}

## Rules

1. Each round, every unit fires at least once (once per base shot) at an enemy unit **drawn at random** among those still alive. Rapid fire never steers a shot towards the units it counters.
2. After each shot, hit or miss, if the shooter has rapid fire of factor $f$ against the unit it just aimed at, it fires again with probability $(f - 1) / f$, at a **new randomly drawn target**.
3. The chain goes on as long as the roll succeeds **and** the last target is one of its rapid-fire targets. As soon as it lands on a unit that is not, it stops after that shot.
4. Against a fleet made only of that target, the shooter therefore fires $f$ times per round on average.
5. A chained shot follows the rules of a normal shot: a shot below 1% of the target's shield bounces off.
6. Some talents strengthen rapid fire (see [Talents](/en/dynasty/talents)): the table below gives the base factors.

## Worked example

A Corvette has rapid fire **6** against the Interceptor.
- After a shot at an Interceptor, it fires again with probability 5 / 6 = **{p6s}**.
- Against a fleet made only of Interceptors, it fires **6 times on average** per round, instead of once.
- Against a fleet that is half Interceptors, half Battleships, the chain stops as soon as it lands on a Battleship: it fires much less.

## Detailed data

### Who rapid-fires at whom

{T1}

### Who is targeted by what

{T2}

## Common pitfalls

- **Scouts and Solar Collectors feed enemy chains**: almost every ship has rapid fire 5 against them. Leaving many of them in orbit during an attack hands the attacker extra shots.
- **Rapid fire guarantees nothing**: the next target is random. In a mixed fleet, chains are shorter than the factor shown.
- **No rapid fire targets the Stellar Colossus**: it can only be brought down by normal shots.
- **Rapid fire does not bypass the 1% rule**: a shot too weak for a big shield bounces off, even inside a chain.

## Related pages

- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [How combat works](/en/combat/how-combat-works)
- [Combat simulator](/en/combat/simulator)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/rapid-fire', body(lang))
