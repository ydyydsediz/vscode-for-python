import numpy as np
import matplotlib.pyplot as plt

# 加载彩色图像
img = plt.imread('jay.jpeg')

# 将彩色图像转换为灰度图像
gray_img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

# 计算灰度图像的最小值和最大值
min_val = gray_img.min()
max_val = gray_img.max()

# 计算灰度分层数量
num_levels = 5

# 计算每个灰度分层的像素值范围
level_range = (max_val - min_val) / num_levels
level_ranges = [(min_val + i * level_range, min_val + (i+1)
                 * level_range) for i in range(num_levels)]

# 创建灰度分层图像
layered_img = np.zeros_like(img)
for i, (level_min, level_max) in enumerate(level_ranges):
    idx = np.where((gray_img >= level_min) & (gray_img <= level_max))
    layered_img[idx] = np.array([255 * (i+1) / num_levels] * 3)

# 保存灰度分层图像到文件
plt.imsave('layered_image.jpg', layered_img)

# 显示结果
plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title('Original Image')
plt.subplot(1, 2, 2)
plt.imshow(layered_img)
plt.title('Layered Image')
plt.show()