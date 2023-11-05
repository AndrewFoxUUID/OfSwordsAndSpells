import pygame

from utilities import *
from constants import *

class Screen():

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        self.win = pygame.Surface((WW, WH), pygame.SRCALPHA)
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

    def run(self):
        self.display.blit(self.win, (0, 0))
        pygame.display.update()

    def encrypt(self, val):
        return ''.join([chr(ord(char)+i%20) for i, char in enumerate(val.replace("(0,0,0)", "<>"))])

    def decrypt(self, val):
        return ''.join([chr(ord(char)-i%20) for i, char in enumerate(val)]).replace("<>", "(0,0,0)")