import cv2 # opencv-python
import easyocr
import pyttsx3

image_path = 'roadsign.jpg'

img = cv2.imread(image_path)

# cap = VideoCa

reader = easyocr.Reader(['en'],gpu=False) # reader object

texts = reader.readtext(img)

engine = pyttsx3.init()
audiotext = ""

while True:
    for text in texts: # danger , stop, sign
        bbox,text,score = text
        audiotext += text
        if score > 0.5:
            cv2.rectangle(img,bbox[0],bbox[2],(255,0,0),5) 
            cv2.putText(img,text,bbox[0],cv2.FONT_HERSHEY_COMPLEX,0.95,(0,255,0),2)
    
    engine.say(audiotext)
    engine.runAndWait()
    audiotext = ""
    cv2.imshow('Image',img)
    cv2.waitKey(1)