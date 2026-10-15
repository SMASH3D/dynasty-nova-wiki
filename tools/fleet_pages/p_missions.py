import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    lv = {'combustion_drive': 6}
    fleet = [('large_cargo', 5)]
    d = distance(0, 0, 4)
    leg = leg_fuel(d, 100, fleet, lv)
    t = duration(d, 100, speed('large_cargo', lv))
    # Espionnage : coût × max(0,5 ; 1 − 0,05 × Renseignement Tactique)
    pd = distance(ring(2, 4, 9), 0, 0)
    probe = leg_fuel(pd, 100, [('espionage_probe', 30)], lv)
    spy_paid = fl(2 * probe * max(0.5, 1 - 0.05 * 4))
    if fr:
        rows = [
            ['**Attaque**', "Planète ou lune d'un autre joueur", 'Combat contre la flotte et les défenses ; en cas de victoire, [pillage](/fr/combat/plunder)', "Ni vos bases, ni celles d'un membre de votre alliance (pas de tir ami). Soumise aux [protections](/fr/players/beginner-protection) et à la [limite d'attaques](/fr/players/attack-limit). Lancer une attaque met fin à votre protection de nouveau joueur"],
            ['**Transport**', 'Une base, la vôtre ou celle de n\'importe quel joueur, alliés compris', 'La cargaison est livrée, même au-delà des entrepôts ; la flotte revient', 'Impossible vers un joueur en vacances'],
            ['**Stationnement**', 'Une de **vos** planètes ou lunes, avec un Dock orbital', 'La flotte et sa cargaison restent sur place', 'Aller simple. Si la base n\'a plus de Dock orbital à l\'arrivée, la cargaison est déposée et les vaisseaux rentrent'],
            ['**Colonisation**', 'Position libre (pas une lune), espionnée au préalable', 'Un Pionnier spatial fonde la colonie et disparaît ; la cargaison devient le stock de départ, les autres vaisseaux y restent', 'Aller simple ; il faut une place de colonie libre (voir [Coloniser](/fr/universe/colonization)). Sinon, la flotte rentre'],
            ['**Espionnage**', "Planète ou lune d'un autre joueur", 'Les Éclaireurs envoient un rapport et rentrent, sauf ceux abattus', 'Éclaireurs seulement. Possible sur un joueur protégé ou en vacances. Hydrogène réduit de 5 % par niveau de Renseignement Tactique, au plus de moitié. Voir [Espionner](/fr/espionage/spying)'],
            ['**Recyclage**', 'Une position, ou l\'espace lointain', 'Les Récupérateurs ramassent les débris, dans la limite de leur propre soute', 'Récupérateurs seulement. La position doit avoir été espionnée au moins une fois, par vous ou un membre de votre alliance, sauf votre propre base et l\'espace lointain. Voir [Champs de ruines](/fr/combat/debris)'],
            ['**Expédition**', "L'espace lointain du système", 'La flotte tient sa position puis revient, avec une trouvaille ou non', 'Voir [Expéditions](/fr/fleet/expeditions)'],
            ['**Destruction de lune**', "Lune d'un autre joueur", 'Combat, puis tentative de destruction', 'Colossus stellaires seulement. Voir [Destruction de lune](/fr/combat/moon-destruction)'],
            ['**Dépôt à la banque**', 'La Station stellaire du système', 'Les ressources sont vendues contre des Crédits ; la flotte rentre à vide', 'Navettes de fret et Cargos stellaires seulement, depuis une base avec un Dock orbital. 1 h aller, 1 h retour, sans hydrogène, sans rappel. Voir [Banque stellaire](/fr/economy/stellar-bank)'],
            ["**Don à l'alliance**", 'La Station stellaire du système', "La trésorerie prend ce que son plafond permet, le reste rentre avec la flotte", "Mêmes conditions que le dépôt à la banque. Voir [Missions et station d'alliance](/fr/players/alliance-missions)"],
        ]
        T = table(['Mission', 'Cible', 'Ce qui se passe', 'À savoir'], rows)
        return f'''# Les missions

> **En bref** : une flotte part toujours avec une mission. Il en existe dix : Attaque, Transport, Stationnement, Colonisation, Espionnage, Recyclage, Expédition et Destruction de lune, plus deux dépôts à la Station stellaire du système, Dépôt à la banque et Don à l'alliance. Chacune a sa cible, ses vaisseaux autorisés et ses règles.
{{.is-info}}

## Règles

1. Chaque flotte occupe un **emplacement de flotte** jusqu'à son retour (voir [Déplacements](/fr/fleet/movement)).
2. L'hydrogène du **retour est payé au départ**, sauf pour la Colonisation et le Stationnement, qui sont des allers simples. Les deux dépôts à la Station stellaire ne consomment pas d'hydrogène : 1 h à l'aller, 1 h au retour, quelle que soit la distance.
3. Une flotte peut être **rappelée** tant qu'elle est à l'aller ou en maintien d'expédition, sans remboursement d'hydrogène. Les dépôts à la Station stellaire ne se rappellent pas.
4. **Composition** : l'Espionnage n'emporte que des Éclaireurs, le Recyclage que des Récupérateurs, la Destruction de lune que des Colossus stellaires, les dépôts que des Navettes de fret et des Cargos stellaires. La Colonisation exige au moins un Pionnier spatial. Le Collecteur solaire ne vole jamais.
5. Une flotte ne peut pas viser la base dont elle part, sauf pour recycler le champ de ruines de sa propre position. Une planète et sa lune sont deux bases distinctes.
6. **Vacances** : en mode vacances, vous ne pouvez envoyer aucune flotte. Un joueur en vacances ne peut recevoir ni Attaque, ni Destruction de lune, ni Transport ; l'Espionnage passe, et son rapport indique seulement que le joueur est absent.
7. **Maintenance** : pendant une maintenance, l'Attaque, l'Espionnage et la Destruction de lune ne peuvent pas partir ; les flottes déjà en vol arrivent normalement.
8. **Il n'existe ni attaque groupée, ni défense alliée** : le Stationnement ne vise que vos propres bases.
9. Le joueur attaqué reçoit une **alerte 1 minute avant l'impact** d'une Attaque, jusqu'à 6 minutes avec les talents de l'[Oracle](/fr/dynasty/classes/oracle).
10. **Retour** : la flotte rentre sur sa base de départ, qui doit encore vous appartenir et avoir un Dock orbital ; sinon elle est perdue. Ce qu'elle rapporte est déchargé même au-delà de la capacité des entrepôts.

## Données détaillées

{T}

## Exemple chiffré

Vous envoyez 5 Cargos stellaires de [2:40:8] vers [2:40:12], à 100 %, avec Propulseur Chimique 6. Distance : 1 000 + 5 × 4 = {N(d)} ; trajet de {N(t)} s ({hms(t, lang)}).
- En **Transport** chez un allié : l'aller ({N(leg)}) **et** le retour ({N(leg)}) sont prélevés au départ, soit **{N(2 * leg)} hydrogène**. La flotte revient.
- En **Stationnement** sur votre colonie : seul l'aller est payé, **{N(leg)} hydrogène**, et la flotte y reste.
- En **Don à l'alliance** vers la Station stellaire : **0 hydrogène**, 1 h à l'aller et 1 h au retour.

Trente Éclaireurs envoyés de [2:40:8] vers [4:12:3] (distance 2 × 20 000) avec Renseignement Tactique 4 : l'aller-retour brûle {N(2 * probe)} hydrogène, et vous n'en payez que {N(2 * probe)} × 0,8 = **{N(spy_paid)}** (arrondi à l'inférieur).

## Pièges fréquents

- **Stationnement ≠ transport** : le Stationnement ne vise que vos propres bases dotées d'un Dock orbital. Pour livrer un allié, utilisez le Transport.
- **Une attaque coûte votre protection** : la première attaque lancée met fin à vos 7 jours de protection de nouveau joueur. L'espionnage et le transport ne la retirent pas.
- **Espionnez avant de recycler ou de coloniser** : une position jamais espionnée refuse le Recyclage et la Colonisation.
- **Les emplacements sont limités** : chaque mission, expéditions et dépôts compris, occupe un emplacement jusqu'au retour de la flotte.
- **Un pacte n'empêche pas l'attaque** : contre une alliance sous pacte, l'attaque part, mais elle coûte des points de fair-play à votre alliance (voir [Pactes, fair-play et guerres](/fr/players/pacts-and-wars)).

## Pages liées

- [Déplacements](/fr/fleet/movement)
- [Pillage](/fr/combat/plunder)
- [Limite d'attaques](/fr/players/attack-limit)
- [Expéditions](/fr/fleet/expeditions)
- [Espionner](/fr/espionage/spying)
- [Banque stellaire](/fr/economy/stellar-bank)
- [Missions et station d'alliance](/fr/players/alliance-missions)
'''
    rows = [
        ['**Attack**', "Another player's planet or moon", 'Battle against fleet and defenses; on victory, [plunder](/en/combat/plunder)', "Not your bases, nor those of a member of your alliance (no friendly fire). Subject to the [protections](/en/players/beginner-protection) and the [attack limit](/en/players/attack-limit). Launching an attack ends your new player protection"],
        ['**Transport**', 'A base, yours or any player\'s, allies included', 'The cargo is delivered, even beyond storage; the fleet returns', 'Not possible towards a player on vacation'],
        ['**Stationing**', 'One of **your** planets or moons, with an Orbital Dock', 'The fleet and its cargo stay there', 'One-way. If the base no longer has an Orbital Dock on arrival, the cargo is dropped and the ships fly home'],
        ['**Colonization**', 'Free position (not a moon), scouted beforehand', 'A Space Pioneer founds the colony and is used up; the cargo becomes the starting stock, the other ships stay there', 'One-way; needs a free colony slot (see [Colonization](/en/universe/colonization)). Otherwise the fleet flies home'],
        ['**Espionage**', "Another player's planet or moon", 'Scouts send back a report and fly home, except those shot down', 'Scouts only. Possible on a protected or vacationing player. Hydrogen cut by 5% per level of Espionage Technology, by half at most. See [Spying](/en/espionage/spying)'],
        ['**Recycling**', 'A position, or deep space', 'Salvagers collect debris, within their own holds', 'Salvagers only. The position must have been scouted at least once, by you or a member of your alliance, except your own base and deep space. See [Debris fields](/en/combat/debris)'],
        ['**Expedition**', "The system's deep space", 'The fleet holds position then returns, with a find or not', 'See [Expeditions](/en/fleet/expeditions)'],
        ['**Moon destruction**', "Another player's moon", 'Battle, then a destruction attempt', 'Stellar Colossi only. See [Moon destruction](/en/combat/moon-destruction)'],
        ['**Bank deposit**', "The system's Stellar Station", 'The resources are sold for Credits; the fleet flies home empty', 'Cargo Shuttles and Stellar Freighters only, from a base with an Orbital Dock. 1 h out, 1 h back, no hydrogen, no recall. See [Stellar bank](/en/economy/stellar-bank)'],
        ['**Alliance donation**', "The system's Stellar Station", 'The treasury takes what its cap allows, the rest flies home with the fleet', 'Same conditions as the bank deposit. See [Alliance missions and station](/en/players/alliance-missions)'],
    ]
    T = table(['Mission', 'Target', 'What happens', 'Good to know'], rows)
    return f'''# Missions

> **In short**: a fleet always leaves on a mission. There are ten: Attack, Transport, Stationing, Colonization, Espionage, Recycling, Expedition and Moon destruction, plus two deposits at the system's Stellar Station, Bank deposit and Alliance donation. Each has its own target, allowed ships and rules.
{{.is-info}}

> Ship names are provisional English translations: the game still shows French names (see the [glossary](/en/getting-started/glossary)).
{{.is-warning}}

## Rules

1. Each fleet takes a **fleet slot** until it returns (see [Fleet movement](/en/fleet/movement)).
2. Hydrogen for the **return is paid at departure**, except for Colonization and Stationing, which are one-way. The two Stellar Station deposits burn no hydrogen: 1 h out, 1 h back, whatever the distance.
3. A fleet can be **recalled** while it is flying out or holding on an expedition, with no hydrogen refund. Stellar Station deposits cannot be recalled.
4. **Composition**: Espionage carries Scouts only, Recycling Salvagers only, Moon destruction Stellar Colossi only, the deposits Cargo Shuttles and Stellar Freighters only. Colonization needs at least one Space Pioneer. The Solar Collector never flies.
5. A fleet cannot target the base it leaves, except to recycle the debris field over its own position. A planet and its moon are two separate bases.
6. **Vacation**: in vacation mode you cannot send any fleet. A player on vacation cannot receive an Attack, a Moon destruction or a Transport; Espionage goes through, and its report only says the player is away.
7. **Maintenance**: during a maintenance, Attack, Espionage and Moon destruction cannot leave; fleets already in flight arrive as usual.
8. **There is no grouped attack and no allied defense**: Stationing only targets your own bases.
9. The attacked player gets an **alert 1 minute before the impact** of an Attack, up to 6 minutes with [Oracle](/en/dynasty/classes/oracle) talents.
10. **Return**: the fleet flies home to its departure base, which must still be yours and have an Orbital Dock; otherwise it is lost. What it brings back is unloaded even beyond storage capacity.

## Detailed data

{T}

## Worked example

You send 5 Stellar Freighters from [2:40:8] to [2:40:12], at 100%, with Combustion Drive 6. Distance: 1,000 + 5 × 4 = {N(d)}; trip of {N(t)} s ({hms(t, lang)}).
- As a **Transport** to an ally: the way out ({N(leg)}) **and** back ({N(leg)}) are taken at departure, so **{N(2 * leg)} hydrogen**. The fleet comes back.
- As **Stationing** at your colony: only the way out is paid, **{N(leg)} hydrogen**, and the fleet stays there.
- As an **Alliance donation** to the Stellar Station: **0 hydrogen**, 1 h out and 1 h back.

Thirty Scouts sent from [2:40:8] to [4:12:3] (distance 2 × 20,000) with Espionage Technology 4: the round trip burns {N(2 * probe)} hydrogen, and you only pay {N(2 * probe)} × 0.8 = **{N(spy_paid)}** (rounded down).

## Common pitfalls

- **Stationing is not transport**: Stationing only targets your own bases with an Orbital Dock. To supply an ally, use Transport.
- **An attack costs your protection**: the first attack you launch ends your 7 days of new player protection. Espionage and transport do not remove it.
- **Scout before recycling or colonizing**: a position never scouted refuses Recycling and Colonization.
- **Slots are limited**: every mission, expeditions and deposits included, takes a slot until the fleet returns.
- **A pact does not stop the attack**: against an alliance under a pact, the attack leaves, but it costs your alliance fair-play points (see [Pacts, fair play and wars](/en/players/pacts-and-wars)).

## Related pages

- [Fleet movement](/en/fleet/movement)
- [Plunder](/en/combat/plunder)
- [Attack limit](/en/players/attack-limit)
- [Expeditions](/en/fleet/expeditions)
- [Spying](/en/espionage/spying)
- [Stellar bank](/en/economy/stellar-bank)
- [Alliance missions and station](/en/players/alliance-missions)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/missions', body(lang),
          description=('Les dix missions de flotte et leurs règles.' if lang == 'fr' else 'The ten fleet missions and their rules.'))
