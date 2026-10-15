from combat_lib import *
from write import write

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    dm, dc = debris({'heavy_fighter': 3})
    ch = moon_chance(dm + dc)
    if lang == 'fr':
        return f'''# Lire un rapport de combat

> **En bref** : après chaque combat, l'attaquant et le défenseur reçoivent un rapport de combat. Il donne les forces engagées de chaque camp, le déroulé round par round, les pertes et les survivants, le résultat, puis les suites : ressources pillées, champ de ruines et formation de lune. L'attaquant ne voit que les unités qu'il a réellement affrontées.
{{.is-info}}

## Règles

### Qui reçoit quoi
1. Chaque combat produit **un rapport pour chaque camp**. Il arrive toujours : les rapports de combat ne se désactivent pas dans les réglages.
2. Le rapport donne les **coordonnées du combat** et celles **d'où venait l'attaque**, aux deux camps.
3. Une attaque sur une **planète abandonnée** ne produit qu'un rapport, celui de l'attaquant, sans nom d'adversaire.

### Contenu
4. **Résultat** : Victoire, Défaite ou Match nul, vu de votre camp.
5. **Forces engagées** : pour chaque camp, les unités au début du combat.
6. **Déroulé du combat** : pour chaque round, les pertes de chaque camp.
7. **Pertes** et **survivants** de chaque camp.
8. **Ressources gagnées** (attaquant) ou **Ressources perdues** (défenseur) : le butin réellement emporté, voir [Pillage](/fr/combat/plunder).
9. **Champ de ruines** : le métal et le cristal laissés en orbite par ce combat, voir [Champs de ruines](/fr/combat/debris).
10. **Formation de lune** : la chance obtenue par ce combat, et le diamètre de la lune si elle s'est formée. La chance est affichée même quand la lune ne se forme pas.

### Vue partielle de l'attaquant
11. L'attaquant ne voit que les **unités adverses que sa flotte a réellement croisées** : celles qui ont tiré sur elle ou sur lesquelles elle a tiré. Le reste de la base n'apparaît pas, et le rapport porte la mention « Vue partielle ».
12. Sur la vue partielle, l'attaquant ne voit pas non plus les forces restantes du défenseur à chaque round.
13. Le défenseur voit tout le combat : il a vu la flotte arriver.

### Ce que seul votre camp voit
14. Le défenseur voit les vaisseaux repris par sa [Station de réparation](/fr/economy/repair-station), sous « Épave récupérée » : ils sont comptés dans les pertes, mais reviendront une fois réparés.
15. Les effets de vos talents de dynastie et de classe apparaissent dans votre rapport seulement (débris chargés en combat, seconde vague, ressources rendues pour les défenses perdues…).
16. Les défenses reconstruites gratuitement après le combat ne sont pas listées : elles sont de nouveau sur la planète. Voir [Reconstruction des défenses](/fr/combat/defense-rebuild).

### Partager
17. **Partager dans l'alliance** : le message ne porte qu'un lien vers le rapport, que chaque membre ouvre avec ses propres droits. Il reste 30 jours dans le canal.
18. **Lien public** (« Exposer ce combat ») : une vitrine que tout le monde peut ouvrir, sans coordonnées, sans nom de planète, sans détail unité par unité, sans débris ni heure du combat. L'adversaire est prévenu et peut masquer son nom. 10 publications au plus par 24 h.

### Destruction de lune
19. Une mission Destruction de lune produit un rapport à part, « Destruction de lune » : voir [Destruction de lune](/fr/combat/moon-destruction).

## Exemple chiffré

Vous attaquez avec 20 Assaillants et 5 Cargos stellaires une planète défendue par 10 Projecteurs balistiques, sans flotte. Votre rapport indique :
- Résultat : Victoire.
- Vos pertes : 3 Assaillants. Survivants : 17 Assaillants et 5 Cargos stellaires.
- Défenseur : 10 Projecteurs balistiques engagés, 10 perdus.
- Champ de ruines : {P(DEBRIS_SHIPS)} de 3 × ({N(6000)} métal + {N(4000)} cristal), soit **{N(dm)} métal et {N(dc)} cristal**. Les Projecteurs détruits ne laissent aucun débris.
- Formation de lune : {N(dm + dc)} débris, sous le seuil de {N(MOON_DEBRIS_FOR_MAX // MOON_MAX)} : chance de **{P(ch)}**.
- Le défenseur verra ensuite revenir environ 7 Projecteurs sur 10 (tirage de 70 % par unité), sans que votre rapport le montre.

## Pièges fréquents

- **Les pertes affichées peuvent revenir** : côté défenseur, les vaisseaux repris par la Station de réparation sont comptés dans les pertes.
- **Une vue partielle n'est pas un espionnage** : ce que votre flotte n'a pas croisé reste inconnu. Pour voir toute la base, [espionnez-la](/fr/espionage/spying).
- **Un match nul ne rapporte rien** : pas de butin.

## Pages liées

- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Pillage](/fr/combat/plunder)
- [Champs de ruines](/fr/combat/debris)
- [Reconstruction des défenses](/fr/combat/defense-rebuild)
- [Station de réparation](/fr/economy/repair-station)
- [Messagerie et rapports](/fr/players/messages-and-reports)
'''
    return f'''# Reading a battle report

> **In short**: after each battle, the attacker and the defender each receive a battle report. It gives each side's forces engaged, the round-by-round log, losses and survivors, the outcome, then what followed: resources plundered, debris field and moon formation. The attacker only sees the units it actually faced.
{{.is-info}}

## Rules

### Who gets what
1. Each battle produces **one report for each side**. It always arrives: battle reports cannot be turned off in the settings.
2. The report gives the **coordinates of the battle** and **where the attack came from**, to both sides.
3. An attack on an **abandoned planet** produces only one report, the attacker's, with no opponent name.

### Contents
4. **Outcome**: Victory, Defeat or Draw, from your side's point of view.
5. **Forces engaged**: for each side, the units at the start of the battle.
6. **Battle log**: for each round, each side's losses.
7. Each side's **losses** and **survivors**.
8. **Resources gained** (attacker) or **Resources lost** (defender): the loot actually carried away, see [Plunder](/en/combat/plunder).
9. **Debris field**: the metal and crystal this battle left in orbit, see [Debris fields](/en/combat/debris).
10. **Moon formation**: the chance this battle obtained, and the moon's diameter if one formed. The chance is shown even when no moon forms.

### The attacker's partial view
11. The attacker only sees the **enemy units its fleet actually engaged**: those that fired at it or that it fired at. The rest of the base does not appear, and the report carries the "Partial view" notice.
12. On a partial view, the attacker does not see the defender's remaining forces at each round either.
13. The defender sees the whole battle: it watched the fleet arrive.

### What only your side sees
14. The defender sees the ships taken back by its [Repair Station](/en/economy/repair-station), under "Salvaged wreckage": they count as losses, but will come back once repaired.
15. The effects of your dynasty and class talents appear in your own report only (debris loaded in battle, second wave, resources given back for defenses lost…).
16. Defenses rebuilt for free after the battle are not listed: they are back on the planet. See [Defense rebuild](/en/combat/defense-rebuild).

### Sharing
17. **Share with the alliance**: the message only carries a link to the report, which each member opens with their own rights. It stays 30 days in the channel.
18. **Public link** ("Show off this battle"): a showcase anyone can open, with no coordinates, no planet names, no unit-by-unit breakdown, no debris and no time of the battle. The opponent is told and can hide their name. At most 10 publications per 24 hours.

### Moon destruction
19. A Moon destruction mission produces a separate "Moon destruction" report: see [Moon destruction](/en/combat/moon-destruction).

## Worked example

You attack with 20 Assailants and 5 Stellar Freighters a planet defended by 10 Ballistic Projectors, with no fleet. Your report shows:
- Outcome: Victory.
- Your losses: 3 Assailants. Survivors: 17 Assailants and 5 Stellar Freighters.
- Defender: 10 Ballistic Projectors engaged, 10 lost.
- Debris field: {P(DEBRIS_SHIPS)} of 3 × ({N(6000)} metal + {N(4000)} crystal), so **{N(dm)} metal and {N(dc)} crystal**. The destroyed Projectors leave no debris.
- Moon formation: {N(dm + dc)} debris, below the {N(MOON_DEBRIS_FOR_MAX // MOON_MAX)} threshold: a **{P(ch)}** chance.
- The defender will then see about 7 Projectors out of 10 come back (a 70% roll per unit), which your report does not show.

Ship names are provisional translations: the game still shows the French names.

## Common pitfalls

- **Losses shown may come back**: on the defender's side, ships taken back by the Repair Station count as losses.
- **A partial view is not a spy report**: whatever your fleet did not meet stays unknown. To see the whole base, [spy on it](/en/espionage/spying).
- **A draw brings nothing**: no loot.

## Related pages

- [How combat works](/en/combat/how-combat-works)
- [Plunder](/en/combat/plunder)
- [Debris fields](/en/combat/debris)
- [Defense rebuild](/en/combat/defense-rebuild)
- [Repair Station](/en/economy/repair-station)
- [Messages and reports](/en/players/messages-and-reports)
'''

def run():
    write('fr', 'combat/battle-report', body('fr'))
    write('en', 'combat/battle-report', body('en'))
