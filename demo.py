import pygame
from src.car import Car
from src.background import Background
from src.light import Light
from src.text import Text
from src.stone import Stone

import sys
sys.path.append("src")
from src.transaction import Transaction
import math
from numpy import sign

## INIT GAME
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 700))

## INIT OBJECT
transaction = Transaction()
text = Text()
background = Background('image/single_central.png', [0,0])
stone = Stone("image/stone.png", [0,0])
car = Car('image/car.png', [0, 0])
light = Light(['image/red.png', 'image/green.png', 'image/yellow.png'], [100,200])

## BLIT
screen.blit(background.image, background.rect)
screen.blit(text.text, text.rect)
screen.blit(car.image, car.rect)
screen.blit(light.image, light.rect)

pygame.display.flip()


## CONTROL DISPLAY
def update_display () :
    global screen, stone, car, background, text
    screen.blit(background.image, background.rect)
    screen.blit(text.text, text.rect) 
    screen.blit(stone.image, stone.rect)
    screen.blit(car.image, car.rect)
    screen.blit(light.image, light.rect)
    pygame.display.update()
    return


## GET START - STONE
def get_point (msg):
    global text
    while True:
        flag = False
        text.set_text(msg, [100, 100])
        ev = pygame.event.get()
        update_display()
        for event in ev:
        # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                print (pos)
                flag = True
        if flag:
            return pos

start = get_point("Select begin position")
end = get_point("Select end position")
stone_pos = get_point("Select stone position")

stone.move_to(stone_pos)
    
## GAME LOOP
path, angles = transaction.find_path(start=start, end=end)
print (angles)
couter = 1

for i in range(len(path)) :
    node = path[i]
    angle = angles[i]

    car.move_to(list(node))
    car.rotate(angle)

    update_display()
    pygame.time.delay(20)

