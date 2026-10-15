from combat_lib import *
from write import write, table

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    m, c = debris({'light_fighter': 100})
    units = m + c
    ch = moon_chance(units)
    dia = moon_diameters(ch)
    recyclers = math.ceil(units / SHIP['recycler'][7])
    floor_units = MOON_DEBRIS_FOR_MAX // MOON_MAX
    ship_rows = []
    for u in SHIPS:
        dm, dc = debris({u[0]: 1})
        ship_rows.append([name(u[0], lang), N(dm), N(dc)])
    chance_rows = []
    for d in (50_000, 100_000, 250_000, 500_000, 1_000_000, 2_000_000, 5_000_000):
        chv = moon_chance(d)
        ds = moon_diameters(chv) if chv else None
        chance_rows.append([N(d), P(round(chv, 2)) if chv else P(0),
                            f'{N(ds[0])} à {N(ds[-1])}' if ds and lang == 'fr' else (f'{N(ds[0])} to {N(ds[-1])}' if ds else ('pas de lune' if lang == 'fr' else 'no moon'))])
    rf = 'métal et cristal'
    if lang == 'fr':
        return f'''# Champs de ruines (débris)

> **En bref** : quand des vaisseaux sont détruits, une part de leur métal et de leur cristal forme un champ de ruines en orbite, {P(DEBRIS_SHIPS)} par défaut. Les défenses n'en laissent pas, sauf réglage de l'univers. Ces débris ne disparaissent jamais : il faut les recycler avec des Récupérateurs. Un gros combat peut aussi faire naître une lune.
{{.is-info}}

> **Paramètre d'univers** : le taux de débris des vaisseaux et des défenses, ainsi que la chance maximale de lune et les débris qui la donnent, peuvent être différents selon l'univers.
> Par défaut : vaisseaux **{P(DEBRIS_SHIPS)}**, défenses **{P(DEBRIS_DEFENSES)}**, lune **{P(MOON_MAX)} au plus, atteints à {N(MOON_DEBRIS_FOR_MAX)} de débris** · Redline : vaisseaux **{P(30)}**, défenses **{P(0)}**, lune **{P(20)} pour {N(2_000_000)}**
{{.is-info}}

<img src="/images/illustrations/ships/recuperateur.jpg" width="180" alt="Récupérateur">

## Règles

### Ce qui part en débris
1. Les vaisseaux détruits **des deux camps**, civils compris, laissent le **taux de débris des vaisseaux** de l'univers ({P(DEBRIS_SHIPS)} par défaut) de leur coût en **métal et cristal**. L'hydrogène ne laisse rien.
2. Les **défenses** détruites laissent le **taux de débris des défenses** de l'univers : **{P(DEBRIS_DEFENSES)}** par défaut, donc rien. Ce taux compte toutes les défenses détruites, même celles qui seront ensuite [reconstruites](/fr/combat/defense-rebuild).
3. Le total est arrondi à l'inférieur, pour le métal comme pour le cristal.
4. Les combats contre les pirates et les aliens d'[expédition](/fr/fleet/expeditions) laissent **{P(DEBRIS_EXPEDITION)}** des vaisseaux détruits, quel que soit l'univers.
5. Une mission [Destruction de lune](/fr/combat/moon-destruction) ne laisse **aucun débris**, ni du combat ni de la lune.
6. Les débris d'un combat **s'ajoutent** au champ déjà présent sur la case.

### Récupérer les débris
7. Les débris **ne disparaissent jamais**. Seul le recyclage les retire. Ils restent même si la planète en dessous est abandonnée.
8. Pour les récupérer, envoyez des **Récupérateurs** en mission **Recyclage**. Seule la soute des Récupérateurs compte ; ce qui ne rentre pas reste en orbite.
9. Le champ appartient à celui qui le recycle, quel que soit le vainqueur du combat.

### Formation d'une lune
10. Après une attaque, la planète visée peut gagner une **lune**. La chance se calcule sur les débris **de ce combat seulement** (métal plus cristal), pas sur le champ déjà en orbite :

$$p = \\min\\left(D \\times \\frac{{p_{{max}}}}{{D_{{max}}}},\\ p_{{max}}\\right) \\quad\\text{{et}}\\quad p = 0 \\text{{ si }} D < \\frac{{D_{{max}}}}{{p_{{max}}}}$$

- $p$ : chance de lune, en % ; $D$ : débris du combat (métal + cristal).
- $p_{{max}}$ : chance maximale de l'univers ({P(MOON_MAX)} par défaut) ; $D_{{max}}$ : débris qui donnent cette chance maximale ({N(MOON_DEBRIS_FOR_MAX)} par défaut).
- Par défaut : **1 % par tranche de {N(floor_units)} débris**, rien en dessous de {N(floor_units)}, {P(MOON_MAX)} au plus.

11. La lune revient **au propriétaire de la planète**, même s'il a perdu le combat. L'attaquant ne gagne jamais de lune chez un autre.
12. Pas de lune si la case en a déjà une, ni au-dessus d'une planète abandonnée, ni quand le combat a lieu au-dessus de la lune elle-même.
13. La formation **ne consomme pas** les débris : les Récupérateurs récoltent tout dans les deux cas.
14. **Taille de la lune** : elle est tirée parmi **11 tailles également probables**, d'autant plus grandes que la chance était élevée. Avec $X$ tiré entre 0 et 10 :

$$c = 10 + X + 60 \\times \\frac{{p}}{{p_{{max}}}} \\qquad \\text{{diamètre}} = \\left\\lfloor 1\\,000 \\sqrt{{c}} \\right\\rfloor \\text{{ km}}$$

- Le dernier terme vaut au moins 3. Une lune mesure donc de **{N(moon_diameters(1)[0])} km** (chance de 1 %) à **{N(moon_diameters(MOON_MAX)[-1])} km** (chance maximale).
- Une lune démarre avec 1 case ; au plus, elle en aura partie entière((diamètre / 1 000)²), ouvertes par la Base lunaire. Voir [Les lunes](/fr/universe/moons).

## Exemple chiffré

Vous détruisez 100 Intercepteurs ({N(3000)} métal et {N(1000)} cristal chacun), dans un univers aux réglages par défaut :
- Débris : {P(DEBRIS_SHIPS)} × {N(300000)} métal = **{N(m)} métal**, et {P(DEBRIS_SHIPS)} × {N(100000)} cristal = **{N(c)} cristal**.
- Récolte totale : {N(units)} ressources. Un Récupérateur emporte {N(SHIP['recycler'][7])} : il en faut **{recyclers}** (sans bonus de Pliage Spatial).
- Chance de lune : {N(units)} × 20 / {N(MOON_DEBRIS_FOR_MAX)} = **{P(ch)}**. Si elle se forme, elle mesure entre **{N(dia[0])} et {N(dia[-1])} km**.

## Données détaillées

Débris laissés par un vaisseau détruit, au taux de {P(DEBRIS_SHIPS)} :

{table(['Vaisseau', 'Métal', 'Cristal'], ship_rows)}

Chance de lune et diamètres possibles selon les débris du combat, réglages par défaut :

{table(['Débris du combat', 'Chance de lune', 'Diamètre (km)'], chance_rows)}

## Pièges fréquents

- **Vos propres pertes nourrissent le champ** : un combat perdu en défense laisse aussi des débris au-dessus de votre planète, que d'autres peuvent recycler.
- **Le champ n'aide pas la lune suivante** : seuls les débris du combat qui vient d'avoir lieu comptent pour la chance de lune.
- **Pliage Spatial augmente la soute** : +5 % par niveau, utile pour recycler avec moins de Récupérateurs.
- **Le premier arrivé se sert** : le champ appartient à celui qui le recycle.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Les lunes](/fr/universe/moons)
- [Station de réparation](/fr/economy/repair-station)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
'''
    return f'''# Debris fields

> **In short**: when ships are destroyed, a share of their metal and crystal forms a debris field in orbit, {P(DEBRIS_SHIPS)} by default. Defenses leave none, unless the universe says otherwise. Debris never disappears: it must be recycled with Salvagers. A big battle can also give birth to a moon.
{{.is-info}}

> **Universe setting**: the debris rate of ships and defenses, and the maximum moon chance and the debris that gives it, may differ from one universe to another.
> Default: ships **{P(DEBRIS_SHIPS)}**, defenses **{P(DEBRIS_DEFENSES)}**, moon **{P(MOON_MAX)} at most, reached at {N(MOON_DEBRIS_FOR_MAX)} debris** · Redline: ships **{P(30)}**, defenses **{P(0)}**, moon **{P(20)} for {N(2_000_000)}**
{{.is-info}}

<img src="/images/illustrations/ships/recuperateur.jpg" width="180" alt="Salvager">

## Rules

### What turns into debris
1. Destroyed ships **on both sides**, civil ones included, leave the universe's **ship debris rate** ({P(DEBRIS_SHIPS)} by default) of their cost in **metal and crystal**. Hydrogen leaves nothing.
2. Destroyed **defenses** leave the universe's **defense debris rate**: **{P(DEBRIS_DEFENSES)}** by default, so nothing. That rate counts every defense destroyed, even those later [rebuilt](/en/combat/defense-rebuild).
3. The total is rounded down, for metal as for crystal.
4. Battles against [expedition](/en/fleet/expeditions) pirates and aliens leave **{P(DEBRIS_EXPEDITION)}** of the ships destroyed, whatever the universe.
5. A [Moon destruction](/en/combat/moon-destruction) mission leaves **no debris**, neither from the battle nor from the moon.
6. A battle's debris **adds up** with the field already on the cell.

### Collecting debris
7. Debris **never disappears**. Only recycling removes it. It stays even if the planet below is abandoned.
8. To collect it, send **Salvagers** on a **Recycle** mission. Only the Salvagers' holds count; whatever does not fit stays in orbit.
9. The field belongs to whoever recycles it, whoever won the battle.

### Moon formation
10. After an attack, the target planet may gain a **moon**. The chance is computed on **this battle's debris only** (metal plus crystal), not on the field already in orbit:

$$p = \\min\\left(D \\times \\frac{{p_{{max}}}}{{D_{{max}}}},\\ p_{{max}}\\right) \\quad\\text{{and}}\\quad p = 0 \\text{{ if }} D < \\frac{{D_{{max}}}}{{p_{{max}}}}$$

- $p$: moon chance, in %; $D$: the battle's debris (metal + crystal).
- $p_{{max}}$: the universe's maximum chance ({P(MOON_MAX)} by default); $D_{{max}}$: debris that gives this maximum chance ({N(MOON_DEBRIS_FOR_MAX)} by default).
- By default: **1% per {N(floor_units)} debris**, nothing below {N(floor_units)}, {P(MOON_MAX)} at most.

11. The moon goes **to the planet's owner**, even if they lost the battle. The attacker never gains a moon over someone else's planet.
12. No moon if the cell already has one, nor over an abandoned planet, nor when the battle takes place above the moon itself.
13. Formation **does not consume** the debris: Salvagers collect all of it either way.
14. **Moon size**: it is drawn among **11 equally likely sizes**, bigger as the chance was higher. With $X$ drawn between 0 and 10:

$$c = 10 + X + 60 \\times \\frac{{p}}{{p_{{max}}}} \\qquad \\text{{diameter}} = \\left\\lfloor 1{{,}}000 \\sqrt{{c}} \\right\\rfloor \\text{{ km}}$$

- The last term is at least 3. A moon is therefore **{N(moon_diameters(1)[0])} km** (1% chance) to **{N(moon_diameters(MOON_MAX)[-1])} km** (maximum chance) wide.
- A moon starts with 1 field; at most it will have integer part((diameter / 1,000)²), opened by the Lunar base. See [Moons](/en/universe/moons).

## Worked example

You destroy 100 Interceptors ({N(3000)} metal and {N(1000)} crystal each), in a universe with default settings:
- Debris: {P(DEBRIS_SHIPS)} × {N(300000)} metal = **{N(m)} metal**, and {P(DEBRIS_SHIPS)} × {N(100000)} crystal = **{N(c)} crystal**.
- Total haul: {N(units)} resources. A Salvager carries {N(SHIP['recycler'][7])}: you need **{recyclers}** (without Hyperspace Technology bonus).
- Moon chance: {N(units)} × 20 / {N(MOON_DEBRIS_FOR_MAX)} = **{P(ch)}**. If it forms, it is between **{N(dia[0])} and {N(dia[-1])} km** wide.

## Detailed data

Debris left by one destroyed ship, at a {P(DEBRIS_SHIPS)} rate (ship names are provisional translations: the game still shows the French names):

{table(['Ship', 'Metal', 'Crystal'], ship_rows)}

Moon chance and possible diameters by the battle's debris, default settings:

{table(['Battle debris', 'Moon chance', 'Diameter (km)'], chance_rows)}

## Common pitfalls

- **Your own losses feed the field**: a battle lost while defending also leaves debris above your planet, which others can recycle.
- **The field does not help the next moon**: only the debris of the battle that just happened counts for the moon chance.
- **Hyperspace Technology raises cargo**: +5% per level, handy to recycle with fewer Salvagers.
- **First come, first served**: the field belongs to whoever recycles it.

## Related pages

- [Ship list](/en/fleet/ships)
- [Missions](/en/fleet/missions)
- [Moons](/en/universe/moons)
- [Repair Station](/en/economy/repair-station)
- [Defense rebuild](/en/combat/defense-rebuild)
'''

def run():
    write('fr', 'combat/debris', body('fr'))
    write('en', 'combat/debris', body('en'))
