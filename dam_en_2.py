from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
img=sys.argv[1]
mark=sys.argv[2]
img=np.array(Image.open(img))
mark=np.array(Image.open(mark))
rows,cols,dims=mark.shape
for i in range(0,dims):
    for j in range(0,rows*2):
        for k in range(0,cols*2):
            img[j,k,i]=img[j,k,i]&252
for i in range(0,dims):
    for j in range(0,rows):
        for k in range(0,cols):
        	img[2*j,2*k,i]=img[2*j,2*k,i]+(mark[j,k,i]&192)//64
        	img[2*j,2*k+1,i]=img[2*j,2*k+1,i]+(mark[j,k,i]&48)//16
        	img[2*j+1,2*k,i]=img[2*j+1,2*k,i]+(mark[j,k,i]&12)//4
        	img[2*j+1,2*k+1,i]=img[2*j+1,2*k+1,i]+(mark[j,k,i]&3)
img=Image.fromarray(img)
img.save('D:/image_with_mark.png')