# -*- coding: utf-8 -*- 
"""
Class Lac.py

Created by Somebody
Friday 3 April 2015

"""



class Lac:
    """
    Classe d'import et de stockage des données emmanant du .csv
    """
    compteur = 0 # Nombre d'instance de Lac.

    def __init__(self, nom, code, lat, long, m2, chloMedian, chloMedSpring, chloFirst, chloSecond, chloThird, pxX, pxY, numLac,):
        """
        :type self: object
        :param nom: Nom du lac
        :param code: Code 4 lettres du lac
        :param lat: latitude du pixel du lac
        :param long: longitude du pixel du lac
        :param m2: surface du lac
        :param chloMedian: taux chlorophyll.a median
        :param chloMedSpring: taux chlorophyll.a median au printemps
        :param chloFirst: taux de chlorophyll.a à la première date
        :param chloSecond: taux de chlorophyll.a à la deuxième date
        :param chloThird: taux de chlorophyll.a à la troisième date
        :param pxX: pixel
        :param numLac: Cette variable est destinée à eviter de définir des objets lac qui n'ont pas à exister
        """
        self.nom = nom, self.code = code, self.lat = lat, self.long = long, self.m2 = m2
        self.chloMedian = chloMedian, self.chloMedSpring = chloMedSpring, self.chloFirst = chloFirst
        self.chloSecond = chloSecond, self.chloThird = chloThird, self.pxX = pxX
        self.pxY = pxY, self.numLac = numLac

        Lac.compteur += 1
        if Lac.compteur > numLac:
            raise wrongNumberExeptions