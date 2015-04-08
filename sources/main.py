# -*- coding: utf-8 -*-

"""
__author__ = 'Somebody'

Création du main.
"""

import LectureCSV as lec
import coord_to_px
import px_to_coord

fichier = "lac.csv"

lacs = []
lecture = lec.LectureCSV(fichier)

lacs = lecture.importation()

print(lacs[0])
