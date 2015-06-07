#!/usr/bin/python
# coding=utf-8

# Dépendances IHM
from PyQt4 import QtGui, QtCore

# Librairies système
import sys

# Fenêtre principale
import MainUI


class FenouilMainWindow(QtGui.QMainWindow, MainUI.Ui_FenouilMain):

    # Initialisation de la classe fenêtre principale
    def __init__(self, parent=None):
        super(FenouilMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        self.center()

    # Définition des connecteurs d'action des widgets
    def connectActions(self):
        # File > Quit
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        # File > Open image file
        self.actionOpenImageFile.triggered.connect(lambda: self.openImage())

    # Ouverture d'un fichier image
    def openImage(self):
        # Fenêtre de choix de fichier, stockage du chemin résultant
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Ouvrir un fichier d'image",
                        QtCore.QDir.homePath(),
                        "Fichiers d'image (*)"
                    )
        # Chemin défini
        if fileName:
            # Conversion du fichier image en carte de pixels
            myPixmap = QtGui.QPixmap(fileName)
            # Redimensionnement à la taille de la zone d'affichage
            myScaledPixmap = myPixmap.scaled(self.imgDisplay.size(), QtCore.Qt.KeepAspectRatio)
            # Affichage dans la zone
            self.imgDisplay.setPixmap(myScaledPixmap)
            self.imgDisplay.setHidden(False)

    # Afficher la fenêtre
    def main(self):
        self.show()

    # Centrer la fenêtre
    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

# Appelé au lancement du fichier par l'interpréteur
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    fenouilMain = FenouilMainWindow()
    fenouilMain.main()
    app.exec_()
