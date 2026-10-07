---
wiki_id: 157
locale: "fr"
path: "dynasty/classes/shadow"
url: "https://wiki.dynastynova.com/fr/dynasty/classes/shadow"
title: "L'Ombre"
description: "Arbre de classe de l'Ombre : Pénétration, Discrétion et Contre-jour."
tags: ["dynasty"]
published: true
created: "2026-10-06T10:29:49.095Z"
updated: "2026-10-06T10:29:50.376Z"
---

# L'Ombre

> **En bref** : l'Ombre joue les deux sens du renseignement : lire chez les autres sans se faire prendre, et rendre son propre territoire illisible. Ses talents sont des règles, pas des pourcentages génériques, et elle n'a aucun accent. Classe commune à toutes les dynasties.
{.is-info}

*Devise : « Savoir sans être vu ».*

## Règles

1. L'arbre de classe suit les règles communes à toutes les classes : 3 branches de 9 rangées, 15 points par branche, 25 points au maximum. Voir [Système de talents](/fr/dynasty/talents).
2. Les talents de l'Ombre s'appuient sur les règles de l'[espionnage](/fr/espionage/spying) : niveau effectif, paliers du rapport (ressources dès 1, flotte dès 3, défenses dès 5, bâtiments dès 7, recherches dès 9), chance de destruction bornée entre 5 % et 25 %.
3. **Plafonds** de l'Ombre :
   - profondeur : **+1 niveau effectif** au plus (Le seuil), jamais compté par le jet de détection ; le bonus tiré des Éclaireurs reste plafonné à +5 ;
   - paliers : **1 palier plus tôt** au plus par catégorie pour les talents, seulement pour les ressources et la flotte ; le trait de dynastie Écouter loin s'y ajoute ;
   - détection : **8 points** au plus de chance de destruction en moins (en attaque) ou en plus (en défense), la borne de 5 % à 25 % restant appliquée ensuite ;
   - survie des sondes d'une vague prise : **50 %** au plus ;
   - pistage : **+15 points** au plus de chance d'être tracé.

## Exemple chiffré

**Sondes économes : lire les bâtiments avec 4 Éclaireurs**
- Votre Renseignement Tactique dépasse celui de la cible de 2. Les bâtiments demandent un niveau effectif de 7 : il faut +5 tiré des Éclaireurs, donc **10 Éclaireurs**.
- Au rang 3 de Sondes économes, votre vague compte pour 6 sondes de plus : **4 Éclaireurs** comptent pour 10, soit +5. Niveau effectif : 2 + 5 = **7**.

**Le seuil**
- Même écart de 2, avec 8 Éclaireurs : 2 + 4 + 1 = **7** : les bâtiments apparaissent.
- Écart de 3, avec 10 Éclaireurs : 3 + 5 + 1 = **9** : les recherches apparaissent.

## Données détaillées

