# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FenouilMain.ui'
#
# Created: Sat May 23 18:14:35 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FenouilMain(object):
    def setupUi(self, FenouilMain):
        FenouilMain.setObjectName(_fromUtf8("FenouilMain"))
        FenouilMain.resize(800, 600)
        self.centralwidget = QtGui.QWidget(FenouilMain)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.imgDisplay = QtGui.QLabel(self.centralwidget)
        self.imgDisplay.setText(_fromUtf8(""))
        self.imgDisplay.setObjectName(_fromUtf8("imgDisplay"))
        self.horizontalLayout.addWidget(self.imgDisplay)
        FenouilMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(FenouilMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuProcess = QtGui.QMenu(self.menubar)
        self.menuProcess.setObjectName(_fromUtf8("menuProcess"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        FenouilMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(FenouilMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        FenouilMain.setStatusBar(self.statusbar)
        self.actionOpen_image_file = QtGui.QAction(FenouilMain)
        self.actionOpen_image_file.setObjectName(_fromUtf8("actionOpen_image_file"))
        self.actionOpen_meta_data_file = QtGui.QAction(FenouilMain)
        self.actionOpen_meta_data_file.setObjectName(_fromUtf8("actionOpen_meta_data_file"))
        self.actionQuit = QtGui.QAction(FenouilMain)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHelp = QtGui.QAction(FenouilMain)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(FenouilMain)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.action_Get_lake_pollution_index = QtGui.QAction(FenouilMain)
        self.action_Get_lake_pollution_index.setObjectName(_fromUtf8("action_Get_lake_pollution_index"))
        self.action_Register_new_lake = QtGui.QAction(FenouilMain)
        self.action_Register_new_lake.setObjectName(_fromUtf8("action_Register_new_lake"))
        self.menuFile.addAction(self.actionOpen_image_file)
        self.menuFile.addAction(self.actionOpen_meta_data_file)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuProcess.addAction(self.action_Get_lake_pollution_index)
        self.menuProcess.addAction(self.action_Register_new_lake)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(FenouilMain)
        QtCore.QMetaObject.connectSlotsByName(FenouilMain)

    def retranslateUi(self, FenouilMain):
        FenouilMain.setWindowTitle(_translate("FenouilMain", "Fenouil", None))
        self.menuFile.setTitle(_translate("FenouilMain", "&File", None))
        self.menuProcess.setTitle(_translate("FenouilMain", "&Process", None))
        self.menuHelp.setTitle(_translate("FenouilMain", "&?", None))
        self.actionOpen_image_file.setText(_translate("FenouilMain", "&Open image file", None))
        self.actionOpen_meta_data_file.setText(_translate("FenouilMain", "Open &meta-data file", None))
        self.actionQuit.setText(_translate("FenouilMain", "&Quit", None))
        self.actionHelp.setText(_translate("FenouilMain", "&Help", None))
        self.actionAbout.setText(_translate("FenouilMain", "&About", None))
        self.action_Get_lake_pollution_index.setText(_translate("FenouilMain", "&Get lake pollution index", None))
        self.action_Register_new_lake.setText(_translate("FenouilMain", "&Register new lake", None))

