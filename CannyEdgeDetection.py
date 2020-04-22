# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import cv2
from matplotlib import pyplot as plt
import scipy

img=cv2.imread("home/vicky/Downloads/wall.png",0)
canny=cv2.Canny(img, 100, 200)

titles=['image','canny']
images=[img, canny]

for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[1], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
    
plt.show()