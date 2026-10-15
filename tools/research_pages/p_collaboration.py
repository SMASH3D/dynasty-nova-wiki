"""Page research/stellar-collaboration (FR et EN), calculée depuis research_lib (ResearchNetworkCalculator)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_lib import *
from write import write, table

# Exemple : Pliage Spatial 8 (prérequis de la Collaboration Stellaire elle-même n'entre pas en jeu ici)
EX_CODE, EX_L = 'hyperspace', 8
OTHERS = [10, 9, 6]
NET = 2
ex_cost = cost(EX_CODE, EX_L)
eff8, kept8 = network_effective(8, OTHERS, NET)
t_alone8 = research_seconds(EX_CODE, EX_L, 8)
t_net8 = research_seconds(EX_CODE, EX_L, eff8)
# Même empire, recherche lancée depuis la planète au Centre 10 : seuls les Centres 10 ou plus entrent
others10 = [8, 9, 6]
eff10, kept10 = network_effective(10, others10, NET)
t_net10 = research_seconds(EX_CODE, EX_L, eff10)
assert kept8 == [10, 9] and eff8 == 27 and kept10 == [] and eff10 == 10

def gain_table(lang):
    fr = lang == 'fr'
    levels = [8, 10, 12]
    rows = []
    for k in range(0, 11):
        row = [str(k)]
        for L in levels:
            eff, _ = network_effective(L, [L] * k, k)
            f = (1 + eff) / (1 + L)
            row.append(f'{eff} (×{n(round(f, 2), lang)})')
        rows.append(row)
    hdr = (['Centres en réseau (tous au même niveau)'] + [f'Centres au niveau {L}' for L in levels]) if fr else \
          (['Pooled Centers (all at the same level)'] + [f'Centers at level {L}' for L in levels])
    return table(hdr, rows)

def cost_table(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    rows = []
    for L in range(1, RES['research_network'][3] + 1):
        m, c, h, e = cost('research_network', L)
        rows.append([L, N(m), N(c), N(h), dur(research_seconds('research_network', L, 10), lang), n(points('research_network', L), lang)])
    hdr = ['Niveau', 'Métal', 'Cristal', 'Hydrogène', 'Durée avec un Centre 10 seul', 'Points'] if fr else \
          ['Level', 'Metal', 'Crystal', 'Hydrogen', 'Duration with a single Center 10', 'Points']
    return table(hdr, rows)

TALENTS = [  # (FR, EN), effet FR, effet EN
 (('Liaison montante', 'Uplink'), "accepte des Centres jusqu'à quelques niveaux sous celui qui étudie", 'accepts Centers a few levels below the one studying'),
 (('Antenne lointaine', 'Distant Antenna'), 'élargit encore cette tolérance', 'widens that tolerance further'),
 (('Un labo de plus', 'One More Lab'), "met en commun un Centre de plus que la Collaboration Stellaire ne l'autorise", 'pools one more Center than Stellar Collaboration allows'),
 (('Labos de campagne', 'Field Labs'), 'chaque Centre de vos planètes mis en réseau compte des niveaux de plus', 'each of your pooled Centers counts extra levels'),
 (('Labo-mère', 'Mother Lab'), 'le Centre qui étudie compte des niveaux de plus', 'the Center studying counts extra levels'),
 (('Échange universitaire', 'University Exchange'), "ajoute le meilleur Centre d'un membre de votre alliance, s'il entre dans la tolérance", "adds the best Center of a member of your alliance, if it fits the tolerance"),
 (('Réseau vivant', 'Living Network'), "recalcule une étude en cours quand un Centre du réseau monte de niveau, jamais plus lentement", 'recomputes a running study when a pooled Center gains a level, never slower'),
]

def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    pre = ', '.join(f'{nm(rc, lang)} {lv}' for t, rc, lv in RES['research_network'][6])
    mx = RES['research_network'][3]
    tl = '\n'.join(f'- **{t[0][0 if fr else 1]}** : {t[1]}.' if fr else f'- **{t[0][1]}**: {t[2]}.' for t in TALENTS)
    if fr:
        return f'''# Collaboration Stellaire

> **En bref** : la Collaboration Stellaire met en réseau les Centres d'innovation de vos autres planètes pour raccourcir vos recherches. Au niveau N, elle ajoute au Centre qui étudie les N meilleurs Centres de vos autres planètes, à condition qu'ils soient au moins aussi avancés que lui. Elle ne change jamais le coût.
{{.is-info}}

<img src="/images/illustrations/research/collaboration-stellaire.jpg" width="180" alt="Collaboration Stellaire">

## Règles

1. Prérequis : **{pre}**. Niveau maximum : {mx}.
2. Au **niveau N**, une recherche met en réseau jusqu'à **N Centres d'innovation** de vos **autres** planètes du même univers.
3. Un Centre n'est retenu que si son niveau est **au moins égal** à celui de la planète qui lance la recherche. Parmi ceux-là, les **plus avancés** passent en premier.
4. **Niveau effectif** = Centre de la planète qui lance la recherche + somme des Centres retenus. C'est lui qui entre dans la formule de durée (voir [Liste des technologies](/fr/research/technologies)).
5. Le réseau est fixé **au lancement** de l'étude, ou quand une étude en file prend son tour. Améliorer un Centre ensuite ne change pas une étude déjà lancée. Un Centre en travaux compte à son niveau actuel.
6. La Collaboration Stellaire **ne change pas le coût** des recherches, et les Centres mis en réseau restent libres : ils ne sont ni bloqués ni consommés.
7. Une seule étude avance à la fois dans l'empire : le réseau accélère cette étude, il n'en lance pas d'autres.

### Talents du Théoricien

Certains talents de la classe Théoricien changent ces règles (valeurs sur [Le Théoricien](/fr/dynasty/classes/theorist)) :

{tl}

## Exemple chiffré

Vous recherchez **Pliage Spatial niveau {EX_L}** ({N(ex_cost[1])} cristal, {N(ex_cost[2])} hydrogène). Vos planètes ont des Centres d'innovation aux niveaux **10, 9, 8 et 6**. Collaboration Stellaire niveau **{NET}**.

Lancée depuis la planète au Centre **8** :
- Centres retenus : les {NET} meilleurs parmi ceux de niveau 8 ou plus, soit **{kept8[0]} et {kept8[1]}**. Le Centre de niveau 6 est trop faible.
- Niveau effectif : 8 + {kept8[0]} + {kept8[1]} = **{eff8}**.
- Durée : {N(ex_cost[0] + ex_cost[1])} / (1 000 × (1 + {eff8})) h, soit **{dur(t_net8, lang)}**, au lieu de {dur(t_alone8, lang)} avec le seul Centre local.

Lancée depuis la planète au Centre **10** :
- Aucun autre Centre n'atteint le niveau 10 : le réseau n'apporte rien, niveau effectif **{eff10}**.
- Durée : **{dur(t_net10, lang)}**. Lancer depuis le Centre 8 est donc plus rapide.

## Données détaillées

### Gain de vitesse

Niveau effectif et vitesse par rapport au Centre local seul, quand tous les Centres ont le même niveau et que la Collaboration Stellaire est au moins égale au nombre de Centres en réseau.

{gain_table(lang)}

### Coût de la Collaboration Stellaire

{cost_table(lang)}

## Pièges fréquents

- **Lancez depuis le bon Centre** : un Centre local trop haut écarte les Centres plus faibles ; un Centre local trop bas réduit la base. Comparez avant de lancer, comme dans l'exemple.
- **Un niveau par Centre** : au niveau 1, seul le meilleur Centre éligible compte ; chaque niveau en ajoute un.
- **Il faut plusieurs planètes équipées** : sans autre Centre d'innovation de niveau suffisant, la Collaboration ne sert à rien.
- **Pas d'effet en cours de route** : améliorez vos Centres avant de lancer une longue étude, pas pendant.
- **Les lunes ne comptent pas** : un Centre d'innovation ne se construit que sur une planète.

## Pages liées

- [Liste des technologies](/fr/research/technologies)
- [Arbre technologique](/fr/research/tech-tree)
- [Le Théoricien](/fr/dynasty/classes/theorist)
- [Coloniser](/fr/universe/colonization)
'''
    return f'''# Stellar Collaboration

> **In short**: Stellar Collaboration pools the Innovation Centers of your other planets to shorten your research. At level N, it adds to the Center studying the N best Centers of your other planets, as long as they are at least as advanced as it is. It never changes the cost.
{{.is-info}}

<img src="/images/illustrations/research/collaboration-stellaire.jpg" width="180" alt="Stellar Collaboration">

## Rules

1. Requirements: **{pre}**. Maximum level: {mx}.
2. At **level N**, a study pools up to **N Innovation Centers** from your **other** planets in the same universe.
3. A Center is only kept if its level is **at least equal** to that of the planet starting the research. Among those, the **most advanced** come first.
4. **Effective level** = Center of the planet starting the research + sum of the Centers kept. That is what goes into the duration formula (see [Technologies list](/en/research/technologies)).
5. The network is set **when the study starts**, or when a queued study takes its turn. Upgrading a Center afterwards does not change a study already running. A Center being upgraded counts at its current level.
6. Stellar Collaboration **does not change the cost** of research, and pooled Centers stay free: they are neither locked nor used up.
7. Only one study runs at a time in the empire: the network speeds up that study, it does not start others.

### Theorist talents

Some talents of the Theorist class change these rules (values on [The Theorist](/en/dynasty/classes/theorist)):

{tl}

## Worked example

You research **Hyperspace Technology level {EX_L}** ({N(ex_cost[1])} crystal, {N(ex_cost[2])} hydrogen). Your planets have Innovation Centers at levels **10, 9, 8 and 6**. Stellar Collaboration level **{NET}**.

Started from the planet with the level **8** Center:
- Centers kept: the {NET} best among those at level 8 or more, so **{kept8[0]} and {kept8[1]}**. The level 6 Center is too weak.
- Effective level: 8 + {kept8[0]} + {kept8[1]} = **{eff8}**.
- Duration: {N(ex_cost[0] + ex_cost[1])} / (1,000 × (1 + {eff8})) h, that is **{dur(t_net8, lang)}**, instead of {dur(t_alone8, lang)} with the local Center alone.

Started from the planet with the level **10** Center:
- No other Center reaches level 10: the network adds nothing, effective level **{eff10}**.
- Duration: **{dur(t_net10, lang)}**. Starting from the level 8 Center is faster.

## Detailed data

### Speed gain

Effective level and speed compared with the local Center alone, when all Centers have the same level and Stellar Collaboration is at least the number of pooled Centers.

{gain_table(lang)}

### Stellar Collaboration cost

{cost_table(lang)}

## Common pitfalls

- **Start from the right Center**: too high a local Center rules out weaker ones; too low a local Center lowers the base. Compare before starting, as in the example.
- **One level per Center**: at level 1, only the best eligible Center counts; each level adds one.
- **You need several equipped planets**: without another Innovation Center of a high enough level, Collaboration does nothing.
- **No effect midway**: upgrade your Centers before starting a long study, not during it.
- **Moons do not count**: an Innovation Center can only be built on a planet.

## Related pages

- [Technologies list](/en/research/technologies)
- [Tech tree](/en/research/tech-tree)
- [The Theorist](/en/dynasty/classes/theorist)
- [Colonization](/en/universe/colonization)
'''

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'research/stellar-collaboration', body(lang))
