import pygame
from utility import *
from settings import *
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 100 
        self.y = 100
        self.spritesheet = pygame.image.load("assets/sprites/walk.png").convert_alpha()
        self.image= image_cut(self.spritesheet, 0, 0, 16,16, 5)
        self.rect = self.image.get_rect(midbottom = (self.x, self.y))
        self.speed =5
        self.lives = 3
        self.nesmrtelnost = False
        self.čas_nesmrtelnosti = 0
        self.index = 0
        self.elapsed_time = 0
    
    def animation(self, direction):
        frame_count = 4
        self.index +=0.1
        
        if self.index > frame_count:#aby to neslo do nekonecna
            self.index = 0
        self.image = image_cut(self.spritesheet,direction,int(self.index), 16,16,5)
    def update(self, monsters, clock):
        self.elapsed_time += clock.get_time()
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.animation(1)
            if self.rect.top > 0:
                self.rect.move_ip(0,-self.speed)
        if key[pygame.K_s]:
            self.animation(0)
            if self.rect.bottom < SCREEN_HEIGHT:
                self.rect.move_ip(0,self.speed)
        if key[pygame.K_a]:
            self.animation(2)
            if self.rect.left > 0:
                self.rect.move_ip(-self.speed, 0)
        if key[pygame.K_d]:
            self.animation(3)
            if self.rect.right < SCREEN_WIDTH:
                self.rect.move_ip(self.speed,0)
        
        if pygame.sprite.spritecollide(self, monsters, False):
            if self.nesmrtelnost == False:
                self.lives -=1
                print(f"Hráč má {self.lives}")
                self.nesmrtelnost = True
                self.čas_nesmrtelnosti = self.elapsed_time
            
            
            
         
        if self.nesmrtelnost == True and self.elapsed_time >= self.čas_nesmrtelnosti+500:
            self.nesmrtelnost = False
            print(f"Může zkapat")

            
       
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)