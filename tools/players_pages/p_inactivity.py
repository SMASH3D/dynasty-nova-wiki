import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *

ME, BIG = 300, 50_000
assert blocks(BIG, ME) and not blocks(BIG, ME, inactive_defender=True)

def body(lang):
    N = lambda x: n(x, lang)
    a1, a2 = FOUNDER_ALERTS
    if lang == 'fr':
        box = setting_box('fr', 'le délai d\'inactivité peut être différent selon l\'univers ; 0 désactive l\'inactivité.', f'**{INACTIVITY_DEFAULT} jours**', f'**{INACTIVITY_REDLINE} jours**')
        return f'''# Inactivité

> **En bref** : un joueur qui ne se montre pas dans un univers pendant plus que le délai d'inactivité ({INACTIVITY_REDLINE} jours sur Redline) perd sa protection par points et devient attaquable par tous. Il n'y a pas d'autre palier : pas de suppression de compte, pas d'abandon automatique des planètes.
{{.is-info}}

{box}

## Règles

1. Vous devenez **inactif** dans un univers quand votre dernière activité dans cet univers remonte à **plus de {INACTIVITY_REDLINE} jours** sur Redline ({INACTIVITY_DEFAULT} par défaut).
2. **Toute visite compte comme activité** : ouvrir un écran, changer de planète, regarder la galaxie suffit. L'activité est enregistrée pour l'univers où vous jouez à ce moment-là : jouer dans un autre univers ne compte pas pour celui-ci.
3. **Effet** : un joueur inactif perd sa [protection par points](/fr/players/beginner-protection). N'importe qui peut l'attaquer, quel que soit l'écart, y compris un joueur beaucoup plus petit que lui.
4. Seule l'inactivité du **défenseur** compte. Dès que vous revenez, vous êtes de nouveau actif et protégé.
5. C'est le **seul effet** sur votre empire : le compte n'est pas supprimé et les planètes ne sont pas abandonnées.
6. La [protection nouvel arrivant](/fr/players/beginner-protection) ne dépend pas de l'activité : elle dure {NEWCOMER_DAYS} jours, que vous jouiez ou non.
7. En [mode vacances](/fr/players/vacation-mode), personne ne peut vous attaquer, inactif ou non. À votre retour, votre activité est de nouveau enregistrée.
8. **Fondateur d'alliance** : un fondateur absent est signalé à l'alliance au bout de **{a1} jours**, puis de **{a2} jours**, et **perd sa place à {FOUNDER_LOSS_DAYS} jours** au profit d'un successeur. Ces délais sont les mêmes dans tous les univers, et les jours de vacances comptent (voir [Alliances](/fr/players/alliances)).
9. Les joueurs non humains (PvE) ne sont jamais inactifs.

## Exemple chiffré

Sur Redline, vous avez {N(ME)} points et partez trois semaines sans activer le mode vacances. Votre dernière visite date d'un lundi à 20:00.
- Jusqu'au lundi suivant 20:00, un joueur de {N(BIG)} points ne peut pas vous attaquer : il a plus de 3 fois vos points (palier 1:3).
- Passé le lundi suivant 20:00 ({INACTIVITY_REDLINE} jours), vous êtes inactif : ce joueur peut vous attaquer.
- Vous ne pouvez toujours pas l'attaquer, lui : il est actif, et l'écart le protège.
- Si vous fondez une alliance, l'alliance est prévenue au {a1}e puis au {a2}e jour, et votre place passe à un autre membre au {FOUNDER_LOSS_DAYS}e.

## Pièges fréquents

- **Une longue absence se prépare** : activez le mode vacances, sinon vous perdez votre protection au bout de {INACTIVITY_REDLINE} jours sur Redline.
- **Jouer ailleurs ne suffit pas** : l'activité se compte univers par univers.
- **Fondateur d'alliance, prévenez** : au bout de {FOUNDER_LOSS_DAYS} jours, même en vacances, votre place passe à un autre membre.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Mode vacances](/fr/players/vacation-mode)
- [Alliances](/fr/players/alliances)
'''
    box = setting_box('en', 'the inactivity delay may differ from one universe to another; 0 turns inactivity off.', f'**{INACTIVITY_DEFAULT} days**', f'**{INACTIVITY_REDLINE} days**')
    return f'''# Inactivity

> **In short**: a player who does not show up in a universe for longer than the inactivity delay ({INACTIVITY_REDLINE} days on Redline) loses their point protection and becomes attackable by anyone. There is no other stage: no account deletion, no automatic abandonment of planets.
{{.is-info}}

{box}

## Rules

1. You become **inactive** in a universe when your last activity there is **more than {INACTIVITY_REDLINE} days** old on Redline ({INACTIVITY_DEFAULT} by default).
2. **Any visit counts as activity**: opening a screen, switching planet or looking at the galaxy is enough. Activity is recorded for the universe you are playing in at that moment: playing in another universe does not count for this one.
3. **Effect**: an inactive player loses their [point protection](/en/players/beginner-protection). Anyone may attack them, whatever the gap, including a much smaller player.
4. Only the **defender's** inactivity counts. As soon as you come back, you are active and protected again.
5. That is the **only effect** on your empire: the account is not deleted and planets are not abandoned.
6. [Newcomer protection](/en/players/beginner-protection) does not depend on activity: it lasts {NEWCOMER_DAYS} days, whether you play or not.
7. In [vacation mode](/en/players/vacation-mode), nobody can attack you, inactive or not. On your return, your activity is recorded again.
8. **Alliance founder**: an absent founder is flagged to the alliance after **{a1} days**, then **{a2} days**, and **loses their seat at {FOUNDER_LOSS_DAYS} days** to a successor. These delays are the same in every universe, and vacation days count (see [Alliances](/en/players/alliances)).
9. Non-human (PvE) players are never inactive.

## Worked example

On Redline, you have {N(ME)} points and leave for three weeks without turning on vacation mode. Your last visit was on a Monday at 20:00.
- Until the following Monday 20:00, a {N(BIG)}-point player cannot attack you: they have more than 3 times your points (1:3 tier).
- After the following Monday 20:00 ({INACTIVITY_REDLINE} days), you are inactive: that player may attack you.
- You still cannot attack them: they are active, and the gap protects them.
- If you founded an alliance, the alliance is warned on day {a1} and then day {a2}, and your seat goes to another member on day {FOUNDER_LOSS_DAYS}.

## Common pitfalls

- **Plan a long absence**: turn on vacation mode, otherwise you lose your protection after {INACTIVITY_REDLINE} days on Redline.
- **Playing elsewhere is not enough**: activity is counted universe by universe.
- **Alliance founders, hand over**: after {FOUNDER_LOSS_DAYS} days, even on vacation, your seat goes to another member.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Vacation mode](/en/players/vacation-mode)
- [Alliances](/en/players/alliances)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/inactivity', body(lang))
