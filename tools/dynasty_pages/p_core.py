"""Pages dynasty (index), dynasty/dynasties et dynasty/classes, FR et EN, d'après le code (DONNEES §18).

Usage : python3 tools/dynasty_pages/p_core.py
"""
from dyn_lib import DATA, RULES, CLASSES, LABELS, n, pct, class_label, branch_name, tree, clean
from write import write, table

TC = DATA['trait_constants']
CC = DATA['class_change']
COST, DAYS = CC['CLASS_CHANGE_COST'], CC['COOLDOWN_DAYS']
CMAX, KMAX = RULES['COMMON_MAX_POINTS'], RULES['CLASS_MAX_POINTS']
ARTICLE = {'fr': {'admiral': "L'Amiral", 'builder': 'Le Bâtisseur', 'energist': "L'Énergéticien", 'theorist': 'Le Théoricien',
                  'navigator': 'Le Navigateur', 'shadow': "L'Ombre", 'archivist': "L'Archiviste", 'veteran': 'Le Vétéran',
                  'symbiote': 'Le Symbiote', 'oracle': "L'Oracle"},
           'en': {c: f'The {class_label("en", c)}' for c in CLASSES}}
ORDER = ['builder', 'energist', 'theorist', 'admiral', 'navigator', 'shadow', 'archivist', 'veteran', 'symbiote', 'oracle']  # ordre du jeu
DYN = {d: LABELS['fr']['dynasties'][d]['name'] for d in DATA['dynasties']}


def dyn_name(lang, d):
    return clean(LABELS[lang]['dynasties'][d]['name'])


def exclusive(lang, d):
    return [c for c in ORDER if DATA['classes'][c]['exclusive_to'] == d]


def link(lang, c):
    return f'[{ARTICLE[lang][c]}](/{lang}/dynasty/classes/{c})'


def index(lang):
    common = [c for c in ORDER if DATA['classes'][c]['exclusive_to'] is None]
    lines = [f'- {link(lang, c)}' + ('' if DATA['classes'][c]['exclusive_to'] is None else f" ({dyn_name(lang, DATA['classes'][c]['exclusive_to'])})") for c in common + [c for c in ORDER if c not in common]]
    if lang == 'fr':
        return f'''# Dynastie et talents

**Dynasties, classes, arbre commun et arbres de classe.**

> **En bref** : dans chaque univers, vous incarnez une **dynastie** et une **classe** prise dans cette dynastie. La dynastie donne deux traits passifs. La classe porte un arbre de talents fait de mécaniques qui lui sont propres. Tout le monde a en plus un **arbre commun**, qui grandit avec votre niveau et règle votre propre vitesse de jeu : production, recherche ou flotte.
{{.is-info}}

| | Dynastie | Classe | Arbre commun |
|---|---|---|---|
| Ce qu'elle donne | 2 traits passifs, 2 classes exclusives | un arbre de talents propre à la classe | les bonus génériques |
| Se choisit | une fois par univers | parmi les classes de votre dynastie | |
| Change | jamais dans l'univers | {COST} Points stellaires, une fois tous les {DAYS} jours | n'est jamais vidé par un changement de classe |
| Points | | 1 point par 2 niveaux de maîtrise, arrondi au supérieur, {KMAX} au maximum | 1 point par niveau, {CMAX} au maximum |

## Pages de cette rubrique

- [Les dynasties](/fr/dynasty/dynasties)
- [Les classes](/fr/dynasty/classes)
- [Les talents : points, portes et réinitialisation](/fr/dynasty/talents)
- [L'arbre commun](/fr/dynasty/common-tree)

### Arbres de classe

''' + '\n'.join(lines) + '\n'
    return f'''# Dynasty and talents

**Dynasties, classes, the common tree and the class trees.**

> **In short**: in each universe, you embody a **dynasty** and a **class** taken from that dynasty. The dynasty gives two passive traits. The class carries a talent tree made of mechanics of its own. Everyone also has a **common tree**, which grows with your level and sets your own pace: production, research or fleet.
{{.is-info}}

| | Dynasty | Class | Common tree |
|---|---|---|---|
| What it gives | 2 passive traits, 2 exclusive classes | a talent tree specific to the class | the generic bonuses |
| Chosen | once per universe | among your dynasty's classes | |
| Changes | never in the universe | {COST} Stellar Points, once every {DAYS} days | never emptied by a class change |
| Points | | 1 point per 2 mastery levels, rounded up, {KMAX} at most | 1 point per level, {CMAX} at most |

## Pages in this section

- [The dynasties](/en/dynasty/dynasties)
- [The classes](/en/dynasty/classes)
- [Talents: points, gates and resets](/en/dynasty/talents)
- [The common tree](/en/dynasty/common-tree)

### Class trees

''' + '\n'.join(lines) + '\n'


