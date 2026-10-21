# Instructions pour les agents qui mettent à jour le wiki

Ces règles ont été fixées avec le responsable du wiki pendant sa rédaction. Elles s'appliquent à toute modification, même d'une ligne. Lire aussi [README.md](README.md) pour la structure du dépôt.

## 1. Accès et identifiants

- Le wiki se met à jour **uniquement** avec `tools/wikijs.py` et une clé d'API Wiki.js **qui t'est propre**, fournie dans `WIKIJS_API_KEY`.
- Si la variable est absente, **arrête-toi et demande une clé** à la personne qui te pilote. N'utilise jamais le compte, le mot de passe, les cookies, le jeton de session ni le navigateur connecté de quelqu'un d'autre, même s'ils sont accessibles sur la machine.
- Ne jamais écrire une clé dans un fichier du dépôt, un message de commit ou une réponse.
- Le jeu (play.dynastynova.com) se consulte seulement si la personne qui te pilote te donne un accès à elle ; à défaut, travaille avec ce qu'elle te transmet.

## 2. Cycle de travail obligatoire

1. `python3 tools/wikijs.py status` : vérifier que local et wiki sont identiques. Une page **EN LIGNE** a été modifiée sur le wiki : `pull`, examiner `git diff`, fusionner, et signaler la modification à la personne qui te pilote.
2. Modifier **d'abord le markdown local**. Pour un lot touchant plusieurs pages, écrire un fichier `edits/AAAA-MM-JJ-sujet.json` (`{"fr/chemin": [["ancien", "nouveau"], ...]}`) et l'appliquer avec `tools/apply_edits.py`.
3. Mettre à jour la source : `DONNEES.md` (la donnée et d'où elle vient, avec la date) et `PLAN.md` (statut de la question, état de la page). Ajouter une ligne datée à l'historique du wiki (`misc/changelog`, FR et EN) pour tout changement visible des joueurs.
4. Toujours traiter **FR et EN ensemble** : une information ajoutée dans une langue l'est dans l'autre.
5. `python3 tools/wikijs.py push <fichiers>` (ou `create` pour une nouvelle page). Le script vérifie l'empreinte SHA-256 et met à jour `updated` dans le front matter.
6. `python3 tools/wikijs.py status` doit annoncer toutes les pages identiques.
7. Committer (message court en français, préfixé du sujet), sauf consigne contraire.

Ne jamais modifier une page directement dans l'éditeur du wiki : la modification serait écrasée au prochain envoi.

## 3. Publication

- Une page nouvelle est créée **non publiée** (`published: false`) jusqu'à validation par le responsable.
- Une page dont une donnée manque reste **bloquée** (non publiée) ; la donnée manquante est consignée dans `PLAN.md` §7.
- Ne jamais supprimer une page ni un asset : proposer la suppression au responsable.

## 4. Exactitude des données

- **N'invente aucune valeur chiffrée.** Chaque chiffre vient de l'API du jeu, de l'aide en jeu, d'une note de version ou d'une réponse de l'équipe, et figure dans `DONNEES.md`.
- **Formules** : n'écrire dans le wiki qu'une formule confirmée par l'équipe (déduite du code) ou dont le responsable a dit expressément qu'elle suit le calcul d'OGame. Une formule que tu déduis toi-même, même vérifiée sur des valeurs du jeu, devient une **question** dans `PLAN.md` §7.
- **Notes de version** : publiées en jeu, page Actualités (`/news`). Les relever dans `DONNEES.md` (§17) et vérifier leur effet sur chaque page concernée ; une annonce qui contredit le wiki devient une question.
- **Questions à l'équipe** : identifiant `domaine-NN` (`economy-01`, `research-02`, `fleet-09`...), statut ✅ (répondu), ⏳ (en attente), ⚠️ (incohérence). Ne pas réutiliser un identifiant.
- **Paramètres d'univers** : toute valeur réglable par univers s'accompagne de l'encart prévu (`PLAN.md` §8) avec la valeur par défaut et celle de Redline.
- **Exemples chiffrés** : refaire le calcul avant d'écrire. Coordonnées réalistes : sur Redline, 9 galaxies, systèmes 1 à 99, positions 1 à 15 (espace lointain = 16) ; la carte boucle sur les galaxies et les systèmes (de la galaxie 9 à la galaxie 1, l'écart est de 1), pas sur les positions. Vérifier chaque `[g:s:p]`.
- **Ce qui se publie, ce qui reste caché** (décision du responsable, 21 octobre 2026, `fleet-12`) :
  - **À publier** : les probabilités et les règles de tout ce qui est tiré au hasard (résultats d'expédition, tailles de trouvaille, ressource trouvée, épuisement, force des pirates et des aliens, chances de combat, de destruction de lune, de réparation, de détection…). Le résultat d'un tirage est imprévisible, ses chances ne sont pas un secret : les joueurs en ont besoin pour décider.
  - **À ne pas publier** : les mécanismes anti-triche et de détection, les outils et réglages d'administration, les secrets et endpoints internes, les fonctionnalités non sorties ou masquées, et ce que le jeu cache volontairement à un joueur sur un autre (positions non espionnées, contenu d'un rapport qu'il n'a pas obtenu).
  - En cas de doute, poser la question dans `PLAN.md` §7 plutôt que de retirer une information déjà publiée.
