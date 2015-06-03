# -*- coding: utf-8 -*-
"""
hierarchie doit être :
Ptut
|-projetia
  |-sources
  |   |-main_script_test.py
  |-Images_Calees_CONFIDENTIELLES/
  |-Dombes-Carto-CONFIDENTIELLE.xls

"""

from lectureXLS import LectureXLS
from lac import Lac
from algo_matrix import *
from coord_manipulation import *
import csv
import pylab as pl
from brain import *
from brainBis import *
fichier_xls = '../Images_Calees_CONFIDENTIELLES/Dombes-Carto-CONFIDENTIELLE.xls'
liste_images = [
    '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif',
    '../Images_Calees_CONFIDENTIELLES/20071001/01102007bilicale.tif'
]
liste_lacs = LectureXLS(
    fichier_xls).importation()  # Maintenant, on a une belle liste de lacs avec leurs infos provenant du XLS.
i = 0
inputs = csv.writer(open("inputs.csv", "wb"))
desired = csv.writer(open("desired.csv", "wb"))

mDesired = []
mPixelColor = []

print "nom_image,lac.nom,lac.chloro_first,lac.chloro_second,lac.chloro_third,pixel.red,pixel.green,pixel.blue"
for image in liste_images:
    for lac in liste_lacs:
        x, y = coord_to_px(lac.longitude, lac.latitude, image)
        print image
        # chaine = str(image) + ";"
        #chaine += str(lac.nom) + ";"

        pixel = lakeAverageColor(image, Pixel(y, x), 50)

        chloroValue = 0.0

        if pixel.red == -1:
            print "nope !"
        else:
            if image == '../Images_Calees_CONFIDENTIELLES/20070805/050807caletif.tif':
                chaine2 = str(lac.chloro_second)
                try:
                    chloroValue = float(lac.chloro_second)
                except Exception:
                    continue
            else:
                chaine2 = str(lac.chloro_third)
                try:
                    chloroValue = float(lac.chloro_third)
                except Exception:
                    continue

            red = str(pixel.red)
            green = str(pixel.green)
            blue = str(pixel.blue)
            i += 1
            print chaine2
            print i
            inputs.writerow([red + ";" + green + ";" + blue])
            desired.writerow([chaine2])

            redBinary = format(pixel.red, '08b')
            greenBinary = format(pixel.green, '08b')
            blueBinary = format(pixel.blue, '08b')
            temp = []
            for i in range(0, 8):
                temp.append(int(redBinary[i]))
            for i in range(0, 8):
                temp.append(int(greenBinary[i]))
            for i in range(0, 8):
                temp.append(int(blueBinary[i]))

            mPixelColor.append(temp)
            mDesired.append(chloroValue)

print len(mPixelColor[0])
print len(mDesired)
inputLayerSize = len(mPixelColor[0])
hiddenLayerSize = 5
outputLayerSize = 1
step = 0.5
momentum = 0.1
iterations = 6000

brain = Brain(inputLayerSize, hiddenLayerSize, outputLayerSize, step, momentum, iterations)

mErrorTesting = brain.training(mPixelColor, mDesired)

pl.plot(mErrorTesting, 'r', label='error during training', lw=1)
pl.title('errors/iterations')
pl.legend()
pl.show()