def dynasties(lang):
    L = LABELS[lang]['dynasties']
    tr = L['traits']
    h, ac = 'heritage', 'accord'
    ex = {d: ', '.join(link(lang, c).replace(ARTICLE[lang][c], class_label(lang, c)) for c in exclusive(lang, d)) for d in (h, ac)}
    refund, rebuild = TC['NOTHING_IS_LOST_REFUND_POINTS'], TC['NOTHING_IS_LOST_DEFENSE_REPAIR_POINTS']
    halden, fork, far = TC['HALDEN_ROTATION_PRODUCTION_PERCENT'], TC['TUNING_FORK_COUNTER_DAMAGE_PERCENT'], TC['FAR_LISTENING_FLEET_TIERS_EARLIER']
    mine = 10000
    if lang == 'fr':
        return f'''# Les dynasties

> **En bref** : la dynastie est le peuple dont vient votre personnage. Vous la choisissez une fois par univers et elle ne change plus. Elle vous donne deux traits passifs dès la première minute, et deux classes que les autres dynasties ne peuvent pas prendre.
{{.is-info}}

## Règles

1. La dynastie se choisit **une fois par univers**, avec votre première classe. Elle ne peut plus être changée dans cet univers.
2. Chaque dynastie donne **deux traits passifs**, actifs dès la première minute, sans rien à débloquer.
3. Chaque dynastie ouvre **deux classes exclusives**, en plus des six classes communes. Voir [Les classes](/fr/dynasty/classes).
4. Un trait s'ajoute **au-delà du plafond de vos talents** : une branche jouée jusqu'à son plafond ne l'absorbe pas. Le **plafond total**, talents d'alliance compris, reste le même pour tout le monde.
5. Les traits s'ajoutent aux talents d'alliance qui touchent le même bonus.
6. Tant que vous n'avez pas choisi de dynastie, vous n'avez aucun trait.

## Les trois dynasties

| Dynastie | Devise | Traits | Classes exclusives | Jouable |
|---|---|---|---|---|
| **{dyn_name(lang, h)}** | « {clean(L[h]['motto'])} » | {tr['nothing_is_lost']['name']}, {tr['halden_rotation']['name']} | {ex[h]} | oui |
| **{dyn_name(lang, ac)}** | « {clean(L[ac]['motto'])} » | {tr['tuning_fork']['name']}, {tr['far_listening']['name']} | {ex[ac]} | oui |
| **{dyn_name(lang, 'choir')}** | « {clean(L['choir']['motto'])} » | | deux classes prévues, sans arbre | pas encore |

### {dyn_name(lang, h)}

*{clean(L[h]['people'])}.* Quand l'Ancienne Terre est devenue inhabitable, ce qui a été emporté n'était ni l'or ni les armes : c'étaient les archives. L'Héritage ne gagne pas parce qu'il invente le plus vite, mais parce qu'il répare, récupère et recommence plus longtemps que les autres.

| Trait | Effet | Valeur |
|---|---|---|
| **{tr['nothing_is_lost']['name']}** | {tr['nothing_is_lost']['description']} | remboursement d'une construction annulée +{refund} points (80 → {80 + refund} %) ; reconstruction gratuite des défenses +{rebuild} points (70 → {70 + rebuild} %) |
| **{tr['halden_rotation']['name']}** | {tr['halden_rotation']['description']} | production des trois mines +{halden} % |

### {dyn_name(lang, ac)}

*{clean(L[ac]['people'])}.* L'Accord n'est pas une espèce, c'est un protocole : se mettre au diapason plutôt que se soumettre. Il ne construit pas plus vite : il attend mieux, écoute plus loin et s'adapte à ce que les autres subissent.

| Trait | Effet | Valeur |
|---|---|---|
| **{tr['tuning_fork']['name']}** | {tr['tuning_fork']['description']} Concrètement : un tir fait plus de dégâts contre les unités sur lesquelles le vaisseau qui tire a un tir rapide. | +{fork} % de dégâts |
| **{tr['far_listening']['name']}** | {tr['far_listening']['description']} Aucune autre section du rapport ne change. | {far} palier |

### {dyn_name(lang, 'choir')}

{dyn_name(lang, 'choir')} n'est pas encore jouable : ses personnages existent comme avatars de boutique, mais personne ne peut l'incarner. Ses deux classes exclusives n'ont pas encore d'arbre.

## Exemple chiffré

**{tr['nothing_is_lost']['name']} et la reconstruction des défenses**
- Une attaque détruit 100 Projecteurs balistiques sur votre planète.
- Sans le trait, chacun a 70 % de chances d'être reconstruit : environ **70** reviennent.
- Avec {tr['nothing_is_lost']['name']}, la chance passe à {70 + rebuild} % : environ **{70 + rebuild}** reviennent.

**{tr['halden_rotation']['name']}**
- Un Excavateur minéral qui produit {n(mine, lang)} métal par heure en produit **{n(mine * (100 + halden) / 100, lang)}** avec le trait (+{halden} %).

## Pièges fréquents

- **Choisir sa dynastie pour un trait seulement** : les traits sont petits. Ce sont les deux classes exclusives qui font la différence. Regardez d'abord quelle classe vous voulez jouer.
- **Croire qu'un trait relève le plafond total** : il passe au-delà du plafond de vos talents, mais le plafond total avec l'alliance est le même pour tout le monde.
- **Croire qu'on peut changer de dynastie** : seule la classe change. Pour une autre dynastie, il faut un autre univers.

## Pages liées

- [Les classes](/fr/dynasty/classes)
- [Les talents](/fr/dynasty/talents)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Files de construction](/fr/economy/build-queue)
- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Tirs rapides](/fr/fleet/rapid-fire)
'''
    return f'''# The dynasties

> **In short**: the dynasty is the people your character comes from. You choose it once per universe and it never changes. It gives you two passive traits from the first minute, and two classes that the other dynasties cannot take.
{{.is-info}}

## Rules

1. The dynasty is chosen **once per universe**, together with your first class. It can no longer be changed in that universe.
2. Each dynasty gives **two passive traits**, active from the first minute, with nothing to unlock.
3. Each dynasty opens **two exclusive classes**, on top of the six common classes. See [The classes](/en/dynasty/classes).
4. A trait adds **past the cap of your talents**: a branch played up to its cap never swallows it. The **total cap**, alliance talents included, stays the same for everyone.
5. Traits add up with the alliance talents that touch the same bonus.
6. As long as you have not chosen a dynasty, you have no trait.

## The three dynasties

| Dynasty | Motto | Traits | Exclusive classes | Playable |
|---|---|---|---|---|
| **{dyn_name(lang, h)}** | "{clean(L[h]['motto'])}" | {tr['nothing_is_lost']['name']}, {tr['halden_rotation']['name']} | {ex[h]} | yes |
| **{dyn_name(lang, ac)}** | "{clean(L[ac]['motto'])}" | {tr['tuning_fork']['name']}, {tr['far_listening']['name']} | {ex[ac]} | yes |
| **{dyn_name(lang, 'choir')}** | "{clean(L['choir']['motto'])}" | | two classes planned, without a tree | not yet |

### {dyn_name(lang, h)}

*{clean(L[h]['people'])}.* When Old Earth became uninhabitable, what was carried away was neither gold nor weapons: it was the archives. The Heritage does not win because it invents fastest, but because it repairs, salvages and starts over longer than anyone else.

| Trait | Effect | Value |
|---|---|---|
| **{tr['nothing_is_lost']['name']}** | {tr['nothing_is_lost']['description']} | refund of a cancelled construction +{refund} points (80 → {80 + refund}%); free defence rebuild +{rebuild} points (70 → {70 + rebuild}%) |
| **{tr['halden_rotation']['name']}** | {tr['halden_rotation']['description']} | production of the three mines +{halden}% |

### {dyn_name(lang, ac)}

*{clean(L[ac]['people'])}.* The Accord is not a species, it is a protocol: tuning in rather than submitting. It does not build faster: it waits better, listens further and adapts to what others endure.

| Trait | Effect | Value |
|---|---|---|
| **{tr['tuning_fork']['name']}** | {tr['tuning_fork']['description']} In practice: a shot deals more damage to the units the firing ship has rapid fire against. | +{fork}% damage |
| **{tr['far_listening']['name']}** | {tr['far_listening']['description']} No other section of the report changes. | {far} tier |

### {dyn_name(lang, 'choir')}

{dyn_name(lang, 'choir')} is not playable yet: its characters exist as shop avatars, but nobody can embody it. Its two exclusive classes have no tree yet.

## Worked example

**{tr['nothing_is_lost']['name']} and the defence rebuild**
- An attack destroys 100 Ballistic Projectors on your planet.
- Without the trait, each has a 70% chance of being rebuilt: about **70** come back.
- With {tr['nothing_is_lost']['name']}, the chance rises to {70 + rebuild}%: about **{70 + rebuild}** come back.

**{tr['halden_rotation']['name']}**
- A Mineral Excavator producing {n(mine, lang)} metal per hour produces **{n(mine * (100 + halden) / 100, lang)}** with the trait (+{halden}%).

## Common pitfalls

- **Choosing a dynasty for a trait alone**: traits are small. The two exclusive classes make the difference. Look first at which class you want to play.
- **Thinking a trait raises the total cap**: it goes past the cap of your talents, but the total cap with the alliance is the same for everyone.
- **Thinking you can change dynasty**: only the class changes. For another dynasty, you need another universe.

## Related pages

- [The classes](/en/dynasty/classes)
- [Talents](/en/dynasty/talents)
- [Defence rebuild](/en/combat/defense-rebuild)
- [Build queues](/en/economy/build-queue)
- [Reading a spy report](/en/espionage/spy-report)
- [Rapid fire](/en/fleet/rapid-fire)
'''


