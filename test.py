# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import socket
import sys

import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication
import back
class MyBeautifulThread(QThread):
    cap=cv2.VideoCapture(0)
    show_img=pyqtSignal()
    a,img=cap.read()
    def __init__(self):
        super(MyBeautifulThread, self).__init__()

    def run(self):
        s = socket.socket()
        s.bind(('192.168.5.123', 8080))  # ip地址和端口号
        s.listen(5)
        while 1:
            cs, address = s.accept()
            print(address)
            n = 1
            while 1:
                ra = cs.recv(1024)
                img_sizestr = ra.decode(encoding='utf-8')  # base64解码
                cs.send(b"ok")
                img_size = int(img_sizestr.replace("size=", ''))
                ra = cs.recv(img_size)
                self.img = cv2.imdecode(np.frombuffer(ra, np.uint8), cv2.IMREAD_COLOR)
                print("start emit")
                self.show_img.emit()
                print("emit end")
                cv2.imshow("ok",self.img)
                cv2.waitKey(20)
                cs.send(b"25,45,62,58,hsjd")
                n = n + 1
                print(n)





class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1000, 600)
        self.pushButton_start = QtWidgets.QPushButton(Dialog)
        self.pushButton_start.setGeometry(QtCore.QRect(800, 430, 93, 28))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_start.clicked.connect(self.opnen_button)
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(800, 480, 93, 28))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.label.setObjectName("label")
        self.mbt = MyBeautifulThread()
        self.mbt.show_img.connect(self.showImg)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_start.setText(_translate("Dialog", "开始采集"))
        self.pushButton_exit.setText(_translate("Dialog", "退出"))
        self.label.setText(_translate("Dialog", "TextLabel"))
    def opnen_button(self):

        self.mbt.start()
    def showImg(self):
        print("1")
        cv2.imshow("ok",self.mbt.img)
        cv2.waitKey(20)
        image_height, image_width, image_depth = self.mbt.img.shape
        im=self.mbt.img
        im=back.detect_han(im)
        if im is None:
            im=self.mbt.img
        QIm = QImage(im.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                     image_width * image_depth,
                     QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(QIm))

        print("1")
