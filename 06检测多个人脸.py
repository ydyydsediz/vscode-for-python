# 导入cv2模块
import cv2 as cv
# 读取图片
img = cv.imread('tfboy.jpeg')
# 人脸检测函数
def face_detect_demo():
    # 图片灰度转换
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 调用opencv训练好的分类器模型
    face_detect = cv.CascadeClassifier(
        'Y:/opencv4.7.0/opencv/sources/data/haarcascades/haarcascade_frontalface_alt2.xml')

    # 检测范围
    face = face_detect.detectMultiScale(img, 1.02, 5)
    # 绘制矩形框
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w, y+h), color=(255, 0, 0), thickness=1)
    # 显示图片
    cv.imshow("show", img)
    
# 调用人脸检测函数
face_detect_demo()
# 按下按钮退出
while True:
    if ord('y') == cv.waitKey(0):
        break
# 释放内存
cv.destroyAllWindows()
