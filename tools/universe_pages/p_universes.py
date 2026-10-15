import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

D, R = DEFAULTS, REDLINE


def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    fr = lang == 'fr'
    tiers = lambda t: ', '.join((f'1:{r} sous {N(p)} points' if fr else f'1:{r} below {N(p)} points') for p, r in t)
    a = D['abandon']
    abandon = (f"disparition au bout de {a['life']} jours, recolonisation interdite à l'ancien propriétaire pendant {a['lock']} jours (détail : [Abandonner une colonie](/fr/universe/abandoning-a-planet))"
               if fr else f"disappears after {a['life']} days, former owner barred from recolonizing for {a['lock']} days (details: [Abandoning a colony](/en/universe/abandoning-a-planet))")
    if fr:
        rows = [
            ['Galaxies × systèmes × positions', f'fixé à la création ; de {POSITIONS_MIN} à {POSITIONS_MAX} positions par système, {GALAXIES_MAX} galaxies au plus', '9 × 99 × 15'],
            ['Joueurs maximum', 'aucun', N(R['max_players'])],
            ["Vitesse d'économie (production)", f"×{D['speeds']}", f"×{R['speeds']}"],
            ['Vitesse de construction (bâtiments, démolitions)', f"×{D['speeds']}", f"×{R['speeds']}"],
            ['Vitesse de recherche', f"×{D['speeds']}", f"×{R['speeds']}"],
            ['Vitesse de chantier (vaisseaux, défenses, réparations)', f"×{D['speeds']}", f"×{R['speeds']}"],
            ['Vitesse des flottes (durée des vols)', f"×{D['speeds']}", f"×{R['speeds']}"],
            ['Ressources de départ', 'fixées à la création', f"{N(R['start'][0])} métal, {N(R['start'][1])} cristal"],
            ["Limite d'attaques", f"{D['bashing'][0]} par {D['bashing'][1]} h", f"{R['bashing'][0]} par {R['bashing'][1]} h"],
            ['Protection des débutants', tiers(D['beginner_tiers']), tiers(R['beginner_tiers'])],
            ['Inactivité levant la protection', f"{D['beginner_inactivity_days']} jours", f"{R['beginner_inactivity_days']} jours"],
            ['Débris', f"vaisseaux {P(D['debris'][0])}, défenses {P(D['debris'][1])}", f"vaisseaux {P(R['debris'][0])}, défenses {P(R['debris'][1])}"],
            ['Formation de lune', f"{P(D['moon'][0])} au plus, atteints pour {N(D['moon'][1])} de débris", f"{P(R['moon'][0])} au plus, atteints pour {N(R['moon'][1])} de débris"],
            ['Abandon de planète', abandon, 'comme par défaut'],
            ['Files de construction', f"{D['queue'][0]} ordres, {D['queue'][1]} en Premium", f"{R['queue'][0]} ordres, {R['queue'][1]} en Premium"],
            ['Favoris', f"{D['bookmarks'][0]}, {D['bookmarks'][1]} en Premium", f"{R['bookmarks'][0]}, {R['bookmarks'][1]} en Premium"],
            ['Expéditions', 'ouvertes', 'ouvertes'],
        ]
        return f'''# Les univers

> **En bref** : Dynasty Nova se joue par univers. Chaque univers est une partie indépendante, avec sa carte, ses joueurs, son classement et ses réglages. Vous pouvez jouer dans plusieurs univers avec le même compte : votre progression y est séparée.
{{.is-info}}

> **Paramètre d'univers** : toutes les valeurs du tableau « Réglages d'un univers » peuvent être différentes selon l'univers.
> Par défaut et Redline : voir les deux colonnes du tableau.
{{.is-info}}

## Règles

### Rejoindre un univers
1. Chaque univers est **indépendant** : planètes, ressources, flottes, classement, alliances, quêtes et expérience y sont propres. Rien ne passe d'un univers à l'autre.
2. L'écran **Univers** liste vos univers et les autres univers ouverts. Un univers peut annoncer une **date d'ouverture** : un compte à rebours s'affiche, et l'inscription n'est possible qu'à partir de cette heure-là. Un univers peut aussi être **fermé aux inscriptions** : ceux qui y jouent déjà continuent.
3. À l'inscription, vous recevez une **planète mère** de **{MOTHER_SIZE} cases**, avec les **ressources de départ** de l'univers. Son emplacement est tiré au hasard : une galaxie, puis un système, puis une position du **centre du système** (positions 5 à 8 sur 15). Quand ces positions sont toutes prises, le tirage s'élargit aux positions 2 à 12, puis au système entier.
4. Pendant vos **{NEWCOMER_DAYS} premiers jours** dans un univers, vous êtes un **nouveau joueur** : personne ne peut vous attaquer (voir [Protection des débutants](/fr/players/beginner-protection)). Cette durée est la même partout.
5. Le **mode vacances** s'active univers par univers.

### Ce qui change d'un univers à l'autre
6. Chaque univers a ses **réglages** (tableau ci-dessous). Le wiki signale chaque valeur concernée par un encart « Paramètre d'univers ».
7. **Cinq vitesses indépendantes** : économie (production des mines, des collecteurs et de l'énergie), construction (bâtiments et démolitions), recherche, chantier (vaisseaux, défenses et réparations) et flottes (durée des vols). Une vitesse ×2 divise la durée par 2, ou double la production pour la vitesse d'économie. La vitesse des flottes ne change **jamais** la consommation d'hydrogène.
8. Le **nombre maximum de joueurs** est affiché sur la fiche de l'univers. Seul un univers privé refuse les inscriptions au-delà.
9. Le **type** d'univers (andromeda, orion, quantum, vega) et sa variante visuelle sont tirés au hasard à sa création. Ils ne changent que l'apparence de la carte.
10. Redline est un univers **JcJ** : les Points stellaires n'y achètent que des objets cosmétiques, jamais un avantage de jeu.
11. Certaines fonctions s'ouvrent univers par univers : les **expéditions** (ouvertes par défaut), les **missions d'alliance** (fermées par défaut, ouvertes sur Redline) et les **événements cosmiques** (météorites, pluies de comètes, impacts géants), fermés par défaut.

### Univers privés
12. Vous pouvez créer votre propre **univers privé**, avec ses joueurs, ses vitesses et ses règles : il a une date de fin, et un changement de règles y est annoncé 24 heures à l'avance (voir [Univers privés](/fr/misc/private-universes)). Les univers officiels n'ont pas de date de fin.

## Exemple chiffré

Un bâtiment demande 2 heures de construction sur Redline, où toutes les vitesses sont à ×1.
- Dans un univers dont la vitesse de construction est à ×2 : 2 / 2 = **1 heure**.
- Si seule la vitesse des flottes y est à ×2, la construction prend toujours **2 heures**, mais un vol de 4 heures n'en prend plus que 2, pour la même quantité d'hydrogène.

## Données détaillées

### Réglages d'un univers

{table(['Réglage', 'Par défaut', 'Redline'], rows)}

« Fixé à la création » : le jeu n'a pas de valeur par défaut, chaque univers reçoit la sienne.

## Pièges fréquents

- **Rien ne passe d'un univers à l'autre** : ressources, flottes et alliances restent dans leur univers.
- **Vérifiez les réglages** : un chiffre du wiki marqué « Paramètre d'univers » peut être différent dans votre univers. L'écran Univers affiche les vitesses, les débris et les lunes de chaque univers.
- **Les vitesses sont séparées** : un univers à économie rapide peut avoir des flottes lentes.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Premiers pas](/fr/getting-started/first-steps)
- [Protection des débutants](/fr/players/beginner-protection)
- [Univers privés](/fr/misc/private-universes)
'''
    tiers_en = tiers
    rows = [
        ['Galaxies × systems × positions', f'set at creation; {POSITIONS_MIN} to {POSITIONS_MAX} positions per system, {GALAXIES_MAX} galaxies at most', '9 × 99 × 15'],
        ['Maximum players', 'none', N(R['max_players'])],
        ['Economy speed (output)', f"×{D['speeds']}", f"×{R['speeds']}"],
        ['Building speed (buildings, demolitions)', f"×{D['speeds']}", f"×{R['speeds']}"],
        ['Research speed', f"×{D['speeds']}", f"×{R['speeds']}"],
        ['Shipyard speed (ships, defenses, repairs)', f"×{D['speeds']}", f"×{R['speeds']}"],
        ['Fleet speed (flight time)', f"×{D['speeds']}", f"×{R['speeds']}"],
        ['Starting resources', 'set at creation', f"{N(R['start'][0])} metal, {N(R['start'][1])} crystal"],
        ['Attack limit', f"{D['bashing'][0]} per {D['bashing'][1]} h", f"{R['bashing'][0]} per {R['bashing'][1]} h"],
        ['Beginner protection', tiers_en(D['beginner_tiers']), tiers_en(R['beginner_tiers'])],
        ['Inactivity that lifts protection', f"{D['beginner_inactivity_days']} days", f"{R['beginner_inactivity_days']} days"],
        ['Debris', f"ships {P(D['debris'][0])}, defenses {P(D['debris'][1])}", f"ships {P(R['debris'][0])}, defenses {P(R['debris'][1])}"],
        ['Moon formation', f"{P(D['moon'][0])} at most, reached at {N(D['moon'][1])} debris", f"{P(R['moon'][0])} at most, reached at {N(R['moon'][1])} debris"],
        ['Abandoning a planet', abandon, 'same as default'],
        ['Build queues', f"{D['queue'][0]} orders, {D['queue'][1]} with Premium", f"{R['queue'][0]} orders, {R['queue'][1]} with Premium"],
        ['Bookmarks', f"{D['bookmarks'][0]}, {D['bookmarks'][1]} with Premium", f"{R['bookmarks'][0]}, {R['bookmarks'][1]} with Premium"],
        ['Expeditions', 'open', 'open'],
    ]
    return f'''# Universes

> **In short**: Dynasty Nova is played in universes. Each universe is a separate game, with its own map, players, ranking and settings. You can play in several universes with the same account: your progress is kept apart in each.
{{.is-info}}

> **Universe setting**: every value in the "Universe settings" table may differ from one universe to another.
> Default and Redline: see the two columns of the table.
{{.is-info}}

## Rules

### Joining a universe
1. Each universe is **separate**: planets, resources, fleets, ranking, alliances, quests and experience are its own. Nothing carries over from one universe to another.
2. The **Universes** screen lists your universes and the other open ones. A universe may announce an **opening date**: a countdown is shown, and signing up is only possible from that time on. A universe may also be **closed to sign-ups**: those already playing there carry on.
3. When you join, you get a **mother planet** of **{MOTHER_SIZE} fields**, with the universe's **starting resources**. Its slot is drawn at random: a galaxy, then a system, then a position in the **middle of the system** (positions 5 to 8 out of 15). Once those are all taken, the draw widens to positions 2 to 12, then to the whole system.
4. During your **first {NEWCOMER_DAYS} days** in a universe you are a **new player**: nobody can attack you (see [Beginner protection](/en/players/beginner-protection)). This length is the same everywhere.
5. **Vacation mode** is switched on universe by universe.

### What changes from one universe to another
6. Each universe has its own **settings** (table below). The wiki flags every value concerned with a "Universe setting" box.
7. **Five separate speeds**: economy (output of mines, collectors and energy), building (buildings and demolitions), research, shipyard (ships, defenses and repairs) and fleet (flight time). A ×2 speed halves the time, or doubles output for the economy speed. Fleet speed **never** changes hydrogen consumption.
8. The **maximum number of players** is shown on the universe card. Only a private universe turns sign-ups away beyond it.
9. The universe **type** (andromeda, orion, quantum, vega) and its visual variant are drawn at random when it is created. They only change how the map looks.
10. Redline is a **PvP** universe: Stellar Points only buy cosmetic items there, never a gameplay advantage.
11. Some features are opened universe by universe: **expeditions** (open by default), **alliance missions** (closed by default, open on Redline) and **cosmic events** (meteorites, comet showers, giant impacts), closed by default.

### Private universes
12. You can create your own **private universe**, with its players, speeds and rules: it has an end date, and a rule change there is announced 24 hours ahead (see [Private universes](/en/misc/private-universes)). Official universes have no end date.

## Worked example

A building takes 2 hours to build on Redline, where every speed is ×1.
- In a universe whose building speed is ×2: 2 / 2 = **1 hour**.
- If only the fleet speed is ×2 there, the building still takes **2 hours**, but a 4-hour flight takes only 2, for the same amount of hydrogen.

## Detailed data

### Universe settings

{table(['Setting', 'Default', 'Redline'], rows)}

"Set at creation": the game has no default value, each universe gets its own.

## Common pitfalls

- **Nothing carries over between universes**: resources, fleets and alliances stay in their universe.
- **Check the settings**: a wiki figure marked "Universe setting" may be different in your universe. The Universes screen shows each universe's speeds, debris and moons.
- **Speeds are separate**: a universe with a fast economy can have slow fleets.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [First steps](/en/getting-started/first-steps)
- [Beginner protection](/en/players/beginner-protection)
- [Private universes](/en/misc/private-universes)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/universes', body(lang))
