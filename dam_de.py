from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
img=sys.argv[1]
img=np.array(Image.open(img))#打开图像并转化为数字矩阵
rows,cols,dims=img.shape
for i in range(0,dims):
    for j in range(0,rows):
        for k in range(0,cols):
            img[j,k,i]=img[j,k,i]&3
imghsv=Image.fromarray(img)#矩阵转换为图像
imghsv=color.rgb2hsv(imghsv)
imghsv=np.array(imghsv)
for i in range(0,rows):
    for j in range(0,cols):
        imghsv[i,j,dims-1]=imghsv[i,j,dims-1]*85
imgrgb=color.hsv2rgb(imghsv)
plt.figure("after")
plt.imshow(imgrgb)
plt.axis('off')
plt.show()