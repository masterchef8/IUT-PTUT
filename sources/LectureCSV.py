# coding=utf-8
"""

__author__ = 'Somebody'
__date__ = 05/04/2015

"""

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

    def creationClassLacs(self, lacs):
        """
        Fonction qui créé une un tableau d'objet de type Lac.
        :param lacs: prend un un tableau de lacs en argument
        """

        for i in lacs:
            print i
