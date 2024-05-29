from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor


import cv2

model = YOLO('yolov8s.pt')

video_path = './test.mp4'
cap = cv2.VideoCapture(video_path)

results = model.predict(source='0',show=True)

print(results)
