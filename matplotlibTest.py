# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:04:30 2017

@author: Harvey
"""

import matplotlib.pyplot as plt
import numpy as np

# 简单的绘图
x = np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.cos(x), 'r-o') # (x,y)
plt.plot(x, np.sin(x), 'g^') # 如果没有第一个参数 x，图形的 x 坐标默认为数组的索引
plt.show() # 显示图形