from combat_lib import *
from write import write, table

DIAMETERS = (3605, 6324, 8944)
COLOSSI = (1, 4, 25, 100, 400)

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    P1 = lambda x: pct(x, lang, 1)
    D, C = 8944, 100
    root = math.sqrt(D)
    pd, pf = moon_destroy(D, C), fleet_loss(D)
    pd_res = pd * 0.75
    pf_res = pf * 0.75
    rows = [[f'{N(d)} km'] + [P1(moon_destroy(d, c)) for c in COLOSSI] + [P1(fleet_loss(d))] for d in DIAMETERS]
    hdr_fr = ['Diamètre'] + [f'{c} Colossus' for c in COLOSSI] + ['Perte de la flotte']
    hdr_en = ['Diameter'] + [f'{c} Colossus' for c in COLOSSI] + ['Fleet loss']
    sq = lambda x: d1(x, lang)
    if lang == 'fr':
        return f'''# Destruction de lune

> **En bref** : une flotte composée uniquement de Colossus stellaires peut tenter de détruire la lune d'un autre joueur. Elle doit d'abord gagner le combat contre ce qui défend la lune. Ensuite, deux tirages indépendants décident si la lune est détruite et si les Colossus sont perdus.
{{.is-info}}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Colossus stellaire">

## Règles

### La mission
1. La mission **Destruction de lune** demande une flotte composée **uniquement de Colossus stellaires**, et vise la **lune** d'un autre joueur. Elle n'est pas proposée sur une planète.
2. Elle suit les mêmes conditions qu'une attaque : elle n'est pas proposée contre un joueur protégé, un membre de votre alliance ou une cible dont la [limite d'attaques](/fr/players/attack-limit) est atteinte.

### Le combat
3. Un **combat classique** a lieu d'abord, contre les vaisseaux et les défenses **de la lune**. Voir [Déroulement d'un combat](/fr/combat/how-combat-works).
4. Les défenses de la lune détruites suivent la [reconstruction des défenses](/fr/combat/defense-rebuild).
5. Ce combat ne laisse **ni pillage, ni débris, ni lune nouvelle**.

### Les deux tirages
6. Les tirages n'ont lieu qu'en cas de **victoire** de l'attaquant. Sur un match nul ou une défaite, la lune n'est pas touchée et les survivants rentrent.
7. Avec $S$ le diamètre de la lune et $N$ le nombre de Colossus **survivants** :

$$p_{{lune}} = \\min\\left(100,\\ (100 - \\sqrt{{S}}) \\times \\sqrt{{N}}\\right) \\qquad p_{{flotte}} = \\frac{{\\sqrt{{S}}}}{{2}}$$

- $p_{{lune}}$ : chance de détruire la lune, en % ; $p_{{flotte}}$ : chance de perdre toute la flotte, en %.
- $S$ : diamètre de la lune en km ; $N$ : Colossus stellaires encore debout après le combat.

8. Les deux tirages sont **indépendants** et ont lieu tous les deux, que la lune soit détruite ou non. Les quatre issues sont possibles, la pire étant une flotte perdue au-dessus d'une lune intacte.
9. La perte de la flotte est **un seul tirage pour toute la flotte** et **ne dépend pas du nombre de Colossus** : envoyer plus de Colossus n'améliore que la chance de détruire la lune.
10. Le talent **Briseur de lunes** ([Amiral](/fr/dynasty/classes/admiral)) multiplie le risque de perdre la flotte par 0,75. Le talent **La lune tient** ([Vétéran](/fr/dynasty/classes/veteran)) multiplie la chance de détruire la lune du Vétéran par 0,75.

### Les suites
11. Si la lune est détruite : tout ce qu'elle portait disparaît, et les points correspondants sont retirés à son propriétaire. Les flottes en route vers la lune, ou qui devaient y rentrer, sont redirigées vers la planète.
12. Chaque camp reçoit un rapport **Destruction de lune**, qui donne les deux chances même quand le combat est perdu. Ce rapport peut être désactivé dans les réglages des rapports.
13. Une lune dont le propriétaire est en vacances ne peut pas être visée.

## Exemple chiffré

Une lune de **{N(D)} km** (la plus grande taille possible) et **{C} Colossus** survivants :
- √{N(D)} ≈ {sq(root)}.
- Chance de détruire la lune : (100 − {sq(root)}) × √{C} ≈ **{P1(pd)}**.
- Chance de perdre les Colossus : {sq(root)} / 2 ≈ **{P1(pf)}**.
- Avec Briseur de lunes, le risque tombe à {P1(pf)} × 0,75 ≈ **{P1(pf_res)}**. Contre un Vétéran qui a La lune tient, la chance de destruction tombe à {P1(pd)} × 0,75 ≈ **{P1(pd_res)}**.

## Données détaillées

Chance de détruire la lune selon son diamètre et le nombre de Colossus survivants, et risque de perdre la flotte (sans talent). Les lunes mesurent de {N(3605)} à {N(8944)} km.

{table(hdr_fr, rows)}

## Pièges fréquents

- **Une grosse lune est plus dure et plus dangereuse** : plus le diamètre est grand, plus la destruction est difficile et plus le risque de perdre la flotte est élevé.
- **Le nombre ne protège pas la flotte** : le risque de perte dépend seulement du diamètre.
- **Il faut gagner le combat d'abord** : sans victoire, aucun tirage. Les Colossus perdus pendant le combat ne comptent plus dans $N$.
- **Ni butin ni débris** : une destruction de lune ne rapporte rien en ressources, à aucun des deux camps.

## Pages liées

- [Les lunes](/fr/universe/moons)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Les missions](/fr/fleet/missions)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Champs de ruines et formation des lunes](/fr/combat/debris)
'''
    return f'''# Moon destruction

> **In short**: a fleet made only of Stellar Colossi can try to destroy another player's moon. It must first win the battle against whatever defends the moon. Then two independent rolls decide whether the moon is destroyed and whether the Colossi are lost.
{{.is-info}}

<img src="/images/illustrations/ships/colossus-stellaire.jpg" width="180" alt="Stellar Colossus">

## Rules

### The mission
1. The **Moon destruction** mission requires a fleet made **only of Stellar Colossi**, and targets another player's **moon**. It is not offered on a planet.
2. It follows the same conditions as an attack: it is not offered against a protected player, a member of your alliance or a target whose [attack limit](/en/players/attack-limit) is reached.

### The battle
3. A **regular battle** takes place first, against the ships and defenses **of the moon**. See [How combat works](/en/combat/how-combat-works).
4. The moon's destroyed defenses follow the [defense rebuild](/en/combat/defense-rebuild).
5. This battle leaves **no plunder, no debris and no new moon**.

### The two rolls
6. The rolls only happen if the attacker **wins**. On a draw or a defeat, the moon is untouched and the survivors fly home.
7. With $S$ the moon's diameter and $N$ the number of **surviving** Colossi:

$$p_{{moon}} = \\min\\left(100,\\ (100 - \\sqrt{{S}}) \\times \\sqrt{{N}}\\right) \\qquad p_{{fleet}} = \\frac{{\\sqrt{{S}}}}{{2}}$$

- $p_{{moon}}$: chance of destroying the moon, in %; $p_{{fleet}}$: chance of losing the whole fleet, in %.
- $S$: moon diameter in km; $N$: Stellar Colossi still standing after the battle.

8. Both rolls are **independent** and both take place, whether or not the moon is destroyed. All four outcomes are possible, the worst being a fleet lost over an intact moon.
9. Losing the fleet is **one roll for the whole fleet** and **does not depend on the number of Colossi**: sending more Colossi only improves the chance of destroying the moon.
10. The **Moonbreaker** talent ([Admiral](/en/dynasty/classes/admiral)) multiplies the risk of losing the fleet by 0.75. The **The Moon Holds** talent ([Veteran](/en/dynasty/classes/veteran)) multiplies the chance of destroying the Veteran's moon by 0.75.

### Aftermath
11. If the moon is destroyed: everything on it disappears, and the matching points are removed from its owner. Fleets on their way to the moon, or due to return to it, are redirected to the planet.
12. Each side receives a **Moon destruction** report, which gives both chances even when the battle is lost. This report can be turned off in the report settings.
13. A moon whose owner is on vacation cannot be targeted.

## Worked example

A **{N(D)} km** moon (the largest possible size) and **{C} Colossi** surviving:
- √{N(D)} ≈ {sq(root)}.
- Chance of destroying the moon: (100 − {sq(root)}) × √{C} ≈ **{P1(pd)}**.
- Chance of losing the Colossi: {sq(root)} / 2 ≈ **{P1(pf)}**.
- With Moonbreaker, the risk drops to {P1(pf)} × 0.75 ≈ **{P1(pf_res)}**. Against a Veteran holding The Moon Holds, the destruction chance drops to {P1(pd)} × 0.75 ≈ **{P1(pd_res)}**.

## Detailed data

Chance of destroying the moon by its diameter and the number of surviving Colossi, and risk of losing the fleet (no talent). Moons are {N(3605)} to {N(8944)} km wide.

{table(hdr_en, rows)}

## Common pitfalls

- **A big moon is harder and more dangerous**: the larger the diameter, the harder the destruction and the higher the risk of losing the fleet.
- **Numbers do not protect the fleet**: the risk of loss depends only on the diameter.
- **You must win the battle first**: without a victory, no roll. Colossi lost during the battle no longer count in $N$.
- **No loot, no debris**: a moon destruction brings no resources to either side.

## Related pages

- [Moons](/en/universe/moons)
- [Ship list](/en/fleet/ships)
- [Missions](/en/fleet/missions)
- [How combat works](/en/combat/how-combat-works)
- [Debris fields and moon formation](/en/combat/debris)
'''

def run():
    write('fr', 'combat/moon-destruction', body('fr'))
    write('en', 'combat/moon-destruction', body('en'))
