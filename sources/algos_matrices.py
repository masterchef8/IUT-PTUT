"""
    Stocke les fonctions et classes dont on pourrait avoir besoin pour le traitement des images
    sans se préoccuper des pixels mais en travaillant avec des matrices (les images ne seront
    probablement que des tableaux de pixels, le traitement sera donc similaire).
"""
__author__ = 'gaugendre'


def croissance_region(matrice, depart):
    """
    :param matrice: Une matrice remplie de 0 ou 1 (couche alpha).
    :param depart: Les coordonnées de la case de départ.
    :return: Une liste de pixels correspondant à la région
    """
    if len(matrice) == 0 or len(matrice[0]) == 0:
        return None
    if depart.vert >= len(matrice) or depart.hor >= len(matrice[0]):
        return None
    if matrice[depart.vert][depart.hor] == 0:
        return None

    pixels_voisins = [depart]
    pixels_voisins.extend(depart.calculer_voisins(len(matrice), len(matrice[0])))
    ens_retour = set()
    ens_retour.add(depart)
    depart.region = True

    for p in pixels_voisins:
        if matrice[p.vert][p.hor] == 1 and p.region is False:
            ens_retour.add(p)
            p.region = True
            set(pixels_voisins).update(p.calculer_voisins(len(matrice), len(matrice[0])))

    return ens_retour


class Pixel:
    """
    Une classe qui représente un pixel avec deux coordonnées pour l'utiliser dans une matrice.
    """

    def __init__(self, vert, hor):
        """
        Constructeur
        :param hor: coordonnée horizontale
        :param vert: coordonnée verticale
        """
        self.hor = hor
        self.vert = vert
        self.region = False

    def calculer_voisins(self, tailleV, tailleH):
        """
        Retourne la liste des pixels voisins
        :return: la liste des pixels voisins
        """
        liste = set()
        if self.hor - 1 >= 0:
            if self.vert - 1 >= 0:
                liste.add(Pixel(self.vert - 1, self.hor - 1))
            if self.vert + 1 < tailleV:
                liste.add(Pixel(self.vert + 1, self.hor - 1))
            liste.add(Pixel(self.vert, self.hor - 1))
        if self.hor + 1 < tailleH:
            if self.vert - 1 >= 0:
                liste.add(Pixel(self.vert - 1, self.hor + 1))
            if self.vert + 1 < tailleV:
                liste.add(Pixel(self.vert + 1, self.hor + 1))
            liste.add(Pixel(self.vert, self.hor + 1))

        if self.vert - 1 >= 0:
            liste.add(Pixel(self.vert - 1, self.hor))
            liste.add(Pixel(self.vert + 1, self.hor))

        return liste

    def __repr__(self):
        return "Pixel ({}, {})".format(self.vert, self.hor)

    def __eq__(self, other):
        if other is None or type(other) is not Pixel:
            return False
        else:
            return self.vert == other.vert and self.hor == other.hor

    def __hash__(self):
        return hash((self.hor, self.vert))


if __name__ == "__main__":
    matrix = [[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
              [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
              [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]]
    region = croissance_region(matrix, Pixel(1, 1))
    print(region)

    print(Pixel(0, 0) == Pixel(0, 0))
    print(Pixel(0, 0) == Pixel(0, 1))