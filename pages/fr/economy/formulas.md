---
wiki_id: 22
locale: "fr"
path: "economy/formulas"
url: "https://wiki.dynastynova.com/fr/economy/formulas"
title: "Formules de l'économie"
description: "Coûts, durées, production et points."
tags: ["economy"]
published: false
created: "2026-10-02T13:08:27.831Z"
updated: "2026-10-02T14:14:51.908Z"
---

# Formules de l'économie

> **En bref** : toutes les formules de l'économie, telles que le jeu les calcule : coût et points d'un niveau, durée des bâtiments, des vaisseaux, des défenses et des recherches, production, énergie et stockage. Chaque bonus de vitesse divise une durée, chaque bonus de production s'ajoute à la production brute des mines.
{.is-info}

> **Paramètre d'univers** : les vitesses d'économie, de construction, de recherche et de chantier peuvent être différentes selon l'univers.
> Par défaut : **×1** · Redline : **×1**
{.is-info}

## Règles

### Coût et points
1. Coût du niveau $N$ d'un bâtiment ou d'une recherche, pour chaque ressource :
$$C_N = \left\lfloor C_1 \times f^{N-1} \right\rfloor$$
   - $C_1$ : coût du niveau 1 ; $f$ : facteur du bâtiment ou de la recherche (voir [Liste des bâtiments](/fr/economy/buildings)).
   - L'énergie requise suit la même formule ; seule la Station de réparation a un facteur d'énergie différent (2,5 au lieu de 5).
2. Un vaisseau ou une défense coûte toujours le même prix à l'unité.
3. **Points** : $P = (M + C + H) / 1\,000$, où $M$, $C$ et $H$ sont le métal, le cristal et l'hydrogène dépensés. L'énergie requise ne compte pas.

### Durées
4. **Bâtiment**, en heures :
$$t = \frac{M + C + H}{2\,500 \times (1 + F) \times 2^{A}} \div v_c \div \left(1 + \frac{b}{100}\right)$$
   - $M + C + H$ : coût du niveau ; $F$ : niveau de la Fabrique d'automates ; $A$ : niveau de l'Assembleur moléculaire ; $v_c$ : vitesse de construction de l'univers ; $b$ : bonus de vitesse en %, additionnés (talent d'alliance Bâtisseurs associés, talents de dynastie).
   - Le résultat est arrondi à la seconde. Une démolition dure la moitié de la construction du niveau retiré, sans les bonus de vitesse.
5. **Vaisseau ou défense**, en secondes par unité, jamais moins d'une seconde :
$$t = \frac{T}{(1 + D) \times 2^{A}} \div v_{ch}$$
   - $T$ : durée de base de l'unité (par exemple 5 400 s pour une Navette de fret, 2 880 s pour un Collecteur solaire) ; $D$ : niveau du Dock orbital ; $A$ : niveau de l'Assembleur moléculaire ; $v_{ch}$ : vitesse de chantier de l'univers. Les bonus de vitesse du chantier (talents) divisent ensuite la durée comme pour les bâtiments.
6. **Recherche**, en heures :
$$t = \frac{M + C}{1\,000 \times (1 + L)} \div v_r$$
   - $M + C$ : métal et cristal du niveau, sans l'hydrogène ; $L$ : niveau effectif du Centre d'innovation, réseau de laboratoires compris (voir [Recherche](/fr/research)) ; $v_r$ : vitesse de recherche de l'univers. Les bonus de vitesse (Centres d'innovation en réseau, talents) divisent la durée comme pour les bâtiments.

