import pygame

from bitmaps.ui import *
from tile import *
from position_utilities import Coord
from constants import *

class EquipmentScreen():
    
    def __init__(self, player):
        pygame.init()
        self.win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        pygame.display.set_caption(player.name + "'s Equipment")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.player = player

        self.pressed = None

        self.tick = 0

        self.running = True
        self.run()

    def drawEquipment(self, bitmap, position: Coord):
        offset = (self.win.get_width()//3 - 60*4) // 4
        if position.x == 0:
            startx = offset
        elif position.x == 1:
            startx = self.win.get_width()//6 - 10*4
        else:
            startx = self.win.get_width()//3 - offset - 20*4
        starty = offset + position.y * (20*4 + offset)
        if type(bitmap) == list:
            colors = placeholder_colors
        else:
            colors = bitmap.colors
        for r, row in enumerate(bitmap):
            for c, item in enumerate(row):
                if item != 0:
                    pygame.draw.rect(self.win, colors[item], (startx + 4*c, starty + 4*r, 4, 4))

    def drawEquipmentMenu(self):
        pygame.draw.rect(self.win, (77, 74, 78), (0, 0, self.win.get_width()//3, self.win.get_height()))
        pygame.draw.rect(self.win, (71, 48, 59), (self.win.get_width()//3 - 3, 0, 3, self.win.get_height()))

        self.drawEquipment(martial_placeholder, Coord(0, 0))
        self.drawEquipment(magic_placeholder, Coord(1, 0))
        self.drawEquipment(shield_placeholder, Coord(2, 0))

        self.drawEquipment(helm_placeholder, Coord(0, 1))
        self.drawEquipment(breastplate_placeholder, Coord(1, 1))
        self.drawEquipment(boots_placeholder, Coord(2, 1))

        self.drawEquipment(ring_placeholder, Coord(0, 2))
        self.drawEquipment(charm_placeholder, Coord(1, 2))
        self.drawEquipment(gauntlet_placeholder, Coord(2, 2))

        self.drawEquipment(scroll_placeholder, Coord(0, 3))
        self.drawEquipment(item_placeholder, Coord(1, 3))
        self.drawEquipment(item_placeholder, Coord(2, 3))

    def run(self):
        while self.running:
            self.tick += 1

            self.win.fill(CLEAR)

            if self.pressed == "x":
                xbtn = x_button_pressed
                xcolors = x_button_pressed_colors
            else:
                xbtn = x_button
                xcolors = x_button_colors
            startx = self.win.get_width()-35
            starty = 34 - len(xbtn)
            for r, row in enumerate(xbtn):
                for c, item in enumerate(row):
                    if item != 0:
                        pygame.draw.rect(self.win, xcolors[item], (startx + c, starty + r, 1, 1))

            tiles[0][0].draw(self.win, Coord(340, 200), 10, True)

            if self.tick % 30 == 0:
                self.player.curIndex += 1
            self.player.draw(self, Coord(100, -225), 8)

            self.drawEquipmentMenu()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected = None
                    if event.pos[0] >= self.win.get_width()-35 and event.pos[0] <= self.win.get_width()-10 and event.pos[1] >= 10 and event.pos[1] <= 34:
                        self.pressed = 'x'
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.pressed == 'x':
                        self.running = False
                    self.pressed = None

            if self.tick > TICKLIM:
                self.tick = 0