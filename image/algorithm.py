
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


def detect (matrix, x, y) :
    # create matrix :
    # map = np.zeros((3,3))
    # for i in range(-1,2,1) :
    #     for j in range(-1,2,1) :
    #         map[i+1][j+1] = matrix[x+i][y+j]

    line = [matrix[x-1][y-1], matrix[x-1][y], matrix[x-1][y+1], matrix[x][y+1],
            matrix[x+1][y+1], matrix[x+1][y], matrix[x+1][y-1], matrix[x][y-1]]
    
    counter = 0
    if line[0]>0 and line[-1]>0 :
        counter = -1 
    for i in range(len(line)) :
        if line[i] > 0 :
            if i==0 :
                counter += 1
                continue
            if line[i-1]== 0 :
                counter += 1
    # print (x,y, line, counter)
    if counter <= 1 : return True 
    return False

     
    

# ===========================================================
img = cv2.imread('hihi.png', 0)

for i in range(len(img)) :
    for j in range(len(img[i])) :
        if img[i][j] == 0 :
            if detect(img, i, j) :
                img[i][j] = 255

cv2.imwrite("haha.png", img)


