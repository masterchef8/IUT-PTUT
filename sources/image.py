# -*- coding: utf-8 -*-
from algo_matrix import Pixel

__author__ = 'adrien'

'''from PIL import Image
im = Image.open('a_image.tif')
im.show()
import numpy
imarray = numpy.array(im)
for line in imarray:
    for pix in line:
        pix += 30
immod = Image.fromarray(imarray)
immod.show()'''

from osgeo import gdal
import numpy
from PIL import Image

path = "/home/adrien/Documents/IUT/ptut/Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif"
#im = Image.open(path)
#im.show()
dataset = gdal.Open(path, gdal.GA_ReadOnly)
globalArray = numpy.empty([4])
RBand = dataset.GetRasterBand(1).ReadAsArray()
GBand = dataset.GetRasterBand(2).ReadAsArray()
BBand = dataset.GetRasterBand(3).ReadAsArray()
ABand = dataset.GetRasterBand(4).ReadAsArray()
'''for x in xrange(1, dataset.RasterCount + 1):
    band = dataset.GetRasterBand(x)
    array = band.ReadAsArray()
    globalArray[x] = array'''

nbLignes =  RBand.shape[0]
nbColonnes = RBand.shape[1]

tableau = numpy.empty([nbLignes, nbColonnes], dtype=object)
for i in range(0, nbLignes - 1):
    for j in range(0, nbColonnes - 1):
        tableau[i][j] = Pixel(i, j, RBand[i][j], GBand[i][j], BBand[i][j], ABand[i][j])
print tableau