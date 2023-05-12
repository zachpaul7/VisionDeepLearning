# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 15:27:30 2023

@author: zachp
"""

from PyQt5.QtWidgets import*
import sys
import cv2 as cv
import numpy as np

class Orim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('오림')
        self.setGeometry(200,200,800,200)
       
        fileButton=QPushButton('파일',self)
        paintButton=QPushButton('페인팅',self)
        cutButton=QPushButton('오림',self)
        incButton=QPushButton('+',self)
        decButton=QPushButton('-',self)
        eraseButton=QPushButton('색칠 지우기',self)
        saveButton=QPushButton('저장',self)
        quitButton=QPushButton('나가기',self)
       
        fileButton.setGeometry(10,10,100,30)
        paintButton.setGeometry(110,10,100,30)
        cutButton.setGeometry(210,10,100,30)
        incButton.setGeometry(310,10,50,30)
        decButton.setGeometry(360,10,50,30)
        eraseButton.setGeometry(410,10,150,30)
        saveButton.setGeometry(560,10,100,30)
        quitButton.setGeometry(660,10,100,30)
       
        fileButton.clicked.connect(self.fileOpenFunction)
        paintButton.clicked.connect(self.paintFunction)
        cutButton.clicked.connect(self.cutFunction)
        incButton.clicked.connect(self.incFunction)
        decButton.clicked.connect(self.decFunction)
        eraseButton.clicked.connect(self.eraseFunction)
        saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
       
        self.BrushSiz=5
        self.LColor,self.RColor=(255,0,0),(0,0,255)
       
    def fileOpenFunction(self):
        fname=QFileDialog.getOpenFileName(self,'Open file>','./')
        self.img=cv.imread(fname[0])
        if self.img is None:sys.exit('파일을 찾을 수 없습니다.')
           
        self.img_show=np.copy(self.img)
        cv.imshow('Painting',self.img_show)
       
        self.mask=np.zeros((self.img.shape[0],self.img.shape[1]),np.uint8)
        self.mask[:,:]=cv.GC_PR_BGD
       
    def paintFunction(self):
        cv.setMouseCallback('Painting',self.painting)
       
    def painting(self,event,x,y,flags,param):
        if event==cv.EVENT_LBUTTONDOWN:
            cv.circle(self.img_show,(x,y),self.BrushSiz,self.LColor,-1)
            cv.circle(self.mask,(x,y),self.BrushSiz,cv.GC_FGD,-1)
        elif event==cv.EVENT_RBUTTONDOWN:
            cv.circle(self.img_show,(x,y),self.BrushSiz,self.RColor,-1)
            cv.circle(self.mask,(x,y),self.BrushSiz,cv.GC_BGD,-1)
        elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
            cv.circle(self.img_show,(x,y),self.BrushSiz,self.LColor,-1)
            cv.circle(self.mask,(x,y),self.BrushSiz,cv.GC_FGD,-1)
        elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
            cv.circle(self.img_show,(x,y),self.BrushSiz,self.RColor,-1)
            cv.circle(self.mask,(x,y),self.BrushSiz,cv.GC_BGD,-1)
        cv.imshow('Painting',self.img_show)
   
    def cutFunction(self):
        if (self.mask == cv.GC_PR_BGD).all() or (self.mask == cv.GC_PR_FGD).all():
            return
        # GMM 초기화를 위한 샘플 데이터(bgSamples 및 fgSamples)가 비어있는 경우 발생
        
        background=np.zeros((1,65),np.float64)
        foreground=np.zeros((1,65),np.float64)
        cv.grabCut(self.img,self.mask,None,background,foreground,5,cv.GC_INIT_WITH_MASK)
        mask2=np.where((self.mask==2)|(self.mask==0),0,1).astype('uint8')
        self.grabImg=self.img*mask2[:,:,np.newaxis]
        cv.imshow('Scissoring',self.grabImg)
        
       
    def incFunction(self):
        self.BrushSiz=min(20,self.BrushSiz+1)
       
    def decFunction(self):
        self.BrushSiz=max(1,self.BrushSiz-1)
    
    def eraseFunction(self): # 추가된 함수
        self.img_show = np.copy(self.img)
        self.mask = np.zeros((self.img.shape[0], self.img.shape[1]), np.uint8)
        self.mask[:, :] = cv.GC_PR_BGD
        cv.imshow('Painting', self.img_show)
        
    def saveFunction(self):
        fname=QFileDialog.getSaveFileName(self,'파일저장','./')
        cv.imwrite(fname[0],self.grabImg)
       
    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()
       
app=QApplication(sys.argv)
win=Orim()
win.show()
app.exec_()