import pygame 

class Light(pygame.sprite.Sprite):
    def __init__(self, list_image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        pygame.font.init()
        self.lights = list_image_file
        ### light :
        # 0 ---> green
        # 1 ---> yellow
        # 2 ---> red

        self.image = pygame.image.load(self.lights[0]).convert_alpha()
        self.status = 0
        self.rect = self.image.get_rect(topleft=location)
        self.center = self.rect.center
        self.time = 0
        self.round_time = 0
        self.status_list = [0 for i in range(10)] + [1 for i in range(5)] + [2 for i in range(10)]

        self.myfont = pygame.font.SysFont('Comic Sans MS', 50)
        self.text = self.myfont.render(str(self.get_time()), False, (100, 100, 0))
        
      
        self.position = self.rect.topleft

    def time_pass(self, unit):
        self.time += unit
        if self.round_time != self.get_time():
            self.text = self.myfont.render(str(self.get_time()), False, (100, 100, 0))
            self.round_time = self.get_time()
        status = round(self.time) % 25
        if self.status_list[status] != self.status:
            self.status = self.status_list[status]
            self.image = pygame.image.load(self.lights[self.status]).convert_alpha()
            

    def get_time (self):
        time = round(self.time) % 25
        if time - 15 > 0:
            return time - 15
        if time - 10 > 0:
            return time - 10
        else :
            return time


    def light_status(self):
        time = round(self.time) % 25
        return time

    def get_rect(self):
        return (self.rect.topleft[0] + self.center[0], self.rect.topleft[1] + self.center[1])
    

    def move_to(self, location) :
        self.rect.topleft = [location[0] - self.center[0], location[1] - self.center[1]]
        self.text_rect = [self.rect[0] + 20, self.rect[1]]

    
