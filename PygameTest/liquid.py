import pygame
from random import randint
from math import sin, pi

from position_utilities import *
from bitmaps.platformerTiles import *

class Liquid(pygame.sprite.Sprite):

    def __init__(self, coord, liquidtype='water'):
        super().__init__()
        self.coords = [coord]
        self.rect = pygame.Rect(coord[0], coord[1], 4, 4)
        self.type = liquidtype

        self.lines = []

    def contains(self, coord):
        return coord in self.coords

    def add(self, coord):
        self.coords.append(coord)
        if coord[0] < self.rect.left:
            self.rect.width += self.rect.left - coord[0]
            self.rect.left = coord[0]
        if coord[1] < self.rect.top:
            self.rect.height += self.rect.top - coord[1]
            self.rect.top = coord[1]
        if coord[0] + 4 > self.rect.right:
            self.rect.width += coord[0] + 4 - self.rect.right
        if coord[1] + 4 > self.rect.bottom:
            self.rect.height += coord[1] + 4 - self.rect.bottom

    def draw(self, world): # one above, two below
        surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        empty_light_height = self.rect.height//2 + (self.rect.height//2)%4 - 8
        # place below then above then below
        # if more than 8 pixels in empty_light_height, place top
        # if more than 14 pixels in empty_light_height, place bottom
        # if more than 18 pixels in empty_light_height, place top
        if len(self.lines) < 1 and empty_light_height >= 8: # (%width, pos)
            s, e = self.rect.width, 0
            for coord in self.coords:
                if coord[1] - self.rect.top == 8:
                    if coord[0] - self.rect.left < s:
                        s = coord[0] - self.rect.left
                    if coord[0] + 4 - self.rect.left > e:
                        e = coord[0] + 4 - self.rect.left
            w = int(randint(20, 40)/100 * (e - s))
            self.lines.append((w, randint(6, e - s - w - 6)))
        if len(self.lines) < 2 and empty_light_height >= 14:
            s, e = self.rect.width, 0
            for coord in self.coords:
                if coord[1] - self.rect.top == 4 + empty_light_height:
                    if coord[0] - self.rect.left < s:
                        s = coord[0] - self.rect.left
                    if coord[0] + 4 - self.rect.left > e:
                        e = coord[0] + 4 - self.rect.left
            w = int(randint(20, 40)/100 * (e - s))
            self.lines.append((w, randint(6, e - s - w - 6)))
        if len(self.lines) < 3 and empty_light_height >= 18:
            s, e = self.rect.width, 0
            for coord in self.coords:
                if coord[1] - self.rect.top == 12:
                    if coord[0] - self.rect.left < s:
                        s = coord[0] - self.rect.left
                    if coord[0] + 4 - self.rect.left > e:
                        e = coord[0] + 4 - self.rect.left
            w = int(randint(10, 20)/100 * (e - s))
            self.lines.append((w, randint(6, e - s - w - 6)))

        for coord in self.coords:
            if coord[1] == self.rect.top:
                pygame.draw.rect(surface, (98, 216, 217, 255), (coord[0] - self.rect.left, coord[1] - self.rect.top + 1, 4, 2))
                pygame.draw.rect(surface, (83, 163, 204, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top + 3, 4, 1))
                for i in range(4):
                    pygame.draw.rect(surface, (98, 216, 217, 255), (coord[0] + i - self.rect.left, coord[1] - self.rect.top + 1 - int(1.3*sin(pi*2/self.rect.width * (coord[0] + i + (world.tick)%self.rect.width))), 1, 2))
            elif coord[1] == self.rect.top + 4:
                pygame.draw.rect(surface, (83, 163, 204, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top, 4, 2))
                pygame.draw.rect(surface, (98, 216, 217, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top + 2, 4, 2))
            elif coord[1] >= self.rect.top + self.rect.height/2 + 4 and coord[1] < self.rect.top + self.rect.height/2 + 8:
                pygame.draw.rect(surface, (83, 163, 204, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top, 4, 2))
                pygame.draw.rect(surface, (43, 103, 192, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top + 2, 4, 2))
            elif coord[1] >= self.rect.top + self.rect.height/2:
                pygame.draw.rect(surface, (43, 103, 192, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top, 4, 4))
            else:
                pygame.draw.rect(surface, (83, 163, 204, 200), (coord[0] - self.rect.left, coord[1] - self.rect.top, 4, 4))

        if len(self.lines) >= 1:
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[0][1], 10, self.lines[0][0], 2))
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[0][1] - 2 - (world.tick%30)//3, 10, int(4 - ((world.tick%30-15)/11)**2), 2))
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[0][1] + self.lines[0][0] + (world.tick%30)//3, 10, int(4 - ((world.tick%30-15)/11)**2), 2))
        if len(self.lines) >= 2:
            pygame.draw.rect(surface, (43, 103, 192, 200), (self.lines[1][1], empty_light_height + 4, self.lines[1][0], 2))
            pygame.draw.rect(surface, (43, 103, 192, 200), (self.lines[1][1] - 2 - (world.tick%30)//3, empty_light_height + 4, int(4 - ((world.tick%30-15)/11)**2), 2))
            pygame.draw.rect(surface, (43, 103, 192, 200), (self.lines[1][1] + self.lines[1][0] + (world.tick%30)//3, empty_light_height + 4, int(4 - ((world.tick%30-15)/11)**2), 2))
        if len(self.lines) >= 3:
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[2][1], 14, self.lines[2][0], 2))
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[2][1] - 2 - (world.tick%30)//3, 14, int(4 - ((world.tick%30-15)/11)**2), 2))
            pygame.draw.rect(surface, (98, 216, 217, 200), (self.lines[2][1] + self.lines[2][0] + (world.tick%30)//3, 14, int(4 - ((world.tick%30-15)/11)**2), 2))

        world.map_overlay_layer.blit(surface, (self.rect.left, self.rect.top))

    def effect(self, target):
        if self.type == 'water':
            target.movementSpeed -= 1

    def __str__(self):
        return 'LIQUID:' + self.type + ':' + str([str(coord).replace(' ', '') for coord in self.coords]) + ':' + str([str(line).replace(' ', '') for line in self.lines])