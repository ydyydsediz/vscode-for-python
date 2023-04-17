import numpy as np
import matplotlib.pyplot as plt
cmap = np.zeros((256, 3))
cmap[:, 0] = np.linspace(0, 1, 256)    # 红色通道
cmap[:, 1] = 0                        # 绿色通道
cmap[:, 2] = np.linspace(1, 0, 256)    # 蓝色通道
img_gray = plt.imread('gray_jay.jpeg').astype(float) / 255
img_color = cmap[np.round(img_gray * 255).astype(int), :]

img_color = (img_color * 255).astype(np.uint8)
img_color = np.clip(img_color, 0, 255)
plt.imshow(img_color)
plt.show()
