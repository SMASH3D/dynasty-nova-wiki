import sys; sys.path.insert(0, sys.argv[1])
from esp_lib import *; from write import *

# Exemple : 2 Éclaireurs, rapport lu jusqu'à la flotte (palier 3), défenses verrouillées.
SENT, DEEPEST = 2, 3
EDGE = DEEPEST - probe_bonus(SENT)  # avance minimale prouvée par le rapport (EspionageEdge::fromScan)
need = {t[0]: probes_for(t[0], EDGE) for t in TIERS}
assert EDGE == 2 and need[5] == 6 and need[7] == 10 and need[9] is None


def body(lang):
    if lang == 'fr':
        return f'''# Lire un rapport d'espionnage

> **En bref** : un rapport d'espionnage décrit toujours la planète ou la lune visée, puis ouvre une section par palier atteint : ressources, flotte, défenses et missiles, bâtiments, recherches. Une section marquée « Niveau d'espionnage insuffisant » n'a pas été lue : cela ne veut pas dire que la cible n'a rien.
{{.is-info}}

## Règles

### L'en-tête

1. Le rapport indique la **cible** (planète ou lune, coordonnées, propriétaire), votre **base de départ**, et le sort de vos sondes : « 2 sondes perdues sur 10 », ou aucune perte.
2. Une case vide donne « Planète inhabitée ». Une planète abandonnée ne donne aucun propriétaire, mais depuis combien de jours elle est abandonnée : ses chiffres sont ceux du jour, dégradation comprise.

### Les caractéristiques, toujours visibles

3. Pour une **planète** : son type, sa taille en cases, les cases encore libres et ses températures minimale et maximale.
4. Pour une **lune** : son diamètre, ses cases, les cases libres et les températures, qui sont celles de sa planète.

### Les sections, selon le niveau effectif

5. Chaque section s'ouvre à son palier de **niveau effectif** (voir [Espionner](/fr/espionage/spying)) :
   - **Ressources** dès 1 : métal, cristal et hydrogène sur place à l'arrivée des sondes, production comprise jusqu'à cet instant (dans la limite des entrepôts) ;
   - **Flotte** dès 3 : les vaisseaux stationnés sur le corps espionné ;
   - **Défenses** et **Missiles** dès 5 : les missiles sont listés à part, car ils ne combattent pas ;
   - **Bâtiments** dès 7 : le niveau de chaque bâtiment ;
   - **Recherches** dès 9 : le niveau de chaque recherche du joueur.
6. Une section **non lue** s'affiche avec la mention « Niveau d'espionnage insuffisant ». Une section lue mais vide affiche « Aucun élément détecté » : là, la cible n'a vraiment rien.
7. Chez un joueur **en vacances**, le rapport donne la planète et son propriétaire, mais **aucune section**, quelle que soit votre avance.
8. Certains talents de dynastie ajoutent des lignes au rapport (activité de la cible, système voisin, production) ou le brouillent (flotte arrondie, stock en partie caché) : voir l'[Ombre](/fr/dynasty/classes/shadow) et l'[Oracle](/fr/dynasty/classes/oracle).

### Vos rapports

9. Le jeu garde vos **{SPY_HISTORY_KEPT} derniers rapports** d'espionnage sur une même cible ; les plus anciens sont supprimés.
10. Un rapport peut être **partagé** avec votre alliance (voir [Messagerie et rapports](/fr/players/messages-and-reports)) et **importé** dans le [simulateur de combat](/fr/combat/simulator).

### L'alerte d'intrusion (côté cible)

11. Le joueur espionné reçoit une **alerte d'intrusion** sur la planète ou la lune visée. Elle porte l'un de ces trois niveaux :
    - **Auteur inconnu** : la vague est passée, l'alerte dit seulement « Sonde repérée » ;
    - **Auteur identifié** : la vague a été abattue, l'alerte donne le pseudo de l'espion ;
    - **Origine localisée** : en plus, les coordonnées de la planète d'où les sondes sont parties.
12. L'alerte indique aussi combien de sondes votre défense a abattues.

## Exemple chiffré

Vous envoyez **{SENT} Éclaireurs**. Le rapport montre les ressources et la flotte, mais les défenses sont marquées « Niveau d'espionnage insuffisant ».
- Le rapport a atteint le palier {DEEPEST} avec un bonus de sondes de +{probe_bonus(SENT)} : votre avance sur cette cible vaut au moins {DEEPEST} − {probe_bonus(SENT)} = **{EDGE}**.
- Pour lire les **défenses** (palier 5), il faut un bonus de 5 − {EDGE} = 3, soit **{need[5]} Éclaireurs**.
- Pour les **bâtiments** (palier 7), il faut le bonus maximal de +5 : **{need[7]} Éclaireurs**.
- Les **recherches** (palier 9) demanderaient +7 : hors de portée des sondes. Il faut monter votre Renseignement Tactique.

## Pièges fréquents

- **« Niveau d'espionnage insuffisant » ≠ rien** : ne concluez jamais qu'une planète est sans défense parce que la section n'a pas été lue.
- **Le rapport vieillit** : la cible produit, construit et déplace sa flotte. Espionnez juste avant d'attaquer.
- **Un rapport vide peut signifier des vacances** : vérifiez le statut dans la vue galaxie.
- **Planète et lune sont deux cibles** : la flotte stationnée sur la lune n'apparaît pas dans le rapport de la planète, et l'inverse.

## Pages liées

- [Espionner](/fr/espionage/spying)
- [Pillage](/fr/combat/plunder)
- [Simulateur de combat](/fr/combat/simulator)
- [Messagerie et rapports](/fr/players/messages-and-reports)
'''
    return f'''# Reading a spy report

> **In short**: a spy report always describes the targeted planet or moon, then opens one section per tier reached: resources, fleet, defenses and missiles, buildings, research. A section marked "Insufficient espionage level" was not read: it does not mean the target has nothing.
{{.is-info}}

## Rules

### The header

1. The report shows the **target** (planet or moon, coordinates, owner), your **departure base**, and what happened to your probes: "2 probes lost out of 10", or no loss.
2. An empty cell reads "Uninhabited planet". An abandoned planet shows no owner, but how many days it has been abandoned: its figures are today's, decay included.

### Characteristics, always shown

3. For a **planet**: its type, its size in fields, the fields still free and its minimum and maximum temperatures.
4. For a **moon**: its diameter, its fields, the free fields and the temperatures, which are its planet's.

### Sections, by effective level

5. Each section opens at its **effective level** tier (see [Spying](/en/espionage/spying)):
   - **Resources** from 1: metal, crystal and hydrogen on hand when the probes arrive, production up to that moment included (within storage limits);
   - **Fleet** from 3: the ships stationed on the spied body;
   - **Defenses** and **Missiles** from 5: missiles are listed apart, since they do not fight;
   - **Buildings** from 7: the level of each building;
   - **Research** from 9: the level of each of the player's research.
6. A section that was **not read** shows "Insufficient espionage level". A section that was read but is empty shows "Nothing detected": then the target really has nothing.
7. For a player **on vacation**, the report gives the planet and its owner, but **no section**, whatever your lead.
8. Some dynasty talents add lines to the report (target activity, neighbouring system, production) or blur it (rounded fleet, partly hidden stock): see the [Shadow](/en/dynasty/classes/shadow) and the [Oracle](/en/dynasty/classes/oracle).

### Your reports

9. The game keeps your **{SPY_HISTORY_KEPT} latest spy reports** on a given target; older ones are deleted.
10. A report can be **shared** with your alliance (see [Messages and reports](/en/players/messages-and-reports)) and **imported** into the [battle simulator](/en/combat/simulator).

### The intrusion alert (target side)

11. The spied player gets an **intrusion alert** on the targeted planet or moon. It carries one of three levels:
    - **Unknown intruder**: the wave got through, the alert only says "Probe spotted";
    - **Intruder identified**: the wave was shot down, the alert gives the spy's username;
    - **Origin traced**: in addition, the coordinates of the planet the probes left from.
12. The alert also shows how many probes your defense shot down.

## Worked example

You send **{SENT} Scouts**. The report shows resources and fleet, but the defenses are marked "Insufficient espionage level".
- The report reached tier {DEEPEST} with a +{probe_bonus(SENT)} probe bonus: your lead on this target is at least {DEEPEST} − {probe_bonus(SENT)} = **{EDGE}**.
- To read the **defenses** (tier 5), you need a bonus of 5 − {EDGE} = 3, so **{need[5]} Scouts**.
- For the **buildings** (tier 7), you need the maximum +5 bonus: **{need[7]} Scouts**.
- **Research** (tier 9) would take +7: beyond what probes can give. You need more Espionage Technology.

## Common pitfalls

- **"Insufficient espionage level" ≠ nothing**: never conclude that a planet is undefended because the section was not read.
- **Reports age**: the target produces, builds and moves its fleet. Spy right before attacking.
- **An empty report may mean vacation**: check the status in the galaxy view.
- **Planet and moon are two targets**: the fleet stationed on the moon does not show in the planet's report, and vice versa.

## Related pages

- [Spying](/en/espionage/spying)
- [Plunder](/en/combat/plunder)
- [Battle simulator](/en/combat/simulator)
- [Messages and reports](/en/players/messages-and-reports)
'''


for lang in ('fr', 'en'):
    write(lang, 'espionage/spy-report', body(lang),
          description="Les sections du rapport, ce qui les débloque, et l'alerte d'intrusion." if lang == 'fr'
          else 'The report sections, what unlocks them, and the intrusion alert.')
