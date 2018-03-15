from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
imgwmark=sys.argv[1]
imgwmark=np.array(Image.open(imgwmark))
result=imgwmark
rows,cols,dims=imgwmark.shape
rows=rows//2
cols=cols//2
box = (0,0,cols,rows) 
for i in range(0,dims):
    for j in range(0,rows*2):
        for k in range(0,cols*2):
           imgwmark[j,k,i]=imgwmark[j,k,i]&3
for i in range(0,dims):
    for j in range(0,rows):
        for k in range(0,cols):
        	result[j,k,i]=imgwmark[2*j,2*k,i]*64+imgwmark[2*j,2*k+1,i]*16+imgwmark[2*j+1,2*k,i]*4+imgwmark[2*j+1,2*k+1,i]
mark_get=Image.fromarray(result)
mark_get=mark_get.crop(box)
mark_get.save('D:/mark_get.png')