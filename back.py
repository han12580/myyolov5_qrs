import numpy

from models.common import DetectMultiBackend
from utils.datasets import IMG_FORMATS, VID_FORMATS, LoadImages, LoadStreams
from utils.general import (LOGGER, check_file, check_img_size, check_imshow, check_requirements, colorstr, cv2,
                           increment_path, non_max_suppression, print_args, scale_coords, strip_optimizer, xyxy2xywh,xywh2xyxy)
from utils.plots import Annotator, colors, save_one_box
from utils.torch_utils import select_device, time_sync

data='data/coco128_QRS.yaml'
device = select_device("cpu")
dnn=False
half=False
imgsz=(640, 640)
model = DetectMultiBackend("./best.pt", device=device, dnn=dnn, data=data, fp16=half)
stride, names, pt = model.stride, model.names, model.pt
imgsz = check_img_size(imgsz, s=stride)  # check image size
max_wh = 7680  # (pixels) maximum box width and height

import time

import torchvision


from utils.downloads import gsutil_getsize
from utils.metrics import box_iou, fitness
from utils.augmentations import Albumentations, augment_hsv, copy_paste, letterbox, mixup, random_perspective
agnostic=False
# opencv 推理
import cv2
import torch
face_detector = cv2.CascadeClassifier(
        r"./haarcascade_frontalface_default.xml")

import socket
import cv2
import numpy as np
def detect_han(img):
    image = img
    face = face_detector.detectMultiScale(image=image, scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(160, 160),
                                          maxSize=(640, 640))
    if len(face) == 0:
        return None
    image=img
    image = cv2.flip(image, 1)

    image = letterbox(image, 640, stride=32)[0]
    im=image
    #255print(im)
    im = im.transpose(2, 0, 1)


    im = torch.from_numpy(im).to(device)
    im = im.half() if model.fp16 else im.float()  # uint8 to fp16/32
    im /= 255  # 0 - 255 to 0.0 - 1.0

    im=torch.unsqueeze(im, 0)

    pred = model(im, augment=False, visualize=False)
    xc = pred[..., 2] > 250  # candidate
    print(xc)
    pred=pred[xc]
    print(pred)
    xc = pred[..., 3] > 250  # candidate
    print(xc)
    pred=pred[xc]
    print(pred)
    bs = pred.shape[0]
    output = [torch.zeros((0, 6), device=pred.device)] * bs
    han=pred[...,5]*pred[...,4]

    zhao=pred[...,6]*pred[...,4]


    val_han, in_han=torch.max(han, -1, True)
    val_zhao, in_zhao=torch.max(zhao,-1,True)
    print(val_han)
    print(val_zhao)



    val_han=float(val_han[0])
    in_han=int(in_han[0])
    val_zhao = float(val_zhao[0])
    in_zhao = int(in_zhao[0])
    print(val_han)
    print(val_zhao)
    text=""
    if val_han>val_zhao:
        print("han")
        print(in_han)
        text="han_juntao"
        output=pred[in_han]
    else:
        print("zhao")
        text="zhao_tianlong"
        output=pred[in_zhao]
    print("output")
    print(output)

    x1 = int(output[0])
    y1 = int(output[1])

    w1 = int(output[2])
    h1 = int(output[3])
    image = cv2.rectangle(image, (int(x1 - w1 / 2), int(y1 - h1 / 2)), (int(x1 + w1 / 2), int(y1 + h1 / 2)),
                          (255, 0, 0), 2)
    cv2.putText(image, text, (int(x1 - w1 / 2), int(y1 + h1 / 2)), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 15)
    return image


