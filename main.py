# coding=gbk
import cv2
import numpy as np
from lib import QRcode_videography_detection
detector = QRcode_videography_detection.QRcode()
while True:
    dataresult,inputresult=detector.detectcode()
    if dataresult:
        corners=detector.get_corners()
        for i in range(4):
            print("x{}:{},y{}:{}".format(i, corners[i].x, i, corners[i].y))
        input_dealed=detector.draw(inputresult)
        cv2.imshow("camera",input_dealed)
    else:
        cv2.imshow("camera",inputresult)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
detector.release()
cv2.destroyAllWindows()



