#C:\Program Files\Tesseract-OCR

import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread(r'data/test2.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print('Hello' + pytesseract.image_to_string(img,lang='eng',config='--psm 7'))
cv2.imshow('Result',img)
cv2.waitKey(0)