from combat_lib import *
from write import write, table

def body(lang):
    N = lambda x: n(x, lang)
    P = lambda x: pct(x, lang)
    stock = (100000, 60000, 20000)
    lt = loot(stock)
    hold10 = cargo('large_cargo', 10)
    hold10h = cargo('large_cargo', 10, 4)
    part = fit(lt, 45000)
    left = tuple(s - l for s, l in zip(stock, lt))
    lt2 = loot(left)
    hf = cargo('heavy_fighter', 50)
    cargo_rows = [[name(u[0], lang), N(u[7]), N(cargo(u[0], 1, 5)), N(cargo(u[0], 1, 10))] for u in SHIPS if u[7] > 0]
    res = 'métal, cristal, hydrogène'
    if lang == 'fr':
        return f'''# Pillage

> **En bref** : quand l'attaquant gagne un combat, il emporte **{P(LOOT)} de chaque ressource** stockée sur la planète ou la lune visée, dans la limite de la soute libre de ses vaisseaux survivants. Si la soute est trop petite, chaque ressource est réduite dans la même proportion. Ce taux est le même dans tous les univers.
{{.is-info}}

## Règles

1. Le pillage n'a lieu **qu'en cas de victoire** de l'attaquant. Un match nul ou une défaite ne rapporte rien.
2. Le stock de la cible est d'abord mis à jour à l'instant de l'arrivée : la production accumulée depuis la dernière visite du joueur compte.
3. Le butin vaut **{P(LOOT)} de chaque ressource** (métal, cristal, hydrogène), arrondi à l'inférieur. L'énergie ne se pille pas.
4. Le butin est limité par la **soute libre des vaisseaux survivants** : leur capacité de fret, augmentée de **5 % par niveau** de Pliage Spatial, moins ce qui est déjà à bord.
5. Si le butin dépasse la soute, **chaque ressource est réduite dans la même proportion** (arrondi à l'inférieur). Il n'y a pas d'ordre de priorité entre les ressources.
6. La cible perd exactement ce qui a été emporté.
7. Le taux ne baisse pas d'une attaque à l'autre : c'est le stock de la cible qui diminue. Piller plusieurs fois le même joueur rapporte donc de moins en moins s'il ne produit pas entre-temps.
8. Une **lune** se pille comme une planète : c'est le stock de la lune qui compte.
9. Les bâtiments, les vaisseaux et les défenses ne se pillent pas.

### Ce qui modifie le pillage
10. Les talents de [dynastie et de classe](/fr/dynasty/talents) peuvent changer ces règles : le défenseur peut mettre une part de son stock à l'abri (le taux qu'il subit ne descend jamais sous **{P(LOOT_FLOOR)}**) ; l'attaquant peut piller davantage une planète abandonnée, piller un peu sur un match nul, agrandir ses soutes ou choisir l'ordre de chargement.

## Exemple chiffré

La cible stocke {N(stock[0])} métal, {N(stock[1])} cristal et {N(stock[2])} hydrogène.
- Butin possible : {N(lt[0])} métal, {N(lt[1])} cristal, {N(lt[2])} hydrogène, soit **{N(sum(lt))}**.
- Avec 10 Cargos stellaires survivants ({N(hold10)} de soute, {N(hold10h)} avec Pliage Spatial 4) : tout est emporté.
- Avec 50 Assaillants seulement ({N(hf)} de soute) : la soute ne prend que {N(hf)} sur {N(sum(lt))}.
- Avec {N(45000)} de soute libre, soit la moitié du butin : **{N(part[0])} métal, {N(part[1])} cristal et {N(part[2])} hydrogène**.
- Après un premier raid complet ({N(sum(lt))} emportés), il reste {N(left[0])} métal, {N(left[1])} cristal et {N(left[2])} hydrogène : une seconde attaque juste après, sans production entre-temps, ne peut plus emporter que **{N(sum(lt2))}**.

## Données détaillées

Capacité de fret par vaisseau, selon le niveau de Pliage Spatial :

{table(['Vaisseau', 'Sans Pliage Spatial', 'Pliage Spatial 5', 'Pliage Spatial 10'], cargo_rows)}

## Pièges fréquents

- **Venez avec de la soute** : les vaisseaux de combat transportent peu. Ajoutez des Cargos stellaires à votre flotte d'attaque.
- **Les pertes réduisent la soute** : seuls les vaisseaux survivants emportent le butin.
- **Un match nul ne rapporte rien** : il faut éliminer toute la défense pour piller.
- **Changez de cible** : chaque raid sur le même joueur rapporte moins que le précédent.

## Pages liées

- [Déroulement d'un combat](/fr/combat/how-combat-works)
- [Limite d'attaques](/fr/players/attack-limit)
- [Liste des vaisseaux](/fr/fleet/ships)
- [Le stockage](/fr/economy/storage)
'''
    return f'''# Plunder

> **In short**: when the attacker wins a battle, it takes **{P(LOOT)} of each resource** stored on the target planet or moon, within the free cargo space of its surviving ships. If the cargo space is too small, each resource is reduced in the same proportion. This rate is the same in every universe.
{{.is-info}}

## Rules

1. Plunder only happens **when the attacker wins**. A draw or a defeat brings nothing.
2. The target's stock is first brought up to the moment of arrival: production built up since the player's last visit counts.
3. The loot is **{P(LOOT)} of each resource** (metal, crystal, hydrogen), rounded down. Energy cannot be plundered.
4. The loot is capped by the **free cargo space of surviving ships**: their cargo capacity, increased by **5% per level** of Hyperspace Technology, minus what is already on board.
5. If the loot exceeds the cargo space, **each resource is reduced in the same proportion** (rounded down). There is no priority order between resources.
6. The target loses exactly what was carried away.
7. The rate does not drop from one attack to the next: the target's stock does. Plundering the same player several times therefore brings less and less if they do not produce in between.
8. A **moon** is plundered like a planet: the moon's own stock counts.
9. Buildings, ships and defenses cannot be plundered.

### What changes plunder
10. [Dynasty and class talents](/en/dynasty/talents) can change these rules: the defender can shelter part of its stock (the rate it suffers never goes below **{P(LOOT_FLOOR)}**); the attacker can plunder more from an abandoned planet, plunder a little on a draw, enlarge its holds or choose the loading order.

## Worked example

The target stores {N(stock[0])} metal, {N(stock[1])} crystal and {N(stock[2])} hydrogen.
- Possible loot: {N(lt[0])} metal, {N(lt[1])} crystal, {N(lt[2])} hydrogen, so **{N(sum(lt))}**.
- With 10 surviving Stellar Freighters ({N(hold10)} cargo, {N(hold10h)} with Hyperspace Technology 4): everything is taken.
- With only 50 Assailants ({N(hf)} cargo): the holds take only {N(hf)} out of {N(sum(lt))}.
- With {N(45000)} free cargo space, half the loot: **{N(part[0])} metal, {N(part[1])} crystal and {N(part[2])} hydrogen**.
- After a first full raid ({N(sum(lt))} taken), {N(left[0])} metal, {N(left[1])} crystal and {N(left[2])} hydrogen remain: a second attack right after, with no production in between, can only take **{N(sum(lt2))}**.

## Detailed data

Cargo capacity per ship, by Hyperspace Technology level (ship names are provisional translations: the game still shows the French names):

{table(['Ship', 'No Hyperspace Technology', 'Hyperspace Technology 5', 'Hyperspace Technology 10'], cargo_rows)}

## Common pitfalls

- **Bring cargo space**: combat ships carry little. Add Stellar Freighters to your attack fleet.
- **Losses shrink the cargo**: only surviving ships carry the loot.
- **A draw brings nothing**: you must wipe out the whole defense to plunder.
- **Switch targets**: each raid on the same player brings less than the previous one.

## Related pages

- [How combat works](/en/combat/how-combat-works)
- [Attack limit](/en/players/attack-limit)
- [Ship list](/en/fleet/ships)
- [Storage](/en/economy/storage)
'''

def run():
    write('fr', 'combat/plunder', body('fr'))
    write('en', 'combat/plunder', body('en'))
