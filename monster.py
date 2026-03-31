import pygame
from utility import *
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self,name,  speed, x, y, spritesheet):
        super().__init__()
        self.x = x
        self.y = y
        self.style = spritesheet
        self.name = name
        self.index = 0
        self.speed = speed
        if spritesheet == True:
            self.spritesheet = pygame.image.load("assets/sprites/lizard.png").convert_alpha()
            self.image= image_cut(self.spritesheet, 0, 0, 16,16, 5)
        else:
            self.idle = pygame.image.load("assets/sprites/monsta.png").convert_alpha()
            self.idle  = pygame.transform.rotozoom(self.idle,0,4)
            self.run_1 = pygame.image.load("assets/sprites/monsta_run1.png").convert_alpha()
            self.run_1 = pygame.transform.rotozoom(self.run_1,0,4)
            self.run_2 = pygame.image.load("assets/sprites/monsta_run2.png").convert_alpha()
            self.run_2 = pygame.transform.rotozoom(self.run_2,0,4)
            self.images = [self.idle, self.run_1, self.run_2]
        
            self.image = self.images[self.index]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        

    def animation(self):
        if self.style == True:
            frame_count = 4
            self.index +=0.1
        
            if self.index > frame_count:#aby to neslo do nekonecna
                self.index = 0
            self.image = image_cut(self.spritesheet,direction,int(self.index), 16,16,5)#místo direction jde dát 0 a půjde doleva, příště musím fixnout

            print("a")
        else:
            self.index +=0.1 #0,1 pro nižší rychlost
            if self.index > len(self.images):#aby to neslo do nekonecna
                self.index = 0
            self.image = self.images[int(self.index)]#vykreslení
    def update(self):
        
        self.rect.right += self.speed
        if self.rect.right >= SCREEN_WIDTH:
            self.speed *= -1
            print(f"Prava {self.name}")
        elif self.rect.left <= 0:
            self.speed *=-1
            print(f"Leva {self.name}")
        self.animation()
    def draw(self, screen):
        screen.blit(self.image, self.rect)