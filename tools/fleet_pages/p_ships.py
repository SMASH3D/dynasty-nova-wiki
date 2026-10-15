import sys; sys.path.insert(0, sys.argv[1])
from fleet_lib import *; from write import *

ROLE = {
    'small_cargo': ('Petit transport rapide', 'Small fast transport'),
    'large_cargo': ('Gros transport', 'Large transport'),
    'colony_ship': ('Fonde une colonie', 'Founds a colony'),
    'recycler': ('Recycle les champs de ruines', 'Recycles debris fields'),
    'espionage_probe': ("Sonde d'espionnage", 'Espionage probe'),
    'solar_satellite': ("Produit de l'énergie en orbite, ne vole pas", 'Produces energy in orbit, never flies'),
    'light_fighter': ('Chasseur de base', 'Basic fighter'),
    'heavy_fighter': ('Chasseur plus résistant', 'Sturdier fighter'),
    'cruiser': ('Spécialiste anti-Intercepteur', 'Anti-Interceptor specialist'),
    'battleship': ('Vaisseau de ligne', 'Ship of the line'),
    'bomber': ('Spécialiste anti-défenses', 'Anti-defense specialist'),
    'predator': ('Chasseur de flottes', 'Fleet hunter'),
    'destroyer': ('Le plus puissant de la flotte standard', 'Strongest of the standard fleet'),
    'battle_cruiser': ('Vaisseau ultime, détruit les lunes', 'Ultimate ship, destroys moons'),
}
DRIVE_RES = {'combustion': 'combustion_drive', 'impulse': 'impulse_drive', 'hyperspace': 'hyperspace_drive'}


def nm(code, lang, img=False):
    s = S[code]
    name = s[1] if lang == 'fr' else f'*{s[2]}* ({s[1]})'
    alt = s[1] if lang == 'fr' else f'{s[2]} ({s[1]})'
    return (f'<img src="/images/illustrations/ships/{s[3]}.jpg" width="48" alt="{alt}"> ' if img else '') + name


def rname(code, lang):
    if code == 'shipyard':
        return 'Dock orbital' if lang == 'fr' else 'Orbital Dock'
    return RES[code][0 if lang == 'fr' else 1]


