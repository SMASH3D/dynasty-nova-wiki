import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *

lvl = 14
mine = cost(METAL_MINE[0], METAL_MINE[1], lvl)
mine_pts = points(*mine)
S = {c[0]: c for c in SHIPS}; D = {c[0]: c for c in DEFENSES}
bs = points(*S['battleship'][3:])
lc10 = 10 * points(*S['large_cargo'][3:])
wh10 = 10 * points(*D['long_range_warheads'][3:])

def body(lang):
    N = lambda x: n(x, lang)
    fr = lang == 'fr'
    ships = [[(c[1] if fr else c[2]), N(c[3]), N(c[4]), N(c[5]), N(points(*c[3:]))] for c in SHIPS]
    defs = [[(c[1] if fr else c[2]), N(c[3]), N(c[4]), N(c[5]), N(points(*c[3:]))] for c in DEFENSES]
    if fr:
        return f'''# Classements et points

> **En bref** : tout ce que vous bâtissez rapporte des points, à raison de **1 point pour {N(POINT_DIVISOR)} ressources** de son coût. Les joueurs sont classés sur quatre tableaux : Points (le total), Économie, Recherche et Militaire. Les alliances ont deux classements à elles : Puissance et Progression.
{{.is-info}}

## Règles

### Calcul des points
1. Un élément vaut **(métal + cristal + hydrogène) / {N(POINT_DIVISOR)}** points. L'énergie ne compte pas.
2. C'est le **coût de catalogue** qui compte, pas ce que vous avez payé : une réduction de coût (talent, bonus) ne change pas les points gagnés.
3. **Économie** : chaque niveau de bâtiment debout sur vos planètes et vos lunes. Le niveau N rapporte le coût du niveau N ; un bâtiment au niveau 10 compte donc les coûts des niveaux 1 à 10.
4. **Recherche** : chaque niveau de technologie, de la même façon.
5. **Militaire** : **tous les vaisseaux**, y compris les vaisseaux civils (Navette de fret, Cargo stellaire, Pionnier spatial, Récupérateur, Éclaireur, Collecteur solaire), toutes les défenses et tous les missiles, à quai comme en vol.
6. **Points** (le classement général) = Économie + Recherche + Militaire.
7. Les points sont gagnés à la **fin** d'un niveau de bâtiment ou de recherche, et **à chaque livraison** du chantier pour les vaisseaux et les défenses.

### Ce qui fait monter ou baisser
8. **Baissent** : vaisseaux et défenses détruits, missiles tirés, niveau de bâtiment démoli (il retire les points de ce niveau), colonie abandonnée (ses bâtiments, vaisseaux et défenses), lune détruite (ses bâtiments et tout ce qui s'y trouve).
9. **Ne baissent pas** : les vaisseaux remorqués par la Station de réparation et les défenses remises en état après un combat, puisqu'ils ne sont pas perdus. Abandonner une colonie ne retire **aucun point de recherche** : les technologies appartiennent à l'empire.
10. **Montent aussi** : vaisseaux trouvés en expédition, niveau de bâtiment offert (il compte comme un niveau construit), planète abandonnée recolonisée (vous recevez les points de ce qui y est encore debout).

### Le classement
11. Le classement est **calculé en direct**. Les points s'affichent arrondis à l'entier inférieur ; c'est aussi ce nombre arrondi qui sert à la [protection des débutants](/fr/players/beginner-protection).
12. Les flèches de **progression** comparent votre rang et vos points à la dernière photographie quotidienne du classement.
13. Le filtre **Humains** masque les joueurs non humains (marqués « Joueur IA (PvE) ») sans changer les rangs : chacun garde son rang dans l'univers.
14. La **recherche** trouve un joueur ou une alliance par pseudo, nom ou tag. Un clic sur un joueur ouvre sa **fiche** : rang, badges (« Joueur IA (PvE) », « En vacances », « Nouveau joueur ») et bouton pour lui écrire.
15. Deux joueurs à égalité de points sont départagés par un ordre interne, pas par l'ancienneté.

### Classements d'alliance
16. **Alliance Puissance** : la somme des Points de tous les membres. La trésorerie et les talents d'alliance n'y comptent pas.
17. **Alliance Progression** : le niveau et l'expérience de l'alliance ; à égalité, la première arrivée passe devant. Voir [Alliances](/fr/players/alliances).

## Exemple chiffré

- Vous montez l'Excavateur minéral du niveau {lvl - 1} au niveau {lvl} pour {N(mine[0])} métal et {N(mine[1])} cristal : **+{N(round(mine_pts, 2))} points** d'économie (le classement affiche l'entier inférieur).
- Vous construisez un Cuirassé ({N(S['battleship'][3])} métal, {N(S['battleship'][4])} cristal) : **+{N(bs)} points** militaires.
- Vous construisez 10 Cargos stellaires ({N(S['large_cargo'][3] + S['large_cargo'][4])} ressources chacun) : **+{N(lc10)} points** militaires. Les vaisseaux civils comptent.
- Vous tirez 10 Ogives longue portée : **{N(-wh10)} points** militaires, qu'elles touchent ou non.
- Votre Cuirassé est détruit en combat et la Station de réparation ne le récupère pas : **{N(-bs)} points** militaires.

## Données détaillées

Points de chaque vaisseau (coût de catalogue) :

{table(['Vaisseau', 'Métal', 'Cristal', 'Hydrogène', 'Points'], ships)}

Points de chaque défense et missile :

{table(['Défense', 'Métal', 'Cristal', 'Hydrogène', 'Points'], defs)}

| Classement | Ce qui compte | Ce qui fait baisser |
|---|---|---|
| Économie | Niveaux de bâtiments, planètes et lunes | Démolition, colonie abandonnée, lune détruite |
| Recherche | Niveaux de technologies | Rien |
| Militaire | Tous les vaisseaux, défenses et missiles | Unités détruites, missiles tirés, colonie abandonnée, lune détruite |
| Points | Somme des trois | Tout ce qui précède |

## Pièges fréquents

- **Une flotte de transport compte** : 100 Cargos stellaires valent {N(100 * points(*S['large_cargo'][3:]))} points militaires, et les perdre les retire.
- **Tirer des missiles coûte des points**, même quand ils sont interceptés.
- **Monter au classement change votre protection** : en passant un palier, vous changez la liste des joueurs que vous pouvez attaquer et de ceux qui peuvent vous attaquer.
- **Abandonner une colonie fait chuter vos points**, mais pas votre recherche.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Alliances](/fr/players/alliances)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des technologies](/fr/research/technologies)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
'''
    return f'''# Rankings and points

> **In short**: everything you build earns points, at **1 point per {N(POINT_DIVISOR)} resources** of its cost. Players are ranked on four boards: Points (the total), Economy, Research and Military. Alliances have two rankings of their own: Power and Progression.
{{.is-info}}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{{.is-warning}}

## Rules

### How points are counted
1. An item is worth **(metal + crystal + hydrogen) / {N(POINT_DIVISOR)}** points. Energy does not count.
2. The **catalogue cost** is what counts, not what you paid: a cost reduction (talent, bonus) does not change the points earned.
3. **Economy**: every building level standing on your planets and moons. Level N earns the cost of level N; a building at level 10 therefore counts the costs of levels 1 to 10.
4. **Research**: every technology level, the same way.
5. **Military**: **every ship**, civilian ships included (Cargo Shuttle, Stellar Freighter, Space Pioneer, Salvager, Scout, Solar Collector), every defense and every missile, docked or in flight.
6. **Points** (the general ranking) = Economy + Research + Military.
7. Points are earned when a building or research level **finishes**, and **at each delivery** from the shipyard for ships and defenses.

### What makes them go up or down
8. **Down**: ships and defenses destroyed, missiles fired, a demolished building level (it removes that level's points), an abandoned colony (its buildings, ships and defenses), a destroyed moon (its buildings and everything on it).
9. **Not down**: ships towed back by the Repair Station and defenses restored after a battle, since they are not lost. Abandoning a colony removes **no research points**: technologies belong to the empire.
10. **Also up**: ships found on an expedition, a building level granted for free (it counts as a built level), a recolonized abandoned planet (you receive the points of what is still standing on it).

### The ranking
11. The ranking is **computed live**. Points are shown rounded down; that rounded number is also what [beginner protection](/en/players/beginner-protection) uses.
12. The **progression** arrows compare your rank and points with the latest daily snapshot of the ranking.
13. The **Humans** filter hides non-human players (marked "AI player (PvE)") without changing ranks: everyone keeps their rank in the universe.
14. **Search** finds a player or an alliance by name or tag. Clicking a player opens their **card**: rank, badges ("AI player (PvE)", "On vacation", "New player") and a button to message them.
15. Two players tied on points are separated by an internal order, not by seniority.

### Alliance rankings
16. **Alliance Power**: the sum of all members' Points. The treasury and alliance talents do not count.
17. **Alliance Progression**: the alliance's level and experience; on a tie, the first to get there ranks higher. See [Alliances](/en/players/alliances).

## Worked example

- You raise the Mineral Excavator from level {lvl - 1} to level {lvl} for {N(mine[0])} metal and {N(mine[1])} crystal: **+{N(round(mine_pts, 2))} points** of economy (the ranking shows the integer part).
- You build a Battleship ({N(S['battleship'][3])} metal, {N(S['battleship'][4])} crystal): **+{N(bs)} points** of military.
- You build 10 Stellar Freighters ({N(S['large_cargo'][3] + S['large_cargo'][4])} resources each): **+{N(lc10)} points** of military. Civilian ships count.
- You fire 10 Long-Range Warheads: **{N(-wh10)} points** of military, whether they hit or not.
- Your Battleship is destroyed in combat and the Repair Station does not recover it: **{N(-bs)} points** of military.

## Detailed data

Points of each ship (catalogue cost):

{table(['Ship', 'Metal', 'Crystal', 'Hydrogen', 'Points'], ships)}

Points of each defense and missile:

{table(['Defense', 'Metal', 'Crystal', 'Hydrogen', 'Points'], defs)}

| Ranking | What counts | What lowers it |
|---|---|---|
| Economy | Building levels, planets and moons | Demolition, abandoned colony, destroyed moon |
| Research | Technology levels | Nothing |
| Military | Every ship, defense and missile | Units destroyed, missiles fired, abandoned colony, destroyed moon |
| Points | Sum of the three | All of the above |

## Common pitfalls

- **A transport fleet counts**: 100 Stellar Freighters are worth {N(100 * points(*S['large_cargo'][3:]))} military points, and losing them takes those away.
- **Firing missiles costs points**, even when they are intercepted.
- **Climbing the ranking changes your protection**: crossing a tier changes who you may attack and who may attack you.
- **Abandoning a colony makes your points drop**, but not your research.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Alliances](/en/players/alliances)
- [Building list](/en/economy/buildings)
- [Technology list](/en/research/technologies)
- [Ship list](/en/fleet/ships)
- [Defense list](/en/defense/defenses)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/rankings', body(lang),
          description='Les quatre classements de joueurs, les deux classements d\'alliance et le calcul des points.' if lang == 'fr' else 'The four player rankings, the two alliance rankings and how points are counted.')
