# -*- coding: utf-8 -*-


from PyQt5 import  QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure 
import numpy as np 
from array import array 
from datetime import datetime
from matplotlib.dates import  date2num, DayLocator, MinuteLocator, SecondLocator, DateFormatter, MicrosecondLocator
from matplotlib.ticker import MultipleLocator
import tushare as ts
 
X_MINUTES = 1 
INTERVAL = 1
 
class BaseShow(FigureCanvas): 
    def __init__(self): 
        self.fig = Figure() 
        self.ax = self.fig.add_subplot(111) 
        FigureCanvas.__init__(self, self.fig) 
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) 
        FigureCanvas.updateGeometry(self)

class  BaseWrapper(QtWidgets.QWidget): 
    def __init__(self , parent =None): 
        QtWidgets.QWidget.__init__(self, parent) 
        self.canvas = BaseShow() 
        self.vbl = QtWidgets.QVBoxLayout() 
        self.ntb = NavigationToolbar(self.canvas, parent) 
        self.vbl.addWidget(self.ntb) 
        self.vbl.addWidget(self.canvas) 
        self.setLayout(self.vbl)

 