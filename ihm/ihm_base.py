#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

import FenouilMainUI


class FenouilMainWindow(QtGui.QMainWindow, FenouilMainUI.Ui_FenouilMain):
    def __init__(self, parent=None):
        super(FenouilMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        #self.center()

    def connectActions(self):
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
        self.actionOpenImageFile.triggered.connect(lambda: self.openImage())

    def openImage(self):
        fileName = QtGui.QFileDialog.getOpenFileName(
                        self,
                        "Ouvrir un fichier d'image",
                        QtCore.QDir.homePath(),
                        "Fichiers d'image (*)"
                    )
        if fileName:
            myPixmap = QtGui.QPixmap(fileName)
            myScaledPixmap = myPixmap.scaled(self.imgDisplay.size(), QtCore.Qt.KeepAspectRatio)
            self.imgDisplay.setPixmap(myScaledPixmap)
            self.imgDisplay.setHidden(False)
 
    def main(self):
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    fenouilMain = FenouilMainWindow()
    fenouilMain.main()
    app.exec_()
