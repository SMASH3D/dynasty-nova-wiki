---
wiki_id: 23
locale: "fr"
path: "economy/build-queue"
url: "https://wiki.dynastynova.com/fr/economy/build-queue"
title: "Files de construction"
description: "Ordres en file, paiement et annulation."
tags: ["economy"]
published: true
created: "2026-10-02T13:08:29.825Z"
updated: "2026-10-15T16:10:23.274Z"
---

# Files de construction

> **En bref** : chaque planète a quatre files : bâtiments, recherche, vaisseaux et défenses. Chaque file accepte 2 ordres (5 en Premium), celui en cours compris. La recherche avance une étude à la fois pour tout votre empire. Un bâtiment ou une recherche n'est payé qu'au moment où il démarre ; s'il ne peut pas être payé, il est abandonné sans frais.
{.is-info}

> **Paramètre d'univers** : la taille des files peut être différente selon l'univers.
> Par défaut et sur Redline : **2 ordres**, **5 en Premium**
{.is-info}

## Règles

1. Quatre files par planète : **bâtiments**, **recherche**, **vaisseaux**, **défenses**. Les études de recherche passent **une à la fois pour tout votre empire** : chaque planète garde sa propre file, mais une étude placée sur une colonie attend que celle en cours sur une autre planète soit terminée (le talent [Second laboratoire](/fr/dynasty/common-tree) permet d'en mener deux).
2. Chaque file accepte **2 ordres**, celui en cours compris, ou **5 en Premium**.
3. Un **bâtiment** ou une **recherche** est **payé au lancement**, pas à la mise en file. Si, au moment de démarrer, la planète n'a pas les ressources, l'ordre est **abandonné sans frais**.
4. Les ordres en attente affichent une **durée estimée**, recalculée au lancement.
5. On ne peut pas mettre en file une amélioration et une démolition du même bâtiment en même temps.
6. Pendant que le **Dock orbital** produit des unités, il ne peut être ni amélioré ni démoli ; pendant qu'il est en travaux, aucun vaisseau ni aucune défense ne peut y être commandé. Pendant que le **Centre d'innovation** d'une planète est en travaux, aucune recherche ne peut être lancée ni ajoutée depuis cette planète ; et tant qu'une recherche lancée depuis une planète est en cours, son Centre d'innovation ne peut pas être amélioré.

### Annulation
7. Annuler un ordre **encore en attente** ne coûte rien et ne rend rien : il n'a pas été payé.
8. Annuler un **bâtiment ou une recherche en cours** rend **80 % du coût × (temps restant / durée totale)**, arrondi à l'inférieur pour chaque ressource. Le trait de dynastie [Rien ne se perd](/fr/dynasty/dynasties) porte ce taux à 85 %.
9. Annuler une commande de **vaisseaux ou de défenses** rend 80 % des unités payées mais pas encore livrées, sans prorata de temps. Les unités déjà livrées sont conservées.
10. L'**énergie requise** n'est jamais remboursée : elle n'est pas dépensée.

## Exemple chiffré

Vous annulez un bâtiment qui coûtait 20 000 métal et 10 000 cristal, alors que 25 % de son temps est écoulé.
- Temps restant : 75 %.
- Remboursement : 80 % × 75 % = **60 %**, soit **12 000 métal et 6 000 cristal**.
- Vous perdez 8 000 métal et 4 000 cristal : annuler tôt coûte déjà 20 %.

## Pièges fréquents

- **Une annulation n'est jamais gratuite** : même juste après le lancement, vous perdez au moins 20 %.
- **Gardez les ressources pour l'ordre suivant** : un ordre qui ne peut pas être payé à son tour est abandonné.
- **Le Premium allonge les quatre files** : bâtiments, recherche, vaisseaux et défenses passent tous à 5 ordres.

## Pages liées

- [Liste des bâtiments](/fr/economy/buildings)
- [Démolir un bâtiment](/fr/economy/demolition)
- [Premium, boutique et Points stellaires](/fr/misc/premium)
