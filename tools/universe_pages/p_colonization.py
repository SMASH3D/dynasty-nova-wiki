import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

LOCK = DEFAULTS['abandon']['lock']
LEVELS = list(range(0, 20))
PIONEER = dict(cost=(10000, 20000, 10000), hull=30000, cargo=7500, speed=2500, fuel=1000)


def body(lang):
    N = lambda x: n(x, lang)
    fr = lang == 'fr'
    lv = [0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    t_head = ['Niveau'] + [str(l) for l in lv] if fr else ['Level'] + [str(l) for l in lv]
    t_row = [['Planètes au total' if fr else 'Total planets'] + [str(max_bases(l)) for l in lv]]
    c = PIONEER['cost']
    cargo_ex = 2 * PIONEER['cargo']
    if fr:
        return f'''# Coloniser

> **En bref** : pour fonder une colonie, espionnez d'abord la position visée, puis envoyez-y un Pionnier spatial en mission Colonisation. Le nombre de planètes que vous pouvez posséder dépend de votre niveau de Cosmologie Appliquée : 2 planètes au niveau 1, puis une de plus tous les deux niveaux. La colonie démarre vide, avec les ressources et les vaisseaux que vous avez envoyés.
{{.is-info}}

> **Paramètre d'univers** : le délai pendant lequel l'ancien propriétaire d'une planète abandonnée ne peut pas la recoloniser peut être différent selon l'univers.
> Par défaut : **{LOCK} jours** · Redline : **{REDLINE['abandon']['lock']} jours**
{{.is-info}}

<img src="/images/illustrations/ships/pionnier-spatial.jpg" width="180" alt="Pionnier spatial">

## Règles

### Avant le départ
1. Il faut un **Pionnier spatial** (Dock orbital 4, Moteur Magnétique 3, Cosmologie Appliquée 1) et une **place de colonie libre**.
2. **Nombre de planètes** (planète mère comprise) = 1 + partie entière((niveau de Cosmologie Appliquée + 1) / 2). Seules les planètes comptent : une lune n'occupe pas de place de colonie.
3. La cible doit avoir été **espionnée**, par vous ou par un membre de votre alliance. Une position jamais espionnée ne peut pas être colonisée.
4. La cible peut être :
   - une **position libre** d'un système ;
   - une planète **abandonnée** par un autre joueur. Son ancien propriétaire, lui, doit attendre {LOCK} jours.
5. L'espace lointain, la Station stellaire et les lunes ne se colonisent pas.
6. La mission **Colonisation** est un aller simple : l'hydrogène du retour n'est pas facturé.

### À l'arrivée
7. Le jeu vérifie à nouveau la place de colonie. Si vous n'en avez plus, ou si la position a été prise entre-temps, la flotte fait demi-tour et un rapport vous l'explique.
8. **Un seul Pionnier spatial est consommé** : il devient la colonie. Les autres vaisseaux de la flotte, autres Pionniers compris, **restent sur la nouvelle colonie** et forment sa première flotte.
9. La cargaison de toute la flotte est déchargée sur la colonie : ce sont ses **ressources de départ**.
10. Sur une position libre, la colonie démarre **sans aucun bâtiment**. Construisez d'abord la **Base Coloniale** (gratuite, 10 secondes) : aucun autre bâtiment ne peut être lancé avant elle. En attendant, la colonie stocke déjà 10 000 de chaque ressource.
11. Sa taille et sa température dépendent de sa position, et elle profite du **bonus de position** (voir [Planètes](/fr/universe/planets)).
12. Sur une planète **abandonnée**, vous reprenez **tout ce qui reste** : bâtiments, ressources, vaisseaux, défenses, et sa lune avec ce qu'elle porte. La dégradation s'arrête, la production reprend à votre profit (voir [Abandonner une colonie](/fr/universe/abandoning-a-planet)).

## Exemple chiffré

Vous avez Cosmologie Appliquée niveau 3 :
- Planètes possibles : 1 + partie entière((3 + 1) / 2) = **{max_bases(3)}**, soit votre planète mère et {max_bases(3) - 1} colonies.
- Monter au niveau 4 ne change rien ({max_bases(4)} planètes). Il faut le niveau 5 pour une {max_bases(5)}e planète.

Vous envoyez 2 Pionniers spatiaux chargés à plein vers une position libre déjà espionnée :
- Ils emportent {N(PIONEER['cargo'])} × 2 = **{N(cargo_ex)} ressources**.
- À l'arrivée, un Pionnier devient la colonie, l'autre reste en orbite de la colonie, et les {N(cargo_ex)} ressources sont déposées sur place.

## Données détaillées

### Planètes selon la Cosmologie Appliquée

{table(t_head, t_row)}

Les niveaux pairs n'ajoutent pas de planète (le niveau 2 donne autant que le niveau 1).

### Le Pionnier spatial

{table(['Coût', 'Structure', 'Fret', 'Vitesse de base', 'Moteur', 'Consommation'], [[f'{N(c[0])} métal, {N(c[1])} cristal, {N(c[2])} hydrogène', N(PIONEER['hull']), N(PIONEER['cargo']), N(PIONEER['speed']), 'Moteur Magnétique', N(PIONEER['fuel'])]])}

## Pièges fréquents

- **Espionnez avant de partir** : sans espionnage de la position, par vous ou votre alliance, la mission est refusée.
- **Chargez la flotte** : la colonie n'a pas d'autres ressources que celles que vous apportez.
- **Les escortes ne rentrent pas** : tout vaisseau envoyé avec le Pionnier reste sur la colonie.
- **Une colonie de plus tous les deux niveaux** : vérifiez que vous avez une place libre avant d'envoyer le Pionnier, et qu'elle l'est encore à l'arrivée.
- **Choisissez la position** : près de l'étoile, une petite planète chaude et un bonus de cristal ; au milieu du système, un bonus de métal ; loin, une grande planète froide, meilleure pour l'hydrogène.

## Pages liées

- [Planètes : taille, température, type](/fr/universe/planets)
- [Abandonner une colonie](/fr/universe/abandoning-a-planet)
- [Liste des technologies](/fr/research/technologies)
- [Les missions](/fr/fleet/missions)
- [Espionner](/fr/espionage/spying)
'''
    return f'''# Colonization

> **In short**: to found a colony, first spy the target position, then send a Space Pioneer there on a Colonization mission. How many planets you can own depends on your Astrophysics level: 2 planets at level 1, then one more every two levels. The colony starts empty, with the resources and ships you sent.
{{.is-info}}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{{.is-warning}}

> **Universe setting**: how long the former owner of an abandoned planet must wait before recolonizing it may differ from one universe to another.
> Default: **{LOCK} days** · Redline: **{REDLINE['abandon']['lock']} days**
{{.is-info}}

<img src="/images/illustrations/ships/pionnier-spatial.jpg" width="180" alt="Space Pioneer">

## Rules

### Before leaving
1. You need a **Space Pioneer** (Orbital Dock 4, Impulse Drive 3, Astrophysics 1) and a **free colony slot**.
2. **Number of planets** (mother planet included) = 1 + whole part of ((Astrophysics level + 1) / 2). Only planets count: a moon does not take a colony slot.
3. The target must have been **spied**, by you or by a member of your alliance. A position never spied cannot be colonized.
4. The target can be:
   - a **free position** in a system;
   - a planet **abandoned** by another player. Its former owner has to wait {LOCK} days.
5. Deep space, the Stellar Station and moons cannot be colonized.
6. The **Colonization** mission is one way: hydrogen for a return trip is not charged.

### On arrival
7. The game checks the colony slot again. If you no longer have one, or if the position was taken in the meantime, the fleet turns back and a report tells you why.
8. **Only one Space Pioneer is used up**: it becomes the colony. The fleet's other ships, other Pioneers included, **stay on the new colony** as its first fleet.
9. The whole fleet's cargo is unloaded on the colony: these are its **starting resources**.
10. On a free position, the colony starts **with no building at all**. First build the **Colonial Base** (free, 10 seconds): no other building can be started before it. Meanwhile, the colony already stores 10,000 of each resource.
11. Its size and temperature depend on its position, and it gets the **position bonus** (see [Planets](/en/universe/planets)).
12. On an **abandoned** planet, you take over **everything left**: buildings, resources, ships, defenses, and its moon with whatever stands on it. The decay stops and output resumes for you (see [Abandoning a colony](/en/universe/abandoning-a-planet)).

## Worked example

You have Astrophysics level 3:
- Possible planets: 1 + whole part of ((3 + 1) / 2) = **{max_bases(3)}**, that is your mother planet and {max_bases(3) - 1} colonies.
- Going to level 4 changes nothing ({max_bases(4)} planets). You need level 5 for a {max_bases(5)}th planet.

You send 2 fully loaded Space Pioneers to a free position already spied:
- They carry {N(PIONEER['cargo'])} × 2 = **{N(cargo_ex)} resources**.
- On arrival, one Pioneer becomes the colony, the other stays in the colony's orbit, and the {N(cargo_ex)} resources are unloaded there.

## Detailed data

### Planets by Astrophysics level

{table(t_head, t_row)}

Even levels add no planet (level 2 gives as many as level 1).

### The Space Pioneer

{table(['Cost', 'Structure', 'Cargo', 'Base speed', 'Drive', 'Fuel use'], [[f'{N(c[0])} metal, {N(c[1])} crystal, {N(c[2])} hydrogen', N(PIONEER['hull']), N(PIONEER['cargo']), N(PIONEER['speed']), 'Impulse Drive', N(PIONEER['fuel'])]])}

## Common pitfalls

- **Spy before you leave**: without the position being spied, by you or your alliance, the mission is refused.
- **Load the fleet**: the colony has no resources other than those you bring.
- **Escorts do not come back**: every ship sent with the Pioneer stays on the colony.
- **One more colony every two levels**: check that you have a free slot before sending the Pioneer, and that you still have it on arrival.
- **Choose the position**: close to the star, a small hot planet and a crystal bonus; in the middle of the system, a metal bonus; far out, a large cold planet, better for hydrogen.

## Related pages

- [Planets: size, temperature, type](/en/universe/planets)
- [Abandoning a colony](/en/universe/abandoning-a-planet)
- [List of technologies](/en/research/technologies)
- [Missions](/en/fleet/missions)
- [Spying](/en/espionage/spying)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/colonization', body(lang))
