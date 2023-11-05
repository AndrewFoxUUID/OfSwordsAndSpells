import pygame, os
from random import randint, choice

import items
from maptile import *
from platformertile import *
from position_utilities import *
from utilities import *
from write import *
from controlsEditMenu import ControlsEditMenu
from liquid import Liquid
from button import *
from particle import *
from images import Images
from utilityclasses import *
from shop import Shop
import ui
from constants import *
from screen import *
import enemy
from spells import *

class World(Screen):

    def __init__(self, game, player):
        super().__init__()
        self.game = game

        self.sprites = pygame.sprite.Group()
        self.player = player

        if not os.path.exists(f"data/{player.name}/worlds/{type(game).__name__.lower()}/"):
            os.mkdir(f"data/{player.name}/worlds/{type(game).__name__.lower()}")
        if not os.path.exists(f"data/{player.name}/worlds/{type(game).__name__.lower()}/tileViews/"):
            os.mkdir(f"data/{player.name}/worlds/{type(game).__name__.lower()}/tileViews")

        self.map = []
        self.environmental_overlays = {}
        self.enemies = pygame.sprite.Group()
        self.static = pygame.sprite.Group()
        self.boss = False
        self.trees = []
        self.buildings = []
        self.top_left = Coord(40, 0)
        self.colorkey = COLORKEYS['meadow']

        self.background_layer = pygame.Surface((4000/3, 480), pygame.SRCALPHA)
        self.background_particle_layer = pygame.Surface((TW, TH), pygame.SRCALPHA)
        self.solids_layer = pygame.Surface((TW, TH), pygame.SRCALPHA)
        self.map_overlay_layer = pygame.Surface((TW, TH), pygame.SRCALPHA)
        self.foreground_particle_layer = pygame.Surface((TW, TH), pygame.SRCALPHA)
        self.equipment_menu_layer = pygame.Surface((WW//6, 480), pygame.SRCALPHA)
        self.spellbook_layer = pygame.Surface((WW//6 + 1, 480), pygame.SRCALPHA)
        self.ui_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)
        self.planeswalking_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)
        self.overlay_layer = pygame.Surface((WW, WH), pygame.SRCALPHA)

        self.solids = pygame.sprite.Group()
        self.interactables = pygame.sprite.Group()

        self.equipment_holders = pygame.sprite.Group()
        for r in range(6):
            for c in range(2):
                self.equipment_holders.add(EquipmentHolder(c, r))

        self.spells = pygame.sprite.Group()
        for i in range(10):
            self.spells.add(SpellUI(i))

        self.paused = False
        self.pausing = 0
        self.running = True
        self.achievment = None
        self.shaking = 0

        self.buttons = pygame.sprite.Group()
        self.particles = pygame.sprite.Group()

        self.tick = 0

        self.planeswalking = 255

        ui.redrawSpellSlots(self)

        self.dx = 0
        self.dy = 0

        self.player.rect = pygame.Rect(self.top_left.x + WW//3 - 100, self.top_left.y + 240 - 55, 200, 110)

    def onKeyDown(self, key):
        for button in self.buttons:
            if isinstance(button, TextEntry):
                button.keydown(key)
        self.player.keydown(self, key)

    def onKeyUp(self, key):
        pass

    def onMousePress(self, event):
        if self.planeswalking == 0:
            if event.button == 1:
                for button in self.buttons:
                    button.focused = button.rect.collidepoint(event.pos)

    def onMouseUp(self, event):
        if self.planeswalking == 0:
            if event.button == 1:
                for button in self.buttons:
                    if not isinstance(button, TextEntry): button.focused = False
                    if button.rect.collidepoint(event.pos):
                        if isinstance(button, Xbutton):
                            self.buttons = pygame.sprite.Group()
                            self.paused = False
                        elif isinstance(button, CustomTextButton) and button.text == "controls":
                            self.paused = False
                            ControlsEditMenu(self.player)
                        elif isinstance(button, LeftButton):
                            if self.paused == 'inventory':
                                self.player.inv_page -= 1
                                ui.refreshInventory(self)
                            elif self.paused == 'spellbook':
                                self.player.spellbook_page -= 1
                                ui.refreshSpellBook(self)
                        elif isinstance(button, RightButton):
                            if self.paused == 'inventory':
                                self.player.inv_page += 1
                                ui.refreshInventory(self)
                            elif self.paused == 'spellbook':
                                self.player.spellbook_page += 1
                                ui.refreshSpellBook(self)
                        elif isinstance(button, ToggleButton) and button.text == "debug":
                            self.player.debug = not self.player.debug
                            button.active = not button.active
                        elif isinstance(button, TextEntry) and button.name == "tutorial stage":
                            pass
                        elif isinstance(button, InventoryButton):
                            if button.item.slot is not None:
                                old = self.player.inventory[button.item.slot]
                                self.player.inventory[button.item.slot] = button.item
                                if old not in items.nonDropables:
                                    self.player.inventory['inventory'][button.i] = old
                                    button.item = old
                                    button.win = old.image
                                    button.focused_win = old.image
                                else:
                                    self.player.inventory['inventory'].pop(button.i)
                                    button.kill()
                                ui.refreshInventory(self)
                            elif issubclass(button.item, items.Consumable):
                                self.player.health += button.item.lifegain
                                button.item.amount -= 1
                                if button.item.amount <= 0:
                                    self.player.inventory['inventory'].pop(button.i)
                                    button.kill()
                                    ui.refreshInventory(self)
                        elif isinstance(button, SpellButton):
                            for i in range(8):
                                if self.player.spell_slots[i] == Spell:
                                    self.player.spell_slots[i] = button.spell
                                    break
                        elif self.paused == 'warlock' and isinstance(button, CustomTextButton) and button.text.replace(" ", "") == "Accept":
                            self.paused = False
                            self.player.changeAlignment(self, 2)
                            self.player.playerclass = "Warlock"
                            for e in self.enemies:
                                if isinstance(e, enemy.Lich):
                                    e.die(self)
                            self.player.learnSpell(self, Drain)
                        elif self.paused == 'warlock' and isinstance(button, CustomTextButton) and button.text.replace(" ", "") == "Decline":
                            self.paused = False
                        elif self.paused[:8] == 'tutorial' and isinstance(button, CustomTextButton) and button.text.replace(" ", "") == "Continue":
                            self.buttons = pygame.sprite.Group()
                            if self.paused[9:] == 'death' and self.player.get_level() < 1:
                                self.running = False
                                self.game.running = False
                                self.game.game.running = False
                            self.paused = False
                        elif isinstance(button, CheckBox):
                            button.checked = not button.checked
                            if self.paused == 'paused':
                                self.player.tutorial[button.name] = button.checked
                        elif isinstance(button, CustomTextButton) and button.text.replace(" ", "") == "quit":
                            self.save()
                            self.running = False
                            self.game.running = False
                            self.game.game.running = False
                self.pressed = None

                if not self.paused:
                    for spellui in self.spells:
                        if spellui.rect.collidepoint(event.pos):
                            self.player.spell_slots[spellui.i].cast(self)
                elif self.paused == 'spellbook':
                    for spellui in self.spells:
                        if spellui.rect.collidepoint(event.pos) and spellui.i < 8:
                            self.player.spell_slots[spellui.i] = Spell

    def onMouseMotion(self, event):
        pass

    def drawBackground(self):
        self.background_layer.fill((100, 140, 186))

    def redrawTileView(self):
        self.solids_layer.fill(CLEAR)

        self.solids = pygame.sprite.Group()
        for r, row in enumerate(self.map):
            for c, item in enumerate(row):
                if item in ['a', 'a_']:
                    continue

                if item not in self.tile_wins:
                    tile = getPlatformerTile(item)
                    if tile is not None:
                        surface = pygame.Surface((len(tile[0])*4, len(tile)*4), pygame.SRCALPHA)
                        surface.fill(CLEAR)

                        for r1, row1 in enumerate(tile):
                            for c1, item1 in enumerate(row1):
                                pygame.draw.rect(surface, (*((0,0,0) if item1[0] == 0 else self.colorkey[item1[0]]), item1[1]), (4*c1, 4*r1, 4, 4))

                        self.tile_wins[item] = surface

                if item[0] == 'w':
                    added = False
                    for liquid in self.liquids:
                        if liquid.contains(Coord(c, r)):
                            added = True
                        elif liquid.adjacentTo(Coord(c, r)):
                            liquid.add(Coord(c, r))
                            added = True
                    if not added:
                        self.liquids.append(Liquid(Coord(c, r), 'water'))
                elif item[0] != 'a':
                    self.solids.add(PlatformerTile(pygame.Rect(32*c, 32*r, 4*len(getPlatformerTile(item)[0]), 4*len(getPlatformerTile(item))), item, pygame.mask.from_surface(self.tile_wins[item], 254)))

                if row[c] is not None and row[c][0] != 'w' and len(row[c]) > 1:
                    self.solids_layer.blit(self.tile_wins[item], (32*c, 32*r))

        if self.player.debug:
            for i in range(0, self.solids_layer.get_width() + 32, 32):
                pygame.draw.line(self.solids_layer, BLACK, (i, 0), (i, 1440))
            for i in range(0, 1440, 32):
                pygame.draw.line(self.solids_layer, BLACK, (0, i), (self.solids_layer.get_width(), i))
            for tile in self.solids:
                pygame.draw.rect(self.solids_layer, YELLOW, tile.rect, 1)

    def leaveTileView(self):
        self.sprites = pygame.sprite.Group()
        self.solids = pygame.sprite.Group()
        self.interactables = pygame.sprite.Group()
        self.paused = False
        self.player.reset()

    def drawPauseScreen(self):
        if self.pausing > 0:
            self.win.blit(pygame.transform.scale(Images.menubooks[2-(self.pausing//5)], (157*3, 160*3)), (WH - 157*3//2, -10))
            self.pausing -= 1
        else:
            self.win.blit(pygame.transform.scale(Images.menubooks[3], (157*3, 160*3)), (WH - 157*3//2, -10))

            for button in self.buttons:
                if isinstance(button, InventoryButton):
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if button.h < 12:
                            button.h += 1
                    else:
                        button.h = 0
                elif isinstance(button, SpellButton):
                    if button.rect.collidepoint(pygame.mouse.get_pos()):
                        if button.h < 10:
                            button.h += 1
                    else:
                        button.h = 0

                button.draw(self.win, self)

                if isinstance(button, InventoryButton) and button.rect.collidepoint(pygame.mouse.get_pos()):
                    name = ''.join([(" " if c.lower() != c else "") + c for c in button.item.__name__])[1:]
                    lines = [name]
                    for descriptor in button.item.descriptors:
                        lines.append(''.join([(" " if c.lower() != c else "") + c for c in descriptor]) + ': ' + str(getattr(button.item, descriptor)))
                    lines.append('')

                    sx, sy = pygame.mouse.get_pos()
                    w = max([writtenlen(lines[0])*3 + 8] + [writtenlen(line)*2 + 8 for line in lines[1:]])
                    sx = min(sx, WW-w)
                    sy = min(sy, 426)
                    pygame.draw.rect(self.overlay_layer, (210, 182, 152), (sx, sy, w, 26 + 12*len(button.item.descriptors)), 0, 4)
                    pygame.draw.rect(self.overlay_layer, (50, 50, 50), (sx, sy, w, 26 + 12*len(button.item.descriptors)), 1, 4)
                    write(self.overlay_layer, name, (sx+4, sy+4), BLACK, 3)
                    for i, line in enumerate(lines[1:-1]):
                        write(
                            self.overlay_layer,
                            line,
                            (sx + 4, sy + 22 + i*12),
                            BLACK,
                            2
                        )
                elif isinstance(button, SpellButton) and button.rect.collidepoint(pygame.mouse.get_pos()):
                    name = ''.join([(" " if c.lower() != c else "") + c for c in button.spell.__name__])[1:]
                    lines = [name]
                    maxlen = max(writtenlen(name)*3 + 16 + 18*len(button.spell.colors), 300)
                    words = button.spell.description.split(" ")
                    while len(words) > 0:
                        line = ''
                        while writtenlen(line)*2 < maxlen:
                            line += words[0] + ' '
                            words = words[1:]
                            if len(words) == 0:
                                break
                        lines.append(line)
                    lines.append('')

                    sx, sy = pygame.mouse.get_pos()
                    w = max([writtenlen(name)*3 + 8] + [writtenlen(line)*2 + 8 for line in lines[1:]])
                    sx = min(sx, WW-w)
                    sy = min(sy, 426)
                    pygame.draw.rect(self.overlay_layer, (210, 182, 152), (sx, sy, w, 26 + 12*len(lines[1:-1])), 0, 4)
                    pygame.draw.rect(self.overlay_layer, (50, 50, 50), (sx, sy, w, 26 + 12*len(lines[1:-1])), 1, 4)
                    write(self.overlay_layer, name, (sx+4, sy+4), BLACK, 3)
                    indent = sx + writtenlen(name)*3 + 20
                    for color in button.spell.colors:
                        write(self.overlay_layer, str(button.spell.costs[color]), (indent, sy + 4), MANA_COLORS[color], 3)
                        indent += 18
                    for i, line in enumerate(lines[1:-1]):
                        write(
                            self.overlay_layer,
                            line,
                            (sx + 4, sy + 22 + i*12),
                            BLACK,
                            2
                        )

    def updateBackground(self):
        remove = []
        for coord in self.environmental_overlays:
            item = self.environmental_overlays[coord]
            if item in ['a-0', 'a-1', 'a-2']:
                if item not in self.tile_wins:
                    tile = getPlatformerTile(item)
                    surface = pygame.Surface((len(tile[0])*4, len(tile)*4), pygame.SRCALPHA)
                    surface.fill(CLEAR)
                    for r, row in enumerate(tile):
                        for c, val in enumerate(row):
                            if val[0] != 0:
                                pygame.draw.rect(surface, self.colorkey[val[0]], (4*c, 4*r, 4, 4))
                    self.tile_wins[item] = surface
                self.map_overlay_layer.blit(self.tile_wins[item], (32*coord.x, 32*coord.y))
                if self.tick % 5 == 0:
                    self.environmental_overlays[coord] = 'a-' + str(randint(0, 2))
            elif item in ['a-3', 'a-4', 'a-5']:
                if item not in self.tile_wins:
                    tile = getPlatformerTile(item)
                    surface = pygame.Surface((len(tile[0])*4, len(tile)*4), pygame.SRCALPHA)
                    surface.fill(CLEAR)
                    for r, row in enumerate(tile):
                        for c, val in enumerate(row):
                            if val != 0:
                                pygame.draw.rect(surface, self.colorkey[val], (4*c, 4*r, 4, 4))
                    self.tile_wins[item] = surface
                self.map_overlay_layer.blit(self.tile_wins[item], (32*coord.x, 32*coord.y))
                if self.tick % 10 == 0:
                    self.environmental_overlays[coord] = 'a-' + str(randint(3, 5))
            elif len(item) >= 14 and item[:14] == 'a-chest-closed':
                if self.player.rect.colliderect(pygame.Rect(coord.x*32 + 8, coord.y*32 - 16, 48, 48)):
                    if pygame.key.get_pressed()[self.player.keybinds['p-interact']]:
                        drops = items.item_drops['chest']
                        itemtype = choice(drops[1][min(self.player.get_level(), len(drops[1])-1)])
                        quantity = randint(drops[0][0], drops[0][1])
                        itemtype.drop(self, Coord(coord.x*32 + 32, coord.y*32 - 32), quantity)
                        self.environmental_overlays[coord] = 'a-chest-open-0'

                    if int(item[15]) < 7:
                        self.environmental_overlays[coord] = 'a-chest-closed-' + str(int(item[15])+1)

                    self.map_overlay_layer.blit(pygame.transform.scale(Images.textpopupbase[int(item[15])], (128, 128)), (coord.x*32 + 36, coord.y*32 - 126))
                    if int(item[15]) > 4:
                        write(self.map_overlay_layer, "press " + pygame.key.name(self.player.keybinds['p-interact']) + " to open", (coord.x*32 + 62, coord.y*32 - 40), WHITE, 2)
                else:
                    self.environmental_overlays[coord] = 'a-chest-closed-0'

                self.map_overlay_layer.blit(pygame.transform.scale(Images.chest[0], (72, 72)), (32*coord.x, 32*coord.y - 40))
            elif item == 'a-chest-open-0':
                if self.tick % 5 == 0:
                    self.environmental_overlays[coord] = 'a-chest-open-1'
                self.map_overlay_layer.blit(pygame.transform.scale(Images.chest[1], (72, 72)), (32*coord.x, 32*coord.y - 40))
            elif item == 'a-chest-open-1':
                if self.tick % 5 == 0:
                    self.environmental_overlays[coord] = 'a-chest-open-2'
                self.map_overlay_layer.blit(pygame.transform.scale(Images.chest[2], (72, 72)), (32*coord.x, 32*coord.y - 40))
            elif item == 'a-chest-open-2':
                if self.tick % 5 == 0:
                    self.environmental_overlays[coord] = 'a-chest-open'
                self.map_overlay_layer.blit(pygame.transform.scale(Images.chest[3], (72, 72)), (32*coord.x, 32*coord.y - 40))
            elif item == 'a-chest-open':
                self.map_overlay_layer.blit(pygame.transform.scale(Images.chest[4], (72, 72)), (32*coord.x, 32*coord.y - 40))
            elif item[-2] == '-':
                if item[2:-2] in items.item_drops:
                    if self.player.rect.colliderect(pygame.Rect(coord.x*32, coord.y*32 - 48, 48, 48)):
                        if pygame.key.get_pressed()[self.player.keybinds['p-interact']]:
                            drops = items.item_drops[item[2:-2]]
                            target = choice(drops[1][min([self.player.get_level(), len(drops[1])-1])])
                            quantity = randint(drops[0][0], drops[0][1])
                            target.drop(self, Coord(coord.x*32 + 32, coord.y*32 - 32), quantity)
                            remove.append(coord)

                        if int(item[-1]) < 7:
                            self.environmental_overlays[coord] = item[:-1] + str(int(item[-1])+1)

                        ystart = {'barrel': 40, 'axe': 49, 'wood': 26, 'boxes': 38}[item[2:-2]]
                        self.map_overlay_layer.blit(pygame.transform.scale(Images.textpopupbase[int(item[-1])], (128, 128)), (coord.x*32 + 32, coord.y*32 - ystart - 86))
                        if int(item[-1]) > 4:
                            write(self.map_overlay_layer, "press " + pygame.key.name(self.player.keybinds['p-interact']) + " to open", (coord.x*32 + 56, coord.y*32 - ystart), WHITE, 2)
                    else:
                        self.environmental_overlays[coord] = item[:-1] + '0'
                self.map_overlay_layer.blit(pygame.transform.scale(Images.objects[item[2:-2]], (48, 48)), (32*coord.x + 8, 32*coord.y-16))
        for coord in remove:
            self.environmental_overlays.pop(coord)

        for building in self.buildings:
            self.map_overlay_layer.blit(pygame.transform.scale(Images.shop, (400, 320)), (building.left, building.top))

            coord = Coord(building.left // 32, building.top // 32)
            item = self.environmental_overlays[coord]
            if building.colliderect(self.player.rect):
                if pygame.key.get_pressed()[self.player.keybinds['p-interact']]:
                    Shop(self)

                if int(item[-1]) < 7:
                    self.environmental_overlays[coord] = item[:-1] + str(int(item[-1])+1)

                self.map_overlay_layer.blit(pygame.transform.scale(Images.textpopupbase[int(item[-1])], (128, 128)), (building.left + 184, building.top + 116))
                if int(item[-1]) > 4:
                    write(self.map_overlay_layer, "press " + pygame.key.name(self.player.keybinds['p-interact']) + " to enter", (building.left + 212, building.top + 202), WHITE, 2)
            else:
                self.environmental_overlays[coord] = item[:-1] + '0'

        for tree in self.trees:
            if randint(0, 20) == 0 and (tree[1] + (7 if tree[0] == 'm' else 13))*32 > self.top_left.x and tree[1]*32 < self.top_left.x + self.win.get_width():
                if tree[0] == 'm':
                    x = randint((tree[1] + 1.5)*32, (tree[1] + 5.5)*32)
                    y = randint((tree[2] + 1)*32, (tree[2] + 3)*32)
                elif tree[0] == 'l':
                    x = randint((tree[1] + 2)*32, (tree[1] + 11)*32)
                    y = randint((tree[2] + 2)*32, (tree[2] + 7)*32)

                    if pygame.Rect.colliderect(pygame.Rect(tree[1]*32, tree[2]*32, 432, 440), self.player.rect):
                        e = enemy.TwigBlight((x, y))
                        self.enemies.add(e)
                        self.sprites.add(e)

                particle = Particle(
                    Coord(x, y),
                    randint(2, 6),
                    randint(-4, 0),
                    randint(1, 2),
                    (
                        self.colorkey['medium_leaf'][0] + randint(-10, 10),
                        self.colorkey['medium_leaf'][1] + randint(-30, 30),
                        self.colorkey['medium_leaf'][2] + randint(-10, 10)
                    )
                )
                self.particles.add(particle)

    def run(self):
        self.win.fill(CLEAR)
        self.background_particle_layer.fill(CLEAR)
        self.map_overlay_layer.fill(CLEAR)
        self.overlay_layer.fill(CLEAR)
        self.foreground_particle_layer.fill(CLEAR)

        while len(self.enemies) > 25:
            list(self.enemies)[-1].kill()

        ui.redrawUI(self)
        ui.redrawSpells(self)
        ui.redrawEquipmentMenu(self)

        self.drawBackground()
        if not self.paused:
            self.updateBackground()

        for sprite in self.static:
            sprite.draw(self)
        for sprite in self.sprites:
            if not self.paused:
                sprite.update(self)
            sprite.draw(self)
        if not self.paused:
            self.player.update(self)
        self.player.draw(self)
        for particle in self.particles:
            particle.update(self)
            particle.draw(self)
        for interactable in self.interactables: # why so slow? - the slowker
            interactable.draw(self)

        if self.player.debug:
            self.map_overlay_layer.blit(self.mask.to_surface(setcolor=(255, 255, 255, 150), unsetcolor=BLACK), (0, 0))

        self.win.blit(self.background_layer, (WW//6, 0))
        self.win.blit(self.background_particle_layer, (WW//6 - self.top_left.x + self.shaking % 5 - 2, -self.top_left.y + self.shaking % 5 - 2))
        self.win.blit(self.solids_layer, (WW//6 - self.top_left.x + self.shaking % 5 - 2, -self.top_left.y + self.shaking % 5 - 2))
        self.win.blit(self.map_overlay_layer, (WW//6 - self.top_left.x + self.shaking % 5 - 2, -self.top_left.y + self.shaking % 5 - 2))
        self.win.blit(self.foreground_particle_layer, (WW//6 - self.top_left.x + self.shaking % 5 - 2, -self.top_left.y + self.shaking % 5 - 2))
        self.win.blit(self.equipment_menu_layer, (0, 0))
        self.win.blit(self.spellbook_layer, ((WW*5)//6 + 1, 0))
        self.win.blit(self.ui_layer, (0, 0))

        if self.shaking > 1:
            self.shaking -= 1

        if self.player.debug:
            write(self.win, "Movement Speed: " + str(abs(self.player.vx)), Coord(WW//6 + 10, 10), WHITE, 2)
            write(self.win, str(self.top_left), Coord(WW//6 + 2, 2))

        if self.paused:
            self.drawPauseScreen()
        else:
            self.tick += 1
            if self.tick >= TICKLIM:
                self.tick = 0

        if not self.player.tutorial['basics'] and not self.paused and self.planeswalking == 0:
            self.player.tutorial['basics'] = True
            self.pausing = 14
            self.paused = 'tutorial:basics'
            DialogButton("Welcome to Arbor.\n\nUse " + pygame.key.name(self.player.keybinds['p-left']) + " to move left,\n" + pygame.key.name(self.player.keybinds['p-right']) + " to move right,\n" + pygame.key.name(self.player.keybinds['p-jump']) + " to jump, and\n" + pygame.key.name(self.player.keybinds['p-roll']) + " to roll.\n\nPress " + pygame.key.name(self.player.keybinds['pause']) + " to pause\nthe game and open\nthe pause menu,\nwhere you can click\nCONTROLS to modify\nyour key binds.", (310, 90), 2).add(self.buttons)
            CustomTextButton((325, 300), 2, "    Continue    ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(self.buttons)
            Button(Images.icon, Images.icon, (WH, 110), 5).add(self.buttons)
        elif not self.player.tutorial['combat'] and not self.paused and self.planeswalking == 0:
            enemyOnScreen = False
            for enemy in self.enemies:
                if enemy.onScreen(self):
                    enemyOnScreen = type(enemy).__name__
            
            if enemyOnScreen:
                self.player.tutorial['combat'] = True
                self.pausing = 14
                self.paused = 'tutorial:combat'
                DialogButton("Beware! Creatures\nmove around you.\nThese little guys are\ncalled " + enemyOnScreen + "s. \n" + ("Although they will\nnot directly attack\nyou, their god just\nmight." if enemyOnScreen == 'Armadillo' else "Careful, for they\nmight be angry!") + "\n\nIn Of Swords And\nSpells, there is an\nALIGNMENT system\nbased on your actions.\nBeware the price\nexacted for every soul\nyou claim.\n\nPress " + pygame.key.name(self.player.keybinds['p-attack']) + " to attack, and\n" + pygame.key.name(self.player.keybinds['p-block']) + " to block.", (310, 90), 2).add(self.buttons)
                CustomTextButton((325, 330), 2, "    Continue    ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(self.buttons)
                Button(Images.icon, Images.icon, (WH, 110), 5).add(self.buttons)
        elif not self.player.tutorial['spellcasting'] and not self.paused and self.planeswalking == 0 and self.player.get_level() > 1:
            self.player.tutorial['spellcasting'] = True
            self.pausing = 14
            self.paused = 'tutorial:spellcasting'
            DialogButton("A strange sensation\nfills you, and you\nfeel magical energy\nfrom the world\naround you begin to\nflow through you.\n\nThere are 4 main\ntypes of energy: <" + str(MANA_COLORS['l'])[1:-1].replace(' ', '') + ":LIFE>,\n<" + str(MANA_COLORS['w'])[1:-1].replace(' ', '') + ":WATER>, <" + str(MANA_COLORS['f'])[1:-1].replace(' ', '') + ":BURNING>, and\n<" + str(MANA_COLORS['d'])[1:-1].replace(' ', '') + ":DEATH>. Use this\nenergy to cast spells\nin your spell slots\nto the right.", (310, 90), 2, True).add(self.buttons)
            DialogButton("You can fill your\nspell slots from\nyour spellbook,\nwhich you can access\nby pressing " + pygame.key.name(self.player.keybinds['p-open_spellbook']) + ".\n\nYou have also learned\nthe spell Planar Step,\nwhich lets you travel\nbetween places in the\nsame realm, " + ("and\nPlaneswalk, which\nlets you travel\nbetween the realms." if self.player.get_level() > 1 else "though\nonly one tile at a\ntime for now."), (530, 90), 2, True).add(self.buttons)
            CustomTextButton((550, 330), 2, "    Continue    ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(self.buttons)
        elif not self.player.tutorial['death'] and not self.paused and self.planeswalking == 0 and self.player.dead:
            self.player.tutorial['death'] = True
            self.pausing = 14
            self.paused = 'tutorial:death'
            DialogButton("The injuries you\nhave sustained in\nbattle are " + ("lethal,\nand your character\nhas perished. Press\n'continue' to create\na new character." if self.player.get_level() < 1 else "grevious, but your magic has saved you, pulling you from the world."), (310, 90), 2).add(self.buttons)
            CustomTextButton((325, 300), 2, "    Continue    ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(self.buttons)
            Button(Images.icon, Images.icon, (WH, 110), 5).add(self.buttons)

        if self.achievment is not None:
            pygame.draw.rect(self.overlay_layer, ALIGNMENT_COLORS[self.player.alignment][0], (970 - writtenlen(self.achievment)*2, 10, 20 + writtenlen(self.achievment)*2, 32), 0, 5)
            pygame.draw.rect(self.overlay_layer, ALIGNMENT_COLORS[self.player.alignment][1], (970 - writtenlen(self.achievment)*2, 10, 20 + writtenlen(self.achievment)*2, 32), 1, 5)
            write(self.overlay_layer, self.achievment, (980 - writtenlen(self.achievment)*2, 20), ALIGNMENT_COLORS[self.player.alignment][1], 2)

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
                self.player.reset()
                self.planeswalking = 0
                self.running = False
                self.game.planeswalking = 255

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.save()
                self.game.save()
                self.player.save()
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

        super().run()

    def save(self, f):
        f.write("map = [\n")
        for line in self.map:
            f.write("    " + str(line) + ",\n")
        f.write("]\n\n")

        f.write("environmental_overlays = {\n")
        for key in self.environmental_overlays:
            f.write("    " + str(key) + ": '" + str(self.environmental_overlays[key]) + "',\n")
        f.write("}\n\n")

        f.write("enemies = [\n")
        for enemy in self.enemies:
            f.write("    " + str(enemy) + ",\n")
        f.write("]\n\n")

        f.write("trees = [\n")
        for tree in self.trees:
            f.write("    " + str(tree) + ",\n")
        f.write("]\n\n")

        f.write("buildings = [\n")
        for building in self.buildings:
            f.write("    " + str((building.left, building.top, building.width, building.height)) + ",\n")
        f.write("]\n\n")

        f.write("x = " + str(self.top_left.x))

        f.close()
