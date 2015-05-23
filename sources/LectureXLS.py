# coding=utf-8
"""

__author__ = 'Somebody'
__date__ = 05/04/2015
10/04/2015 : utilisation de la lib xlrd
    addresse : https://pypi.python.org/pypi/xlrd
    package : https://pypi.python.org/packages/source/x/xlrd/xlrd-0.9.3.tar.gz
    install : python setup.py install


"""

import xlrd
import Lac

#
# Ouverture du fichier source.
#
# le mode ''b'' est
# obligatoire sur les plate-formes où il est
# significatif. Dans la pratique, il est conseillé
# de toujours le mettre.
#


class LectureXLS:
    def __init__(self, fichier):
        """
        :param fichier: le nom du fichier xls à importer
        """
        self.fichier = fichier

        self.fichier_Un = '../Images_Calees_CONFIDENTIELLES/20070406/06042007caletif.tif'
        self.fichier_Deux = '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif'
        self.fichier_Trois = '../Images_Calees_CONFIDENTIELLES/20071001/tif10102007calee.tif'
        self.lacs = []

    def importation(self):
        #Faudrait gerer les erreurs mosieur !

        with xlrd.open_workbook(self.fichier) as classeur:
            page = classeur.sheet_by_index(0) #Feuille 1 du classeur
            for ligne in range(page.nrows):
                if(ligne == 0):
                    pass  #la première ligne est celle avec les en-têtes de colonnes

                #Ce gros bloc est à clean il faut juste trouver le
                #moyen de faire une boucle, une list comprehension
                #ou autre, sachant qu'on utilise pas la colonne 3
                #à voir, à refléchir. De plus les valeurs sont
                #hardcoded ... bof hein :)
                self.lacs.append(Lac.Lac(
                    page.cell_value(ligne, 0), #nom
                    page.cell_value(ligne, 1), #code
                    page.cell_value(ligne, 3), #latitude
                    page.cell_value(ligne, 4), #longitude
                    page.cell_value(ligne, 5), #surface
                    page.cell_value(ligne, 6), #chloro_median
                    page.cell_value(ligne, 7), #chloro_median_spring
                    page.cell_value(ligne, 8), #chloro_first
                    page.cell_value(ligne, 9), #chloro_second
                    page.cell_value(ligne, 10), #chloro_third
                    0,
                    0,
                    ligne
                ))
            return self.lacs

    def creationClassLacs(self):
        """
        Fonction qui créé une un tableau d'objet de type Lac.
        """
        tabLacs = []
        lacs = self.importation()
        for i, elt in enumerate(lacs):
            print lacs[i][0]
            tabLacs[i] = Lac.Lac(lacs[i][0], lacs[i][1], lacs[i][3],
                                 lacs[i][4], lacs[i][5], lacs[i][6],
                                 lacs[i][7], lacs[i][8], lacs[i][9],
                                 lacs[i][10], self.fichier_Un, self.fichier_Deux,
                                 self.fichier_Trois)

