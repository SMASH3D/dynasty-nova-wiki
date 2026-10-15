"""L'Énergéticien : textes vérifiés sur le code (backend 7b255c83, notes du 15 octobre 2026)."""

FR = {
    'brief': "pour l'Énergéticien, l'énergie n'est jamais perdue. Surrégime pousse les mines au-delà de leur plein régime et convertit le surplus en hydrogène ; Centrales rend les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires plus forts et moins chers à faire tourner ; Continuité empêche un manque d'énergie de freiner les mines.",
    'rules': [
        "Le bonus générique d'énergie, +8 % sur les Capteurs photovoltaïques, le Réacteur thermonucléaire et les Collecteurs solaires ([[common_prosperity_6:1]]), vient de l'[arbre commun](/fr/dynasty/common-tree). L'Énergéticien n'a que des **mécaniques**, et un seul accent : la vitesse de construction des Capteurs photovoltaïques et du Réacteur thermonucléaire ([[energist_continuity_6:2]], 10 %).",
        "Le surplus de production d'une mine en surrégime se calcule sur sa **production propre**, à côté de la Maîtrise du Plasma et des bonus de production, sans être multiplié par eux et hors du plafond de production des mines. Le manque d'énergie freine ensuite toute la production de la base ; l'électrolyse convertit enfin l'énergie restée inutilisée.",
        "**Surrégime** : une mine réglée à 100 % tourne à 110 %. [[energist_overdrive_3:1]] et [[energist_overdrive_4]] montent ce taux à **131 %** sur une mine par base ; [[energist_overdrive_3:2]] permet trois mines par base, à 119 % au plus. [[energist_overdrive_9]] porte une mine désignée par base à 140 %.",
        "**Délestage** : en déficit, chaque mine récupère une part des points de rendement qui lui manquent, **15 points au plus** (30 avec [[energist_continuity_7]]).",
    ],
    'example': """Univers à vitesse 1. Un Excavateur minéral niveau 20 produit **4 036 métal par heure** et consomme **1 345 d'énergie** (voir [L'énergie](/fr/economy/energy)).

**Surrégime complet**
- [[energist_overdrive_7]] au rang 3 : 1 345 × 0,91 = **1 223** d'énergie (arrondi inférieur).
- [[energist_overdrive_1]], [[energist_overdrive_3:1]] et [[energist_overdrive_4]] au rang 3 (131 %) : 4 036 + 4 036 × 31 % = 4 036 + 1 251 = **5 287 métal par heure**.
- Avec [[energist_overdrive_2]] au rang 3, le surcoût passe de 25 % à 13 % : 1 223 × 1,13 = **1 381** d'énergie, à peine 36 de plus que la mine sans aucun talent.
- [[energist_overdrive_9]] sur cette mine (140 %) : 4 036 + 1 614 = **5 650 métal par heure**. Les 9 points au-delà de 131 % coûtent 4 % chacun : surcoût 13 + 36 = 49 %, soit 1 223 × 1,49 = **1 822** d'énergie.

**Délestage, base à 50 % d'énergie**
- Avec [[energist_continuity_2]] au rang 3 et [[energist_continuity_3:1]] (40 %), il manque 50 points ; 40 % de 50 = 20, ramenés à 15 : les mines tournent à **65 %**. Avec [[energist_continuity_7]] au rang 3 (30 points au plus) : **70 %**.
- L'Excavateur 20 produit alors 2 623 puis **2 825 métal par heure**, au lieu de 2 018.

**Réacteur thermonucléaire niveau 10, Science Énergétique 3**
- Production : 30 × 10 × 1,08^10 = 647 d'énergie. Avec [[energist_plants_5]] (Science Énergétique comptée au niveau 4) : 30 × 10 × 1,09^10 = **710**, puis **766** avec [[common_prosperity_6:1]] (+8 %).
- Il brûle 10 × 10 × 1,1^10 = **259 hydrogène par heure**, 207 avec [[energist_plants_3:2]], **0** sur la base de [[energist_plants_9]] : 6 216 hydrogène économisés par jour.

**Collecteurs solaires, planète à 60 °C de température maximale**
- 100 Collecteurs : 100 × (60 / 4 + 20) = 3 500 d'énergie. [[energist_plants_2]] au rang 3 et [[common_prosperity_6:1]] (+23 %) : **4 305**. Pendant une [[energist_continuity_8]] : 4 305 × 1,5 = **6 457**.
- Une défense en détruit 100, sans Station de réparation : **49** restent sur la base avec [[energist_plants_1]], **70** avec [[energist_plants_7]] au rang 3.

**Électrolyse**
- 1 000 d'énergie inutilisée donnent **250 hydrogène par heure** avec [[energist_overdrive_5]], **333** avec [[energist_overdrive_6:1]], à condition que le Condensateur d'hydrogène de la base produise au moins 84 (ou 111) hydrogène par heure : l'électrolyse ne dépasse jamais 3 fois sa production.""",
    'branch_notes': {
        'overdrive': """- **[[energist_overdrive_1]]** : seule une mine réglée à 100 % peut passer en surrégime ; baisser son taux l'arrête. Le surcoût d'énergie s'applique sur la consommation déjà réduite par [[energist_overdrive_7]].
- **[[energist_overdrive_5]]** : l'énergie restée inutilisée une fois tout servi, surrégime compris. Par heure, l'électrolyse ne donne jamais plus de 3 fois ce que produit le Condensateur d'hydrogène de la base : pas de Condensateur, pas d'hydrogène. Elle s'arrête tant que la réserve de [[energist_continuity_6:1]] se remplit.
- **[[energist_overdrive_6:2]]** se choisit base par base ; il exclut [[energist_overdrive_6:1]], donc il faut 4 d'énergie pour 3 métal ou 2 cristal. Le plafond est alors 3 fois la production de l'Excavateur minéral ou de l'Extracteur cristallin de la base.
- **[[energist_overdrive_8]]** : si le surrégime devait faire passer la base en déficit, tout le surrégime de la base ([[energist_overdrive_9]] compris) recule de la même part, juste assez pour garder l'énergie à l'équilibre ; il revient seul quand l'énergie le permet.
- **[[energist_overdrive_9]]** : la mine désignée doit être en surrégime. Chaque point au-delà du taux de surrégime coûte 4 % d'énergie (20 % par tranche de 5 points), ajoutés au surcoût du surrégime : 36 % depuis 131 %, 84 % depuis 119 %.""",
        'plants': """- **[[energist_plants_1]]** : après un combat où la base perd des Collecteurs solaires, 49 % des Collecteurs détruits (arrondi inférieur) restent aussitôt sur la base. Ceux que la Station de réparation a déjà pris en charge sont décomptés : vous récupérez le plus grand des deux nombres. Le champ de débris est calculé sur toutes les pertes.
- **[[energist_plants_2]]**, **[[energist_plants_3:1]]** : ces pourcentages s'ajoutent aux 8 % de [[common_prosperity_6:1]] (23 % pour les Collecteurs, 18 % pour les Capteurs).
- **[[energist_plants_4]]** : les Capteurs lisent la température du jour plus 45 % de l'écart jusqu'au maximum du mois. Les Capteurs ne gagnent rien sous 0 °C : sur une planète froide, le nœud ne change rien.
- **[[energist_plants_6:1]]** : sans ce nœud, le Réacteur tourne toujours à 100 %, quel que soit son réglage. Avec lui, son énergie et sa consommation d'hydrogène suivent le taux choisi.
- **[[energist_plants_6:2]]** s'applique en plus du plafond de 5 % des réductions de coût.
- **[[energist_plants_8]]** : les Collecteurs bâtis sur leur propre file ne puisent pas dans l'avance du Dock orbital d'un Bâtisseur.
- **[[energist_plants_9]]** : vous désignez la base, et pouvez en changer.""",
        'continuity': """- **[[energist_continuity_1]]** : le niveau qui s'achève produit aussitôt ; seule sa consommation attend, celle du niveau précédent restant en vigueur pendant le délai.
- **[[energist_continuity_3:2]]** : sur une colonie fondée par un Pionnier spatial depuis moins de 30 jours, pas sur la planète mère.
- **[[energist_continuity_5]]** : la mine désignée tourne à plein tant que la production d'énergie couvre **sa** consommation ; les autres se partagent le reste, avec leur délestage.
- **[[energist_continuity_6:1]]** : la base garde au plus 12 heures de son surplus du moment. En déficit, la réserve couvre tout le manque, les mines tournant à plein, jusqu'à épuisement.
- **[[energist_continuity_8]]** : sur une base qui a des Capteurs photovoltaïques ou des Collecteurs solaires, 24 h après la précédente, pour tout votre empire.
- **[[energist_continuity_9]]** : chaque planète en déficit reçoit au plus le plus petit de son manque et de 20 % de sa consommation, dans la limite du surplus des autres, partagé à proportion. Les lunes n'y prennent pas part. Le partage se refait régulièrement.
- **[[energist_continuity_8]]** et **[[energist_continuity_9]]** ne comptent pas pour l'énergie qu'exige une recherche comme Manipulation Gravitationnelle.""",
    },
    'builds': """| Build | Répartition | Ce qu'il obtient |
|---|---|---|
| Mineur à excédent | Surrégime 15 · Centrales 10 | une mine à 131 % ou trois à 119 % par base, surcoût de 13 %, électrolyse, mines −9 % d'énergie, [[energist_overdrive_8]], une mine jusqu'à 140 % avec [[energist_overdrive_9]] ; Collecteurs +15 %, [[energist_plants_3:1]] ou [[energist_plants_3:2]], [[energist_plants_4]], [[energist_plants_5]] |
| Grimpeur | Continuité 15 · Surrégime 10 | report de 10 h, délestage jusqu'à 30 points (40 % du manque), [[energist_continuity_5]], [[energist_continuity_8]], [[energist_continuity_9]] ; une mine à 131 % ou trois à 119 %, électrolyse |
| Seigneur des Collecteurs | Centrales 15 · Continuité 10 | Collecteurs relevés à 70 %, [[energist_plants_8]], [[energist_plants_6:2]] −20 %, [[energist_plants_9]] sur une base ; report de 10 h, délestage, [[energist_continuity_5]] |

Avant la rangée 7 de la branche principale, placez au moins 2 points dans la seconde : la porte demande 12 points, et les rangées 1 à 6 d'une branche n'en contiennent que 10.""",
    'pitfalls': [
        "**Le surrégime se paie toujours en énergie** : sans surplus, il fait passer la base en déficit et freine les trois mines. [[energist_overdrive_8]] le fait reculer à temps.",
        "**Une mine en surrégime doit rester à 100 %** : baisser son taux arrête le surrégime.",
        "**L'électrolyse ne crée rien à partir d'une énergie déjà utilisée**, ni sans Condensateur d'hydrogène sur la base, ni tant que la réserve de [[energist_continuity_6:1]] se remplit.",
        "**Le délestage est borné** : en déficit profond, il ne rend que 15 points de rendement (30 avec [[energist_continuity_7]]).",
        "**Aucun talent de Continuité ne produit de minerai** : la branche retire le frein qui empêche de monter une mine avant sa centrale.",
        "**La rangée 3 des Centrales décide de votre énergie** : les Capteurs photovoltaïques ne brûlent rien mais dépendent de la température, et [[energist_plants_4]] ne sert à rien sur une planète froide ; le Réacteur brûle de l'hydrogène mais monte avec la Science Énergétique.",
        "**[[energist_continuity_8]] et [[energist_continuity_9]] ne débloquent pas Manipulation Gravitationnelle** : l'énergie qu'elle exige se lit sans eux.",
    ],
    'related': [
        "[Les talents](/fr/dynasty/talents)", "[Arbre commun](/fr/dynasty/common-tree)", "[Classes](/fr/dynasty/classes)",
        "[L'énergie](/fr/economy/energy)", "[Planètes : taille, température, type](/fr/universe/planets)",
        "[Station de réparation](/fr/economy/repair-station)",
    ],
}

