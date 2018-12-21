import pygame 

class Car(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.original_image = pygame.image.load(image_file).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=location)
        self.center = self.rect.center
        self.loc = (0,0)


    def rotate(self, angle) :
        self.image = pygame.transform.rotate(self.original_image, angle)
        # Get a new rect and pass the center of the previous rect. This
        # will keep the car centered.
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def move_to(self, location) :
        self.rect.topleft = [location[0] - self.center[0], location[1] - self.center[1]]
        self.loc = location
        # self.rect.topleft = location
    
    def move(self, top, left) :
        # print (self.rect)
        top = top - self.center[0]
        left = left - self.center[1]
        self.rect.topleft = [self.rect.topleft[0] + top, self.rect.topleft[1] + left]
        self.loc = (top, left)