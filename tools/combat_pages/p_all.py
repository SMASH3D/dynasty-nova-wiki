"""Regénère les huit pages de la rubrique Combat, FR et EN : python3 tools/combat_pages/p_all.py tools/combat_pages"""
import sys
sys.path.insert(0, sys.argv[1] if len(sys.argv) > 1 else '.')
import p_index, p_how, p_report, p_plunder, p_debris, p_rebuild, p_sim, p_moon
for page in (p_index, p_how, p_report, p_plunder, p_debris, p_rebuild, p_sim, p_moon):
    page.run()
