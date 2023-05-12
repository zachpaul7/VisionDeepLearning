# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 16:06:17 2023

@author: zachp
"""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import sys
import cv2 as cv

class Video(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("비디오에서 프레임 수집")
        self.setGeometry(200, 200, 600, 100)
        
        videoButton = QPushButton('비디오 켜기', self)
        captureButton = QPushButton('프레임 잡기', self)
        saveButton = QPushButton('프레임 저장', self)
        quitButton = QPushButton('나가기', self)
        multiCaptureButton = QPushButton('여러프레임 잡기', self)
        
        videoButton.setGeometry(10, 10, 100, 30)
        captureButton.setGeometry(110, 10, 100, 30)
        saveButton.setGeometry(210, 10, 100, 30)
        quitButton.setGeometry(310, 10, 100, 30)
        multiCaptureButton.setGeometry(410, 10, 100, 30)
        
        videoButton.clicked.connect(self.videoFunction)
        captureButton.clicked.connect(self.captureFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        multiCaptureButton.clicked.connect(self.multiCaptureFunction)
        
        self.capturedFrames = [] # 여러 프레임을 저장할 리스트
        self.MAX_CAPTURES = 3 # 최대 획득 가능한 프레임 수
        
    def videoFunction(self):
        self.cap = cv.VideoCapture(0,cv.CAP_DSHOW)
        if not self.cap.isOpened(): self.close()
        
        while True:
            ret, self.frame = self.cap.read()
            if not ret : break
            cv.imshow('video display',self.frame)
            cv.waitKey(1)
        
    def captureFunction(self):
        self.capturedFrames = [self.frame] # 단일 프레임만 저장
        cv.imshow('Captured Frame', self.capturedFrames[0])
        
    def multiCaptureFunction(self):
        if len(self.capturedFrames) < self.MAX_CAPTURES: # 최대 획득 가능한 프레임 수보다 적을 때
            self.capturedFrames.append(self.frame) # 새로운 프레임 추가
        else:
            self.capturedFrames.pop(0) # 리스트의 첫번째 프레임 삭제
            self.capturedFrames.append(self.frame) # 새로운 프레임 추가
        for i, frame in enumerate(self.capturedFrames):
            cv.imshow(f'Captured Frame {i+1}', frame)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_C:
            self.multiCaptureFunction()
        
    def saveFunction(self):
        fname = QFileDialog.getSaveFileName(self, '파일 저장', './')
        cv.imwrite(fname[0],self.capturedFrames[-1])
    
    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()
        
app = QApplication(sys.argv)
win = Video()
win.show()
app.exec_()
