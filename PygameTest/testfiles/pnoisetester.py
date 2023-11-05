import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, random, numpy
from math import sin, pi
from write import write
from noise import pnoise2
from scipy.spatial import Voronoi

class Main():

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Noise Field: pnoise2(x*7, y*7)")#, octaves=10, persistence=0.4, lacunarity=6.0)")
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

        self.remap()

        self.run()

    def remap(self):
        noise_map = []
        noises = []
        for y in range(250):
            noise_map.append([])
            for x in range(500):
                noise_map[-1].append(pnoise2(x/500*7 - 0.5, y/250*7 - 0.5, octaves=2, persistence=3.0, lacunarity=1.0))#, octaves=10, persistence=0.4, lacunarity=6.0))
                noises.append(pnoise2(x/500*7 - 0.5, y/250*7 - 0.5, octaves=2, persistence=3.0, lacunarity=1.0))#, octaves=10, persistence=0.4, lacunarity=6.0))

        self.layer1.fill((0, 0, 0, 0))
        maxval = max(noises)
        minval = min(noises)
        for y in range(250):
            for x in range(500):
                try:
                    color = int(255 * abs((noise_map[y][x]-minval)/(maxval-minval)))
                    if color > 255:
                        color = 255
                    elif color < 0:
                        color = 0
                except Exception as e:
                    color = 0
                pygame.draw.rect(self.layer1, (color, color, color), (x*2, y*2, 2, 2))
                #pygame.draw.rect(self.layer1, (0, 0, 0, 255) if color < 80 else (255, 255, 255, 255), (x*2, y*2, 2, 2))

        #self.draw_voronoi()

    def draw_voronoi(self):
        point_arr = numpy.zeros([900, 2], numpy.uint16)

        for i in range(900):
            point_arr[i][0] = numpy.uint16(random.randint(0, 1600))
            point_arr[i][1] = numpy.uint16(random.randint(0, 900))

        vor = Voronoi(point_arr)

        for indx_pair in vor.ridge_vertices:

            if -1 not in indx_pair:

                start_pos = vor.vertices[indx_pair[0]]
                end_pos = vor.vertices[indx_pair[1]]

                pygame.draw.line(self.layer1, (255, 0, 0, 255), start_pos/2, end_pos/2)

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