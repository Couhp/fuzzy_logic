import pygame
from src.car import Car
from src.background import Background
import sys
sys.path.append("src")
from src.transaction import Transaction
import math
from numpy import sign

## INIT GAME
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))

## INIT OBJECT
transaction = Transaction()
background = Background('image/single_central.png', [0,0])
car = Car('image/car.png', [0, 0])

screen.blit(background.image, background.rect)
screen.blit(car.image, car.rect)

pygame.display.flip()

## CONTROL DISPLAY
def update_display () :
    global screen, car, background 
    screen.blit(background.image, background.rect)
    screen.blit(car.image, car.rect)
    pygame.display.update()
    return

## GAME LOOP
def mean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

def get_angle (path, i, node) :
    def cal_angle (node, next_node) :
        x1, y1 = node
        x2, y2 = next_node
        ZERO = 0.01
        if abs(x1 - x2) < ZERO : 
            if y2 > y1 : return -90
            if y2 < y1 : return 90
        else :
            angle = abs(math.degrees(math.atan( (y1-y2)/(x1-x2) )))
            if      x1 < x2 and y1 >= y2 : return angle
            elif    x1 < x2 and y1 <= y2 : return -angle
            elif    x1 > x2 and y1 >= y2 : return 180-angle
            elif    x1 > x2 and y1 <= y2 : return angle-180
        print ("Oh shit @@@ $$$")
        return 0
    #### 
    if i+5 > len(path) :
        next_node = (mean([x[0] for x in path[i:]]), mean([x[1] for x in path[i:]]))
    else :
        next_node = (mean([x[0] for x in path[i+5:i+10]]), mean([x[1] for x in path[i+5:i+10]]))
    
    angle = cal_angle(node, next_node)
    return angle

def soft_move (angles) :
    new_angles = []
    RANGE = 5
    for i in range(len(angles)) :
        if i < RANGE :
            new_angles.append(mean(angles[:i]))
        elif i+RANGE-1 > len(angles) :
            new_angles.append(mean(angles[i:]))
        else :
            new_angles.append(mean(angles[i-RANGE:i+RANGE]))    
    return new_angles


path = transaction.find_path(start=(600,500), end=(100,100))
angles = []
for i in range(len(path)) :
    node = path[i]
    angle = get_angle (path, i, node)    
    angles.append(angle)

new_angles = soft_move(angles)

print (new_angles)

for i in range(len(path)) :
    node = path[i]
    angle = new_angles[i]

    car.move_to(list(node))
    car.rotate(angle)

    update_display()
    pygame.time.delay(30)

