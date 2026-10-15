import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    t4 = build_time('small_cargo', 4)
    t7 = build_time('small_cargo', 7, 1)
    rows = []
    for s in SHIPS:
        nm = s[1] if fr else f'*{s[2]}*'
        rows.append([nm, N(s[13]), N(build_time(s[0], 4)), N(build_time(s[0], 8)), N(build_time(s[0], 12)), N(build_time(s[0], 12, 2))])
    hdr = (['Vaisseau', 'Durée de base (s)', 'Dock 4', 'Dock 8', 'Dock 12', 'Dock 12 et Assembleur 2'] if fr
           else ['Ship', 'Base time (s)', 'Dock 4', 'Dock 8', 'Dock 12', 'Dock 12 and Assembler 2'])
    T = table(hdr, rows)
    refund = (fl(0.8 * 2000), fl(0.8 * 2000))
    if fr:
        return f'''# Dock orbital (chantier)

> **En bref** : le Dock orbital construit les vaisseaux et les défenses. Chaque niveau accélère la production, l'Assembleur moléculaire la divise par deux à chaque niveau. Une commande est vérifiée en entier quand vous la passez, puis chaque unité est payée au moment où elle entre en production et livrée dès qu'elle est terminée.
{{.is-info}}

> **Paramètre d'univers** : la vitesse de chantier divise la durée de construction des vaisseaux et des défenses.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

> **Paramètre d'univers** : la taille des files de construction peut être différente selon l'univers.
> Par défaut : **2 ordres**, **5 en Premium** · Redline : **2 ordres**, **5 en Premium**
{{.is-info}}

<img src="/images/illustrations/facilities/dock-orbital.jpg" width="180" alt="Dock orbital">

## Règles

### Le bâtiment
1. Le Dock orbital se construit sur une planète **ou une lune**. Prérequis : Fabrique d'automates 2. Niveau maximum : **12**. Il faut au moins le niveau 1 pour commander un vaisseau ou une défense, en plus des prérequis propres à chaque unité.
2. Sur une lune, le Dock travaille sans Assembleur moléculaire, qui ne se construit que sur une planète.

### Les files
3. Chaque base a **une file de vaisseaux et une file de défenses**, qui avancent **en parallèle**. Chacune accepte 2 ordres (5 en Premium), celui en cours compris (voir [Files de construction](/fr/economy/build-queue)).
4. Commander le même vaisseau ou la même défense que le **dernier ordre en attente** l'ajoute à cet ordre, sans prendre de place dans la file. La Barrière défensive et le Dôme protecteur, uniques, ne se fusionnent jamais.
5. Une commande compte au moins 1 unité et au plus **1 000 000**.

### Paiement et livraison
6. Une commande n'est acceptée que si la base peut la **payer en entier** au moment où vous la passez.
7. Chaque unité est ensuite **payée au moment où elle entre en production**, pas avant. Si la première ne peut pas être payée au lancement, l'ordre est abandonné sans frais.
8. Les unités sont **livrées une par une**, chacune dès qu'elle est terminée, et rapportent aussitôt leurs points militaires.
9. Après chaque livraison, l'unité suivante est payée. Si la base ne peut plus la payer, la commande **s'arrête là** : les unités déjà livrées sont gardées, les autres ne coûtent rien.
10. **Durée d'une unité**, en secondes, jamais moins d'une seconde :

$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v$$

- $t$ : durée de construction d'une unité, arrondie à la seconde ;
- $T$ : durée de base de l'unité (table plus bas, et [Liste des défenses](/fr/defense/defenses)) ;
- $D$ : niveau du Dock orbital de la base ;
- $A$ : niveau de l'Assembleur moléculaire de la base ;
- $v$ : vitesse de chantier de l'univers.

Les bonus de vitesse des talents divisent ensuite cette durée, comme pour les bâtiments (voir [Formules de l'économie](/fr/economy/formulas)). La durée d'une unité est fixée quand la commande démarre ; la commande dure cette durée × le nombre d'unités.

### Annuler
11. Annuler un ordre **en attente** ne coûte rien et ne rend rien.
12. Annuler une commande **en cours** rend **80 %** de l'unité payée mais pas encore livrée ; les unités livrées sont gardées, les suivantes ne coûtent rien. Des talents montent ce taux, jusqu'à 95 %.
13. Vous pouvez aussi demander d'**arrêter après l'unité en cours** : elle se termine normalement, le reste de la commande est abandonné sans frais.

### Pendant les travaux
14. Tant que le Dock a une commande de vaisseaux ou de défenses, en attente ou en cours, il ne peut être **ni amélioré ni démoli**.
15. Pendant que le Dock est en travaux, aucun vaisseau ni aucune défense ne peut y être commandé. Les autres bâtiments se construisent normalement.

## Exemple chiffré

**Une Navette de fret** (durée de base 5 400 s) :
- Dock orbital 4, sans Assembleur : 5 400 / 5 = **{N(t4)} s** (18 min).
- Dock orbital 7 et Assembleur moléculaire 1 : 5 400 / (8 × 2) = 337,5, arrondi à **{N(t7)} s**. Dix Navettes : {N(10 * t7)} s ({hms(10 * t7, lang)}).

**Annulation** : vous commandez 10 Navettes de fret et annulez après la 3e livraison. La 4e est en production et payée : vous récupérez 80 % de son coût, soit **{N(refund[0])} métal et {N(refund[1])} cristal**. Les 3 Navettes livrées restent, les 6 suivantes n'ont rien coûté.

## Données détaillées

### Durée d'un vaisseau selon le Dock orbital (en secondes, vitesse ×1, sans talent)

{T}

Le Dock orbital lui-même : coût du niveau 1 de 400 métal, 200 cristal et 100 hydrogène, doublé à chaque niveau (voir [Liste des bâtiments](/fr/economy/buildings)).

## Pièges fréquents

- **Gardez les ressources pour la suite** : une commande longue s'arrête dès qu'une unité ne peut plus être payée.
- **Les files ne se partagent pas** : vaisseaux et défenses avancent en même temps, mais chaque file est limitée à 2 ordres (5 en Premium).
- **Ne lancez pas l'amélioration du Dock en pleine production** : elle est refusée tant qu'une commande attend ou tourne.
- **Une lune construit plus lentement** : pas d'Assembleur moléculaire sur une lune.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Files de construction](/fr/economy/build-queue)
- [Formules de l'économie](/fr/economy/formulas)
- [Station de réparation](/fr/economy/repair-station)
- [Liste des bâtiments](/fr/economy/buildings)
'''
    return f'''# Orbital Dock (shipyard)

> **In short**: the Orbital Dock builds ships and defenses. Each level speeds production up, and the Molecular Assembler halves it at each level. An order is checked in full when you place it, then each unit is paid when it enters production and delivered as soon as it is done.
{{.is-info}}

> Ships are not translated in the game yet: it shows their French name in every language. The English names used here are provisional (see [Ships list](/en/fleet/ships)).
{{.is-warning}}

> **Universe setting**: the shipyard speed divides ship and defense build times.
> Default: **×1** · Redline: **×1**
{{.is-info}}

> **Universe setting**: the size of build queues may differ from one universe to another.
> Default: **2 orders**, **5 with Premium** · Redline: **2 orders**, **5 with Premium**
{{.is-info}}

<img src="/images/illustrations/facilities/dock-orbital.jpg" width="180" alt="Orbital Dock">

## Rules

### The building
1. The Orbital Dock is built on a planet **or a moon**. Requirement: Automaton Factory 2. Maximum level: **12**. You need at least level 1 to order a ship or a defense, on top of each unit's own requirements.
2. On a moon the Dock works without a Molecular Assembler, which can only be built on a planet.

### Queues
3. Each base has **a ship queue and a defense queue**, which run **side by side**. Each takes 2 orders (5 with Premium), the running one included (see [Build queues](/en/economy/build-queue)).
4. Ordering the same ship or defense as the **last waiting order** adds to that order, without taking a queue slot. The Defensive Barrier and the Protective Dome, which are unique, never merge.
5. An order holds at least 1 unit and at most **1,000,000**.

### Payment and delivery
6. An order is only accepted if the base can **pay for all of it** when you place it.
7. Each unit is then **paid when it enters production**, not before. If the first one cannot be paid at start, the order is dropped at no cost.
8. Units are **delivered one by one**, each as soon as it is done, and bring their military points at once.
9. After each delivery the next unit is paid. If the base can no longer pay for it, the order **stops there**: delivered units are kept, the others cost nothing.
10. **Time per unit**, in seconds, never under one second:

$$t = \\frac{{T}}{{(1 + D) \\times 2^{{A}}}} \\div v$$

- $t$: build time of one unit, rounded to the second;
- $T$: the unit's base time (table below, and [Defenses list](/en/defense/defenses));
- $D$: the base's Orbital Dock level;
- $A$: the base's Molecular Assembler level;
- $v$: the universe's shipyard speed.

Talent speed bonuses then divide this time, as for buildings (see [Economy formulas](/en/economy/formulas)). The time per unit is set when the order starts; the order lasts that time × the number of units.

### Cancelling
11. Cancelling a **waiting** order costs nothing and refunds nothing.
12. Cancelling a **running** order refunds **80%** of the unit paid but not yet delivered; delivered units are kept, the next ones cost nothing. Talents raise this rate, up to 95%.
13. You can also ask to **stop after the current unit**: it finishes as usual, the rest of the order is dropped at no cost.

### While building
14. As long as the Dock has a ship or defense order, waiting or running, it can be **neither upgraded nor demolished**.
15. While the Dock is being upgraded, no ship or defense can be ordered there. Other buildings go up as usual.

## Worked example

**A Cargo Shuttle** (base time 5,400 s):
- Orbital Dock 4, no Assembler: 5,400 / 5 = **{N(t4)} s** (18 min).
- Orbital Dock 7 and Molecular Assembler 1: 5,400 / (8 × 2) = 337.5, rounded to **{N(t7)} s**. Ten Shuttles: {N(10 * t7)} s ({hms(10 * t7, lang)}).

**Cancelling**: you order 10 Cargo Shuttles and cancel after the 3rd delivery. The 4th is in production and paid: you get back 80% of its cost, so **{N(refund[0])} metal and {N(refund[1])} crystal**. The 3 delivered Shuttles stay, the next 6 cost nothing.

## Detailed data

### Ship build time by Orbital Dock level (seconds, speed ×1, no talent)

{T}

The Orbital Dock itself: level 1 costs 400 metal, 200 crystal and 100 hydrogen, doubled at each level (see [Buildings list](/en/economy/buildings)).

## Common pitfalls

- **Keep resources for what comes next**: a long order stops as soon as a unit can no longer be paid.
- **Queues are not shared**: ships and defenses progress at the same time, but each queue is capped at 2 orders (5 with Premium).
- **Do not upgrade the Dock mid-production**: it is refused while an order waits or runs.
- **A moon builds slower**: there is no Molecular Assembler on a moon.

## Related pages

- [Ships list](/en/fleet/ships)
- [Defenses list](/en/defense/defenses)
- [Build queues](/en/economy/build-queue)
- [Economy formulas](/en/economy/formulas)
- [Repair Station](/en/economy/repair-station)
- [Buildings list](/en/economy/buildings)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/orbital-dock', body(lang),
          description=('Construire vaisseaux et défenses : files, paiement, livraison, durées.' if lang == 'fr' else 'Building ships and defenses: queues, payment, delivery, build times.'))
