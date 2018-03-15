from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
img=np.array(Image.open('D:/image_with_mark.png'))
result=img[:,:,0]
rows,cols,dims=img.shape
for i in range(0,rows):
	for j in range(0,cols):
		if (img[i,j,3]&1==0):
			result[i,j]=0
		else:
			result[i,j]=255
result=Image.fromarray(result)
result.save('D:/get_mark.png')
