"""L'Amiral : textes vérifiés sur le code (notes du 15 octobre 2026, DONNEES §18)."""

FR = {
    'brief': "l'Amiral est la classe du combat frontal. Elle ne change pas les vaisseaux que vous construisez, mais ce qu'ils valent une fois face à l'ennemi. Tout le combat tient dans la branche Ligne de feu ; Campagne fait partir vite, enchaîner et rentrer plus tôt ; Butin de guerre ramène davantage de chaque bataille.",
    'rules': [
        "La vitesse de flotte, l'hydrogène et les soutes génériques viennent de l'[arbre commun](/fr/dynasty/common-tree). L'Amiral n'y ajoute que des **accents** étroits : la vitesse des attaques, espionnages et destructions de lune ([[admiral_campaign_1]]) et des recyclages ([[admiral_spoils_6:2]]), l'hydrogène et la construction des vaisseaux de combat, et une flotte réservée aux attaques.",
        "Les **vaisseaux de combat** sont l'Intercepteur, l'Assaillant, la Corvette, le Cuirassé, le Frappe-orbital, le Prédateur, l'Annihilateur et le Colossus stellaire. Les vaisseaux civils (Navette de fret, Cargo stellaire, Récupérateur, Éclaireur, Pionnier spatial) et le Collecteur solaire n'en sont pas.",
        "Les bonus de statistiques s'appliquent **après** la recherche et se multiplient avec elle. Ils jouent en attaque comme en défense. Les bonus de dégâts d'une paire ([[admiral_firing_line_7]], [[admiral_firing_line_9]]) se multiplient entre eux.",
    ],
    'example': """**[[admiral_firing_line_2]] et [[admiral_firing_line_3:2]], sur une Corvette**
- Armement de base 400, Systèmes Offensifs niveau 10 : 400 × 2 = 800. Avec [[admiral_firing_line_2]] au rang 3 : 800 × 1,09 = **872**.
- Avec [[admiral_firing_line_3:2]], les 9 % passent à la coque et s'ajoutent aux 4 % du nœud : coque +13 %, armement 800 sans bonus.

**[[admiral_spoils_1]] et [[admiral_spoils_2]] (50 %), Station de réparation niveau 10, 30 % de débris**
- Part de la Station : 54 % × (1 − 30 %) = 37,8 %. [[admiral_spoils_1]] : 37,8 % × 50 % = **18,9 %**.
- 30 Corvettes perdues en attaque : 30 × 18,9 % = 5,67, soit **5 Corvettes**, et 67 % de chances d'en avoir une sixième.
- Les mêmes 30 Corvettes perdues en défense, avec [[admiral_spoils_8]] : 54 % × 1,2 × 70 % = 45,36 %, soit **13** Corvettes (11 sans le nœud).

**[[admiral_spoils_3:2]]**
- Un match nul pille à 30 % du taux d'une victoire : 50 % × 30 % = **15 %** du stock. Sur 2 000 000 de métal, vous emportez **300 000**, dans la limite de vos soutes.

**[[admiral_firing_line_8]]**
- Contre une lune de 8 944 km, le risque de perdre votre flotte est √8 944 / 2 = 47,29 % ; avec le nœud : 47,29 % × 0,75 = **35,47 %**. La chance de détruire la lune ne change pas.""",
    'branch_notes': {
        'firing_line': """- **[[admiral_firing_line_3:1]]** : vos défenses reçoivent la moitié du bonus d'armement de vos vaisseaux, soit +4,5 % avec [[admiral_firing_line_2]] au rang 3. Elle ne sert que lorsqu'on vous attaque.
- **[[admiral_firing_line_3:2]]** : [[admiral_firing_line_2]] ne donne plus d'armement, ses points vont à la coque.
- **[[admiral_firing_line_4]]** et **[[admiral_firing_line_6:1]]** allongent les chaînes de tirs rapides de vos vaisseaux (contre les vaisseaux, contre les défenses).
- **[[admiral_firing_line_5]]** : vous désignez, dans l'onglet Compétences, un type parmi la Corvette, le Frappe-orbital, l'Annihilateur et le Colossus stellaire. Il **ne s'ajoute pas** à [[admiral_firing_line_4]] ou [[admiral_firing_line_6:1]] : chaque tir rapide prend le meilleur des deux.
- **[[admiral_firing_line_6:2]]** protège vos vaisseaux et vos défenses, en attaque comme en défense. Toutes sources confondues, cette réduction ne dépasse jamais 15 %.
- **[[admiral_firing_line_7]]** joue sur toute paire où le tireur a un tir rapide contre sa cible. Le diapason de L'Accord ajoute 5 % au-delà du plafond.
- **[[admiral_firing_line_9]]** se règle à l'envoi d'une mission Attaque (pas d'une destruction de lune). Il ne joue pas quand on vous attaque.""",
        'campaign': """- **[[admiral_campaign_2]]** rend une part de l'hydrogène de l'aller sur une attaque gagnée dont la flotte survit. Il est chargé hors capacité et livré au retour.
- **[[admiral_campaign_3:1]]** accélère les Navettes de fret et Cargos stellaires d'une mission Attaque, sans dépasser le vaisseau le plus rapide. **[[admiral_campaign_3:2]]** réduit la part d'hydrogène brûlée par vos vaisseaux de combat : une flotte où ils brûlent la moitié du carburant économise 5 %.
- **[[admiral_campaign_5]]** ne sert qu'à la mission Attaque (ni espionnage ni destruction de lune).
- **[[admiral_campaign_6:2]]** : une défaite détruit toute la flotte, il n'y a donc rien à rendre ; en pratique, elle ne joue que sur un match nul.
- **[[admiral_campaign_8]]** vaut pour vos attaques et vos destructions de lune.
- **[[admiral_campaign_9]]** : à l'envoi, vous nommez une seconde cible, une planète d'un autre joueur ou abandonnée, dans la même galaxie, à 1 système au plus de la première. Si l'attaque est gagnée et la flotte survit, elle y repart aussitôt, une fois par vol, en prenant l'hydrogène du saut dans ses soutes. Trêve, alliance, mode vacances, protections et limite d'attaques sont vérifiés au moment du saut : en cas de refus, la flotte rentre.""",
        'spoils': """- **[[admiral_spoils_1]]** : c'est la Station de réparation de la planète de départ qui remorque. Une lune n'a pas de Station : une flotte partie d'une lune ne remorque rien. Le remorquage utilise un **arrondi probabiliste** : la partie décimale devient une chance d'avoir un vaisseau de plus.
- **[[admiral_spoils_3:2]]** : 30 % du taux de pillage d'une victoire, abris du défenseur déduits.
- **[[admiral_spoils_4]]** accélère toutes les réparations de la Station ; une réparation reste comprise entre 30 min (15 min avec [[admiral_spoils_6:1]]) et 12 h.
- **[[admiral_spoils_5]]** : les Récupérateurs de la flotte d'attaque ramassent les débris de ce combat, après le pillage.
- **[[admiral_spoils_7]]** ajoute l'hydrogène seulement dans la place qui reste en soute.
- **[[admiral_spoils_8]]** ne joue qu'en défense, pas sur le remorquage.
- **[[admiral_spoils_9]]** : après une attaque gagnée, vos vaisseaux de combat chargent 30 % des débris du combat dans leurs soutes libres, après le pillage et les Récupérateurs.""",
    },
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Chasseur de flottes | Ligne de feu 15 · Campagne 10 | [[admiral_firing_line_9]], armement +9 % (ou coque +13 %), bouclier +3 %, [[admiral_firing_line_4]], [[admiral_firing_line_7]] ; [[admiral_campaign_1]], hydrogène rendu sur les victoires, retour victorieux, une flotte d'attaque en plus |
| Raideur | Campagne 15 · Butin de guerre 10 | [[admiral_campaign_9]], [[admiral_campaign_7]], [[admiral_campaign_8]] ; remorquage jusqu'à 50 %, [[admiral_spoils_3:1]] ou [[admiral_spoils_3:2]], réparations plus rapides, recyclage de combat |
| Pilleur de batailles | Butin de guerre 15 · Ligne de feu 10 | [[admiral_spoils_9]], remorquage, [[admiral_spoils_7]], [[admiral_spoils_8]] ; armement +9 %, bouclier +3 %, [[admiral_firing_line_4]], [[admiral_firing_line_5]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**[[admiral_firing_line_9]] se règle avant le départ** : le type d'unité visé se désigne dans le formulaire d'envoi. Espionnez d'abord.",
        "**[[admiral_firing_line_3:2]] retire l'armement** : avec elle, [[admiral_firing_line_2]] ne donne plus aucun dégât.",
        "**[[admiral_firing_line_5]] peut ne rien ajouter** : avec [[admiral_firing_line_4]] au rang 3 et [[admiral_firing_line_6:1]], chaque tir rapide est déjà mieux servi.",
        "**[[admiral_campaign_9]] ne va pas loin** : la seconde cible doit être à 1 système au plus de la première, et la flotte paie le saut avec l'hydrogène de ses soutes.",
        "**Pas de Station de réparation, pas de remorquage** : une flotte partie d'une lune ne remorque rien. Sans [[admiral_spoils_3:1]], une flotte entièrement détruite ne rend rien.",
        "**[[admiral_campaign_4]] ne compte pas dans le plafond de vitesse**, mais [[admiral_campaign_1]], si : elle occupe l'accent de vitesse de 10 % de la classe.",
        "**[[admiral_campaign_8]] frappe aussi un Vétéran** : sa réparation des défenses perd 15 points contre vous.",
    ],
    'related': [
        "[Talents](/fr/dynasty/talents)", "[Classes](/fr/dynasty/classes)", "[Arbre commun](/fr/dynasty/common-tree)",
        "[Dynasties](/fr/dynasty/dynasties)", "[Tirs rapides](/fr/fleet/rapid-fire)", "[Pillage](/fr/combat/plunder)",
        "[Champs de débris](/fr/combat/debris)", "[Station de réparation](/fr/economy/repair-station)",
        "[Reconstruction des défenses](/fr/combat/defense-rebuild)", "[Destruction de lune](/fr/combat/moon-destruction)",
    ],
}

