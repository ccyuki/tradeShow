# -*- coding: utf-8 -*-

"""
    绑定按钮事件及中间逻辑。
"""

from PyQt5 import QtGui,QtCore, QtWidgets
from Ui_MplMainWindow import Ui_MainWindow
from mplCanvasWrapper import MplCanvasWrapper
from historyShowWrapper import HistoryShowWrapper
import sys

class Code_MainWindow(Ui_MainWindow):#修改为从Ui_MainWindow继承
    def __init__(self, parent = None):    
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.startBtn.clicked.connect(self.startPlot)
        self.stopBtn.clicked.connect(self.stopPlot)
        
    def startPlot(self):
        self.func = self.funcComboBox.currentIndex()
        if self.func is 0:
            self.mplCanvas = MplCanvasWrapper(self.centralwidget)
        elif self.func is 1:
            self.mplCanvas = HistoryShowWrapper(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mplCanvas.sizePolicy().hasHeightForWidth())
        self.mplCanvas.setSizePolicy(sizePolicy)
        self.mplCanvas.setObjectName("mplCanvas")
        self.gridLayout.addWidget(self.mplCanvas, 1, 0, 1, 1)
        
        code = self.codeLineEdit.text()
        self.mplCanvas.startPlot(code)
        pass
    
    def stopPlot(self):
        ''' pause plot '''
        self.mplCanvas.pausePlot()
        pass
    
    def releasePlot(self):
        ''' stop and release thread'''
        self.mplCanvas.releasePlot()
        
    def closeEvent(self,event):
        result =QtWidgets.QMessageBox.question(self,
                                           "Confirm Exit...",
                                           "Are you sure you want to exit ?",
                                           QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        event.ignore()
        if result ==QtWidgets.QMessageBox.Yes:
            self.releasePlot()#release thread's resouce
        event.accept()
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)     
    ui = Code_MainWindow()     
    ui.show()     
    sys.exit(app.exec_())