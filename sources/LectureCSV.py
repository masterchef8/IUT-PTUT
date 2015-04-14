# -*- coding: utf-8 -*-

__author__ = 'Somebody'
__date__ = 05 / 04 / 2015

import csv
import Lac

#
# Ouverture du fichier source.
#
# le mode ''b'' est
# obligatoire sur les plate-formes où il est
# significatif. Dans la pratique, il est conseillé
# de toujours le mettre.
#


class LectureCSV:
    def __init__(self, fichier):
        """
        :param fichier: le nom du fichier csv à importer
        """
        self.fichier = fichier

        self.fichier_Un = "../Images_Calees_CONFIDENTIELLES/20070406/06042007caletif.tif"
        self.fichier_Deux = "../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif"
        self.fichier_Trois = "../Images_Calees_CONFIDENTIELLES/20071001/tif10102007calee.tif"


    def importation(self):

        """
        :param fichier: le nom du fichier csv à importer
        :return une liste de lac de tuples qui correspond aux différentes infos sur les lacs.

        """
        try:
            with open(self.fichier, 'rb') as f:
                reader = csv.reader(f, delimiter=';')
                lacs = []

                for row in reader:
                    lac = row
                    lacs.append(lac)

        finally:
            f.close()
        return lacs

    def creationClassLacs(self):
        """
        Fonction qui créé une un tableau d'objet de type Lac.
        :param lacs: prend un un tableau de lacs en argument
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

