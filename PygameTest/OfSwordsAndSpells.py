import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from player import Player
from write import *
from position_utilities import *
from worlds import Worlds
from newPlayer import NewPlayer
from utilities import *
from images import Images
from screen import *
from bitmaps.ui import *
from constants import *

class Game(Screen):

    def __init__(self):
        super().__init__()
        pygame.display.set_caption("Of Swords And Spells")

        self.running = True
        self.tick = 0

        self.open = False
        self.book_stage = 0
        self.direction = 1

        self.players = []
        if not os.path.exists("data/"):
            os.mkdir("data")
        for file in os.listdir("data"):
            if os.path.isdir(os.path.join("data", file)):
                self.players.append(Player(file))
        self.players.append("＋")
        self.left = 0

        try:
            self.run()
        except pygame.error:
            pass

    def mouseButtonUp(self, event):
        if event.pos[0] < 254 or event.pos[0] > 717 or event.pos[1] < 66 or event.pos[1] > 433:
            if event.pos[0] < WH and self.left > 1:
                self.left -= 2
                self.book_stage = 6
                self.direction = -1
            elif event.pos[0] >= WH and self.left + 2 < len(self.players):
                self.left += 2
                self.book_stage = 4
                self.direction = 1
        else:
            pos = self.left
            if event.pos[0] >= WH:
                if self.left + 1 < len(self.players):
                    pos += 1
                else:
                    return
            if self.players[pos] != '＋':
                Worlds(Player(self.players[pos].name))
            else:
                NewPlayer()

            self.open = False
            self.book_stage = 0
            self.direction = 1

            self.players = []
            if not os.path.exists("data/"):
                os.mkdir("data")
            for file in os.listdir("data"):
                if os.path.isdir(os.path.join("data", file)):
                    self.players.append(Player(file))
            self.players.append("＋")
            self.left = 0

    def run(self):
        while self.running:
            self.tick += 1
            self.win.fill(BLACK)

            self.win.blit(pygame.transform.scale(Images.menubooks[self.book_stage], (157*3, 160*3)), (WH - 157*3//2, 0))
            if self.open:
                if self.tick % 10 == 0:
                    if self.book_stage != 3:
                        self.book_stage += self.direction
                    if self.book_stage == 7:
                        self.book_stage = 3
                if self.book_stage == 3:
                    if self.left > 0:
                        for y, row in enumerate(right_arrow):
                            for x, item in enumerate(row[::-1]):
                                if item != 0:
                                    pygame.draw.rect(self.win, right_arrow_colors[item], (240 + x*4, 220 + y*4, 4, 4))

                    if self.players[self.left] != '＋':
                        self.players[self.left].die() if self.players[self.left].dead else self.players[self.left].idle()
                        if self.players[self.left].dead:
                            self.players[self.left].curIndex = 9
                        elif self.tick % 10 == 0:
                            self.players[self.left].curIndex += 1
                        self.players[self.left].draw(self, Coord(255, 125), 3)
                        font_size = 4
                        while font_size > 1 and writtenlen(self.players[self.left].name)*font_size > 170:
                            font_size -= 1
                        write(
                            self.win,
                            self.players[self.left].name,
                            (390-(writtenlen(self.players[self.left].name)*font_size//2), 325),
                            ALIGNMENT_COLORS[self.players[self.left].alignment][0],
                            font_size
                        )
                    else:
                        write(self.win, '＋', (365, 175), (50, 50, 50), 10)
                        write(self.win, "New Player", (305, 325), BLACK, 4)

                    if self.left + 1 < len(self.players):
                        if self.players[self.left+1] != '＋':
                            self.players[self.left+1].die() if self.players[self.left+1].dead else self.players[self.left+1].idle()
                            if self.players[self.left+1].dead:
                                self.players[self.left+1].curIndex = 9
                            elif self.tick % 10 == 5:
                                self.players[self.left+1].curIndex += 1
                            self.players[self.left+1].draw(self, Coord(485, 125), 3)
                            font_size = 4
                            while font_size > 1 and writtenlen(self.players[self.left+1].name)*font_size > 170:
                                font_size -= 1
                            write(
                                self.win,
                                self.players[self.left+1].name,
                                (615-(writtenlen(self.players[self.left+1].name)*font_size//2), 325),
                                ALIGNMENT_COLORS[self.players[self.left+1].alignment][0],
                                font_size
                            )

                            for y, row in enumerate(right_arrow):
                                for x, item in enumerate(row):
                                    if item != 0:
                                        pygame.draw.rect(self.win, right_arrow_colors[item], (746 + x*4, 220 + y*4, 4, 4))
                        else:
                            write(self.win, '＋', (585, 175), (50, 50, 50), 10)
                            write(self.win, "New Player", (530, 325), BLACK, 4)
                    
            elif self.tick % 10 == 0:
                self.book_stage += 1
                if self.book_stage == 3:
                    self.open = True

            if self.tick > TICKLIM:
                self.tick = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouseButtonUp(event)

            super().run()

        self.quit()

    def quit(self):
        self.running = False
        pygame.quit()

if __name__ == "__main__":
    Game()