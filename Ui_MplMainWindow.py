# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MplMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from baseWrapper import BaseWrapper

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.funcComboBox = QtWidgets.QComboBox()
        self.funcComboBox.insertItem(0, self.tr("实时行情"))
        self.funcComboBox.insertItem(1, self.tr("历史行情"))
        self.horizontalLayout.addWidget(self.funcComboBox)
        self.codeLabel = QtWidgets.QLabel('Stock Code:')
        self.codeLineEdit = QtWidgets.QLineEdit("399300")
        self.horizontalLayout.addWidget(self.codeLabel)
        self.horizontalLayout.addWidget(self.codeLineEdit)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.mplCanvas = BaseWrapper(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName("mplCanvas")
        self.gridLayout.addWidget(self.mplCanvas, 1, 0, 1, 1)
        self.centralwidget.setLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TradeInfoShow"))
        self.startBtn.setText(_translate("MainWindow", "start"))
        self.stopBtn.setText(_translate("MainWindow", "stop"))


