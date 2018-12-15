import pygame 

class Light(pygame.sprite.Sprite):
    def __init__(self, list_image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        index = 1
        self.lights = list_image_file
        self.image = pygame.image.load(self.lights[index]).convert_alpha()
        self.rect = self.image.get_rect(topleft=location)
        self.time = 0

    def time_pass() :
        self.time += 1
    


    
