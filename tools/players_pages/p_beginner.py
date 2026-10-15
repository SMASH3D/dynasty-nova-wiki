import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *

CASES = [(400, 1000, False), (400, 1200, False), (400, 1500, False), (0, 50, False), (0, 0, False),
         (500, 2400, False), (6000, 50000, False), (6000, 80000, False), (6000, 80000, True), (600000, 5000000, False)]

def ratio_label(t):
    return '1:' + str(t[1])

def rows(lang):
    N = lambda x: n(x, lang)
    out = []
    for a, b, inact in CASES:
        t = tier_of(min(a, b))
        if lang == 'fr':
            tl = 'aucun (≥ 500 000)' if t is None else f'{ratio_label(t)} (< {N(t[0])})'
        else:
            tl = 'none (≥ 500,000)' if t is None else f'{ratio_label(t)} (< {N(t[0])})'
        gap = '' if min(a, b) == 0 else N(round(max(a, b) / min(a, b), 2))
        ab = not blocks(a, b, inact)   # A attaque B (B défenseur, inactif ou non)
        ba = not blocks(b, a, False)   # B attaque A (A actif)
        if lang == 'fr':
            res = 'oui, dans les deux sens' if ab and ba else ('**non, dans aucun sens**' if not ab and not ba else ('A peut attaquer B (inactif), pas l\'inverse' if ab else 'B peut attaquer A, pas l\'inverse'))
            pt = lambda v: f'{N(v)} point' if v < 2 else f'{N(v)} points'
        else:
            res = 'yes, both ways' if ab and ba else ('**no, either way**' if not ab and not ba else ('A may attack B (inactive), not the reverse' if ab else 'B may attack A, not the reverse'))
            pt = lambda v: f'{N(v)} point' if v == 1 else f'{N(v)} points'
        out.append([pt(a), pt(b) + (' (inactif)' if inact and lang == 'fr' else (' (inactive)' if inact else '')), tl, gap, res])
    return out

