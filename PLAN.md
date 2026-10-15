# Wiki joueurs Dynasty Nova : plan de travail

Version 3, 2 octobre 2026 (réponses de l'équipe intégrées). Univers de référence : **Redline** (vitesses ×1).
Données brutes et sources : [DONNEES.md](DONNEES.md).

Légende : ✅ confirmé (équipe ou jeu) · 🔶 à vérifier · ❌ manquant.
Chaque question porte un identifiant (`economy-01`, `fleet-03`…) : il suffit de répondre « economy-01 : … ».

---

## 1. Ce que la collecte a changé

**Confirmé par le jeu, en plus de ton brief**
- Catalogues complets : 17 bâtiments (+3 lunaires), 17 recherches, 14 vaisseaux, 10 défenses et missiles, avec coûts, prérequis, statistiques, tirs rapides et niveaux maximum.
- **Formules de coût, de durée et de production identiques à OGame** (vérifiées sur plusieurs niveaux), sauf la consommation du Condensateur (moitié de celle d'OGame).
- **Statistiques des vaisseaux et défenses identiques à OGame.** Nouveauté : le facteur de distorsion (`warpFactor`).
- **Niveaux maximum** propres à Dynasty Nova (Centre d'innovation 12, Dock orbital 12, Fabrique d'automates 10, entrepôts 20, recherches de 8 à 25).
- Lunes, Base lunaire, Phalange, Porte de saut, Destruction de lune : **existent**.
- Station de réparation : récupère 31,5 % à 37,8 % des vaisseaux détruits.
- Missiles : les défenses détruites par missile sont **perdues définitivement**.
- Pillage : 50 % du stock à chaque attaque, taux fixe (`combat-05`).
- Mode vacances : 48 h minimum, conditions de départ.
- Abandon de colonie et dégradation des planètes abandonnées : règles chiffrées.
- Alliances riches : pactes, fair-play, guerres votées, station, talents, missions d'alliance.
- Univers PvP : boutique uniquement cosmétique.
- Didacticiel : 7 paliers de quêtes.
- 8 missions de flotte. **Ni attaque groupée ni défense alliée** (`fleet-05`).

**Points de vigilance**
- Les **vaisseaux n'ont pas de nom traduit** : l'interface EN et ES affiche les noms français (question `glossary-01`).
- Les noms EN des recherches ne correspondent pas aux noms FR et ES (`glossary-02`).
- Protection des débutants : le texte du jeu fait foi, le plus fort est aussi protégé (`players-03`).
- Wiki : l'espagnol n'est pas activé, et la création de pages est encore refusée (§6).

---

## 2. Conventions multilingues

1. Un seul chemin en anglais, identique dans les langues : `/fr/fleet/ships`, `/en/fleet/ships`, `/es/fleet/ships`. Wiki.js relie automatiquement les traductions.
2. Les noms des unités sont ceux qu'affiche le jeu dans chaque langue (table dans [DONNEES.md §1](DONNEES.md)). Le code technique est donné entre parenthèses à la première mention dans les pages « chiffres ».
3. Tant que les vaisseaux ne sont pas traduits, les pages EN utilisent les noms anglais provisoires (§8), avec le nom français affiché en jeu entre parenthèses.
4. Valeurs dépendant de l'univers : toujours dans l'encart standard « paramètre d'univers » (§8).
5. Rédaction FR d'abord, puis EN et ES dès validation.

---

## 3. Arborescence

Chaque page porte un identifiant de page (P-xx). Abréviations : *[B]* = ton brief, *[J]* = relevé dans le jeu.

### `home`
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-00 | `home` | Accueil | Portail par profil : débutant, ancien d'OGame, joueur « chiffres ». Lien Discord. | ✅ | |

### `getting-started`, bien démarrer
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-01 | `getting-started` | Bien démarrer (index) | Sommaire de la rubrique. | | |
| P-02 | `getting-started/first-steps` | Premiers pas | Les premières actions, appuyées sur le didacticiel et la FAQ du jeu. | Quêtes, FAQ [J] | `start-01` |
| P-03 | `getting-started/tutorial-quests` | Le didacticiel (quêtes) | Les 7 paliers, objectifs, récompenses, expérience. | Quêtes [J] | `start-02`, `start-03` |
| P-04 | `getting-started/interface` | L'interface | Menus, barre de ressources, cartes de bâtiments. | Textes d'aide [J] | captures d'écran |
| P-05 | `getting-started/glossary` | Glossaire et nomenclature | Table FR / EN / ES / code / OGame. **Rédigée FR + EN le 2 octobre, à valider.** | [J] complet | |
| P-06 | `getting-started/coming-from-ogame` | Vous venez d'OGame ? | Toutes les différences, tenues à jour. | [B] + [J] | `ogame-01` |
| P-07 | `getting-started/faq` | FAQ | Questions courtes, renvois. | FAQ du jeu [J] | |

### `universe`, univers et planètes
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-10 | `universe` | Univers (index) | | | |
| P-11 | `universe/universes` | Les univers | Paramètres d'un univers, Redline, calendrier. | Code + [J] | `universe-13` |
| P-12 | `universe/coordinates` | Coordonnées | `[galaxie:système:position]`, 9 × 99 × 15, plus l'espace lointain au-delà de la position 15. | [B] + [J] | `universe-03` |
| P-13 | `universe/galaxy-view` | La vue galaxie | Lignes, statuts, débris, quota d'attaques, sondage rapide, partage de position. | [B] + [J] | `universe-04` |
| P-14 | `universe/planets` | Planètes : taille, température, type | Cases, température, types, bonus de position. | [J] partiel | `universe-05`, `universe-06` |
| P-15 | `universe/colonization` | Coloniser | Pionnier spatial, Cosmologie appliquée, emplacements de colonie. | [B] + [J] | `universe-07` |
| P-16 | `universe/abandoning-a-planet` | Abandonner une colonie | Conditions, conséquences, dégradation. | [J] complet | |
| P-17 | `universe/moons` | Les lunes | Formation, Base lunaire, cases, diamètre. **Rédigée d'après le code le 15 octobre 2026, non publiée.** | Code | |

### `economy`, ressources et bâtiments
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-20 | `economy` | Économie (index) | | | |
| P-21 | `economy/resources` | Les ressources | Métal, cristal, hydrogène, production continue. | [B] + [J] | |
| P-22 | `economy/energy` | L'énergie | Sources, consommation, déficit proportionnel, taux de fonctionnement. | [B] + [J] | `economy-01`, `economy-02` |
| P-23 | `economy/storage` | Le stockage | Capacités, arrêt de production quand c'est plein. | [J] complet | |
| P-24 | `economy/buildings` | Liste des bâtiments | Tableau : rôle, coût niv. 1, facteur, niveau max, prérequis. | [J] complet | `economy-03` |
| P-24b | `economy/building-levels` | Annexe : les bâtiments niveau par niveau | Coût, énergie, production de chaque niveau (50 au plus), générée par `tools/building_tables.py`. | Code (DONNEES §4) | `formula-01`, `formula-02`, `formula-06` |
| P-25 | `economy/formulas` | Formules de l'économie | Coûts, durées, production, points. | [J] vérifié | `economy-04` |
| P-26 | `economy/build-queue` | Files de construction | 2 ordres (5 en Premium), annulation, remboursement. | [J] | `economy-05`, `economy-06` |
| P-27 | `economy/demolition` | Démolir un bâtiment | Retour au niveau précédent, case libérée. | [J] | `economy-07` |
| P-28 | `economy/repair-station` | Station de réparation | Part récupérée par niveau. | [J] complet | `economy-08` |
| P-29 | `economy/terraformer-and-logistics` | Modulateur planétaire et Centre logistique | Effets. | [J] coûts | `economy-09`, `economy-10` |

### `research`, recherche
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-30 | `research` | Recherche (index) | En bref et sommaire. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-31 | `research/technologies` | Liste des technologies | Tableau : effet, coût niv. 1, facteur, max, prérequis ; formule de durée, une étude à la fois, Second centre d'innovation, énergie de Manipulation Gravitationnelle, changements de moteur. Réécrite d'après le code le 15 octobre 2026 (`tools/research_pages/`). | code | `research-03` |
| P-32 | `research/tech-tree` | Arbre technologique | Schéma Mermaid des prérequis entre technologies, chemins complets calculés pour les 14 vaisseaux, 10 défenses, bâtiments et 17 technologies, déblocages. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-33 | `research/stellar-collaboration` | Collaboration Stellaire | Réseau de Centres d'innovation (`ResearchNetworkCalculator`), talents du Théoricien, gains et coûts. Réécrite d'après le code le 15 octobre 2026. | code | `research-04` |

### `fleet`, flotte
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-40 | `fleet` | Flotte (index) | Sommaire avec une ligne par page. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-41 | `fleet/ships` | Liste des vaisseaux | 14 vaisseaux : coûts, durées de base, statistiques, changements de moteur, prérequis, points militaires. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-42 | `fleet/rapid-fire` | Tirs rapides | Table complète, mécanique de la chaîne. Réécrite d'après le code le 15 octobre 2026. | code | `combat-01` |
| P-43 | `fleet/orbital-dock` | Dock orbital (chantier) | Files parallèles, paiement unité par unité, livraison, durées, annulation, blocages. Rédigée d'après le code le 15 octobre 2026, **non publiée**. | code | `fleet-01`, `fleet-09`, `formula-04` |
| P-44 | `fleet/movement` | Déplacements | Emplacements, vitesse 1 à 100 %, carte circulaire, durée, hydrogène dans les soutes, bonus, rappel, retour. Réécrite d'après le code le 15 octobre 2026. | code | `fleet-02`, `fleet-03`, `fleet-04` |
| P-45 | `fleet/missions` | Les missions | Les 8 missions et les 2 dépôts à la Station stellaire (banque, don à l'alliance). Réécrite d'après le code le 15 octobre 2026. | code | `fleet-05` |
| P-46 | `fleet/expeditions` | Expéditions | Espace lointain, conditions, résultats sans leurs probabilités, taille des trouvailles, épuisement. Réécrite d'après le code le 15 octobre 2026. | code | `fleet-06`, `patch-03`, `patch-04` |
| P-47 | `fleet/jump-gate` | Porte de saut | Recharge, coût, lunes du joueur seulement, talents. Réécrite d'après le code le 15 octobre 2026. | code | `fleet-07` |

### `defense`, défense
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-50 | `defense` | Défense (index) | Résumé de la rubrique. **Réécrite d'après le code le 15 octobre 2026.** | code | |
| P-51 | `defense/defenses` | Liste des défenses | 8 défenses : coûts, statistiques, prérequis, durées par niveau de Dock, file, paiement, tirs rapides subis. **Réécrite d'après le code le 15 octobre 2026** (`tools/defense_pages`). | code | |
| P-52 | `defense/shield-domes` | Barrière et Dôme | Uniques, rôle, résistance face aux Ogives. **Réécrite d'après le code le 15 octobre 2026.** | code | |
| P-53 | `defense/missiles` | Missiles | Arsenal, cases, portée, vol, cibles, interception, dégâts et ordre des cibles. **Réécrite d'après le code le 15 octobre 2026**, `defense-03` tranchée. | code | |

### `combat`, combat
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-60 | `combat` | Combat (index) | | | |
| P-61 | `combat/how-combat-works` | Déroulement d'un combat | Statistiques effectives, rounds, tirs rapides, boucliers, explosions. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-62 | `combat/battle-report` | Lire un rapport de combat | Contenu, vue partielle, partage. Réécrite d'après le code le 15 octobre 2026. | code | captures |
| P-63 | `combat/plunder` | Pillage | 50 % fixe, soute, talents. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-64 | `combat/debris` | Champs de débris (« Champ de ruines » en jeu) | Taux réglables, formation et taille des lunes. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-65 | `combat/defense-rebuild` | Reconstruction des défenses | Tirage à 70 % par unité, L'Héritage, plafond 85 %. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-66 | `combat/simulator` | Simulateur | Import de rapport, hypothèses, 50 combats, limites. Réécrite d'après le code le 15 octobre 2026. | code | |
| P-67 | `combat/moon-destruction` | Destruction de lune | Colossus, deux tirages, talents. Réécrite d'après le code le 15 octobre 2026. | code | |

### `espionage`, espionnage
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-70 | `espionage` | Espionnage (index) | Réécrite d'après le code le 15 octobre 2026. | [E] | |
| P-71 | `espionage/spying` | Espionner | Éclaireur, sondage rapide, détail, interception, vision partagée d'alliance, alerte. **Réécrite d'après le code le 15 octobre 2026.** | [E] | `spy-05` |
| P-72 | `espionage/spy-report` | Lire un rapport d'espionnage | Sections, mention « Niveau d'espionnage insuffisant », historique, alerte d'intrusion. **Réécrite d'après le code le 15 octobre 2026.** | [E] | |
| P-73 | `espionage/sensor-phalanx` | Phalange de capteur | Portée (galaxie qui boucle), coût, prérequis, invisibilités. **Réécrite d'après le code le 15 octobre 2026.** | [E] | |

### `players`, joueurs et règles
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-80 | `players` | Joueurs (index) | | | |
| P-81 | `players/rankings` | Classements et points | 4 classements de joueurs et 2 d'alliance, 1 point par 1 000 ressources du coût de catalogue, tous les vaisseaux au militaire. Réécrite d'après le code le 15 octobre 2026 (`tools/players_pages`). | [J] + code | |
| P-82 | `players/beginner-protection` | Protection des débutants | Protection nouvel arrivant (7 jours, fixe), paliers de points, inactivité. Réécrite d'après le code le 15 octobre 2026. | [J] + code | |
| P-83 | `players/attack-limit` | Limite d'attaques | 6 par tranche fixe de 24 h, missiles compris, destruction de lune exclue. Réécrite d'après le code le 15 octobre 2026. | [J] + code | |
| P-84 | `players/vacation-mode` | Mode vacances | 48 h min, conditions, univers privé gelé. Réécrite d'après le code le 15 octobre 2026. | [J] + code | |
| P-85 | `players/inactivity` | Inactivité | Délai par univers, activité par univers, succession du fondateur. Réécrite d'après le code le 15 octobre 2026. | [J] + code | `players-14` |
| P-86 | `players/alliances` | Alliances | Créer, rejoindre, rangs, quarantaine, capacité. | [J] | `players-07` |
| P-87 | `players/pacts-and-wars` | Pactes, fair-play et guerres | | [J] | |
| P-88 | `players/alliance-missions` | Missions et station d'alliance | Trésorerie par convois, entraide, station à 3 paliers, missions V2 (inscription, effort relatif), talents. Réécrite d'après le code le 15 octobre 2026. | [J] + code | `players-08`, `players-12` |
| P-89 | `players/messages-and-reports` | Messagerie et rapports | Chat, rapports gardés 7 jours, partage (30 jours), réglages des rapports. Réécrite d'après le code le 15 octobre 2026. | [J] + code | |
| P-90 | `players/game-rules` | Règlement | | | `players-09` |

Nouvelle page (15 octobre 2026, non publiée) :

| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-106 | `economy/stellar-bank` | Banque stellaire | Vendre et acheter des ressources contre des Crédits, cours, taxe, livraisons. | code | `bank-01` |

### `misc`, divers
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-91 | `misc` | Divers (index) | | | |
| P-92 | `misc/maintenance` | Maintenance | | [B] + [J] | `misc-01` |
| P-93 | `misc/premium` | Premium, boutique, Points stellaires | PvP = cosmétique seulement. | [J] | `misc-02` |
| P-94 | `misc/empire-and-bookmarks` | Vue Empire et favoris | Favoris avec note, page Favoris, envoi de flotte vers un favori. | [J] + note de version | |
| P-95 | `misc/referral` | Parrainage | | [J] | `misc-03` |
| P-97 | `misc/changelog` | Historique du wiki | | | |

### `dynasty`, dynastie et talents (ajoutée le 6 octobre 2026, non publiée jusqu'à la sortie)
| ID | Chemin | Page | Contenu | Sources | Manque |
|---|---|---|---|---|---|
| P-100 | `dynasty` | Dynastie et talents (index) | Modèle dynastie + classe + arbre commun, sommaire. | Code [E] | |
| P-101 | `dynasty/dynasties` | Les dynasties | L'Héritage, L'Accord, Le Chœur ; traits et classes exclusives. | Code [E] | |
| P-102 | `dynasty/classes` | Les classes | Les 10 classes, maîtrise, changement de classe. | Code [E] | |
| P-103 | `dynasty/talents` | Les talents | Deux arbres, points par niveau, portes, brouillon, réinitialisation, plafonds et accents. | Code [E] | `dynasty-04` |
| P-104 | `dynasty/common-tree` | L'arbre commun | Prospérité, Exploration, Logistique, builds à 50 points. | Code [E] | |
| P-105 à P-114 | `dynasty/classes/<code>` | Un arbre de classe par page | `admiral`, `builder`, `energist`, `theorist`, `navigator`, `shadow`, `archivist`, `veteran`, `symbiote`, `oracle` : 3 branches × 9 rangées, exemples, builds à 25 points. | Code [E] | `dynasty-05` à `dynasty-20` |

[E] = code du jeu fourni par l'équipe (règles « déduites du code », AGENTS §4). Détail des données : [DONNEES.md §18](DONNEES.md).

Pages par unité (17 bâtiments, 17 recherches, 14 vaisseaux, 10 défenses) : plus tard, sous `economy/buildings/<code>`, `research/technologies/<code>`, `fleet/ships/<code>` et `defense/defenses/<code>`. Les pages de liste suffisent pour le lancement.

---

## 4. Modèle de page

En bref · encart « paramètre d'univers » si besoin · Règles · Exemple chiffré · Données détaillées · Pièges fréquents · Pages liées. **Aucune mention d'OGame**, sauf sur P-06 « Vous venez d'OGame ? », qui ne traite que de ce en quoi Dynasty Nova se démarque. Titres de section dans les trois langues :

| FR | EN | ES |
|---|---|---|
| En bref | In short | En resumen |
| Règles | Rules | Reglas |
| Exemple chiffré | Worked example | Ejemplo numérico |
| Données détaillées | Detailed data | Datos detallados |
| Pièges fréquents | Common pitfalls | Errores frecuentes |
| Pages liées | Related pages | Páginas relacionadas |

---

## 5. Ordre de rédaction (lots 1 et 2 inversés)

**Lot 1, pages catalogue et débutant (données du jeu complètes)**
1. P-05 Glossaire
2. P-41 Vaisseaux, P-42 Tirs rapides
3. P-51 Défenses, P-53 Missiles
4. P-24 Bâtiments, P-25 Formules
5. P-31 Technologies, P-32 Arbre technologique
6. P-03 Didacticiel, P-02 Premiers pas
7. P-06 Vous venez d'OGame ?
8. P-15 Coloniser, P-16 Abandonner, P-14 Planètes
9. P-04 Interface

**Lot 2, règles déjà confirmées**
10. P-82 Protection des débutants (après `players-03`), P-81 Classements
11. P-64 Débris, P-65 Reconstruction
12. P-12 Coordonnées, P-13 Vue galaxie
13. P-83 Limite d'attaques, P-84 Vacances, P-92 Maintenance
14. P-21 Ressources, P-22 Énergie, P-23 Stockage
15. P-73 Phalange, P-47 Porte de saut (débloquées) ; P-17 Lunes bloquée (`universe-09`)
16. P-86 à P-89 Alliances
17. P-93 Premium

**Lot 3, après les réponses de l'équipe**
18. Espionnage (P-71, P-72), Combat (P-61, P-63, P-67)
19. Déplacements et missions (P-44, P-45, P-46)
20. P-90 Règlement, P-85 Inactivité, P-11 Univers
21. Pages par unité, FAQ, index des rubriques

---

## 6. Création sur le wiki

- `wiki-01` ✅ Droits actifs. Arborescence créée le 2 octobre 2026 (FR et EN, non publiée).
- `wiki-02` : espagnol en attente. Les pages ES seront créées dès l'activation.
- `wiki-05` ⏳ **Menu de navigation** : il est en mode statique et ne contient que « Accueil » (mon compte n'a pas accès à sa configuration). À régler par un administrateur : Administration > Navigation > mode **« Arborescence du site »** (Site Tree), qui liste automatiquement rubriques et pages dans chaque langue. En attendant, l'accueil FR et EN contient l'index complet.
- `wiki-06` ✅ Droit `write:assets` actif ; 67 illustrations et 4 captures en ligne. (Ancien point : : le compte peut créer des dossiers de médias mais pas y déposer de fichiers (« You are not authorized to upload files »). À donner : le droit `write:assets` au groupe « Membre ». Dossier prêt : `/game/client-3-1-0`. Plan des images : [assets/manifest.json](assets/manifest.json).)
- `wiki-04` ⏳ Sur les pages EN, l'interface du wiki affiche des clés brutes (« page.unpublished », « actions.edit », « comments.title »). L'administrateur doit installer le pack de langue anglais (Administration > Langues > English > télécharger).
- `wiki-03` ✅ : pages **non publiées** jusqu'à validation.
- [tools/create-tree.js](tools/create-tree.js) a créé les 70 pages squelettes en FR et en EN (accueil exclu), non publiées. Il ignore les pages existantes : on peut le relancer avec `es` quand la langue sera activée.

## 7. Questions pour l'équipe

✅ = répondu · ⏳ = en attente de l'équipe de développement · ⚠️ = réponse à clarifier.

### Généraux
- `general-01` ✅ Pas de liste officielle des divergences avec OGame.
- `general-02` ✅ Les formules peuvent être publiées.
- `general-03` ✅ Le wiki couvre **tous les univers**. Tout paramètre réglable par univers est signalé par l'encart standard (§8).

### Accueil
- `home-01` ✅ Discord : https://discord.gg/mpKjSWFrz

### Bien démarrer
- `start-01` ✅ Conseil officiel : se laisser guider par les quêtes.
- `start-02` ✅ L'expérience servira à la progression du personnage (fonctionnalité à venir).
- `start-03` ✅ Pas de palier après le 7e. Les quêtes ne rapportent de Points stellaires dans aucun univers.

### Glossaire
- `glossary-01` ✅ Les vaisseaux seront traduits. En attendant, le wiki utilise une traduction anglaise des noms français (§8).
- `glossary-02` ✅ On reprend les noms du jeu tels quels, même incohérents entre langues.

### Vous venez d'OGame
- `ogame-01` ✅ Liste officielle fournie (DONNEES §13).

### Univers
- `universe-01` ✅ Type d'univers (andromeda, orion, quantum, vega) et biome (1 à 8) : tirés au hasard, purement cosmétiques. Biome de planète (1 à 6) : cosmétique aussi.
- `universe-02` ✅ (code, 15 octobre 2026) Le code ne porte ni liste ni calendrier : chaque univers est créé avec sa date d'ouverture, et le jeu les affiche à l'écran Univers (compte à rebours, inscriptions fermées). Seuls les univers privés ont une date de fin. P-11 renvoie à cet écran ; tenir une liste dans le wiki reste un choix éditorial. (Question : Liste et calendrier des univers.)
- `universe-03` ✅ Révisé par le code (15 octobre 2026) : **la carte boucle** sur les galaxies et sur les systèmes depuis le 9 octobre 2026 (Backend #509, #513), plus court des deux sens ; les positions ne bouclent pas. Distance entre galaxies : 20 000 × écart. P-12 corrigée. (Ancienne réponse : la carte n'est pas circulaire.)
- `universe-04` ✅ PvE = combats contre des joueurs non humains. Des planètes non joueurs existent sur la bêta, équilibrage en cours.
- `universe-05` ✅ Table par position (taille moyenne ± 15, température, types), planète mère à 163 cases. Voir [DONNEES.md §3](DONNEES.md).
- `universe-06` ✅ Plus une planète est proche du soleil, plus elle est chaude et plus les Capteurs photovoltaïques produisent. Plus elle est loin, plus elle est froide et plus le Condensateur produit d'hydrogène. ✅ Formules : Condensateur × (1,44 − 0,004 × Tmax), Collecteur Tmax / 4 + base, Capteurs × (1 + T actuelle / 100). Les +23 % de ma planète sont confirmés (T = 23 °C).
- `universe-07` ✅ Cosmologie appliquée 1 = planète mère + 1 colonie, puis 1 colonie de plus tous les 2 niveaux. ✅ Confirmé par le code (15 octobre 2026) : planètes = 1 + partie entière((N + 1) / 2), lunes non comptées.
- `universe-08` ✅ Comme OGame : 1 % par 100 000 débris, plafond 20 %.
- `universe-09` ✅ Comme OGame. ✅ (code, 15 octobre 2026) Base lunaire : 20 000 métal, 40 000 cristal, 20 000 hydrogène au niveau 1, facteur 2, aucun prérequis, pas de niveau maximal ; premier bâtiment obligatoire d'une lune, non démolissable ; 3 cases ouvertes et 1 occupée par niveau, plafond partie entière((diamètre / 1 000)²). P-17 rédigée d'après le code, laissée non publiée pour relecture.

### Économie
- `economy-01` ✅ Taux de fonctionnement par pas de 10 %.
- `economy-02` ✅ Le Collecteur solaire produit selon la position (température).
- `economy-03` ✅ Niveaux maximum définitifs : aller plus haut ne débloquerait rien.
- `economy-04` ✅ Hydrogène : 10 × N × 1,1^N × (1,44 − 0,004 × Tmax).
- `economy-05` ✅ 80 % × (temps restant / durée totale) pour bâtiments et recherches ; 80 % des unités non livrées pour vaisseaux et défenses ; rien pour une commande encore en file.
- `economy-06` ✅ Les ordres en file sont payés au lancement.
- `economy-07` ✅ La démolition retire les points, ne coûte et ne rend rien, dure la moitié du temps de construction.
- `economy-08` ✅ Règles complètes (part, délai 30 min à 12 h, vaisseaux hors stock pendant la réparation). ✅ Le wiki s'arrête au niveau 10.
- `economy-09` ✅ Le Modulateur planétaire ajoute des cases. Il ne consomme pas d'énergie en fonctionnement. ✅ 5 cases par niveau, +1 aux niveaux pairs (table complète). ✅ 1 000 énergie requise au niveau 1 : seuil de production, non consommé.
- `economy-10` ✅ Le Centre logistique agrandit les entrepôts de 10 % par niveau et n'est plus un prérequis de Diplomatie Stellaire. P-29 rédigée.

### Recherche
- `research-01` ✅ Effets détaillés (DONNEES §11.1). Calcul Quantique : 1 + niveau emplacements de flotte. Cosmologie : bases = 1 + partie entière((N + 1) / 2), ce qui confirme `universe-07`. Confirmé et complété par le code le 15 octobre 2026 (DONNEES §5, « Relevé dans le code ») : Plasma 1 / 0,66 / 0,33 % par niveau, Science Énergétique (Réacteur), portée des missiles, changements de moteur.
- `research-02` ✅ N meilleurs Centres des autres bases au niveau N, s'ils sont au moins au niveau du Centre local. Confirmé par le code le 15 octobre 2026 (`ResearchNetworkCalculator`) : réseau fixé au lancement, Centre local d'au moins 1, talents du Théoricien en plus.
- `research-03` ⏳ (code, 15 octobre 2026) Le Récupérateur doit passer au Moteur Magnétique au niveau 17 de cette recherche (`ship.reactor_upgrades`), mais Moteur Magnétique plafonne au niveau 15 : ce changement de moteur est inatteignable. Voulu (seul le passage à la Navigation Transdimensionnelle 15 compte) ou niveau à corriger ? Le wiki ne cite que le passage atteignable.
- `research-04` ⏳ (texte du jeu, 15 octobre 2026) L'aide du réseau en jeu (`pages.research.network.description`, FR et EN) parle « du Centre d'innovation le plus avancé de votre empire », alors que la Collaboration Stellaire en met jusqu'à N en réseau (N = son niveau). À remonter à l'équipe ; le wiki suit le code.

### Flotte
- `fleet-01` ✅ (corrigé par le code le 15 octobre 2026) Une commande de vaisseaux ou de défenses est vérifiée en entier quand elle est passée, puis chaque unité est payée à son entrée en production (voir `fleet-09`) ; bâtiments et recherches payés au lancement. P-43 et P-41. (Ancienne réponse : payés par unité à la mise en file.)
- `fleet-02` ✅ Statistique réservée, **sans effet** (toujours lue par aucun calcul, code du 15 octobre 2026).
- `fleet-03` ✅ (code, 15 octobre 2026) Vitesse réglable de **1 % à 100 %, par pas de 1** (l'ancien pas de 10 % est périmé). Formules de distance, durée et consommation confirmées ; la carte est circulaire pour galaxies et systèmes, et l'hydrogène du voyage occupe la soute (DONNEES « Flotte (code, 15 octobre 2026) »). Retour payé au départ, sauf Colonisation et Stationnement.
- `fleet-04` ✅ (code, 15 octobre 2026) Rappel possible à l'aller et pendant le maintien d'une expédition, jamais au retour ni pour un dépôt à la Station stellaire. Retour en autant de temps que l'aller déjà volé. L'hydrogène n'est pas remboursé (sauf talent).
- `fleet-05` ✅ (le terme « Attaque groupée » existe dans les traductions du jeu) Attaque groupée et défense alliée possibles **uniquement au sein d'une alliance**. ⏳ L'équipe vérifie si c'est implémenté : elles n'apparaissent pas dans les 8 missions du jeu. Non documenté d'ici là.
- `fleet-06` ✅ (code, 15 octobre 2026) Note de version : espace lointain, résultats possibles, taille des trouvailles, épuisement. Durée, nombre simultané, plafond lié au meilleur joueur et seuils d'épuisement (10 et 25 sur 24 h) tirés du code et publiés. Les probabilités des résultats, des tailles et l'effet chiffré de l'épuisement sont des tirages cachés : **retirés** de P-46 (voir `fleet-12`).
- `fleet-07` ✅ Table de recharge, coût, prérequis (DONNEES §11.6), confirmés par le code le 15 octobre 2026 ; sauts entre lunes du même joueur seulement, pas de niveau maximum.

### Défense
- `defense-01` ✅ Barrière et Dôme : 70 % de chances de reconstruction. L'équipe confirme pour toutes les défenses : « chaque unité de défense détruite a 70 % de chance d'être réparée ». Voir `combat-09`.
- `defense-02` ✅ 10 cases par niveau ; Intercepteurs 1 case, Ogives 2.
- `defense-03` ✅ (code, 15 octobre 2026) Portée : 5 × Moteur Magnétique − 1 systèmes, dans la même galaxie seulement, distance mesurée sur l'anneau des systèmes. Vol : 30 s par système, 30 s au moins. Interception : un Intercepteur abat une Ogive, sans tirage, avant les dégâts, et il est consommé. Dégâts : 12 000 × (1 + 0,1 × Systèmes Offensifs) par Ogive arrivée, mis en commun, dépensés sur bouclier + coque de chaque défense par ordre de résistance (cible désignée d'abord), unités entières seulement, lignes trop chères sautées. Voir DONNEES §7.

### Combat
- `combat-01` ✅ Même fonctionnement qu'OGame (tours, tirs, cibles, tirs rapides).
- `combat-02` ✅ Règle du 1 %, absorption puis coque, régénération à chaque round. Barrière et Dôme : boucliers individuels, pas global.
- `combat-03` ✅ (code, 15 octobre 2026) Les dégâts de coque ne durent que le temps du combat : seuls les boucliers se rechargent entre les rounds, et après le combat le jeu ne garde que les quantités, donc une unité survivante repart intacte. Écrit sur P-61 (DONNEES §11.4, « Relevé dans le code »). (Question : Réparation des unités endommagées.)
- `combat-04` ⚠️ (code, 15 octobre 2026) Le taux de 50 % est une **constante du code** (`LootRate`), pas un paramètre d'univers : l'encart est retiré de P-63. Ancienne réponse : Pillage de 50 % de chaque ressource par défaut, **paramètre d'univers**. ✅ Pas d'ordre : réduction proportionnelle si la soute est trop petite. Butin uniquement en cas de victoire.
- `combat-05` ✅ Taux fixe de 50 %, dégressif de fait sur le stock. La limite d'attaques fonctionne par tranche de 24 h fixe (pas glissante).
- `combat-06` ✅ Les vaisseaux civils détruits produisent des débris. ✅ Les débris ne disparaissent jamais.
- `combat-07` ✅ Reconstruction des défenses : 70 % fixe.
- `combat-08` ✅ Formules OGame, un combat d'abord, tirages sur victoire nette (DONNEES §11.4).
- `combat-09` ✅ Tirage indépendant à 70 % par unité. **P-65 débloquée.** (ta question) Reconstruction : chance de 70 % par unité, ou 70 % arrondi à l'inférieur ? Avec 2 Barrières détruites, combien reviennent ? ⚠️ `defense-01` (« 70 % de chances ») et `combat-07` (« fixe ») se contredisent. Le brief disait « 10 canons détruits → 7 reconstruits ».

### Espionnage
- `spy-01` ✅ Formule et paliers (DONNEES §11.5). Revérifié dans le code le 15 octobre 2026 : inchangé ; les talents d'alliance comptent aussi dans le risque (DONNEES « Espionnage (code, 15 octobre 2026) »).
- `spy-02` ✅ Formule bornée 5 à 25 %, un tirage pour toute la vague.
- `spy-03` ✅ Le joueur espionné est prévenu. Précisé par le code le 15 octobre 2026 : sans nom si la vague passe, identifié ou localisé si elle est abattue ; pas d'alerte sur une planète abandonnée, en vacances ou si le joueur a désactivé ces alertes.
- `spy-04` ✅ Portée niveau² − 1 systèmes, 5 000 hydrogène par scan. ⚠️ corrigé le 15 octobre 2026 : la portée boucle sur les systèmes de la galaxie (le code mesure la distance par le plus court côté de l'anneau), contrairement à « carte non circulaire » ; missions Espionnage et Recyclage invisibles, trafic de la lune invisible.
- `spy-05` ⏳ **Éditoriale, au responsable** : la formule du contre-espionnage (5 à 25 %) est publiée depuis le 2 octobre (`spy-02`) et la réécriture la garde. La consigne « pas de probabilités ni de tirages cachés » invite à la retirer ; un talent de l'Ombre affiche d'ailleurs ce risque en jeu. La réécriture ne publie pas les chances du second tirage (identifié ou localisé). Garder la formule, ou ne donner que la fourchette 5 à 25 % et les cas à risque nul ?
- `spy-06` ⏳ **Éditoriale, au responsable** : le code mesure toutes les distances sur une carte qui boucle (galaxies et systèmes), alors qu'AGENTS.md §4 et plusieurs pages disent « la carte n'est pas circulaire ». P-73 suit le code ; AGENTS.md n'est pas modifié dans ce lot (fichier commun aux rubriques).

### Joueurs
- `players-01` ✅ Classement général = économie + recherche + militaire. ✅ (code, 15 octobre 2026) Tous les vaisseaux comptent au militaire, civils compris ; points sur le coût de catalogue.
- `players-02` ✅ Les points baissent quand on perd des unités ou qu'on démolit.
- `players-03` ✅ **Le texte du jeu fait foi** : on ne peut attaquer ni un joueur beaucoup plus faible, ni un joueur beaucoup plus fort, selon la tranche du plus faible. Le brief est corrigé.
- `players-04` ✅ Les espionnages ne comptent pas. Guerres et pactes ne changent ni le combat, ni le pillage, ni la limite.
- `players-05` ✅ L'inactivité ne s'accumule pas pendant les vacances. ✅ Pas de durée maximale, pas de fin automatique. ✅ (code, 15 octobre 2026) Nuance : sans effet pour les attaques, mais la succession du fondateur compte les jours de vacances (perte du siège à 14 jours) ; écrit sur P-84 et P-85.
- `players-06` ✅ Un seul palier, 14 jours par défaut (paramètre d'univers). Pas de suppression ni d'abandon automatique.
- `players-07` ✅ 10 à 50 membres selon la Diplomatie Stellaire du fondateur, +6 avec Ambassades.
- `players-08` ✅ 14 talents (DONNEES §11.7).
- `players-09` ✅ **Aucun règlement publié.** P-90 bloquée tant que l'équipe n'a pas rédigé de règlement (`rules-01`).

### Note de version du 2 octobre 2026
- `patch-01` ✅ (code, 15 octobre 2026) ~~Les 7 jours sont un paramètre d'univers.~~ Non : 7 jours en dur (`NewcomerProtection::DURATION_DAYS`), identiques dans tous les univers. ✅ Les deux protections se cumulent : une attaque doit passer l'une et l'autre (puis la limite d'attaques).
- `patch-02` ⏳ (remonté à l'équipe) Le Premium (files de 5 ordres au lieu de 2) s'obtient avec 350 Points stellaires. Or l'aide du jeu dit qu'en PvP les Points stellaires ne servent qu'au cosmétique, « sans aucun avantage de jeu ». Le Premium est-il disponible dans les univers PvP ? Faut-il corriger le texte de l'aide ?
- `patch-03` ✅ L'Éclaireur n'est pas perdu. Cosmologie Appliquée est requise. Durée sur place, nombre d'expéditions simultanées et coût en hydrogène connus (DONNEES §10).
- `patch-04` ⏳ La note 3.5.0 annonce « Premium : une expédition simultanée de plus pour les abonnés ». C'est un avantage de jeu, alors que le wiki présente le Premium comme du confort et affirme qu'aucun achat ne donne d'avantage de jeu en PvP. L'avantage s'applique-t-il aux univers PvP ? Faut-il nuancer la section « Aucun pay to win » ? (Non reporté dans le wiki en attendant.)

### Nouvelles questions (2 octobre 2026)
- `players-10` ✅ 7 jours sur Redline (constaté, confirmé le 2026-10-06), réglable par univers ; 14 jours par défaut. (Ancienne question : Inactivité : 14 jours par défaut selon l'équipe, mais l'univers Redline renvoie `inactivityDays: 7`. Redline est-il réglé à 7 jours ?)
- `rules-01` ✅ (P-90 bloquée jusqu'à un texte officiel) Qui rédige le règlement (multicompte, sitting, push, partage de compte) et la page de conditions d'utilisation ? Le wiki ne publiera rien tant qu'il n'existe pas de texte officiel.
- `text-01` ✅ Le texte sur le pillage est jugé correct (50 % à chaque fois, donc dégressif de fait). Ne pas parler de l'indicateur d'inactivité. Reste à corriger : DONNEES §11.9.
- `moon-01` ✅ P-47 et P-73 débloquées. (Question : Porte de saut et Phalange sont maintenant entièrement documentées. Peut-on débloquer P-47 et P-73 ? P-17 Lunes reste bloquée faute de données sur la Base lunaire.)

### Formules à confirmer par l'équipe (déduites des valeurs du jeu, pas encore confirmées)

Règle : aucune de ces formules ne va dans le wiki avant confirmation. Les pages concernées n'affichent que des valeurs relevées en jeu.

- `formula-01` ✅ (code, 15 octobre 2026) Exact : mines 30, 20 et 10 × N × 1,1^N, consommation 10 × N × 1,1^N, Condensateur × (1,44 − 0,004 × Tmax), Capteurs 20 × N × 1,1^N × (1 + T actuelle / 100). Rédigé sur P-21, P-22 et P-25. (Question initiale : ⏳ Production et consommation des mines. Les valeurs du jeu suivent : Excavateur minéral 30 × N × 1,1^N métal/h ; Extracteur cristallin 20 × N × 1,1^N cristal/h ; Capteurs photovoltaïques 20 × N × 1,1^N énergie (avant bonus de température) ; consommation d'énergie 10 × N × 1,1^N pour l'Excavateur, l'Extracteur et le Condensateur. Est-ce exact ? Le Condensateur produit-il 10 × N × 1,1^N × (1,44 − 0,004 × Tmax) ?)
- `formula-02` ✅ (code) Exact : 5 000 × partie entière(2,5 × e^(20N/33)), plus 10 000 de la Base planetaire. P-23 et P-25. (Question initiale : ⏳ Capacité des entrepôts : les valeurs suivent 5 000 × partie entière(2,5 × e^(20 × N / 33)), plus 10 000 de la Base planetaire. Est-ce exact ?)
- `formula-03` ✅ (code) Corrigé : (métal + cristal + **hydrogène**) / (2 500 × (1 + Fabrique) × 2^Assembleur) heures ÷ vitesse construction, puis ÷ (1 + bonus de vitesse). P-25. (Question initiale : ⚠️ (audit du 15 octobre 2026 : le code compte métal + cristal + **hydrogène**, voir DONNEES §4 ; statut à trancher dans le lot des formules) Durée de construction d'un bâtiment : les valeurs suivent (métal + cristal) / (2 500 × (1 + Fabrique d'automates) × 2^Assembleur moléculaire) heures, divisé par la vitesse construction de l'univers. Est-ce exact ?)
- `formula-04` ✅ (code) Durée de base de l'unité (catalogue) / ((1 + Dock orbital) × 2^Assembleur) ÷ vitesse chantier, puis ÷ bonus de vitesse, au moins 1 s. Navette de fret : 5 400 s de base, 1 080 s au Dock 4. P-25. (Question initiale : ⏳ (ex `fleet-08`) Durée de construction des vaisseaux et défenses au Dock orbital : quelle formule ? Exemple relevé : une Navette de fret avec Dock orbital 4 et Assembleur 0 prend 1 080 s.)
- `formula-05` ✅ (code) Partie entière(Tmax / 4 + 20) par Collecteur, jamais négatif. P-22 et P-25. (Question initiale : ⏳ Collecteur solaire : l'équipe indique « Tmax / 4 plus sa base d'énergie ». La base vaut-elle 20 (35 relevés à Tmax = 60 °C) ?)
- `formula-06` ✅ (code) Exact, arrondi à l'inférieur par ressource ; l'énergie requise suit le même facteur sauf la Station de réparation (2,5). P-24 et P-25. (Question initiale : ⏳ Coût des bâtiments et recherches : coût du niveau N = coût du niveau 1 × facteur^(N − 1), avec les facteurs relevés (1,5 ; 1,6 ; 1,75 ; 1,8 ; 2 ; 3 ; 5) ? Arrondi appliqué ?)
- `moon-02` ⏳ **À clarifier pour compléter P-73** : coût de construction et prérequis de la Phalange de capteur. P-73 est rédigée sans ces données, et P-17 Lunes reste bloquée faute de données sur la Base lunaire (`universe-09`).

### Nouvelles questions (2 octobre 2026, fin de journée)
- `universe-10` ✅ Position ramenée sur une échelle de 15. (Question : Les systèmes comptent de 9 à 20 positions selon l'univers : comment se répartissent taille moyenne, température et types quand un système n'a pas 15 positions ? (P-14 ne donne que la table à 15 positions.))
- `universe-11` ✅ Pionnier consommé ; la colonie démarre avec les ressources embarquées. (Question : Le Pionnier spatial est-il consommé à la colonisation ? Sa cargaison est-elle déchargée sur la nouvelle colonie ? Avec quelles ressources démarre une colonie ?)
- `players-11` ✅ Oui. (Question : Les missiles tirés (Ogives) font-ils baisser les points militaires du tireur ?)
- `fleet-09` ✅ (code, 15 octobre 2026) Une commande de vaisseaux ou de défenses n'est acceptée que si la planète peut la payer en entier quand elle est passée ; chaque unité est ensuite payée quand elle entre en production, et la commande s'arrête si l'unité suivante ne peut pas être payée (`Base::startNextUnit`). Rédigé sur P-26. (Question initiale : ⏳ Paiement des vaisseaux et défenses : « payés par unité à la mise en file » (`fleet-01`) ou « payés à leur tour, abandonnés sans frais si la base ne peut pas payer » (liste du 2 octobre) ? Un texte du jeu évoque une commande coupée « faute de ressources pour l'unité suivante ». Bloque P-43 avec `formula-04`.)
- `misc-05` ✅ L'attaque aboutit ; seuls les nouveaux départs sont bloqués. (Question : Une flotte d'attaque qui arrive pendant une maintenance : combat différé, annulé, ou retour automatique ?)

- `economy-11` ✅ (code, 15 octobre 2026) Oui, il s'applique aux 10 000 de la Base planetaire, et il s'**additionne** aux autres bonus (Entrepôts fédérés, talents) : DONNEES §4, « Relevé dans le code ». Page `economy/storage` FR et EN complétée. (Question : Le bonus du Centre logistique (+10 % par niveau) s'applique-t-il aussi aux 10 000 de la Base planetaire ? Se cumule-t-il avec le talent Entrepôts fédérés (addition ou multiplication) ?)

- `universe-12` ✅ (code, 15 octobre 2026) Oui, mais **sans arrondi** : la position est lue sur 15 (1 + (p − 1) × 14 / (n − 1)) et le bonus interpolé entre les deux positions voisines ; taille, types et température utilisent, eux, la position arrondie. Pas réglable par univers. Planète mère exclue (sauf part accordée par un talent de dynastie). (Question : Le bonus de position suit-il aussi la mise à l'échelle sur 15 positions dans les univers de 9 à 20 positions ? Est-il réglable par univers ?)
- `universe-13` ⏳ Valeurs Redline non relevées : expéditions (ouvertes ?) et événements cosmiques (météorites, pluies de comètes, impacts géants ; fermés par défaut). P-11 indique « ouvertes » pour les expéditions d'après la note de version.

### Alliances et banque (15 octobre 2026)
- `players-12` ✅ (responsable, 15 octobre 2026) Oui : encart « Par défaut : fermées · Redline : ouvertes » ajouté à P-88. (Question : Les missions d'alliance sont-elles ouvertes sur Redline ? Elles s'ouvrent univers par univers (fermées par défaut, réglage du back-office) ; la page P-88 dit seulement que l'onglet peut manquer.)
- `players-13` ✅ (responsable, 15 octobre 2026) Oui, c'est écrit sur P-87 (règle 3), FR et EN. (Question **éditoriale** : un membre en période d'intégration qui viole un pacte ne coûte aucun point de fair-play à son alliance. Faut-il l'écrire dans le wiki ?)
- `players-14` ⏳ (éditoriale, 15 octobre 2026) L'indicateur « Inactif » est maintenant affiché aux joueurs (badge de la fiche joueur au classement ; aussi calculé pour la galaxie). `text-01` demandait de ne pas en parler tant qu'il n'était pas affiché. Le wiki doit-il le décrire sur P-85 et P-81 ? (Non écrit en attendant.)
- `bank-01` ✅ (responsable, 15 octobre 2026) On laisse comme ça : rien ne change dans le jeu ni dans P-106. (Question **éditoriale** : la boutique appelle « Crédits » l'onglet des packs de Points stellaires et « Ajouter des crédits » sa recharge, alors que les Crédits de la Banque stellaire ne s'achètent pas. Risque de confusion avec un achat qui donnerait un avantage de jeu (voir `patch-04`). P-106 précise que les deux n'ont rien à voir ; à trancher par le responsable, et à remonter à l'équipe (DONNEES §11.9).)

### Divers
- `misc-01` ✅ Les flottes en vol arrivent normalement pendant une maintenance.
- `misc-02` ✅ Prix et contenu du Premium connus (DONNEES §13).
- `misc-03` ✅ 30 Points stellaires quand le filleul atteint 100 points.
- `misc-04` ✅ Consigne levée le 2 octobre au soir : page P-96 `misc/private-universes` créée et publiée.
- `misc-06` ⏳ En partie répondue par les actualités du jeu : formules Escouade (25), Flotte (75), Armada (200), à partir de 4,99 € la semaine. Reste : prix de chaque formule à la semaine et au mois, et de la durée fixe (minimum de jours, remise) ?

---

### Dynastie et talents (6 octobre 2026)
- `dynasty-01` ✅ Le wiki n'annonce aucune date de sortie. Les pages restent non publiées tant que la fonctionnalité n'est pas en jeu ; les modifications des pages existantes sont prêtes dans `edits/2026-10-06-dynasty-release.json`, à appliquer à ce moment-là.
- `dynasty-02` ✅ Ce n'est pas du pay to win : changer de classe ou réinitialiser un arbre ne donne aucune puissance de plus. Les pages donnent les prix sans les présenter comme un avantage.
- `dynasty-03` ✅ Le wiki emploie les noms du jeu, d'après les traductions du client (Centre d'innovation, Récupérateur, Capteurs photovoltaïques, Collecteur solaire, Condensateur d'hydrogène, Dock orbital, Éclaireur…). Les noms des talents restent ceux qu'affiche le jeu.
- `dynasty-04` ✅ Le plafond de classe compte l'arbre commun : Vétéran 15 points (pillage 35 %), Oracle 10 points (pillage 40 %, La cache s'ajoute à Coffres enterrés). Code corrigé (Backend #476). Question initiale : Protection contre le pillage : plafond de classe de 15 points pour le Vétéran (arbre commun compris) ; le plafond de 5 de l'Oracle porte-t-il sur La cache seule ou sur le total ?
- `dynasty-05` ✅ (code) En relatif : × 0,75. Question initiale : Amiral, Vétéran : La lune tient et Briseur de lunes baissent-ils le risque de 25 % en relatif (27 % → 20 %) ou en points ?
- `dynasty-06` ✅ (code) Multiplicatif : part de la Station de réparation × 1,2. Question initiale : Amiral : le « +20 % d'efficacité » de Chantier de démontage s'ajoute-t-il en points à la part de la Station de réparation, ou la multiplie-t-il ?
- `dynasty-07` ✅ Tous les vaisseaux non civils ; le code exclut le Collecteur solaire. Question initiale : Amiral : quels vaisseaux comptent comme « vaisseaux de combat » (Chantier de guerre, Économie de guerre, Rapaces) ? Seulement la catégorie combat (Intercepteur, Assaillant, Corvette, Cuirassé) ou aussi Frappe-orbital, Prédateur, Annihilateur, Colossus stellaire ?
- `dynasty-08` ✅ 24 h glissantes. Remorquage depuis une lune : non traité. Question initiale : Vétéran : le cycle de 24 h de Pluie d'acier est-il glissant ou calendaire ? Amiral : Remorquage pour une flotte partie d'une lune ?
- `dynasty-09` ✅ 49 % de la part qui ne part pas en débris. Question initiale : Énergéticien : La nuit est courte (49 %) s'applique-t-elle à tous les Collecteurs solaires détruits ou seulement à la part qui ne part pas en débris ?
- `dynasty-10` ✅ Le cycle de température suit le mois du calendrier (formule dans DONNEES §18) ; pages `universe/planets` FR et EN précisées. Question initiale : Énergéticien : Plein midi parle du « maximum du mois ». Le cycle mensuel de la température des Capteurs photovoltaïques n'est pas décrit sur le wiki (`economy/energy` parle de la température actuelle).
- `dynasty-11` ✅ Retard comblé ne double que Fonds d'archives (10 + 15 × 2 = 40 %), comme le dit le texte. Code corrigé (Backend #476). Question initiale : Archiviste : Retard comblé double-t-il seulement Fonds d'archives ou toute la vitesse des niveaux connus (plafond de 25 % dans le code) ?
- `dynasty-12` ✅ (code) Additif, après le plafond de 25 % ; ressources créées au retour, le champ n'est pas vidé davantage ; Indemnité ressource par ressource. Question initiale : Archiviste : Épaves fraîches (+20 %) s'ajoute-t-il ou se multiplie-t-il avec Ferrailleur et Tri des métaux ? L'Indemnité est-elle versée ressource par ressource ?
- `dynasty-13` ✅ Civile = n'augmente ni la puissance militaire ni la vitesse des vaisseaux. Question initiale : Théoricien : quelles recherches sont « civiles » pour Prototype ?
- `dynasty-14` ✅ Formation serrée nivelle les vitesses : tous les vaisseaux sauf le plus rapide +15 %, plafonnés au plus rapide (le code, qui n'accélère que le plus lent, donne la même vitesse de flotte). Question initiale : Navigateur : effet exact de Formation serrée sur une flotte de plus de deux types de vaisseaux.
- `dynasty-15` ✅ Depuis le décollage. Question initiale : Navigateur : la fenêtre de retour de Décollage d'urgence (1 h à 3 h) compte-t-elle depuis le décollage ou depuis l'impact ?
- `dynasty-16` ✅ (code) Après les bornes. Question initiale : Ombre : le seuil de 15 % de Prudence se compare-t-il à la chance avant ou après les bornes de 5 % et 25 % ?
- `dynasty-17` ✅ Quand les sondes devraient être détruites, une partie revient. Nuance à ajouter à `espionage/spying` à la sortie. ⚠️ Plafond de survie de l'Ombre à 41 % alors que l'arbre ne monte qu'à 27 %. Question initiale : Ombre : Sondes larguées et Coques muettes contredisent la règle « toute la vague tombe » de `espionage/spying` ; à nuancer sur cette page à la sortie.
- `dynasty-18` ✅ Pas de limite : Écouter loin et Lecture des hangars se cumulent (2 paliers). Code corrigé (Backend #476). Question initiale : Ombre : Écouter loin (trait de L'Accord) et Lecture des hangars ne se cumulent pas (un palier plus tôt au plus par catégorie). Voulu ?
- `dynasty-19` ✅ Ajoutée à `fleet/missions` FR et EN (60 s, jusqu'à 6 min avec l'Oracle). Question initiale : Oracle : l'alerte d'attaque de base (60 s avant l'impact, d'après le code) n'est décrite sur aucune page du wiki.
- `dynasty-20` ✅ Se cumule avec la case des niveaux pairs. Question initiale : Symbiote : la case de plus par niveau de Modulateur planétaire (Terraformeur vivant) se cumule-t-elle avec la case de plus aux niveaux pairs ?

### Flotte (15 octobre 2026)
- `fleet-10` ⏳ (équipe, code) La Destruction de lune ne repasse pas, au départ, les contrôles de l'Attaque (tir ami, protections, limite d'attaques) : seule la vue galaxie retire la mission. Voulu ? Rien n'est écrit dans le wiki.
- `fleet-11` ⏳ (équipe, code) Un joueur qui a désactivé les rapports de recyclage : `RecycleArrivalResolver::resolve()` s'arrête avant de renvoyer la flotte, qui semble rester sur place. Bogue ?
- `fleet-12` ⏳ (**éditoriale**) Les probabilités des résultats d'expédition, des tailles de trouvaille, de la ressource trouvée et l'effet chiffré de l'épuisement étaient publiés sur P-46 ; ce sont des tirages cachés : retirés le 15 octobre 2026. Faut-il aussi les retirer de DONNEES §11.3 (dépôt public) ? Et publier la force typique des flottes pirates et aliens (part de votre flotte selon la taille) ?

## 8. Conventions issues des réponses

### Encart « paramètre d'univers » (`general-03`)

À placer à chaque endroit où une valeur dépend de l'univers. Les valeurs Redline sont celles relevées le 2 octobre 2026.

FR :
```markdown
> **Paramètre d'univers** : cette valeur peut être différente selon l'univers.
> Par défaut : **50 %** · Redline : **50 %**
{.is-info}
```

EN :
```markdown
> **Universe setting**: this value may differ from one universe to another.
> Default: **50%** · Redline: **50%**
{.is-info}
```

Paramètres d'univers repérés : vitesses (économie, construction, recherche, chantier, flotte), taille de la carte, ressources de départ, paliers de protection des débutants et durée d'inactivité, limite d'attaques, taux de débris (vaisseaux, défenses), formation des lunes, règles d'abandon, part pillée.

### Noms anglais provisoires des vaisseaux (`glossary-01`)

Traduction des noms français, à utiliser dans les pages EN (et ES tant que le jeu n'a pas ses noms). Une note sur chaque page EN précise que le jeu affiche encore le nom français.

| Code | FR (jeu) | EN (provisoire) |
|---|---|---|
| small_cargo | Navette de fret | Cargo Shuttle |
| large_cargo | Cargo stellaire | Stellar Freighter |
| colony_ship | Pionnier spatial | Space Pioneer |
| recycler | Récupérateur | Salvager |
| espionage_probe | Éclaireur | Scout |
| solar_satellite | Collecteur solaire | Solar Collector |
| light_fighter | Intercepteur | Interceptor |
| heavy_fighter | Assaillant | Assailant |
| cruiser | Corvette | Corvette |
| battleship | Cuirassé | Battleship |
| bomber | Frappe-orbital | Orbital Striker |
| predator | Prédateur | Predator |
| destroyer | Annihilateur | Annihilator |
| battle_cruiser | Colossus stellaire | Stellar Colossus |

- « Stellar Colossus » est déjà le nom qu'utilisent les textes anglais du jeu (destruction de lune).
- `glossary-03` ✅ Vaisseau : **Interceptor**. Missile : **Interception Missile** dans le wiki EN (le jeu affiche « Interceptors »).


---

## 9. État des pages (2 octobre 2026, fin de journée)

**Publication le 2 octobre 2026 (16:35 à 16:39 UTC)** : 130 pages publiées (65 FR, 65 EN). Restent non publiées les 5 pages bloquées, en FR et en EN. L'accueil FR (`fr/home`) et l'accueil EN (`en/home`, ancienne page de test réutilisée) sont réécrits le 2 octobre (portail et index complet). L'espagnol attend `wiki-02`.

**Publiées** : P-96, P-29, P-02, P-03, P-05, P-06, P-07, P-11, P-12, P-13, P-14, P-15, P-16, P-21, P-22, P-23, P-24, P-26, P-27, P-28, P-31, P-32, P-33, P-41, P-42, P-44, P-45, P-46, P-47, P-51, P-52, P-53, P-61, P-62, P-63, P-64, P-65, P-66, P-67, P-71, P-72, P-73, P-81, P-82, P-83, P-84, P-85, P-86, P-87, P-88, P-89, P-92, P-93, P-94, P-95, P-97, et les 10 pages de rubrique.

**Rubrique `dynasty` (6 octobre 2026)** : 15 pages FR et 15 pages EN rédigées en local (P-100 à P-114), **non créées sur le wiki** (pas de clé d'API sur ce poste) et non publiées tant que la fonctionnalité n'est pas en jeu (`dynasty-01`). À la sortie : `create`, application de `edits/2026-10-06-dynasty-release.json` (déplacements, didacticiel, reconstruction des défenses, accueil), ligne d'historique FR et EN, publication.

**Bloquées** :
| Page | Bloquée par |
|---|---|
| P-00 Accueil | Page déjà publiée : modification à faire avec ton accord |
| P-04 Interface | Captures d'écran FR et EN à fournir |
| P-17 Lunes | Débloquée (`universe-09`, `moon-02` tranchées par le code le 15 octobre 2026) : rédigée, publication à décider à la relecture |
| P-25 Formules de l'économie | Débloquée le 15 octobre 2026 (code) : rédigée, non publiée, en attente de relecture |
| P-43 Dock orbital | Débloquée le 15 octobre 2026 (`fleet-09` et `formula-04` tranchées par le code) : rédigée dans le lot Flotte, non publiée, en attente de relecture |
| P-90 Règlement | `rules-01` : aucun texte officiel |

**Source des pages** : `wiki/pages/<langue>/<chemin>.md`, une copie locale de chaque page (142 fichiers) avec un front matter (`wiki_id`, `path`, `url`, `title`, `updated`…). **Toute modification se fait d'abord en local**, puis est rejouée sur le wiki :
1. écrire la liste de remplacements dans `wiki/edits/<date>-<sujet>.json` ;
2. `python3 tools/apply_edits.py edits/<fichier>.json` (pages locales) ;
3. rejouer la même liste sur le wiki (GraphQL `pages.update`) ;
4. comparer les empreintes (`tools/body_hash.py` en local, SHA-256 du contenu distant) et reporter `updated` dans le front matter.
