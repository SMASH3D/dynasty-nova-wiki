import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

G, S, P = REDLINE['map']
EX = [  # (origine, cible) sur Redline
    ((3, 40, 8), (5, 40, 8)),
    ((1, 40, 8), (9, 40, 8)),
    ((2, 45, 8), (2, 50, 8)),
    ((2, 97, 8), (2, 3, 8)),
    ((2, 45, 3), (2, 45, 6)),
]


def c(t): return f'[{t[0]}:{t[1]}:{t[2]}]'


def body(lang):
    N = lambda x: n(x, lang)
    fr = lang == 'fr'
    d = [distance(o, t, G, S) for o, t in EX]
    cross = 2700 + 95 * (S // 2)
    if fr:
        return f'''# Coordonnées

> **En bref** : chaque planète a une adresse à trois nombres, [galaxie:système:position], par exemple [2:83:6]. Le nombre de galaxies, de systèmes par galaxie et de positions par système dépend de l'univers. La carte **boucle** : la dernière galaxie est voisine de la première, et le dernier système d'une galaxie voisin du premier. La distance entre deux coordonnées fixe la durée et le coût en hydrogène d'un vol.
{{.is-info}}

> **Paramètre d'univers** : le nombre de galaxies, de systèmes par galaxie et de positions par système (de {POSITIONS_MIN} à {POSITIONS_MAX}) est fixé à la création de l'univers.
> Par défaut : **aucun, chaque univers a le sien** · Redline : **{G} galaxies, {S} systèmes, {P} positions**
{{.is-info}}

## Règles

1. Une coordonnée s'écrit **[galaxie:système:position]**.
2. Chaque galaxie compte le même nombre de **systèmes** : {S} sur Redline, numérotés de 1 à {S}.
3. Chaque système compte le même nombre de **positions** : {P} sur Redline. Chaque position accueille au plus une planète, et éventuellement sa lune.
4. Après la dernière position, chaque système a deux cases de plus, sans planète :
   - l'**espace lointain** (position {P + 1} sur Redline), pour les expéditions et le recyclage ;
   - la **Station stellaire** (position {P + 2} sur Redline), où se trouvent la Banque stellaire et la trésorerie d'alliance.
5. **La carte boucle sur les galaxies et sur les systèmes** : de la galaxie {G} à la galaxie 1, l'écart est de 1, comme de la galaxie 1 à la galaxie 2. De même, le système {S} est voisin du système 1 dans la même galaxie. Le jeu prend toujours le plus court des deux sens.
6. Les **positions ne bouclent pas** : de la position 1 à la position {P}, l'écart est de {P - 1}.
7. La **distance** entre deux points ne dépend que de l'écart le plus important (tableau ci-dessous) : un écart de galaxie l'emporte sur tout le reste, puis un écart de système, puis un écart de position.

## Formules

Avec $\\Delta G$, $\\Delta S$ et $\\Delta P$ les écarts de galaxie, de système et de position :

$$
D = \\begin{{cases}}
20\\,000 \\times \\Delta G & \\text{{si }} \\Delta G > 0 \\\\
2\\,700 + 95 \\times \\Delta S & \\text{{sinon, si }} \\Delta S > 0 \\\\
1\\,000 + 5 \\times \\Delta P & \\text{{sinon, si }} \\Delta P > 0 \\\\
5 & \\text{{entre une planète et sa lune}}
\\end{{cases}}
$$

- $\\Delta G = \\min(|G_1 - G_2|,\\ n_G - |G_1 - G_2|)$, avec $n_G$ le nombre de galaxies de l'univers ;
- $\\Delta S = \\min(|S_1 - S_2|,\\ n_S - |S_1 - S_2|)$, avec $n_S$ le nombre de systèmes par galaxie ;
- $\\Delta P = |P_1 - P_2|$ ;
- $D$ : distance du vol, qui entre dans sa durée et sa consommation (voir [Déplacements](/fr/fleet/movement)).

## Exemples chiffrés

Sur Redline ({G} galaxies, {S} systèmes) :

| Trajet | Écart retenu | Distance |
|---|---|---|
| {c(EX[0][0])} vers {c(EX[0][1])} | 2 galaxies | 20 000 × 2 = **{N(d[0])}** |
| {c(EX[1][0])} vers {c(EX[1][1])} | 1 galaxie (la carte boucle) | 20 000 × 1 = **{N(d[1])}** |
| {c(EX[2][0])} vers {c(EX[2][1])} | 5 systèmes | 2 700 + 95 × 5 = **{N(d[2])}** |
| {c(EX[3][0])} vers {c(EX[3][1])} | 5 systèmes (la galaxie boucle) | 2 700 + 95 × 5 = **{N(d[3])}** |
| {c(EX[4][0])} vers {c(EX[4][1])} | 3 positions | 1 000 + 5 × 3 = **{N(d[4])}** |
| [2:45:3] vers sa lune | même case | **5** |

## Pièges fréquents

- **Changer de galaxie coûte cher** : une seule galaxie d'écart (20 000) vaut plus que le trajet le plus long à l'intérieur d'une galaxie de Redline, {S // 2} systèmes d'écart au plus grâce à la boucle (2 700 + 95 × {S // 2} = {N(cross)}).
- **Pensez à la boucle** : une cible dans la galaxie {G} est à une seule galaxie de vous si vous êtes dans la galaxie 1.
- **Planète et lune ne sont pas au même endroit** : un trajet de 5 reste un vrai vol, très court.

## Pages liées

- [La vue galaxie](/fr/universe/galaxy-view)
- [Déplacements](/fr/fleet/movement)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Expéditions](/fr/fleet/expeditions)
'''
    return f'''# Coordinates

> **In short**: every planet has a three-number address, [galaxy:system:position], for example [2:83:6]. The number of galaxies, systems per galaxy and positions per system depends on the universe. The map **wraps around**: the last galaxy is next to the first one, and the last system of a galaxy is next to its first one. The distance between two coordinates sets a flight's duration and hydrogen cost.
{{.is-info}}

> **Universe setting**: the number of galaxies, systems per galaxy and positions per system ({POSITIONS_MIN} to {POSITIONS_MAX}) is set when the universe is created.
> Default: **none, each universe has its own** · Redline: **{G} galaxies, {S} systems, {P} positions**
{{.is-info}}

## Rules

1. A coordinate is written **[galaxy:system:position]**.
2. Every galaxy has the same number of **systems**: {S} on Redline, numbered 1 to {S}.
3. Every system has the same number of **positions**: {P} on Redline. Each position holds at most one planet, and possibly its moon.
4. After the last position, each system has two more cells, with no planet:
   - **deep space** (position {P + 1} on Redline), for expeditions and recycling;
   - the **Stellar Station** (position {P + 2} on Redline), home of the Stellar Bank and the alliance treasury.
5. **The map wraps around on galaxies and on systems**: from galaxy {G} to galaxy 1 the gap is 1, as from galaxy 1 to galaxy 2. Likewise, system {S} is next to system 1 in the same galaxy. The game always takes the shorter way.
6. **Positions do not wrap**: from position 1 to position {P}, the gap is {P - 1}.
7. The **distance** between two points depends only on the largest gap (table below): a galaxy gap outweighs everything else, then a system gap, then a position gap.

## Formulas

With $\\Delta G$, $\\Delta S$ and $\\Delta P$ the galaxy, system and position gaps:

$$
D = \\begin{{cases}}
20{{,}}000 \\times \\Delta G & \\text{{if }} \\Delta G > 0 \\\\
2{{,}}700 + 95 \\times \\Delta S & \\text{{else, if }} \\Delta S > 0 \\\\
1{{,}}000 + 5 \\times \\Delta P & \\text{{else, if }} \\Delta P > 0 \\\\
5 & \\text{{between a planet and its moon}}
\\end{{cases}}
$$

- $\\Delta G = \\min(|G_1 - G_2|,\\ n_G - |G_1 - G_2|)$, with $n_G$ the universe's number of galaxies;
- $\\Delta S = \\min(|S_1 - S_2|,\\ n_S - |S_1 - S_2|)$, with $n_S$ the number of systems per galaxy;
- $\\Delta P = |P_1 - P_2|$;
- $D$: the flight distance, which feeds its duration and consumption (see [Movement](/en/fleet/movement)).

## Worked examples

On Redline ({G} galaxies, {S} systems):

| Trip | Gap used | Distance |
|---|---|---|
| {c(EX[0][0])} to {c(EX[0][1])} | 2 galaxies | 20,000 × 2 = **{N(d[0])}** |
| {c(EX[1][0])} to {c(EX[1][1])} | 1 galaxy (the map wraps) | 20,000 × 1 = **{N(d[1])}** |
| {c(EX[2][0])} to {c(EX[2][1])} | 5 systems | 2,700 + 95 × 5 = **{N(d[2])}** |
| {c(EX[3][0])} to {c(EX[3][1])} | 5 systems (the galaxy wraps) | 2,700 + 95 × 5 = **{N(d[3])}** |
| {c(EX[4][0])} to {c(EX[4][1])} | 3 positions | 1,000 + 5 × 3 = **{N(d[4])}** |
| [2:45:3] to its moon | same cell | **5** |

## Common pitfalls

- **Changing galaxy is expensive**: a single galaxy gap (20,000) is worth more than the longest trip inside a Redline galaxy, {S // 2} systems apart at most thanks to the wrap (2,700 + 95 × {S // 2} = {N(cross)}).
- **Remember the wrap**: a target in galaxy {G} is only one galaxy away if you are in galaxy 1.
- **A planet and its moon are not in the same place**: a trip of 5 is still a real, very short flight.

## Related pages

- [The galaxy view](/en/universe/galaxy-view)
- [Movement](/en/fleet/movement)
- [Planets: size, temperature, type](/en/universe/planets)
- [Expeditions](/en/fleet/expeditions)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/coordinates', body(lang))
