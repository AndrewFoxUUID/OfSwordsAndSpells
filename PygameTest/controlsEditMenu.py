import pygame

from bitmaps.ui import *
from write import *
from position_utilities import *
from utilities import *

class ControlsEditMenu():

    def __init__(self, player):
        pygame.init()
        self.win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        pygame.display.set_caption("Edit Controls")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.player = player
        self.pressed = None
        self.selected = None
        self.running = True

        self.lengths = [0, 0, 0]
        for key in player.keybinds:
            if key[1] != '-':
                self.lengths[0] += 1
            elif key[:2] == 'm-':
                self.lengths[1] += 1
            elif key[:2] == 'p-':
                self.lengths[2] += 1

        self.start = 0

        self.run()

    def run(self):
        while self.running:
            self.win.fill((200, 200, 200))

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

            start = 46 + self.start
            write(self.win, "General Controls", Coord(10, start), RED, 4)
            start += 30
            for key in self.player.keybinds:
                if key[1] != '-':
                    string = key.replace("_", " ") + "\t"
                    for j in range(((self.win.get_width()//3 - 88 - writtenlen(string)) % 2)):
                        string += '\t'
                    for j in range((self.win.get_width()//3 - 88 - writtenlen(string)) // 2):
                        string += '.'
                    write(self.win, string, Coord(10, start), (200, 20, 20), 3)
                    string = ' "' + pygame.key.name(self.player.keybinds[key]) + '"'
                    if key == self.selected:
                        string = ' >' + pygame.key.name(self.player.keybinds[key]) + '<'
                    write(self.win, string, Coord(self.win.get_width() - 255, start), (20, 20, 200) if key == self.selected else BLACK, 3)
                    start += 25
            start += 20
            write(self.win, "Map View Controls", Coord(10, start), RED, 4)
            start += 30
            for key in self.player.keybinds:
                if key[:2] == 'm-':
                    string = key[2:].replace("_", " ") + "\t"
                    for j in range(((self.win.get_width()//3 - 88 - writtenlen(string)) % 2)):
                        string += '\t'
                    for j in range((self.win.get_width()//3 - 88 - writtenlen(string)) // 2):
                        string += '.'
                    write(self.win, string, Coord(10, start), (200, 20, 20), 3)
                    string = ' "' + pygame.key.name(self.player.keybinds[key]) + '"'
                    if key == self.selected:
                        string = ' >' + pygame.key.name(self.player.keybinds[key]) + '<'
                    write(self.win, string, Coord(self.win.get_width() - 255, start), (20, 20, 200) if key == self.selected else BLACK, 3)
                    start += 25
            start += 20
            write(self.win, "Tile View Controls", Coord(10, start), RED, 4)
            start += 30
            for key in self.player.keybinds:
                if key[:2] == 'p-':
                    string = key[2:].replace("_", " ") + "\t"
                    for j in range(((self.win.get_width()//3 - 88 - writtenlen(string)) % 2)):
                        string += '\t'
                    for j in range((self.win.get_width()//3 - 88 - writtenlen(string)) // 2):
                        string += '.'
                    write(self.win, string, Coord(10, start), (200, 20, 20), 3)
                    string = ' "' + pygame.key.name(self.player.keybinds[key]) + '"'
                    if key == self.selected:
                        string = ' >' + pygame.key.name(self.player.keybinds[key]) + '<'
                    write(self.win, string, Coord(self.win.get_width() - 255, start), (20, 20, 200) if key == self.selected else BLACK, 3)
                    start += 25

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.selected = None
                    if event.pos[0] >= self.win.get_width()-35 and event.pos[0] <= self.win.get_width()-10 and event.pos[1] >= 10 and event.pos[1] <= 34:
                        self.pressed = 'x'
                    elif event.pos[0] >= self.win.get_width() - 255 and event.pos[0] <= self.win.get_width() and event.pos[1] >= 76 and event.pos[1] <= 196 + 25*len(self.player.keybinds.keys()):
                        if event.pos[1] > 76 and event.pos[1] < 76 + 25*self.lengths[0]:
                            self.selected = list(self.player.keybinds.keys())[(event.pos[1]-76)//25]
                        elif event.pos[1] > 126 + 25*self.lengths[0] and event.pos[1] < 126 + 25*self.lengths[0] + 25*self.lengths[1]:
                            self.selected = list(self.player.keybinds.keys())[(event.pos[1]-126)//25]
                        elif event.pos[1] > 176 + 25*self.lengths[0] + 25*self.lengths[1] and event.pos[1] < 176 + 25*self.lengths[0] + 25*self.lengths[1] + 25*self.lengths[2]:
                            self.selected = list(self.player.keybinds.keys())[(event.pos[1]-176)//25]
                elif event.type == pygame.MOUSEBUTTONUP:
                    if self.pressed == 'x':
                        self.running = False
                    self.pressed = None
                elif event.type == pygame.MOUSEWHEEL:
                    self.start += event.y * 4
                    if self.start > 0:
                        self.start = 0
                    if self.start < -start:
                        self.start = -start
                elif event.type == pygame.KEYDOWN:
                    if self.selected is not None:
                        self.player.keybinds[self.selected] = event.key
                        self.selected = None