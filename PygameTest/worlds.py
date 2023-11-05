import pygame

from arbor import *
from nixpeculus import *
from malleandor import *
from bitmaps.worlds import *
from write import *
from skinEditor import *
from screen import *
from ui import *

class Worlds(Screen):

    def __init__(self, player):
        super().__init__()
        pygame.display.set_caption("The World Stage")

        self.running = True
        self.tick = 0

        self.player = player

        self.worldlist = worlds
        self.planet_move_stage = None

        self.ui_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)

        self.planeswalking_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)
        self.planeswalking = 0

        try:
            self.run()
        except pygame.error:
            pass

    def draw_planet(self, bitmap, center, scale, top=WH/3):
        if bitmap == self.worldlist[3]:
            font = 3
        elif bitmap in self.worldlist[2:5]:
            font = 2
        else:
            font = 1
        write(
            self.win,
            bitmap.name,
            (center - writtenlen(bitmap.name)*font//2, WH / 3 - 25),
            [(40, 100, 20), (210, 200, 40), (200, 130, 40), (200, 40, 20), (220, 200, 40), (200, 130, 40), (200, 200, 200)][bitmap.i],
            font
        )
        for i, row in enumerate(bitmap.bitmap):
            for j, pixel in enumerate(row):
                if bitmap.colors[pixel] is not None:
                    left = center - (scale * 24)
                    pygame.draw.rect(self.win, bitmap.colors[pixel], [j*scale + left, i*scale + top, scale, scale])

    def draw_planets(self):
        if self.planet_move_stage is None:
            unsortedworldlist = list(enumerate(self.worldlist))
            worldlist = []
            start = True
            while len(unsortedworldlist) > 0:
                if start:
                    worldlist.append(unsortedworldlist.pop(0))
                else:
                    worldlist.append(unsortedworldlist.pop(-1))
                start = not start

            for i, world in worldlist:
                if self.planeswalking > 0 and i == 3:
                    self.draw_planet(
                        world,
                        WW * 2**(2 - 7 // 2),
                        5 + (255 - self.planeswalking) // 4,
                        WH/3 - (len(world)//2 * ((255 - self.planeswalking) // 4 + 1))
                    )
                elif self.planeswalking < 0 and i == 3:
                    self.draw_planet(
                        world,
                        WW * 2**(2 - 7 // 2),
                        5 - self.planeswalking // 4,
                        WH/3 - (len(world)//2 * (1 - self.planeswalking // 4))
                    )
                elif i < len(worldlist) / 2:
                    self.draw_planet(
                        world,
                        WW * 2**(i - 7 // 2 - 1),
                        i + 1
                    )
                else:
                    self.draw_planet(
                        world,
                        WW * (1 - 2**(7 // 2 - i - 1)),
                        len(worldlist) - i
                    )
        else:    
            unsortedworldlist = list(enumerate(self.worldlist))
            newunsortedworldlist = list(enumerate(self.worldlist))
            if self.planet_move_stage > 0:
                newunsortedworldlist = newunsortedworldlist[1:] + [newunsortedworldlist[0]]
            elif self.planet_move_stage < 0:
                newunsortedworldlist = [newunsortedworldlist[-1]] + newunsortedworldlist[:-1]
            
            worldlist = []
            newworldlist = []
            start = True
            while len(unsortedworldlist) > 0:
                if start:
                    worldlist.append(unsortedworldlist.pop(0))
                    newworldlist.append(newunsortedworldlist.pop(0))
                else:
                    worldlist.append(unsortedworldlist.pop(-1))
                    newworldlist.append(newunsortedworldlist.pop(-1))
                start = not start

            index = 0
            for old_i, old_world in worldlist:
                new_i = newworldlist[index][0]
                world = newworldlist[index][1]
                i = old_i + ((new_i - old_i) * ((5 - abs(self.planet_move_stage)) / 5))
                if i < len(worldlist) / 2:
                    center = WW * 2**(i - int(len(worldlist) / 2) - 1)
                    self.draw_planet(
                        world,
                        center,
                        round(i + 1)
                    )
                else:
                    center = WW * (1 - 2**(int(len(worldlist) / 2) - i - 1))
                    self.draw_planet(
                        world,
                        center,
                        round(len(worldlist) - i)
                    )
                index += 1

    def mouseButtonUp(self, event):
        if event.pos[0] >= 10 and event.pos[1] >= 40 and event.pos[0] <= 48 and event.pos[1] <= 78:
            SkinEditor(self.player)#EquipmentScreen(self.player)
        elif event.pos[0] < WH - len(worlds) * 24:
            if self.worldlist[int(len(self.worldlist)/2) - 1] is not None and self.planet_move_stage is None:
                self.planet_move_stage = -1
        elif event.pos[0] > WH + len(worlds) * 24:
            if self.worldlist[int(len(self.worldlist)/2) + 1] is not None and self.planet_move_stage is None:
                self.planet_move_stage = 1
        elif self.planeswalking == 0 and event.pos[1] > WH/3 and event.pos[1] < WH/3 + 192:
            self.planeswalking = 255

    def run(self):
        while self.running:
            self.tick += 1
            self.win.fill(CLEAR)

            if self.planet_move_stage != None and self.tick % 5 == 0:
                if self.planet_move_stage > 0 and self.planet_move_stage < 4:
                    self.planet_move_stage += 1
                elif self.planet_move_stage >= 4:
                    self.planet_move_stage = None
                    self.worldlist = self.worldlist[1:] + [self.worldlist[0]]
                elif self.planet_move_stage < 0 and self.planet_move_stage > -4:
                    self.planet_move_stage -= 1
                elif self.planet_move_stage <= -4:
                    self.planet_move_stage = None
                    self.worldlist = [self.worldlist[-1]] + self.worldlist[:-1]
                else:
                    self.planet_move_stage = None

            if self.tick % 5 == 0:
                self.player.curIndex += 1
            write(self.win, self.player.name + " the " + self.player.playerclass, (10, 10), (255,255,255) if self.player.alignment == 1 else ALIGNMENT_COLORS[self.player.alignment][1], 2)
            self.player.idle()
            self.player.draw(self, Coord(-20, 0), 1)

            write(self.win, "Level " + str(self.player.get_level()), (940, 10), size=2)

            self.draw_planets()

            drawSoulEnergyBar(self)
            self.win.blit(self.ui_layer, (0, 0))

            if self.planeswalking > 0: # leaving
                self.planeswalking_layer.fill((251, 188, 50, 255-self.planeswalking))
                self.win.blit(self.planeswalking_layer, (0, 0))
                self.planeswalking -= 2
                if self.planeswalking <= 0:
                    self.planeswalking = 0
                    if self.worldlist[3].name == "Arbor": Arbor(self, self.player)
                    elif self.worldlist[3].name == "Tempestus": Tempestus(self, self.player)
                    elif self.worldlist[3].name == "Nixpeculus": Nixpeculus(self, self.player)
                    elif self.worldlist[3].name == "Tempus": Tempus(self, self.player)
                    elif self.worldlist[3].name == "Ardor": Ardor(self, self.player)
                    elif self.worldlist[3].name == "Malleandor": Malleandor(self, self.player)
                    elif self.worldlist[3].name == "Nilheld": Nilheld(self, self.player)
                    self.planeswalking = -255
            elif self.planeswalking < 0: # entering
                self.win.blit(self.planeswalking_layer, (0, 0))
                self.planeswalking_layer.fill((251, 188, 50, -self.planeswalking))
                self.planeswalking += 2
                if self.planeswalking >= 0:
                    self.planeswalking = 0

            if self.player.get_level() < 2:
                if self.worldlist[3].name == "Arbor": Arbor(self, self.player)
                elif self.worldlist[3].name == "Tempestus": Tempestus(self, self.player)
                elif self.worldlist[3].name == "Nixpeculus": Nixpeculus(self, self.player)
                elif self.worldlist[3].name == "Tempus": Tempus(self, self.player)
                elif self.worldlist[3].name == "Ardor": Ardor(self, self.player)
                elif self.worldlist[3].name == "Malleandor": Malleandor(self, self.player)
                elif self.worldlist[3].name == "Nilheld": Nilheld(self, self.player)

            if self.tick > TICKLIM:
                self.tick = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save()
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouseButtonUp(event)

            super().run()

        self.save()

    def save(self):
        self.player.save()
