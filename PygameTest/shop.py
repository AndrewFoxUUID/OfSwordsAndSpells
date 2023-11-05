import pygame

from utilities import *
from position_utilities import *
from ui import *

class Shop():
    def __init__(self, world):
        self.world = world
        self.player = world.player
        self.win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        pygame.display.set_caption("Item Shop")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))
        
        self.equipment_menu_layer = pygame.Surface((WW//6, 480), pygame.SRCALPHA)
        self.spellbook_layer = pygame.Surface((WW//6 + 1, 480), pygame.SRCALPHA)
        self.ui_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)

        self.player_pos = Coord(100, 450 - world.player.rect.height)
        self.dx = 0
        self.dy = 0

        self.solids = pygame.sprite.Group()
        for rect in [pygame.Rect(0, 450, WW, 50), pygame.Rect(-10, 0, 10, WH), pygame.Rect(WW, 0, 10, WH)]:
            sprite = pygame.sprite.Sprite()
            sprite.rect = rect
            sprite.ramp = 'none'
            self.solids.add(sprite)

        self.running = True
        self.tick = 0
        self.paused = False
        self.planeswalking = 0

        redrawSpellSlots(self)

        self.run()

    def run(self):
        while self.running:
            self.win.fill((107, 102, 131))

            redrawUI(self)
            redrawSpells(self)
            redrawEquipmentMenu(self)

            pygame.draw.rect(self.win, (210, 127, 106), (0, 450, WW, 50))

            for i in range(300**2):
                a = i**2

            self.player_pos.x += self.dx
            self.player_pos.y += self.dy

            self.player.update(self)
            self.player.draw(self)

            pygame.display.update()

            self.tick += 1
            if self.tick > TICKLIM:
                self.tick = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.player.keydown(self, event.key)
                #elif event.type == pygame.KEYUP:
                #    self.onKeyUp(event.key)
                #elif event.type == pygame.MOUSEBUTTONDOWN:
                #    self.onMousePress(event)
                #elif event.type == pygame.MOUSEBUTTONUP:
                #    self.onMouseUp(event)
                #elif event.type == pygame.MOUSEMOTION:
                #    self.onMouseMotion(event)