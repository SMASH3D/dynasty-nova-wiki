import sys; sys.path.insert(0, sys.argv[1])
from esp_lib import *; from write import *


def body(lang):
    if lang == 'fr':
        return '''# Espionnage

**Sondes, rapports, vision partagée et phalange.**

## Pages de cette rubrique

- [Espionner](/fr/espionage/spying) : envoyer des Éclaireurs, niveau de détail, risque pour les sondes, vision partagée d'alliance.
- [Lire un rapport d'espionnage](/fr/espionage/spy-report) : les sections du rapport et l'alerte d'intrusion.
- [Phalange de capteur](/fr/espionage/sensor-phalanx) : observer les flottes depuis une lune.
'''
    return '''# Espionage

**Probes, reports, shared vision and the phalanx.**

## Pages in this section

- [Spying](/en/espionage/spying): sending Scouts, detail level, risk to the probes, shared alliance vision.
- [Reading a spy report](/en/espionage/spy-report): the report sections and the intrusion alert.
- [Sensor phalanx](/en/espionage/sensor-phalanx): watching fleets from a moon.
'''


for lang in ('fr', 'en'):
    write(lang, 'espionage', body(lang),
          description='Sondes, rapports, vision partagée et phalange.' if lang == 'fr'
          else 'Probes, reports, shared vision and the phalanx.')
