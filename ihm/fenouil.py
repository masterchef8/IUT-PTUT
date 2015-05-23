#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys
import FenouilMain
 
class FenouilMain(QtGui.QMainWindow, FenouilMain.Ui_FenouilMain):
    def __init__(self, parent=None):
        super(FenouilMain, self).__init__(parent)
        self.setupUi(self)
        self.center()
        self.connectActions()

    def connectActions(self):
        self.actionQuit.triggered.connect(QtGui.qApp.quit)
 
    def main(self):
        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    fenouilMain = FenouilMain()
    fenouilMain.main()
    app.exec_()
