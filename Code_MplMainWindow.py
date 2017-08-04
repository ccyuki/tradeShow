# -*- coding: utf-8 -*-

"""
    绑定按钮事件及中间逻辑。
"""

from PyQt5 import QtGui,QtCore, QtWidgets
from Ui_MplMainWindow import Ui_MainWindow
import sys

class Code_MainWindow(Ui_MainWindow):#修改为从Ui_MainWindow继承
    def __init__(self, parent = None):    
        super(Code_MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.startBtn.clicked.connect(self.startPlot)
        print ("Code_mainwindow...startBtn connect")
        #self.stopBtn.clicked.connect(self.stopPlot)
        
    def startPlot(self):
        self.mplCanvas.startPlot()
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