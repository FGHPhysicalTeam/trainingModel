import numpy as np
import random
import cv2
from PIL import Image
from matplotlib import pyplot as plt
import os

def sp_noise(image,prob):
    '''
        添加椒盐噪声
        prob:噪声比例
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    #cv.imshow("gasuss", out)
    return out

index = 0
i = 15
tmp = 1200
dir = '.\\Pic\\charPic\\%s\\' % i
for rt, dirs, files in os.walk(dir):
    for filename in files:
        filename = dir + filename
        if filename != ".\\Pic\\charPic\\%s\\.DS_Store" % i:
            print(filename)
            img = cv2.imread(filename)
            # 添加椒盐噪声，噪声比例为 0.002
            tmpPath = ".\\Pic\\charPic\\{}\\E({}).png".format(i,tmp)
            out1 = sp_noise(img, prob=0.002)
            cv2.imwrite(tmpPath, out1)
            tmp = tmp + 1

# # 添加高斯噪声，均值为0，方差为0.001
# out2 = gasuss_noise(img, mean=0, var=0.001)

# 显示图像
# plt.figure(1)
# plt.subplot(131)
# plt.axis('off')  # 关闭坐标轴
# plt.title('Original')
# plt.imshow(img)
# plt.subplot(132)
# plt.axis('off')
# plt.title('Add Salt and Pepper noise')
# plt.imshow(out1)
# plt.subplot(133)
# plt.axis('off')
# plt.title('Add Gaussian noise')
# plt.imshow(out2)
# plt.show()