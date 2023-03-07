# 导入cv2模块
import cv2 as cv
# 读取图片
img = cv.imread('jay.jpeg')
# 修改图片尺寸
resize_img = cv.resize(img, dsize=(200, 200))
# 显示原图
cv.imshow('jay.jpeg', img)
# 显示修改后的图片
cv.imshow('resize_img', resize_img)
# 保存修改尺寸后的图片
cv.imwrite('resize_jay.jpeg', resize_img)
# 打印未修改图片的尺寸大小
print('未修改前', img.shape)
# 打印修改后图片的尺寸大小
print('修改后', resize_img.shape)
# 按下按钮退出
while True:
    if ord('y') == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
