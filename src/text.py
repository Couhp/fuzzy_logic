import pygame 

class Text(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        self.text = self.myfont.render(' ', False, (100, 100, 0))
        self.rect = [0, 0]
    
    def set_text (self, text, rect):
        self.text = self.myfont.render(text, False, (100, 100, 0))
        self.rect = rect
