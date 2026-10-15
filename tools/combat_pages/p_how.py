from combat_lib import *
from write import write, table

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    bs = stats('battleship')
    bs10 = stats('battleship', 10, 10, 10, DOCTRINE, DOCTRINE)
    lf = stats('light_fighter')
    dome = stats('protective_dome')
    sh_fr = lambda c: name(c, 'fr')
    rows = []
    for u in SHIPS + DEFENSES:
        s = stats(u[0])
        seuil = s['shield'] * BOUNCE
        rows.append([name(u[0], lang), N(s['weapon']), N(s['shield']), N(s['hull']), N(seuil) if seuil else '0'])
    rf_cs_lf = 200
    if lang == 'fr':
        hdr = ['Unité', 'Attaque', 'Bouclier', 'Coque de combat', 'Tir qui rebondit en dessous de']
        return f'''# Déroulement d'un combat

> **En bref** : un combat dure au plus {ROUNDS} rounds. À chaque round, les boucliers se rechargent, l'attaquant tire, puis le défenseur. Chaque tir vise une unité adverse au hasard et touche toujours. Un tir trop faible rebondit sur les boucliers ; les dégâts de coque, eux, restent d'un round à l'autre et peuvent faire exploser l'unité touchée.
{{.is-info}}

## Règles

### Statistiques de combat
1. Chaque unité combat avec trois valeurs : **attaque**, **bouclier** et **coque**. Elles partent des statistiques du catalogue ([vaisseaux](/fr/fleet/ships), [défenses](/fr/defense/defenses)) et montent avec trois recherches, de **10 % par niveau** : Systèmes Offensifs pour l'attaque, Champs de Protection pour le bouclier, Métallurgie Avancée pour la coque.
2. La **coque de combat** vaut le dixième de la structure.
3. Les talents d'alliance **Doctrine d'armement** et **Doctrine de protection** ajoutent chacun **{DOCTRINE} %** : le premier à l'attaque, le second au bouclier et à la coque. Ils s'appliquent après la recherche, à partir de la fin de la période d'intégration du membre.
4. Les talents de [dynastie et de classe](/fr/dynasty/talents) peuvent ajouter leurs propres pourcentages. Ils s'additionnent à la Doctrine et le total est appliqué en une fois.

$$A = \\mathrm{{arr}}\\left(A_0 (1 + 0{{,}}1\\,W)\\right) \\times \\left(1 + \\frac{{b_A}}{{100}}\\right) \\qquad B = \\mathrm{{arr}}\\left(B_0 (1 + 0{{,}}1\\,S)\\right) \\times \\left(1 + \\frac{{b_P}}{{100}}\\right) \\qquad C = \\frac{{\\mathrm{{arr}}\\left(T (1 + 0{{,}}1\\,M)\\right)}}{{10}} \\times \\left(1 + \\frac{{b_P}}{{100}}\\right)$$

- $A$, $B$, $C$ : attaque, bouclier et coque de combat ; $A_0$, $B_0$ : attaque et bouclier du catalogue ; $T$ : structure du catalogue.
- $W$, $S$, $M$ : niveaux de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée.
- $b_A$ : Doctrine d'armement plus talents d'attaque, en % ; $b_P$ : Doctrine de protection plus talents de bouclier ou de coque, en %.
- $\\mathrm{{arr}}$ : arrondi à l'entier le plus proche. La coque est arrondie à l'entier ; le dernier produit est arrondi à l'inférieur.

### Déroulement d'un round
5. Un combat compte **{ROUNDS} rounds au plus**. Il s'arrête dès qu'un camp n'a plus d'unité.
6. Au début de chaque round, **tous les boucliers se rechargent** entièrement. La **coque ne se répare pas** : les dégâts reçus au round précédent restent.
7. **L'attaquant tire, puis le défenseur.** Chaque unité vivante au début du round tire, même si elle est détruite pendant le round : en pratique, les tirs sont simultanés.
8. Chaque unité tire **un coup par round**, sur une **unité adverse tirée au hasard** parmi les unités encore vivantes, toutes catégories confondues. **Tout tir touche.**

### Tirs rapides
9. Après chaque tir, si le tireur a un [tir rapide](/fr/fleet/rapid-fire) de facteur $f$ contre l'unité qu'il vient de viser, il tire à nouveau avec une chance de $(f - 1) / f$, sur une **nouvelle cible tirée au hasard**. Il continue tant que le tirage réussit.
10. Le tir rapide donne donc des tirs en plus, il ne guide pas le tir vers les unités contrées. Contre des cibles toutes du même type, un facteur $f$ donne en moyenne $f$ tirs.
11. Dans le catalogue, seuls des vaisseaux ont des tirs rapides. Les défenses tirent une fois par round.

### Dégâts
12. **Règle du 1 %** : un tir dont les dégâts sont inférieurs à **1 % du bouclier maximal** de la cible **rebondit** sans aucun effet.
13. Sinon, le **bouclier absorbe** les dégâts tant qu'il en reste, et l'excédent passe entièrement sur la **coque**. À zéro de coque, l'unité est détruite.
14. **Explosion** : après chaque tir qui n'a pas rebondi, si la coque de la cible est **sous {P(70)}** de sa coque de combat, elle explose avec une chance égale à **1 − part de coque restante**. Un tir absorbé par le bouclier ouvre aussi ce tirage, puisque la coque était déjà entamée ; un tir qui rebondit, jamais.

### Résultat
15. **Victoire de l'attaquant** si le défenseur n'a plus d'unité ; **victoire du défenseur** si l'attaquant n'a plus d'unité ; sinon **match nul** : les deux camps encore debout après {ROUNDS} rounds, ou les deux détruits.
16. Une unité qui survit au combat **repart intacte** : les dégâts de coque ne durent que le temps du combat.
17. Les missiles du silo ne combattent pas : ce sont des munitions, tirées par une autre mission.
18. Ensuite viennent le [pillage](/fr/combat/plunder) (victoire seulement), le [champ de ruines](/fr/combat/debris) et la chance de lune, la [reconstruction des défenses](/fr/combat/defense-rebuild) et la [Station de réparation](/fr/economy/repair-station).

### Le hasard
19. Le hasard d'un combat (cibles, tirs rapides, explosions) est fixé à l'arrivée de la flotte : rejoué, le même combat donne exactement le même résultat, tir pour tir. Les tirages qui suivent (reconstruction des défenses, lune) sont eux aussi fixés par ce combat.

## Exemple chiffré

**Un Cuirassé sans recherche** : attaque {N(bs['weapon'])}, bouclier {N(bs['shield'])}, coque de combat {N(60000)} / 10 = **{N(bs['hull'])}**.

**Le même Cuirassé avec Systèmes Offensifs, Champs de Protection et Métallurgie Avancée au niveau 10, et les deux Doctrines** :
- Attaque : {N(1000)} × 2 = {N(2000)}, puis × 1,05 = **{N(bs10['weapon'])}**.
- Bouclier : {N(200)} × 2 = {N(400)}, puis × 1,05 = **{N(bs10['shield'])}**.
- Coque : {N(60000)} × 2 / 10 = {N(12000)}, puis × 1,05 = **{N(bs10['hull'])}**.

**Ce Cuirassé sans recherche tire sur un Intercepteur sans recherche** (bouclier {N(lf['shield'])}, coque {N(lf['hull'])}) : le bouclier absorbe {N(lf['shield'])}, la coque prend {N(bs['weapon'] - lf['shield'])}. L'Intercepteur est **détruit**.

**4 Intercepteurs tirent sur ce Cuirassé** (attaque {N(lf['weapon'])}) :
- Seuil du 1 % : {N(bs['shield'] * BOUNCE)}. Les tirs passent.
- Les 4 tirs ({N(4 * lf['weapon'])} au total) vident le bouclier ({N(bs['shield'])}), **sans toucher la coque**. Au round suivant, le bouclier est de nouveau plein.

**Un Intercepteur tire sur un Dôme protecteur** (bouclier {N(dome['shield'])}) : seuil du 1 % à {N(dome['shield'] * BOUNCE)}, le tir de {N(lf['weapon'])} **rebondit**. Les Intercepteurs ne peuvent rien contre le Dôme, quel que soit leur nombre.

**Une unité dont la coque est tombée à 60 %** : à chaque tir qui ne rebondit pas, elle explose avec une chance de 1 − 0,60 = **40 %**.

**Un Colossus stellaire contre une flotte d'Intercepteurs** : son tir rapide de {N(rf_cs_lf)} lui donne en moyenne {N(rf_cs_lf)} tirs par round.

## Données détaillées

Statistiques de combat sans recherche ni bonus. Chaque niveau de recherche ajoute 10 % de la valeur de base.

{table(hdr, rows)}

## Pièges fréquents

- **Les petits tirs s'écrasent sur les boucliers** : des unités faibles, même nombreuses, peuvent ne jamais entamer une grosse cible, puisque son bouclier se recharge à chaque round.
- **La cible est aléatoire** : vous ne choisissez pas ce que vos vaisseaux visent. Les unités nombreuses et bon marché absorbent beaucoup de tirs.
- **{ROUNDS} rounds, pas plus** : si personne n'est éliminé, c'est un match nul et l'attaquant ne pille rien.
- **Les blessures comptent** : une unité entamée explose plus facilement aux rounds suivants. Une rafale de petits tirs peut achever une cible déjà touchée.

## Pages liées

- [Tirs rapides](/fr/fleet/rapid-fire)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Liste des défenses](/fr/defense/defenses)
- [Pillage](/fr/combat/plunder)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Simulateur de combat](/fr/combat/simulator)
'''
    hdr = ['Unit', 'Attack', 'Shield', 'Combat hull', 'Shots bounce below']
    return f'''# How combat works

> **In short**: a battle lasts at most {ROUNDS} rounds. Each round, shields recharge, the attacker fires, then the defender. Each shot targets a random enemy unit and always hits. A shot that is too weak bounces off shields; hull damage, however, carries over from one round to the next and can make the unit hit explode.
{{.is-info}}

## Rules

### Combat stats
1. Each unit fights with three values: **attack**, **shield** and **hull**. They start from the catalogue stats ([ships](/en/fleet/ships), [defenses](/en/defense/defenses)) and grow with three research technologies, by **10% per level**: Weapon Systems for attack, Shielding Technology for shield, Armor Technology for hull.
2. The **combat hull** is one tenth of the structure.
3. The **Weapons doctrine** and **Protection doctrine** alliance talents each add **{DOCTRINE}%**: the first to attack, the second to shield and hull. They apply after research, once the member's settling-in period is over.
4. [Dynasty and class talents](/en/dynasty/talents) can add their own percentages. They add up with the doctrine and the total is applied once.

$$A = \\mathrm{{round}}\\left(A_0 (1 + 0.1\\,W)\\right) \\times \\left(1 + \\frac{{b_A}}{{100}}\\right) \\qquad B = \\mathrm{{round}}\\left(B_0 (1 + 0.1\\,S)\\right) \\times \\left(1 + \\frac{{b_P}}{{100}}\\right) \\qquad C = \\frac{{\\mathrm{{round}}\\left(T (1 + 0.1\\,M)\\right)}}{{10}} \\times \\left(1 + \\frac{{b_P}}{{100}}\\right)$$

- $A$, $B$, $C$: attack, shield and combat hull; $A_0$, $B_0$: catalogue attack and shield; $T$: catalogue structure.
- $W$, $S$, $M$: Weapon Systems, Shielding Technology and Armor Technology levels.
- $b_A$: Weapons doctrine plus attack talents, in %; $b_P$: Protection doctrine plus shield or hull talents, in %.
- $\\mathrm{{round}}$: rounded to the nearest integer. The hull is rounded to an integer; the last product is rounded down.

### How a round unfolds
5. A battle has **at most {ROUNDS} rounds**. It stops as soon as one side has no units left.
6. At the start of each round, **all shields recharge** fully. The **hull is not repaired**: damage taken in earlier rounds stays.
7. **The attacker fires, then the defender.** Every unit alive at the start of the round fires, even if it is destroyed during the round: in practice, fire is simultaneous.
8. Each unit fires **one shot per round**, at an **enemy unit picked at random** among the units still alive, all kinds together. **Every shot hits.**

### Rapid fire
9. After each shot, if the shooter has [rapid fire](/en/fleet/rapid-fire) with factor $f$ against the unit it just targeted, it fires again with a chance of $(f - 1) / f$, at a **new randomly picked target**. It keeps going as long as the roll succeeds.
10. Rapid fire therefore gives extra shots; it does not steer shots towards the units it counters. Against targets all of the same type, a factor $f$ gives $f$ shots on average.
11. In the catalogue, only ships have rapid fire. Defenses fire once per round.

### Damage
12. **1% rule**: a shot dealing less than **1% of the target's maximum shield** **bounces** with no effect at all.
13. Otherwise, the **shield absorbs** damage as long as it lasts, and the rest goes entirely to the **hull**. At zero hull, the unit is destroyed.
14. **Explosion**: after every shot that did not bounce, if the target's hull is **below {P(70)}** of its combat hull, it explodes with a chance of **1 − share of hull left**. A shot absorbed by the shield also opens this roll, since the hull was already damaged; a bounced shot never does.

### Outcome
15. **Attacker wins** if the defender has no units left; **defender wins** if the attacker has no units left; otherwise it is a **draw**: both sides still standing after {ROUNDS} rounds, or both wiped out.
16. A unit that survives the battle **leaves intact**: hull damage only lasts for the battle.
17. Silo missiles do not fight: they are ammunition, fired by another mission.
18. Then come [plunder](/en/combat/plunder) (victory only), the [debris field](/en/combat/debris) and the moon chance, the [defense rebuild](/en/combat/defense-rebuild) and the [Repair Station](/en/economy/repair-station).

### Chance
19. The chance in a battle (targets, rapid fire, explosions) is set when the fleet arrives: replayed, the same battle gives exactly the same result, shot for shot. The rolls that follow (defense rebuild, moon) are set by that battle too.

## Worked example

**A Battleship with no research**: attack {N(bs['weapon'])}, shield {N(bs['shield'])}, combat hull {N(60000)} / 10 = **{N(bs['hull'])}**.

**The same Battleship with Weapon Systems, Shielding Technology and Armor Technology at level 10, and both doctrines**:
- Attack: {N(1000)} × 2 = {N(2000)}, then × 1.05 = **{N(bs10['weapon'])}**.
- Shield: {N(200)} × 2 = {N(400)}, then × 1.05 = **{N(bs10['shield'])}**.
- Hull: {N(60000)} × 2 / 10 = {N(12000)}, then × 1.05 = **{N(bs10['hull'])}**.

**This Battleship with no research fires at an Interceptor with no research** (shield {N(lf['shield'])}, hull {N(lf['hull'])}): the shield absorbs {N(lf['shield'])}, the hull takes {N(bs['weapon'] - lf['shield'])}. The Interceptor is **destroyed**.

**4 Interceptors fire at this Battleship** (attack {N(lf['weapon'])}):
- 1% threshold: {N(bs['shield'] * BOUNCE)}. The shots go through.
- The 4 shots ({N(4 * lf['weapon'])} in total) empty the shield ({N(bs['shield'])}), **without touching the hull**. Next round, the shield is full again.

**An Interceptor fires at a Protective Dome** (shield {N(dome['shield'])}): the 1% threshold is {N(dome['shield'] * BOUNCE)}, the {N(lf['weapon'])} shot **bounces**. Interceptors can do nothing against the Dome, however many there are.

**A unit whose hull has dropped to 60%**: on every shot that does not bounce, it explodes with a chance of 1 − 0.60 = **40%**.

**A Stellar Colossus against a fleet of Interceptors**: its rapid fire of {N(rf_cs_lf)} gives it {N(rf_cs_lf)} shots per round on average.

## Detailed data

Combat stats with no research and no bonus. Each research level adds 10% of the base value. Ship names are provisional translations: the game still shows the French names.

{table(hdr, rows)}

## Common pitfalls

- **Small shots crash on shields**: weak units, even in numbers, may never scratch a big target, since its shield recharges every round.
- **Targets are random**: you do not choose what your ships aim at. Numerous, cheap units soak up many shots.
- **{ROUNDS} rounds, no more**: if nobody is wiped out, it is a draw and the attacker plunders nothing.
- **Wounds matter**: a damaged unit explodes more easily in later rounds. A burst of small shots can finish off a target that is already hit.

## Related pages

- [Rapid fire](/en/fleet/rapid-fire)
- [Ship list](/en/fleet/ships)
- [Defense list](/en/defense/defenses)
- [Plunder](/en/combat/plunder)
- [Reading a battle report](/en/combat/battle-report)
- [Battle simulator](/en/combat/simulator)
'''

def run():
    write('fr', 'combat/how-combat-works', body('fr'))
    write('en', 'combat/how-combat-works', body('en'))
