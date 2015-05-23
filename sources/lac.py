# -*- coding: utf-8 -*- 
"""
Class lac.py

Created by Somebody
Friday 3 April 2015
08/04/215 : renommage des variables selon la convention + desambiguation des noms de variables.

"""

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
            chloro_first, chloro_second, chloro_third):
        """
        :param nom: Nom du lac
        :param code: Code 4 lettres du lac
        :param latitude: latitude du pixel du lac
        :param longitude: longitude du pixel du lac
        :param surface: surface du lac
        :param chloro_median: taux chlorophyll.a median
        :param chloro_median_spring: taux chlorophyll.a median au printemps
        :param chloro_first: taux de chlorophyll.a à la première date
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

        Lac.compteur += 1


    def __repr__(self):
        return "nom=" + self.nom + ", lat=" + str(self.latitude) + ", long=" + str(self.longitude)

