# -*- coding: utf-8 -*- 

"""Stores functions and classes we could use for images computing
without taking in account actual pixels but working with matrix. Images will
probably only be treated as pixels arrays, so it will be easy to change.
"""
__author__ = 'Gabriel Augendre'
from osgeo import gdal
import Queue


def region_growing(matrix_alpha, beginning, threshold, matrix_red, matrix_green, matrix_blue):
    """Region growing algorithm adapted to our problem.

    :param matrix_alpha: 2D-array filled with alpha layer values.
    :param beginning: Start case coordinates.
    :param threshold: Below this value, a pixel is considered as part of a lake
    :return: A list of pixels belonging to the region.
    """
    if len(matrix_alpha) == 0 or len(matrix_alpha[0]) == 0:
        return None
    if beginning.vert >= len(matrix_alpha) or beginning.hor >= len(matrix_alpha[0]):
        return None
    if matrix_alpha[beginning.hor][beginning.vert] >= threshold:
        return None
    if (matrix_red[beginning.hor][beginning.vert] == 0 and matrix_green[beginning.hor][beginning.vert] == 0 and matrix_blue[beginning.hor][beginning.vert] == 0) or \
            (matrix_red[beginning.hor][beginning.vert] == 5 and matrix_green[beginning.hor][beginning.vert] == 3 and matrix_blue[beginning.hor][beginning.vert] == 3):
        return None

    returned_set = set()
    point_queue = Queue.Queue()

    point_queue.put(beginning)
    beginning.region = True
    returned_set.add(beginning)

    # i = 0
    # printed = False
    while not point_queue.empty():
        # if not printed and i % 1000 == 0:
        #     print i
        #     printed = True
        pixel = point_queue.get()
        neighbours = pixel.compute_neighbours(len(matrix_alpha), len(matrix_alpha[0]))
        for neighbour in neighbours:
            if not (neighbour in returned_set) and matrix_alpha[neighbour.hor][neighbour.vert] < threshold:
                point_queue.put(neighbour)
                returned_set.add(neighbour)
                neighbour.region = True
                # i += 1
                # printed = False

    return returned_set


def lakeAverageColor(path, beginning, threshold):
    """Prepares the data for region growing algorithm, and computes the average color of the lake.

    :param path: Path to image.
    :param beginning: Type = Pixel, Start case coordinates.
    :param threshold: Below this value, a pixel is considered as part of a lake
    :return: A pixel with the coordinates of the beginning pixel and the average color of the lake.
    """

    dataset = gdal.Open(path, gdal.GA_ReadOnly)
    RBand = dataset.GetRasterBand(1).ReadAsArray()
    GBand = dataset.GetRasterBand(2).ReadAsArray()
    BBand = dataset.GetRasterBand(3).ReadAsArray()
    ABand = dataset.GetRasterBand(4).ReadAsArray()

    region = region_growing(ABand, beginning, threshold, RBand, GBand, BBand)

    cptPix = 0
    sumR = 0
    sumG = 0
    sumB = 0
    sumA = 0

    if not region:
        return Pixel(beginning.hor, beginning.vert)
    else:
        for pixel in region:
            sumR += RBand[pixel.hor][pixel.vert]
            sumG += GBand[pixel.hor][pixel.vert]
            sumB += BBand[pixel.hor][pixel.vert]
            sumA += ABand[pixel.hor][pixel.vert]
            cptPix += 1

        # Par défaut on réalise une division entière => Troncature à l'entier inférieur.
        # On préfère réaliser une division décimale et arrondir à l'entier le plus proche.
        avgR = int(round(float(sumR) / cptPix))
        avgG = int(round(float(sumG) / cptPix))
        avgB = int(round(float(sumB) / cptPix))
        avgA = int(round(float(sumA) / cptPix))

        return Pixel(beginning.hor, beginning.vert, avgR, avgG, avgB, avgA)


class Pixel:
    """Class used to represent a pixel with two coordinates."""

    def __init__(self, hor, vert, red=-1, green=-1, blue=-1, alpha=-1):
        """Constructor

        :param vert: Vertical coordinate
        :param hor: Horizontal coordinate
        """
        self.hor = hor
        self.vert = vert
        self.region = False
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    def compute_neighbours(self, height, width):
        """Computes the list of neighbouring pixels.

        :return: A list containing all the neighbours of the considered pixel.
        """
        neighbours = set()
        if self.vert - 1 >= 0:
            neighbours.add(Pixel(self.hor, self.vert - 1))
            if self.hor - 1 >= 0:
                neighbours.add(Pixel(self.hor - 1, self.vert - 1))
            if self.hor + 1 < height:
                neighbours.add(Pixel(self.hor + 1, self.vert - 1))
        if self.vert + 1 < width:
            neighbours.add(Pixel(self.hor, self.vert + 1))
            if self.hor - 1 >= 0:
                neighbours.add(Pixel(self.hor - 1, self.vert + 1))
            if self.hor + 1 < height:
                neighbours.add(Pixel(self.hor + 1, self.vert + 1))

        if self.hor - 1 >= 0:
            neighbours.add(Pixel(self.hor - 1, self.vert))

        if self.hor + 1 < height:
            neighbours.add(Pixel(self.hor + 1, self.vert))

        return neighbours

    def __repr__(self):
        return "Pixel ({}, {}, R={}, G={}, B={}, alpha={})".format(self.vert, self.hor, self.red, self.green, self.blue,
                                                                   self.alpha)

    def __eq__(self, other):
        if other is None or not isinstance(other, Pixel):
            return False
        else:
            return self.hor == other.hor and self.vert == other.vert

    def __hash__(self):
        return hash((self.vert, self.hor))
