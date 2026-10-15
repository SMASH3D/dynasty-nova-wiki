import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *

# ExpeditionFindCap::forLeaderPoints
CAP = [(10_000, 200), (100_000, 2_500), (1_000_000, 6_000), (5_000_000, 9_000), (25_000_000, 12_000),
       (50_000_000, 15_000), (75_000_000, 18_000), (100_000_000, 21_000), (None, 25_000)]
# ExpeditionShipLadder::standard
LADDER = ['espionage_probe', 'small_cargo', 'light_fighter', 'large_cargo', 'heavy_fighter', 'cruiser', 'battleship', 'predator', 'bomber', 'destroyer']


def exp_points(fleet):
    return max(200, sum(S[c][7] * q for c, q in fleet) // 200)


def cap_for(top):
    for lim, c in CAP:
        if lim is None or top < lim:
            return c


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    L = 0 if fr else 1
    fleet = [('large_cargo', 50), ('espionage_probe', 1)]
    lv = {'combustion_drive': 6}
    pts = exp_points(fleet); cap = cap_for(500_000)
    d = distance(0, 0, 16 - 8)
    v = min(speed(c, lv) for c, q in fleet)
    t = duration(d, 100, v)
    leg = leg_fuel(d, 100, fleet, lv)
    hold = hold_fuel(3, fleet, lv)
    total_fuel = 2 * leg + hold
    capa = sum(cargo(c, 0) * q for c, q in fleet)
    caprows = []
    prev = 0
    for lim, c in CAP:
        if lim is None:
            caprows.append([(f'{N(prev)} ou plus' if fr else f'{N(prev)} or more'), N(c)])
        else:
            caprows.append([(f'moins de {N(lim)}' if fr else f'under {N(lim)}'), N(c)])
            prev = lim
    T_cap = table(['Points du meilleur joueur' if fr else "Top player's points", 'Plafond' if fr else 'Cap'], caprows)
    nm = (lambda c: S[c][1]) if fr else (lambda c: f'*{S[c][2]}*')
    T_lad = table(['Rang' if fr else 'Rank', 'Vaisseau' if fr else 'Ship'], [[i + 1, nm(c)] for i, c in enumerate(LADDER)])
    T_slots = table(['Cosmologie Appliquée' if fr else 'Astrophysics', 'Maintien maximal' if fr else 'Longest hold', 'Expéditions simultanées' if fr else 'Simultaneous expeditions'],
                    [[lvl, f'{lvl} h', math.isqrt(lvl)] for lvl in (1, 2, 3, 4, 6, 9, 12, 16)])
    if fr:
        return f'''# Expéditions

> **En bref** : au-delà de la dernière position de chaque système s'étend l'espace lointain. Une flotte qui y tient sa position revient parfois chargée de ressources ou de vaisseaux abandonnés, parfois retardée, ou tombe sur des pirates, des aliens, voire un trou noir. Il faut la Cosmologie Appliquée pour partir.
{{.is-info}}

> **Paramètre d'univers** : les expéditions peuvent être ouvertes ou fermées selon l'univers.
> Par défaut : **ouvertes** · Redline : **ouvertes**
{{.is-info}}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Cosmologie Appliquée">

## Règles

### Partir
1. Il faut **Cosmologie Appliquée niveau 1** au minimum.
2. La cible est l'**espace lointain** du système : la position qui suit la dernière (16 sur Redline). Seuls l'Expédition et le Recyclage peuvent y aller.
3. La flotte ne peut pas être composée **uniquement d'Éclaireurs** ; un Éclaireur peut accompagner n'importe quelle autre coque. Le Collecteur solaire ne vole jamais.
4. Vous choisissez la **durée de maintien**, par heure entière : de 1 h jusqu'à autant d'heures que votre niveau de Cosmologie Appliquée.
5. **Expéditions simultanées** = partie entière de la racine carrée du niveau de Cosmologie Appliquée. Elles comptent toutes vos expéditions de l'univers, à l'aller, sur place ou au retour. Chacune occupe **aussi** un emplacement de flotte.
6. **Hydrogène** : l'aller, le retour et le maintien sont payés au départ. Le maintien coûte $\\lceil h \\times C / 10 \\rceil$, où $h$ est le nombre d'heures et $C$ la somme des consommations de base des vaisseaux envoyés (consommation × nombre). Aucun talent d'économie de carburant ne s'applique au maintien. Tout l'hydrogène du voyage doit tenir dans les soutes avec la cargaison.

### Sur place
7. La **durée de maintien ne change pas les chances** de trouver quelque chose. Elle allonge seulement le voyage et la consommation, et un éventuel retard (règle 12).
8. **Rappel** : une flotte rappelée pendant son maintien refait tout le trajet de l'aller pour rentrer et ne rapporte **rien**, ni résultat ni rapport.
9. Une zone trop visitée **s'épuise** : à partir de **10 expéditions** résolues sur l'espace lointain d'un même système en 24 heures, tous joueurs confondus, la zone est « exploitée » et les chances de trouvaille baissent ; à partir de **25**, elle est « épuisée » et elles baissent davantage. La part perdue va au résultat « rien ». Si la flotte emporte au moins un **Éclaireur**, le rapport indique l'état de la zone.

### Résultats
10. **Ressources** : un seul type de ressource par trouvaille, métal, cristal ou hydrogène. Le montant est proportionnel aux points d'expédition de la flotte (règle 15), en équivalent métal : il est divisé par 2 pour le cristal et par 3 pour l'hydrogène. La trouvaille est limitée par la **soute libre** : le surplus est perdu, et le rapport le signale.
11. **Vaisseaux** : des vaisseaux abandonnés rejoignent votre flotte, pour une valeur égale à la moitié d'une trouvaille de ressources. Ils ne prennent pas de place dans la soute. Vous pouvez trouver jusqu'au rang qui suit celui de votre meilleur vaisseau à bord (table plus bas). Jamais de Colossus stellaire, de Pionnier spatial, de Récupérateur ni de Collecteur solaire, qui ne comptent pas non plus pour le rang. Les vaisseaux trouvés rapportent leurs points militaires.
12. **Retard** : le retour est allongé de 2, 3 ou 5 fois la durée de maintien choisie, selon l'ampleur de l'événement. **Retour anticipé** : la durée du retour est divisée par 2, 3 ou 5.
13. **Pirates** et **aliens** : un vrai combat contre une flotte calquée sur la vôtre, plus forte quand l'événement est plus grand, renforcée d'une escorte. Les aliens sont plus forts que les pirates. Les pirates combattent avec vos recherches de combat moins 3 niveaux, les aliens avec 3 niveaux de plus. Vous recevez un rapport de combat ; les survivants gardent leur cargaison, sans pillage. Les débris (10 % des vaisseaux détruits, des deux camps) restent sur l'espace lointain.
14. **Trou noir** : la flotte entière et sa cargaison sont perdues. **Rien** : la flotte rentre comme elle est partie.

### Taille des trouvailles
15. **Points d'expédition** = max(200, structure totale de la flotte / 200, arrondi à l'inférieur), plafonnés selon les points du **meilleur joueur humain** de l'univers (table plus bas). Plus la flotte est grande, plus elle rapporte, jusqu'au plafond.

## Exemple chiffré

50 Cargos stellaires et 1 Éclaireur partent de [2:40:8] vers l'espace lointain [2:40:16], avec Propulseur Chimique 6, à 100 %, pour 3 heures de maintien. Le meilleur joueur de l'univers a 500 000 points.
- Distance : 1 000 + 5 × 8 = **{N(d)}**. Vitesse de la flotte : celle du Cargo, 7 500 × 1,6 = {N(v)}. Trajet : **{N(t)} s** ({hms(t, lang)}) à l'aller comme au retour.
- Hydrogène : {N(leg)} par trajet, soit {N(2 * leg)} pour l'aller-retour, plus le maintien $\\lceil 3 \\times 2\\,501 / 10 \\rceil$ = {N(hold)} : **{N(total_fuel)}** payés au départ. Ils voyagent dans les {N(capa)} de soute.
- Structure totale : 50 × 12 000 + 1 000 = 601 000. Points d'expédition : 601 000 / 200 = **{N(pts)}**, sous le plafond de **{N(cap)}** (meilleur joueur sous 1 000 000 de points).
- Avec Cosmologie Appliquée 5 : jusqu'à 5 heures de maintien et **{math.isqrt(5)}** expéditions simultanées.

## Données détaillées

### Maintien et expéditions simultanées

{T_slots}

### Plafond des points d'expédition

{T_cap}

### Rang des vaisseaux trouvés

{T_lad}

Exemple : une flotte dont le meilleur vaisseau est un Cuirassé (rang 7) peut trouver jusqu'au Prédateur (rang 8). Une flotte sans vaisseau de cette table compte comme rang 1.

## Pièges fréquents

- **Rester plus longtemps ne sert à rien** pour les chances : choisissez la durée selon votre emploi du temps. Elle allonge en plus un éventuel retard.
- **Prévoyez de la soute** : une trouvaille de ressources qui ne rentre pas est perdue, et l'hydrogène du voyage occupe déjà une partie des soutes.
- **Changez de système** : l'espace lointain très fréquenté s'épuise, quel que soit le joueur qui l'a visité.
- **Un rappel annule tout** : la flotte rentre bredouille, après un retour aussi long que l'aller.
- **Le trou noir existe** : n'envoyez pas votre flotte principale.

## Pages liées

- [Les missions](/fr/fleet/missions)
- [Déplacements](/fr/fleet/movement)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des technologies](/fr/research/technologies)
- [Coordonnées](/fr/universe/coordinates)
- [Champs de ruines](/fr/combat/debris)
'''
    return f'''# Expeditions

> **In short**: past the last position of every system lies deep space. A fleet holding position there sometimes comes back loaded with resources or abandoned ships, sometimes late, or runs into pirates, aliens, even a black hole. You need Astrophysics to go.
{{.is-info}}

> **Universe setting**: expeditions can be open or closed depending on the universe.
> Default: **open** · Redline: **open**
{{.is-info}}

<img src="/images/illustrations/research/cosmologie-appliquee.jpg" width="180" alt="Astrophysics">

## Rules

### Setting off
1. You need **Astrophysics level 1** at least.
2. The target is the system's **deep space**: the position after the last one (16 on Redline). Only Expedition and Recycling can go there.
3. The fleet cannot be **Scouts only**; a Scout may join any other hull. The Solar Collector never flies.
4. You pick the **hold duration**, in whole hours: from 1 h up to as many hours as your Astrophysics level.
5. **Simultaneous expeditions** = the integer part of the square root of your Astrophysics level. They count all your expeditions in the universe, flying out, holding or coming back. Each one **also** takes a fleet slot.
6. **Hydrogen**: the way out, the way back and the hold are paid at departure. The hold costs $\\lceil h \\times C / 10 \\rceil$, where $h$ is the number of hours and $C$ the sum of the base consumption of the ships sent (consumption × count). No fuel-saving talent applies to the hold. All the trip's hydrogen must fit in the holds alongside the cargo.

### In deep space
7. The **hold duration does not change the odds** of finding something. It only lengthens the trip and the fuel bill, and any delay (rule 12).
8. **Recall**: a fleet recalled during its hold flies the whole way out again to get home and brings back **nothing**, neither outcome nor report.
9. An over-visited area **runs dry**: from **10 expeditions** resolved in the same system's deep space within 24 hours, all players combined, the area is "exploited" and the odds of a find drop; from **25**, it is "depleted" and they drop further. The lost share goes to the "nothing" outcome. If the fleet carries at least one **Scout**, the report gives the area's state.

### Outcomes
10. **Resources**: a single resource type per find, metal, crystal or hydrogen. The amount is proportional to the fleet's expedition points (rule 15), in metal equivalent: divided by 2 for crystal and by 3 for hydrogen. The find is capped by **free cargo space**: the excess is lost, and the report says so.
11. **Ships**: abandoned ships join your fleet, worth half a resource find. They take no cargo space. You can find up to the rank right above your best ship aboard (table below). Never a Stellar Colossus, Space Pioneer, Salvager or Solar Collector, which do not count for the rank either. Found ships bring their military points.
12. **Delay**: the way back is lengthened by 2, 3 or 5 times the chosen hold duration, depending on the size of the event. **Early return**: the way back is divided by 2, 3 or 5.
13. **Pirates** and **aliens**: a real battle against a fleet modelled on yours, stronger when the event is bigger, with an escort on top. Aliens are stronger than pirates. Pirates fight with your combat research minus 3 levels, aliens with 3 levels more. You get a battle report; survivors keep their cargo, no plunder. Debris (10% of the ships destroyed, both sides) stays in deep space.
14. **Black hole**: the whole fleet and its cargo are lost. **Nothing**: the fleet comes back as it left.

### Size of finds
15. **Expedition points** = max(200, total fleet structure / 200, rounded down), capped by the points of the universe's **top human player** (table below). The bigger the fleet, the more it brings back, up to the cap.

## Worked example

50 Stellar Freighters and 1 Scout fly from [2:40:8] to deep space [2:40:16], with Combustion Drive 6, at 100%, for a 3-hour hold. The universe's top player has 500,000 points.
- Distance: 1,000 + 5 × 8 = **{N(d)}**. Fleet speed: the Freighter's, 7,500 × 1.6 = {N(v)}. Trip: **{N(t)} s** ({hms(t, lang)}) each way.
- Hydrogen: {N(leg)} per leg, so {N(2 * leg)} for the round trip, plus the hold $\\lceil 3 \\times 2{{,}}501 / 10 \\rceil$ = {N(hold)}: **{N(total_fuel)}** paid at departure. It travels in the {N(capa)} of cargo space.
- Total structure: 50 × 12,000 + 1,000 = 601,000. Expedition points: 601,000 / 200 = **{N(pts)}**, under the cap of **{N(cap)}** (top player under 1,000,000 points).
- With Astrophysics 5: up to 5 hours of hold and **{math.isqrt(5)}** simultaneous expeditions.

## Detailed data

### Hold and simultaneous expeditions

{T_slots}

### Expedition points cap

{T_cap}

### Rank of found ships

{T_lad}

Example: a fleet whose best ship is a Battleship (rank 7) can find up to a Predator (rank 8). A fleet with no ship from this table counts as rank 1.

## Common pitfalls

- **Staying longer does not help** the odds: pick the duration to suit your schedule. It also lengthens any delay.
- **Keep cargo space free**: a resource find that does not fit is lost, and the trip's hydrogen already takes part of the holds.
- **Switch systems**: a busy deep space runs dry, whoever visited it.
- **A recall cancels everything**: the fleet comes home empty-handed, after a way back as long as the way out.
- **Black holes exist**: do not send your main fleet.

## Related pages

- [Missions](/en/fleet/missions)
- [Fleet movement](/en/fleet/movement)
- [Ships list](/en/fleet/ships)
- [Technologies](/en/research/technologies)
- [Coordinates](/en/universe/coordinates)
- [Debris fields](/en/combat/debris)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/expeditions', body(lang), description=("Explorer l'espace lointain : conditions, résultats et taille des trouvailles." if lang == 'fr' else 'Exploring deep space: conditions, outcomes and size of finds.'))
