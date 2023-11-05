import pygame
from math import sin
from random import randint, choice

from projectile import Projectile
from utilities import *
from write import *

class Particle(Projectile):

    def __init__(self, topleft, width, x_velocity, y_velocity, color, lifespan=-1):
        super().__init__(
            topleft,
            (width, width),
            x_velocity,
            y_velocity,
            lifespan,
            False,
            [],
            [],
            None
        )
        self.color = color

    def update(self, world):
        self.rect.left += self.x_velocity
        self.rect.top += self.y_velocity

        if self.rect.left < 0 or self.rect.right > TW:
            self.kill()
        elif self.rect.top < 0 or self.rect.bottom > TH:
            self.kill()
        elif self.lifespan > 0:
            self.lifespan -= 1
            if self.lifespan == 0:
                self.kill()

    def draw(self, world):
        pygame.draw.rect(world.background_particle_layer, self.color, self.rect)


class TextBounce(Particle):

    def __init__(self, topleft, text, color):
        super().__init__(topleft, writtenlen(text)*2, randint(-20, 20)/10, randint(-30, -10)/10, color)
        self.text = text

    def update(self, world):
        super().update(world)
        self.y_velocity += 0.2
        if self.y_velocity >= 2:
            self.kill()

    def draw(self, world):
        write(world.map_overlay_layer, self.text, self.rect.topleft, self.color, 2)


class StatusParticle(Particle):

    def __init__(self, topleft, start_color, end_color):
        self.lifetime = choice([-2, 2]) * randint(20, 30)
        self.start_vx = self.lifetime / 20
        super().__init__(topleft, 4, self.start_vx, randint(5, 10)/10, start_color)
        self.start_color = start_color
        self.end_color = end_color
        self.tick = 0

    def update(self, world):
        super().update(world)
        self.color = (
            int(self.start_color[0] + (self.end_color[0] - self.start_color[0]) * (self.tick/self.lifetime)),
            int(self.start_color[1] + (self.end_color[1] - self.start_color[1]) * (self.tick/self.lifetime)),
            int(self.start_color[2] + (self.end_color[2] - self.start_color[2]) * (self.tick/self.lifetime))
        )
        self.x_velocity -= self.start_vx / abs(self.start_vx) * 0.1
        self.tick += self.start_vx / abs(self.start_vx)
        if self.tick == self.lifetime:
            self.kill()

    def draw(self, world):
        pygame.draw.rect(world.foreground_particle_layer, self.color, self.rect)