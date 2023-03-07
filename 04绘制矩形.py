#导入cv2模块
import cv2 as cv
#读取图片
img = cv.imread('jay.jpeg')
#定坐标
x,y,w,h = 100,100,100,100
#绘制矩形
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=1)
#绘制圆形
cv.circle(img, center=(x+w, y+h),radius=(100),color=(255,0,0), thickness=2)
#显示图片
cv.imshow('draw',img)
# 按下按钮退出
while True:
    if ord('y') == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
