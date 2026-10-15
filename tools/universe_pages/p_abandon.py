import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

A = DEFAULTS['abandon']
SHIP_DEBRIS = DEFAULTS['debris'][0]
EX_LEVEL, EX_SHIPS, EX_DEF, EX_SAT = 10, 1000, 200, 50
LF = (3000, 1000)  # coût d'un Intercepteur (métal, cristal)
DAYS = [0, 2, 6, 10, 20, 40, 60]


def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    fr = lang == 'fr'
    lost_s = share_of(EX_SHIPS, A['f_init'])
    ships0 = EX_SHIPS - lost_s
    def0 = EX_DEF - share_of(EX_DEF, A['d_init'])
    wm, wc = fl(lost_s * LF[0] * SHIP_DEBRIS / 100), fl(lost_s * LF[1] * SHIP_DEBRIS / 100)
    lvl = lambda d: max(0, EX_LEVEL - A['b_init'] - (d // A['b_int']) * A['b_loss'])
    zero_day = (EX_LEVEL - A['b_init']) * A['b_int']
    rows = [[d, lvl(d), N(wasted(ships0, A['f_loss'], d // A['f_int'])), N(wasted(def0, A['d_loss'], d // A['d_int']))] for d in DAYS]
    if fr:
        data = [
            ['Bâtiments', f"−{A['b_init']} niveau", f"−{A['b_loss']} niveau tous les {A['b_int']} jours"],
            ['Vaisseaux', f"−{P(A['f_init'])}", f"−{P(A['f_loss'])} de ce qui reste tous les {A['f_int']} jours"],
            ['Défenses', f"−{P(A['d_init'])}", f"−{P(A['d_loss'])} de ce qui reste tous les {A['d_int']} jours"],
            ['Collecteurs solaires', f"−{P(A['sat_init'])}", ''],
            ['Ressources', 'aucune perte', 'aucune perte'],
            ['Planète', '', f"disparaît au bout de {A['life']} jours, ou plus tôt s'il n'y reste plus rien"],
            ["Recolonisation par l'ancien propriétaire", '', f"interdite pendant {A['lock']} jours"],
        ]
        return f'''# Abandonner une colonie

> **En bref** : vous pouvez abandonner définitivement une colonie pour récupérer sa place. La planète reste sur la carte avec ce qu'elle contient, mais perd aussitôt une partie de ses bâtiments, de sa flotte et de ses défenses, puis se dégrade jusqu'à disparaître au bout de {A['life']} jours. Tout autre joueur peut la piller ou la recoloniser pendant ce temps, et récupère alors ce qui reste.
{{.is-info}}

> **Paramètre d'univers** : toutes les valeurs de dégradation d'une planète abandonnée (pertes immédiates, rythme des pertes, durée de vie, délai avant que l'ancien propriétaire puisse la reprendre) peuvent être différentes selon l'univers.
> Par défaut : **valeurs du tableau ci-dessous** · Redline : **identiques**
{{.is-info}}

## Règles

### Conditions
1. La **planète mère** ne peut pas être abandonnée. Une lune ne s'abandonne pas seule : elle part avec sa planète.
2. L'abandon est impossible tant que quelque chose est en cours **sur cette planète ou sur sa lune** : construction de bâtiment, de vaisseaux ou de défenses, réparation, recherche lancée depuis cette planète, flotte en route depuis ou vers elle, frappe de missiles encore en vol. Le jeu affiche la liste de tout ce qui bloque. Vos autres planètes, elles, peuvent être occupées.
3. Pour confirmer, vous devez saisir le nom de la planète. **L'abandon est irréversible.**

### Conséquences immédiates
4. Vous perdez la planète **définitivement**. Rien n'est remboursé, et ses points sortent de votre score.
5. Vous récupérez **immédiatement une place de colonie**. Si vous regardiez cette planète, le jeu vous ramène sur votre planète mère.
6. Les ressources restent sur place, sans jamais se dégrader. La production s'arrête.
7. Le **premier choc**, sur la planète comme sur sa lune : chaque bâtiment perd **{A['b_init']} niveau**, la flotte perd **{P(A['f_init'])}** de chaque type de vaisseau et les défenses **{P(A['d_init'])}** de chaque type (arrondi à l'inférieur). Les Collecteurs solaires sont **tous perdus**.
8. Les vaisseaux détruits par ce choc laissent un **champ de ruines** en orbite, au taux de débris des vaisseaux de l'univers ({P(SHIP_DEBRIS)} par défaut). Les défenses et les Collecteurs solaires n'en laissent pas.
9. La **lune** de la planète, et tout ce qu'elle porte, est abandonnée avec elle.

### Ensuite
10. Les bâtiments perdent {A['b_loss']} niveau **tous les {A['b_int']} jours**. La flotte restante perd {P(A['f_loss'])} de ce qui reste tous les {A['f_int']} jours, les défenses {P(A['d_loss'])} tous les {A['d_int']} jours : au moins une unité à chaque fois, tant qu'il en reste.
11. Les autres joueurs peuvent l'**espionner, l'attaquer, la piller ou la recoloniser**. Personne ne peut y transporter de ressources. La limite d'attaques ne s'applique pas : la planète n'a plus de propriétaire.
12. Celui qui la recolonise reprend **tout ce qui reste**, lune comprise, et la dégradation s'arrête.
13. La planète **disparaît** au bout de **{A['life']} jours**, ou plus tôt quand il ne reste plus rien sur elle ni sur sa lune (tous les bâtiments à 0, plus aucun vaisseau ni défense). Les ressources disparaissent avec elle ; la position redevient libre, sous son nom d'origine. Les champs de ruines en orbite, eux, restent.
14. L'ancien propriétaire ne peut pas la recoloniser pendant **{A['lock']} jours**.

## Exemple chiffré

Vous abandonnez une colonie avec un Excavateur minéral niveau {EX_LEVEL}, {N(EX_SHIPS)} Intercepteurs, {N(EX_DEF)} défenses d'un même type et {N(EX_SAT)} Collecteurs solaires.
- Aussitôt : Excavateur niveau **{EX_LEVEL - A['b_init']}** ; {N(lost_s)} Intercepteurs détruits, il en reste **{N(ships0)}** ; il reste **{N(def0)}** défenses ; plus aucun Collecteur solaire.
- Les {N(lost_s)} Intercepteurs détruits laissent {N(lost_s)} × {N(LF[0])} × {P(SHIP_DEBRIS)} = **{N(wm)} métal** et {N(lost_s)} × {N(LF[1])} × {P(SHIP_DEBRIS)} = **{N(wc)} cristal** de débris.
- L'Excavateur tombe à 0 au bout de {zero_day} jours. La planète dure tout de même {A['life']} jours, tant qu'il reste des vaisseaux ou des défenses.

Ce qui reste au fil des jours :

{table(['Jour', 'Excavateur minéral', 'Intercepteurs', 'Défenses'], rows)}

Si un joueur la recolonise au bout de 6 jours, il récupère l'Excavateur au niveau **{lvl(6)}**, {N(wasted(ships0, A['f_loss'], 6 // A['f_int']))} Intercepteurs, {N(wasted(def0, A['d_loss'], 6 // A['d_int']))} défenses et toutes les ressources.

## Données détaillées

{table(['Élément', 'Perte immédiate', 'Perte ensuite'], data)}

## Pièges fréquents

- **Videz la planète avant** : rapatriez flotte et ressources avant d'abandonner, sinon elles restent à la merci des pillards et de celui qui la recolonisera.
- **La lune est perdue aussi** : une lune et ses bâtiments partent avec la planète.
- **Pas de retour en arrière** : vous ne pourrez pas la reprendre avant {A['lock']} jours, et elle aura continué à se dégrader.
- **Tout doit être à l'arrêt, lune comprise** : une construction, une recherche ou une flotte en route bloque l'abandon.

## Pages liées

- [Coloniser](/fr/universe/colonization)
- [Planètes : taille, température, type](/fr/universe/planets)
- [Les lunes](/fr/universe/moons)
- [Champs de débris](/fr/combat/debris)
'''
    data = [
        ['Buildings', f"−{A['b_init']} level", f"−{A['b_loss']} level every {A['b_int']} days"],
        ['Ships', f"−{P(A['f_init'])}", f"−{P(A['f_loss'])} of what is left every {A['f_int']} days"],
        ['Defenses', f"−{P(A['d_init'])}", f"−{P(A['d_loss'])} of what is left every {A['d_int']} days"],
        ['Solar Collectors', f"−{P(A['sat_init'])}", ''],
        ['Resources', 'no loss', 'no loss'],
        ['Planet', '', f"disappears after {A['life']} days, or earlier if nothing is left on it"],
        ['Recolonization by the former owner', '', f"barred for {A['lock']} days"],
    ]
    return f'''# Abandoning a colony

> **In short**: you can give up a colony for good to get its slot back. The planet stays on the map with what it holds, but immediately loses part of its buildings, fleet and defenses, then decays until it disappears after {A['life']} days. Any other player can raid or recolonize it in the meantime, and then gets what is left.
{{.is-info}}

> **Universe setting**: every decay value of an abandoned planet (immediate losses, pace of losses, lifetime, delay before the former owner can take it back) may differ from one universe to another.
> Default: **values in the table below** · Redline: **the same**
{{.is-info}}

## Rules

### Conditions
1. The **mother planet** cannot be abandoned. A moon is never abandoned on its own: it leaves with its planet.
2. Abandoning is impossible while something is under way **on this planet or its moon**: building, ship or defense construction, repair, research started from this planet, a fleet travelling from or to it, a missile strike still in flight. The game lists everything that blocks it. Your other planets may be busy.
3. To confirm, you must type the planet's name. **Abandoning cannot be undone.**

### Immediate consequences
4. You lose the planet **for good**. Nothing is refunded, and its points leave your score.
5. You get **a colony slot back at once**. If you were looking at that planet, the game takes you back to your mother planet.
6. Resources stay where they are, and never decay. Production stops.
7. The **first shock**, on the planet as on its moon: each building loses **{A['b_init']} level**, the fleet loses **{P(A['f_init'])}** of each ship type and the defenses **{P(A['d_init'])}** of each type (rounded down). Solar Collectors are **all lost**.
8. Ships destroyed by this shock leave a **debris field** in orbit, at the universe's ship debris rate ({P(SHIP_DEBRIS)} by default). Defenses and Solar Collectors leave none.
9. The planet's **moon**, and everything on it, is abandoned along with it.

### Afterwards
10. Buildings lose {A['b_loss']} level **every {A['b_int']} days**. The remaining fleet loses {P(A['f_loss'])} of what is left every {A['f_int']} days, the defenses {P(A['d_loss'])} every {A['d_int']} days: at least one unit each time, as long as any are left.
11. Other players can **spy on, attack, raid or recolonize** it. Nobody can transport resources to it. The attack limit does not apply: the planet no longer has an owner.
12. Whoever recolonizes it takes over **everything left**, moon included, and the decay stops.
13. The planet **disappears** after **{A['life']} days**, or earlier once nothing is left on it or its moon (every building at 0, no ship or defense left). Resources go with it; the position becomes free again, under its original name. Debris fields in orbit stay.
14. The former owner cannot recolonize it for **{A['lock']} days**.

## Worked example

You abandon a colony with a level {EX_LEVEL} Mineral Excavator, {N(EX_SHIPS)} Interceptors, {N(EX_DEF)} defenses of one type and {N(EX_SAT)} Solar Collectors.
- At once: Excavator level **{EX_LEVEL - A['b_init']}**; {N(lost_s)} Interceptors destroyed, **{N(ships0)}** left; **{N(def0)}** defenses left; no Solar Collector left.
- The {N(lost_s)} destroyed Interceptors leave {N(lost_s)} × {N(LF[0])} × {P(SHIP_DEBRIS)} = **{N(wm)} metal** and {N(lost_s)} × {N(LF[1])} × {P(SHIP_DEBRIS)} = **{N(wc)} crystal** of debris.
- The Excavator reaches 0 after {zero_day} days. The planet still lasts {A['life']} days, as long as ships or defenses are left.

What is left over the days:

{table(['Day', 'Mineral Excavator', 'Interceptors', 'Defenses'], rows)}

If a player recolonizes it after 6 days, they get the Excavator at level **{lvl(6)}**, {N(wasted(ships0, A['f_loss'], 6 // A['f_int']))} Interceptors, {N(wasted(def0, A['d_loss'], 6 // A['d_int']))} defenses and all the resources.

## Detailed data

{table(['Item', 'Immediate loss', 'Loss afterwards'], data)}

## Common pitfalls

- **Empty the planet first**: bring fleet and resources home before abandoning, or they stay at the mercy of raiders and of whoever recolonizes it.
- **The moon is lost too**: a moon and its buildings leave with the planet.
- **No way back**: you cannot take it back for {A['lock']} days, and it will have kept decaying.
- **Everything must be idle, moon included**: a construction, a research or a fleet on its way blocks the abandonment.

## Related pages

- [Colonization](/en/universe/colonization)
- [Planets: size, temperature, type](/en/universe/planets)
- [Moons](/en/universe/moons)
- [Debris fields](/en/combat/debris)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/abandoning-a-planet', body(lang))
