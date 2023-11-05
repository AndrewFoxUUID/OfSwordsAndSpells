import pygame
from images import Images

class Object(pygame.sprite.Sprite):

    def __init__(self, name, position):
        super().__init__()
        self.name = name
        self.image = Images.interactables[name]
        self.rect = (*position, self.image.get_width(), self.image.get_height())
        self.coords = position

    def draw(self, world):
        world.background_particle_layer.blit(self.image, self.coords)

    def __str__(self):
        return "OBJECT:" + self.name + ":" + str(self.coords).replace(' ', '')