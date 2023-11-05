import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random
from math import sin, pi
from write import write

class Main():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Version 1: Randomized Non-Periodic Sine Curve")
        self.win = pygame.display.set_mode((1000, 500), pygame.SRCALPHA)
        cursor = (
            "      XXX       ",
            "      X.X       ",
            "      X.X       ",
            "      X.X       ",
            "      XXX       ",
            "                ",
            "XXXXX XXX XXXXX ",
            "X...X X.X X...X ",
            "XXXXX XXX XXXXX ",
            "                ",
            "      XXX       ",
            "      X.X       ",
            "      X.X       ",
            "      X.X       ",
            "      XXX       ",
            "                ",
        )
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.layer1 = pygame.Surface((8640, 500), pygame.SRCALPHA)

        self.running = True
        self.x, self.y = 0, 0
        self.left_held, self.up_held, self.right_held, self.down_held = False, False, False, False
        self.tick = 0

        self.map = [[(0, 0, 0, 0) for i in range(4320)] for i in range(250)]

        self.variance = 0

        self.remap()

        self.run()

    def remap(self):
        self.variance = random.randint(0, 60)

        for x in range(4320):
            height = int(self.variance * (sin(0.0002*x) + sin(0.0001*pi*x)) + 125)
            for y in range(250):
                if y == height:
                    self.map[249-y][x] = (106, 162, 34, 255)
                elif y == height - 1:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*22 + [(53, 119, 55, 255)]*2)
                elif y == height - 2:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*19 + [(53, 119, 55, 255)]*5)
                elif y == height - 3:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*13 + [(53, 119, 55, 255)]*11)
                elif y == height - 4:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*7 + [(53, 119, 55, 255)]*17)
                elif y == height - 5:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*8 + [(53, 119, 55, 255)]*14 + [(33, 60, 63, 255)]*2)
                elif y == height - 6:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*8 + [(53, 119, 55, 255)]*12 + [(33, 60, 63, 255)]*4)
                elif y == height - 7:
                    self.map[249-y][x] = random.choice([(106, 162, 34, 255)]*4 + [(53, 119, 55, 255)]*8 + [(33, 60, 63, 255)]*12)
                elif y == height - 8:
                    self.map[249-y][x] = random.choice([(53, 119, 55, 255)]*3 + [(33, 60, 63, 255)]*21)
                elif y == height - 9:
                    self.map[249-y][x] = random.choice([(33, 60, 63, 255)]*17 + [(45, 36, 61, 255)]*2 + [(33, 24, 46, 255)]*5)
                elif y == height - 10:
                    self.map[249-y][x] = random.choice([(33, 60, 63, 255)]*8 + [(45, 36, 61, 255)]*4 + [(33, 24, 46, 255)]*12 + [(22, 16, 32, 255)]*1)
                elif y == height - 11:
                    self.map[249-y][x] = random.choice([(45, 36, 61, 255)]*7 + [(33, 24, 46, 255)]*13 + [(22, 16, 32, 255)]*4)
                elif y == height - 12:
                    self.map[249-y][x] = random.choice([(45, 36, 61, 255)]*7 + [(33, 24, 46, 255)]*9 + [(22, 16, 32, 255)]*8)
                elif y < height:
                    self.map[249-y][x] = (22, 16, 32, 255)

        self.layer1.fill((100, 140, 186, 255))
        for r, row in enumerate(self.map):
            for c, item in enumerate(row):
                try:
                    pygame.draw.rect(self.layer1, item, (c*2, r*2, 2, 2))
                except ValueError:
                    print(item)

    def run(self):
        while self.running:
            self.win.fill((100, 140, 186, 255))
            self.tick += 1

            """
            (106, 162, 34, 255)
            (53, 119, 55, 255)
            (33, 60, 63, 255)
            (45, 36, 61, 255)
            (33, 24, 46, 255)
            (22, 16, 32, 255)
            """

            self.win.blit(self.layer1, (self.x, self.y))

            write(self.win, str(self.variance), (10, 10))

            if self.tick % 5 == 0:
                if self.left_held:
                    self.x += 5
                elif self.up_held:
                    self.y += 5
                elif self.right_held:
                    self.x -= 5
                elif self.down_held:
                    self.y -= 5
                        
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x += 5
                        self.left_held = True
                    elif event.key == pygame.K_UP:
                        self.y += 5
                        self.up_held = True
                    elif event.key == pygame.K_RIGHT:
                        self.x -= 5
                        self.right_held = True
                    elif event.key == pygame.K_DOWN:
                        self.y -= 5
                        self.down_held = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left_held = False
                    elif event.key == pygame.K_UP:
                        self.up_held = False
                    elif event.key == pygame.K_RIGHT:
                        self.right_held = False
                    elif event.key == pygame.K_DOWN:
                        self.down_held = False
                    elif event.key == pygame.K_RETURN:
                        self.remap()

Main()