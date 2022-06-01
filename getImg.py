import cv2
i=0
cap = cv2.VideoCapture(0)
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    # cv2.imshow("ok",frame)
    # cv2.waitKey(20)
    face_detector = cv2.CascadeClassifier(
        r"C:\opencv\opencv300\opencv\build\etc\haarcascades\haarcascade_frontalface_default.xml")
    face = face_detector.detectMultiScale(image=frame, scaleFactor=1.1, minNeighbors=5, flags=0, minSize=(160, 160),
                                          maxSize=(640, 640))
    # scaleFactor  缩放因子
    print(face)
    for x, y, w, h in face:
        m=frame [ y :(y + h),x:(x + w)]
        cv2.imwrite("./cap_img/m_img/train/z"+i.__str__()+".jpg",frame)
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow("ok", frame)
        cv2.waitKey(20)

        with open("./cap_img/m_labels/train/z"+i.__str__()+".txt", "w") as f:
            x1=x+w/2
            y1=y+h/2
            xf=x1/(frame.shape[1])
            yf = y1 / (frame.shape[0])
            wf=w/(frame.shape[0])
            hf = h / (frame.shape[1])
            f.write("0 "+xf.__str__()+" "+yf.__str__()+" "+str(wf)+" "+str(hf))  # 自带文件关闭功能，不需要再写f.close()
            # f.write("1 0.5 0.5 1 1")
        i = i + 1
        break

cap.release()
cv2.destroyAllWindows()
