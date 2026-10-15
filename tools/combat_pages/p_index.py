from combat_lib import *
from write import write

def body(lang):
    P = lambda x: pct(x, lang)
    if lang == 'fr':
        return f'''# Combat

**Déroulement des combats et leurs suites.**

Une flotte en mission Attaque combat ce qui défend la planète ou la lune visée : vaisseaux en orbite et défenses. Le combat dure au plus {ROUNDS} rounds, puis viennent le butin, les débris, la chance de lune et les réparations.

```mermaid
graph TB
  A[Arrivée de la flotte] --> B[Combat : {ROUNDS} rounds au plus]
  B --> C{{Résultat}}
  C -->|Victoire de l'attaquant| D[Pillage : {P(LOOT)} du stock, dans la soute]
  C --> E[Champ de ruines et chance de lune]
  C --> F[Défenses reconstruites : {P(REPAIR)} par unité]
  C --> G[Station de réparation du défenseur]
  C --> H[Rapport de combat pour chaque camp]
```

## Pages de cette rubrique

- [Déroulement d'un combat](/fr/combat/how-combat-works) : statistiques, rounds, tirs rapides, boucliers, explosions.
- [Lire un rapport de combat](/fr/combat/battle-report) : ce que chaque camp voit, vue partielle, partage.
- [Pillage](/fr/combat/plunder) : la part emportée et la soute.
- [Champs de ruines (débris)](/fr/combat/debris) : débris, recyclage et formation des lunes.
- [Reconstruction des défenses](/fr/combat/defense-rebuild) : le tirage à {P(REPAIR)} par défense détruite.
- [Simulateur de combat](/fr/combat/simulator) : préparer une attaque.
- [Destruction de lune](/fr/combat/moon-destruction) : les Colossus stellaires et les deux tirages.
'''
    return f'''# Combat

**How battles work and what follows.**

A fleet on an Attack mission fights whatever defends the target planet or moon: ships in orbit and defenses. The battle lasts at most {ROUNDS} rounds, then come the loot, the debris, the moon chance and the repairs.

```mermaid
graph TB
  A[Fleet arrives] --> B[Battle: at most {ROUNDS} rounds]
  B --> C{{Outcome}}
  C -->|Attacker wins| D[Plunder: {P(LOOT)} of the stock, within the holds]
  C --> E[Debris field and moon chance]
  C --> F[Defenses rebuilt: {P(REPAIR)} per unit]
  C --> G[Defender's Repair Station]
  C --> H[Battle report for each side]
```

## Pages in this section

- [How combat works](/en/combat/how-combat-works): stats, rounds, rapid fire, shields, explosions.
- [Reading a battle report](/en/combat/battle-report): what each side sees, partial view, sharing.
- [Plunder](/en/combat/plunder): the share taken and the cargo space.
- [Debris fields](/en/combat/debris): debris, recycling and moon formation.
- [Defense rebuild](/en/combat/defense-rebuild): the {P(REPAIR)} roll per destroyed defense.
- [Battle simulator](/en/combat/simulator): preparing an attack.
- [Moon destruction](/en/combat/moon-destruction): Stellar Colossi and the two rolls.
'''

def run():
    write('fr', 'combat', body('fr'))
    write('en', 'combat', body('en'))
