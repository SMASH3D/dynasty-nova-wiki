import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *

DAYS = {'fr': ['Lundi', 'Mardi', 'Mercredi'], 'en': ['Monday', 'Tuesday', 'Wednesday']}
def hh(t, lang):
    d, h = divmod(10 + t, 24)
    return f'{DAYS[lang][d]} {h:02d}:00'

# (heure relative à lundi 10:00, action) ; rejoué avec la tranche du code
EVENTS = [(0, 'attack'), (2, 'attack'), (4, 'salvo'), (5, 'attack_recalled'), (8, 'attack'), (9, 'attack'), (10, 'attack'), (13, 'attack'), (24, 'reset'), (25, 'attack')]
LBL = {
 'fr': {'attack': 'Attaque de flotte', 'salvo': 'Salve de missiles', 'attack_recalled': 'Attaque de flotte, rappelée une heure plus tard', 'refused': 'Attaque de flotte : **refusée à l\'envoi**', 'reset': 'La tranche est écoulée', 'open': ' (la tranche s\'ouvre jusqu\'à {end})'},
 'en': {'attack': 'Fleet attack', 'salvo': 'Missile salvo', 'attack_recalled': 'Fleet attack, recalled one hour later', 'refused': 'Fleet attack: **refused at sending**', 'reset': 'The window has elapsed', 'open': ' (the window opens until {end})'},
}
def timeline(lang):
    T, rows = Tally(), []
    for t, ev in EVENTS:
        if ev == 'reset':
            rows.append([hh(t, lang), LBL[lang]['reset'], T.remaining(t)]); continue
        start_before = T.start
        ok = T.attack(t)
        label = LBL[lang][ev] if ok else LBL[lang]['refused']
        if ok and T.start != start_before:
            end = hh(T.start + BASH_WINDOW_H, lang); label += LBL[lang]['open'].format(end=end[0].lower() + end[1:] if lang == 'fr' else end)
        if ev == 'attack_recalled':
            T.refund()
            label += ' : créneau rendu' if lang == 'fr' else ': slot given back'
        rows.append([hh(t, lang), label, T.remaining(t)])
    return rows

