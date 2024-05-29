import cv2
import easyocr
import matplotlib.pyplot as plt
import pyttsx3
import time 

image_path = 'data/test1.png'

img = cv2.imread(image_path)
 
reader = easyocr.Reader(['en'],gpu=False)

text_ = reader.readtext(img)
engine = pyttsx3.init()
audiotext = ""

while True:
    for t in text_:
        bbox,text,score = t
        audiotext+=text
        if score > 0.25:
            cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
            cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.65,(255,0,0),2)

    cv2.imshow('Image',img)
    cv2.waitKey(30)
    engine.say(audiotext)
    engine.runAndWait()
    break

#plt.show()
# upper left and bottom right corner
# 3 lines for 3 lines of text 
# bounding box, text and accuracy 

