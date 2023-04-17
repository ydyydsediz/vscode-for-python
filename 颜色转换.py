import cv2 as cv
import numpy as np
img = cv.imread("jay.jpeg")
img_gray = cv.cvtColor(img ,cv.COLOR_BGR2GRAY)
img_inverted = cv.bitwise_not(img)
cv.imshow("yuantu",img)
cv.imshow("fanzhuan",img_inverted)
cv.waitKey(0)
img = cv.normalize