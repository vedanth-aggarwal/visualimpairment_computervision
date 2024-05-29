from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0) # video1.mp4

while True:
    success,img = cap.read()
    results = model.track(img,persist=True)
    object = results[0].plot()

    cv2.imshow('Image',object)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


