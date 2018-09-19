import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

# img = cv2.imread('central.png', 0)
# fig=plt.figure()
# print (np.shape(img), img)



# histogram = set()
# for width in range(len(img)) :
#     for height in range(len(img[width])) :
#         if img[width][height] < 100 :
#             img[width][height] = 0
#         else :
#             img[width][height] = 255
            # histogram.add (img[width][height])
# print (histogram)


# ==== CREATE ===========================================
img =  [[0,0,0,0,0,0,0,0],
        [0,255,255,255,255,255,255,0],
        [0,255,255,0,255,255,255,0],
        [0,255,0,0,0,0,255,0],
        [0,255,255,0,0,0,255,0],
        [0,255,0,0,0,0,255,0],
        [0,0,255,255,255,255,0,0],
        [0,0,0,0,0,0,0,0]]
img = np.array(img)
for line in img :
    line = np.array(line)

for w in range(len(img)) :
    for h in range(len(img[w])) :
        img[w][h] = abs(img[w][h] - 255) 

cv2.imwrite("central_test.png", img)
# ===========================================================

# plt.imshow(img, cmap='gray')
# plt.show()


# kernel =  np.ones((2,2),np.uint8)
# erosion1 = cv2.erode(img,kernel,iterations = 60)

# plt.imshow(erosion1, cmap='gray')
# plt.show()