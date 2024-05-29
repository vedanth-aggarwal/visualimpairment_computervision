# gtts playsound
# pip3 install PyObjC

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from testing import gTTS
from playsound import playsound

cap = cv2.VideoCapture(0)
labels = []

while True:
    ret,frame = cap.read()
    if frame is not None:
        bbox,label,conf = cv.detect_common_objects(frame,model='yolov8')
    output_image = draw_bbox(frame,bbox,label,conf)
    cv2.imshow('Image',output_image)
    
    for item in label:
        if item not in labels:
            labels.append(item)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


