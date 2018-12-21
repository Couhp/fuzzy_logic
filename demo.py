import pygame
import time as timer
from src.user_interface import UI
from src.fuzzy.speed import get_speed


game = UI()
game.setup_game()

game.speed_setup(20, 0)
counter = 0


while True:
    game.loop()

    # print (time, light_dis, stone_dis)
    # print (get_speed(time, light_dis, stone_dis))
    start = timer.time()    
    time, light_dis, stone_dis = game.get_environment_info()
    speed = get_speed(time, light_dis, stone_dis)
    print (speed, light_dis)
    calc_time = timer.time() - start
    game.speed_setup(speed, calc_time)