EN = {
    'brief': "for the Energetician, energy is never wasted. Overdrive pushes mines past their full rate and turns the surplus into hydrogen; Plants makes the Photovoltaic Sensors, the Thermonuclear Reactor and the Solar Collectors stronger and cheaper to run; Continuity keeps an energy shortfall from slowing the mines.",
    'rules': [
        "The generic energy bonus, +8% on the Photovoltaic Sensors, the Thermonuclear Reactor and the Solar Collectors ([[common_prosperity_6:1]]), comes from the [common tree](/en/dynasty/common-tree). The Energetician only has **mechanics**, and a single accent: the construction speed of the Photovoltaic Sensors and the Thermonuclear Reactor ([[energist_continuity_6:2]], 10%).",
        "The extra output of an overdriven mine is computed on its **own production**, beside Plasma Technology and the production bonuses, without being multiplied by them and outside the mines' production cap. The energy shortfall then slows the base's whole production; electrolysis finally converts the energy left unused.",
        "**Overdrive**: a mine set to 100% runs at 110%. [[energist_overdrive_3:1]] and [[energist_overdrive_4]] raise that rate to **131%** on one mine per base; [[energist_overdrive_3:2]] allows three mines per base, at 119% at most. [[energist_overdrive_9]] takes one designated mine per base to 140%.",
        "**Load shedding**: in deficit, each mine wins back a share of the output points it lacks, **15 points at most** (30 with [[energist_continuity_7]]).",
    ],
    'example': """Universe at speed 1. A level 20 Mineral Excavator produces **4,036 metal per hour** and draws **1,345 energy** (see [Energy](/en/economy/energy)).

**Full overdrive**
- [[energist_overdrive_7]] at rank 3: 1,345 × 0.91 = **1,223** energy (rounded down).
- [[energist_overdrive_1]], [[energist_overdrive_3:1]] and [[energist_overdrive_4]] at rank 3 (131%): 4,036 + 4,036 × 31% = 4,036 + 1,251 = **5,287 metal per hour**.
- With [[energist_overdrive_2]] at rank 3, the extra draw goes from 25% to 13%: 1,223 × 1.13 = **1,381** energy, only 36 more than the mine without any talent.
- [[energist_overdrive_9]] on this mine (140%): 4,036 + 1,614 = **5,650 metal per hour**. The 9 points past 131% cost 4% each: extra draw 13 + 36 = 49%, that is 1,223 × 1.49 = **1,822** energy.

**Load shedding, base at 50% energy**
- With [[energist_continuity_2]] at rank 3 and [[energist_continuity_3:1]] (40%), 50 points are missing; 40% of 50 = 20, brought down to 15: the mines run at **65%**. With [[energist_continuity_7]] at rank 3 (30 points at most): **70%**.
- The level 20 Excavator then produces 2,623, then **2,825 metal per hour**, instead of 2,018.

**Level 10 Thermonuclear Reactor, Energy Science 3**
- Output: 30 × 10 × 1.08^10 = 647 energy. With [[energist_plants_5]] (Energy Science counted at level 4): 30 × 10 × 1.09^10 = **710**, then **766** with [[common_prosperity_6:1]] (+8%).
- It burns 10 × 10 × 1.1^10 = **259 hydrogen per hour**, 207 with [[energist_plants_3:2]], **0** on the [[energist_plants_9]] base: 6,216 hydrogen saved per day.

**Solar Collectors, planet with a 60 °C maximum temperature**
- 100 Collectors: 100 × (60 / 4 + 20) = 3,500 energy. [[energist_plants_2]] at rank 3 and [[common_prosperity_6:1]] (+23%): **4,305**. While [[energist_continuity_8]] runs: 4,305 × 1.5 = **6,457**.
- A defense destroys 100 of them, without a Repair Station: **49** stay on the base with [[energist_plants_1]], **70** with [[energist_plants_7]] at rank 3.

**Electrolysis**
- 1,000 unused energy gives **250 hydrogen per hour** with [[energist_overdrive_5]], **333** with [[energist_overdrive_6:1]], provided the base's Hydrogen Condenser produces at least 84 (or 111) hydrogen per hour: electrolysis never exceeds 3 times its output.""",
    'branch_notes': {
        'overdrive': """- **[[energist_overdrive_1]]**: only a mine set to 100% can be overdriven; lowering its rate stops it. The extra draw applies to the draw already reduced by [[energist_overdrive_7]].
- **[[energist_overdrive_5]]**: the energy left unused once everything is served, overdrive included. Per hour, electrolysis never yields more than 3 times what the base's Hydrogen Condenser produces: no Condenser, no hydrogen. It stops while the [[energist_continuity_6:1]] reserve is filling.
- **[[energist_overdrive_6:2]]** is chosen base by base; it excludes [[energist_overdrive_6:1]], so it takes 4 energy for 3 metal or 2 crystal. The cap is then 3 times the output of the base's Mineral Excavator or Crystal Extractor.
- **[[energist_overdrive_8]]**: if overdrive would throw the base into deficit, the base's whole overdrive ([[energist_overdrive_9]] included) backs off by the same share, just enough to keep energy balanced; it comes back on its own when energy allows.
- **[[energist_overdrive_9]]**: the designated mine must be overdriven. Each point past the overdrive rate costs 4% energy (20% per 5-point step), added to the overdrive's extra draw: 36% from 131%, 84% from 119%.""",
        'plants': """- **[[energist_plants_1]]**: after a battle where the base loses Solar Collectors, 49% of the destroyed Collectors (rounded down) stay on the base at once. Those the Repair Station already took in are counted off: you get back the larger of the two numbers. The debris field is computed on all losses.
- **[[energist_plants_2]]**, **[[energist_plants_3:1]]**: these percentages add to the 8% of [[common_prosperity_6:1]] (23% for Collectors, 18% for Sensors).
- **[[energist_plants_4]]**: the Sensors read the day's temperature plus 45% of the gap up to the month's maximum. The Sensors gain nothing below 0 °C: on a cold planet, the node changes nothing.
- **[[energist_plants_6:1]]**: without this node, the Reactor always runs at 100%, whatever its setting. With it, its energy and hydrogen burn follow the chosen rate.
- **[[energist_plants_6:2]]** applies on top of the 5% cap on cost reductions.
- **[[energist_plants_8]]**: Collectors built on their own lane do not draw on a Builder's Orbital Dock head start.
- **[[energist_plants_9]]**: you designate the base, and can change it.""",
        'continuity': """- **[[energist_continuity_1]]**: the completed level produces at once; only its draw waits, the previous level's draw staying in force during the delay.
- **[[energist_continuity_3:2]]**: on a colony founded by a Space Pioneer less than 30 days ago, not on the home planet.
- **[[energist_continuity_5]]**: the designated mine runs full as long as energy production covers **its** draw; the others share the rest, with their load shedding.
- **[[energist_continuity_6:1]]**: the base stores at most 12 hours of its current surplus. In deficit, the reserve covers the whole shortfall, the mines running full, until it runs out.
- **[[energist_continuity_8]]**: on a base with Photovoltaic Sensors or Solar Collectors, 24 h after the previous one, for your whole empire.
- **[[energist_continuity_9]]**: each planet in deficit receives at most the smaller of its shortfall and 20% of its draw, within the others' surplus, shared in proportion. Moons take no part. The sharing is redone regularly.
- **[[energist_continuity_8]]** and **[[energist_continuity_9]]** do not count toward the energy a research such as Graviton Technology requires.""",
    },
    'builds': """| Build | Split | What it gets |
|---|---|---|
| Surplus Miner | Overdrive 15 · Plants 10 | one mine at 131% or three at 119% per base, 13% extra draw, electrolysis, mines −9% energy, [[energist_overdrive_8]], one mine up to 140% with [[energist_overdrive_9]]; Collectors +15%, [[energist_plants_3:1]] or [[energist_plants_3:2]], [[energist_plants_4]], [[energist_plants_5]] |
| Climber | Continuity 15 · Overdrive 10 | 10 h delay, load shedding up to 30 points (40% of the shortfall), [[energist_continuity_5]], [[energist_continuity_8]], [[energist_continuity_9]]; one mine at 131% or three at 119%, electrolysis |
| Lord of the Collectors | Plants 15 · Continuity 10 | Collectors raised at 70%, [[energist_plants_8]], [[energist_plants_6:2]] −20%, [[energist_plants_9]] on one base; 10 h delay, load shedding, [[energist_continuity_5]] |

Before row 7 of the main branch, place at least 2 points in the second one: the gate requires 12 points, and rows 1 to 6 of a branch only hold 10.""",
    'pitfalls': [
        "**Overdrive always costs energy**: without a surplus it throws the base into deficit and slows all three mines. [[energist_overdrive_8]] makes it back off in time.",
        "**An overdriven mine must stay at 100%**: lowering its rate stops the overdrive.",
        "**Electrolysis creates nothing from energy already used**, nor without a Hydrogen Condenser on the base, nor while the [[energist_continuity_6:1]] reserve is filling.",
        "**Load shedding is bounded**: in a deep deficit, it only gives back 15 output points (30 with [[energist_continuity_7]]).",
        "**No Continuity talent produces ore**: the branch removes the brake that stops you from raising a mine before its plant.",
        "**Row 3 of Plants decides your energy**: Photovoltaic Sensors burn nothing but depend on temperature, and [[energist_plants_4]] is useless on a cold planet; the Reactor burns hydrogen but grows with Energy Science.",
        "**[[energist_continuity_8]] and [[energist_continuity_9]] do not unlock Graviton Technology**: the energy it requires is read without them.",
    ],
    'related': [
        "[Talents](/en/dynasty/talents)", "[Common tree](/en/dynasty/common-tree)", "[Classes](/en/dynasty/classes)",
        "[Energy](/en/economy/energy)", "[Planets: size, temperature, type](/en/universe/planets)",
        "[Repair Station](/en/economy/repair-station)",
    ],
}
