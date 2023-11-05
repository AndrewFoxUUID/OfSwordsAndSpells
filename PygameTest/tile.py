import os, pygame, importlib
from random import randint, choice
from math import sin, pi
from noise import pnoise1
from liquid import Liquid

from world import World
from position_utilities import *
import enemy as Enemies
from maptile import *
from constants import *
from object import Object

class Tile(World):
    
    def __init__(self, game, player, position):
        super().__init__(game, player)

        self.position = position
        self.type = importlib.import_module(f"data.{player.name}.worlds.{type(game).__name__.lower()}.worlddata").mapsave[position.y][position.x]
        self.overlay = None
        if self.type.find('-') != -1:
            self.overlay = self.type[self.type.find('-')+1:]
            self.type = self.type[:self.type.find('-')]
        self.colorkey = COLORKEYS[TILE_COMPOSITION_MAP[self.type][0]]

        self.background1 = [[]]
        self.background1_image = pygame.Surface((TW, WW), pygame.SRCALPHA)
        self.background1_image.fill(CLEAR)
        self.background2 = [[]]
        self.background2_image = pygame.Surface((TW, WH), pygame.SRCALPHA)
        self.background2_image.fill(CLEAR)
        self.solids = [[]]

        try:
            loading = True
            loadDir = os.path.join('data', player.name, 'worlds', type(game).__name__.lower(), 'tileViews', f'{position.x}_{position.y}')
            if not os.path.exists(loadDir): os.mkdir(loadDir)
            loadStages = ['background1', 'background2', 'solids', 'interactables', 'entities']
            loadStage = loadStages[0]
            loadFile = None

            for stage in loadStages[1:]:
                open(os.path.join(loadDir, stage), 'r')

            loadFile = open(os.path.join(loadDir, loadStage), 'r')
            x, y = 0, 0
            line = self.decrypt(loadFile.readline()[:-1]).split(', ')

            text = ''
            prev_percent = -1
            progress = 0
            end = 0
            while loading:
                if line and x < len(line) and line[x] != '':
                    if loadStage == 'background1': # (4320, WH)
                        item = [int(i) for i in line[x][2:-2].split(',')]
                        self.background1[-1].append(item)
                        pygame.draw.rect(self.background1_image, item, (x*2, y*2, 2, 2))
                        text = 'Skyscape'
                        end = 2160000
                    elif loadStage == 'background2': # (TW//4, 125)
                        item = [int(i) for i in line[x][2:-2].split(',')]
                        self.background2[-1].append(item)
                        pygame.draw.rect(self.background2_image, item, (x*4, y*4, 4, 4))
                        text = 'Mountainscape'
                        end = 270000
                    elif loadStage == 'solids': # (TW//4, 240)
                        item = [int(i) for i in line[x][2:-2].split(',')]
                        self.solids[-1].append(item)
                        pygame.draw.rect(self.solids_layer, item, (x*4, y*4, 4, 4))
                        text = 'Landscape'
                        end = 518400
                    elif loadStage == 'interactables':
                        args = line[x].split(':')
                        if args[0] == 'LIQUID':
                            coords = [[int(val) for val in coord[2:-2].split(',')] for coord in args[2][1:-1].split(', ')]
                            l = Liquid(coords[0], args[1])
                            for coord in coords[1:]:
                                l.add(coord)
                            l.lines = [[int(val) for val in lineargs[2:-2].split(',')] for lineargs in args[3][1:-1].split(', ')]
                            self.interactables.add(l)
                        elif args[0] == 'OBJECT':
                            o = Object(args[1], (*(int(val) for val in args[2][1:-1].split(',')),))
                            self.interactables.add(o)
                        text = 'Interactables'
                        end = progress + 1 # obviously not accurate, but should be fast enough not to matter
                    elif loadStage == 'entities':
                        pass
                    x += 1
                    progress += 1
                elif line and line != ['']:
                    x = 0
                    y += 1
                    progress += 1
                    line = self.decrypt(loadFile.readline()[:-1]).split(', ' if loadStage in ['background1', 'background2', 'solids'] else '?')
                    if loadStage == 'background1': self.background1.append([])
                    elif loadStage == 'background2': self.background2.append([])
                    elif loadStage == 'solids': self.solids.append([])
                else:
                    stage = loadStages.index(loadStage)
                    prev_percent = 0
                    progress = 0
                    if stage < len(loadStages) - 1:
                        loadStage = loadStages[stage+1]
                        loadFile = open(os.path.join(loadDir, loadStage), 'r')
                        line = self.decrypt(loadFile.readline()[:-1]).split(', ' if loadStage in ['background1', 'background2', 'solids'] else '?')
                        x, y = 0, 0
                    else:
                        loading = False

                if prev_percent != int(round(progress/end, 2)*100):
                    prev_percent = int(round(progress/end, 2)*100)
                    self.win.fill(BLACK)
                    write(self.win, "Loading " + text + " ... (" + str(prev_percent) + "%)", (20, 20), WHITE, 4)
                    self.display.blit(self.win, (0, 0))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            self.game.save()
                            self.player.save()
                            pygame.quit()

        except Exception as e:
            self.background1 = [[CLEAR for x in range(TW//2)] for y in range(WH)]
            self.background2 = [[CLEAR for x in range(TW//4)] for y in range(WH//4)]

            extrema = [(0, WH/4)]
            for x in range(TW//4):
                if (self.mountainwave(x-1) < self.mountainwave(x) and self.mountainwave(x) > self.mountainwave(x+1)) or (self.mountainwave(x-1) > self.mountainwave(x) and self.mountainwave(x) < self.mountainwave(x+1)):
                    extrema.append((x, self.mountainwave(x)))
            extrema.append((TW//4, WH/4))

            heights = []
            for i in range(len(extrema)-1):
                x_dif = extrema[i+1][0] - extrema[i][0]
                y_dif = extrema[i+1][1] - extrema[i][1]
                heights += [extrema[i][1] + j/x_dif * y_dif + self.mountainwave(extrema[i][0] + j)/2 - 188 for j in range(x_dif)]

            self.solids = [[CLEAR for x in range(TW//4)] for y in range(240)]

            args = TILE_COMPOSITION_MAP[self.type].copy()
            if self.overlay is not None:
                overlay_args = TILE_COMPOSITION_MAP[self.overlay]
                for terrain_piece in overlay_args[0]:
                    if terrain_piece in args[1]:
                        args[1][terrain_piece] += overlay_args[0][terrain_piece]
                    else:
                        args[1][terrain_piece] = overlay_args[0][terrain_piece]
                args[2] += overlay_args[1]
                args[3] = overlay_args[2]
                args[4] += overlay_args[3]
            self.boss = False

            x, y = 0, 0
            height = int(args[1]['intensity'] * (sin(0.0002*x) + sin(0.0001*pi*x)) + 62)
            light_green = height - 5
            dark_green = height - 7

            if player.name == "TEST":
                enemy = Enemies.Dummy((500, 0))
                self.enemies.add(enemy)
                self.sprites.add(enemy)

            loadStage = 'background1'
            text = 'Generating Skyscape'
            prev_percent = -1
            progress = 0
            end = 2160000
            while loading:
                if loadStage == 'background1':
                    startType = randint(0, y + 20)
                    top_left = (min(x + randint(0, 7), 4315), min(y + randint(0, 7), 495))
                    
                    if startType < 4:
                        self.background1[top_left[1]][top_left[0]] = (142, 194, 192, 255)
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2, 2, 2))
                    elif startType < 8:
                        self.background1[top_left[1]][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1]][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0] + 1] = (142, 194, 192, 255)
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2 + 2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2 + 2, 2, 2))
                    elif startType < 10:
                        self.background1[top_left[1] + 1][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1]][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0] + 2] = (142, 194, 192, 255)
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2 + 2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2 + 2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2 + 4, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2 + 2, 2, 2))
                    elif startType < 11:
                        self.background1[top_left[1]][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1]][top_left[0] + 2] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0] + 2] = (142, 194, 192, 255)
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2 + 4, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2 + 2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2 + 4, 2, 2))
                    elif startType < 12:
                        self.background1[top_left[1] + 2][top_left[0]] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0] + 1] = (142, 194, 192, 255)
                        self.background1[top_left[1]][top_left[0] + 2] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 1][top_left[0] + 2] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 3][top_left[0] + 2] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 4][top_left[0] + 2] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0] + 3] = (142, 194, 192, 255)
                        self.background1[top_left[1] + 2][top_left[0] + 4] = (142, 194, 192, 255)
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2, top_left[1]*2 + 4, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 2, top_left[1]*2 + 4, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2 + 2, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2 + 6, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 4, top_left[1]*2 + 8, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 6, top_left[1]*2 + 4, 2, 2))
                        pygame.draw.rect(self.background1_image, (142, 194, 192, 255), (top_left[0]*2 + 8, top_left[1]*2 + 4, 2, 2))

                    y += 10
                    progress += 10
                    if y >= WH:
                        y = 0
                        x += 10
                        progress += 10
                    if x >= 4320:
                        x, y = 0, 0
                        progress = 0
                        end = 270000
                        loadStage = 'background2'
                        text = 'Raising Mountains'
                elif loadStage == 'background2':
                    if y*4 > WH - heights[x]:
                        self.background2[y][x] = (33, 36, 58, 255)
                        pygame.draw.rect(self.background2_image, (33, 36, 58, 255), (x*4, y*4, 4, 4))

                    y += 1
                    progress += 1
                    if y >= 125:
                        y = 0
                        x += 1
                        progress += 1
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        end = 518400
                        loadStage = 'solids'
                        text = 'Landscaping'

                elif loadStage == 'solids':
                    if y > 240 - height:
                        if y < 240 - light_green:
                            self.solids[y][x] = (193, 198, 88, 255)
                            pygame.draw.rect(self.solids_layer, (193, 198, 88, 255), (x*4, y*4, 4, 4))
                        elif y < 240 - dark_green:
                            self.solids[y][x] = (105, 124, 62, 255)
                            pygame.draw.rect(self.solids_layer, (105, 124, 62, 255), (x*4, y*4, 4, 4))
                        else:
                            self.solids[y][x] = (29, 15, 27, 255)
                            pygame.draw.rect(self.solids_layer, (29, 15, 27, 255), (x*4, y*4, 4, 4))

                    y += 1
                    progress += 1
                    if y >= 240:
                        y = 0
                        x += 1
                        progress += 1
                        height = int(args[1]['intensity'] * (sin(0.0002*x) + sin(0.0001*pi*x)) + 62)
                        light_green = height - (sin(0.5*x) + sin(0.25*pi*x) + 5)
                        dark_green = height - (sin(x) + sin(0.5*pi*x) + 7)
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        end = 518400
                        loadStage = 'dirt'
                        text = 'Texturizing'

                elif loadStage == 'dirt':
                    if randint(0, 15) == 0:
                        self.generateShape(x + randint(2, 7), y + randint(2, 7), randint(2, 6), bool(randint(0, 1)), (58, 35, 54, 255))
                    
                    x += 10
                    progress += 10
                    if x + 10 >= TW//4:
                        x = 0
                        y += 10
                        progress += 1
                    if y + 10 >= 240:
                        x, y = 0, 0
                        start, finish = -1, -1
                        progress = 0
                        end = TW//4
                        loadStage = 'water'
                        text = 'Watering the Ground'

                elif loadStage == 'water':
                    pond_frequency = 2 # temp
                    pond_width = 60 # temp

                    if x <= finish:
                        for i in range(top - self.getTop(x)):
                            self.solids[top-i-1][x] = CLEAR
                            pygame.draw.rect(self.solids_layer, CLEAR, (x*4, (top - i - 1)*4, 4, 4))
                        for i in range(int(abs(radius**2 - (x - start - radius)**2)**0.5)//2):
                            water_obj.add((x*4, (top + i)*4))
                            self.solids[top + i][x] = (29, 15, 27, 254) if i > 0 else CLEAR
                            pygame.draw.rect(self.solids_layer, self.solids[top + i][x], (x*4, (top + i)*4, 4, 4))
                    elif randint(0, 1080//pond_frequency) == 0:
                        start = x
                        finish = x + pond_width * (1 + randint(-20, 20)/100)
                        radius = (finish - start)/2

                        top = self.getTop(x)
                        water_obj = Liquid((x*4 + 4, top*4))
                        self.interactables.add(water_obj)
                    
                    x += 1
                    progress = x
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        end = TW//4
                        loadStage = 'grass'
                        text = 'Growing Grass'
                
                elif loadStage == 'grass':
                    bottom_grass_height = int(10*pnoise1(x*10 + 0.1) - 1)
                    top_grass_height = int(12*pnoise1(x*20 + 0.1) - 1)
                    if bottom_grass_height > 0:
                        top = self.getTop(x)
                        for i in range(bottom_grass_height):
                            self.solids[top-i-1][x] = (149, 161, 75, 254)
                            pygame.draw.rect(self.solids_layer, (149, 161, 75, 254), (x*4, (top - i - 1)*4, 4, 4))
                    if top_grass_height > 0:
                        top = self.getTop(x)
                        for i in range(bottom_grass_height):
                            self.solids[top-i-1][x] = (204, 208, 117, 254)
                            pygame.draw.rect(self.solids_layer, (204, 208, 117, 254), (x*4, (top - i - 1)*4, 4, 4))

                    x += 1
                    progress += 1
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        end = TW//4
                        loadStage = 'rocks'
                        text = 'Dropping Rocks'

                elif loadStage == 'rocks':
                    rockChance = 100 # temp

                    if randint(0, rockChance) == 0:
                        for i in range(randint(5, 15)):
                            height = int(abs(pnoise1((x + i + 0.1)/WW)*20))
                            for j in range(height):
                                self.solids[self.getTop(x)-1][x] = (140, 142, 171, 255)
                                pygame.draw.rect(self.solids_layer, (140, 142, 171, 255), (x*4, (self.getTop(x))*4, 4, 4))
                            x += 1
                            if x >= TW//4:
                                break

                    x += 1
                    progress += 1
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        end = TW//4
                        loadStage = 'trees'
                        text = 'Planting Trees'

                elif loadStage == 'trees':
                    treeChance = 100 # temp

                    if randint(0, treeChance) == 0:
                        self.interactables.add(Object('tree' + str(randint(0, 3)), (x*4 - 94, self.getTop(x)*4-192)))

                    x += 1
                    progress += 1
                    if x >= TW//4:
                        x, y = 0, 0
                        progress = 0
                        loading = False

                if prev_percent != int(round(progress/end, 2)*100):
                    prev_percent = int(round(progress/end, 2)*100)
                    self.win.fill(BLACK)
                    write(self.win, text + " ... (" + str(prev_percent) + "%)", (20, 20), WHITE, 4)
                    self.display.blit(self.win, (0, 0))
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            self.game.save()
                            self.player.save()
                            pygame.quit()

        self.mask = pygame.mask.from_surface(self.solids_layer, 254)

        while self.running:
            self.run()

        self.save()
        self.game.save()
        self.player.save()
   
    def mountainwave(self, x):
        return 50 * (sin(0.02*x) + sin(0.01*pi*x) + sin(0.01*x) + 7.5)

    def generateShape(self, x, y, size, direction, color):
        self.drawSquare(x, y, size, color)
        newsize = randint(size - 1, size)
        if direction:
            if randint(0, 1) == 0:
                self.drawSquare(x - 1, y - 1, newsize, color)
            if randint(0, 1) == 0:
                self.drawSquare(x + 1 + size - newsize, y + 1 + size - newsize, newsize, color)
        else:
            if randint(0, 1) == 1:
                self.drawSquare(x - 1, y + 1 + size - newsize, newsize, color)
            if randint(0, 1) == 1:
                self.drawSquare(x + 1 + size - newsize, y - 1, newsize, color)

        for i in range(size):
            if randint(0, 1) == 0:
                radius = size + 2*randint(2, 4)
                xpoint = randint(-radius//2, radius//2)
                ypoint = randint(-1, 1) * (radius**2 - xpoint**2)**0.5
                self.drawSquare(x + int(xpoint), y + int(ypoint), randint(1, 2), color)

        if size > 2 and randint(0, 1) == 0:
            self.generateShape(x+2, y+2, size-2, not direction, (85, 69, 97, 255))

    def drawSquare(self, x, y, size, color):
        for i in range(size):
            for j in range(size):
                if x+j >= 0 and y+i >= 0 and x+j < TW//4 and y+i < 240 and self.solids[y+i][x+j] in [(29, 15, 27, 255), (58, 35, 54, 255)]:
                    self.solids[y+i][x+j] = color
                    pygame.draw.rect(self.solids_layer, color, ((x+j)*4, (y+i)*4, 4, 4))

    def getTop(self, x):
        for y in range(240):
            if self.solids[y][x][3] == 255:
                return y

    def drawBackground(self):
        self.background_layer.fill(self.colorkey['background_top'])
        center = (
            self.top_left.x + 2000/3,
            self.top_left.y + 240
        )
        self.background_layer.blit(
            self.background1_image,
            (
                WW/3 - self.background1_image.get_width()/2 - self.top_left.x/8,
                center[1] - self.background1_image.get_height()/2 - (center[1] - 960) / 32 + 50 - self.top_left.y
            )
        )
        self.background_layer.blit(
            self.background2_image,
            (
                WW/3 - self.background2_image.get_width()/2 - self.top_left.x/4,
                center[1] - self.background2_image.get_height()/2 - (center[1] - 960) / 16 + 50 - self.top_left.y
            )
        )

    def run(self):
        super().run()

    def save(self):
        dir = os.path.join('data', self.player.name, 'worlds', type(self.game).__name__.lower(), 'tileViews', f'{self.position.x}_{self.position.y}')
        saving = True
        stages = ['background1', 'background2', 'solids', 'interactables', 'entities']
        stage = 0
        f = open(os.path.join(dir, 'background1'), 'w')
        lines = self.background1
        line = 0
        progress = 0
        totallines = len(self.background1) + len(self.background2) + len(self.solids) + len(self.interactables)
        last_percent = -1

        while saving:
            if line < len(lines):
                if stage < 3:
                    f.write(self.encrypt(str([str(c).replace(' ', '') for c in lines[line]])[1:-1]) + '\n')
                elif stage == 3:
                    f.write(self.encrypt(str(lines[line])) + '\n')
                line += 1
                progress += 1
            else:
                f.close()
                if stage + 1 >= len(stages):
                    saving = False
                else:
                    line = 0
                    stage += 1
                    progress += 1
                    f = open(os.path.join(dir, stages[stage]), 'w')
                    if stage == 1:
                        lines = self.background2
                    elif stage == 2:
                        lines = self.solids
                    elif stage == 3:
                        lines = list(self.interactables)
                    else:
                        lines = []

            if int(round(progress / totallines, 2)*100) > last_percent:
                last_percent = int(round(progress / totallines, 2)*100)
                self.win.fill(BLACK)
                write(self.win, "Saving ... (" + str(last_percent) + "%)", (20, 20), WHITE, 4)
                self.display.blit(self.win, (0, 0))
                pygame.display.update()
                for event in pygame.event.get():
                    pass
