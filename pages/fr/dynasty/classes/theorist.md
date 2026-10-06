---
locale: "fr"
path: "dynasty/classes/theorist"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/theorist"
title: "Le Théoricien"
description: "Arbre de classe du Théoricien : Méthode, Réseau, Prototypes."
tags: ["dynasty"]
published: false
---

# Le Théoricien

> **En bref** : « Comprendre avant ». Le Théoricien a toujours une étude en cours et un niveau d'avance. **Méthode** fait que sa file de recherche ne s'arrête jamais, **Réseau** met en commun les Centres d'innovation de ses colonies, **Prototypes** lui fait profiter d'un niveau de recherche avant tout le monde. Classe commune à toutes les dynasties.
{.is-info}

## Règles

1. Le Théoricien est une classe **commune** : toutes les dynasties peuvent la prendre.
2. Son arbre compte **3 branches de 9 rangées** (15 points par branche). Les règles de points, de portes et d'ultime sont celles de tous les arbres de classe : voir [Système de talents](/fr/dynasty/talents).
3. La vitesse de recherche générique, le coût du Pionnier spatial et les colonies jeunes sont dans l'[arbre commun](/fr/dynasty/common-tree) (Exploration). L'arbre du Théoricien ne contient que des mécaniques qui lui sont propres.
4. **Avances au départ** : Fil continu et Départ lancé font partir une étude avec une partie de son temps déjà écoulé. Ensemble, ces avances ne dépassent jamais **10 %** de l'étude. Éclair de génie, Brouillon conservé et Symposium sont hors de ce plafond.
5. **Réseau d'étude** : sans talent, [Collaboration Stellaire](/fr/research/stellar-collaboration) ne met en réseau que les Centres d'innovation au moins aussi avancés que celui de la base qui étudie. Liaison montante et Antenne lointaine acceptent des Centres plus bas.
6. **Prototype** : après la fin d'un niveau de recherche civile ou de propulsion (une recherche civile est une recherche qui n'augmente ni la puissance militaire ni la vitesse des vaisseaux), le joueur profite pendant un temps de l'effet du niveau suivant. Le prototype ne s'applique aux trois technologies de combat qu'avec Prototype de combat (ou Banc d'essai, Spécialité, Révolution).
7. Deux bonus de la classe sont des **accents** (plafond propre, voir [Système de talents](/fr/dynasty/talents)) : la vitesse de construction des Centres d'innovation (Paillasses en kit) et le coût des niveaux de recherche au-delà du 10e (Brevets).

## Exemple chiffré

Étude de référence : **Systèmes Offensifs 10** (409 600 métal, 102 400 cristal), univers à vitesse de recherche ×1, Centre d'innovation 10 sur la planète qui étudie : **46 h 32 min** sans réseau.

**Méthode**
- Fil continu : l'étude, lancée à la suite de la précédente dans la file, part avec 10 % de son temps écoulé : il reste **41 h 53 min**.
- Éclair de génie : un clic avance l'étude de 10 % de son temps total, soit **4 h 39 min** d'un coup. Avec Coup de génie au rang 3 (19 %) : **8 h 50 min**.
- Protocoles au rang 3 (−6 %) : 409 600 → **385 024** métal, 102 400 → **96 256** cristal.

**Réseau** : trois colonies avec des Centres d'innovation 10, 9 et 8, Collaboration Stellaire 3.
- Sans talent, seul le Centre 10 entre dans le réseau : niveau effectif 20, **24 h 22 min**.
- Liaison montante (tolérance de 2 niveaux) : les Centres 9 et 8 entrent, niveau effectif 37, **13 h 28 min**.
- Labos de campagne au rang 3 : chaque Centre du réseau compte 3 niveaux de plus, niveau effectif 46, **10 h 53 min**.
- Bourses d'étude au rang 3 : l'étude achevée rend 9 % de son coût, soit **46 080** ressources.

