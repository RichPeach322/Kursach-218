# -*- coding: utf-8 -*-
import sys
import math 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib import style
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,QComboBox,QPushButton,QLineEdit,
    QAction, QFileDialog, QApplication,QMenu, QVBoxLayout, QSizePolicy, QMessageBox)
from PyQt5.QtGui import QIcon


class Fig(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        
        self.ys=[]
        self.xs=[]
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.plot()
 
    def plot(self):
        ax = self.figure.add_subplot(111)
        ax.plot(self.xs,self.ys, 'r-')
        ax.set_title('Your data')
        self.draw()
    def clear(self):
        ax = self.figure.add_subplot(111)
        self.xs=[]
        self.ys=[]
        ax.plot(self.xs,self.ys, 'r-')
        ax.set_title('Your data')
        self.draw()


class Window(QMainWindow) :

    def __init__(self, parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.graph = Fig()
        self.setCentralWidget(self.graph)
        self.statusBar()
        self.methtext = '0'
        self.functext = '0'

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        procmethod = QComboBox(self)
        procmethod.addItems([' ','Summation','Multiplication'])
        procmethod.move(50, 550)
        procmethod.activated[str].connect(self.methact)

        procfunction = QComboBox(self)
        procfunction.addItems([' ','Sin','Sinc'])
        procfunction.move(200, 550)
        procfunction.activated[str].connect(self.funcact)

        btn = QPushButton('Confirm',self)
        btn.move(350,550)
        btn.clicked.connect(self.btnclick)

        self.textbox = QLineEdit(self)
        self.textbox.move(450, 550)
        self.textbox.resize(100,40)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QComboBox')
        self.show()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Interface')
        self.show()      

    def btnclick(self):
        self.datastr = self.methtext + ' ' + self.functext
        self.textbox.setText(self.datastr)

    def methact(self, text):
        self.methtext = text

    def funcact(self, text):
        self.functext = text

    def showDialog(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]

        self.graph.clear()
        f = open(fname, 'r')
        data = f.readlines()
        for str in data:
            xbuf,ybuf=str.split(' ')
            self.graph.xs.append(xbuf)
            self.graph.ys.append(ybuf)
        self.graph.plot()

                    



app = QtWidgets.QApplication(sys.argv)
widget = Window()
widget.show()
sys.exit(app.exec_())
