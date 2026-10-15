"""Page research/technologies (FR et EN), calculée depuis research_lib."""
import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_lib import *
from write import ROOT, write, table

src = (ROOT / 'fr' / 'research' / 'technologies.md').read_text()
IMG = {}
for r in RESEARCH:
    m = re.search(r'<img src="([^"]+)" width="48" alt="' + re.escape(nm(r[0], 'fr')), src)
    IMG[r[0]] = m.group(1) if m else None
assert all(IMG.values()), [k for k, v in IMG.items() if not v]

def img(code, lang):
    return f'<img src="{IMG[code]}" width="48" alt="{nm(code, lang)}"> '

# Exemples recalculés
EX_CODE, EX_L, EX_LAB = 'espionage', 4, 4
ex_cost = cost(EX_CODE, EX_L)
ex_t = research_seconds(EX_CODE, EX_L, EX_LAB)
ex_pts = points(EX_CODE, EX_L)
ex_t15 = hasten(ex_t, 15)
grav = [cost('graviton', L)[3] for L in (1, 2, 3)]
fus0, fus10 = fusion(10, 0), fusion(10, 10)
# Plasma : exemple sur des mines au niveau 13 (production brute, vitesse ×1)
mine13 = (int(30 * 13 * 1.1 ** 13), int(20 * 13 * 1.1 ** 13))
plasma1 = (fl(mine13[0] * 1 * PLASMA[0] / 100), fl(mine13[1] * 1 * PLASMA[1] / 100))

SHIP_BY = {s[0]: s for s in SHIPS}
SPEED = {'small_cargo': (5000, 10), 'recycler': (2000, 300), 'bomber': (4000, 700)}  # vitesse et consommation de base (table ship)

