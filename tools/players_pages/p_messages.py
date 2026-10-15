import sys; sys.path.insert(0, sys.argv[1])
from players_lib import *; from write import *
from datetime import date, timedelta

# Réglages des rapports (Paramètres > Rapports) : groupes et libellés du front (ReportPreferencesSection, notifications.json)
GROUPS = {
 'fr': [('Combats et espionnage', ["Rapport d'espionnage*", 'Rapport de combat*', "Alerte d'intrusion", 'Rapport de frappe', 'Destruction de lune']),
        ('Missions de flotte', ['Rapport de transport', 'Rapport de recyclage', "Rapport d'expédition", 'Rapport de stationnement', 'Rapport de colonisation']),
        ('Retours de flotte', ["Retour d'espionnage", 'Retour de combat', 'Retour de transport', 'Retour de recyclage', "Retour d'expédition", 'Retour de stationnement', 'Retour de colonisation', 'Retour de destruction', 'Retour de la banque', "Retour de la trésorerie d'alliance"])],
 'en': [('Combat and espionage', ['Spy report*', 'Battle report*', 'Intrusion alert', 'Strike report', 'Moon destruction']),
        ('Fleet missions', ['Transport report', 'Recycling report', 'Expedition report', 'Stationing report', 'Colonization report']),
        ('Fleet returns', ['Spy return', 'Battle return', 'Transport return', 'Recycling return', 'Expedition return', 'Stationing return', 'Colonization return', 'Moon strike return', 'Return from the bank', 'Return from the alliance treasury'])],
}
SHARE = date(2026, 11, 1)
SHARE_END = SHARE + timedelta(days=ALLIANCE_CHAT_D)
DEL = date(2026, 11, 28)
DEL_END = max(SHARE_END, DEL + timedelta(days=SHARED_GRACE_D))
MFR = ['', 'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
def dd(x, lang):
    if lang == 'fr':
        return f"{'1er' if x.day == 1 else x.day} {MFR[x.month]}"
    return x.strftime('%B ') + str(x.day)

def settings_table(lang):
    rows = []
    for g, items in GROUPS[lang]:
        for it in items:
            locked = it.endswith('*')
            name = it.rstrip('*')
            if lang == 'fr':
                rows.append([g, name, 'toujours' if locked else 'au choix', 'au choix'])
            else:
                rows.append([g, name, 'always' if locked else 'your choice', 'your choice'])
    return table(['Groupe', 'Rapport', 'Reçu', 'Annoncé dans la cloche'] if lang == 'fr' else ['Group', 'Report', 'Received', 'Announced in the bell'], rows)

def body(lang):
    N = lambda x: n(x, lang)
    if lang == 'fr':
        return f'''# Messagerie et rapports

> **En bref** : la messagerie a trois canaux (Général, Alliance, Privé). La page Rapports regroupe vos rapports d'espionnage, de combat et de missions ; ils sont gardés **{REPORT_RETENTION_D} jours**. Un rapport d'espionnage ou de combat peut être partagé avec votre alliance, qui le garde alors {ALLIANCE_CHAT_D} jours. Dans les Paramètres, vous choisissez les rapports que vous recevez.
{{.is-info}}

## Règles

### Messagerie
1. Trois canaux : **Général** (tous les joueurs de l'univers), **Alliance** (les membres de votre alliance, ouvert dès que vous y avez un siège) et **Privé** (une conversation avec un joueur, trouvé par son pseudo).
2. Vous pouvez écrire à un joueur depuis la galaxie, la fiche d'une planète ou sa fiche au classement.
3. Un message fait **{N(CHAT_MAX_CHARS)} caractères au plus**. Les **liens** et les propos interdits sont refusés.
4. **Anti-flood** : au plus **{SPAM_MAX} messages par {SPAM_WINDOW_S} secondes** ; le suivant est refusé (« Vous écrivez trop vite »).
5. Vous pouvez **répondre** à un message, **mentionner** un joueur avec @pseudo, **réagir** avec l'une des 10 réactions proposées (et voir qui a réagi), et **traduire** un message dans votre langue.
6. **Bloquer** un joueur : il ne peut plus vous écrire en privé, ses messages sur les canaux sont repliés et ses réactions ne comptent plus pour vous. La liste « Joueurs bloqués » permet de le débloquer.
7. Le canal **Alliance** garde les messages **{ALLIANCE_CHAT_D} jours**, puis ils disparaissent. Le fondateur et la vice-présidence peuvent y **épingler {PINS_MAX} messages** au plus.
8. Dans le canal Alliance, vous pouvez partager des cartes : rapport d'espionnage, rapport de combat, coordonnée galactique, contribution à la trésorerie, projet collectif, mission d'alliance. Un **combat exposé**, déjà public, se partage dans tous les canaux.
9. La modération peut retirer le droit d'écrire dans le chat, pour une durée donnée ou jusqu'à nouvel ordre. Vous continuez de jouer normalement.
10. Dans les Paramètres, la rubrique **Notifications** règle ce que la cloche et la pastille de la messagerie vous signalent (canal général, canal d'alliance, messages privés, événements d'alliance, etc.).

### Rapports
11. Chaque espionnage, combat, frappe de missiles, destruction de lune, transport, recyclage, expédition, stationnement, colonisation, alerte d'intrusion et retour de flotte produit un **rapport** dans la page Rapports, filtrable par type.
12. Un rapport est gardé **{REPORT_RETENTION_D} jours** après sa création, lu ou non, puis il disparaît.
13. Vous pouvez supprimer un rapport, une sélection, une catégorie (« Vider la catégorie ») ou tout (« Tout supprimer »). La suppression est **définitive**.
14. **Partager** un rapport d'espionnage ou de combat qui vous appartient le rend lisible par tous les membres de votre alliance, présents et futurs, depuis le canal d'alliance. Le message ne contient qu'un lien : chacun l'ouvre avec ses propres droits.
15. Un rapport partagé est gardé **{ALLIANCE_CHAT_D} jours** à compter du partage, dans votre historique comme dans le canal. Si vous le supprimez ensuite, il quitte votre historique mais reste ouvrable par l'alliance jusqu'à la fin de ces {ALLIANCE_CHAT_D} jours, et au moins **{SHARED_GRACE_D} jours** après la suppression.
16. Un rapport qu'un allié a partagé appartient à son destinataire : vous ne pouvez ni le supprimer ni le partager à nouveau.
17. Vous pouvez aussi partager une **position** de la galaxie avec votre alliance (voir [La vue galaxie](/fr/universe/galaxy-view)).

### Réglages des rapports
18. Dans les Paramètres, la rubrique **Rapports** propose deux commandes par rapport : **Rapport** (le recevoir ou non) et **Notif.** (l'annoncer ou non dans la cloche).
19. Un rapport **non reçu n'est pas écrit du tout** : ni dans la page Rapports, ni dans la cloche.
20. Les rapports d'**espionnage** et de **combat** sont toujours reçus : seule leur annonce peut être coupée.
21. Les retours de flotte se règlent **mission par mission**, par exemple pour couper les retours d'espionnage sans perdre les retours de combat.
22. Un **incident** est toujours signalé, même si le rapport est coupé : flotte perdue au retour, colonisation ou stationnement manqués, expédition disparue.

## Exemple chiffré

- Un rapport de transport reçu le {dd(SHARE, 'fr')} disparaît le {dd(SHARE + timedelta(days=REPORT_RETENTION_D), 'fr')}, que vous l'ayez lu ou non.
- Vous partagez un rapport d'espionnage le {dd(SHARE, 'fr')} : il reste ouvrable jusqu'au **{dd(SHARE_END, 'fr')}**, pour vous comme pour votre alliance.
- Vous le supprimez le {dd(DEL, 'fr')} : il quitte votre historique, mais l'alliance peut encore l'ouvrir jusqu'au **{dd(DEL_END, 'fr')}** ({SHARED_GRACE_D} jours après la suppression, plus tard que la fin des {ALLIANCE_CHAT_D} jours).

## Données détaillées

Réglages de la rubrique Rapports :

{settings_table('fr')}

## Pièges fréquents

- **Un rapport ne dure que {REPORT_RETENTION_D} jours** : partagez dans l'alliance ce que vous voulez garder plus longtemps.
- **Supprimer une catégorie efface tout** : il n'y a pas de corbeille.
- **Un rapport non reçu n'existe pas** : couper un rapport le supprime aussi de la page Rapports, pas seulement de la cloche.
- **Un rapport d'espionnage sur un joueur en vacances est vide** : ce n'est pas une erreur.

## Pages liées

- [Alliances](/fr/players/alliances)
- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Lire un rapport de combat](/fr/combat/battle-report)
- [Mode vacances](/fr/players/vacation-mode)
'''
    return f'''# Messages and reports

> **In short**: messaging has three channels (General, Alliance, Private). The Reports page gathers your espionage, battle and mission reports; they are kept for **{REPORT_RETENTION_D} days**. A spy or battle report can be shared with your alliance, which then keeps it for {ALLIANCE_CHAT_D} days. In Settings, you choose which reports you receive.
{{.is-info}}

## Rules

### Messaging
1. Three channels: **General** (every player of the universe), **Alliance** (the members of your alliance, open as soon as you hold a seat in it) and **Private** (a conversation with one player, found by name).
2. You can message a player from the galaxy, a planet's card or their ranking card.
3. A message is **{N(CHAT_MAX_CHARS)} characters at most**. **Links** and forbidden words are refused.
4. **Anti-flood**: at most **{SPAM_MAX} messages per {SPAM_WINDOW_S} seconds**; the next one is refused ("You are typing too fast").
5. You can **reply** to a message, **mention** a player with @name, **react** with one of the 10 reactions offered (and see who reacted), and **translate** a message into your language.
6. **Blocking** a player: they can no longer message you privately, their channel messages are folded and their reactions no longer count for you. The "Blocked players" list lets you unblock them.
7. The **Alliance** channel keeps messages for **{ALLIANCE_CHAT_D} days**, then they disappear. The founder and the vice-presidency can **pin up to {PINS_MAX} messages** there.
8. In the Alliance channel you can share cards: spy report, battle report, galactic coordinate, treasury contribution, collective project, alliance mission. A **battle showcase**, already public, can be shared in every channel.
9. Moderation can take away the right to write in chat, for a given time or until further notice. You keep playing normally.
10. In Settings, the **Notifications** section sets what the bell and the messaging badge tell you about (general channel, alliance channel, private messages, alliance events, etc.).

### Reports
11. Every espionage, battle, missile strike, moon destruction, transport, recycling, expedition, stationing, colonization, intrusion alert and fleet return produces a **report** on the Reports page, which can be filtered by type.
12. A report is kept for **{REPORT_RETENTION_D} days** after it is created, read or not, then it disappears.
13. You can delete one report, a selection, a category ("Clear category") or everything ("Delete all"). Deletion is **permanent**.
14. **Sharing** a spy or battle report of yours makes it readable by every member of your alliance, current and future, from the alliance channel. The message only carries a link: everyone opens it with their own rights.
15. A shared report is kept for **{ALLIANCE_CHAT_D} days** from the share, in your history as in the channel. If you then delete it, it leaves your history but stays openable by the alliance until the end of those {ALLIANCE_CHAT_D} days, and for at least **{SHARED_GRACE_D} days** after the deletion.
16. A report an ally shared belongs to its recipient: you can neither delete nor re-share it.
17. You can also share a galaxy **position** with your alliance (see [The galaxy view](/en/universe/galaxy-view)).

### Report settings
18. In Settings, the **Reports** section offers two controls per report: **Report** (receive it or not) and **Notif.** (announce it in the bell or not).
19. A report **you do not receive is not written at all**: neither on the Reports page nor in the bell.
20. **Spy** and **battle** reports are always received: only their announcement can be turned off.
21. Fleet returns are set **mission by mission**, for instance to drop spy returns without losing battle returns.
22. An **incident** is always reported, even when the report is turned off: a fleet lost on its way home, a failed colonization or deployment, a missing expedition.

## Worked example

- A transport report received on {dd(SHARE, 'en')} disappears on {dd(SHARE + timedelta(days=REPORT_RETENTION_D), 'en')}, read or not.
- You share a spy report on {dd(SHARE, 'en')}: it stays openable until **{dd(SHARE_END, 'en')}**, for you and for your alliance.
- You delete it on {dd(DEL, 'en')}: it leaves your history, but the alliance can still open it until **{dd(DEL_END, 'en')}** ({SHARED_GRACE_D} days after the deletion, later than the end of the {ALLIANCE_CHAT_D} days).

## Detailed data

Settings of the Reports section:

{settings_table('en')}

## Common pitfalls

- **A report only lasts {REPORT_RETENTION_D} days**: share with your alliance what you want to keep longer.
- **Clearing a category erases everything**: there is no recycle bin.
- **A report you do not receive does not exist**: turning a report off also removes it from the Reports page, not just from the bell.
- **A spy report on a player on vacation is empty**: it is not a bug.

## Related pages

- [Alliances](/en/players/alliances)
- [Reading a spy report](/en/espionage/spy-report)
- [Reading a battle report](/en/combat/battle-report)
- [Vacation mode](/en/players/vacation-mode)
'''

for lang in ('fr', 'en'):
    write(lang, 'players/messages-and-reports', body(lang),
          description='Chat, rapports, conservation, partage avec l\'alliance et réglages des rapports.' if lang == 'fr' else 'Chat, reports, retention, sharing with your alliance and report settings.')
