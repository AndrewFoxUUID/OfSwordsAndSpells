import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random
from math import pi, sin, sqrt
from noise import pnoise2

class Main():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Version 5: Shapes")
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
        self.layer2 = pygame.Surface((8640, 500), pygame.SRCALPHA)

        self.running = True
        self.x, self.y = 0, 0
        self.left_held, self.up_held, self.right_held, self.down_held = False, False, False, False
        self.tick = 0
        self.debug = False

        self.remap()

        self.run()

    def mountainwave(self, x):
        return 50 * (sin(0.02*x) + sin(0.01*pi*x) + sin(0.01*x) + 7.5)

    def remap(self):
        self.map = [[(0, 0, 0, 0) for i in range(2160)] for i in range(125)]
        self.background = [[(0, 0, 0, 0) for i in range(2160)] for i in range(125)]

        self.variance = random.randint(0, 60)

        for x in range(2160):
            height = int(self.variance * (sin(0.0002*x) + sin(0.0001*pi*x)) + 62) # Eventually will be a piecewise, using the old stretch length system, but replacing flat stretches and ramps with a random graph type (sin, flat, -abs, -sin)
            for y in range(125):
                light_green = height - random.randint(4, 8)
                medium_green = light_green - random.randint(1, 3)
                dark_green = medium_green - random.randint(3, 5)
                if y > 125 - height:
                    if y < 125 - light_green:
                        self.map[y][x] = (106, 162, 34, 255)
                    elif y < 125 - medium_green:
                        self.map[y][x] = (53, 119, 55, 255)
                    elif y < 125 - dark_green:
                        self.map[y][x] = (33, 60, 63, 255)
                    else:
                        self.map[y][x] = (22, 16, 32, 255)

        for i in range(100):
            self.generateShape(random.randint(0, 2159), random.randint(0, 124), random.randint(2, 6), random.choice([True, False]), (33, 24, 46, 255))
            #self.shapeBuilder(random.randint(0, 2159), random.randint(0, 124), random.choice([0, 0, 0, 1, 1, 2]))

        self.layer1.fill((100, 140, 186, 255))
        for r, row in enumerate(self.map):
            for c, item in enumerate(row):
                pygame.draw.rect(self.layer1, item, (c*4, r*4, 4, 4))

        # -- Background --

        extrema = [(0, 125)]
        for x in range(2160):
            if (self.mountainwave(x-1) < self.mountainwave(x) and self.mountainwave(x) > self.mountainwave(x+1)) or (self.mountainwave(x-1) > self.mountainwave(x) and self.mountainwave(x) < self.mountainwave(x+1)):
                extrema.append((x, self.mountainwave(x)))
        extrema.append((2160, 125))

        heights = []
        for i in range(len(extrema)-1):
            x_dif = extrema[i+1][0] - extrema[i][0]
            y_dif = extrema[i+1][1] - extrema[i][1]
            heights += [extrema[i][1] + j/x_dif * y_dif + self.mountainwave(extrema[i][0] + j)/2 - 188 for j in range(x_dif)]

        noise_map = []
        for y in range(125):
            noise_map.append([])
            for x in range(2160):
                noise_map[-1].append(pnoise2(x/500*7 - 0.5, y/250*7 - 0.5, octaves=2, persistence=6.0, lacunarity=6.0))

        for x in range(0, 8640, 4):
            for y in range(0, 500, 4):
                if y > 500 - heights[x//4]:
                    #if noise_map[y//4][x//4] > 0.2:
                    #    self.background[y//4][x//4] = (101, 139, 139, 255)
                    #elif noise_map[y//4][x//4] > -0.05:
                    #    self.background[y//4][x//4] = (58, 73, 96, 255)
                    #else:
                    self.background[y//4][x//4] = (33, 36, 58,255)

        self.layer2.fill((100, 140, 186, 255))
        for r, row in enumerate(self.background):
            for c, item in enumerate(row):
                pygame.draw.rect(self.layer2, item, (c*4, r*4, 4, 4))

    def generateShape(self, x, y, size, direction, color):
        self.drawSquare(x, y, size, color)
        newsize = random.randint(size - 1, size)
        if direction:
            if random.randint(0, 1) == 0:
                self.drawSquare(x - 1, y - 1, newsize, color)
            if random.randint(0, 1) == 0:
                self.drawSquare(x + 1 + size - newsize, y + 1 + size - newsize, newsize, color)
        else:
            if random.randint(0, 1) == 1:
                self.drawSquare(x - 1, y + 1 + size - newsize, newsize, color)
            if random.randint(0, 1) == 1:
                self.drawSquare(x + 1 + size - newsize, y - 1, newsize, color)

        # (xpoint)^2 + (ypoint)^2 = (size+8)^2
        for i in range(size):
            if random.randint(0, 1) == 0:
                radius = size + random.choice(range(4, 8, 2))
                xpoint = random.randint(-radius//2, radius//2)
                ypoint = random.choice([-1, 1]) * sqrt(radius**2 - xpoint**2)
                self.drawSquare(x + int(xpoint), y + int(ypoint), random.randint(1, 2), (33, 24, 46, 255))

        if size > 2 and random.randint(0, 1) == 0:
            self.generateShape(x+2, y+2, size-2, not direction, (45, 36, 61, 255))

    def drawSquare(self, x, y, size, color):
        for i in range(size):
            for j in range(size):
                if x+i >= 0 and y+j >= 0 and x+i < len(self.map[0]) and y+j < len(self.map) and self.map[y+j][x+i] not in [(0, 0, 0, 0), (106, 162, 34, 255), (53, 119, 55, 255), (33, 60, 63, 255)]:
                    self.map[y+j][x+i] = color

    def shapeBuilder(self, x, y, level, probability=4):
        color = [(33, 24, 46, 255), (45, 36, 61, 255), (88, 67, 90, 255)][level]
        self.drawSquare(x, y, 1, color)
        if random.randint(0, probability) == 0:
            self.shapeBuilder(x-1, y, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x-1, y, level-1)
        if random.randint(0, probability+2) == 0:
            self.shapeBuilder(x-1, y-1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x-1, y-1, level-1)
        if random.randint(0, probability) == 0:
            self.shapeBuilder(x, y-1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x, y-1, level-1)
        if random.randint(0, probability+2) == 0:
            self.shapeBuilder(x+1, y-1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x+1, y-1, level-1)
        if random.randint(0, probability) == 0:
            self.shapeBuilder(x+1, y, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x+1, y, level-1)
        if random.randint(0, probability+2) == 0:
            self.shapeBuilder(x+1, y+1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x+1, y+1, level-1)
        if random.randint(0, probability) == 0:
            self.shapeBuilder(x, y+1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x, y+1, level-1)
        if random.randint(0, probability+2) == 0:
            self.shapeBuilder(x-1, y+1, level, probability+2)
        elif level > 0:
            self.shapeBuilder(x-1, y+1, level-1)

    def run(self):
        while self.running:
            self.win.fill((100, 140, 186, 255))
            self.tick += 1

            """
            Colors
            (106, 162, 34, 255)
            (53, 119, 55, 255)
            (33, 60, 63, 255)

            (88, 67, 90, 255)
            (45, 36, 61, 255)
            (33, 24, 46, 255)
            (22, 16, 32, 255)
            """

            self.win.blit(self.layer2, (self.x, self.y))
            self.win.blit(self.layer1, (self.x, self.y))

            if self.tick % 5 == 0:
                if self.left_held:
                    self.x += 10
                if self.up_held:
                    self.y += 10
                if self.right_held:
                    self.x -= 10
                if self.down_held:
                    self.y -= 10
                        
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x += 10
                        self.left_held = True
                    elif event.key == pygame.K_UP:
                        self.y += 10
                        self.up_held = True
                    elif event.key == pygame.K_RIGHT:
                        self.x -= 10
                        self.right_held = True
                    elif event.key == pygame.K_DOWN:
                        self.y -= 10
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
                    elif event.key == pygame.K_0:
                        self.x, self.y = 0, 0
                    elif event.key == pygame.K_p:
                        self.debug = not self.debug
                        self.remap()

Main()