
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import pickle


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
img = cv2.imread('temp_central.png', 0)

for width in range(len(img)) :
    for height in range(len(img[width])) :
        if img[width][height] < 200 :
            img[width][height] = 0
        else :
            img[width][height] = 255

for i in range(len(img)) :
    for j in range(len(img[i])) :
        if img[i][j] == 0 :
            if detect(img, i, j) :
                img[i][j] = 255

cv2.imwrite("single_central.png", img)



# =====    Create matrix =============================
def neighbor (x, y) :
    global img
    result = []
    for i in range(-1, 2, 1) :
        for j in range(-1, 2, 1) :
            if (i!= 0 or j != 0) and img[x+i][y+j] == 0 :
                result.append((x+i,y+j))
    return result 

img = cv2.imread('single_central.png', 0)
print (np.shape(img))
nodes = {}

counter = 0
for i in range(len(img)-1) :
    for j in range(len(img[i])-1) :
        if i == 0 or j == 0 :
            continue
        if img[i][j] == 0 :
            nodes[(i,j)] = neighbor(i, j)
            if len(neighbor(i,j)) == 2 :
                counter += 1

# print (nodes, counter)

with open('map.dat', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=2)


