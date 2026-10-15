"""Textes propres à chaque page de classe (FR et EN), vérifiés sur le code : un module t_<classe>.py par classe.

Chaque module définit FR et EN : brief, rules (règles après les trois règles communes), example, branch_notes
(précisions sous le tableau d'une branche, par clé de branche), caps_note, builds, pitfalls, related.
"""
import importlib

from dyn_lib import CLASSES

PROSE = {}
for _c in CLASSES:
    try:
        _m = importlib.import_module(f't_{_c}')
    except ModuleNotFoundError:
        continue
    PROSE[_c] = {'fr': _m.FR, 'en': _m.EN}
