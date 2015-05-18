# -*- coding: utf-8 -*- 
"""
Class Lac.py

Created by Somebody
Friday 3 April 2015
08/04/215 : renommage des variables selon la convention + desambiguation des noms de variables.

"""
import coord_manipulation as cm
import algo_matrix as am
import Brain.py

"""
class WrongNumberException(Exception):
    def __init__(self, valeur):
        self.valeur = valeur
        def __str__(self):
            return repr(self.value)
"""


class Lac:
    """
    Classe d'import et de stockage des données emmanant du .csv
    """
    compteur = 0
    def __init__(
            self, nom, code, latitude,
            longitude, surface, chloro_median, chloro_median_spring,
            chloro_first, chloro_second, chloro_third, fichier_Un, fichier_Deux, fichier_Trois):
        """
        :type self: object
        :param nom: Nom du lac
        :param code: Code 4 lettres du lac
        :param latitude: latitude du pixel du lac
        :param longitude: longitude du pixel du lac
        :param surface: surface du lac
        :param chloro_median: taux chlorophyll.a median
        :param chloro_median_spring: taux chlorophyll.a median au printemps
        :param chloro_irst: taux de chlorophyll.a à la première date
        :param chloro_second: taux de chlorophyll.a à la deuxième date
        :param chloro_third: taux de chlorophyll.a à la troisième date

        """
        self.nom = nom
        self.code = code
        self.latitude = latitude
        self.longitude = longitude
        self.surface = surface
        self.chloro_median = chloro_median
        self.chloro_median_spring = chloro_median_spring
        self.chloro_first = chloro_first
        self.chloro_second = chloro_second
        self.chloro_third = chloro_third

        self.fichier_Un = fichier_Un
        self.fichier_Deux = fichier_Deux
        self.fichier_Trois = fichier_Trois

        self.px_X, self.px_Y = cm.coord_to_px(self.longitude,
                                              self.latitude,
                                              self.fichier_Un)
        self.px_X2, self.px_Y2 = cm.coord_to_px(self.longitude,
                                                self.latitude,
                                                self.fichier_Deux)
        self.px_X3, self.px_Y3 = cm.coord_to_px(self.longitude,
                                                self.latitude,
                                                self.fichier_Trois)

        self.etat_Connu = 0

        if (self.chloro_median == 0.0):
            self.etat_Connu = 0
        else:
            self.etat_Connu = 1

        Lac.compteur += 1

    def afficheCoord(self):
        """
        Affiche les coordonnées des trois lacs.
        """
        pass

    def envoie_Croissance(self, px_X, px_Y):
        """
        Envoie les coordonnées en pixel du lac pour effectuer une croissance de région.
        """
        #pixel = am.Pixel(px_X,px_Y)
        #return am.
        pass

    def envoie_To_Nn(self):
        """
        Appel la classe NN (Neural Network)
        """
        Brain

