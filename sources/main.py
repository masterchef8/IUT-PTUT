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
liste_images = [
                '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif',
                '../Images_Calees_CONFIDENTIELLES/20071001/01102007bilicale.tif'
                ]
liste_lacs = LectureXLS(fichier_xls).importation()  # Maintenant, on a une belle liste de lacs avec leurs infos provenant du XLS.
i = 0
print "nom_image,lac.nom,lac.chloro_first,lac.chloro_second,lac.chloro_third,pixel.red,pixel.green,pixel.blue"
for image in liste_images:
    for lac in liste_lacs:
        x, y = coord_to_px(lac.longitude, lac.latitude, image)
        chaine = str(image) + ","
        chaine += str(lac.nom) + ","
        chaine += str(lac.chloro_first) + ","
        chaine += str(lac.chloro_second) + ","
        chaine += str(lac.chloro_third) + ","
        pixel = lakeAverageColor(image, Pixel(y, x), 50)
        chaine += str(pixel.red) + ","
        chaine += str(pixel.green) + ","
        chaine += str(pixel.blue)
        print chaine
