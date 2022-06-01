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


import socket
import cv2
import numpy as np
s=socket.socket()
s.bind(('192.168.5.123',8080)) #ip地址和端口号
s.listen(5)
global cs
while 1:
    try:
        cs,address = s.accept()
        print(address)
        n=1
        while 1:
            ra=cs.recv(1024)
            img_sizestr = ra.decode(encoding = 'utf-8')  # base64解码
            cs.send(b"ok")
            img_size=int(img_sizestr.replace("size=",''))

            ra=cs.recv(img_size)

            img = cv2.imdecode(np.frombuffer(ra, np.uint8), cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



            image = img
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
            xc = pred[..., 4] > 0.2  # candidate


            bs = pred.shape[0]
            output = [torch.zeros((0, 6), device=pred.device)] * bs



            pred=[pred]


            for xi, x in enumerate(pred):  # image index, image inference
                # Apply constraints
                # x[((x[..., 2:4] < min_wh) | (x[..., 2:4] > max_wh)).any(1), 4] = 0  # width-height

                x = x[0][xc[xi]]  # confidence
                # If none remain process next image

                if not x.shape[0]:
                    continue

                # Compute conf
                x[:, 5:] *= x[:, 4:5]  # conf = obj_conf * cls_conf

                # Box (center x, center y, width, height) to (x1, y1, x2, y2)
                box = xywh2xyxy(x[:, :4])

                i, j = (x[:, 5:] > 0.5).nonzero(as_tuple=False).T
                x = torch.cat((box[i], x[i, j + 5, None], j[:, None].float()), 1)

                max_nms=1
                # Check shape
                n = x.shape[0]  # number of boxes
                if not n:  # no boxes
                    continue
                elif n > max_nms:  # excess boxes
                    x = x[x[:, 4].argsort(descending=True)[:max_nms]]  # sort by confidence

                # Batched NMS
                c = x[:, 5:6] * (0 if agnostic else max_wh)  # classes
                boxes, scores = x[:, :4] + c, x[:, 4]  # boxes (offset by class), scores
                print("boxs"+boxes)
                i = torchvision.ops.nms(boxes, scores, 0.5)  # NMS
                if i.shape[0] > 1:  # limit detections
                    i = i[:1]

                output[xi] = x[i]
            print(output)
            if len(output) ==  0:
                cs.send(b"0,0,0,0,ok")
                n = n + 1
                print(n)
                continue
            res=output
            try:
                x1 = int(res[0][0][0])
                y1 = int(res[0][0][1])

                w1 = int(res[0][0][2])
                h1 = int(res[0][0][3])
                image = cv2.rectangle(image, (int(x1 - w1 / 2), int(y1 - h1 / 2)), (int(x1 + w1 / 2), int(y1 + h1 / 2)),
                                      (255, 0, 0), 2)
                cv2.imshow("ok", image)
                cv2.waitKey(20)
            except:
                cs.send(b"0,0,0,0,ok")
                n = n + 1
                print(n)
                cv2.imshow("ok", image)
                cv2.waitKey(20)
                continue
            #res = non_max_suppression(pred, 0.25, 0.45, classes=None, agnostic=False, labels=(), max_det=1)    print(res)
            x1=int(x1 - w1 / 2).__str__()
            y1=int(y1 - h1 / 2).__str__()
            x2=int(w1).__str__()
            y2=int(h1).__str__()
            str=x1 + "," + y1 + "," + x2 + "," + y2 + "," + "ok"
            print(str)
            cs.send(bytes(str,encoding = "utf8"))
            n = n + 1
            print(n)
    except:
        cs.close()
        continue

