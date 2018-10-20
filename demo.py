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
screen = pygame.display.set_mode((1400, 700))

## INIT OBJECT
transaction = Transaction()
background = Background('image/raw_map.png', [0,0])
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
path, angles = transaction.find_path(start=(100,500), end=(1200,500))

for i in range(len(path)) :
    node = path[i]
    angle = angles[i]

    car.move_to(list(node))
    car.rotate(angle)

    update_display()
    pygame.time.delay(10)