def body(lang):
    fr = lang == 'fr'
    N = lambda x: n(x, lang)
    L = 0 if fr else 1
    costs, stats, prereq, drives = [], [], [], []
    for s in SHIPS:
        code = s[0]
        m, c, h = s[6]
        p = points(code)
        costs.append([nm(code, lang, True), TYPE[s[4]][L], N(m), N(c), N(h), N(p), hms(s[13], lang), ROLE[code][L]])
        drv = RES[DRIVE_RES[s[5]]][L] if s[5] else ('aucun' if fr else 'none')
        stats.append([nm(code, lang), N(s[7]), N(s[7] // 10), N(s[8]), N(s[9]), N(s[10]), N(s[11]), drv, N(s[12])])
        dock = s[15][0][1]
        rs = ', '.join(f'{rname(r, lang)} {lv}' for r, lv in s[15][1:]) or ('aucune' if fr else 'none')
        prereq.append([nm(code, lang), N(dock), rs])
        for (d, lv, spd, fuel) in s[14]:
            drives.append([nm(code, lang), f'{RES[DRIVE_RES[s[5]]][L]} · {N(s[11])} · {N(s[12])}',
                           f'{RES[DRIVE_RES[d]][L]} {lv}', f'{RES[DRIVE_RES[d]][L]} · {N(spd)} · {N(fuel)}'])
    if fr:
        T1 = table(['Vaisseau', 'Famille', 'Métal', 'Cristal', 'Hydrogène', 'Points', 'Durée de base', 'Rôle'], costs)
        T2 = table(['Vaisseau', 'Structure', 'Coque en combat', 'Bouclier', 'Attaque', 'Fret', 'Vitesse', 'Moteur', 'Consommation'], stats)
        T3 = table(['Vaisseau', 'Dock orbital', 'Recherches'], prereq)
        T4 = table(["Vaisseau", "Moteur d'origine · vitesse · consommation", 'Change de moteur à', 'Nouveau moteur · vitesse · consommation'], drives)
    else:
        T1 = table(['Ship', 'Family', 'Metal', 'Crystal', 'Hydrogen', 'Points', 'Base time', 'Role'], costs)
        T2 = table(['Ship', 'Structure', 'Combat hull', 'Shield', 'Attack', 'Cargo', 'Speed', 'Drive', 'Consumption'], stats)
        T3 = table(['Ship', 'Orbital Dock', 'Research'], prereq)
        T4 = table(['Ship', 'Built-in drive · speed · consumption', 'Switches drive at', 'New drive · speed · consumption'], drives)

    # Exemples recalculés
    lv_a = {'combustion_drive': 6, 'impulse_drive': 4}
    lv_b = {'combustion_drive': 6, 'impulse_drive': 5}
    va, vb = speed('small_cargo', lv_a), speed('small_cargo', lv_b)
    fa, fb = propulsion('small_cargo', lv_a)[2], propulsion('small_cargo', lv_b)[2]
    car = cargo('large_cargo', 3)
    li_v = speed('light_fighter', {'combustion_drive': 6})
    att = round(50 * 1.2); hull = round(round(4000 * 1.3) / 10)
    if fr:
        return f'''# Liste des vaisseaux

> **En bref** : Dynasty Nova compte 14 vaisseaux, construits au Dock orbital. Le jeu les range en trois familles : civils (transporter, coloniser, recycler, espionner), de combat et spéciaux. Cette page donne pour chacun son coût, sa durée de construction, ses prérequis, ses statistiques et son moteur.
{{.is-info}}

> **Paramètre d'univers** : la vitesse de chantier divise la durée de construction des vaisseaux.
> Par défaut : **×1** · Redline : **×1**
{{.is-info}}

## Règles

1. Les vaisseaux se construisent au **Dock orbital**, sur une planète ou une lune. Une commande n'est acceptée que si la base peut la payer en entier ; chaque unité est ensuite payée au moment où elle entre en production (voir [Dock orbital](/fr/fleet/orbital-dock)).
2. Un vaisseau coûte **toujours le même prix**, quel que soit le nombre déjà construit.
3. Le jeu les classe en trois familles : **Vaisseaux Civils**, **Vaisseaux de Combat** et **Vaisseaux Spéciaux**.
4. Chaque vaisseau a un **moteur d'origine**. La Navette de fret, le Récupérateur et le Frappe-orbital **passent d'eux-mêmes à un meilleur moteur** quand la recherche de ce moteur atteint un niveau donné : leur vitesse de base et leur consommation changent avec lui (table plus bas). Si plusieurs objectifs sont atteints, le moteur le plus avancé l'emporte.
5. **Vitesse** = vitesse de base du moteur × (1 + bonus × niveau de la recherche de ce moteur) : **+10 %** par niveau de Propulseur Chimique, **+20 %** de Moteur Magnétique, **+30 %** de Navigation Transdimensionnelle. Une flotte avance à la vitesse de son vaisseau le plus lent (voir [Déplacements](/fr/fleet/movement)).
6. **Consommation** : aucune recherche ne la baisse. Un meilleur moteur consomme davantage.
7. **Fret** : +5 % par niveau de Pliage Spatial, arrondi à l'unité.
8. **Combat** : l'attaque, le bouclier et la structure augmentent de 10 % par niveau de Systèmes Offensifs, Champs de Protection et Métallurgie Avancée. La **coque en combat** vaut la structure divisée par 10.
9. **Points** : chaque vaisseau rapporte 1 point par tranche de 1 000 ressources de son coût (métal, cristal et hydrogène). **Tous les vaisseaux**, civils compris, comptent dans les points militaires : ils sont crédités à la livraison et retirés quand le vaisseau est perdu.
10. Le **Collecteur solaire** ne vole jamais : il reste en orbite et produit partie entière(Tmax / 4 + 20) énergie, jamais moins de 0, où Tmax est la température maximale de la planète en °C (voir [L'énergie](/fr/economy/energy)).
11. Un vaisseau détruit est perdu. Après un combat où votre base se défend, la [Station de réparation](/fr/economy/repair-station) en récupère une partie.

## Exemple chiffré

**Une Navette de fret avant et après son changement de moteur**, avec Propulseur Chimique 6 :
- Moteur Magnétique 4 : elle garde le Propulseur Chimique, vitesse 5 000 × (1 + 0,1 × 6) = **{N(va)}**, consommation **{N(fa)}**.
- Moteur Magnétique 5 : elle passe au Moteur Magnétique, vitesse 10 000 × (1 + 0,2 × 5) = **{N(vb)}**, consommation **{N(fb)}**.

**10 Cargos stellaires avec Pliage Spatial 3** : fret d'un Cargo 25 000 × (1 + 0,05 × 3) = {N(car)}, soit **{N(10 * car)} ressources** pour la flotte.

**Un Intercepteur** avec Propulseur Chimique 6, Systèmes Offensifs 2, Champs de Protection 0, Métallurgie Avancée 3 : vitesse 12 500 × 1,6 = **{N(li_v)}** ; attaque 50 × 1,2 = **{att}** ; bouclier **10** ; coque en combat 4 000 × 1,3 / 10 = **{hull}**.

## Données détaillées

### Coûts, durées et rôles

La durée de base se divise par (1 + niveau du Dock orbital) × 2^(niveau de l'Assembleur moléculaire) et par la vitesse de chantier (voir [Dock orbital](/fr/fleet/orbital-dock)).

{T1}

### Statistiques de base (sans recherche, moteur d'origine)

{T2}

Chaque vaisseau tire une fois par round, plus les tirs supplémentaires de ses [tirs rapides](/fr/fleet/rapid-fire).

### Changements de moteur

{T4}

Le Récupérateur passe à la Navigation Transdimensionnelle dès son niveau 15, même sans Moteur Magnétique 17 : chaque objectif suffit à lui seul.

### Prérequis

{T3}

## Pièges fréquents

- **Le moteur change, la consommation aussi** : une Navette de fret au Moteur Magnétique va deux fois plus vite au départ mais consomme le double. Un Récupérateur à la Navigation Transdimensionnelle consomme trois fois plus qu'au Propulseur Chimique.
- **Un tir trop faible rebondit** : un tir inférieur à 1 % du bouclier de la cible n'a aucun effet (voir [Déroulement d'un combat](/fr/combat/how-combat-works)).
- **Le Colossus stellaire est très lent** : vitesse de base 100. Une flotte qui en contient un avance à son rythme.
- **Le facteur de distorsion n'a aucun effet** : le jeu l'affiche, mais aucun calcul ne s'en sert.
- **Le fret ne sert pas qu'au transport** : il limite aussi le pillage, le recyclage, les trouvailles d'expédition et l'hydrogène du voyage, qui voyage dans les soutes.
- **Les civils comptent aussi** : perdre des Cargos ou des Éclaireurs fait baisser vos points militaires.

## Pages liées

- [Tirs rapides](/fr/fleet/rapid-fire)
- [Dock orbital](/fr/fleet/orbital-dock)
- [Déplacements](/fr/fleet/movement)
- [Les missions](/fr/fleet/missions)
- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Station de réparation](/fr/economy/repair-station)
- [Glossaire](/fr/getting-started/glossary)
'''
    return f'''# Ships list

> **In short**: Dynasty Nova has 14 ships, built at the Orbital Dock. The game sorts them into three families: civil (carry, colonize, recycle, spy), combat and special. This page gives each ship's cost, build time, requirements, stats and drive.
{{.is-info}}

> Ships are not translated in the game yet: it shows their French name (in brackets below) in every language. The English names used here are provisional.
{{.is-warning}}

> **Universe setting**: the shipyard speed divides ship build times.
> Default: **×1** · Redline: **×1**
{{.is-info}}

## Rules

1. Ships are built at the **Orbital Dock**, on a planet or a moon. An order is only accepted if the base can pay for all of it; each unit is then paid when it enters production (see [Orbital Dock](/en/fleet/orbital-dock)).
2. A ship **always costs the same**, however many you already built.
3. The game sorts them into three families: **Civil Ships**, **Combat Ships** and **Special Ships**.
4. Every ship has a **built-in drive**. The Cargo Shuttle, the Salvager and the Orbital Striker **switch to a better drive on their own** once that drive's research reaches a given level: their base speed and consumption change with it (table below). If several goals are met, the most advanced drive wins.
5. **Speed** = the drive's base speed × (1 + bonus × level of that drive's research): **+10%** per level of Combustion Drive, **+20%** of Impulse Drive, **+30%** of Hyperspace Drive. A fleet flies at the speed of its slowest ship (see [Fleet movement](/en/fleet/movement)).
6. **Consumption**: no research lowers it. A better drive burns more.
7. **Cargo**: +5% per level of Hyperspace Technology, rounded to the unit.
8. **Combat**: attack, shield and structure rise by 10% per level of Weapon Systems, Shielding Technology and Armor Technology. The **combat hull** equals structure divided by 10.
9. **Points**: each ship is worth 1 point per 1,000 resources of its cost (metal, crystal and hydrogen). **Every ship**, civil ones included, counts towards military points: they are credited on delivery and removed when the ship is lost.
10. The **Solar Collector** never flies: it stays in orbit and produces floor(Tmax / 4 + 20) energy, never below 0, where Tmax is the planet's maximum temperature in °C (see [Energy](/en/economy/energy)).
11. A destroyed ship is lost. After a battle where your base defends, the [Repair Station](/en/economy/repair-station) recovers part of them.

## Worked example

**A Cargo Shuttle before and after its drive switch**, with Combustion Drive 6:
- Impulse Drive 4: it keeps the Combustion Drive, speed 5,000 × (1 + 0.1 × 6) = **{N(va)}**, consumption **{N(fa)}**.
- Impulse Drive 5: it switches to the Impulse Drive, speed 10,000 × (1 + 0.2 × 5) = **{N(vb)}**, consumption **{N(fb)}**.

**10 Stellar Freighters with Hyperspace Technology 3**: one Freighter carries 25,000 × (1 + 0.05 × 3) = {N(car)}, so **{N(10 * car)} resources** for the fleet.

**An Interceptor** with Combustion Drive 6, Weapon Systems 2, Shielding Technology 0, Armor Technology 3: speed 12,500 × 1.6 = **{N(li_v)}**; attack 50 × 1.2 = **{att}**; shield **10**; combat hull 4,000 × 1.3 / 10 = **{hull}**.

## Detailed data

### Costs, build times and roles

The base time is divided by (1 + Orbital Dock level) × 2^(Molecular Assembler level) and by the shipyard speed (see [Orbital Dock](/en/fleet/orbital-dock)).

{T1}

### Base stats (no research, built-in drive)

{T2}

Each ship fires once per round, plus the extra shots of its [rapid fire](/en/fleet/rapid-fire).

### Drive switches

{T4}

The Salvager switches to the Hyperspace Drive at level 15, even without Impulse Drive 17: each goal is enough on its own.

### Requirements

{T3}

## Common pitfalls

- **New drive, new consumption**: a Cargo Shuttle on the Impulse Drive starts twice as fast but burns twice as much. A Salvager on the Hyperspace Drive burns three times what it does on the Combustion Drive.
- **A weak shot bounces off**: a shot below 1% of the target's shield does nothing (see [How combat works](/en/combat/how-combat-works)).
- **The Stellar Colossus is very slow**: base speed 100. A fleet with one in it flies at its pace.
- **The warp factor does nothing**: the game shows it, but no calculation uses it.
- **Cargo is not only for transport**: it also caps plunder, recycling, expedition finds and the trip's hydrogen, which travels in the holds.
- **Civil ships count too**: losing Freighters or Scouts lowers your military points.

## Related pages

- [Rapid fire](/en/fleet/rapid-fire)
- [Orbital Dock](/en/fleet/orbital-dock)
- [Fleet movement](/en/fleet/movement)
- [Missions](/en/fleet/missions)
- [How combat works](/en/combat/how-combat-works)
- [Repair Station](/en/economy/repair-station)
- [Glossary](/en/getting-started/glossary)
'''


for lang in ('fr', 'en'):
    write(lang, 'fleet/ships', body(lang))
