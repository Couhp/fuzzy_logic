import pygame 
from src.car import Car
from src.background import Background
from src.light import Light
from src.text import Text
from src.stone import Stone

class UI:

    def __init__(self):
        ## INIT GAME
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1400, 700))

        ## INIT OBJECT
        self.transaction = Transaction()
        self.text = Text()
        self.background = Background('image/single_central.png', [0,0])
        self.stone = Stone("image/stone.png", [0,0])
        self.car = Car('image/car.png', [0, 0])
        self.light = Light(['image/red.png', 'image/yellow.png', 'image/green.png'], [100,200])

        ## BLIT
        self.screen.blit(self.background.image, self.background.rect)
        self.screen.blit(self.text.text, self.text.rect)
        self.screen.blit(self.car.image, self.car.rect)
        self.screen.blit(self.light.image, self.light.rect)
        self.screen.blit(self.light.text, self.light.text_rect)

        pygame.display.flip()


    def update_display () :
        self.screen.blit(self.background.image, self.background.rect)
        self.screen.blit(self.text.text, self.text.rect)
        self.screen.blit(self.car.image, self.car.rect)
        self.screen.blit(self.light.image, self.light.rect)
        self.screen.blit(self.stone.image, self.stone.rect)
        self.screen.blit(self.light.text, self.light.text_rect)
        pygame.display.update()
        return

    
    def setup_game (self):
        while True:
            flag = False
            self.text.set_text(msg, [100, 100])
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

    self.start_point = get_point("Select begin position")
    self.end_point = get_point("Select end position")
    self.stone_pos = get_point("Select stone position")
    self.text.set_text('', [100, 100])
    self.stone.move_to(stone_pos)