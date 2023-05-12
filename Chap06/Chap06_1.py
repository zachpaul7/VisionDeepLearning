# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 15:39:44 2023

@author: zachp
"""

from PyQt5.QtWidgets import *
import sys
import winsound

class BeepSound(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("소리 내기")
        self.setGeometry(200, 200, 500, 100)
        
        shortBeepButton = QPushButton('또롱', self)
        longBeepButton = QPushButton('삐익', self)
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다.',self)
        
        shortBeepButton.setGeometry(10, 10, 100, 30)
        longBeepButton.setGeometry(110, 10, 100, 30)
        quitButton.setGeometry(210, 10, 100, 30)
        self.label.setGeometry(10, 40, 500, 70)
        
        shortBeepButton.clicked.connect(self.shortBeepFunction)
        longBeepButton.clicked.connect(self.longBeepFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def shortBeepFunction(self):
        self.label.setText('또롱')
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
        
    def longBeepFunction(self):
        self.label.setText('주파수 1000으로 3초 동안 삑 소리를 냅니다.')
        winsound.Beep(1000, 3000)
    
    def quitFunction(self):
        self.close()
        
app = QApplication(sys.argv)
win = BeepSound()
win.show()
app.exec_()

        