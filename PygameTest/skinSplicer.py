import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from utilities import *
from bitmaps.temp import *
from bitmaps.noswordbackup import *
from write import *

class SkinSplicer():

    def __init__(self):
        self.win = pygame.display.set_mode((1440, 855), pygame.SRCALPHA)
        pygame.display.set_caption("The Skin Splicer")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.running = True

        self.curNum = 0
        self.erasing = False
        self.teardropping = False

        r, g, b = 0, 0, 0

        self.colors = {}
        for i in range(417):
            r += 36
            if r > 255:
                r = 0
                g += 36
                if g > 255:
                    g = 0
                    b += 36
                    if b > 255:
                        print("NUM TOO LARGE")
            self.colors[str(i)] = (r, g, b)

        self.run()

    def run(self):
        while self.running:
            self.win.fill(WHITE)

            for r in range(len(bitmaps)):
                pygame.draw.line(self.win, BLACK, (0, 80*r*4), (1320, 80*r*4), 1)
                for c in range(len(bitmaps[r])):
                    pygame.draw.line(self.win, BLACK, (100*c*4, 0), (100*c*4, 855), 1)
                    for y in range(80):
                        for x in range(100):
                            if bitmaps[r][c][y][x] != 0:
                                pygame.draw.rect(self.win, colors[bitmaps[r][c][y][x]] if type(bitmaps[r][c][y][x]) == int else self.colors[bitmaps[r][c][y][x]], (4*(100*c + x), 4*(80*r + y), 4, 4))

            write(self.win, str(self.curNum), (5, 5), self.colors[str(self.curNum)])

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_0:
                        self.curNum *= 10
                    elif event.key == pygame.K_1:
                        self.curNum *= 10
                        self.curNum += 1
                    elif event.key == pygame.K_2:
                        self.curNum *= 10
                        self.curNum += 2
                    elif event.key == pygame.K_3:
                        self.curNum *= 10
                        self.curNum += 3
                    elif event.key == pygame.K_4:
                        self.curNum *= 10
                        self.curNum += 4
                    elif event.key == pygame.K_5:
                        self.curNum *= 10
                        self.curNum += 5
                    elif event.key == pygame.K_6:
                        self.curNum *= 10
                        self.curNum += 6
                    elif event.key == pygame.K_7:
                        self.curNum *= 10
                        self.curNum += 7
                    elif event.key == pygame.K_8:
                        self.curNum *= 10
                        self.curNum += 8
                    elif event.key == pygame.K_9:
                        self.curNum *= 10
                        self.curNum += 9
                    elif event.key == pygame.K_BACKSPACE:
                        self.curNum = self.curNum // 10
                    elif event.key in [pygame.K_UP, pygame.K_RIGHT]:
                        self.curNum += 1
                    elif event.key in [pygame.K_DOWN, pygame.K_LEFT]:
                        self.curNum -= 1
                    elif event.key == pygame.K_e:
                        self.erasing = True
                    elif event.key == pygame.K_t:
                        self.teardropping = True

                    if self.curNum >= 415:
                        self.curNum = 414
                    if self.curNum < 0:
                        self.curNum = 0
                elif event.type == pygame.KEYUP:
                    self.erasing = False
                    self.teardropping = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    frame_coords = (
                        event.pos[0] // (4*100),
                        (event.pos[1]) // (4*80)
                    )
                    pixel_coords = (
                        (event.pos[0] - (frame_coords[0]*100*4))//4,
                        (event.pos[1] - (frame_coords[1]*80*4))//4
                    )
                    if bitmaps[frame_coords[1]][frame_coords[0]][pixel_coords[1]][pixel_coords[0]] != 0:
                        if self.erasing:
                            bitmaps[frame_coords[1]][frame_coords[0]][pixel_coords[1]][pixel_coords[0]] = original_bitmaps[frame_coords[1]][frame_coords[0]][pixel_coords[1]][pixel_coords[0]]
                        elif self.teardropping:
                            self.curNum = int(bitmaps[frame_coords[1]][frame_coords[0]][pixel_coords[1]][pixel_coords[0]])
                        else:
                            bitmaps[frame_coords[1]][frame_coords[0]][pixel_coords[1]][pixel_coords[0]] = str(self.curNum)

        self.quit()

    def quit(self):
        self.running = False
        pygame.quit()

        f = open('bitmaps/temp.py', 'w')
        f.write("colors = [BLACK, (211, 211, 211), (171, 171, 171), (248, 248, 248), (94, 94, 94), (125, 125, 125)]\n")

        f.write("bitmaps = [\n")
        for row in bitmaps:
            f.write("    [\n")
            for bitmap in row:
                f.write("        [\n")
                for line in bitmap:
                    f.write("            " + str(line).replace(" ", "") + ",\n")
                f.write("        ],\n")
            f.write("    ],\n")
        f.write("]\n")

if __name__ == "__main__":
    SkinSplicer()