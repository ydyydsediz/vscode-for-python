# 导入cv模块
import cv2 as cv
# 读取图片
img = cv.imread('jay.jpeg')
# 显示图片
cv.imshow("photo", img)
# 等待时间，单位ms
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