def classes(lang):
    rows = []
    for c in ORDER:
        d = DATA['classes'][c]['exclusive_to']
        avail = ('toutes les dynasties' if lang == 'fr' else 'every dynasty') if d is None else dyn_name(lang, d)
        rows.append([link(lang, c), class_label(lang, c, 'motto'), avail, ', '.join(branch_name(lang, b['key']) for b in tree(c))])
    # Exemple : Bâtisseur joué depuis le début, niveau 30 ; passage à l'Amiral jamais joué.
    lvl = 30
    pts = min(KMAX, (lvl + 1) // 2)
    if lang == 'fr':
        tbl = table(['Classe', 'Devise', 'Disponible pour', 'Branches'], rows)
        return f'''# Les classes

> **En bref** : la classe est votre manière de jouer. Elle porte un arbre de talents fait de mécaniques que personne d'autre n'a. Six classes sont ouvertes à toutes les dynasties, quatre sont réservées à une seule. Vous pouvez changer de classe, dans votre dynastie, une fois tous les {DAYS} jours.
{{.is-info}}

## Règles

1. Vous choisissez votre classe **parmi celles de votre dynastie** : les six classes communes et les deux exclusives de votre dynastie.
2. La classe porte l'**arbre de classe** : 3 branches de 9 rangées. Voir [Les talents](/fr/dynasty/talents).
3. Chaque mécanique n'a **qu'une classe propriétaire** : le combat de flotte appartient à l'Amiral, les défenses et les missiles au Vétéran, le recyclage hors combat à l'Archiviste, le manque d'énergie à l'Énergéticien, le pistage des espions à l'Ombre.
4. Les bonus génériques (production, recherche, vitesse de flotte…) sont dans l'[arbre commun](/fr/dynasty/common-tree), le même pour toutes les classes. Une classe ne peut les pousser que sur un périmètre étroit : c'est un **accent** (voir [Les talents](/fr/dynasty/talents#plafonds-des-bonus-partagés)).

## Les dix classes

{tbl}

## Maîtrise de classe

5. La **maîtrise** mesure votre expérience dans la classe que vous jouez. Elle donne les points de l'arbre de classe : **1 point par 2 niveaux de maîtrise**, arrondi au supérieur, **{KMAX} au maximum**.
6. La **première classe** choisie dans l'univers a sa maîtrise **au niveau de votre personnage**, même si vous l'avez choisie tard : toute votre expérience compte.
7. Une classe prise ensuite part de sa propre maîtrise et monte avec l'expérience que vous gagnez à partir de ce moment, en suivant la même courbe que votre niveau : rattraper demande le même effort que monter de niveau.
8. La maîtrise **ne dépasse jamais votre niveau**, ni le niveau 50.
9. Une classe jamais jouée est à 0. Elle passe au niveau 1 dès votre première expérience dans cette classe.
10. Chaque classe **garde sa maîtrise** : revenir à une classe déjà jouée reprend là où vous l'aviez laissée.

## Changer de classe

11. Vous pouvez prendre une autre classe **de votre dynastie** pour **{COST} Points stellaires**.
12. Un changement n'est possible qu'**une fois tous les {DAYS} jours**.
13. Il est refusé en **mode vacances**, tant qu'une **flotte ennemie** se dirige vers l'une de vos planètes, et tant qu'une de vos **flottes d'attaque** est en route vers sa cible (pas au retour).
14. L'**arbre de classe est vidé** : tous ses points vous reviennent. Vos nouveaux points de classe dépendent de la maîtrise de la nouvelle classe. Sa prochaine réinitialisation redevient gratuite.
15. L'**arbre commun ne bouge pas**.
16. La dynastie ne change jamais.

## Exemple chiffré

**Changer de classe au niveau {lvl}**
- Vous jouez le Bâtisseur depuis le début : maîtrise {lvl}, soit **{pts} points** de classe.
- Vous passez à l'Amiral, jamais joué : maîtrise 0, **0 point**. Votre arbre commun garde ses {lvl} points. Vous payez {COST} Points stellaires.
- Votre première expérience comme Amiral le met au niveau de maîtrise 1 : **1 point**. Il monte ensuite avec l'expérience gagnée, sans dépasser votre niveau.
- Si vous revenez au Bâtisseur {DAYS} jours plus tard, il reprend sa maîtrise de {lvl} et monte à partir de là.

## Pièges fréquents

- **Changer de classe pour essayer** : l'arbre de classe repart presque de zéro avec une classe neuve. Lisez d'abord sa page.
- **Oublier le délai** : après un changement, il faut attendre {DAYS} jours avant le suivant.
- **Changer pendant un raid** : une flotte ennemie en approche, ou l'une de vos attaques en route, bloque le changement jusqu'à l'impact.
- **Croire que l'arbre commun est perdu** : il ne bouge jamais quand vous changez de classe.

## Pages liées

- [Les dynasties](/fr/dynasty/dynasties)
- [Les talents](/fr/dynasty/talents)
- [L'arbre commun](/fr/dynasty/common-tree)
- [Premium, boutique, Points stellaires](/fr/misc/premium)
'''
    tbl = table(['Class', 'Motto', 'Available to', 'Branches'], rows)
    return f'''# The classes

> **In short**: the class is your way of playing. It carries a talent tree made of mechanics nobody else has. Six classes are open to every dynasty, four are reserved to a single one. You can change class, within your dynasty, once every {DAYS} days.
{{.is-info}}

## Rules

1. You choose your class **among your dynasty's classes**: the six common classes and your dynasty's two exclusive ones.
2. The class carries the **class tree**: 3 branches of 9 rows. See [Talents](/en/dynasty/talents).
3. Each mechanic has **a single owning class**: fleet combat belongs to the Admiral, defences and missiles to the Veteran, recycling outside combat to the Archivist, energy shortage to the Energetician, tracing spies to the Shadow.
4. The generic bonuses (production, research, fleet speed…) are in the [common tree](/en/dynasty/common-tree), the same for every class. A class may push them only on a narrow scope: an **accent** (see [Talents](/en/dynasty/talents#caps-of-the-shared-bonuses)).

## The ten classes

{tbl}

## Class mastery

5. **Mastery** measures your experience in the class you play. It gives the class tree's points: **1 point per 2 mastery levels**, rounded up, **{KMAX} at most**.
6. The **first class** chosen in the universe has its mastery **at your character's level**, even if you chose it late: all your experience counts.
7. A class taken later starts from its own mastery and grows with the experience you earn from then on, along the same curve as your level: catching up takes the same effort as levelling up.
8. Mastery **never exceeds your level**, nor level 50.
9. A class never played is at 0. It reaches level 1 with your first experience in that class.
10. Each class **keeps its mastery**: going back to a class already played resumes where you left it.

## Changing class

11. You can take another class **of your dynasty** for **{COST} Stellar Points**.
12. A change is only possible **once every {DAYS} days**.
13. It is refused in **vacation mode**, while an **enemy fleet** is heading for one of your planets, and while one of your **attack fleets** is on its way to its target (not on the way back).
14. The **class tree is emptied**: all its points come back to you. Your new class points depend on the new class's mastery. Its next reset becomes free again.
15. The **common tree does not move**.
16. The dynasty never changes.

## Worked example

**Changing class at level {lvl}**
- You have played the Builder from the start: mastery {lvl}, that is **{pts} class points**.
- You switch to the Admiral, never played: mastery 0, **0 points**. Your common tree keeps its {lvl} points. You pay {COST} Stellar Points.
- Your first experience as an Admiral brings it to mastery level 1: **1 point**. It then grows with the experience earned, never past your level.
- If you go back to the Builder {DAYS} days later, it resumes its mastery of {lvl} and grows from there.

## Common pitfalls

- **Changing class to try it out**: the class tree starts almost from scratch with a new class. Read its page first.
- **Forgetting the delay**: after a change, you must wait {DAYS} days before the next one.
- **Changing during a raid**: an incoming enemy fleet, or one of your attacks on its way, blocks the change until impact.
- **Thinking the common tree is lost**: it never moves when you change class.

## Related pages

- [The dynasties](/en/dynasty/dynasties)
- [Talents](/en/dynasty/talents)
- [The common tree](/en/dynasty/common-tree)
- [Premium, shop, Stellar Points](/en/misc/premium)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'dynasty', index(lang))
        write(lang, 'dynasty/dynasties', dynasties(lang))
        write(lang, 'dynasty/classes', classes(lang))
