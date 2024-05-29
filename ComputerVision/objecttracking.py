from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

video_path = './test.mp4'
cap = cv2.VideoCapture(0)

ret = True
while ret:
    ret,frame = cap.read() # ret if read is success

    results = model.track(frame,persist=True) # remenber past frame objects

    frame_ = results[0].plot()

    cv2.imshow('frame',frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
