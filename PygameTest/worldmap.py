import pygame, importlib

import enemy as Enemies
from utilities import *
from utilityclasses import *
from ui import *
from button import *
from controlsEditMenu import *
from maptile import *
from screen import *
from tile import *

class WorldMap(Screen):

    def __init__(self, game, player):
        super().__init__()
        self.game = game
        #pygame.display.set_caption(["Arbor", "Tempus", "Nixpeculus", "Ardor", "Tempestus", "Malleandor", "???"][worldtype])

        self.player = player

        self.map_layer = pygame.Surface((TW, TW), pygame.SRCALPHA)
        self.map_overlay_layer = pygame.Surface((TW, TW), pygame.SRCALPHA)
        self.equipment_menu_layer = pygame.Surface((WW//6, 480), pygame.SRCALPHA)
        self.spellbook_layer = pygame.Surface((WW//6 + 1, 480), pygame.SRCALPHA)
        self.ui_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)
        self.planeswalking_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)
        self.overlay_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)

        self.equipment_holders = pygame.sprite.Group()
        for r in range(6):
            for c in range(2):
                self.equipment_holders.add(EquipmentHolder(c, r))

        self.spells = pygame.sprite.Group()
        for i in range(10):
            self.spells.add(SpellUI(i))

        self.hovered = None

        self.paused = False
        self.running = True
        self.mapChange = True

        self.tick = 0

        self.planeswalking = 255

        redrawSpellSlots(self)

        self.moved = False

    def outlineTile(self, coord: ScreenCoord, color):
        coord = coord.get_topleft()
        points = [(coord.x+16+2*i,coord.y-2) for i in range(16)]
        points += [
            (coord.x+14,coord.y),
            (coord.x+12,coord.y+2),
            (coord.x+12,coord.y+4),
            (coord.x+10,coord.y+6),
            (coord.x+8,coord.y+8),
            (coord.x+8,coord.y+10),
            (coord.x+6,coord.y+12),
            (coord.x+6,coord.y+14),
            (coord.x+4,coord.y+16),
            (coord.x+2,coord.y+18),
            (coord.x+2,coord.y+20),
            (coord.x,coord.y+22),
            (coord.x,coord.y+24),
            (coord.x,coord.y+26), # -2
            (coord.x+48,coord.y),
            (coord.x+50,coord.y+2),
            (coord.x+50,coord.y+4),
            (coord.x+52,coord.y+6),
            (coord.x+54,coord.y+8),
            (coord.x+54,coord.y+10),
            (coord.x+56,coord.y+12),
            (coord.x+56,coord.y+14),
            (coord.x+58,coord.y+16),
            (coord.x+60,coord.y+18),
            (coord.x+60,coord.y+20),
            (coord.x+62,coord.y+22),
            (coord.x+62,coord.y+24),
            (coord.x+62,coord.y+26), # +64
            (coord.x,coord.y+28),
            (coord.x+2,coord.y+30),
            (coord.x+2,coord.y+32),
            (coord.x+4,coord.y+34),
            (coord.x+6,coord.y+36),
            (coord.x+6,coord.y+38),
            (coord.x+8,coord.y+40),
            (coord.x+8,coord.y+42),
            (coord.x+10,coord.y+44),
            (coord.x+12,coord.y+46),
            (coord.x+12,coord.y+48),
            (coord.x+14,coord.y+50),
            (coord.x+14,coord.y+52),
            (coord.x+62,coord.y+28),
            (coord.x+60,coord.y+30),
            (coord.x+60,coord.y+32),
            (coord.x+58,coord.y+34),
            (coord.x+56,coord.y+36),
            (coord.x+56,coord.y+38),
            (coord.x+54,coord.y+40),
            (coord.x+54,coord.y+42),
            (coord.x+52,coord.y+44),
            (coord.x+50,coord.y+46),
            (coord.x+50,coord.y+48),
            (coord.x+48,coord.y+50),
            (coord.x+48,coord.y+52)
        ]
        points += [(coord.x+16+2*i,coord.y+54) for i in range(16)]

        for point in points:
            pygame.draw.rect(self.map_overlay_layer, color, (point[0], point[1], 2, 2))

    def onKeyDown(self, key):
        self.player.keydown(self, key)

    def onKeyUp(self, key):
        if self.planeswalking == 0:
            if not self.paused:
                if key == self.player.keybinds['m-zoom_in'] and self.ps < 5:
                    self.ps += 1
                elif key == self.player.keybinds['m-zoom_out'] and self.ps > 2:
                    self.ps -= 1
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-up_left'] and self.player_coords.x >= 1 and self.player_coords.y >= 1:
                    self.player.flip = True
                    self.player_coords.x -= 1
                    self.player_coords.y -= 1
                    self.hovered = None
                    self.moved = True
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-down_left'] and self.player_coords.x >= 1 and self.player_coords.y < len(self.map) - 1:
                    self.player.flip = True
                    self.player_coords.x -= 1
                    self.player_coords.y += 1
                    self.hovered = None
                    self.moved = True
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-up_right'] and self.player_coords.x < len(self.map[0]) - 1 and self.player_coords.y >= 1:
                    self.player.flip = False
                    self.player_coords.x += 1
                    self.player_coords.y -= 1
                    self.hovered = None
                    self.moved = True
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-down_right'] and self.player_coords.x < len(self.map[0]) - 1 and self.player_coords.y < len(self.map) - 1:
                    self.player.flip = False
                    self.player_coords.x += 1
                    self.player_coords.y += 1
                    self.hovered = None
                    self.moved = True
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-up'] and self.player_coords.y >= 2:
                    self.player_coords.y -= 2
                    self.hovered = None
                    self.moved = True
                elif (not self.moved or self.player.get_level() > 1) and key == self.player.keybinds['m-down'] and self.player_coords.y < len(self.map) - 2:
                    self.player_coords.y += 2
                    self.hovered = None
                    self.moved = True
                elif key == self.player.keybinds['m-enter']:
                    self.moved = False
                    self.planeswalking = -255

    def onMousePress(self, event):
        if self.planeswalking == 0:
            if event.button == 1:
                if self.paused:
                    for button in self.buttons:
                        button.focused = button.rect.collidepoint(event.pos)
                else:
                    if event.pos[0] > WW//6 and event.pos[0] < 5000//6:
                        screen_coords = ScreenCoord(self, event.pos[0] - WW//6, event.pos[1])
                        
                        if screen_coords.x > 0 and screen_coords.x < (WW*4)//6 and screen_coords.y > 0 and screen_coords.y < 440:
                            map_coords = ScreenCoord(self, screen_coords.x + self.player_coords.x*48, screen_coords.y + self.player_coords.y*28).map_coords()
                            if map_coords == self.player_coords:
                                self.moved = False
                                self.planeswalking = -255
                            elif self.player.get_level() > 1 and map_coords is not None and map_coords.x >= 0 and map_coords.x < len(self.map[0]) and map_coords.y >= 0 and map_coords.y < len(self.map) and self.map[map_coords.y][map_coords.x] is not None:
                                self.player_coords = map_coords
                                self.hovered = None

    def onMouseUp(self, event):
        pass

    def onMouseMotion(self, event):
        if self.planeswalking == 0:
            screen_coords = ScreenCoord(self, event.pos[0] - WW//6, event.pos[1])
            
            self.hovered = None
            if screen_coords.x > 0 and screen_coords.x < (WW*4)//6 and screen_coords.y > 0 and screen_coords.y < 440:
                map_coords = ScreenCoord(self, screen_coords.x + self.player_coords.x*48, screen_coords.y + self.player_coords.y*28).map_coords()
                if map_coords is not None and map_coords.x >= 0 and map_coords.x < len(self.map[0]) and map_coords.y >= 0 and map_coords.y < len(self.map) and self.map[map_coords.y][map_coords.x] is not None:
                    self.hovered = map_coords

    def redrawMap(self):
        self.map_layer.fill(CLEAR)

        for r, row in list(enumerate(self.map)):
            for c in list(range(r % 2, len(row), 2)):
                if row[c] is not None:
                    dash = row[c].find('-')
                    if dash != -1:
                        self.map_layer.blit(tile_wins[row[c][:dash]], ((c + 7) * 48 - 30, (r + 9) * 28 - 82))
                        self.map_layer.blit(tile_wins[row[c][dash+1:]], ((c + 7) * 48 - 30, (r + 9) * 28 - 82))
                    else:
                        self.map_layer.blit(tile_wins[row[c]], ((c + 7) * 48 - 30, (r + 9) * 28 - 82))

    def redrawMapInfo(self):
        pygame.draw.rect(self.ui_layer, (200, 200, 200), (WW//6, 400, 4000//6 + 1, 80))
        pygame.draw.line(self.ui_layer, (100, 100, 100), (WW//6, 400), (5000//6 - 1, 400), 2)

        try:
            save = importlib.import_module("data." + self.player.name + ".worlds." + type(self).__name__.lower() + ".tileViews." + str(self.player_coords.x) + "_" + str(self.player_coords.y))
        except Exception:
            save = None

        if save is None:
            write(
                self.ui_layer,
                f"{self.map[self.player_coords.y][self.player_coords.x].replace('_', ' ').replace('-', ' ')}\nunexplored",
                Coord(WW//6+10, 400+10),
                BLACK,
                2
            )
        else:
            boss = False
            for enemy in save.enemies:
                enemy = getattr(Enemies, enemy[0])(enemy[1], enemy[2])
                if isinstance(enemy, Enemies.Boss):
                    boss = enemy.__class__
                    break
            write(
                self.ui_layer,
                f"{self.map[self.player_coords.y][self.player_coords.x].replace('_', ' ').replace('-', ' ')}\n{str(len(save.enemies))} enemies\n{'! ' + boss.__name__ + ' active' if boss else 'no boss active'}",
                Coord(WW//6+10, 400+10),
                BLACK,
                2
            )

    def drawPauseScreen(self):
        self.win.blit(pygame.transform.scale(Images.menubooks[3], (Images.menubooks[3].get_width()*3, Images.menubooks[3].get_height()*3)), (self.win.get_width()//2 - 260, -10))

        for button in self.buttons:
            button.draw(self.win)

    def run(self):
        while self.running == True:
            if self.player.get_level() < 1:
                Tile(self, self.player, self.player_coords)

            self.win.fill(CLEAR)
            self.map_overlay_layer.fill(CLEAR)
            self.overlay_layer.fill(CLEAR)

            redrawUI(self)
            redrawSpells(self)
            redrawEquipmentMenu(self)

            if self.planeswalking == 0 and self.hovered is not None and self.map[self.hovered.y][self.hovered.x] is not None:
                hoveredtile = self.map[self.hovered.y][self.hovered.x]
                dash = hoveredtile.find('-')
                if dash != -1:
                    self.map_overlay_layer.blit(tile_wins[hoveredtile[:dash]], (self.hovered.screen_coords().get_topleft().x, self.hovered.screen_coords().y - 86))
                    self.map_overlay_layer.blit(tile_wins[hoveredtile[dash+1:]], (self.hovered.screen_coords().get_topleft().x, self.hovered.screen_coords().y - 86))
                else:
                    self.map_overlay_layer.blit(tile_wins[hoveredtile], (self.hovered.screen_coords().get_topleft().x, self.hovered.screen_coords().y - 86))
            elif self.planeswalking < 0:
                growth_factor = (255 + self.planeswalking) // 10
                tilename = self.map[self.player_coords.y][self.player_coords.x]
                dash = tilename.find('-')
                if dash != -1:
                    self.map_overlay_layer.blit(pygame.transform.scale(tile_wins[tilename[:dash]], (64 * growth_factor, 96 * growth_factor)), (1104 - 32*growth_factor, 1148 - 70*growth_factor))
                    self.map_overlay_layer.blit(pygame.transform.scale(tile_wins[tilename[dash+1:]], (64 * growth_factor, 96 * growth_factor)), (1104 - 32*growth_factor, 1148 - 70*growth_factor))
                else:
                    self.map_overlay_layer.blit(pygame.transform.scale(tile_wins[tilename], (64 * growth_factor, 96 * growth_factor)), (1104 - 32*growth_factor, 1148 - 70*growth_factor))

            if not self.paused and self.mapChange:
                self.redrawMap()
                self.mapChange = False
            self.redrawMapInfo()

            if not self.paused:
                if self.player.get_level() == 1:
                    for graveyard in self.graveyards:
                        self.map_overlay_layer.blit(pygame.transform.scale(Images.exclamation_point[(self.tick%60)//10], (32, 32)), ((graveyard[0] + 7) * 48 - 13, (graveyard[1] + 9) * 28 - 45))
                self.player.update(self)
            self.player.draw(self)

            self.win.blit(self.map_layer, (WW//6 - (self.player_coords.x * 48), 0 - (self.player_coords.y * 28)))
            self.win.blit(self.map_overlay_layer, (WW//6 - (self.player_coords.x * 48), 0 - (self.player_coords.y * 28)))
            self.win.blit(self.equipment_menu_layer, (0, 0))
            self.win.blit(self.spellbook_layer, ((WW*5)//6 + 1, 0))
            self.win.blit(self.ui_layer, (0, 0))

            if self.paused:
                self.drawPauseScreen()
            else:
                self.tick += 1
                if self.tick >= TICKLIM:
                    self.tick = 0

            self.win.blit(self.overlay_layer, (0, 0))

            if self.planeswalking > 0: # entering
                self.win.blit(self.planeswalking_layer, (0, 0))
                self.planeswalking_layer.fill((251, 188, 50, self.planeswalking))
                self.planeswalking -= 5
                if self.planeswalking < 0:
                    self.planeswalking = 0
            elif self.planeswalking < 0: # leaving
                self.win.blit(self.planeswalking_layer, (0, 0))
                self.planeswalking_layer.fill((251, 188, 50, 255+self.planeswalking))
                self.planeswalking += 5
                if self.planeswalking >= 0:
                    self.planeswalking = 0
                    self.player.reset()
                    self.running = False
                    Tile(self, self.player, self.player_coords)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.onKeyDown(event.key)
                elif event.type == pygame.KEYUP:
                    self.onKeyUp(event.key)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.onMousePress(event)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.onMouseUp(event)
                elif event.type == pygame.MOUSEMOTION:
                    self.onMouseMotion(event)
                elif event.type == pygame.VIDEORESIZE:
                    self.mapChange = True

            super().run()

        self.save()
        self.game.save()
        self.player.save()