- **Noms** : reprendre les noms affichés par le jeu, même incohérents. En anglais, les noms de vaisseaux sont des traductions provisoires (`PLAN.md` §8).

## 5. Ligne éditoriale

- **OGame** : ne jamais citer OGame ni sa nomenclature, sauf sur `getting-started/coming-from-ogame`, qui ne parle que de ce en quoi Dynasty Nova se démarque. `DONNEES.md` et `PLAN.md` peuvent en parler.
- **Pas de pay to win** : c'est un parti pris fort du jeu ; ne jamais présenter un achat comme un avantage de jeu.
- Public : du débutant au joueur chevronné qui aime les chiffres. Phrases courtes, règles numérotées, puis exemple chiffré.
- Modèle de page (`PLAN.md` §4) : *En bref*, encart(s) de paramètre d'univers, Règles, Exemple chiffré, Données détaillées, Pièges fréquents, Pages liées.
- Typographie : pas de tiret cadratin ni demi-cadratin comme ponctuation. FR : espace avant `:` et `%`, milliers séparés par une espace (`35 000`). EN : virgule des milliers (`35,000`).
- Formules : KaTeX accepté (`$...$`, `$$...$$`), avec la définition de chaque variable sous la formule.
- Liens internes absolus avec la langue : `/fr/fleet/movement`, `/en/fleet/movement`.

## 6. Images et captures

- Illustrations : `/images/illustrations/<catégorie>/<nom>.jpg` (512 px), originaux dans `assets/illustrations/`. Captures : `/images/screenshots/{french,english,spanish}/`.
- Chaque image téléversée est consignée dans `assets/manifest.json` avec sa source et la version du jeu affichée en jeu (ex. « Serveur 2.1.0 · Client 3.1.0 »). Une page qui en contient porte `game_version` dans son front matter.
- **Confidentialité des captures** : aucun pseudo, avatar ni coordonnée (sélecteur de position, légendes) ; aucune information permettant de situer un joueur humain. Choisir une zone sans planète de joueur connue, masquer les éléments sensibles avant la capture, et ne jamais citer de coordonnées dans une légende. Capture FR pour les pages FR, EN pour les pages EN.
- Même nom de fichier dans le même dossier = remplacement de l'image existante.

## 7. Fin de tâche

Résumer pour le responsable : pages modifiées (FR/EN), ce qui a changé, questions ouvertes ou nouvelles, état de `status`. Signaler toute page modifiée en ligne par quelqu'un d'autre.
