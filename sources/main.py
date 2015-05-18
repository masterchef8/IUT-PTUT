# -*- coding: utf-8 -*-

"""
__author__ = 'Somebody'

Création du main.
"""

import LectureCSV as lec
import coord_manipulation
import numpy as np


fichier = "lac.csv"
text = "lecture"
lacs = []
lecture = lec.LectureCSV(fichier)

lecture.creationClassLacs()