### Pénétration : « Ce que le rapport dit »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Stock à l'arrivée** | chaque rapport calcule ce que la planète aura en stock quand votre raid y arrivera, production comprise et dans la limite de ses entrepôts (180 000 métal à 12 000/h, raid de 1 h : 192 000 à l'arrivée, 96 000 pillables) | déblocage |
| 2 | 3 rangs | **Sondes économes** | votre vague compte pour 2 Éclaireurs de plus par rang dans le niveau effectif, sans dépasser le +5 tiré des sondes (bâtiments à +2 d'écart avec 4 Éclaireurs au lieu de 10) | 3 × 2 sondes |
| 3 | choix | **A · Lecture des cales** / **B · Lecture des hangars** | A : les ressources se lisent 1 palier plus tôt, donc toujours, même avec un écart négatif et un seul Éclaireur <br> B : la flotte se lit 1 palier plus tôt (dès le niveau effectif 2 : à écart égal, 4 Éclaireurs au lieu de 6) | 1 palier |
| 4 | 3 rangs | **Dossier vivant** | chaque nouveau rapport reprend, datées, les sections que vos rapports des 8 dernières heures par rang avaient lues : 24 h au rang 3. Une vague complète le matin, des passages légers ensuite gardent bâtiments et défenses | 3 × 8 h |
| 5 | clé | **Regard en orbite** | une vague lit aussi l'autre corps de la case (la lune d'une planète, la planète d'une lune), 2 niveaux plus bas, dans un second rapport : c'est là que se cachent les flottes à l'abri | −2 niveaux |
| 6 | choix | **A · Repérage de système** / **B · Lecture de combat** | A : la vague liste aussi les autres planètes du système, « actif » ou « inactif », avec une fourchette de stock <br> B : armes, bouclier et coque de la cible se lisent dès le palier de la flotte (3) au lieu de celui des recherches (9) : on simule sans vague complète | déblocage |
| 7 | 3 rangs | **Rapport d'activité** | le rapport dit quand la cible a joué pour la dernière fois. Rang 1 : dans l'heure, dans la journée ou plus tôt. Rang 2 : à 15 min près. Rang 3 : et sur quelle planète | 3 degrés |
| 8 | clé | **Le seuil** | +1 niveau effectif, pour la profondeur du rapport seulement, jamais compté par le jet de détection | +1 niveau |
| 9 | ultime | **Mouchard** | une vague non détectée peut laisser un Éclaireur en orbite 6 h. Il envoie un rapport ressources et flotte chaque fois que la flotte au sol change (départ, retour, mise à l'abri). Chaque envoi rejoue la détection à la moitié de la chance ; pris, il est détruit | 6 h |

### Discrétion : « Entrer, lire, repartir »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Le risque mesuré** | l'écran d'envoi et chaque rapport affichent la chance de destruction que la vague affronte : vous voyez le risque avant de partir | déblocage |
| 2 | 3 rangs | **Basse signature** | −2 points de chance d'être détecté par rang : −6 au rang 3 (16 % → 10 %). La borne de 25 % d'une cible bien gardée s'applique après | 3 × 2 pts |
| 3 | choix | **A · Sondes larguées** / **B · Sans adresse** | A : 20 % des Éclaireurs d'une vague prise survivent et rentrent (10 pris → 2 rentrent) <br> B : une vague prise est identifiée mais jamais tracée : le défenseur apprend qui, jamais d'où | 20 % / déblocage |
| 4 | 3 rangs | **Coques muettes** | +7 % de survie par rang des Éclaireurs d'une vague prise : +21 % au rang 3 (41 % avec Sondes larguées : 10 pris → 4 rentrent) | 3 × 7 % |
| 5 | clé | **Prudence** | une vague qui affronte 15 % de risque ou plus fait demi-tour avant l'orbite : ni rapport, ni perte, ni alerte. Elle vous a appris que la cible est gardée. Le risque comparé est celui affiché, bornes de 5 et 25 % comprises. Désactivable à l'envoi | 15 % |
| 6 | choix | **A · Silhouette** / **B · Écran de fumée** | A : les [Phalanges de capteur](/fr/espionage/sensor-phalanx) adverses voient vos flottes, mais pas leur composition ni leur cargaison <br> B : vos attaques apparaissent chez la cible comme « flotte inconnue », sans nombre de vaisseaux, jusqu'à 15 min de l'impact | déblocage |
| 7 | 3 rangs | **Fausse piste** | une vague tracée a 30 % de chances par rang de donner au défenseur une fausse origine (une planète inactive de votre galaxie) : 90 % au rang 3 | 3 × 30 % |
| 8 | clé | **Le vide parfait** | une vague qui ne courait aucun risque (cible deux fois moins avancée, ou orbite vide) ne laisse qu'une trace vague : « activité repérée dans votre système », sans planète, sans nom, à l'heure près | déblocage |
| 9 | ultime | **Ni vu ni connu** | une fois par 24 h, une vague prise n'est pas abattue : elle échappe à la défense et tous ses Éclaireurs rentrent | 1 par 24 h |

Budget de détection : −6 points ici, sous le plafond de 8. Survie : 20 + 21 = 41 %, sous le plafond de 50 %.

### Contre-jour : « Votre territoire ne se lit pas »

| Rangée | Type | Nœud | Effet (exemple) | Valeur |
|---|---|---|---|---|
| 1 | clé | **Orbite gardée** | le contre-espionnage joue même sur une orbite vide, au plancher de 5 % : vos colonies sans flotte ne sont plus un livre ouvert | 5 % |
| 2 | 3 rangs | **Sentinelles** | +2 points de chance de détecter les vagues sur vos planètes par rang : +6 au rang 3 (un espion à 10 % passe à 16 %) | 3 × 2 pts |
| 3 | choix | **A · Alerte partagée** / **B · Rapport d'incident** | A : vos alertes d'intrusion sont copiées à toute votre alliance <br> B : une intrusion non détectée vous dit quand même combien d'Éclaireurs, et de quelle galaxie | déblocage |
| 4 | 3 rangs | **Coffre caché** | les rapports ennemis sur vos planètes et lunes affichent 10 % de stock en moins par rang : 30 % au rang 3 (300 000 cristal lus 210 000). Le stock reste pillable : l'attaquant vient avec trop peu de soute | 3 × 10 % |
| 5 | clé | **Lumière dans le dos** | vous êtes prévenu quand une Phalange de capteur balaie l'une de vos planètes, et par qui | déblocage |
| 6 | choix | **A · Sentinelles de lune** / **B · Flotte voilée** | A : le contre-espionnage d'une planète compte aussi les vaisseaux de sa lune, et l'inverse <br> B : les rapports ennemis donnent votre flotte arrondie à 10 % près (« ≈ 120 Corvettes ») | déblocage |
| 7 | 3 rangs | **Filature** | +5 points de chance par rang de tracer une vague détectée : +15 au rang 3 | 3 × 5 pts |
| 8 | clé | **Brouillage** | les rapports adverses sur vos planètes lisent 1 niveau effectif plus bas, profondeur seule : de quoi annuler Le seuil d'une Ombre d'en face | −1 niveau |
| 9 | ultime | **Retour de sonde** | une vague tracée vous rapporte, sans sonde et sans que l'espion le sache, un rapport sur sa planète d'origine, lu au palier 3 : ressources et flotte | palier 3 |

Coffre caché et Flotte voilée trompent sur la quantité, jamais sur ce qui existe, et laissent le pillage intact.

### Ce que 25 points donnent

| Build | Répartition | Ressenti |
|---|---|---|
| **Chasseur** | Pénétration 15 · Discrétion 10 | Mouchard sur la cible, Lecture de combat, Le seuil, activité à la planète près ; 10 % de risque au lieu de 16, Prudence, phalanges aveugles |
| **Fantôme** | Discrétion 15 · Pénétration 10 | Ni vu ni connu, Le vide parfait, fausses pistes ; stock à l'arrivée, bâtiments lus avec 4 Éclaireurs, dossier vivant de 24 h, lunes lues au passage |
| **Gardien** | Contre-jour 15 · Discrétion 10 | Retour de sonde, Brouillage, stock affiché à 70 %, filature +15 ; ses propres vagues à 10 % de risque avec Prudence |

## Pièges fréquents

- **Écouter loin et Lecture des hangars se cumulent** : une Ombre de L'Accord qui prend Lecture des hangars lit la flotte **deux paliers** plus tôt.
- **Le seuil ne réduit pas le risque** : il ajoute de la profondeur, jamais de discrétion.
- **Plus de « toutes ou aucune »** : avec Sondes larguées et Coques muettes, une partie des Éclaireurs d'une vague prise rentre ; sans ces talents, la règle reste que toute la vague tombe.
- **Coffre caché ne protège rien** : il fausse le rapport ennemi, le stock reste entièrement pillable.
- **Brouillage annule Le seuil** : contre une Ombre qui a pris Contre-jour jusqu'à la rangée 8, votre niveau effectif en plus disparaît.

## Pages liées

- [Système de talents](/fr/dynasty/talents)
- [Arbre commun](/fr/dynasty/common-tree)
- [Classes](/fr/dynasty/classes)
- [Dynasties](/fr/dynasty/dynasties)
- [Espionner](/fr/espionage/spying)
- [Lire un rapport d'espionnage](/fr/espionage/spy-report)
- [Phalange de capteur](/fr/espionage/sensor-phalanx)
