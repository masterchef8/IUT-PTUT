# -*- coding: utf-8 -*- 

"""Stores functions and classes we could use for images computing
without taking in account actual pixels but working with matrix. Images will
probably only be treated as pixels arrays, so it will be easy to change.
"""
__author__ = 'Gabriel Augendre'
from osgeo import gdal
import numpy

def region_growing(matrix, beginning, threshold):
    """Region growing algorithm adapted to our problem.

    :param matrix: 2D-array filled with alpha layer values.
    :param beginning: Start case coordinates.
    :param threshold: Below this value, a pixel is considered as part of a lake
    :return: A list of pixels belonging to the region.
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    if beginning.vert >= len(matrix) or beginning.hor >= len(matrix[0]):
        return None
    if matrix[beginning.vert][beginning.hor] >= threshold:
        return None

    neighbouring_pixels = [beginning]
    neighbouring_pixels.extend(
        beginning.compute_neighbours(len(matrix), len(matrix[0])))
    returned_set = set()
    returned_set.add(beginning)
    beginning.region = True

    for pixel in neighbouring_pixels:
        if matrix[pixel.vert][pixel.hor] < threshold and not pixel.region:
            returned_set.add(pixel)
            pixel.region = True
            set(neighbouring_pixels).update(
                pixel.compute_neighbours(len(matrix), len(matrix[0])))

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

    region = region_growing(ABand, beginning, threshold)

    cptPix = 0
    sumR = 0
    sumG = 0
    sumB = 0
    sumA = 0

    print Pixel(beginning.vert, beginning.hor, RBand[beginning.vert][beginning.hor],
                GBand[beginning.vert][beginning.hor], BBand[beginning.vert][beginning.hor],
                ABand[beginning.vert][beginning.hor])
    print "Taille de la region : ", len(region)
    print "Region :"
    print region

    for pixel in region:
        sumR += RBand[pixel.vert][pixel.hor]
        sumG += GBand[pixel.vert][pixel.hor]
        sumB += BBand[pixel.vert][pixel.hor]
        sumA += ABand[pixel.vert][pixel.hor]
        cptPix += 1
    avgR = sumR / cptPix
    avgG = sumG / cptPix
    avgB = sumB / cptPix
    avgA = sumA / cptPix

    return Pixel(beginning.vert, beginning.hor, avgR, avgG, avgB, avgA)


class Pixel:
    """Class used to represent a pixel with two coordinates."""
    def __init__(self, vert, hor, red=-1, green=-1, blue=-1, alpha=-1):
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
        if self.hor - 1 >= 0:
            if self.vert - 1 >= 0:
                neighbours.add(Pixel(self.vert - 1, self.hor - 1))
            if self.vert + 1 < height:
                neighbours.add(Pixel(self.vert + 1, self.hor - 1))
            neighbours.add(Pixel(self.vert, self.hor - 1))
        if self.hor + 1 < width:
            if self.vert - 1 >= 0:
                neighbours.add(Pixel(self.vert - 1, self.hor + 1))
            if self.vert + 1 < height:
                neighbours.add(Pixel(self.vert + 1, self.hor + 1))
            neighbours.add(Pixel(self.vert, self.hor + 1))

        if self.vert - 1 >= 0:
            neighbours.add(Pixel(self.vert - 1, self.hor))
            neighbours.add(Pixel(self.vert + 1, self.hor))

        return neighbours

    def __repr__(self):
        return "Pixel ({}, {}, R={}, G={}, B={}, alpha={})".format(self.vert, self.hor, self.red, self.green, self.blue, self.alpha)

    def __eq__(self, other):
        if other is None or not isinstance(other, Pixel):
            return False
        else:
            return self.vert == other.vert and self.hor == other.hor

    def __hash__(self):
        return hash((self.hor, self.vert))


