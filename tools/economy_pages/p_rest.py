import sys; sys.path.insert(0, sys.argv[1])
from econ_lib import *; from write import *
def N(x, l): return n(x, l)
# ---------- build-queue
def bq(l):
    if l == 'fr': return '''# Files de construction

> **En bref** : chaque planète a quatre files : bâtiments, recherche, vaisseaux et défenses. Chaque file accepte 2 ordres (5 en Premium), celui en cours compris. La recherche n'avance qu'une étude à la fois pour tout votre empire. Un bâtiment ou une recherche n'est payé qu'au moment où il démarre ; s'il ne peut pas être payé, il est abandonné sans frais.
{.is-info}

> **Paramètre d'univers** : la taille des files peut être différente selon l'univers.
> Par défaut : **2 ordres**, **5 en Premium** · Redline : **2 ordres**, **5 en Premium**
{.is-info}

## Règles

1. Quatre files par planète : **bâtiments**, **recherche**, **vaisseaux**, **défenses**. Chacune accepte **2 ordres**, celui en cours compris, ou **5 en Premium**.
2. **Recherche** : les études passent **une à la fois pour tout votre empire**. Chaque planète garde sa propre file, mais une étude placée sur une colonie attend que celle en cours sur une autre planète soit terminée, dans l'ordre où vous les avez placées. Le talent [Second laboratoire](/fr/dynasty/common-tree) permet d'en mener deux.
3. Un **bâtiment** ou une **recherche** est **payé au lancement**, pas à la mise en file. Si, au moment de démarrer, la planète n'a pas les ressources, l'ordre est **abandonné sans frais**. Les prérequis, eux, sont vérifiés dès la mise en file, aux niveaux qu'auront vos bâtiments et recherches une fois les ordres précédents terminés.
4. Une commande de **vaisseaux** ou de **défenses** n'est acceptée que si la planète peut la payer en entier au moment où vous la passez. Les unités sont ensuite payées **une par une**, au moment où chacune entre en production ; si la planète ne peut plus payer l'unité suivante, la commande s'arrête là et les unités déjà construites sont gardées.
5. Commander le même vaisseau ou la même défense que la dernière commande en attente l'ajoute à cette commande, sans prendre de place dans la file.
6. Les ordres en attente affichent une **durée estimée**, recalculée au lancement.
7. Une amélioration ne peut pas attendre derrière une démolition du même bâtiment, ni une démolition derrière son amélioration.
8. Pendant que le **Dock orbital** produit des unités, il ne peut être ni amélioré ni démoli ; pendant qu'il est en travaux, aucun vaisseau ni aucune défense ne peut y être commandé. Pendant que le **Centre d'innovation** d'une planète est en travaux, aucune recherche ne peut être lancée ni ajoutée depuis cette planète ; et tant qu'une recherche lancée depuis une planète est en cours, son Centre d'innovation ne peut pas être amélioré.

### Annulation
9. Annuler un ordre **encore en attente** ne coûte rien et ne rend rien : il n'a pas été payé.
10. Annuler un **bâtiment ou une recherche en cours** rend **80 % du coût × (temps restant / durée totale)**, arrondi à l'inférieur pour chaque ressource. Le trait de dynastie [Rien ne se perd](/fr/dynasty/dynasties) porte ce taux à 85 %.
11. Annuler une commande de **vaisseaux ou de défenses** rend 80 % de l'unité payée mais pas encore livrée, sans prorata de temps. Les unités déjà livrées sont conservées.
12. Annuler une **démolition** ne rend rien : elle n'a rien coûté.
13. L'**énergie requise** n'est jamais remboursée : elle n'est pas dépensée.

## Exemple chiffré

Vous annulez un bâtiment qui coûtait 20 000 métal et 10 000 cristal, alors que 25 % de son temps est écoulé.
- Temps restant : 75 %.
- Remboursement : 80 % × 75 % = **60 %**, soit **12 000 métal et 6 000 cristal**.
- Vous perdez 8 000 métal et 4 000 cristal : annuler tôt coûte déjà 20 %.

## Pièges fréquents

- **Une annulation n'est jamais gratuite** : même juste après le lancement, vous perdez au moins 20 %.
- **Gardez les ressources pour l'ordre suivant** : un bâtiment ou une recherche qui ne peut pas être payé à son tour est abandonné, une commande d'unités s'arrête.
- **Une recherche à la fois pour tout l'empire** : une colonie ne fait pas avancer une deuxième étude en parallèle.
- **Le Premium allonge les quatre files** : bâtiments, recherche, vaisseaux et défenses passent tous à 5 ordres.

## Pages liées

- [Liste des bâtiments](/fr/economy/buildings)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Formules de l'économie](/fr/economy/formulas)
- [Premium, boutique et Points stellaires](/fr/misc/premium)
'''
    return '''# Build queues

> **In short**: each planet has four queues: buildings, research, ships and defenses. Each queue takes 2 orders (5 with Premium), the running one included. Research only moves one study at a time across your whole empire. A building or a research is paid only when it starts; if it cannot be paid then, it is dropped at no cost.
{.is-info}

> **Universe setting**: queue size may differ from one universe to another.
> Default: **2 orders**, **5 with Premium** · Redline: **2 orders**, **5 with Premium**
{.is-info}

## Rules

1. Four queues per planet: **buildings**, **research**, **ships**, **defenses**. Each takes **2 orders**, the running one included, or **5 with Premium**.
2. **Research**: studies run **one at a time across your whole empire**. Each planet keeps its own queue, but a study placed on a colony waits until the one running on another planet is finished, in the order you placed them. The [Second Laboratory](/en/dynasty/common-tree) talent lets you run two.
3. A **building** or a **research** is **paid when it starts**, not when queued. If the planet cannot afford it when it is due to start, the order is **dropped at no cost**. Requirements, though, are checked when you queue, at the levels your buildings and research will have once the orders ahead are done.
4. A **ship** or **defense** order is only accepted if the planet can pay for all of it when you place it. Units are then paid **one at a time**, as each one goes into production; if the planet can no longer pay for the next unit, the order stops there and the units already built are kept.
5. Ordering the same ship or defense as the last waiting order adds to that order, without taking a queue slot.
6. Waiting orders show an **estimated duration**, recalculated when they start.
7. An upgrade cannot wait behind a demolition of the same building, nor a demolition behind its upgrade.
8. While the **Orbital Dock** is producing units, it can be neither upgraded nor demolished; while it is under work, no ship or defense can be ordered there. While a planet's **Innovation Center** is under work, no research can be started or queued from that planet; and while a research started from a planet is running, its Innovation Center cannot be upgraded.

### Cancelling
9. Cancelling an order **still waiting** costs nothing and refunds nothing: it has not been paid.
10. Cancelling a **running building or research** refunds **80% of the cost × (remaining time / total time)**, rounded down for each resource. The [Nothing Is Lost](/en/dynasty/dynasties) dynasty trait raises this rate to 85%.
11. Cancelling a **ship or defense order** refunds 80% of the unit paid but not yet delivered, with no time proration. Units already delivered are kept.
12. Cancelling a **demolition** refunds nothing: it cost nothing.
13. **Required energy** is never refunded: it is not spent.

## Worked example

You cancel a building that cost 20,000 metal and 10,000 crystal, with 25% of its time elapsed.
- Remaining time: 75%.
- Refund: 80% × 75% = **60%**, so **12,000 metal and 6,000 crystal**.
- You lose 8,000 metal and 4,000 crystal: cancelling early already costs 20%.

## Common pitfalls

- **Cancelling is never free**: even right after the start, you lose at least 20%.
- **Keep resources for the next order**: a building or research that cannot be paid on its turn is dropped, a unit order stops.
- **One research at a time for the whole empire**: a colony does not run a second study alongside.
- **Premium lengthens all four queues**: buildings, research, ships and defenses all go to 5 orders.

## Related pages

- [Buildings list](/en/economy/buildings)
- [Demolishing a building](/en/economy/demolition)
- [Economy formulas](/en/economy/formulas)
- [Premium, shop and Stellar Points](/en/misc/premium)
'''
# ---------- demolition
t = btime(sum(cost((60,15,0),1.5,14)), robo=4)
def dm(l):
    if l == 'fr': return f'''# Démolir un bâtiment

> **En bref** : vous pouvez démolir un niveau de vos bâtiments pour libérer une case. La démolition est gratuite, dure la moitié du temps de construction de ce niveau, ne rend aucune ressource et retire les points correspondants.
{{.is-info}}

## Règles

1. Démolir fait **redescendre le bâtiment d'un niveau** et **libère une case**.
2. La démolition **ne coûte rien et ne rend rien**, ni au lancement ni à la fin ; l'annuler ne rend rien non plus.
3. Elle **retire les points** du niveau démoli.
4. Sa durée vaut **la moitié du temps de construction** du niveau retiré, avec la Fabrique d'automates, l'Assembleur moléculaire et la vitesse de construction de l'univers, mais **sans les bonus de vitesse** d'alliance ou de talents.
5. Impossible de démolir la **Base planetaire**, la **Base lunaire** ou un bâtiment au **niveau 0**.
6. Une démolition passe par la file des bâtiments et y prend une place. Elle ne peut pas attendre derrière une amélioration du même bâtiment, ni l'inverse.
7. Le **Dock orbital** ne peut pas être démoli pendant qu'il produit des unités.
8. Démolir l'**Arsenal balistique** ne détruit aucun missile : ceux qui sont stockés restent.

## Exemple chiffré

Sur une planète avec Fabrique d'automates 4, construire l'Excavateur minéral niveau 14 prend **{N(t,"fr")} secondes** (1 h 10 min).
- Démolir ce niveau 14 prend la moitié : **{N(round(t/2),"fr")} secondes** (35 min).
- Vous récupérez 1 case, perdez 14,6 points d'économie et ne récupérez aucune ressource.

## Pièges fréquents

- **Aucun remboursement** : démolir n'est utile que pour libérer de la place, jamais pour récupérer des ressources.
- **Vos points baissent** : une démolition peut vous faire changer de palier de protection.
- **La démolition occupe la file** : pendant ce temps, vous ne construisez rien d'autre sur cette planète si la file est pleine.

## Pages liées

- [Liste des bâtiments](/fr/economy/buildings)
- [Files de construction](/fr/economy/build-queue)
- [Planètes : taille, température, type](/fr/universe/planets)
'''
    return f'''# Demolishing a building

> **In short**: you can demolish one level of a building to free a field. Demolition is free, takes half the construction time of that level, refunds no resources and removes the matching points.
{{.is-info}}

## Rules

1. Demolishing **brings the building down one level** and **frees a field**.
2. Demolition **costs nothing and refunds nothing**, neither at the start nor at the end; cancelling it refunds nothing either.
3. It **removes the points** of the demolished level.
4. It takes **half the construction time** of the level removed, with the Automaton Factory, the Molecular Assembler and the universe's construction speed, but **without** alliance or talent **speed bonuses**.
5. You cannot demolish the **Planetary Base**, the **Lunar base** or a building at **level 0**.
6. A demolition goes through the buildings queue and takes a slot in it. It cannot wait behind an upgrade of the same building, nor the other way round.
7. The **Orbital Dock** cannot be demolished while it is producing units.
8. Demolishing the **Ballistic Arsenal** destroys no missile: the ones in stock stay.

## Worked example

On a planet with Automaton Factory 4, building the Mineral Excavator level 14 takes **{N(t,"en")} seconds** (1 h 10 min).
- Demolishing that level 14 takes half: **{N(round(t/2),"en")} seconds** (35 min).
- You get 1 field back, lose 14.6 economy points and recover no resources.

## Common pitfalls

- **No refund**: demolishing is only useful to free space, never to get resources back.
- **Your points drop**: a demolition can move you to another protection tier.
- **Demolition uses the queue**: meanwhile, you build nothing else on that planet if the queue is full.

## Related pages

- [Buildings list](/en/economy/buildings)
- [Build queues](/en/economy/build-queue)
- [Planets: size, temperature, type](/en/universe/planets)
'''
# ---------- repair station
share = [round(f*0.7*100,2) for f in REPAIR]
dur = math.ceil(35*4000/(10*4))
def rs(l):
    S = ' | '.join((f'{s:g}'.replace('.', ',') + ' %') if l=='fr' else f'{s:g}%' for s in share)
    hdr = ' | '.join(str(i) for i in range(1,11))
    if l == 'fr': return f'''# Station de réparation

> **En bref** : après un combat où votre planète a perdu des vaisseaux en défense, la Station de réparation en récupère une partie et vous les rend réparés, au bout de 30 minutes à 12 heures. La part récupérée augmente avec son niveau. Elle n'occupe aucune case.
{{.is-info}}

> **Paramètre d'univers** : la part récupérée dépend du taux de débris de l'univers, et la durée de réparation de sa vitesse de chantier.
> Par défaut : débris **30 %**, chantier **×1** · Redline : débris **30 %**, chantier **×1**
{{.is-info}}

<img src="/images/illustrations/facilities/station-de-reparation.jpg" width="180" alt="Station de réparation">

## Règles

1. La Station intervient après **tout combat où votre planète défend et perd des vaisseaux**, que vous gagniez ou perdiez le combat.
2. Elle récupère une part des vaisseaux détruits : **part = coefficient du niveau × (1 − taux de débris)**. Le coefficient va de 45 % au niveau 1 à 54 % au niveau 10 ; certains talents l'augmentent.
3. La part s'applique **à chaque type de vaisseau séparément**, arrondie à l'inférieur : quelques pertes peuvent ne rien rapporter.
4. **Il n'y a pas de tirage** : la part est fixe.
5. **Durée** : la Station répare **10 points de structure par seconde et par niveau**, multipliés par la vitesse de chantier de l'univers. La durée est comprise entre **30 minutes et 12 heures**. Tous les vaisseaux d'un même combat reviennent en même temps.
6. Pendant la réparation, les vaisseaux sont **hors de la planète** : ils ne défendent pas, ne peuvent être ni détruits ni pillés, et ne comptent ni dans vos flottes ni dans vos points. Ils reviennent intacts.
7. Une réparation **ne peut pas être annulée**.
8. Les vaisseaux récupérés apparaissent dans les **pertes** du rapport de combat, avec une mention.
9. La Station **n'occupe aucune case** et ne consomme pas d'énergie en fonctionnement ; l'énergie n'est qu'un seuil requis pour la construire.
10. Les **défenses** ne sont pas concernées : elles ont leur propre reconstruction (voir [Reconstruction des défenses](/fr/combat/defense-rebuild)).

## Exemple chiffré

Vous perdez **100 Intercepteurs** en défense, avec une Station de réparation niveau 4, sur Redline :
- Part récupérée : 50 % × (1 − 30 %) = **35 %**, soit **35 Intercepteurs**.
- Structure à réparer : 35 × 4 000 = 140 000. Vitesse : 10 × 4 = 40 par seconde, soit {N(dur,"fr")} secondes : environ **58 minutes**.
- Si vous n'aviez perdu que 2 Intercepteurs : 35 % de 2 = 0,7, arrondi à **0** : rien n'est récupéré.

## Données détaillées

| Niveau | {hdr} |
|---|---|---|---|---|---|---|---|---|---|---|
| Coefficient | 45 % | 48 % | 49 % | 50 % | 51 % | 52 % | 53 % | 53 % | 54 % | 54 % |
| Part récupérée (débris 30 %) | {S} |

Prérequis : Dock orbital 2. Coût du niveau 1 : 200 métal, 50 hydrogène, 50 énergie requise ; le coût est multiplié par 5 à chaque niveau, l'énergie requise par 2,5.

## Pièges fréquents

- **Les petites pertes ne rapportent rien** : l'arrondi se fait par type de vaisseau.
- **Les vaisseaux en réparation ne vous défendent pas** : une nouvelle attaque pendant ce temps trouve une orbite plus vide.
- **Le coût grimpe très vite** : ×5 par niveau.

## Pages liées

- [Liste des vaisseaux](/fr/fleet/ships)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Champs de ruines](/fr/combat/debris)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
'''
    return f'''# Repair Station

> **In short**: after a battle in which your planet lost ships in defense, the Repair Station recovers part of them and gives them back repaired, after 30 minutes to 12 hours. The recovered share grows with its level. It takes no field.
{{.is-info}}

> **Universe setting**: the recovered share depends on the universe's debris rate, and repair time on its shipyard speed.
> Default: debris **30%**, shipyard **×1** · Redline: debris **30%**, shipyard **×1**
{{.is-info}}

<img src="/images/illustrations/facilities/station-de-reparation.jpg" width="180" alt="Repair Station">

## Rules

1. The Station steps in after **any battle in which your planet defends and loses ships**, whether you win or lose the battle.
2. It recovers part of the destroyed ships: **share = level coefficient × (1 − debris rate)**. The coefficient goes from 45% at level 1 to 54% at level 10; some talents raise it.
3. The share applies **to each ship type separately**, rounded down: a few losses may recover nothing.
4. **There is no roll**: the share is fixed.
5. **Time**: the Station repairs **10 structure points per second per level**, multiplied by the universe's shipyard speed. The time is between **30 minutes and 12 hours**. All ships from one battle come back together.
6. During the repair, the ships are **off the planet**: they do not defend, cannot be destroyed or plundered, and count neither in your fleets nor in your points. They come back intact.
7. A repair **cannot be cancelled**.
8. Recovered ships appear in the battle report's **losses**, with a note.
9. The Station **takes no field** and uses no energy while running; energy is only a threshold to build it.
10. **Defenses** are not concerned: they have their own rebuild (see [Defense rebuild](/en/combat/defense-rebuild)).

## Worked example

You lose **100 Interceptors** in defense, with a Repair Station level 4, on Redline:
- Recovered share: 50% × (1 − 30%) = **35%**, so **35 Interceptors**.
- Structure to repair: 35 × 4,000 = 140,000. Speed: 10 × 4 = 40 per second, so {N(dur,"en")} seconds: about **58 minutes**.
- Had you lost only 2 Interceptors: 35% of 2 = 0.7, rounded to **0**: nothing is recovered.

## Detailed data

| Level | {hdr} |
|---|---|---|---|---|---|---|---|---|---|---|
| Coefficient | 45% | 48% | 49% | 50% | 51% | 52% | 53% | 53% | 54% | 54% |
| Recovered share (debris 30%) | {S} |

Requirement: Orbital Dock 2. Level 1 cost: 200 metal, 50 hydrogen, 50 required energy; the cost is multiplied by 5 at each level, the required energy by 2.5.

## Common pitfalls

- **Small losses recover nothing**: rounding is done per ship type.
- **Ships under repair do not defend you**: a new attack meanwhile finds an emptier orbit.
- **The cost climbs very fast**: ×5 per level.

## Related pages

- [Ships list](/en/fleet/ships)
- [Reading a battle report](/en/combat/battle-report)
- [Debris fields](/en/combat/debris)
- [Defense rebuild](/en/combat/defense-rebuild)
'''
for l in ('fr','en'):
    write(l, 'economy/build-queue', bq(l)); write(l, 'economy/demolition', dm(l)); write(l, 'economy/repair-station', rs(l))
