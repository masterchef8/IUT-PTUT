# -*- coding: utf-8 -*-
"""
hierarchie doit être :
Ptut
|-projetia
  |-sources
  |   |-main_script_test.py
  |-Images_Calees_CONFIDENTIELLES/
  |-Dombes-Carto-CONFIDENTIELLE.xls

"""

from lectureXLS import LectureXLS
from lac import Lac
from algo_matrix import *
from coord_manipulation import *

fichier_xls = '../Images_Calees_CONFIDENTIELLES/Dombes-Carto-CONFIDENTIELLE.xls'
liste_images = ['../Images_Calees_CONFIDENTIELLES/20070406/06042007caletif.tif',
                '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif',
                '../Images_Calees_CONFIDENTIELLES/20071001/tif10102007calee.tif'
                ]
liste_lacs = LectureXLS(fichier_xls).importation() # Maintenant, on a une belle liste de lacs avec leurs infos provenant du XLS.

for image in liste_images:
    for lac in liste_lacs:
        try:
            x, y = coord_to_px(lac.longitude, lac.latitude, image)
        except RuntimeError:
            pass
        finally:
            print "hello"
