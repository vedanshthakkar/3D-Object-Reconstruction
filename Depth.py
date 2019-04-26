import numpy as np
import cv2
from matplotlib import pyplot as plt

leftImage  = cv2.imread('1.jpg',0)
rightImage = cv2.imread('2.jpg',0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(leftImage,rightImage)
plt.imshow(disparity,'gray')
plt.show()
gray = cv2.cvtColor(disparity, cv2.COLOR_BGR2GRAY)
plt.imsave('Depth',gray )