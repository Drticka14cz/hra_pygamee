import pygame
from utility import image_cut

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sheet = pygame.image.load("assets/TilesetNature.png").convert_alpha()
        self.image = image_cut(self.sheet, 0, 14, 16, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


class Crystal(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.image = image_cut(self.sheet, 0, 14, 16, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
class Crystal_2(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.image = image_cut(self.sheet, 1, 14, 16, 16, 3)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))