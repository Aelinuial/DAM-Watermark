from PIL import Image
from skimage import color
import numpy as np
import matplotlib.pyplot as plt
import qrcode
import sys
img=sys.argv[1]
qrcmark=sys.argv[2]
mark = qrcode.make(qrcmark)
mark=np.array(mark);
img=np.array(Image.open(img))
rows,cols=mark.shape
irows,icols,idims=img.shape
if (rows>irows) or (cols>icols):
	raise Exception("Error:The mark is too big to be encoded into the image")
for i in range(0,rows):
	for j in range(0,cols):
		if (mark[i,j]==True):
			img[i,j,3]=img[i,j,3]&254 +1
		else:
			img[i,j,3]=img[i,j,3]&254
img=Image.fromarray(img)
img.save('D:/image_with_mark.png')