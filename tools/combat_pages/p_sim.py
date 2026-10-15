from combat_lib import *
from write import write

def body(lang):
    N = lambda x: n(x, lang)
    ok_side = SIM_DEPLOY // SIM_FRONT_ITER // 2
    too_side = 150_000
    if lang == 'fr':
        return f'''# Simulateur de combat

> **En bref** : le simulateur rejoue un combat avec le vrai moteur du jeu avant que vous l'engagiez. Aucune flotte n'est envoyée, aucune ressource dépensée. Vous partez d'un rapport d'espionnage ou saisissez le défenseur à la main ; le simulateur livre des taux de victoire, des pertes moyennes et le champ de ruines d'un combat moyen.
{{.is-info}}

## Règles

### Le défenseur
1. Deux modes : **Depuis un rapport d'espionnage** ou **Saisie manuelle**. Un rapport partagé dans votre alliance peut aussi servir.
2. Depuis un rapport, chaque partie du défenseur compte comme **vue** seulement si l'espionnage a atteint son palier. Le simulateur indique ce qu'il a supposé et la date du rapport.
3. Un rapport qui **n'a pas vu la flotte** est refusé : il n'y a rien à simuler.
4. Des **défenses non vues** sont supposées **absentes** : le taux de victoire affiché est alors un plancher optimiste. Saisissez une estimation si vous en avez une.
5. Des **recherches non vues** sont supposées **égales aux vôtres**, sans vos talents.
6. Modifier une valeur importée fait passer la simulation en **saisie manuelle** : le rapport n'est plus utilisé.
7. Le défenseur combat **sans talents ni bonus de dynastie** : ils ne sont jamais révélés.
8. Les missiles du silo ne combattent jamais : ils ne figurent pas dans le simulateur.

### Votre camp
9. Votre flotte combat avec vos recherches, votre dynastie et vos talents, comme dans un vrai combat.
10. Vous pouvez saisir plus de vaisseaux que vous n'en possédez : le simulateur sert aussi à décider quoi construire.
11. Pour simuler d'autres niveaux de Systèmes Offensifs, Champs de Protection ou Métallurgie Avancée, remplissez les **trois** champs de recherche.

### Le résultat
12. Chaque simulation rejoue le combat **{SIM_FRONT_ITER} fois** et donne les **taux de victoire** de l'attaquant et du défenseur et le taux de match nul, le nombre moyen de rounds, les **pertes** et **survivants** moyens, arrondis à l'unité.
13. Le **détail round par round** est celui d'un seul des {SIM_FRONT_ITER} combats, à titre d'exemple : il n'illustre pas la série.
14. Le **champ de ruines** est celui d'un combat moyen, débris des deux camps, au taux de débris de votre univers.
15. Certains talents ajoutent un **Butin prévu** (ce qu'une victoire rapporterait au plus, d'après le stock lu par le rapport et les soutes des survivants) ou un **Bilan de chasse**.

### Les limites
16. Une simulation est refusée au-delà de **{N(SIM_UNITS)} unités par camp**, de **{SIM_ITER} combats**, ou de **{N(SIM_DEPLOY)} déploiements** (unités des deux camps × nombre de combats).

## Exemple chiffré

**Rapport incomplet** : votre rapport a vu la flotte, mais ni les défenses ni les recherches. Le simulateur suppose zéro défense et des technologies égales aux vôtres. Si la cible a en réalité 20 Batteries ioniques, votre vraie chance de victoire sera **plus faible** que celle affichée.

**Limite de taille** : avec {SIM_FRONT_ITER} combats par simulation, la limite de {N(SIM_DEPLOY)} déploiements autorise {N(SIM_DEPLOY // SIM_FRONT_ITER)} unités en tout, par exemple {N(ok_side)} de chaque côté. Avec {N(too_side)} unités de chaque côté, ({N(too_side)} + {N(too_side)}) × {SIM_FRONT_ITER} = {N(2 * too_side * SIM_FRONT_ITER)} : la simulation est refusée.

## Pièges fréquents

- **Un rapport incomplet rend le simulateur optimiste** : complétez les catégories manquantes avant de vous fier au résultat.
- **Un vieux rapport ment** : une planète change vite, refaites un espionnage avant d'engager.
- **Le défenseur peut être plus fort que prévu** : ses talents ne sont pas simulés.
- **Les technologies comptent** : si vous connaissez celles de la cible, saisissez-les.

## Pages liées

- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Champs de ruines](/fr/combat/debris)
- [Pillage](/fr/combat/plunder)
'''
    return f'''# Battle simulator

> **In short**: the simulator replays a battle with the game's real engine before you commit to it. No fleet is sent, no resource is spent. You start from a spy report or type in the defender by hand; the simulator gives victory rates, average losses and the debris field of an average battle.
{{.is-info}}

## Rules

### The defender
1. Two modes: **From a spy report** or **Manual entry**. A report shared with your alliance can be used too.
2. From a report, each part of the defender counts as **seen** only if the espionage reached its tier. The simulator says what it assumed and how old the report is.
3. A report that **did not see the fleet** is refused: there is nothing to simulate.
4. **Unseen defenses** are assumed to be **absent**: the victory rate shown is then an optimistic floor. Enter an estimate if you have one.
5. **Unseen research** is assumed to be **equal to yours**, without your talents.
6. Changing an imported value switches the simulation to **manual entry**: the report is no longer used.
7. The defender fights **without talents or dynasty bonuses**: they are never revealed.
8. Silo missiles never fight: they do not appear in the simulator.

### Your side
9. Your fleet fights with your research, dynasty and talents, as in a real battle.
10. You can enter more ships than you own: the simulator also helps decide what to build.
11. To simulate other Weapon Systems, Shielding Technology or Armor Technology levels, fill in **all three** research fields.

### The result
12. Each simulation replays the battle **{SIM_FRONT_ITER} times** and gives the attacker's and defender's **victory rates** and the draw rate, the average number of rounds, and the average **losses** and **survivors**, rounded to whole units.
13. The **round-by-round log** is that of one of the {SIM_FRONT_ITER} battles, as an example: it does not describe the series.
14. The **debris field** is that of an average battle, both sides' wreckage, at your universe's debris rate.
15. Some talents add an **Expected loot** (the most a victory would bring, based on the stock the report read and the survivors' holds) or a **Hunt balance**.

### Limits
16. A simulation is refused beyond **{N(SIM_UNITS)} units per side**, **{SIM_ITER} battles**, or **{N(SIM_DEPLOY)} deployments** (both sides' units × number of battles).

## Worked example

**Incomplete report**: your report saw the fleet, but neither defenses nor research. The simulator assumes zero defenses and technologies equal to yours. If the target actually has 20 Ion Batteries, your real chance of victory will be **lower** than shown.

**Size limit**: with {SIM_FRONT_ITER} battles per simulation, the {N(SIM_DEPLOY)} deployment limit allows {N(SIM_DEPLOY // SIM_FRONT_ITER)} units in all, for example {N(ok_side)} on each side. With {N(too_side)} units on each side, ({N(too_side)} + {N(too_side)}) × {SIM_FRONT_ITER} = {N(2 * too_side * SIM_FRONT_ITER)}: the simulation is refused.

## Common pitfalls

- **An incomplete report makes the simulator optimistic**: fill in the missing categories before trusting the result.
- **An old report lies**: a planet changes fast, spy again before you commit.
- **The defender may be stronger than expected**: its talents are not simulated.
- **Technologies matter**: if you know the target's, enter them.

## Related pages

- [Reading a spy report](/en/espionage/spy-report)
- [How combat works](/en/combat/how-combat-works)
- [Debris fields](/en/combat/debris)
- [Plunder](/en/combat/plunder)
'''

def run():
    write('fr', 'combat/simulator', body('fr'))
    write('en', 'combat/simulator', body('en'))