def body(lang):
    N = lambda x: n(x, lang)
    if lang == 'fr':
        box = setting_box('fr', 'le nombre d\'attaques et la durée de la tranche peuvent être différents selon l\'univers ; un maximum de 0 désactive la règle.',
                          f'**{BASH_MAX} attaques par {BASH_WINDOW_H} h**', f'**{BASH_REDLINE[0]} attaques par {BASH_REDLINE[1]} h**')
        return f'''# Limite d'attaques

> **En bref** : vous pouvez attaquer un même joueur au plus **{BASH_MAX} fois par tranche de {BASH_WINDOW_H} heures**, toutes ses planètes et lunes confondues, salves de missiles comprises. La tranche s'ouvre à votre première attaque contre lui et ne glisse pas. L'attaque de trop est refusée dès l'envoi.
{{.is-info}}

{box}

## Règles

1. La limite porte sur **un couple attaquant et joueur visé** : toutes les planètes et lunes du joueur visé comptent ensemble. Chaque joueur que vous attaquez a son propre compteur.
2. Comptent : les **attaques de flotte** et les **salves de missiles** (une salve compte pour une attaque, quel que soit le nombre de missiles).
3. Ne comptent pas : l'espionnage, le transport, le stationnement, le recyclage et la destruction de lune. Quand votre quota contre un joueur est épuisé, la vue galaxie ne propose plus ni l'attaque, ni les missiles, ni la destruction de lune contre lui.
4. L'attaque est comptée **à l'envoi**. Celle qui dépasserait le maximum est **refusée à l'envoi**.
5. La **tranche est fixe** : elle s'ouvre à votre première attaque contre ce joueur et dure {BASH_WINDOW_H} heures. Une fois écoulée, le compteur repart à zéro, et l'attaque suivante ouvre une nouvelle tranche.
6. **Rappeler** une flotte d'attaque avant son arrivée rend le créneau. Une salve de missiles ne se rappelle pas : son créneau est consommé.
7. Les **planètes abandonnées** ne sont pas concernées : elles n'ont plus de propriétaire. Les joueurs non humains (PvE) le sont, comme les joueurs humains.
8. Les guerres et les pactes d'alliance ne changent rien à la limite. Les membres de votre propre alliance ne peuvent de toute façon pas être attaqués.
9. La vue galaxie affiche le nombre d'attaques qu'il vous reste contre chaque joueur.

## Exemple chiffré

Univers réglé à {BASH_MAX} attaques par {BASH_WINDOW_H} h, attaques contre un même joueur X :

{table(['Heure', 'Action contre X', 'Attaques restantes'], timeline('fr'))}

## Pièges fréquents

- **La tranche ne glisse pas** : elle part de votre première attaque, pas de la dernière. Mais elle ne se rouvre qu'à votre prochaine attaque.
- **Les missiles comptent** : une salve est une attaque à part entière, et elle ne se rappelle pas.
- **Toutes ses planètes comptent ensemble** : attaquer deux colonies d'un même joueur consomme deux créneaux.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Missiles](/fr/defense/missiles)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Pillage](/fr/combat/plunder)
'''
    box = setting_box('en', 'the number of attacks and the window length may differ from one universe to another; a maximum of 0 turns the rule off.',
                      f'**{BASH_MAX} attacks per {BASH_WINDOW_H} h**', f'**{BASH_REDLINE[0]} attacks per {BASH_REDLINE[1]} h**')
    return f'''# Attack limit

> **In short**: you may attack the same player at most **{BASH_MAX} times per {BASH_WINDOW_H}-hour window**, all their planets and moons together, missile salvos included. The window opens at your first attack on them and does not slide. The attack that would go over the limit is refused at sending.
{{.is-info}}

{box}

## Rules

1. The limit applies to **one attacker and one targeted player**: all the targeted player's planets and moons count together. Each player you attack has their own counter.
2. Counted: **fleet attacks** and **missile salvos** (a salvo counts as one attack, whatever the number of missiles).
3. Not counted: espionage, transport, stationing, recycling and moon destruction. Once your quota against a player is used up, the galaxy view no longer offers the attack, missiles or moon destruction against them.
4. The attack is counted **when it is sent**. The one that would go over the maximum is **refused at sending**.
5. The **window is fixed**: it opens at your first attack on that player and lasts {BASH_WINDOW_H} hours. Once it has elapsed the counter goes back to zero, and the next attack opens a new window.
6. **Recalling** an attack fleet before it arrives gives the slot back. A missile salvo cannot be recalled: its slot is used up.
7. **Abandoned planets** are not concerned: they no longer have an owner. Non-human (PvE) players are, like human players.
8. Alliance wars and pacts change nothing about the limit. Members of your own alliance cannot be attacked anyway.
9. The galaxy view shows how many attacks you have left against each player.

## Worked example

Universe set to {BASH_MAX} attacks per {BASH_WINDOW_H} h, attacks on the same player X:

{table(['Time', 'Action against X', 'Attacks left'], timeline('en'))}

## Common pitfalls

- **The window does not slide**: it starts at your first attack, not your last. But it only reopens with your next attack.
- **Missiles count**: a salvo is a full attack, and it cannot be recalled.
- **All their planets count together**: attacking two colonies of the same player uses two slots.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Missiles](/en/defense/missiles)
- [The galaxy view](/en/universe/galaxy-view)
- [Plunder](/en/combat/plunder)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/attack-limit', body(lang),
          description=f'{BASH_MAX} attaques sur un même joueur par tranche de {BASH_WINDOW_H} heures.' if lang == 'fr' else f'{BASH_MAX} attacks on the same player per {BASH_WINDOW_H}-hour window.')
