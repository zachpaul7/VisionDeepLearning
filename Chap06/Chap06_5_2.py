# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 11:38:49 2023

@author: zachp
"""

from PyQt5.QtWidgets import *
import cv2 as cv
import numpy as np
import winsound
import sys

class Panorama(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('파노라마 영상')
        self.setGeometry(200,200,800,200)
        
        collectButton=QPushButton('영상수집',self)
        self.showButton=QPushButton('영상보기',self)
        self.stitchButton=QPushButton('봉합',self)
        self.removeButton=QPushButton('영역 제거',self) # 검은색 영역 제거 버튼 추가
        self.saveButton=QPushButton('저장',self)
        quitButton=QPushButton('나가기',self)
        self.label=QLabel('환영합니다.',self)
        
        collectButton.setGeometry(10,25,100,30)
        self.showButton.setGeometry(110,25,120,30)
        self.stitchButton.setGeometry(230,25,120,30)
        self.removeButton.setGeometry(350, 25, 120, 30) # 검은색 영역 제거 버튼 좌표 설정
        self.saveButton.setGeometry(470,25,100,30)
        quitButton.setGeometry(570,25,100,30)
        self.label.setGeometry(10,40,600,170)
        
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.removeButton.setEnabled(False) # 영상 수집이 끝나기 전 까지 검은색 영역 제거 버튼 비활성화
        self.saveButton.setEnabled(False)
        
        collectButton.clicked.connect(self.collectFunction)
        self.showButton.clicked.connect(self.showFunction)
        self.stitchButton.clicked.connect(self.stitchFunction)
        self.removeButton.clicked.connect(self.vignetteFunction) # 검은색 영역 제거 버튼클릭시 removeBlack 함수 연결
        self.saveButton.clicked.connect(self.saveFunction)
        quitButton.clicked.connect(self.quitFunction)
        
    def collectFunction(self):  
        self.showButton.setEnabled(False)
        self.stitchButton.setEnabled(False)
        self.removeButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.label.setText('c를 여러 번 눌러 수집하고 끝나면 q를 눌러 비디오를 끕니다.')
        
        self.cap=cv.VideoCapture(0,cv.CAP_DSHOW)
        if not self.cap.isOpened(): sys.exit('카메라 연결 실패')
            
        self.imgs=[]
        while True:
            ret,frame=self.cap.read()
            if not ret: break
                
            cv.imshow('video display',frame)
            
            key=cv.waitKey(1)
            if key==ord('c'):
                self.imgs.append(frame)
            elif key==ord('q'):
                self.cap.release()
                cv.destroyWindow('video display')
                break
                
            if len(self.imgs)>=2:
                self.showButton.setEnabled(True)
                self.stitchButton.setEnabled(True)
                self.removeButton.setEnabled(True)
                self.saveButton.setEnabled(True)
    def showFunction(self):
        self.label.setText('수집된 영상은'+str(len(self.imgs))+'장입니다.')
        stack=cv.resize(self.imgs[0],dsize=(0,0),fx=0.25,fy=0.25)
        for i in range(1,len(self.imgs)):
            stack=np.hstack((stack,cv.resize(self.imgs[i],dsize=(0,0),fx=0.25,
            fy=0.25)))
        cv.imshow('Image collection',stack)
            
    def stitchFunction(self):
        stitcher=cv.Stitcher_create()
        status,self.img_stitched=stitcher.stitch(self.imgs)
        if status==cv.STITCHER_OK:
            cv.imshow('Image stitched panorama',self.img_stitched)
        else:
            winsound.Beep(3000,500)
            self.label.setText('파노라마 제작에 실패하였습니다. 다시 시도하세요.')
                
    
    def vignetteFunction(self):
        if hasattr(self, 'img_stitched'):
            h, w = self.img_stitched.shape[:2]
            mask = np.zeros((h, w), np.uint8)
            cv.ellipse(mask, (int(w/2), int(h/2)), (int(w/2), int(h/2)), 0, 0, 360, (255, 255, 255), -1)
            masked_img = cv.bitwise_and(self.img_stitched, self.img_stitched, mask=mask)
            vignette = cv.addWeighted(masked_img, 0.7, cv.blur(masked_img, (int(w/2.5), int(h/2.5))), 0.3, 0)
            cv.imshow('Vignette', vignette)
        else:
            self.parent().label.setText("파노라마 영상이 없습니다.")

    def saveFunction(self):
        fname=QFileDialog.getSaveFileName(self,'파일저장','./')
        cv.imwrite(fname[0],self.img_stitched)
            
    def quitFunction(self):
        self.cap.release()
        cv.destroyAllWindows()
        self.close()
        
app=QApplication(sys.argv)
win=Panorama()
win.show()
app.exec_()