def body(lang):
    N = lambda x: n(x, lang)
    t = TIERS
    if lang == 'fr':
        box = setting_box('fr', 'les paliers de points et le délai d\'inactivité peuvent être différents selon l\'univers.',
                          f'**1:{t[0][1]}** sous {N(t[0][0])} points, **1:{t[1][1]}** sous {N(t[1][0])}, **1:{t[2][1]}** sous {N(t[2][0])}, inactif après **{INACTIVITY_DEFAULT} jours**',
                          f'mêmes paliers, inactif après **{INACTIVITY_REDLINE} jours**')
        return f'''# Protection des débutants

> **En bref** : deux protections tiennent les joueurs trop inégaux à l'écart l'un de l'autre. La **protection nouvel arrivant** vous rend inattaquable pendant vos {NEWCOMER_DAYS} premiers jours dans un univers, tant que vous n'attaquez personne. La **protection par points** interdit toute attaque entre deux joueurs dont l'écart de points est trop grand, dans un sens comme dans l'autre.
{{.is-info}}

{box}

## Règles

### Protection nouvel arrivant
1. Pendant **{NEWCOMER_DAYS} jours** à compter de votre **première arrivée** dans un univers, personne ne peut vous attaquer ni vous tirer de missiles. Cette durée est la même dans tous les univers.
2. Le temps restant s'affiche en haut de l'écran (« Protection nouvel arrivant »). Vos planètes et votre fiche portent le badge « Nouveau joueur », avec la date de fin.
3. **Lancer une attaque ou une salve de missiles y met fin, définitivement**, quelle que soit la cible (joueur, joueur non humain, planète abandonnée). Un avertissement s'affiche avant de confirmer. Rappeler la flotte ne rend pas la protection.
4. L'espionnage, le transport, le stationnement, le recyclage et la colonisation ne la retirent pas, dans un sens comme dans l'autre : un nouvel arrivant peut être espionné et ravitaillé.
5. Elle vaut **par univers**. Quitter un univers puis y revenir ne la renouvelle pas : la date de première arrivée reste la même.
6. Les joueurs non humains (PvE) n'en ont jamais.

### Protection par points
7. Une attaque est interdite quand le plus fort des deux joueurs a **au moins N fois** les points du plus faible, N dépendant du palier du **plus faible** :
   - moins de {N(t[0][0])} points : **1:{t[0][1]}** ;
   - de {N(t[0][0])} à moins de {N(t[1][0])} points : **1:{t[1][1]}** ;
   - de {N(t[1][0])} à moins de {N(t[2][0])} points : **1:{t[2][1]}** ;
   - {N(t[2][0])} points ou plus : **plus aucune protection**, quel que soit l'écart.
8. La règle joue **dans les deux sens** : le petit joueur est protégé du gros, et le petit ne peut pas attaquer le gros non plus.
9. Une borne appartient au palier du dessus : à exactement {N(t[0][0])} points, on est en 1:{t[1][1]}. Exactement N fois plus de points suffit à bloquer.
10. Les points comptés sont le **total** du classement, arrondi à l'entier inférieur (voir [Classements et points](/fr/players/rankings)).
11. Un joueur à **0 point** ne peut être attaqué par aucun joueur qui en a ; deux joueurs à 0 point peuvent s'affronter.
12. Elle s'applique aux **attaques** et aux **salves de missiles**. L'espionnage, le transport et le recyclage restent libres.
13. Un défenseur **inactif** (voir [Inactivité](/fr/players/inactivity)) perd cette protection : n'importe qui peut l'attaquer, quel que soit l'écart, y compris un joueur beaucoup plus petit que lui. Seule l'inactivité du défenseur compte.

### Les deux ensemble
14. Les deux protections **s'ajoutent** : une attaque doit passer l'une et l'autre, puis la [limite d'attaques](/fr/players/attack-limit). La protection nouvel arrivant ne dépend pas des points ; la protection par points ne dépend pas de l'ancienneté.
15. Dans la [vue galaxie](/fr/universe/galaxy-view), l'attaque, les missiles et la destruction de lune ne sont pas proposés contre un joueur que l'une des deux protections couvre.

## Exemple chiffré

Joueurs actifs, protection nouvel arrivant terminée, paliers par défaut :

{table(['Joueur A', 'Joueur B', 'Palier du plus faible', 'Écart', 'Attaque possible ?'], rows('fr'))}

## Pièges fréquents

- **Le plus fort est protégé aussi** : un petit joueur ne peut pas attaquer un joueur bien plus gros que lui, sauf s'il est inactif.
- **Votre première attaque vous coûte le reste de vos {NEWCOMER_DAYS} jours**, même contre une planète abandonnée.
- **L'inactivité lève la protection par points** : avant une longue absence, pensez au [mode vacances](/fr/players/vacation-mode).
- **Les points comptent tout** : économie, recherche et militaire. Construire beaucoup peut vous faire changer de palier.

## Pages liées

- [Classements et points](/fr/players/rankings)
- [Limite d'attaques](/fr/players/attack-limit)
- [Mode vacances](/fr/players/vacation-mode)
- [Inactivité](/fr/players/inactivity)
- [La vue galaxie](/fr/universe/galaxy-view)
'''
    box = setting_box('en', 'point tiers and the inactivity delay may differ from one universe to another.',
                      f'**1:{t[0][1]}** under {N(t[0][0])} points, **1:{t[1][1]}** under {N(t[1][0])}, **1:{t[2][1]}** under {N(t[2][0])}, inactive after **{INACTIVITY_DEFAULT} days**',
                      f'same tiers, inactive after **{INACTIVITY_REDLINE} days**')
    return f'''# Beginner protection

> **In short**: two protections keep players who are too unequal away from each other. **Newcomer protection** makes you unattackable for your first {NEWCOMER_DAYS} days in a universe, as long as you attack nobody. **Point protection** forbids any attack between two players whose point gap is too wide, in either direction.
{{.is-info}}

{box}

## Rules

### Newcomer protection
1. For **{NEWCOMER_DAYS} days** from your **first arrival** in a universe, nobody can attack you or fire missiles at you. This duration is the same in every universe.
2. The time left is shown at the top of the screen ("Newcomer protection"). Your planets and your card carry the "New player" badge, with the end date.
3. **Launching an attack or a missile salvo ends it, for good**, whatever the target (player, non-human player, abandoned planet). A warning is shown before you confirm. Recalling the fleet does not give the protection back.
4. Espionage, transport, stationing, recycling and colonization do not remove it, in either direction: a newcomer can be spied on and supplied.
5. It applies **per universe**. Leaving a universe and coming back does not renew it: the first arrival date stays the same.
6. Non-human (PvE) players never have it.

### Point protection
7. An attack is forbidden when the stronger of the two players has **at least N times** the points of the weaker one, N depending on the tier of the **weaker** player:
   - under {N(t[0][0])} points: **1:{t[0][1]}**;
   - from {N(t[0][0])} to under {N(t[1][0])} points: **1:{t[1][1]}**;
   - from {N(t[1][0])} to under {N(t[2][0])} points: **1:{t[2][1]}**;
   - {N(t[2][0])} points or more: **no protection at all**, whatever the gap.
8. The rule works **both ways**: the small player is protected from the big one, and the small one cannot attack the big one either.
9. A boundary belongs to the upper tier: at exactly {N(t[0][0])} points you are in 1:{t[1][1]}. Exactly N times more points is enough to block.
10. The points used are the ranking **total**, rounded down (see [Rankings and points](/en/players/rankings)).
11. A player with **0 points** cannot be attacked by any player who has some; two players with 0 points may fight each other.
12. It applies to **attacks** and **missile salvos**. Espionage, transport and recycling stay free.
13. An **inactive** defender (see [Inactivity](/en/players/inactivity)) loses this protection: anyone may attack them, whatever the gap, including a much smaller player. Only the defender's inactivity matters.

### Both together
14. The two protections **stack**: an attack must clear both, then the [attack limit](/en/players/attack-limit). Newcomer protection does not depend on points; point protection does not depend on seniority.
15. In the [galaxy view](/en/universe/galaxy-view), attack, missiles and moon destruction are not offered against a player covered by either protection.

## Worked example

Active players, newcomer protection over, default tiers:

{table(['Player A', 'Player B', 'Tier of the weaker', 'Gap', 'Attack possible?'], rows('en'))}

## Common pitfalls

- **The stronger player is protected too**: a small player cannot attack a much bigger one, unless that player is inactive.
- **Your first attack costs you the rest of your {NEWCOMER_DAYS} days**, even against an abandoned planet.
- **Inactivity lifts point protection**: before a long absence, think of [vacation mode](/en/players/vacation-mode).
- **Points count everything**: economy, research and military. Building a lot can move you to another tier.

## Related pages

- [Rankings and points](/en/players/rankings)
- [Attack limit](/en/players/attack-limit)
- [Vacation mode](/en/players/vacation-mode)
- [Inactivity](/en/players/inactivity)
- [The galaxy view](/en/universe/galaxy-view)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/beginner-protection', body(lang),
          description='Qui peut attaquer qui : protection nouvel arrivant et paliers de points.' if lang == 'fr' else 'Who can attack whom: newcomer protection and point tiers.')
