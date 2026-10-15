from combat_lib import *
from write import write, table

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    P1 = lambda x: pct(x, lang, 1)
    rows = [[k, P1(binom(k, 3, REPAIR / 100) * 100), P1(binom(k, 3, (REPAIR + REPAIR_HERITAGE) / 100) * 100)] for k in (3, 2, 1, 0)]
    all10 = (REPAIR / 100) ** 10 * 100
    all10h = ((REPAIR + REPAIR_HERITAGE) / 100) ** 10 * 100
    exp_rows = [[q, N(q * REPAIR / 100), N(q * (REPAIR + REPAIR_HERITAGE) / 100), N(q * REPAIR_CEILING / 100)] for q in (1, 2, 10, 50, 200)]
    heritage = REPAIR + REPAIR_HERITAGE
    if lang == 'fr':
        return f'''# Reconstruction des défenses

> **En bref** : à la fin d'un combat, chaque défense détruite a **{P(REPAIR)} de chances** d'être reconstruite, gratuitement et aussitôt. Le tirage se fait unité par unité : en moyenne, 7 défenses détruites sur 10 reviennent, mais rien n'est garanti. La dynastie L'Héritage et certains talents relèvent cette chance. Les vaisseaux, eux, ne sont jamais reconstruits ainsi.
{{.is-info}}

## Règles

1. À la fin de **chaque combat**, gagné, perdu ou nul, **chaque défense détruite** fait l'objet d'un **tirage indépendant à {P(REPAIR)}**. Réussi, elle est reconstruite sans frais, tout de suite ; raté, elle est perdue.
2. Ce n'est **pas un pourcentage appliqué au lot** : avec 10 défenses détruites, entre 0 et 10 reviennent, 7 en moyenne.
3. La **Barrière défensive** et le **Dôme protecteur** suivent la même règle : {P(REPAIR)} de chances de les garder. Perdus, ils peuvent être reconstruits au chantier.
4. Les points des défenses reconstruites ne sont pas retirés ; seules les défenses perdues font baisser vos points.
5. La règle vaut aussi pour les défenses d'une **lune**, y compris pendant une [destruction de lune](/fr/combat/moon-destruction).
6. Les défenses détruites par des **Ogives longue portée** ne sont **pas** reconstruites ainsi : une frappe de missiles détruit pour de bon (sauf talent qui le permet).
7. Les **vaisseaux** ne sont jamais reconstruits gratuitement. Seule la [Station de réparation](/fr/economy/repair-station) en reprend une partie, sans tirage.
8. Les missiles stockés ne combattent pas : ils ne sont pas concernés.

### Ce qui modifie la chance
9. La dynastie **L'Héritage** porte la chance à **{P(heritage)}** (trait Rien ne se perd).
10. Les talents de dynastie et de classe peuvent l'augmenter de **{N(REPAIR_TALENT_CEILING)} points** au plus. Quels que soient les bonus, elle ne dépasse jamais **{P(REPAIR_CEILING)}**.
11. Certains talents du [Vétéran](/fr/dynasty/classes/veteran) font toujours revenir certaines défenses, ou toutes celles d'une seconde attaque rapprochée ; ceux de l'[Amiral](/fr/dynasty/classes/admiral) baissent la chance chez les défenseurs qu'il attaque.

## Exemple chiffré

Vous perdez 3 Batteries ioniques lors d'une attaque :

{table(['Batteries reconstruites', f'Probabilité à {P(REPAIR)}', f'Probabilité à {P(heritage)} (L\'Héritage)'], rows)}

Avec 10 Projecteurs balistiques détruits, la probabilité de tous les récupérer n'est que de **{P1(all10)}** (**{P1(all10h)}** avec L'Héritage).

## Données détaillées

Nombre moyen de défenses reconstruites :

{table(['Défenses détruites', f'À {P(REPAIR)}', f'À {P(heritage)}', f'Au plafond ({P(REPAIR_CEILING)})'], exp_rows)}

## Pièges fréquents

- **Comptez sur 70 % en moyenne, pas à coup sûr** : sur un petit nombre de défenses, l'écart peut être grand.
- **Le Dôme peut disparaître** : {P(100 - REPAIR)} de chances de le perdre chaque fois qu'il est détruit. Vous pourrez alors en reconstruire un.
- **Les missiles ennemis détruisent pour de bon** : face à des Ogives, la reconstruction ne joue pas.
- **Les débris comptent toutes les défenses détruites** : dans un univers où les défenses laissent des débris, même celles qui reviennent en laissent.

## Pages liées

- [Liste des défenses](/fr/defense/defenses)
- [Missiles](/fr/defense/missiles)
- [Station de réparation](/fr/economy/repair-station)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Les dynasties](/fr/dynasty/dynasties)
'''
    return f'''# Defense rebuild

> **In short**: at the end of a battle, each destroyed defense has a **{P(REPAIR)} chance** of being rebuilt, for free and at once. The roll is made unit by unit: on average, 7 destroyed defenses out of 10 come back, but nothing is guaranteed. The Heritage dynasty and some talents raise this chance. Ships, on the other hand, are never rebuilt this way.
{{.is-info}}

## Rules

1. At the end of **every battle**, won, lost or drawn, **each destroyed defense** gets an **independent {P(REPAIR)} roll**. On success it is rebuilt at no cost, at once; on failure it is lost.
2. It is **not a percentage applied to the batch**: with 10 defenses destroyed, between 0 and 10 come back, 7 on average.
3. The **Defensive Barrier** and the **Protective Dome** follow the same rule: a {P(REPAIR)} chance of keeping them. Once lost, they can be built again at the shipyard.
4. Rebuilt defenses keep their points; only the defenses lost lower your score.
5. The rule also applies to a **moon**'s defenses, including during a [moon destruction](/en/combat/moon-destruction).
6. Defenses destroyed by **Long-Range Warheads** are **not** rebuilt this way: a missile strike destroys for good (unless a talent allows it).
7. **Ships** are never rebuilt for free. Only the [Repair Station](/en/economy/repair-station) takes part of them back, with no roll.
8. Stored missiles do not fight: they are not concerned.

### What changes the chance
9. The dynasty **The Heritage** raises the chance to **{P(heritage)}** (Nothing Is Lost trait).
10. Dynasty and class talents can raise it by **{N(REPAIR_TALENT_CEILING)} points** at most. Whatever the bonuses, it never goes above **{P(REPAIR_CEILING)}**.
11. Some [Veteran](/en/dynasty/classes/veteran) talents always bring certain defenses back, or all of those of a second attack close behind; the [Admiral](/en/dynasty/classes/admiral)'s lower the chance for the defenders it attacks.

## Worked example

You lose 3 Ion Batteries in an attack:

{table(['Batteries rebuilt', f'Probability at {P(REPAIR)}', f'Probability at {P(heritage)} (The Heritage)'], rows)}

With 10 Ballistic Projectors destroyed, the chance of getting them all back is only **{P1(all10)}** (**{P1(all10h)}** with The Heritage).

## Detailed data

Average number of defenses rebuilt:

{table(['Defenses destroyed', f'At {P(REPAIR)}', f'At {P(heritage)}', f'At the ceiling ({P(REPAIR_CEILING)})'], exp_rows)}

## Common pitfalls

- **Count on 70% on average, not for sure**: with few defenses, the gap can be large.
- **The Dome can vanish**: a {P(100 - REPAIR)} chance of losing it every time it is destroyed. You can then build a new one.
- **Enemy missiles destroy for good**: against Warheads, the rebuild does not apply.
- **Debris counts every defense destroyed**: in a universe where defenses leave debris, even those that come back leave some.

## Related pages

- [Defense list](/en/defense/defenses)
- [Missiles](/en/defense/missiles)
- [Repair Station](/en/economy/repair-station)
- [How combat works](/en/combat/how-combat-works)
- [Dynasties](/en/dynasty/dynasties)
'''

def run():
    write('fr', 'combat/defense-rebuild', body('fr'))
    write('en', 'combat/defense-rebuild', body('en'))
