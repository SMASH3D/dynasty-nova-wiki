import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *

# JumpGateCooldown::LADDER (minutes), niveau 14 et plus : 10
LADDER = {1: 60, 2: 53, 3: 47, 4: 41, 5: 36, 6: 31, 7: 27, 8: 23, 9: 19, 10: 17, 11: 14, 12: 13, 13: 11, 14: 10}


def cooldown_s(level, cut=0):
    """JumpGateCooldown::forLevel() puis shortenedBy() : ⌈secondes × (100 − p) / 100⌉, p plafonné à 30 (PlayerBonuses)."""
    sec = 60 * LADDER.get(level, LADDER[14])
    return math.ceil(round(sec * (100 - min(cut, 30)) / 100, 6))


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    lv = list(range(1, 15))
    T1 = '| ' + ('Niveau' if fr else 'Level') + ' | ' + ' | '.join(str(l) for l in lv[:-1]) + (' | 14 et plus |' if fr else ' | 14 and above |') + '\n|' + '---|' * (len(lv) + 1) + '\n| ' + \
         ('Recharge (minutes)' if fr else 'Recharge (minutes)') + ' | ' + ' | '.join(str(LADDER[l]) for l in lv) + ' |'
    T2 = table(['Niveau' if fr else 'Level', 'Métal' if fr else 'Metal', 'Cristal' if fr else 'Crystal', 'Hydrogène' if fr else 'Hydrogen'],
               [[l, N(2_000_000 * 2 ** (l - 1)), N(4_000_000 * 2 ** (l - 1)), N(2_000_000 * 2 ** (l - 1))] for l in range(1, 6)])
    a, b = cooldown_s(3) // 60, cooldown_s(1) // 60
    c5, c5t = cooldown_s(5), cooldown_s(5, 30)
    if fr:
        return f'''# Porte de saut

> **En bref** : la Porte de saut se construit sur une lune. Elle envoie instantanément des vaisseaux vers une autre de vos lunes équipée d'une Porte, sans temps de vol ni hydrogène. Elle ne transporte aucune ressource, et les deux portes doivent ensuite se recharger.
{{.is-info}}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Porte de saut">

## Règles

1. La Porte de saut se construit **uniquement sur une lune**. Prérequis : **Base lunaire 1** et **Pliage Spatial 7**. Elle n'a pas de niveau maximum ; son coût double à chaque niveau.
2. Un saut relie **deux lunes différentes qui vous appartiennent**, dans le même univers, chacune équipée d'une Porte de saut prête. Impossible de sauter vers la lune d'un autre joueur, même allié.
3. Le saut est **instantané** et ne consomme **aucun hydrogène**. Il n'occupe aucun emplacement de flotte.
4. **Coques seulement** : aucune ressource ne passe.
5. Après un saut, **les deux portes**, départ et arrivée, se rechargent, chacune selon son propre niveau (table plus bas). La recharge ne dépend pas des vitesses de l'univers.
6. Les deux lunes sont vérifiées avant tout mouvement : un saut refusé (porte en recharge, lune sans Porte) ne déplace rien et ne déclenche aucune recharge.
7. Des talents du Navigateur raccourcissent la recharge (jusqu'à 30 %) ou permettent deux sauts avant recharge (voir [Navigateur](/fr/dynasty/classes/navigator)).

## Exemple chiffré

Vous avez une Porte de saut niveau 3 sur la lune A et niveau 1 sur la lune B. Vous faites sauter votre flotte de A vers B.
- La flotte arrive aussitôt sur B, sans dépenser d'hydrogène.
- La porte de A se recharge en **{a} minutes** (niveau 3), celle de B en **{b} minutes** (niveau 1).
- Un nouveau saut depuis B, ou vers A, ne sera possible qu'une fois la porte concernée rechargée.

Avec une recharge raccourcie de 30 % par les talents, une porte niveau 5 passe de {c5 // 60} à **{c5t // 60} minutes**.

## Données détaillées

### Recharge selon le niveau

{T1}

### Coût

{T2}

Le coût continue de doubler aux niveaux suivants.

## Pièges fréquents

- **La recharge frappe les deux bouts** : améliorer seulement la porte de départ ne suffit pas à enchaîner les sauts.
- **Pas de ressources** : une flotte chargée doit d'abord décharger sa cargaison.
- **Il faut deux lunes à vous** : une seule Porte ne sert à rien, et celle d'un allié non plus.
- **Au-delà du niveau 14, la recharge ne baisse plus** : elle reste à 10 minutes.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [Déplacements](/fr/fleet/movement)
- [Liste des bâtiments](/fr/economy/buildings)
'''
    return f'''# Jump gate

> **In short**: the Jump gate is built on a moon. It sends ships instantly to another of your moons with a Gate, with no flight time and no hydrogen. It carries no resources, and both gates must then recharge.
{{.is-info}}

<img src="/images/illustrations/facilities/porte-de-saut.jpg" width="180" alt="Jump gate">

## Rules

1. The Jump gate can **only be built on a moon**. Requirements: **Lunar base 1** and **Hyperspace Technology 7**. It has no maximum level; its cost doubles at each level.
2. A jump links **two different moons that you own**, in the same universe, each with a ready Jump gate. You cannot jump to another player's moon, not even an ally's.
3. The jump is **instant** and burns **no hydrogen**. It takes no fleet slot.
4. **Hulls only**: no resources go through.
5. After a jump, **both gates**, departure and arrival, recharge, each by its own level (table below). The recharge does not depend on universe speeds.
6. Both moons are checked before anything moves: a refused jump (gate recharging, moon without a Gate) moves nothing and starts no recharge.
7. Navigator talents shorten the recharge (by up to 30%) or allow two jumps before recharging (see [Navigator](/en/dynasty/classes/navigator)).

## Worked example

You have a level 3 Jump gate on moon A and a level 1 on moon B. You jump your fleet from A to B.
- The fleet lands on B at once, without spending hydrogen.
- Gate A recharges in **{a} minutes** (level 3), gate B in **{b} minutes** (level 1).
- A new jump from B, or to A, is only possible once the gate in question has recharged.

With a recharge cut by 30% through talents, a level 5 gate goes from {c5 // 60} to **{c5t // 60} minutes**.

## Detailed data

### Recharge by level

{T1}

### Cost

{T2}

The cost keeps doubling at higher levels.

## Common pitfalls

- **The recharge hits both ends**: upgrading only the departure gate is not enough to chain jumps.
- **No resources**: a loaded fleet must unload its cargo first.
- **You need two moons of your own**: a single Gate is useless, and so is an ally's.
- **Past level 14 the recharge stops dropping**: it stays at 10 minutes.

## Related pages

- [Moons](/en/universe/moons)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [Fleet movement](/en/fleet/movement)
- [Buildings list](/en/economy/buildings)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/jump-gate', body(lang))
