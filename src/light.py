import pygame 

class Light(pygame.sprite.Sprite):
    def __init__(self, list_image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        red, green, yellow = list_image_file
        self.image = pygame.image.load(red).convert_alpha()
        self.rect = self.image.get_rect(topleft=location)
        self.time = 0

    def time_pass() :
        self.time += 1
    
    

    
