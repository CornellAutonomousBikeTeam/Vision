import cv2
import numpy as np


def non(x):
    pass


pic = cv2.imread("download.jpg")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    key = cv2.waitKey(1)
    if key == 27:
        break
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grey, (5, 5), 1)
    o = cv2.Canny(blur, 150, 170)
    lines = cv2.HoughLinesP(o, 1, np.pi/180, 200)
    if lines is not None:
        for i in lines:
            x1, y1, x2, y2 = i[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("sa", o)
    cv2.imshow("msl", frame)


cap.release()
cv2.destroyAllWindows()
