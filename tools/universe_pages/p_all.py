"""Régénère toutes les pages de la rubrique Univers : python3 tools/universe_pages/p_all.py"""
import runpy, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
for name in ('p_index', 'p_universes', 'p_coordinates', 'p_galaxy', 'p_planets', 'p_colonization', 'p_abandon', 'p_moons'):
    sys.argv = [str(HERE / f'{name}.py'), str(HERE)]
    runpy.run_path(str(HERE / f'{name}.py'), run_name='__main__')
