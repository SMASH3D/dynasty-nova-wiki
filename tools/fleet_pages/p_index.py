import sys; sys.path.insert(0, sys.argv[1])
from write import *

FR = '''# Flotte

**Vaisseaux, déplacements et missions.** Les 14 vaisseaux du jeu se construisent au Dock orbital, volent à la vitesse du plus lent d'entre eux et partent toujours avec une mission.

## Pages de cette rubrique

- [Liste des vaisseaux](/fr/fleet/ships) : coûts, durées, statistiques, moteurs et prérequis.
- [Tirs rapides](/fr/fleet/rapid-fire) : qui tire plusieurs fois sur quoi, et comment.
- [Dock orbital (chantier)](/fr/fleet/orbital-dock) : files, paiement, livraison et durées de construction.
- [Déplacements](/fr/fleet/movement) : emplacements de flotte, distance, durée, hydrogène, rappel.
- [Les missions](/fr/fleet/missions) : les dix missions et leurs règles.
- [Expéditions](/fr/fleet/expeditions) : l'espace lointain, ses conditions et ses résultats.
- [Porte de saut](/fr/fleet/jump-gate) : sauts instantanés entre vos lunes.
'''
EN = '''# Fleet

**Ships, movement and missions.** The game's 14 ships are built at the Orbital Dock, fly at the speed of the slowest among them and always leave on a mission.

## Pages in this section

- [Ships list](/en/fleet/ships): costs, build times, stats, drives and requirements.
- [Rapid fire](/en/fleet/rapid-fire): who fires several times at what, and how.
- [Orbital Dock (shipyard)](/en/fleet/orbital-dock): queues, payment, delivery and build times.
- [Fleet movement](/en/fleet/movement): fleet slots, distance, duration, hydrogen, recall.
- [Missions](/en/fleet/missions): the ten missions and their rules.
- [Expeditions](/en/fleet/expeditions): deep space, its conditions and outcomes.
- [Jump gate](/en/fleet/jump-gate): instant jumps between your moons.
'''
write('fr', 'fleet', FR)
write('en', 'fleet', EN)
