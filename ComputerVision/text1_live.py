import cv2
import easyocr
import matplotlib.pyplot as plt
import pyttsx3

image_path = 'data/test1.png'

img = cv2.imread(image_path)
 
reader = easyocr.Reader(['en'],gpu=False)

cap = cv2.VideoCapture(0)
engine = pyttsx3.init()

while True:
    _,img = cap.read()
    try:
        text_ = reader.readtext(img)
        audiotext = ""
        for t in text_:
            bbox,text,score = t
            audiotext = audiotext + text + "\n"
            if score > 0.8:
                cv2.rectangle(img,bbox[0],bbox[2],(0,255,0),5)
                cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.65,(255,0,0),2)
                
    except:
        pass

    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(audiotext)
        engine.say(audiotext)
        engine.runAndWait()




# upper left and bottom right corner
# 3 lines for 3 lines of text 
# bounding box, text and accuracy 

