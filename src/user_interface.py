import pygame 
from src.car import Car
from src.background import Background
from src.light import Light
from src.text import Text
from src.stone import Stone
import sys
sys.path.append("src")
from src.transaction import Transaction

class UI:

    def __init__(self):
        ## INIT GAME
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1400, 700))

        ## INIT OBJECT
        self.transaction = Transaction()
        self.text = Text()
        self.background = Background('image/raw_map.png', [0,0])
        self.stone = Stone("image/stone.png", [0,0])
        self.car = Car('image/car.png', [0, 0])
        self.light = Light(['image/green.png', 'image/yellow.png', 'image/red.png'], [300,300])
        self.light.position =  self.transaction.find_nearest_node(self.light.get_rect())
        self.stop_flag = False
        ## BLIT
        self.screen.blit(self.background.image, self.background.rect)
        self.screen.blit(self.light.image, self.light.rect)
        self.screen.blit(self.light.text, self.light.text_rect)

        pygame.display.flip()


    def set_text (self, text):
        self.text.set_text(str(text), (0,0))

    def update_display (self) :
        self.screen.blit(self.background.image, self.background.rect)
        self.screen.blit(self.text.text, self.text.rect)
        self.screen.blit(self.car.image, self.car.rect)
        self.screen.blit(self.light.image, self.light.rect)
        self.screen.blit(self.stone.image, self.stone.rect)
        self.screen.blit(self.light.text, self.light.text_rect)
        pygame.display.update()
        return

    
    def setup_game (self):
        def get_point(msg):
            while True:
                flag = False
                self.text.set_text(msg, [10, 10])
                ev = pygame.event.get()
                self.update_display()
                for event in ev:
                # handle MOUSEBUTTONUP
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        flag = True
                if flag:
                    return pos

        self.start_point = self.transaction.find_nearest_node(get_point("Select begin position"))
        self.end_point = self.transaction.find_nearest_node(get_point("Select end position"))
        self.stone_pos = self.transaction.find_nearest_node(get_point("Select stone position"))
        print (self.start_point, self.end_point, self.stone_pos)
        self.text.set_text('', [100, 100])
        self.stone.move_to(self.stone_pos)
        self.path, self.angles = self.transaction.find_path(start=self.start_point, end=self.end_point)

        self.car.move_to(self.start_point)


    def speed_setup(self, speed, calc_time):
        if speed < 1:
            self.stop_flag = True
            return 
        else:
            speed = round(35.0 - speed)
            time = speed / 1000
            self.delay = speed
            self.time_light = time + calc_time


    def get_environment_info(self):
        time = self.light.light_status()
        light_distance = self.transaction.distance(self.car.loc, self.light.position)
        stone_distance = self.transaction.distance(self.car.loc, self.stone.position)

        return (time, light_distance, stone_distance)



    def loop(self):
        node = self.path[0]
        angle = self.angles[0]

        if not self.stop_flag:
            self.car.move_to(list(node))
            self.car.rotate(angle)

            self.path = self.path[1:]
            self.angles = self.angles[1:]
        self.update_display()        
        pygame.time.delay(self.delay)
        self.light.time_pass(self.time_light)
        self.stop_flag = False



###
# Time unit in this game is 20ms ~ normal, 
#                           10ms ~ fast
#                           30ms ~ slow 
# light                     0.02 ~ normal
#                           0.01 ~ fast
#                           0.03 ~ slow
