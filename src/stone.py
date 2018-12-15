import pygame 

class Stone(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.original_image = pygame.image.load(image_file).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=location)
        self.center = self.rect.center

    def move_to(self, location) :
        top = location[0] - self.center[0]
        left = location[1] - self.center[1]
        self.rect.topleft = [self.rect.topleft[0] + top, self.rect.topleft[1] + left]
