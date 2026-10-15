import sys; sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
from univ_lib import *; from write import *

MAXA, WIN = DEFAULTS['bashing']
BF, BP = DEFAULTS['bookmarks']
G, S, P = REDLINE['map']


def body(lang):
    N = lambda x: n(x, lang)
    if lang == 'fr':
        badges = [
            ['Haut gauche', 'Nouveau joueur', f'Joueur dans ses {NEWCOMER_DAYS} premiers jours dans l\'univers : ni attaque ni missiles'],
            ['Haut gauche', 'Débutant protégé / Trop fort pour vous', 'Écart de points trop grand entre vous (voir [Protection des débutants](/fr/players/beginner-protection))'],
            ['Haut gauche', 'Attaques restantes : x / y', 'Attaques qu\'il vous reste contre ce joueur dans la fenêtre en cours, affiché dès la première attaque'],
            ['Haut droit', 'Champ de ruines', 'Débris en orbite, à recycler'],
            ['Bas droit', 'Espionnée récemment', 'Vous l\'avez espionnée il y a moins de 5 minutes'],
            ['Bas droit', 'Découverte par un membre de l\'alliance', 'Case révélée par l\'espionnage d\'un membre de votre alliance'],
            ['Bas gauche', 'Membre de votre alliance, Sous pacte de non-agression, Sous pacte d\'alliance, Ennemi', 'Relation entre votre alliance et la sienne'],
            ['Bas gauche', 'Joueur IA (PvE)', 'Planète d\'un adversaire contrôlé par le jeu'],
        ]
        return f'''# La vue galaxie

> **En bref** : la vue galaxie affiche un système à la fois, position par position, puis l'espace lointain et la Station stellaire. Une case que ni vous ni votre alliance n'avez espionnée reste illisible. Pour chaque planète découverte, vous voyez son propriétaire, ses points, ses badges, sa lune et ses débris. C'est aussi d'ici que vous espionnez d'un clic, partagez une position avec votre alliance, l'ajoutez à vos favoris ou lancez une mission.
{{.is-info}}

> **Paramètre d'univers** : le nombre d'attaques permises contre un même joueur et sa fenêtre peuvent être différents selon l'univers.
> Par défaut : **{MAXA} attaques par {WIN} h** · Redline : **{REDLINE['bashing'][0]} attaques par {REDLINE['bashing'][1]} h**
{{.is-info}}

> **Paramètre d'univers** : le nombre de favoris peut être différent selon l'univers.
> Par défaut : **{BF}, {BP} en Premium** · Redline : **{REDLINE['bookmarks'][0]}, {REDLINE['bookmarks'][1]} en Premium**
{{.is-info}}

![La vue galaxie en affichage orbites](/images/screenshots/french/vue-galaxie-orbites.jpg)
*La vue galaxie en affichage orbites : chaque planète a son aspect, selon son type et son biome. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

![La vue galaxie en affichage liste](/images/screenshots/french/vue-galaxie.jpg)
*En affichage liste, les positions pas encore espionnées restent illisibles. Capture du jeu en version Serveur 2.1.0 · Client 3.1.0.*

## Règles

### Se déplacer
1. La vue galaxie montre **un système** : toutes ses positions, puis deux lignes de plus, l'**espace lointain** et la **Station stellaire**.
2. **Navigation** : flèches ← / → du clavier pour changer de système, Ctrl + ← / → (⌘ sur Mac) pour changer de galaxie. Le sélecteur du bas permet aussi de saisir une galaxie et un système. Après le dernier système, on revient au premier.
3. À l'ouverture, la vue affiche le système de votre planète actuelle.
4. Deux affichages sont proposés sur grand écran : **Orbites** (par défaut) et **Liste**. Votre choix est mémorisé.

### Ce que vous voyez
5. **Cases inexplorées** : tant que ni vous ni un membre de votre alliance n'avez espionné une position, tout y reste caché. Une écriture exotique remplace le nom de la planète et celui de son propriétaire, et la vignette reste grise. Une case illisible peut être libre ou occupée : seul l'espionnage le révèle. Seul l'espionnage y est proposé.
6. **Une case espionnée le reste pour de bon** : chaque espionnage arrivé à destination révèle la position, pour vous et pour votre alliance. En rejoignant une alliance, vous lui apportez les cases que vous aviez déjà découvertes.
7. Sur une case découverte, une ligne affiche la position, la vignette avec ses **badges** (tableau ci-dessous), le nom de la planète (une couronne distingue planète mère et colonie), le propriétaire (en vert pour un allié, en rouge pour un ennemi), ses **points** et ses points militaires, et la pastille **« En vacances »** s'il y a lieu.
8. Le propriétaire peut aussi s'afficher **« Abandonnée »** (planète abandonnée, voir [Abandonner une colonie](/fr/universe/abandoning-a-planet)), **« Inhabitée »** (position libre) ou **« Vous »**.
9. Sur une case inexplorée, le nom d'un joueur qui vous a espionné ou attaqué depuis cette position peut apparaître, avec la mention de ce qu'il a fait.
10. Une **lune** s'affiche sur une sous-ligne, sous sa planète, avec son diamètre (et ses cases si c'est la vôtre). Elle a sa propre fiche.
11. En affichage Orbites, survoler une planète découverte montre ses points, sa **taille** en cases, sa **température**, ses débris et sa lune. En affichage Liste, taille et température sont dans la fiche de la case.
12. Un bandeau annonce une **pluie de comètes** quand l'univers en prévoit une, avec les galaxies touchées et un compte à rebours.

### Lignes spéciales
13. **Espace lointain** (position {P + 1} sur Redline) : la ligne propose l'**expédition**, si l'univers les autorise, et le **recyclage** des débris qui s'y trouvent. Aucune planète ne s'y pose.
14. **Station stellaire** (position {P + 2} sur Redline) : une par système. Le bouton **« Ouvrir la station »** mène à la [Banque stellaire](/fr/economy/stellar-bank) et, si vous avez une alliance, à sa trésorerie.

### Agir depuis une case
15. **Espionnage rapide** : le bouton de la ligne envoie **un Éclaireur** à vitesse maximale depuis votre planète actuelle. Il faut un Éclaireur disponible sur cette planète.
16. **Fiche de la case** : un clic ouvre la fiche, avec les missions possibles (espionner, attaquer, coloniser, transporter, recycler, frappe de missiles ; sur une lune : espionner, attaquer, détruire, transporter ; déployer sur vos propres planètes et lunes).
17. **Coloniser** et **recycler** demandent une case déjà espionnée, par vous ou par votre alliance.
18. **Partager une position** avec votre alliance : chaque membre l'ouvre dans sa propre vue galaxie, avec ce qu'il a le droit d'y voir. Le message reste **30 jours** dans le canal.
19. Une **étoile** ajoute la position (ou la lune) à vos **favoris**.
20. Vous pouvez écrire au propriétaire d'une planète découverte, sauf à un adversaire contrôlé par le jeu.
21. Si vous êtes en mode vacances, aucune mission n'est proposée.

## Exemple chiffré

Sur Redline, vous pouvez attaquer un même joueur **{MAXA} fois par {WIN} heures**. Vous l'avez déjà attaqué deux fois : sur sa ligne, le badge affiche **« Attaques restantes : {MAXA - 2} / {MAXA} »**. Après {MAXA - 2} autres attaques, il affichera 0 / {MAXA} et toute nouvelle attaque sera refusée jusqu'à ce que la première sorte de la fenêtre de {WIN} heures.

## Données détaillées

### Badges d'une case

Chaque coin de la vignette n'affiche qu'un badge à la fois.

{table(['Coin', 'Badge', 'Signification'], badges)}

## Pièges fréquents

- **Une case illisible ne dit rien** : elle peut cacher un joueur comme être vide. Envoyez un Éclaireur avant de conclure.
- **Pas de colonisation à l'aveugle** : une position jamais espionnée ne peut pas être colonisée.
- **Le compteur d'attaques est par joueur** : il compte toutes ses planètes ensemble.
- **L'espionnage rapide part de la planète sélectionnée** : sans Éclaireur sur cette planète, le bouton ne fonctionne pas.
- **Les débris sont à tout le monde** : un champ de ruines repéré revient au premier qui le recycle.

## Pages liées

- [Coordonnées](/fr/universe/coordinates)
- [Protection des débutants](/fr/players/beginner-protection)
- [Limite d'attaques](/fr/players/attack-limit)
- [Espionner](/fr/espionage/spying)
- [Vue Empire et favoris](/fr/misc/empire-and-bookmarks)
- [Banque stellaire](/fr/economy/stellar-bank)
'''
    badges = [
        ['Top left', 'New player', f'Player in their first {NEWCOMER_DAYS} days in the universe: no attacks, no missiles'],
        ['Top left', 'Protected beginner / Too strong for you', 'Points gap between you too wide (see [Beginner protection](/en/players/beginner-protection))'],
        ['Top left', 'Attacks remaining: x / y', 'Attacks you have left against this player in the current window, shown from the first attack on'],
        ['Top right', 'Debris field', 'Debris in orbit, to be recycled'],
        ['Bottom right', 'Spied recently', 'You spied it less than 5 minutes ago'],
        ['Bottom right', 'Discovered by an alliance member', 'Cell revealed by a member of your alliance spying it'],
        ['Bottom left', 'Member of your alliance, Under a non-aggression pact, Under an alliance pact, Enemy', 'Relation between your alliance and theirs'],
        ['Bottom left', 'AI player (PvE)', 'Planet of an opponent controlled by the game'],
    ]
    return f'''# The galaxy view

> **In short**: the galaxy view shows one system at a time, position by position, then deep space and the Stellar Station. A cell that neither you nor your alliance has spied stays unreadable. For each discovered planet you see its owner, points, badges, moon and debris. It is also where you spy in one click, share a position with your alliance, bookmark it or launch a mission.
{{.is-info}}

> **Universe setting**: the number of attacks allowed against the same player, and its window, may differ from one universe to another.
> Default: **{MAXA} attacks per {WIN} h** · Redline: **{REDLINE['bashing'][0]} attacks per {REDLINE['bashing'][1]} h**
{{.is-info}}

> **Universe setting**: the number of bookmarks may differ from one universe to another.
> Default: **{BF}, {BP} with Premium** · Redline: **{REDLINE['bookmarks'][0]}, {REDLINE['bookmarks'][1]} with Premium**
{{.is-info}}

![The galaxy view in orbit layout](/images/screenshots/english/galaxy-view-orbits.jpg)
*The galaxy view in orbit layout: each planet has its own look, according to its type and biome. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

![The galaxy view in list layout](/images/screenshots/english/galaxy-view.jpg)
*In list layout, positions not yet spied stay unreadable. Screenshot from game version Server 2.1.0 · Client 3.1.0.*

## Rules

### Getting around
1. The galaxy view shows **one system**: all its positions, then two more lines, **deep space** and the **Stellar Station**.
2. **Navigation**: ← / → arrow keys to change system, Ctrl + ← / → (⌘ on Mac) to change galaxy. The selector at the bottom also lets you type a galaxy and a system. After the last system you are back at the first one.
3. When opened, the view shows the system of your current planet.
4. Two layouts are offered on large screens: **Orbits** (the default) and **List**. Your choice is remembered.

### What you see
5. **Unexplored cells**: as long as neither you nor a member of your alliance has spied a position, everything there stays hidden. Alien script replaces the planet's and the owner's names, and the thumbnail stays grey. An unreadable cell may be free or taken: only spying tells. Spying is the only mission offered there.
6. **A spied cell stays revealed for good**: every spy mission that reaches its target reveals the position, for you and for your alliance. When you join an alliance, you bring it the cells you had already discovered.
7. On a discovered cell, a line shows the position, the thumbnail with its **badges** (table below), the planet's name (a crown tells mother planet from colony), the owner (green for an ally, red for an enemy), their **points** and military points, and the **"On vacation"** tag when relevant.
8. The owner may also read **"Abandoned"** (abandoned planet, see [Abandoning a colony](/en/universe/abandoning-a-planet)), **"Uninhabited"** (free position) or **"You"**.
9. On an unexplored cell, the name of a player who spied on or attacked you from that position may show, with what they did.
10. A **moon** is shown on a sub-line below its planet, with its diameter (and its fields if it is yours). It has its own card.
11. In Orbits layout, hovering a discovered planet shows its points, its **size** in fields, its **temperature**, its debris and its moon. In List layout, size and temperature are in the cell's card.
12. A banner announces a **comet shower** when the universe has one coming, with the galaxies hit and a countdown.

### Special lines
13. **Deep space** (position {P + 1} on Redline): the line offers the **expedition**, if the universe allows them, and **recycling** of the debris found there. No planet ever stands there.
14. **Stellar Station** (position {P + 2} on Redline): one per system. The **"Open the station"** button leads to the [Stellar Bank](/en/economy/stellar-bank) and, if you have an alliance, to its treasury.

### Acting from a cell
15. **Quick spy**: the button on the line sends **one Scout** at full speed from your current planet. You need a Scout available on that planet.
16. **Cell card**: a click opens the card, with the possible missions (spy, attack, colonize, transport, recycle, missile strike; on a moon: spy, attack, destroy, transport; deploy on your own planets and moons).
17. **Colonizing** and **recycling** require a cell already spied, by you or by your alliance.
18. **Share a position** with your alliance: each member opens it in their own galaxy view, with what they are allowed to see there. The message stays **30 days** in the channel.
19. A **star** adds the position (or the moon) to your **bookmarks**.
20. You can write to the owner of a discovered planet, except to an opponent controlled by the game.
21. While you are in vacation mode, no mission is offered.

## Worked example

On Redline you can attack the same player **{MAXA} times per {WIN} hours**. You have already attacked them twice: on their line, the badge reads **"Attacks remaining: {MAXA - 2} / {MAXA}"**. After {MAXA - 2} more attacks it will read 0 / {MAXA}, and any new attack will be refused until the first one leaves the {WIN}-hour window.

## Detailed data

### Cell badges

Each corner of the thumbnail shows one badge at a time.

{table(['Corner', 'Badge', 'Meaning'], badges)}

## Common pitfalls

- **An unreadable cell says nothing**: it may hide a player or be empty. Send a Scout before concluding.
- **No blind colonizing**: a position never spied cannot be colonized.
- **The attack counter is per player**: it counts all their planets together.
- **Quick spy leaves from the selected planet**: without a Scout on that planet, the button does not work.
- **Debris belongs to everyone**: a debris field you spot goes to whoever recycles it first.

## Related pages

- [Coordinates](/en/universe/coordinates)
- [Beginner protection](/en/players/beginner-protection)
- [Attack limit](/en/players/attack-limit)
- [Spying](/en/espionage/spying)
- [Empire view and bookmarks](/en/misc/empire-and-bookmarks)
- [Stellar Bank](/en/economy/stellar-bank)
'''


if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'universe/galaxy-view', body(lang))
