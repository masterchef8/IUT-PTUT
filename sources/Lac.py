# -*- coding: utf-8 -*- 
"""
Class Lac.py

Created by Somebody
Friday 3 April 2015
08/04/215 : renommage des variables selon la convention + desambiguation des noms de variables.

"""



class Lac:
    """
    Classe d'import et de stockage des données emmanant du .csv
    """
    compteur = 0 # Nombre d'instances de Lac (membre static en Java).

    def __init__(self, nom, code, latitude, longitude, surface, chloro_median, chloro_med_spring, chloro_first, chloro_second, chloro_third, px_X, px_Y, num_lac):
        """
        :type self: object
        :param nom: Nom du lac
        :param code: Code 4 lettres du lac
        :param latitude: latitude du pixel du lac
        :param longitude: longitude du pixel du lac
        :param surface: surface du lac
        :param chloro_median: taux chlorophyll.a median
        :param chloro_med_spring: taux chlorophyll.a median au rpintemps
        :param chloro_first: taux de chlorophyll.a à la première date
        :param chloro_second: taux de chlorophyll.a à la deuxième date
        :param chloro_third: taux de chlorophyll.a à la troisième date
        :param px_X: pixel x
        :param px_Y: pixel y
        :param num_lac: Cette variable est destinée à eviter de définir des objets lac qui n'ont pas à exister
        """
        self.nom = nom
        self.code = code
        self.latitude = latitude
        self.longitude = longitude
        self.surface = surface
        self.chloro_median = chloro_median
        self.chloro_med_spring = chloro_med_spring
        self.chloro_first = chloro_first
        self.chloro_second = chloro_second
        self.chloro_third = chloro_third
        self.px_X = px_X
        self.px_Y = px_Y
        self.num_lac = num_lac

        Lac.compteur += 1
        if Lac.compteur > numLac:
            raise WrongNumberExeption