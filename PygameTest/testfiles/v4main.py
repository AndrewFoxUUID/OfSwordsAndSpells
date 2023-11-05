import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random, shapely.geometry, shapely.ops
from scipy.spatial import Voronoi

class Main():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Version 4: Smooth Voronoi")
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
        self.debug = False

        self.map = [[(0, 0, 0, 0) for i in range(2160)] for i in range(250)]

        self.remap()

        self.run()

    def remap(self):
        # -- Generate Grid Points --
        point_arr = []
        for y in range(250, 511, 16):
            for x in range(0, 1009, 16):
                point_arr.append([random.randint(x+10, x+21), random.randint(y+10, y+21)])
        # -- Generate Voronoi Edges --
        vor = Voronoi(point_arr)
        lines = []
        for line in vor.ridge_vertices:
            if -1 not in line:
                lines.append(shapely.geometry.LineString(vor.vertices[line]))
        # -- Draw Voronoi Shapes --
        self.layer1.fill((0, 0, 0, 0))
        splitline = shapely.geometry.LineString([(-200, 250), (1200, 250)])
        for shape in shapely.ops.polygonize(lines):
            split = list(shapely.ops.split(shape, splitline))
            checkindex = 0
            if len(split) == 1:
                split = split[0]
                if split.exterior.coords[0][1] < 250:
                    continue
            else:
                while True:
                    if split[0].exterior.coords[checkindex][1] < split[1].exterior.coords[checkindex][1]:
                        split = split[1]
                        break
                    elif split[0].exterior.coords[checkindex][1] > split[1].exterior.coords[checkindex][1]:
                        split = split[0]
                        break
                    else:
                        checkindex += 1

            color = (22, 16, 32, 255)
            if split.centroid.y < 270:
                color = (106, 162, 34, 255)
            elif split.centroid.y < 290:
                color = (53, 119, 55, 255)
            elif split.centroid.y < 310:
                color = (33, 60, 63, 255)
            elif split.centroid.y < 340 or random.randint(0, 20 if split.centroid.y < 370 else 60) == 0:
                color = (45, 36, 61, 255)
            elif split.centroid.y < 380 or random.randint(0, 40) == 0:
                color = (33, 24, 46, 255)

            pygame.draw.polygon(self.layer1, color, list(split.exterior.coords))
        # -- Draw Shape Borders --
        if self.debug:
            for line in lines:
                pygame.draw.line(self.layer1, (0, 0, 0, 255), line.coords[0], line.coords[1], 2)

    def run(self):
        while self.running:
            self.win.fill((100, 140, 186, 255))
            self.tick += 1

            """
            Layer Borders
            250 to 260
            260 to 270
            270 to 280
            280 to 300
            300 to 350
            350 to 550
            """

            """
            Colors
            (106, 162, 34, 255)
            (53, 119, 55, 255)
            (33, 60, 63, 255)
            (45, 36, 61, 255)
            (33, 24, 46, 255)
            (22, 16, 32, 255)
            """

            self.win.blit(self.layer1, (self.x, self.y))

            if self.tick % 5 == 0:
                if self.left_held:
                    self.x += 5
                if self.up_held:
                    self.y += 5
                if self.right_held:
                    self.x -= 5
                if self.down_held:
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
                    elif event.key == pygame.K_0:
                        self.x, self.y = 0, 0
                    elif event.key == pygame.K_p:
                        self.debug = not self.debug
                        self.remap()

Main()