import pygame
import time

'''
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file).convert()
        self.rect = self.image.get_rect(topleft=location)


class Car(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.original_image = pygame.image.load(image_file).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=location)


    def rotate(self, angle) :
        self.image = pygame.transform.rotate(self.original_image, angle)
        # Get a new rect and pass the center of the previous rect. This
        # will keep the car centered.
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def move(self, location) :
        self.rect.topleft = location
    


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))

background = Background('image/raw_map.png', [0,0])
car = Car('image/car.png', [50,100])
# car = pygame.image.load('image/car.png')

screen.blit(background.image, background.rect)
screen.blit(car.image, [50, 100])

pygame.display.flip()

for i in range(90) :
    # screen.fill((255, 0, 0))
    car.rotate(i)
    # new_car = pygame.transform.rotate(car, i)

    screen.blit(background.image, background.rect)
    screen.blit(car.image, car.rect)
    clock.tick(15)
    pygame.display.update()
    
'''

import math
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


A = (1,1)
B = (0.5,2)
print (cal_angle(A, B))