### Production et énergie (par heure, au niveau $N$)
7. Excavateur minéral : $30 \times N \times 1{,}1^N$ métal ; Extracteur cristallin : $20 \times N \times 1{,}1^N$ cristal ; Condensateur d'hydrogène : $10 \times N \times 1{,}1^N \times k_H$ hydrogène, avec $k_H = 1{,}44 - 0{,}004 \times T_{max}$ (jamais négatif). Le tout multiplié par la vitesse d'économie.
8. Consommation d'énergie de chaque mine : $10 \times N \times 1{,}1^N$, sans la vitesse d'économie.
9. Capteurs photovoltaïques : $20 \times N \times 1{,}1^N \times (1 + T / 100)$, avec $T$ la température actuelle, comptée 0 si elle est négative.
10. Réacteur thermonucléaire : $30 \times N \times (1{,}05 + 0{,}01 \times S)^N$ énergie, $S$ étant le niveau de Science Énergétique ; il consomme $10 \times N \times 1{,}1^N$ hydrogène, multiplié par la vitesse d'économie.
11. Collecteur solaire : $\lfloor T_{max} / 4 + 20 \rfloor$ énergie par unité, jamais négatif.
12. Bonus de production : Maîtrise du Plasma (+1 % de métal, +0,66 % de cristal, +0,33 % d'hydrogène par niveau), Extraction coordonnée (+5 % par niveau), bonus de position des colonies, dynastie et talents. Chacun se calcule sur la production brute des mines, s'arrondit à l'inférieur, et ils s'additionnent.
13. Déficit d'énergie : la production des mines, bonus compris, est multipliée par $\min(1, \text{production} / \text{consommation})$. Puis s'ajoutent 20 métal et 10 cristal de la Base planetaire, multipliés par la vitesse d'économie.

### Stockage
14. Capacité d'un entrepôt au niveau $N$ : $5\,000 \times \lfloor 2{,}5 \times e^{20N/33} \rfloor$. Base planetaire : 10 000 par ressource. Bonus (Centre logistique +10 % par niveau, Entrepôts fédérés +10 % par niveau, talents) additionnés et appliqués à toute la capacité.

$T_{max}$ : température maximale de la planète, en °C.

## Exemple chiffré

Monter le Dock orbital du niveau 6 au niveau 7 avec une Fabrique d'automates niveau 6, un Assembleur moléculaire niveau 1, le talent Bâtisseurs associés niveau 2 (+20 %), vitesse ×1 :
- Coût du niveau 7 : 400 × 2^6 = 25 600 métal, 12 800 cristal, 6 400 hydrogène, soit 44 800 ressources et 44,8 points.
- Durée de base : 44 800 / (2 500 × 7 × 2) heures = **4 608 secondes**.
- Avec +20 % de vitesse : 4 608 / 1,2 = **3 840 secondes** (1 h 04 min).

Une Navette de fret construite ensuite au Dock orbital 7 avec l'Assembleur 1 : 5 400 / (8 × 2) = **338 secondes** par unité.

## Données détaillées

### Ce que change chaque vitesse d'univers

| Vitesse | Effet |
|---|---|
| Économie | Multiplie la production des mines, de la Base planetaire et la consommation d'hydrogène du Réacteur ; ne change ni l'énergie ni la consommation d'énergie |
| Construction | Divise la durée des bâtiments et des démolitions |
| Recherche | Divise la durée des recherches |
| Chantier | Divise la durée des vaisseaux et des défenses, accélère la Station de réparation |
| Flotte | Voir [Déplacements](/fr/fleet/movement) |

## Pièges fréquents

- **L'hydrogène compte dans la durée d'un bâtiment** : un bâtiment qui coûte de l'hydrogène dure plus longtemps qu'une mine au même total de métal et de cristal. En recherche, il ne compte pas.
- **Les bonus de vitesse ne réduisent pas de leur pourcentage** : +20 % de vitesse divise la durée par 1,2, soit environ 17 % de moins.
- **L'Assembleur moléculaire divise par deux à chaque niveau** : bâtiments, vaisseaux et défenses.

## Pages liées

- [Les ressources](/fr/economy/resources)
- [L'énergie](/fr/economy/energy)
- [Le stockage](/fr/economy/storage)
- [Liste des bâtiments](/fr/economy/buildings)
- [Files de construction](/fr/economy/build-queue)
