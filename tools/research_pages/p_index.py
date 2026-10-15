"""Page d'index research (FR et EN)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from research_lib import *
from write import write

def body(lang):
    if lang == 'fr':
        return f'''# Recherche

**Technologies, arbre technologique et réseau de laboratoires.**

> **En bref** : les {len(RESEARCH)} technologies se recherchent dans un Centre d'innovation et valent pour toutes vos planètes. Une seule étude avance à la fois dans tout l'empire. Sa durée dépend du métal et du cristal du niveau et du niveau effectif du Centre d'innovation, que la Collaboration Stellaire augmente en mettant vos Centres en réseau.
{{.is-info}}

## Pages de cette rubrique

- [Liste des technologies](/fr/research/technologies) : effets, coûts, maxima, prérequis, formule de durée.
- [Arbre technologique](/fr/research/tech-tree) : tout ce qu'il faut atteindre pour chaque bâtiment, technologie, vaisseau et défense.
- [Collaboration Stellaire](/fr/research/stellar-collaboration) : mettre ses Centres d'innovation en réseau.
'''
    return f'''# Research

**Technologies, tech tree and the laboratory network.**

> **In short**: the {len(RESEARCH)} technologies are researched in an Innovation Center and apply to all your planets. Only one study runs at a time across the whole empire. Its duration depends on the level's metal and crystal and on the effective Innovation Center level, which Stellar Collaboration raises by pooling your Centers.
{{.is-info}}

## Pages in this section

- [Technologies list](/en/research/technologies): effects, costs, maximum levels, requirements, duration formula.
- [Tech tree](/en/research/tech-tree): everything you need to reach for each building, technology, ship and defense.
- [Stellar Collaboration](/en/research/stellar-collaboration): pooling your Innovation Centers.
'''

if __name__ == '__main__':
    for lang in ('fr', 'en'):
        write(lang, 'research', body(lang))
