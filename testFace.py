# opencv 推理
import cv2
import numpy as np
import torch
from utils.mygeneral import non_max_suppression
from utils.torch_utils import select_device
face_detector = cv2.CascadeClassifier(
        r"./haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)
net = cv2.dnn.readNetFromONNX("best.onnx")  # 加载训练好的识别模型

while 1:
    image = cap.read()[1]
    face = face_detector.detectMultiScale(image=image, scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(160, 160),
                                          maxSize=(640, 640))
    print(len(face))
    for x, y, w, h in face:
        if x<20 or y<20 or w<160 or h<160:
            break
        m=image [ (y-20) :(y+20 + h),(x-20):(x+20 + w)]
        temp=m
        print(m.shape)
        cv2.imshow("ok",m)
        cv2.waitKey(20)
        blob = cv2.dnn.blobFromImage(m,scalefactor=1,size=(640,640))  # 由图片加载数据 这里还可以进行缩放、归一化等预处理
        net.setInput(blob)  # 设置模型输入
        pre = net.forward()  # 推理出结果
        res=non_max_suppression(pre,0.25,0.45,classes=None,agnostic=False,multi_label=False,labels=(),max_det=1)
        print("res:")
        print(res)
        x1=int(res[0][0][0])
        y1=int(res[0][0][1])

        w1=int(res[0][0][2])
        h1=int(res[0][0][3])
        image =m
        image=cv2.resize(image,(640,640))
        image=cv2.rectangle(image,(int(x1-w1/2),int(y1-h1/2)),(int(x1+w1/2),int(y1+h1/2)),(255,0,0),2)
        cv2.imshow("ok",image)
        cv2.waitKey(1)
