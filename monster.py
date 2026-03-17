import pygame
from utility import *
from settings import *

class Monster(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 450
        self.idle = pygame.image.load("assets/sprites/monsta.png").convert_alpha()
        self.idle  = pygame.transform.rotozoom(self.idle,0,4)
        self.run_1 = pygame.image.load("assets/sprites/monsta_run1.png").convert_alpha()
        self.run_1 = pygame.transform.rotozoom(self.run_1,0,4)
        self.run_2 = pygame.image.load("assets/sprites/monsta_run2.png").convert_alpha()
        self.run_2 = pygame.transform.rotozoom(self.run_2,0,4)
        self.images = [self.idle, self.run_1, self.run_2]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.idle.get_rect(midbottom=(self.x, self.y))
        self.speed = 1

    def animation(self):
       
        self.index +=0.1 #0,1 pro nižší rychlost
        if self.index > len(self.images):#aby to neslo do nekonecna
            self.index = 0
        self.image = self.images[int(self.index)]#vykreslení
    def update(self):
        
        self.rect.right += self.speed
        if self.rect.right >= SCREEN_WIDTH:
            self.speed *= -1
            print("awdawdad")
        elif self.rect.left <= 0:
            self.speed *=-1
            print("acip")
        self.animation()
    def draw(self, screen):
        screen.blit(self.image, self.rect)