# -*- coding: utf-8 -*-

from PyQt5 import  QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure 
import numpy as np 
from array import array 
import time
import random
import threading
from datetime import datetime
from matplotlib.dates import  date2num, MinuteLocator, SecondLocator, DateFormatter, MicrosecondLocator
from matplotlib.ticker import MultipleLocator
import tushare as ts
 
X_MINUTES = 1 
INTERVAL = 1
 
MAXCOUNTER = int(X_MINUTES * 60/ INTERVAL)
 
class MplCanvas(FigureCanvas): 
    def __init__(self): 
        self.fig = Figure() 
        self.ax = self.fig.add_subplot(111) 
        FigureCanvas.__init__(self, self.fig) 
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding) 
        FigureCanvas.updateGeometry(self) 
        self.ax.set_title("Get Real Price")
        self.ax.set_xlabel("time(s)") 
        self.ax.set_ylabel('price(RMB)') 
        self.ax.legend(loc='best')  # 显示图例
        #self.ax.xaxis.set_major_locator(MinuteLocator())  # 时间间隔 every minute is a major locator 
        self.ax.xaxis.set_major_locator(SecondLocator(interval=3))  # 时间间隔 every second is a major locator 
        #self.ax.xaxis.set_minor_locator(SecondLocator([10,20,30,40,50])) # every 10 second is a minor locator 
        self.ax.xaxis.set_major_formatter( DateFormatter('%Y-%m-%d %H:%M:%S') ) #tick label formatter 
        self.ax.yaxis.set_major_locator(MultipleLocator(10))  # Y轴间隔10
        self.curveObj = None # draw object
 
    def plot(self, datax, datay):
        if self.curveObj is None: 
            #create draw object once 
            self.curveObj = self.ax.plot_date(np.array(datax), np.array(datay['price']),'bo-', label='price')
            self.curveObj.extend(self.ax.plot_date(np.array(datax), np.array(datay['a2_p']),'g*-', label='a2_p'))
        else: 
            #update data of draw object 
            self.curveObj[0].set_data(np.array(datax), np.array(datay['price']))
            self.curveObj[1].set_data(np.array(datax), np.array(datay['a2_p']))
            #update limit of X axis,to make sure it can move 
            if datax[0] != datax[-1]:
                if len(datax) < 20:
                    self.ax.set_xlim(datax[0],datax[-1])  # 设置x轴范围
                else:
                    self.ax.set_xlim(datax[-20],datax[-1])  # 只显示最后20笔
        self.ax.set_ylim(min(datay['price'])-10,max(datay['price'])+10)  # list max +/- 10 Y轴范围
        ticklabels = self.ax.xaxis.get_ticklabels() 
        for tick in ticklabels: 
            tick.set_rotation(25)   # x轴标签旋转25°
        self.draw()
 
class  MplCanvasWrapper(QtWidgets.QWidget): 
    def __init__(self , parent =None): 
        QtWidgets.QWidget.__init__(self, parent) 
        self.canvas = MplCanvas() 
        self.vbl = QtWidgets.QVBoxLayout() 
        self.ntb = NavigationToolbar(self.canvas, parent) 
        self.vbl.addWidget(self.ntb) 
        self.vbl.addWidget(self.canvas) 
        self.setLayout(self.vbl) 
        self.dataX= [] 
        self.dataY= {'price':[], 'a2_p':[]}
        self.initDataGenerator()
 
    def startPlot(self): 
        self.__generating = True
 
    def pausePlot(self): 
        self.__generating = False
        pass
 
    def initDataGenerator(self):
        self.__generating=False 
        self.__exit = False 
        self.tData = threading.Thread(name = "dataGenerator",target = self.generateData) 
        self.tData.start()        
 
    def releasePlot(self): 
        self.__exit  = True 
        self.tData.join()
 
    def generateData(self):
        counter=0 
        while(True): 
            if self.__exit: 
                print ("exit.....")
                break 
            if self.__generating:
                #stockData = ts.get_realtime_quotes('000581')
                #if stockData is None:
                #    continue
                #newDataPrice = stockData.price[0]
                #newDataA2_p  = stockData.a2_p[0]
                #newTime = stockData.date[0]+" "+stockData.time[0]
                newDataPrice = random.randint(1, 100) 
                newDataA2_p  = random.randint(1, 100) 
                newTime= date2num(datetime.now()) 
                self.dataX.append(newTime) 
                self.dataY['price'].append(newDataPrice)
                self.dataY['a2_p'].append(newDataA2_p) 
                print (self.dataX, self.dataY)
                self.canvas.plot(self.dataX, self.dataY)                 
                if counter >= MAXCOUNTER: 
                    self.dataX.pop(0) 
                    self.dataY['price'].pop(0)
                    self.dataY['a2_p'].pop(0)
                else: 
                    counter+=1 
            time.sleep(INTERVAL)