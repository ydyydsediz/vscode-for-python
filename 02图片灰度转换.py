# 导入cv模块
import cv2 as cv
# 读取图片
img = cv.imread('jay.jpeg')
#灰度转换
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#显示灰度图片
cv.imshow('gray_jay',gray_img)
#保存灰度图片
cv.imwrite('gray_jay.jpeg', gray_img)
#显示【没有】灰度转化后的图片
cv.imshow('not_gray_jay.jpeg',img)
# 等待时间，单位ms
cv.waitKey(0)
# 释放内存
cv.destroyAllWindows()
