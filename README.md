# Wiki joueurs Dynasty Nova

Sources du wiki joueurs de [Dynasty Nova](https://play.dynastynova.com), publié sur [wiki.dynastynova.com](https://wiki.dynastynova.com) (Wiki.js 2).

Ce dépôt est la **source de vérité** : chaque page du wiki existe ici en markdown. On modifie le fichier, on le pousse sur le wiki, on vérifie que les deux sont identiques, puis on committe.

Un agent IA qui travaille sur ce dépôt doit lire [AGENTS.md](AGENTS.md) avant toute modification.

## Contenu

| Chemin | Rôle |
|---|---|
| `pages/<langue>/<chemin>.md` | Une page du wiki par fichier (`fr`, `en` ; `es` à venir). Front matter avec `wiki_id`, titre, description, tags, dates. |
| `PLAN.md` | Arborescence (P-00 à P-97), modèle de page, conventions, **questions à l'équipe** (§7) et état des pages (§9). |
| `DONNEES.md` | Toutes les données collectées et leur source : API du jeu, aide en jeu, réponses de l'équipe, notes de version. |
| `edits/` | Historique des lots de modifications (`AAAA-MM-JJ-sujet.json`), rejouables avec `tools/apply_edits.py`. |
| `assets/` | Illustrations du jeu (originaux et versions 512 px) et `manifest.json` (source, version du jeu, emplacement sur le wiki). |
| `tools/` | Scripts de synchronisation et de vérification. |

## Outils

| Script | Usage |
|---|---|
| `tools/wikijs.py` | Synchronisation avec Wiki.js : `status`, `push`, `create`, `pull`, `upload`. |
| `tools/apply_edits.py` | Applique un lot de remplacements `[ancien, nouveau]` aux pages locales. |
| `tools/talent_diagrams.py` | Diagrammes Mermaid des arbres de talents, générés depuis les tableaux des pages de classe (compatibles Mermaid 8.8.2). Finitions facultatives : `assets/talent-tree.css`. |
| `tools/body_hash.py` | Empreinte SHA-256 du corps d'une page (sans front matter). |
| `tools/export_to_md.py` | Export initial du wiki vers les fichiers markdown (historique). |

## Accès au wiki

`tools/wikijs.py` s'authentifie avec une **clé d'API Wiki.js** lue dans l'environnement :

```bash
export WIKIJS_API_KEY="<clé dédiée>"
```

Chaque personne ou agent utilise **sa propre clé**, créée par un administrateur dans *Administration > Accès API* avec les droits de lecture et d'écriture sur les pages (et les assets si besoin). Ne jamais committer une clé, ne jamais réutiliser le compte ou la session de quelqu'un d'autre.

## Cycle de modification

```bash
python3 tools/wikijs.py status                       # rien ne doit diverger avant de commencer
python3 tools/apply_edits.py edits/2026-10-06-sujet.json   # ou édition directe des fichiers
python3 tools/wikijs.py push pages/fr/x.md pages/en/x.md
python3 tools/wikijs.py status                       # tout identique
git add -A && git commit -m "sujet : ce qui change"
```

Si `status` signale une page **EN LIGNE**, quelqu'un l'a modifiée directement sur le wiki : `pull`, relire la différence avec `git diff`, garder ce qui est juste, puis pousser.
