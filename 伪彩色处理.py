import matplotlib.pyplot as plt
import numpy as np

# 加载灰度图像
img_gray = plt.imread('gray_jay.jpeg')

# 创建 colormap
cmap = plt.cm.jet

# 应用 colormap 将灰度值映射到颜色值
img_color = cmap(img_gray)

# 显示伪彩色图像
plt.imshow(img_color)

# 显示色度条
plt.colorbar()

# 显示图像
plt.show()