def effects(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    E = {
     'energy_science': (f"Augmente la production d'énergie du {nm('fusion_plant', lang)} (formule plus bas) : un Réacteur niveau 10 donne {N(fus0)} énergie sans Science Énergétique, {N(fus10)} avec Science Énergétique 10. Aucun effet sur les Capteurs photovoltaïques ni les Collecteurs solaires.",
                        f"Raises the energy output of the {nm('fusion_plant', lang)} (formula below): a level 10 Reactor gives {N(fus0)} energy without Energy Science, {N(fus10)} with Energy Science 10. No effect on Photovoltaic Sensors or Solar Collectors."),
     'plasma': (f"Par niveau : {P(1)} de métal, {P(0.66)} de cristal et {P(0.33)} d'hydrogène en plus, calculés sur la production brute des mines de chaque planète (Base planetaire exclue).",
                f"Per level: {P(1)} metal, {P(0.66)} crystal and {P(0.33)} hydrogen on top, worked out on the gross output of each planet's mines (Planetary Base excluded)."),
     'quantum_computing': ("Emplacements de flotte = 1 + niveau. Une expédition occupe aussi un emplacement.",
                           "Fleet slots = 1 + level. An expedition also takes a slot."),
     'research_network': ("Met en réseau les Centres d'innovation de vos autres planètes pour raccourcir les recherches (voir [Collaboration Stellaire](/fr/research/stellar-collaboration)).",
                          "Pools the Innovation Centers of your other planets to shorten research (see [Stellar Collaboration](/en/research/stellar-collaboration))."),
     'interstellar_diplomacy': ("Niveau 1 requis pour fonder une alliance. Fixe la capacité de l'alliance que vous fondez (tableau plus bas).",
                                "Level 1 needed to found an alliance. Sets the capacity of the alliance you found (table below)."),
     'combustion_drive': (f"+{P(10)} de vitesse par niveau pour les vaisseaux qui volent au Propulseur Chimique.",
                          f"+{P(10)} speed per level for ships flying on the Combustion Drive."),
     'impulse_drive': (f"+{P(20)} de vitesse par niveau pour les vaisseaux qui volent au Moteur Magnétique. Portée des {nm('long_range_warheads', lang)} : 5 × niveau − 1 systèmes. Au niveau 5, la {nm('small_cargo', lang)} passe à ce moteur.",
                       f"+{P(20)} speed per level for ships flying on the Impulse Drive. {nm('long_range_warheads', lang)} range: 5 × level − 1 systems. At level 5, the {nm('small_cargo', lang)} switches to this drive."),
     'hyperspace_drive': (f"+{P(30)} de vitesse par niveau pour les vaisseaux qui volent à la Navigation Transdimensionnelle. Le {nm('bomber', lang)} y passe au niveau 8, le {nm('recycler', lang)} au niveau 15.",
                          f"+{P(30)} speed per level for ships flying on the Hyperspace Drive. The {nm('bomber', lang)} switches to it at level 8, the {nm('recycler', lang)} at level 15."),
     'laser': ("Aucun effet propre : prérequis de technologies, de vaisseaux et de défenses.",
               "No effect of its own: a requirement for technologies, ships and defenses."),
     'ion': ("Aucun effet propre : prérequis de technologies, de vaisseaux et de défenses.",
             "No effect of its own: a requirement for technologies, ships and defenses."),
     'hyperspace': (f"+{P(5)} de capacité de soute par niveau (transport, pillage, recyclage, trouvailles d'expédition). Niveau 7 requis pour la Porte de saut.",
                    f"+{P(5)} cargo capacity per level (transport, plunder, recycling, expedition finds). Level 7 needed for the Jump gate."),
     'weapons': (f"+{P(10)} d'attaque par niveau pour vos vaisseaux et vos défenses, et +{P(10)} de dégâts par niveau pour vos {nm('long_range_warheads', lang)}.",
                 f"+{P(10)} attack per level for your ships and defenses, and +{P(10)} damage per level for your {nm('long_range_warheads', lang)}."),
     'shielding': (f"+{P(10)} de bouclier par niveau pour vos vaisseaux et vos défenses.",
                   f"+{P(10)} shield per level for your ships and defenses."),
     'armor': (f"+{P(10)} de structure par niveau pour vos vaisseaux et vos défenses.",
               f"+{P(10)} structure per level for your ships and defenses."),
     'graviton': ("Prérequis du Colossus stellaire. Se paie en énergie produite, ne prend aucun temps et ne rapporte aucun point.",
                  f"Requirement for the {nm('battle_cruiser', lang)}. Paid in energy produced, takes no time and earns no points."),
     'espionage': (f"Profondeur des rapports d'espionnage et contre-espionnage (voir [Espionner](/fr/espionage/spying)) ; −{P(5)} par niveau sur l'hydrogène des missions d'espionnage, jusqu'à −{P(50)} ; au niveau 10, une position espionnée reste découverte durablement.",
                   f"Depth of spy reports and counter-espionage (see [Spying](/en/espionage/spying)); −{P(5)} per level on the hydrogen of spy missions, down to −{P(50)}; at level 10, a spied position stays discovered for good."),
     'astrophysics': ("Nombre de planètes, expéditions simultanées et maintien maximal d'une expédition (tableau plus bas). Niveau 1 requis pour les expéditions.",
                      "Number of planets, simultaneous expeditions and longest expedition hold (table below). Level 1 needed for expeditions."),
    }
    return {k: v[0 if fr else 1] for k, v in E.items()}

def section_of(code, lang):
    for (fr, en), codes in SECTIONS:
        if code in codes:
            return fr if lang == 'fr' else en

def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    eff = effects(lang)
    order = [c for _, codes in SECTIONS for c in codes]
    t_eff = table(['Technologie', 'Effet'] if fr else ['Technology', 'Effect'],
                  [[img(c, lang) + nm(c, lang), eff[c]] for c in order])
    rows = []
    for c in order:
        code, cat, pos, mx, f, base, rq = RES[c]
        m_, c_, h_, e_ = base
        c1 = (f'{N(e_)} {"énergie requise" if fr else "required energy"}' if e_ else f'{N(m_)} / {N(c_)} / {N(h_)}')
        fac = str(f).replace('.', ',') if fr else str(f)
        pre = ', '.join(f'{nm(rc, lang)} {lv}' for t, rc, lv in rq)
        rows.append([nm(c, lang), section_of(c, lang), c1, fac, N(mx), pre])
    t_cat = table(['Technologie', 'Rubrique en jeu', 'Coût du niveau 1 (métal / cristal / hydrogène)', 'Facteur', 'Niveau max', 'Prérequis']
                  if fr else ['Technology', 'In-game section', 'Level 1 cost (metal / crystal / hydrogen)', 'Factor', 'Max level', 'Requirements'], rows)
    astro = table(['Niveau', 'Planètes au total (planète mère comprise)', 'Expéditions simultanées', "Maintien maximal d'une expédition"]
                  if fr else ['Level', 'Planets in total (home planet included)', 'Simultaneous expeditions', 'Longest expedition hold'],
                  [[L, max_bases(L), expeditions(L), f'{hold_hours(L)} h' if L else ('aucun' if fr else 'none')] for L in range(0, RES['astrophysics'][3] + 1)])
    dipl = table(['Niveau du fondateur' if fr else "Founder's level"] + [str(L) for L in ALLIANCE_CAPACITY],
                 [["Membres de l'alliance" if fr else 'Alliance members'] + [str(v) for v in ALLIANCE_CAPACITY.values()]])
    switch = []
    for code, (lvl_res, lvl) in [('small_cargo', ('impulse_drive', 5)), ('bomber', ('hyperspace_drive', 8)), ('recycler', ('hyperspace_drive', 15))]:
        s = SHIP_BY[code]
        up = [u for u in s[4] if DRIVE_OF[u[1]] == lvl_res and u[0] == lvl][0]
        b_sp, b_fc = SPEED[code]
        switch.append([nm(code, lang), nm(DRIVE_OF[s[3]], lang), f'{nm(lvl_res, lang)} {lvl}', f'{N(b_sp)} → {N(up[2])}', f'{N(b_fc)} → {N(up[3])}'])
    t_switch = table(['Vaisseau', 'Moteur de départ', 'Change de moteur à', 'Vitesse de base', 'Consommation de base']
                     if fr else ['Ship', 'Starting drive', 'Switches drive at', 'Base speed', 'Base consumption'], switch)
    if fr:
        return f'''# Liste des technologies

> **En bref** : les 17 technologies se recherchent dans un Centre d'innovation. Un niveau acquis vaut pour toutes vos planètes de l'univers. Elles débloquent bâtiments, vaisseaux et défenses, et donnent des bonus permanents : production, énergie, vitesse, soute, combat, espionnage, colonies, emplacements de flotte. Une seule étude avance à la fois dans tout l'empire.
{{.is-info}}

> **Paramètre d'univers** : la vitesse de recherche divise la durée des recherches.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

## Règles

1. Une recherche se lance depuis une planète équipée d'un **Centre d'innovation**. Ses prérequis de bâtiment (le niveau du Centre d'innovation, le plus souvent) se lisent sur **cette planète**, ses prérequis de recherche sur tout l'empire.
2. Un niveau acquis profite à **toutes vos planètes** de l'univers.
3. **Coût** du niveau N = coût du niveau 1 × facteur^(N − 1), arrondi à l'inférieur pour chaque ressource. La recherche est **payée au lancement**.
4. **Durée** (formule plus bas) : elle ne dépend que du métal et du cristal du niveau, du **niveau effectif** du Centre d'innovation et de la vitesse de recherche de l'univers. L'hydrogène ne la change pas.
5. **Niveau effectif** = Centre d'innovation de la planète qui lance la recherche, plus les Centres mis en réseau par la [Collaboration Stellaire](/fr/research/stellar-collaboration). Il est fixé au lancement.
6. **Bonus de vitesse** (alliance, talents) : la durée est divisée par (1 + bonus). Les talents de vitesse de recherche plafonnent à {P(25)}, alliance et talents ensemble à {P(45)} ; quelques talents de classe s'y ajoutent au-delà (voir [Le Théoricien](/fr/dynasty/classes/theorist) et les autres classes). Une réduction de coût par un talent ne raccourcit pas la durée : celle-ci se calcule sur le coût du catalogue.
7. **Une seule étude à la fois pour tout l'empire.** Chaque planète a sa propre file de recherche (même taille que les [files de construction](/fr/economy/build-queue)) ; les études en file, toutes planètes confondues, passent à tour de rôle dans l'ordre où elles ont été placées. Une étude en file n'est payée qu'à son tour ; si sa planète n'a pas les ressources à ce moment-là, elle est abandonnée sans frais.
8. **Second centre d'innovation** (talent ultime de l'arbre commun) : une seconde étude peut avancer en même temps que la première, à {P(50)} de la vitesse normale. Elle doit porter sur une autre technologie, et ne démarre en parallèle que si aucune étude n'attend en file (voir [L'arbre commun](/fr/dynasty/common-tree)).
9. **Points** : 1 point de recherche par tranche de 1 000 ressources dépensées (métal, cristal et hydrogène).
10. **Manipulation Gravitationnelle** se paie en **énergie** : la production d'énergie de la planète qui lance la recherche doit atteindre le seuil demandé, rien n'est consommé. Elle ne prend aucun temps et ne rapporte aucun point.
11. **Annulation** : comme pour un bâtiment, 80 % du coût × part du temps restant (voir [Files de construction](/fr/economy/build-queue)).
12. Tant que le Centre d'innovation d'une planète est **en chantier**, le jeu n'y lance ni n'y met en file aucune recherche.
13. Chaque technologie a un **niveau maximum**.

### Formule de durée

$$t = \\frac{{M + C}}{{1\\,000 \\times (1 + L)}} \\times \\frac{{3\\,600}}{{v}}$$

- $t$ : durée en secondes, arrondie à la seconde ;
- $M$, $C$ : métal et cristal du niveau étudié (coût du catalogue) ;
- $L$ : niveau effectif du Centre d'innovation (règle 5) ;
- $v$ : vitesse de recherche de l'univers.

Avec un bonus de vitesse $b$ en pour cent (règle 6) :

$$t' = \\left\\lceil \\frac{{100 \\times t}}{{100 + b}} \\right\\rceil$$

- $t'$ : durée finale en secondes, arrondie au supérieur et jamais sous 1 seconde ;
- $b$ : somme des bonus de vitesse de recherche (alliance et talents), plafonnée comme dit en règle 6.

### Production du Réacteur thermonucléaire

$$E = 30 \\times N \\times (1{{,}}05 + 0{{,}}01 \\times S)^N$$

- $E$ : énergie produite, arrondie à l'inférieur ;
- $N$ : niveau du Réacteur thermonucléaire ;
- $S$ : niveau de Science Énergétique.

## Exemple chiffré

Renseignement Tactique niveau 4, lancé depuis une planète dont le Centre d'innovation est au niveau 4, sans Collaboration Stellaire :
- Coût : 200 × 2^3 = **{N(ex_cost[0])} métal**, **{N(ex_cost[1])} cristal** et **{N(ex_cost[2])} hydrogène**.
- Durée : ({N(ex_cost[0])} + {N(ex_cost[1])}) / (1 000 × (1 + 4)) = 1,92 h, soit **{dur(ex_t)}**.
- Avec {P(15)} de vitesse de recherche (talents) : {N(ex_t)} × 100 / 115, arrondi au supérieur, soit **{dur(ex_t15)}**.
- Points de recherche gagnés : ({N(ex_cost[0])} + {N(ex_cost[1])} + {N(ex_cost[2])}) / 1 000 = **{n(ex_pts, lang)}**.

Manipulation Gravitationnelle : le niveau 1 demande une production d'énergie de **{N(grav[0])}**, le niveau 2 **{N(grav[1])}**, le niveau 3 **{N(grav[2])}** (facteur 3).

Maîtrise du Plasma niveau 1, sur une planète avec Excavateur minéral et Extracteur cristallin au niveau 13 (vitesse ×1) : les mines produisent {N(mine13[0])} métal et {N(mine13[1])} cristal par heure ; le Plasma ajoute **{N(plasma1[0])} métal** ({P(1)}) et **{N(plasma1[1])} cristal** ({P(0.66)}) par heure.

## Données détaillées

### Effets

{t_eff}

### Coûts, maxima et prérequis

{t_cat}

Le coût du niveau N se calcule avec le facteur : par exemple, Systèmes Offensifs niveau 5 coûte 800 × 2^4 = 12 800 métal et 3 200 cristal. Les tables complètes niveau par niveau sont prévues sur des pages à part.

### Cosmologie Appliquée

{astro}

Planètes au total = 1 + partie entière((niveau + 1) / 2). Expéditions simultanées = partie entière(√niveau), prises sur vos emplacements de flotte. Maintien maximal = niveau, en heures.

### Diplomatie Stellaire

{dipl}

Seul compte le niveau du **fondateur** de l'alliance. La capacité monte dès que le fondateur termine un niveau, et ne redescend jamais.

### Changement de moteur

Trois vaisseaux changent de moteur quand une technologie de propulsion atteint un niveau donné. Leur vitesse de base et leur consommation deviennent alors celles du nouveau moteur, et c'est la technologie de ce moteur qui les accélère.

{t_switch}

## Pièges fréquents

- **Le Centre de la planète compte** : la durée et les prérequis se lisent sur la planète qui lance la recherche. Lancez depuis votre meilleur Centre ; une colonie au Centre trop faible ne peut pas lancer une technologie qui en demande davantage.
- **L'hydrogène n'allonge pas la recherche** : seuls le métal et le cristal entrent dans la durée. L'hydrogène compte dans les points.
- **Une étude en file n'est pas payée** : préparez les ressources sur la bonne planète avant son tour.
- **Calcul Quantique limite vos flottes** : avec le niveau 2, vous n'avez que 3 flottes en vol, expéditions comprises.
- **Une colonie de plus tous les deux niveaux** : Cosmologie Appliquée 2 ne donne pas de planète de plus que le niveau 1.
- **Science Énergétique n'améliore que le Réacteur thermonucléaire**, pas les Capteurs photovoltaïques ni les Collecteurs solaires.
- **Manipulation Gravitationnelle ne consomme pas d'énergie**, mais il faut la produire au moment du lancement : Capteurs, Réacteur et Collecteurs solaires de la planète comptent.
- **Systèmes Photoniques et Manipulation Ionique n'ont pas d'effet propre** : on les monte pour ce qu'ils débloquent.

## Pages liées

- [Arbre technologique](/fr/research/tech-tree)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Files de construction](/fr/economy/build-queue)
- [Liste des bâtiments](/fr/economy/buildings)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Déplacements](/fr/fleet/movement)
- [Coloniser](/fr/universe/colonization)
- [Expéditions](/fr/fleet/expeditions)
- [Alliances](/fr/players/alliances)
- [L'arbre commun](/fr/dynasty/common-tree)
'''
    return f'''# Technologies list

> **In short**: the 17 technologies are researched in an Innovation Center. A level you gain applies to all your planets in the universe. They unlock buildings, ships and defenses, and give permanent bonuses: output, energy, speed, cargo, combat, espionage, colonies, fleet slots. Only one study runs at a time across the whole empire.
{{.is-info}}

> **Universe setting**: the research speed divides research times.
> Default: **×1** · Redline: **×1**
{{.is-info}}

## Rules

1. Research is started from a planet with an **Innovation Center**. Its building requirements (most often the Innovation Center level) are read on **that planet**, its research requirements across the whole empire.
2. A level you gain applies to **all your planets** in the universe.
3. **Cost** of level N = level 1 cost × factor^(N − 1), rounded down for each resource. Research is **paid when it starts**.
4. **Duration** (formula below): it only depends on the level's metal and crystal, the **effective level** of the Innovation Center and the universe's research speed. Hydrogen does not change it.
5. **Effective level** = Innovation Center of the planet starting the research, plus the Centers networked by [Stellar Collaboration](/en/research/stellar-collaboration). It is set when the study starts.
6. **Speed bonuses** (alliance, talents): the duration is divided by (1 + bonus). Research speed talents are capped at {P(25)}, alliance and talents together at {P(45)}; a few class talents come on top of that (see [The Theorist](/en/dynasty/classes/theorist) and the other classes). A cost cut from a talent does not shorten the duration: it is worked out on the catalogue cost.
7. **Only one study at a time across the whole empire.** Each planet has its own research queue (same size as the [build queues](/en/economy/build-queue)); queued studies from all planets take their turn in the order they were placed. A queued study is only paid when its turn comes; if its planet lacks the resources then, it is dropped at no cost.
8. **Second Innovation Center** (ultimate talent of the common tree): a second study can run alongside the first, at {P(50)} of the normal speed. It must be on another technology, and only starts in parallel when no study is waiting in a queue (see [The common tree](/en/dynasty/common-tree)).
9. **Points**: 1 research point per 1,000 resources spent (metal, crystal and hydrogen).
10. **Graviton Technology** is paid in **energy**: the energy output of the planet starting the research must reach the required threshold; nothing is used up. It takes no time and earns no points.
11. **Cancelling**: as for a building, 80% of the cost × share of the time left (see [Build queues](/en/economy/build-queue)).
12. While a planet's Innovation Center is **being upgraded**, the game neither starts nor queues any research there.
13. Every technology has a **maximum level**.

### Duration formula

$$t = \\frac{{M + C}}{{1{{,}}000 \\times (1 + L)}} \\times \\frac{{3{{,}}600}}{{v}}$$

- $t$: duration in seconds, rounded to the second;
- $M$, $C$: metal and crystal of the level studied (catalogue cost);
- $L$: effective Innovation Center level (rule 5);
- $v$: the universe's research speed.

With a speed bonus $b$ in percent (rule 6):

$$t' = \\left\\lceil \\frac{{100 \\times t}}{{100 + b}} \\right\\rceil$$

- $t'$: final duration in seconds, rounded up and never under 1 second;
- $b$: sum of the research speed bonuses (alliance and talents), capped as rule 6 says.

### Thermonuclear Reactor output

$$E = 30 \\times N \\times (1.05 + 0.01 \\times S)^N$$

- $E$: energy produced, rounded down;
- $N$: Thermonuclear Reactor level;
- $S$: Energy Science level.

## Worked example

Espionage Technology level 4, started from a planet whose Innovation Center is level 4, without Stellar Collaboration:
- Cost: 200 × 2^3 = **{N(ex_cost[0])} metal**, **{N(ex_cost[1])} crystal** and **{N(ex_cost[2])} hydrogen**.
- Duration: ({N(ex_cost[0])} + {N(ex_cost[1])}) / (1,000 × (1 + 4)) = 1.92 h, that is **{dur(ex_t)}**.
- With {P(15)} research speed (talents): {N(ex_t)} × 100 / 115, rounded up, that is **{dur(ex_t15)}**.
- Research points gained: ({N(ex_cost[0])} + {N(ex_cost[1])} + {N(ex_cost[2])}) / 1,000 = **{n(ex_pts, lang)}**.

Graviton Technology: level 1 needs an energy output of **{N(grav[0])}**, level 2 **{N(grav[1])}**, level 3 **{N(grav[2])}** (factor 3).

Plasma Technology level 1, on a planet with Mineral Excavator and Crystal Extractor at level 13 (speed ×1): the mines make {N(mine13[0])} metal and {N(mine13[1])} crystal per hour; Plasma adds **{N(plasma1[0])} metal** ({P(1)}) and **{N(plasma1[1])} crystal** ({P(0.66)}) per hour.

## Detailed data

### Effects

{t_eff}

### Costs, maximum levels and requirements

{t_cat}

Level N cost follows from the factor: for instance, Weapon Systems level 5 costs 800 × 2^4 = 12,800 metal and 3,200 crystal. Full level-by-level tables are planned on separate pages.

### Astrophysics

{astro}

Planets in total = 1 + whole part of ((level + 1) / 2). Simultaneous expeditions = whole part of √level, taken from your fleet slots. Longest hold = level, in hours.

### Stellar Diplomacy

{dipl}

Only the alliance **founder's** level counts. Capacity goes up when they complete a level, and never goes down.

### Drive switch

Three ships switch drive when a propulsion technology reaches a given level. Their base speed and fuel consumption then become the new drive's, and that drive's technology speeds them up.

{t_switch}

## Common pitfalls

- **The planet's Center matters**: duration and requirements are read on the planet starting the research. Start from your best Center; a colony with too weak a Center cannot start a technology that asks for more.
- **Hydrogen does not lengthen research**: only metal and crystal go into the duration. Hydrogen counts for points.
- **A queued study is not paid**: get the resources ready on the right planet before its turn.
- **Quantum Computing limits your fleets**: at level 2, you only have 3 fleets in flight, expeditions included.
- **One more colony every two levels**: Astrophysics 2 gives no more planets than level 1.
- **Energy Science only improves the Thermonuclear Reactor**, not Photovoltaic Sensors or Solar Collectors.
- **Graviton Technology does not use up energy**, but you must produce it when the study starts: the planet's Sensors, Reactor and Solar Collectors count.
- **Laser Technology and Ion Technology have no effect of their own**: you raise them for what they unlock.

## Related pages

- [Tech tree](/en/research/tech-tree)
- [Stellar Collaboration](/en/research/stellar-collaboration)
- [Build queues](/en/economy/build-queue)
- [Buildings list](/en/economy/buildings)
- [Ships list](/en/fleet/ships)
- [Fleet movement](/en/fleet/movement)
- [Colonization](/en/universe/colonization)
- [Expeditions](/en/fleet/expeditions)
- [Alliances](/en/players/alliances)
- [The common tree](/en/dynasty/common-tree)
'''

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'research/technologies', body(lang))
