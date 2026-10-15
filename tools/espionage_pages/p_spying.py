import sys; sys.path.insert(0, sys.argv[1])
from esp_lib import *; from write import *

# Exemple : Renseignement 6 contre 4, 6 puis 10 Éclaireurs ; 30 puis 100 vaisseaux en orbite.
A, D = 6, 4
e6, e10 = effective(A, D, 6), effective(A, D, 10)
raw30, c30 = raw_chance(D, A, 30), chance(D, A, 30)
raw100, c100 = raw_chance(D, A, 100), chance(D, A, 100)
assert e6 == 5 and e10 == 7 and c30 == MIN_CHANCE and chance(D, 2 * D, 100) == 0
# avec Réseau d'informateurs 2 : le niveau d'attaque passe à 8 = 2 × 4, plus de risque
c_inf = chance(D, A + 2, 100)
e_inf = effective(A + 2, D, 6)


def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    probe_rows = []
    for lo, hi in [(1, 1), (2, 3), (4, 5), (6, 7), (8, 9), (10, None)]:
        b = probe_bonus(lo)
        assert hi is None or probe_bonus(hi) == b
        if lang == 'fr':
            label = str(lo) if hi == lo else (f'{lo} à {hi}' if hi else f'{lo} et plus')
        else:
            label = str(lo) if hi == lo else (f'{lo} to {hi}' if hi else f'{lo} or more')
        probe_rows.append((label, f'+{b}' if b else '0'))
    fuel_rows = [[l, P(round(fuel_factor(l) * 100))] for l in range(0, 11)]
    tier_rows = []
    bounds = [t[0] for t in TIERS] + [None]
    for i, t in enumerate(TIERS):
        hi = bounds[i + 1]
        if lang == 'fr':
            lv = f'{t[0]} à {hi - 1}' if hi else f'{t[0]} et plus'
        else:
            lv = f'{t[0]} to {hi - 1}' if hi else f'{t[0]} or more'
        tier_rows.append([lv, ', '.join(sections(t[0], lang))])
    if lang == 'fr':
        return f'''# Espionner

> **En bref** : envoyez des Éclaireurs sur une planète ou une lune pour obtenir un rapport sur ses ressources, sa flotte, ses défenses, ses bâtiments et ses recherches. Ce que vous voyez dépend de votre écart de Renseignement Tactique avec la cible et du nombre d'Éclaireurs envoyés. Si la cible a des vaisseaux en orbite, vos sondes peuvent être abattues.
{{.is-info}}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Éclaireur">

## Règles

### Envoyer des sondes

1. L'espionnage se fait en mission **Espionnage**, avec des **Éclaireurs seulement** : aucun autre vaisseau ne peut les accompagner. Le bouton d'espionnage rapide de la [vue galaxie](/fr/universe/galaxy-view) lance la même mission.
2. Vous pouvez espionner toute **planète ou lune** qui n'est pas à vous : un joueur protégé, un membre de votre alliance, une planète inhabitée ou abandonnée. L'espace lointain ne s'espionne pas.
3. L'espionnage **ne compte pas** dans la limite d'attaques et ne met pas fin à votre protection.
4. L'hydrogène facturé pour une mission d'espionnage baisse de **5 %** par niveau de **Renseignement Tactique**, jusqu'à **la moitié** au niveau 10 (arrondi à l'unité inférieure). La consommation du vol, elle, ne change pas.
5. Pendant une **maintenance**, l'espionnage est suspendu. Si **vous** êtes en mode vacances, vous ne pouvez envoyer aucune mission.

### La case découverte

6. Une case de la vue galaxie reste illisible tant que personne ne l'a espionnée pour vous. Dès votre premier espionnage, sa planète et son propriétaire s'affichent, **sans limite de durée**.
7. **Vision partagée d'alliance** : chaque case qu'un membre espionne est découverte pour **toute l'alliance**. En rejoignant une alliance, vous lui apportez les cases que vous aviez déjà découvertes. Une case connue grâce à l'alliance porte la mention « Découverte par un membre de l'alliance », sans date : seule la découverte est partagée, jamais le rapport.
8. La vision partagée vaut dès votre arrivée dans l'alliance et disparaît quand vous la quittez. Vos propres découvertes vous restent.
9. Coloniser une planète ou recycler un champ de débris demande que la case ait été espionnée, par vous **ou par votre alliance**. Vos propres planètes et l'espace lointain en sont dispensés.

### Niveau de détail

10. Le **niveau effectif** de votre espionnage se calcule ainsi :

$$N = \\max\\left(0,\\ R_a - R_d + \\min\\left(5,\\ \\left\\lfloor \\frac{{E}}{{2}} \\right\\rfloor\\right)\\right)$$

- $N$ : niveau effectif de l'espionnage ;
- $R_a$ : votre niveau de Renseignement Tactique, plus les niveaux de Réseau d'informateurs de votre alliance ;
- $R_d$ : le niveau de Renseignement Tactique de la cible, plus les niveaux de Contre-espionnage fédéré de son alliance ;
- $E$ : nombre d'Éclaireurs envoyés ; $\\lfloor\\ \\rfloor$ : partie entière.

11. Selon ce niveau, le rapport révèle : les **ressources** dès 1, la **flotte** dès 3, les **défenses et missiles** dès 5, les **bâtiments** dès 7, les **recherches** dès 9. Le type, la taille et les températures de la planète sont toujours visibles.
12. Chaque paire d'Éclaireurs ajoute 1 niveau, jusqu'à **+5 avec 10 Éclaireurs**. Au delà, le bonus ne monte plus : les bâtiments et les recherches demandent une vraie avance en Renseignement Tactique.
13. **Talents d'alliance** : **Réseau d'informateurs** ajoute 1 niveau à votre Renseignement Tactique quand vous espionnez, **Contre-espionnage fédéré** 1 niveau à celui de vos planètes espionnées, par niveau de talent ({ALLIANCE_TALENT_MAX} niveaux chacun, branche Renseignement). Ces niveaux comptent comme de la recherche : ils changent le détail **et** le risque. Ils s'appliquent après **{ALLIANCE_QUARANTINE_HOURS} heures** dans l'alliance (voir [Missions et station d'alliance](/fr/players/alliance-missions)).
14. Certains **talents de dynastie** de l'[Ombre](/fr/dynasty/classes/shadow) lisent plus profond ou ouvrent la flotte et les ressources plus tôt. Ceux-là ne changent pas le risque.

### Risque pour les sondes

15. La **chance d'être abattu** se calcule ainsi, puis se borne entre **5 % et 25 %** :

$$C = (2 \\times R_d - R_a) \\times V \\times 0{{,}}05$$

- $C$ : chance, en pourcentage, que la vague soit abattue ;
- $R_d$ et $R_a$ : les niveaux de la règle 10 ;
- $V$ : nombre de vaisseaux stationnés sur la planète ou la lune espionnée.

16. Le risque est **nul** si votre niveau atteint le **double** de celui de la cible, s'il n'y a **aucun vaisseau** en orbite (les défenses ne comptent pas), ou si la cible est inhabitée, abandonnée ou en vacances.
17. **Un seul tirage pour toute la vague** : toutes les sondes sont abattues, ou aucune. Le nombre d'Éclaireurs ne change pas le risque. Il n'y a pas de combat. Exceptions : certains talents de l'[Ombre](/fr/dynasty/classes/shadow) ramènent une partie d'une vague prise.
18. Une vague abattue rapporte **quand même** son rapport, qui indique combien de sondes ont été perdues. Les sondes perdues sont détruites pour de bon.

### Ce que voit la cible

19. La cible reçoit une **alerte d'intrusion** : « Sonde repérée », sans nom, si la vague est passée sans encombre.
20. Si la vague a été abattue, l'alerte **identifie** l'espion (son pseudo), et peut aussi **localiser son origine** (pseudo et coordonnées de la planète de départ).
21. Pas d'alerte sur une planète abandonnée, chez un joueur en vacances, ni pour un joueur qui a désactivé les alertes d'intrusion dans ses préférences de rapports.

## Exemple chiffré

Vous avez Renseignement Tactique {A}, la cible le niveau {D}.
- Avec **6 Éclaireurs** : ({A} − {D}) + min(5, 3) = **{e6}** : ressources, flotte, défenses et missiles. Pas les bâtiments (il faut 7).
- Avec **10 Éclaireurs** : ({A} − {D}) + 5 = **{e10}** : les bâtiments apparaissent. Les recherches (9) restent hors de portée, même avec plus de sondes.

Risque, si la cible a 30 vaisseaux en orbite : (2 × {D} − {A}) × 30 × 0,05 = {N(raw30)}, relevé au plancher de **{P(c30)}**. Avec 100 vaisseaux : {N(raw100)}, soit **{P(c100)}**.

Si votre alliance détient Réseau d'informateurs niveau 2, votre niveau compte pour {A} + 2 = 8, le double de {D} : le risque tombe à **{P(c_inf)}**, et 6 Éclaireurs lisent désormais au niveau **{e_inf}** (bâtiments compris).

## Données détaillées

| Niveau effectif | Le rapport révèle aussi |
|---|---|
| 0 | rien de plus que la planète (type, taille, températures) |
{chr(10).join(f'| {r[0]} | {r[1]} |' for r in tier_rows)}

{table(['Éclaireurs envoyés'] + [r[0] for r in probe_rows], [['Bonus'] + [r[1] for r in probe_rows]])}

Hydrogène facturé pour une mission d'espionnage, selon votre niveau de Renseignement Tactique (part du coût normal) :

{table(['Niveau'] + [str(r[0]) for r in fuel_rows[:6]], [['Facturé'] + [r[1] for r in fuel_rows[:6]]])}

{table(['Niveau'] + [str(r[0]) for r in fuel_rows[6:]] + ['11 à 15'], [['Facturé'] + [r[1] for r in fuel_rows[6:]] + [P(50)]])}

## Pièges fréquents

- **Inutile d'envoyer plus de 10 sondes** : le bonus plafonne à +5, et le risque ne dépend pas du nombre.
- **Toutes ou aucune** : si le tirage échoue, vous perdez toute la vague.
- **Une orbite vide n'abat aucune sonde** : sans vaisseau stationné, le risque est nul, même avec beaucoup de défenses.
- **Le talent d'alliance de la cible compte aussi** : Contre-espionnage fédéré augmente à la fois sa protection et le risque pour vos sondes.
- **Espionner un allié est permis** : il reçoit l'alerte comme n'importe qui.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Liste des technologies](/fr/research/technologies)
- [Missions et station d'alliance](/fr/players/alliance-missions)
'''
    return f'''# Spying

> **In short**: send Scouts to a planet or a moon to get a report on its resources, fleet, defenses, buildings and research. What you see depends on your Espionage Technology gap with the target and on how many Scouts you send. If the target has ships in orbit, your probes can be shot down.
{{.is-info}}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{{.is-warning}}

<img src="/images/illustrations/ships/eclaireur.jpg" width="180" alt="Scout">

## Rules

### Sending probes

1. Spying is done on an **Espionage** mission, with **Scouts only**: no other ship may go along. The quick spy button of the [galaxy view](/en/universe/galaxy-view) launches the same mission.
2. You can spy on any **planet or moon** that is not yours: a protected player, a member of your alliance, an uninhabited or abandoned planet. Deep space cannot be spied on.
3. Espionage **does not count** towards the attack limit and does not end your protection.
4. The hydrogen charged for a spy mission drops by **5%** per **Espionage Technology** level, down to **half** at level 10 (rounded down). The flight's actual consumption does not change.
5. During **maintenance**, espionage is suspended. If **you** are on vacation, you cannot send any mission.

### Discovered cells

6. A cell of the galaxy view stays unreadable until someone has spied on it for you. From your first spy run on, its planet and owner are shown, **with no time limit**.
7. **Shared alliance vision**: every cell a member spies on is discovered for **the whole alliance**. When you join an alliance, you bring it the cells you had already discovered. A cell known through the alliance reads "Discovered by an alliance member", without a date: only the discovery is shared, never the report.
8. The shared vision applies as soon as you join the alliance and is gone when you leave it. Your own discoveries stay yours.
9. Colonizing a planet or recycling a debris field requires the cell to have been spied on, by you **or by your alliance**. Your own planets and deep space are exempt.

### Detail level

10. The **effective level** of your espionage is:

$$N = \\max\\left(0,\\ R_a - R_d + \\min\\left(5,\\ \\left\\lfloor \\frac{{E}}{{2}} \\right\\rfloor\\right)\\right)$$

- $N$: effective espionage level;
- $R_a$: your Espionage Technology level, plus your alliance's Informant network levels;
- $R_d$: the target's Espionage Technology level, plus its alliance's Federated counterintelligence levels;
- $E$: number of Scouts sent; $\\lfloor\\ \\rfloor$: integer part.

11. Depending on that level, the report reveals: **resources** from 1, **fleet** from 3, **defenses and missiles** from 5, **buildings** from 7, **research** from 9. The planet's type, size and temperatures are always shown.
12. Each pair of Scouts adds 1 level, up to **+5 with 10 Scouts**. Beyond that the bonus stops growing: buildings and research need a real lead in Espionage Technology.
13. **Alliance talents**: **Informant network** adds 1 level to your Espionage Technology when you spy, **Federated counterintelligence** 1 level to that of your spied planets, per talent level ({ALLIANCE_TALENT_MAX} levels each, Intelligence branch). These levels count as research: they change the detail **and** the risk. They apply after **{ALLIANCE_QUARANTINE_HOURS} hours** in the alliance (see [Alliance missions and station](/en/players/alliance-missions)).
14. Some **dynasty talents** of the [Shadow](/en/dynasty/classes/shadow) read deeper or open the fleet and resources earlier. Those do not change the risk.

### Risk to the probes

15. The **chance of being shot down** is computed as follows, then kept between **5% and 25%**:

$$C = (2 \\times R_d - R_a) \\times V \\times 0.05$$

- $C$: chance, in percent, that the wave is shot down;
- $R_d$ and $R_a$: the levels of rule 10;
- $V$: number of ships stationed on the spied planet or moon.

16. The risk is **zero** if your level reaches **twice** the target's, if there is **no ship** in orbit (defenses do not count), or if the target is uninhabited, abandoned or on vacation.
17. **A single roll for the whole wave**: either every probe is shot down, or none. The number of Scouts does not change the risk. There is no combat. Exceptions: some [Shadow](/en/dynasty/classes/shadow) talents bring part of a caught wave home.
18. A wave that is shot down **still** brings back its report, which shows how many probes were lost. Lost probes are destroyed for good.

### What the target sees

19. The target gets an **intrusion alert**: "Probe spotted", with no name, if the wave got through untouched.
20. If the wave was shot down, the alert **identifies** the spy (their username), and may also **trace its origin** (username and coordinates of the departure planet).
21. No alert on an abandoned planet, for a player on vacation, or for a player who switched intrusion alerts off in their report preferences.

## Worked example

You have Espionage Technology {A}, the target level {D}.
- With **6 Scouts**: ({A} − {D}) + min(5, 3) = **{e6}**: resources, fleet, defenses and missiles. Not the buildings (that takes 7).
- With **10 Scouts**: ({A} − {D}) + 5 = **{e10}**: the buildings show up. Research (9) stays out of reach, even with more probes.

Risk, if the target has 30 ships in orbit: (2 × {D} − {A}) × 30 × 0.05 = {N(raw30)}, raised to the **{P(c30)}** floor. With 100 ships: {N(raw100)}, so **{P(c100)}**.

If your alliance holds Informant network level 2, your level counts as {A} + 2 = 8, twice {D}: the risk drops to **{P(c_inf)}**, and 6 Scouts now read at level **{e_inf}** (buildings included).

## Detailed data

| Effective level | The report also reveals |
|---|---|
| 0 | nothing beyond the planet (type, size, temperatures) |
{chr(10).join(f'| {r[0]} | {r[1]} |' for r in tier_rows)}

{table(['Scouts sent'] + [r[0] for r in probe_rows], [['Bonus'] + [r[1] for r in probe_rows]])}

Hydrogen charged for a spy mission, by Espionage Technology level (share of the normal cost):

{table(['Level'] + [str(r[0]) for r in fuel_rows[:6]], [['Charged'] + [r[1] for r in fuel_rows[:6]]])}

{table(['Level'] + [str(r[0]) for r in fuel_rows[6:]] + ['11 to 15'], [['Charged'] + [r[1] for r in fuel_rows[6:]] + [P(50)]])}

## Common pitfalls

- **No point sending more than 10 probes**: the bonus caps at +5, and the risk does not depend on the number.
- **All or nothing**: if the roll goes wrong, you lose the whole wave.
- **An empty orbit shoots nothing down**: with no ship stationed, the risk is zero, even behind many defenses.
- **The target's alliance talent counts too**: Federated counterintelligence raises both its protection and the risk to your probes.
- **Spying on an ally is allowed**: they get the alert like anyone else.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [Sensor phalanx](/en/espionage/sensor-phalanx)
- [The galaxy view](/en/universe/galaxy-view)
- [Technologies list](/en/research/technologies)
- [Alliance missions and station](/en/players/alliance-missions)
'''


for lang in ('fr', 'en'):
    write(lang, 'espionage/spying', body(lang),
          description='Envoyer des Éclaireurs : niveau de détail, vision partagée, risques et alertes.' if lang == 'fr'
          else 'Sending Scouts: detail level, shared vision, risks and alerts.')