EN = {
    'brief': "the Admiral is the head-on combat class. It does not change the ships you build, but what they are worth once facing the enemy. All the combat lies in the Firing Line branch; Campaign leaves fast, chains raids and comes home sooner; Spoils of War brings more back from every battle.",
    'rules': [
        "Generic fleet speed, hydrogen and holds come from the [common tree](/en/dynasty/common-tree). The Admiral only adds narrow **accents**: the speed of attacks, espionage and moon destruction ([[admiral_campaign_1]]) and of recycling ([[admiral_spoils_6:2]]), combat ships' hydrogen and build speed, and a fleet reserved for attacks.",
        "**Combat ships** are the Interceptor, Assailant, Corvette, Battleship, Orbital Striker, Predator, Annihilator and Stellar Colossus. Civil ships (Cargo Shuttle, Stellar Freighter, Salvager, Scout, Space Pioneer) and the Solar Collector are not.",
        "Stat bonuses apply **after** research and multiply with it. They work in attack as in defence. Damage bonuses on a pair ([[admiral_firing_line_7]], [[admiral_firing_line_9]]) multiply with each other.",
    ],
    'example': """**[[admiral_firing_line_2]] and [[admiral_firing_line_3:2]], on a Corvette**
- Base weapons 400, Offensive Systems level 10: 400 × 2 = 800. With [[admiral_firing_line_2]] at rank 3: 800 × 1.09 = **872**.
- With [[admiral_firing_line_3:2]], the 9% moves to the hull and adds to the node's 4%: hull +13%, weapons 800 with no bonus.

**[[admiral_spoils_1]] and [[admiral_spoils_2]] (50%), Repair Station level 10, 30% debris**
- Station share: 54% × (1 − 30%) = 37.8%. [[admiral_spoils_1]]: 37.8% × 50% = **18.9%**.
- 30 Corvettes lost in attack: 30 × 18.9% = 5.67, that is **5 Corvettes**, and a 67% chance of a sixth.
- The same 30 Corvettes lost in defence, with [[admiral_spoils_8]]: 54% × 1.2 × 70% = 45.36%, that is **13** Corvettes (11 without the node).

**[[admiral_spoils_3:2]]**
- A draw plunders at 30% of a victory's rate: 50% × 30% = **15%** of the stock. On 2,000,000 metal, you take **300,000**, within your holds' limit.

**[[admiral_firing_line_8]]**
- Against an 8,944 km moon, the risk of losing your fleet is √8,944 / 2 = 47.29%; with the node: 47.29% × 0.75 = **35.47%**. The chance of destroying the moon does not change.""",
    'branch_notes': {
        'firing_line': """- **[[admiral_firing_line_3:1]]**: your defences get half of your ships' weapons bonus, that is +4.5% with [[admiral_firing_line_2]] at rank 3. It only helps when you are attacked.
- **[[admiral_firing_line_3:2]]**: [[admiral_firing_line_2]] no longer gives weapons, its points go to the hull.
- **[[admiral_firing_line_4]]** and **[[admiral_firing_line_6:1]]** lengthen your ships' rapid fire chains (against ships, against defences).
- **[[admiral_firing_line_5]]**: in the Abilities tab, you designate one type among the Corvette, Orbital Striker, Annihilator and Stellar Colossus. It **does not add** to [[admiral_firing_line_4]] or [[admiral_firing_line_6:1]]: each rapid fire takes the better of the two.
- **[[admiral_firing_line_6:2]]** protects your ships and defences, in attack as in defence. All sources together, this reduction never exceeds 15%.
- **[[admiral_firing_line_7]]** works on every pair where the shooter has rapid fire against its target. The Accord's Tuning Fork adds 5% past the cap.
- **[[admiral_firing_line_9]]** is set when sending an Attack mission (not a moon destruction). It does not work when you are attacked.""",
        'campaign': """- **[[admiral_campaign_2]]** gives back part of the outbound hydrogen on a won attack whose fleet survives. It is loaded outside capacity and delivered on return.
- **[[admiral_campaign_3:1]]** speeds up the Cargo Shuttles and Stellar Freighters of an Attack mission, never past the fastest ship. **[[admiral_campaign_3:2]]** cuts the share of hydrogen burned by your combat ships: a fleet where they burn half the fuel saves 5%.
- **[[admiral_campaign_5]]** only serves the Attack mission (neither espionage nor moon destruction).
- **[[admiral_campaign_6:2]]**: a defeat destroys the whole fleet, so there is nothing to give back; in practice, it only works on a draw.
- **[[admiral_campaign_8]]** applies to your attacks and your moon destructions.
- **[[admiral_campaign_9]]**: when sending, you name a second target, a planet of another player or an abandoned one, in the same galaxy, at most 1 system from the first. If the attack is won and the fleet survives, it leaves for it at once, once per flight, taking the jump's hydrogen from its holds. Truce, alliance, vacation mode, protections and the attack limit are checked at the time of the jump: if refused, the fleet goes home.""",
        'spoils': """- **[[admiral_spoils_1]]**: the Repair Station of the departure planet does the towing. A moon has no Station: a fleet leaving from a moon tows nothing. [[admiral_spoils_1]] uses **probabilistic rounding**: the decimal part becomes a chance of one more ship.
- **[[admiral_spoils_3:2]]**: 30% of a victory's plunder rate, the defender's shelters deducted.
- **[[admiral_spoils_4]]** speeds up every Station repair; a repair stays between 30 min (15 min with [[admiral_spoils_6:1]]) and 12 h.
- **[[admiral_spoils_5]]**: the attack fleet's Salvagers collect this battle's debris, after plunder.
- **[[admiral_spoils_7]]** only adds hydrogen in the space left in the holds.
- **[[admiral_spoils_8]]** only works in defence, not on towing.
- **[[admiral_spoils_9]]**: after a won attack, your combat ships load 30% of the battle's debris into their free holds, after plunder and the Salvagers.""",
    },
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Fleet Hunter | Firing Line 15 · Campaign 10 | [[admiral_firing_line_9]], weapons +9% (or hull +13%), shield +3%, [[admiral_firing_line_4]], [[admiral_firing_line_7]]; [[admiral_campaign_1]], hydrogen back on victories, victorious return, one more attack fleet |
| Raider | Campaign 15 · Spoils of War 10 | [[admiral_campaign_9]], [[admiral_campaign_7]], [[admiral_campaign_8]]; towing up to 50%, [[admiral_spoils_3:1]] or [[admiral_spoils_3:2]], faster repairs, combat recycling |
| Battle Looter | Spoils of War 15 · Firing Line 10 | [[admiral_spoils_9]], towing, [[admiral_spoils_7]], [[admiral_spoils_8]]; weapons +9%, shield +3%, [[admiral_firing_line_4]], [[admiral_firing_line_5]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**[[admiral_firing_line_9]] is set before leaving**: the targeted unit type is designated in the sending form. Spy first.",
        "**[[admiral_firing_line_3:2]] removes the weapons bonus**: with it, [[admiral_firing_line_2]] no longer gives any damage.",
        "**[[admiral_firing_line_5]] may add nothing**: with [[admiral_firing_line_4]] at rank 3 and [[admiral_firing_line_6:1]], every rapid fire is already better served.",
        "**[[admiral_campaign_9]] does not go far**: the second target must be at most 1 system from the first, and the fleet pays the jump with the hydrogen in its holds.",
        "**No Repair Station, no towing**: a fleet leaving from a moon tows nothing. Without [[admiral_spoils_3:1]], a fleet wiped out gives nothing back.",
        "**[[admiral_campaign_4]] does not count toward the speed cap**, but [[admiral_campaign_1]] does: it takes the class's 10% speed accent.",
        "**[[admiral_campaign_8]] also hits a Veteran**: their defence repair loses 15 points against you.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Classes](/en/dynasty/classes)", "[Common tree](/en/dynasty/common-tree)",
        "[Dynasties](/en/dynasty/dynasties)", "[Rapid fire](/en/fleet/rapid-fire)", "[Plunder](/en/combat/plunder)",
        "[Debris fields](/en/combat/debris)", "[Repair Station](/en/economy/repair-station)",
        "[Defense rebuild](/en/combat/defense-rebuild)", "[Moon destruction](/en/combat/moon-destruction)",
    ],
}
