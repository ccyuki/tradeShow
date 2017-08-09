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
 
class HistoryShow(FigureCanvas): 
    def __init__(self): 
        self.fig = Figure() 
        self.ax = self.fig.add_subplot(111) 
        FigureCanvas.__init__(self, self.fig) 
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) 
        FigureCanvas.updateGeometry(self) 
        self.ax.set_title("Get History Price")
        self.ax.set_xlabel("time(s)") 
        self.ax.set_ylabel('volume')         
        self.ax.legend(loc='best')  # 显示图例
        #self.ax.xaxis.set_major_locator(YearLocator())  # 时间间隔 every minute is a major locator 
        self.ax.xaxis.set_major_locator(DayLocator(interval=3))  # 时间间隔 every second is a major locator 
        #self.ax.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator 
        self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d') ) #tick label formatter 
        #self.ax.yaxis.set_major_locator(MultipleLocator(10))  # Y轴间隔10
        self.curveObj = None # draw object
        
    def getYtick(self, datay):
        t_avg = sum(datay)/len(datay)
        t_min = min(datay) - (t_avg-min(datay))
        t_max = max(datay) + (max(datay)-t_avg)
        return t_min, t_max
 
    def plot(self, datax, datay):
        if self.curveObj is None: 
            #create draw object once 
            self.curveObj = self.ax.plot_date(np.array(datax), np.array(datay),'ro-', label='volume')
        else: 
            #update data of draw object 
            self.curveObj[0].set_data(np.array(datax), np.array(datay))
            #update limit of X axis,to make sure it can move 
            if datax[0] != datax[-1]:
                if len(datax) < 31:
                    self.ax.set_xlim(datax[0],datax[-1])  # 设置x轴范围
                else:
                    self.ax.set_xlim(datax[-31],datax[-1])  # 只显示最后31笔
        minx,maxx = self.getYtick(datay)
        self.ax.set_ylim(minx,maxx)  # list max +/- 10 Y轴范围
        minx,maxx = self.getYtick(datay)
        ticklabels = self.ax.xaxis.get_ticklabels() 
        for tick in ticklabels: 
            tick.set_rotation(25)   # x轴标签旋转25°
        self.draw()
 
class  HistoryShowWrapper(QtWidgets.QWidget): 
    def __init__(self , parent =None): 
        QtWidgets.QWidget.__init__(self, parent) 
        self.canvas = HistoryShow() 
        self.vbl = QtWidgets.QVBoxLayout() 
        self.ntb = NavigationToolbar(self.canvas, parent) 
        self.vbl.addWidget(self.ntb) 
        self.vbl.addWidget(self.canvas) 
        self.setLayout(self.vbl) 
        self.dataX= [] 
        self.dataY= []
 
    def startPlot(self, code): 
        stockData = ts.get_k_data(code)
        volumeData = list(stockData.volume)
        timeData = list(stockData.date)
        self.dataX.extend(timeData) 
        self.dataY.extend(volumeData)
        print (self.dataX, self.dataY)
        self.canvas.plot(self.dataX, self.dataY)         
        
    def pausePlot(self): 
        pass
    
    def releasePlot(self):
        pass
 