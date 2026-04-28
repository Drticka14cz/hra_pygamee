import pygame
from utility import image_cut

class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super().__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image_cut("/assets/TilesetNature.png", 0, 13, 16, 16, 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


class Crystal(GameObject):
    def __init__(self, x, y, w, h):
        super().__init__(x, y, w, h)
        self.image = image_cut("/assets/TilesetNature.png", 0, 13, 16, 16, 5)
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
