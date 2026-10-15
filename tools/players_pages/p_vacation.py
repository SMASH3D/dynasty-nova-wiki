import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *
from datetime import datetime, timedelta

START = datetime(2026, 10, 16, 18, 0)   # un vendredi
BACK = START + timedelta(hours=VACATION_MIN_H)
DFR = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
DEN = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def d(dt, lang): return f'{(DFR if lang == "fr" else DEN)[dt.weekday()]} {dt:%H:%M}'

def body(lang):
    N = lambda x: n(x, lang)
    if lang == 'fr':
        return f'''# Mode vacances

> **En bref** : le mode vacances met votre empire en pause dans un univers. Plus aucune production, plus aucune action de votre part, et personne ne peut vous atteindre. Il dure au moins {VACATION_MIN_H} heures, n'a pas de durée maximale et ne s'arrête que quand vous le décidez.
{{.is-info}}

## Règles

### Partir
1. Le mode vacances s'active **par univers**, dans les Paramètres (« Partir en vacances »). Vous pouvez être en vacances dans un univers et jouer dans un autre.
2. **Conditions de départ**, toutes nécessaires :
   - aucune de vos flottes n'est en vol ;
   - aucun ordre n'est en cours : bâtiment, recherche, vaisseaux ou défenses ;
   - aucune attaque n'est en approche.
   Tant qu'une condition manque, le bouton est grisé et le jeu dit ce qu'il faut attendre.
3. Au départ, chaque planète reçoit ce qu'elle a produit jusqu'à cet instant. Ensuite, la **production tombe à zéro** sur toutes vos planètes et lunes.

### Pendant les vacances
4. **Vous ne pouvez plus agir** dans cet univers : ni flotte, ni missile, ni construction, ni annulation, ni démolition, ni Phalange, ni convoi d'alliance. Vous pouvez toujours **consulter** la galaxie, vos rapports, la messagerie et votre alliance.
5. **Les autres joueurs** ne peuvent ni vous attaquer, ni détruire votre lune, ni vous transporter des ressources, ni vous tirer des missiles.
6. L'**espionnage** reste possible : les sondes partent et révèlent la case, mais le rapport dit seulement que le propriétaire est absent. Le **recyclage** des champs de ruines au-dessus de vos planètes reste possible aussi.
7. Vos planètes portent le statut « En vacances » (« (v) ») dans la vue galaxie, et votre fiche le badge « En vacances ».

### Revenir
8. **Séjour minimum : {VACATION_MIN_H} heures.** Ensuite, vous revenez quand vous voulez avec le bouton « Revenir ». Il n'y a **ni durée maximale, ni fin automatique, ni délai** avant de repartir.
9. Au retour, la production reprend à partir de cet instant : les jours d'absence ne rapportent rien.
10. Pendant les vacances, personne ne peut vous attaquer, inactif ou non. Votre activité est de nouveau enregistrée dès votre retour.
11. Ce qui continue de courir : la [protection nouvel arrivant](/fr/players/beginner-protection) (ses {NEWCOMER_DAYS} jours se comptent depuis votre arrivée) et, si vous **fondez une alliance**, le délai de succession : un fondateur absent perd sa place au bout de {FOUNDER_LOSS_DAYS} jours, vacances comprises (voir [Inactivité](/fr/players/inactivity)).

### Univers privé gelé
12. Un [univers privé](/fr/misc/private-universes) dont l'abonnement est interrompu est **gelé** : c'est un mode vacances pour tous ses joueurs à la fois, sans condition de départ.
13. Personne n'y agit ; on peut seulement consulter. La production s'arrête. Les attaques et espionnages en vol font demi-tour et rendent leur créneau de [limite d'attaques](/fr/players/attack-limit) ; les transports, les retours et les constructions déjà payées vont à leur terme.
14. Au dégel, le temps du gel est rendu : la dernière activité de chaque joueur, les échéances des votes d'alliance, les préavis des pactes dénoncés, les demandes d'aide et la durée de conservation des rapports sont repoussés d'autant. Ne sont pas repoussés : les cycles des missions d'alliance, la conservation des messages du canal d'alliance et la protection nouvel arrivant.

## Exemple chiffré

Vous partez le {d(START, 'fr')} :
- vous pouvez revenir à partir du **{d(BACK, 'fr')}** ({VACATION_MIN_H} h plus tard) ;
- le samedi, le bouton « Revenir » affiche encore le temps restant ;
- si vous restez trois semaines, rien ne s'arrête tout seul, et vos planètes n'ont rien produit pendant ces trois semaines ;
- si vous êtes fondateur d'alliance, votre place passe à un autre membre au bout de {FOUNDER_LOSS_DAYS} jours d'absence : confiez-la avant de partir.

## Pièges fréquents

- **Préparez le départ** : faites rentrer vos flottes, laissez finir ou annulez vos ordres, sinon le départ est refusé.
- **Pas de départ sous la menace** : une attaque déjà lancée contre vous bloque le mode vacances.
- **Les débris restent recyclables** : un champ de ruines au-dessus de votre planète peut être récupéré par d'autres pendant votre absence.
- **Pas de production** : vos mines ne travaillent pas pendant les vacances.

## Pages liées

- [Protection des débutants](/fr/players/beginner-protection)
- [Inactivité](/fr/players/inactivity)
- [La vue galaxie](/fr/universe/galaxy-view)
- [Univers privés](/fr/misc/private-universes)
'''
    return f'''# Vacation mode

> **In short**: vacation mode pauses your empire in a universe. No more production, no more actions on your side, and nobody can reach you. It lasts at least {VACATION_MIN_H} hours, has no maximum duration and only ends when you decide.
{{.is-info}}

## Rules

### Leaving
1. Vacation mode is turned on **per universe**, in Settings ("Go on vacation"). You can be on vacation in one universe and play in another.
2. **Departure conditions**, all required:
   - none of your fleets is in flight;
   - no order is running: building, research, ships or defenses;
   - no attack is inbound.
   While a condition is missing, the button is greyed out and the game says what to wait for.
3. On departure, each planet is paid what it produced up to that moment. Then **production drops to zero** on all your planets and moons.

### While on vacation
4. **You can no longer act** in that universe: no fleet, missile, construction, cancellation, demolition, Phalanx or alliance convoy. You can still **look at** the galaxy, your reports, messaging and your alliance.
5. **Other players** can neither attack you, destroy your moon, transport resources to you nor fire missiles at you.
6. **Espionage** stays possible: probes fly and reveal the cell, but the report only says that the owner is away. **Recycling** the debris fields above your planets stays possible too.
7. Your planets show the "On vacation" status ("(v)") in the galaxy view, and your card the "On vacation" badge.

### Coming back
8. **Minimum stay: {VACATION_MIN_H} hours.** After that, you come back whenever you want with the "Come back" button. There is **no maximum duration, no automatic end and no delay** before leaving again.
9. On your return, production resumes from that moment: the days away earn nothing.
10. While on vacation nobody can attack you, inactive or not. Your activity is recorded again as soon as you come back.
11. What keeps running: [newcomer protection](/en/players/beginner-protection) (its {NEWCOMER_DAYS} days count from your arrival) and, if you **founded an alliance**, the succession delay: an absent founder loses their seat after {FOUNDER_LOSS_DAYS} days, vacation included (see [Inactivity](/en/players/inactivity)).

### Frozen private universe
12. A [private universe](/en/misc/private-universes) whose subscription has stopped is **frozen**: it is vacation mode for all its players at once, with no departure condition.
13. Nobody acts there; you can only look. Production stops. Attacks and espionage in flight turn back and give their [attack limit](/en/players/attack-limit) slot back; transports, returns and constructions already paid for run to completion.
14. When it thaws, the frozen time is given back: each player's last activity, alliance vote deadlines, notices of denounced pacts, aid requests and report retention are pushed back by the same amount. Not pushed back: alliance mission cycles, the retention of alliance channel messages and newcomer protection.

## Worked example

You leave on {d(START, 'en')}:
- you can come back from **{d(BACK, 'en')}** ({VACATION_MIN_H} h later);
- on Saturday, the "Come back" button still shows the time left;
- if you stay three weeks, nothing stops on its own, and your planets have produced nothing during those three weeks;
- if you are an alliance founder, your seat goes to another member after {FOUNDER_LOSS_DAYS} days away: hand it over before you leave.

## Common pitfalls

- **Prepare your departure**: bring your fleets home, let your orders finish or cancel them, otherwise the departure is refused.
- **No departure under threat**: an attack already launched at you blocks vacation mode.
- **Debris stays recyclable**: a debris field above your planet can be collected by others while you are away.
- **No production**: your mines do not work during the vacation.

## Related pages

- [Beginner protection](/en/players/beginner-protection)
- [Inactivity](/en/players/inactivity)
- [The galaxy view](/en/universe/galaxy-view)
- [Private universes](/en/misc/private-universes)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/vacation-mode', body(lang),
          description='Mettre son empire en pause dans un univers.' if lang == 'fr' else 'Pausing your empire in a universe.')
