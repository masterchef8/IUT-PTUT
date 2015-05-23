# -*- coding: utf-8 -*-
"""
hierarchie doit être :
Ptut
|-projetia
| |-sources
|   |-main_script_test.py
|-Images_Calees_CONFIDENTIELLES/
  |-Dombes-Carto-CONFIDENTIELLE.xls

"""

from lectureXLS import LectureXLS
from lac import Lac

fichier_xls = '../../Images_Calees_CONFIDENTIELLES/Dombes-Carto-CONFIDENTIELLE.xls'

liste_lacs = LectureXLS(fichier_xls).importation() # Maintenant, on a une belle liste de lacs avec leurs infos provenant du XLS.

for lac in liste_lacs:
    print lac
