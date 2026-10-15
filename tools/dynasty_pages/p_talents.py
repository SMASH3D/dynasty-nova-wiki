"""Page dynasty/talents, FR et EN, d'après le code (DONNEES §18).

Usage : python3 tools/dynasty_pages/p_talents.py
"""
from dyn_lib import DATA, RULES, CEIL, n, pct, tree
from write import write, table

XP = DATA['experience']
STARTS = XP['LEVEL_STARTS']
PER_POINT = XP['EXPERIENCE_PER_POINT']
LAST = XP['LAST_REWARDED_LEVEL']
CMAX, KMAX, ULT = RULES['COMMON_MAX_POINTS'], RULES['CLASS_MAX_POINTS'], RULES['ULTIMATE_LEVEL']
CG, KG = RULES['COMMON_ROW_GATES'], RULES['CLASS_ROW_GATES']
CR, KR = RULES['COMMON_ROW_RANKS'], RULES['CLASS_ROW_RANKS']
PRICE, COOL = DATA['respec']['price'], DATA['respec']['cooldown_hours']
WARN_EN = '''> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{.is-warning}
'''


def common_pts(level):
    return min(CMAX, level)


def class_pts(mastery):
    return min(KMAX, (mastery + 1) // 2)


def first_mastery(points):
    """Plus petite maîtrise qui donne `points` points de classe."""
    return next(m for m in range(0, LAST + 1) if class_pts(m) >= points)


BRANCH_C = sum(int(v) for v in CR.values())   # 28
BRANCH_K = sum(int(v) for v in KR.values())   # 15
ABOVE_LAST_C = BRANCH_C - 1 - int(CR[str(len(CR))]) + 1 - int(CR[str(len(CR) - 1)])  # rangées 1 à 8 : 22
ROWS8_C = sum(int(CR[str(r)]) for r in range(1, 9))   # 22
ROWS8_K = sum(int(KR[str(r)]) for r in range(1, 9))   # 14
ROWS6_K = sum(int(KR[str(r)]) for r in range(1, 7))   # 10
ULT_MASTERY = first_mastery(BRANCH_K)                  # 29


def gates_text(gates, lang):
    """Rangées regroupées par porte : [(première, dernière, points)]."""
    groups, rows = [], sorted(int(r) for r in gates)
    for r in rows:
        g = gates[str(r)]
        if groups and groups[-1][2] == g:
            groups[-1][1] = r
        else:
            groups.append([r, r, g])
    return groups


def rows_label(a, b, lang):
    if a == b:
        return (f'rangée {a}' if lang == 'fr' else f'row {a}')
    if b == a + 1:
        return (f'rangées {a} et {b}' if lang == 'fr' else f'rows {a} and {b}')
    return (f'rangées {a} à {b}' if lang == 'fr' else f'rows {a} to {b}')


def gate_cells(gates, lang):
    out = []
    for a, b, g in gates_text(gates, lang):
        out.append(f"{rows_label(a, b, lang)} : {'ouvertes' if g == 0 else f'{g} points'}" if lang == 'fr'
                   else f"{rows_label(a, b, lang)}: {'open' if g == 0 else f'{g} points'}")
    return ' ; '.join(out) if lang == 'fr' else '; '.join(out)


# Niveaux repères : portes de l'arbre commun, portes et ultime de l'arbre de classe, ultime commun, dernier niveau.
MILESTONES = {}
for r, g in CG.items():
    if g:
        MILESTONES.setdefault(g, []).append(('c', int(r)))
for r, g in KG.items():
    if g:
        MILESTONES.setdefault(first_mastery(g), []).append(('k', int(r)))
MILESTONES.setdefault(ULT_MASTERY, []).append(('ku', 0))
MILESTONES.setdefault(ULT, []).append(('cu', 0))
MILESTONES.setdefault(1, [])
MILESTONES.setdefault(LAST, [])


def opens(level, lang):
    things = MILESTONES.get(level, [])
    c = sorted(r for k, r in things if k == 'c')
    k = sorted(r for k, r in things if k == 'k')
    out = []
    if level == 1:
        out.append('commun et classe, rangées 1 à 3' if lang == 'fr' else 'common and class, rows 1 to 3')
    if c:
        out.append(('commun, ' if lang == 'fr' else 'common, ') + rows_label(c[0], c[-1], lang))
    if k:
        out.append(('classe, ' if lang == 'fr' else 'class, ') + rows_label(k[0], k[-1], lang))
    if any(x[0] == 'ku' for x in things):
        out.append("ultime de classe (branche pleine)" if lang == 'fr' else 'class ultimate (full branch)')
    if any(x[0] == 'cu' for x in things):
        out.append("ultime commun (avec la branche pleine)" if lang == 'fr' else 'common ultimate (with the full branch)')
    if level == LAST:
        out.append('tout le budget' if lang == 'fr' else 'the whole budget')
    return ', '.join(out)


def level_rows(lang):
    rows = []
    for lvl in sorted(MILESTONES):
        rows.append([lvl, n(STARTS[lvl - 1], lang), common_pts(lvl), class_pts(lvl), opens(lvl, lang)])
    return rows


def pc(x, lang):
    return pct(x, lang)


def caps_rows(lang):
    """Plafonds des bonus partagés (PlayerBonuses, ClassCaps)."""
    C, P = CEIL, (lambda x: pc(x, lang))
    fr = lang == 'fr'
    pts = (lambda x: f'{n(x, lang)} points')
    return [
        ['Vitesse de flotte' if fr else 'Fleet speed', P(C['FLEET_SPEED_COMMON_CEILING']),
         (f"+{P(C['FLEET_SPEED_ACCENT_CEILING'])} sur une famille de missions : attaques, espionnages et destructions de lune (Amiral), missions pacifiques ou vers une cible abandonnée (Navigateur), recyclage (Amiral, Archiviste), attaque préparée (Oracle, {P(9)})"
          if fr else f"+{P(C['FLEET_SPEED_ACCENT_CEILING'])} on a mission family: attacks, espionage and moon destruction (Admiral), peaceful missions or missions to an abandoned target (Navigator), recycling (Admiral, Archivist), prepared strike (Oracle, {P(9)})"),
         P(C['FLEET_SPEED_TALENT_CEILING']), P(C['FLEET_SPEED_CEILING'])],
        ['Hydrogène consommé' if fr else 'Hydrogen burned', '−' + P(C['FUEL_CONSUMPTION_COMMON_CEILING']),
         (f"−{P(C['FUEL_CONSUMPTION_ACCENT_CEILING'])} sur les vaisseaux de combat (Amiral)" if fr else f"−{P(C['FUEL_CONSUMPTION_ACCENT_CEILING'])} on combat ships (Admiral)"),
         '−' + P(C['FUEL_CONSUMPTION_TALENT_CEILING']), '−' + P(C['FUEL_CONSUMPTION_CEILING'])],
        ['Capacité de fret' if fr else 'Cargo capacity', P(25), '', P(C['CARGO_TALENT_CEILING']), P(C['CARGO_TALENT_CEILING'])],
        ['Flottes en vol' if fr else 'Fleets in flight', '+2', ('+1 réservée aux attaques (Amiral)' if fr else '+1 reserved for attacks (Admiral)'),
         f"+{C['FLEET_SLOTS_CEILING']}", f"+{C['FLEET_SLOTS_CEILING']}"],
        ['Vitesse de recherche' if fr else 'Research speed', P(15) + (' (+15 % sur deux recherches avec Astrométrie)' if fr else ' (+15% on two studies with Astrometry)'), '',
         P(C['RESEARCH_SPEED_TALENT_CEILING']), P(C['RESEARCH_SPEED_CEILING'])],
        ['Production des mines' if fr else 'Mine production', P(25), '', P(C['PRODUCTION_TALENT_CEILING']), P(C['PRODUCTION_CEILING'])],
        ['Capacité des entrepôts' if fr else 'Storage capacity', P(20), '', P(C['STORAGE_TALENT_CEILING']), P(C['STORAGE_CEILING'])],
        ['Vitesse des bâtiments' if fr else 'Building speed', P(25),
         (f"+{P(C['BUILDING_SPEED_ACCENT_CEILING'])} au plus sur une famille : rattrapage des colonies (Bâtisseur), centrales (Énergéticien, {P(10)}), centres d'innovation (Théoricien, {P(9)})"
          if fr else f"+{P(C['BUILDING_SPEED_ACCENT_CEILING'])} at most on a family: colony catch-up (Builder), power plants (Energetician, {P(10)}), innovation centers (Theorist, {P(9)})"),
         P(C['BUILDING_SPEED_TALENT_CEILING']) + (f" ({P(40)} sur la famille)" if fr else f" ({P(40)} on the family)"),
         P(C['BUILDING_SPEED_CEILING']) + (f" ({P(C['BUILDING_SPEED_ACCENT_SCOPE_CEILING'])} sur la famille)" if fr else f" ({P(C['BUILDING_SPEED_ACCENT_SCOPE_CEILING'])} on the family)")],
        ['Vitesse des vaisseaux et défenses' if fr else 'Ship and defence build speed', P(C['UNIT_SPEED_CEILING']),
         (f"+{P(C['UNIT_SPEED_ACCENT_CEILING'])} sur une famille : vaisseaux de combat (Amiral), défenses et missiles (Vétéran), vaisseaux civils (Navigateur)"
          if fr else f"+{P(C['UNIT_SPEED_ACCENT_CEILING'])} on a family: combat ships (Admiral), defences and missiles (Veteran), civil ships (Navigator)"),
         P(C['UNIT_SPEED_CEILING']) + (f" ({P(C['UNIT_SPEED_CEILING'] + C['UNIT_SPEED_ACCENT_CEILING'])} sur la famille)" if fr else f" ({P(C['UNIT_SPEED_CEILING'] + C['UNIT_SPEED_ACCENT_CEILING'])} on the family)"), ''],
        ['Coûts des bâtiments, vaisseaux et défenses' if fr else 'Building, ship and defence costs', '',
         (f"−{P(C['COST_REDUCTION_CEILING'])} (Bâtisseur)" if fr else f"−{P(C['COST_REDUCTION_CEILING'])} (Builder)"), '−' + P(C['COST_REDUCTION_CEILING']), ''],
        ['Cases de planète' if fr else 'Planet fields', '+2', ('+2 (Symbiote)'), f"+{C['PLANET_FIELDS_CEILING']}", ''],
        ['Pillage des cibles abandonnées' if fr else 'Plunder of abandoned targets', '+' + pts(20), '', '+' + pts(C['RUIN_LOOT_RATE_POINTS_CEILING']), ''],
        ['Ressources à l\'abri du pillage' if fr else 'Resources sheltered from plunder', pts(5),
         ('Vétéran (Abri souterrain), Oracle (La cache)' if fr else 'Veteran (Underground Shelter), Oracle (The Cache)'),
         (f"{pts(15)} pour le Vétéran, {pts(10)} pour l'Oracle, {pts(5)} pour les autres, arbre commun compris" if fr
          else f"{pts(15)} for the Veteran, {pts(10)} for the Oracle, {pts(5)} for the others, common tree included"),
         (f"taux de pillage jamais sous {P(C['LOOT_RATE_FLOOR'])}" if fr else f"plunder rate never below {P(C['LOOT_RATE_FLOOR'])}")],
    ]


def body(lang):
    fr = lang == 'fr'
    ex20_c, ex20_k = common_pts(20), class_pts(20)
    rtab = table(['Niveau', 'Expérience totale', 'Points communs', 'Points de classe (maîtrise égale)', "Ce qui s'ouvre"] if fr else
                 ['Level', 'Total experience', 'Common points', 'Class points (equal mastery)', 'What opens'], level_rows(lang))
    gtab = table(['Arbre', 'Portes (points placés au-dessus de la rangée, toutes branches confondues)', 'Ultime'] if fr else
                 ['Tree', 'Gates (points placed above the row, every branch together)', 'Ultimate'],
                 [['Commun' if fr else 'Common', gate_cells(CG, lang), (f'niveau {ULT} et branche pleine au-dessus' if fr else f'level {ULT} and full branch above')],
                  ['Classe' if fr else 'Class', gate_cells(KG, lang), ('branche pleine au-dessus, sans condition de niveau' if fr else 'full branch above, no level requirement')]])
    ctab = table(['Bonus', 'Arbre commun', 'Accent de classe', 'Plafond des talents', 'Plafond total (avec l\'alliance)'] if fr else
                 ['Bonus', 'Common tree', 'Class accent', 'Talent cap', 'Total cap (with the alliance)'], caps_rows(lang))
    box_fr = f'''> **Paramètre d'univers** : l'expérience par point de classement est divisée par la vitesse d'économie de l'univers.
> Par défaut : **×1, {PER_POINT} par point** · Redline : **×1, {PER_POINT} par point**
{{.is-info}}'''
    box_en = f'''> **Universe setting**: the experience per ranking point is divided by the universe's economy speed.
> Default: **×1, {PER_POINT} per point** · Redline: **×1, {PER_POINT} per point**
{{.is-info}}'''
    if fr:
        return f'''# Les talents

> **En bref** : vous avez deux arbres. L'**arbre commun** reçoit 1 point par niveau, {CMAX} au maximum, et porte les bonus génériques. L'**arbre de classe** reçoit 1 point par 2 niveaux de maîtrise, {KMAX} au maximum, et porte les mécaniques de votre classe. Vous préparez vos choix en brouillon, puis vous validez. Un point validé ne se reprend que par une réinitialisation.
{{.is-info}}

## Règles

### Deux arbres, deux réserves
1. L'**arbre commun** : 3 branches de {len(CR)} rangées, {BRANCH_C} points par branche. Il reçoit **1 point par niveau** de votre personnage, **{CMAX} au maximum**.
2. L'**arbre de classe** : 3 branches de {len(KR)} rangées, {BRANCH_K} points par branche. Il reçoit **1 point par 2 niveaux de maîtrise** de votre classe, arrondi au supérieur, **{KMAX} au maximum**. Voir [Maîtrise de classe](/fr/dynasty/classes#maîtrise-de-classe).
3. Les deux réserves sont **séparées** : un point commun ne va jamais dans l'arbre de classe, et l'inverse.

### Nœuds et rangées
4. Chaque rangée d'une branche contient un nœud. Quatre sortes de nœuds :
   - **à rangs** : chaque point ajoute un rang (3 rangs dans l'arbre de classe, 3 ou 5 dans l'arbre commun) ;
   - **choix** : un seul point, deux options **A** et **B**, une seule à la fois ;
   - **clé** : un seul point, une mécanique ;
   - **ultime** : la dernière rangée de chaque branche, un seul point.
5. Un nœud ne s'ouvre que lorsque le **nœud au-dessus de lui est plein** (pour un choix : une option prise). Une branche se remplit donc de haut en bas.
6. Chaque arbre a trois ultimes, et votre budget n'en permet qu'**un**.

### Portes
7. Une rangée s'ouvre quand les rangées **au-dessus d'elle** contiennent assez de points, **toutes branches confondues**.

{gtab}

8. Un **ultime** demande en plus que **tous les nœuds au-dessus de lui dans sa branche** soient pleins. Dans l'arbre commun, il demande aussi le **niveau {ULT}**. Dans l'arbre de classe, il n'y a pas de condition de niveau : une branche pleine suffit, soit {BRANCH_K} points de classe, atteints à la maîtrise {ULT_MASTERY}.

### Brouillon et validation
9. Vous placez et retirez vos points librement en **brouillon**. Rien ne s'applique tant que vous n'avez pas cliqué sur **Valider**.
10. Un point validé est **définitif** : il ne se reprend que par une réinitialisation. Une option de choix validée ne change pas non plus.

### Réinitialisation
11. Chaque arbre se réinitialise **séparément** et rend tous ses points d'un coup.
12. La **première** réinitialisation de chaque arbre est **gratuite**. Les suivantes coûtent **{PRICE} Points stellaires** et demandent **{COOL} heures** d'attente depuis la précédente du même arbre.
13. Elle est impossible tant qu'une **flotte ennemie** se dirige vers l'une de vos planètes, et tant qu'une de vos **flottes d'attaque** est en route vers sa cible (le retour ne bloque rien). Un arbre vide n'a rien à réinitialiser : rien n'est facturé.
14. Un [changement de classe](/fr/dynasty/classes#changer-de-classe) vide l'arbre de classe et rend sa prochaine réinitialisation gratuite. L'arbre commun ne bouge pas.

### Plafonds
15. Chaque bonus a un **plafond pour les talents** (les deux arbres ensemble) et un **plafond total**, talents d'alliance compris. Un point qui ferait dépasser un plafond n'ajoute rien.
16. Le trait de votre dynastie s'ajoute **au-delà** du plafond des talents, puis l'alliance ; le plafond total reste le même pour tout le monde.
17. Une classe peut renforcer un bonus commun, mais seulement sur un **périmètre étroit** (une famille de missions, de vaisseaux ou de bâtiments). C'est un **accent**, avec son propre plafond.
18. Les bonus de vitesse de flotte (talents et alliance) **divisent la durée du vol** : +50 % de vitesse = un vol 1,5 fois plus court. Voir [Déplacements](/fr/fleet/movement).

## Exemple chiffré

**Au niveau 20, avec une classe jouée depuis le début**
- Arbre commun : **{ex20_c} points**. Les rangées 7 et 8 s'ouvrent dès que {CG['7']} points sont placés au-dessus d'elles.
- Arbre de classe : maîtrise 20, soit **{ex20_k} points**. Les rangées 4 à 6 sont ouvertes, les rangées 7 à 9 attendent {KG['7']} points placés au-dessus.

**Une branche commune pleine**
- Elle coûte {BRANCH_C} points. Ses rangées 1 à 8 en contiennent {ROWS8_C}, mais la rangée 9 demande {CG['9']} points au-dessus d'elle : il faut en avoir placé **{CG['9'] - ROWS8_C} ailleurs** avant de la finir.
- Au niveau {CMAX}, il reste {CMAX - BRANCH_C} points pour une deuxième branche, assez pour aller jusqu'à sa rangée 8, sans son ultime.
- Dans l'arbre de classe, les rangées 1 à 8 d'une branche contiennent {ROWS8_K} points : la porte de {KG['7']} s'ouvre sans rien placer ailleurs. Avec {KMAX} points, il en reste {KMAX - BRANCH_K} pour une deuxième branche, jusqu'à sa rangée 6 ({ROWS6_K} points).

**Une réinitialisation**
- Première réinitialisation de l'arbre commun : gratuite.
- Deuxième, le lendemain : {PRICE} Points stellaires, possible {COOL} heures après la première.

## Données détaillées

### Points par niveau

L'expérience vient des quêtes et de votre record de points : **{PER_POINT} points d'expérience par point** de [classement](/fr/players/rankings) gagné au-delà de votre meilleur total. Perdre des points ne retire pas d'expérience.

{box_fr}

{rtab}

Au-delà du niveau {LAST}, l'expérience continue de compter, chaque niveau coûtant autant que le {LAST}e, mais ne donne plus de point.

### Plafonds des bonus partagés

{ctab}

Les bonus qui ne servent qu'à vous, sur vos retours ou entre vos propres planètes (Vent arrière, Liaisons internes, Retour victorieux…), sont **hors** du plafond de vitesse.

## Pièges fréquents

- **Valider trop vite** : un point validé ne se reprend pas sans réinitialisation, et seule la première est gratuite.
- **Viser deux ultimes** : deux branches pleines demandent {2 * BRANCH_C} points communs ou {2 * BRANCH_K} points de classe. Le budget n'en permet qu'une.
- **Attendre le niveau {ULT} pour un ultime de classe** : il ne demande que sa branche pleine.
- **Réinitialiser pendant un raid** : une flotte ennemie en approche, ou l'une de vos attaques en route, bloque la réinitialisation jusqu'à l'impact.
- **Empiler un bonus au-delà de son plafond** : les points en trop ne donnent rien. Vérifiez le plafond avant d'ajouter un talent d'alliance sur le même bonus.
- **Lire +50 % de vitesse comme un vol deux fois plus court** : la vitesse divise la durée. +50 % donne un vol de 1 h en 40 min.

## Pages liées

- [Les classes](/fr/dynasty/classes)
- [L'arbre commun](/fr/dynasty/common-tree)
- [Missions et station d'alliance](/fr/players/alliance-missions)
- [Classements et points](/fr/players/rankings)
- [Déplacements](/fr/fleet/movement)
'''
    return f'''# Talents

> **In short**: you have two trees. The **common tree** gets 1 point per level, {CMAX} at most, and carries the generic bonuses. The **class tree** gets 1 point per 2 mastery levels, {KMAX} at most, and carries your class's mechanics. You prepare your choices as a draft, then you confirm. A confirmed point only comes back through a reset.
{{.is-info}}

{WARN_EN}
## Rules

### Two trees, two pools
1. The **common tree**: 3 branches of {len(CR)} rows, {BRANCH_C} points per branch. It gets **1 point per level** of your character, **{CMAX} at most**.
2. The **class tree**: 3 branches of {len(KR)} rows, {BRANCH_K} points per branch. It gets **1 point per 2 mastery levels** of your class, rounded up, **{KMAX} at most**. See [Class mastery](/en/dynasty/classes#class-mastery).
3. The two pools are **separate**: a common point never goes into the class tree, and the other way round.

### Nodes and rows
4. Each row of a branch holds one node. Four kinds of nodes:
   - **ranked**: each point adds a rank (3 ranks in the class tree, 3 or 5 in the common tree);
   - **choice**: a single point, two options **A** and **B**, only one at a time;
   - **key**: a single point, a mechanic;
   - **ultimate**: the last row of each branch, a single point.
5. A node only opens once the **node above it is full** (for a choice: an option taken). A branch therefore fills from top to bottom.
6. Each tree has three ultimates, and your budget only allows **one**.

### Gates
7. A row opens when the rows **above it** hold enough points, **every branch together**.

{gtab}

8. An **ultimate** also requires **every node above it in its branch** to be full. In the common tree, it also requires **level {ULT}**. In the class tree there is no level requirement: a full branch is enough, that is {BRANCH_K} class points, reached at mastery {ULT_MASTERY}.

### Draft and confirmation
9. You place and remove your points freely as a **draft**. Nothing applies until you click **Confirm**.
10. A confirmed point is **final**: it only comes back through a reset. A confirmed choice option cannot be changed either.

### Reset
11. Each tree is reset **separately** and gives back all its points at once.
12. The **first** reset of each tree is **free**. The next ones cost **{PRICE} Stellar Points** and require **{COOL} hours** since the previous reset of the same tree.
13. It is impossible while an **enemy fleet** is heading for one of your planets, and while one of your **attack fleets** is on its way to its target (the way back blocks nothing). An empty tree has nothing to reset: nothing is charged.
14. A [class change](/en/dynasty/classes#changing-class) empties the class tree and makes its next reset free. The common tree does not move.

### Caps
15. Each bonus has a **talent cap** (both trees together) and a **total cap**, alliance talents included. A point that would go past a cap adds nothing.
16. Your dynasty's trait adds **past** the talent cap, then the alliance; the total cap stays the same for everyone.
17. A class may strengthen a common bonus, but only on a **narrow scope** (a family of missions, ships or buildings). This is an **accent**, with its own cap.
18. Fleet speed bonuses (talents and alliance) **divide the flight duration**: +50% speed = a flight 1.5 times shorter. See [Movement](/en/fleet/movement).

## Worked example

**At level 20, with a class played from the start**
- Common tree: **{ex20_c} points**. Rows 7 and 8 open as soon as {CG['7']} points are placed above them.
- Class tree: mastery 20, that is **{ex20_k} points**. Rows 4 to 6 are open, rows 7 to 9 wait for {KG['7']} points placed above.

**A full common branch**
- It costs {BRANCH_C} points. Its rows 1 to 8 hold {ROWS8_C}, but row 9 requires {CG['9']} points above it: you must have placed **{CG['9'] - ROWS8_C} elsewhere** before finishing it.
- At level {CMAX}, {CMAX - BRANCH_C} points remain for a second branch, enough to reach its row 8, without its ultimate.
- In the class tree, rows 1 to 8 of a branch hold {ROWS8_K} points: the {KG['7']}-point gate opens without placing anything elsewhere. With {KMAX} points, {KMAX - BRANCH_K} remain for a second branch, down to its row 6 ({ROWS6_K} points).

**A reset**
- First reset of the common tree: free.
- Second one, the next day: {PRICE} Stellar Points, possible {COOL} hours after the first.

## Detailed data

### Points per level

Experience comes from quests and from your points record: **{PER_POINT} experience points per [ranking](/en/players/rankings) point** gained above your best total. Losing points takes no experience away.

{box_en}

{rtab}

Past level {LAST}, experience keeps counting, each level costing as much as level {LAST}, but no longer gives any point.

### Caps of the shared bonuses

{ctab}

The bonuses that only serve you, on your way home or between your own planets (Tailwind, Internal Links, Victorious Return…), are **outside** the speed cap.

## Common pitfalls

- **Confirming too fast**: a confirmed point does not come back without a reset, and only the first one is free.
- **Aiming for two ultimates**: two full branches require {2 * BRANCH_C} common points or {2 * BRANCH_K} class points. The budget only allows one.
- **Waiting for level {ULT} for a class ultimate**: it only requires its full branch.
- **Resetting during a raid**: an incoming enemy fleet, or one of your attacks on its way, blocks the reset until impact.
- **Stacking a bonus past its cap**: extra points give nothing. Check the cap before adding an alliance talent on the same bonus.
- **Reading +50% speed as a flight twice as short**: speed divides the duration. +50% turns a 1 h flight into 40 min.

## Related pages

- [The classes](/en/dynasty/classes)
- [The common tree](/en/dynasty/common-tree)
- [Alliance missions and station](/en/players/alliance-missions)
- [Rankings and points](/en/players/rankings)
- [Movement](/en/fleet/movement)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'dynasty/talents', body(lang))
