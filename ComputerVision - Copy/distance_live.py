import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import pyttsx3

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
engine = pyttsx3.init()

while True:
    success, img = cap.read()
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img, faces = detector.findFaceMesh(img, draw=False)
    #img = cv2.flip(img,flipCode=1)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # Drawing
        cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w, _ = detector.findDistance(pointLeft, pointRight)
        W = 6.3

        # # Finding the Focal Length
        # d = 50
        # f = (w*d)/W
        # print(f)

        # Finding distance
        f = 840
        d = (W * f) / w
        print(d)

        
        cvzone.putTextRect(img, f'Depth : {int(d)}',
                           (face[10][0] - 100, face[10][1] - 50),
                           scale=2)
    
    if face[10][0] < 300:
            cvzone.putTextRect(img, 'MOVE LEFT -------->',
                           (100, 100),
                           scale=2)
    else:
         cvzone.putTextRect(img, 'MOVE RIGHT <-------',(200,200),scale=2)

    #img = cv2.flip(img,flipCode=1)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        if d < 90:
            engine.say('Person is close to you!')
            engine.runAndWait()
        else:
            engine.say('Person is far to you!')
            engine.runAndWait()