**Laboratoire jumeau** : une seconde étude de 10 h avance à 80 % de la vitesse normale et prend **12 h 30 min** (20 h avec le seul Second laboratoire de l'arbre commun). Sans Second laboratoire, elle avance à 40 % et prend **25 h**.

## Données détaillées

Types de rangée : *clé* (1 point), *3 rangs*, *choix* (un point, option A ou B), *ultime*.

### Méthode : « Une étude n'attend jamais. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Fil continu** | Une étude qui démarre d'elle-même, à la suite de la précédente dans la file, part avec une part de son temps déjà écoulé. | 10 % |
| 2 | 3 rangs | **Départ lancé** | Une étude lancée à la main sur une file de recherche vide part avec une part de son temps déjà écoulé, sans dépasser le plafond de 10 % des avances. | 3 % par rang (9 %) |
| 3 | choix | **A : Veille de nuit** | File de recherche vide, le Centre d'innovation met de côté 25 % du temps qui passe (1 min toutes les 4 min), jusqu'à 2 h d'avance versées à la prochaine étude. | 2 h |
| | | **B : Brouillon conservé** | Une étude annulée garde sa progression : relancée plus tard au même niveau, elle reprend où elle s'était arrêtée. | déblocage |
| 4 | 3 rangs | **Protocoles** | Vos recherches coûtent moins. | −2 % par rang (−6 %) |
| 5 | clé | **Éclair de génie** | Une fois toutes les 24 h, d'un bouton, l'étude en cours avance d'un coup d'une part de son temps total, sans jamais l'achever. | 10 % |
| 6 | choix | **A : Esprit vif** | L'Éclair de génie se recharge en 16 h au lieu de 24 h. | 16 h |
| | | **B : Réflexe** | L'Éclair de génie part tout seul dès qu'il est prêt et qu'une étude tourne, même sans vous connecter. | déblocage |
| 7 | 3 rangs | **Coup de génie** | L'Éclair de génie avance l'étude de plus. | +3 % par rang (19 %) |
| 8 | clé | **Inspiration** | Chaque étude achevée fait revenir l'Éclair de génie plus tôt, d'une part de la durée de l'étude. | 20 % |
| 9 | ultime | **Laboratoire jumeau** | Votre seconde recherche (Second laboratoire) avance à 80 % de la vitesse normale. Sans le Second laboratoire, vous en menez quand même une seconde, à 40 %. | 80 % / 40 % |

### Réseau : « Chaque colonie est un laboratoire. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Liaison montante** | Le réseau d'étude accepte les Centres d'innovation jusqu'à 2 niveaux sous celui qui étudie. | 2 niveaux |
| 2 | 3 rangs | **Labos de campagne** | Chaque Centre d'innovation mis en réseau compte des niveaux de plus. | +1 niveau par rang (+3) |
| 3 | choix | **A : Antenne lointaine** | Le réseau accepte les Centres jusqu'à 5 niveaux sous celui qui étudie : pour un empire de jeunes colonies. | 5 niveaux |
| | | **B : Labo-mère** | Le Centre qui étudie compte 3 niveaux de plus : pour un empire compact. | +3 niveaux |
| 4 | 3 rangs | **Paillasses en kit** | Vos Centres d'innovation se construisent plus vite (accent). | 3 % par rang (9 %) |
| 5 | clé | **Un labo de plus** | Le réseau met en commun 1 Centre de plus que Collaboration Stellaire ne l'autorise. | +1 Centre |
| 6 | choix | **A : Réseau vivant** | Quand un Centre du réseau monte de niveau pendant une étude, son temps restant est recalculé, jamais plus lent. | déblocage |
| | | **B : Partage des résultats** | Une étude achevée verse une part de son temps en avance à la prochaine étude de la même famille, même lancée à la main. | 10 % |
| 7 | 3 rangs | **Bourses d'étude** | Une étude achevée avec au moins 2 Centres en réseau rend une part de son coût à la planète qui étudie. | 3 % par rang (9 %) |
| 8 | clé | **Échange universitaire** | Le réseau accepte 1 Centre allié : le meilleur d'un membre de votre alliance, dans la tolérance du réseau. L'allié ne perd rien. | +1 Centre allié |
| 9 | ultime | **Symposium** | Une étude lancée avec au moins 4 Centres en réseau part avec une part de son temps déjà écoulé, au-delà du plafond des avances. | 20 % |

### Prototypes : « Un niveau d'avance sur tout le monde. »

| Rangée | Type | Talent | Effet | Valeur |
|---|---|---|---|---|
| 1 | clé | **Prototype** | Après la fin d'un niveau de recherche civile ou de propulsion, vous profitez déjà de l'effet du niveau suivant. | 12 h |
| 2 | 3 rangs | **Essais prolongés** | Vos prototypes durent plus longtemps. | +12 h par rang (48 h) |
| 3 | choix | **A : Prototype de combat** | Le prototype couvre aussi Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. | déblocage |
| | | **B : Feu vert** | Pendant un prototype, vous pouvez déjà lancer ce qui demande le niveau suivant de cette recherche. | déblocage |
| 4 | 3 rangs | **Ingénierie inverse** | Après une bataille contre un joueur plus avancé que vous dans une technologie de combat, votre prochain niveau de cette technologie coûte moins, une fois par niveau. | −5 % par rang (−15 %) |
| 5 | clé | **Double prototype** | Pendant les 6 h qui suivent la fin d'une étude, son prototype vaut 2 niveaux au lieu d'un. Pas sur les technologies de combat. | 2 niveaux, 6 h |
| 6 | choix | **A : Brevets** | Les niveaux de recherche au-delà du 10e coûtent moins (accent). | −3 % |
| | | **B : Banc d'essai** | Une fois toutes les 24 h, lancez à la main un prototype de 6 h sur une recherche déjà étudiée, par exemple juste avant une attaque. | 6 h |
| 7 | 3 rangs | **Retombées** | Quand un prototype expire, la planète qui a mené l'étude reçoit une part de son coût. | 2 % par rang (6 %) |
| 8 | clé | **Spécialité** | Choisissez une recherche : son prototype ne s'arrête jamais. Vous pouvez en changer une fois par semaine. Calcul Quantique et Cosmologie Appliquée sont exclues. | permanent |
| 9 | ultime | **Révolution** | Une fois par semaine, d'un bouton : pendant 12 h, toutes vos recherches valent 1 niveau de plus. | 12 h |

### Builds à 25 points

| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chercheur pur | Méthode 15 · Réseau 10 | File qui ne s'arrête jamais, Éclair de génie à 19 %, Laboratoire jumeau ; réseau ouvert par Liaison montante, Centres de colonie +3 niveaux, un Centre de plus. |
| Grand réseau | Réseau 15 · Méthode 10 | Symposium et Centre allié ; Fil continu, Éclair de génie, Esprit vif ou Réflexe. |
| Savant de guerre | Prototypes 15 · Méthode 10 | Révolution, prototypes de combat ou Feu vert, Spécialité ; Éclair de génie pour rattraper les niveaux. |

## Pièges fréquents

- **Les avances ne s'additionnent pas sans limite** : Fil continu et Départ lancé restent sous 10 % de l'étude, quel que soit le rang. Seuls l'Éclair de génie, le Brouillon conservé et le Symposium passent au-delà.
- **Liaison montante ne crée pas de Centre** : elle accepte des Centres plus bas dans le réseau, mais leur nombre reste fixé par Collaboration Stellaire (plus 1 avec Un labo de plus).
- **Double prototype ne touche pas le combat** : les technologies de combat ne gagnent jamais deux niveaux de prototype.
- **Laboratoire jumeau** se lit à 80 % seulement avec le Second laboratoire de l'arbre commun ; sans lui, la seconde étude avance à 40 %.
- **Brevets** ne s'applique qu'aux niveaux au-delà du 10e.

## Pages liées

- [Classes](/fr/dynasty/classes)
- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Collaboration Stellaire](/fr/research/stellar-collaboration)
- [Liste des technologies](/fr/research/technologies)
