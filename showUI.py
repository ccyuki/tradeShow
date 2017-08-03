"""*************************************************************************                                                                                                                           
    > File Name: te.py                                                          
    > Copyright 2014 BONC, Inc.                                                 
    > Author: Harvey                                                            
    > Mail: ccyuki@qq.com•                                                
    > Created Time: Thu 03 Aug 2017 06:57:42 AM UTC                             
 ************************************************************************"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget,QApplication,QPushButton,QTextEdit,
                             QVBoxLayout)

# 自定义的窗口类
class TestWindow(QWidget):
    # 窗口初始化
    def __init__(self, parent = None):
        super(TestWindow, self).__init__(parent)
        self.setWindowTitle(u'TradeShow')

        # 创建按钮
        self.pushButton = QPushButton(u'Say Hello')

        # 创建文本框
        self.textEdit = QTextEdit()

        # 创建垂直布局
        layout = QVBoxLayout()

        # 将控件添加到布局中
        layout.addWidget(self.textEdit)
        layout.addWidget(self.pushButton)

        # 设置窗口布局
        self.setLayout(layout)

        # 设置按钮单击动作
        self.pushButton.clicked.connect(self.sayHello)

    # 按钮动作处理
    def sayHello(self):
        self.textEdit.setText('Hello World!')

# 程序主入口
if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = TestWindow()
    mainWindow.show()
    sys.exit(app.exec_())