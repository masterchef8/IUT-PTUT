__author__ = 'Somebody'

"""
Main de validation
"""



from sources.lectureXLS import LectureXLS
from sources.lac import Lac
from sources.algo_matrix import *
from sources.coord_manipulation import *

fichier_xls = '../Images_Calees_CONFIDENTIELLES/Dombes-Carto-CONFIDENTIELLE.xls'
liste_images = ['../Images_Calees_CONFIDENTIELLES/20070406/06042007caletif.tif',
                '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif',
                '../Images_Calees_CONFIDENTIELLES/20071001/tif10102007calee.tif'
                ]
liste_lacs = LectureXLS(fichier_xls).importation()

"""
for image in liste_images:
    for lac in liste_lacs:
        try:
            x, y = coord_to_px(lac.longitude, lac.latitude, image)
        except RuntimeError:
            pass
        finally:
            print "hello"
"""