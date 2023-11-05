import pygame

import items
from position_utilities import *
from write import *
from bitmaps.ui import *
from images import Images
from utilityclasses import *
import enemy as Enemies
from utilities import *
from spells import *
import world
from button import *
from constants import *

book = [[item for item in line] for line in book_background]

def drawEquipment(game, item, position: Coord):
    offset = (WW//6 - 120) // 3
    if position.x == 0:
        startx = offset + 6
    else:
        startx = WW//6 - offset - 60 + 6
    starty = offset + position.y * (60 + offset) + 6

    game.equipment_menu_layer.blit(pygame.transform.scale(item.image, (48, 48)), (startx, starty))
    if item.amount > 0 or item == items.Coins:
        write(game.equipment_menu_layer, str(item.amount), (startx + 42, starty + 38), WHITE, 2)

    if game.paused == 'inventory' and pygame.Rect(startx, starty, 48, 48).collidepoint(pygame.mouse.get_pos()):
        name = ''.join([(" " if c.lower() != c else "") + c for c in item.__name__])[1:]
        lines = [name, '']
        for descriptor in item.descriptors:
            lines.insert(1, ''.join([(" " if c.lower() != c else "") + c for c in descriptor]) + ': ' + str(getattr(item, descriptor)))
        if issubclass(item, items.Food):
            lines.append("click to eat")
        elif issubclass(item, items.Potion):
            lines.append("click to drink")

        sx, sy = pygame.mouse.get_pos()
        w = max([writtenlen(lines[0])*3 + 8] + [writtenlen(line)*2 + 8 for line in lines[1:]])
        sx = min(sx, WW-w)
        sy = min(sy, 426)
        pygame.draw.rect(game.overlay_layer, (210, 182, 152), (sx, sy, w, 26 + 12*len(item.descriptors)), 0, 4)
        pygame.draw.rect(game.overlay_layer, (50, 50, 50), (sx, sy, w, 26 + 12*len(item.descriptors)), 1, 4)
        write(game.overlay_layer, name, (sx+4, sy+4), BLACK, 3)
        for i, line in enumerate(lines[1:-1]):
            write(
                game.overlay_layer,
                line,
                (sx + 4, sy + 22 + i*12),
                BLACK,
                2
            )

def redrawEquipmentMenu(game):
    game.equipment_menu_layer.fill((77, 74, 78))
    pygame.draw.rect(game.equipment_menu_layer, (71, 48, 59), (WW//6 - 3, 0, 3, 480))

    for holder in game.equipment_holders:
        holder.update()
        holder.draw(game.equipment_menu_layer)

    drawEquipment(game, game.player.inventory['martialweapon'], Coord(0, 0))
    drawEquipment(game, game.player.inventory['magicweapon'], Coord(1, 0))
    drawEquipment(game, game.player.inventory['helm'], Coord(0, 1))
    drawEquipment(game, game.player.inventory['charm'], Coord(1, 1))
    drawEquipment(game, game.player.inventory['breastplate'], Coord(0, 2))
    drawEquipment(game, game.player.inventory['ring'], Coord(1, 2))
    drawEquipment(game, game.player.inventory['boots'], Coord(0, 3))
    drawEquipment(game, game.player.inventory['gauntlet'], Coord(1, 3))
    drawEquipment(game, game.player.inventory['shield'], Coord(0, 4))
    drawEquipment(game, game.player.inventory['cloak'], Coord(1, 4))
    drawEquipment(game, game.player.inventory['coins'], Coord(0, 5))
    drawEquipment(game, game.player.inventory['ammo'], Coord(1, 5))

    invlen = str(len(game.player.inventory['inventory']))
    write(game.equipment_menu_layer, invlen, Coord(WH//6 - writtenlen(invlen)*3//2, 458), (71, 48, 59), 3)

def refreshInventory(game):
    game.buttons = pygame.sprite.Group()
    game.pausing = 14
    game.paused = 'inventory'
    Xbutton((673, 78)).add(game.buttons)
    if game.player.inv_page < 0:
        game.player.inv_page = 0
    if game.player.inv_page > len(game.player.inventory['inventory'])//16:
        game.player.inv_page = len(game.player.inventory['inventory'])//16
    for i, item in enumerate(game.player.inventory['inventory'][game.player.inv_page*16:min(game.player.inv_page*16 + len(game.player.inventory['inventory']), game.player.inv_page*16 + 16)]):
        InventoryButton((315 + 90*(i%4) + (42 if i%4 >= 2 else 0), 110 + 65*(i//4)), item, 3, game.player.inv_page*16 + i).add(game.buttons)
    if game.player.inv_page > 0: LeftButton((295, 220), 4).add(game.buttons)
    if game.player.inv_page < len(game.player.inventory['inventory'])//16: RightButton((691, 220), 4).add(game.buttons)

def refreshSpellBook(game):
    game.buttons = pygame.sprite.Group()
    game.pausing = 14
    game.paused = 'spellbook'
    Xbutton((673, 78)).add(game.buttons)
    if game.player.spellbook_page < 0:
        game.player.spellbook_page = 0
    if game.player.spellbook_page > len(game.player.spellbook)//24:
        game.player.spellbook_page = len(game.player.spellbook)//24
    game.player.spellbook = game.player.spellbook
    for i, item in enumerate(game.player.spellbook[game.player.spellbook_page*24:min(game.player.spellbook_page*24 + len(game.player.spellbook), game.player.spellbook_page*24 + 24)]):
        SpellButton((310 + 58*(i%6) + (44 if i%6 >= 3 else 0), 110 + 58*(i//6)), item, 2).add(game.buttons)
    if game.player.spellbook_page > 0: LeftButton((290, 220), 4).add(game.buttons)
    if game.player.spellbook_page < len(game.player.spellbook)//24: RightButton((695, 220), 4).add(game.buttons)

def redrawSpells(game):
    for spellui in game.spells:
        spellui.update(game)
        spellui.draw(game)

def redrawSpellSlots(game):
    for r, row in enumerate(book):
        for c, item in enumerate(row):
            if item != 0:
                pygame.draw.rect(game.spellbook_layer, book_background_colors[item], (2*c, 2*r, 2, 2))

def redrawUI(game):
    game.ui_layer.fill(CLEAR)
    # heart layer
    indent = 0
    numhearts = 0
    if game.player.max_health % 4 > 0:
        if game.player.max_health % 4 == 1:
            heart = Images.base1
        elif game.player.max_health % 4 == 2:
            heart = Images.base2
        elif game.player.max_health % 4 == 3:
            heart = Images.base3
        game.ui_layer.blit(pygame.transform.scale(heart, (heart.get_width()*2, heart.get_height()*2)), ((WW*5)//6 - 10 - indent - 22, 10, 2, 2))
        indent += 27
        numhearts += 1
    for i in range(game.player.max_health//4):
        game.ui_layer.blit(pygame.transform.scale(Images.base4, (Images.base4.get_width()*2, Images.base4.get_height()*2)), ((game.win.get_width()*5)//6 - indent - 32, 10))
        indent += 27
        numhearts += 1
    indent = 27 * (numhearts - (game.player.health//4 + (1 if game.player.health % 4 > 0 else 0)))
    if game.player.health % 4 > 0:
        if game.player.health % 4 == 1:
            heart = Images.heart1
        elif game.player.health % 4 == 2:
            heart = Images.heart2
        elif game.player.health % 4 == 3:
            heart = Images.heart3
        game.ui_layer.blit(pygame.transform.scale(heart, (heart.get_width()*2, heart.get_height()*2)), ((WW*5)//6 - 10 - indent - 22, 10, 2, 2))
        indent += 27
    for i in range(game.player.health//4):
        game.ui_layer.blit(pygame.transform.scale(Images.heart4, (Images.heart4.get_width()*2, Images.heart4.get_height()*2)), ((game.win.get_width()*5)//6 - indent - 32, 10))
        indent += 27
    for i in range(0, game.player.shielded):
        game.ui_layer.blit(pygame.transform.scale(Images.shield, (Images.shield.get_width()*2, Images.shield.get_height()*2)), ((game.win.get_width()*5)//6 - indent - 32, 10))
        indent += 27

    # mana bars
    if game.player.get_level() > 0:
        totals = game.player.get_max_mana(game)
        for i, total in enumerate(totals):
            if totals[total] > 0:
                bar = []
                for line in mana_bar_frame_edge:
                    bar.append([])
                    for item in line:
                        bar[-1].append(item)
                if totals[total] >= 14:
                    for j, line in enumerate(mana_bar_frame_left):
                        bar[j] += line
                    for k in range(totals[total] - 14):
                        for j in range(6):
                            bar[j] += mana_bar_frame_middle[j] + mana_bar_frame_middle[j]
                    for j, line in enumerate(mana_bar_frame_right):
                        bar[j] += line
                else:
                    for j, line in enumerate(mana_bar_frame_left):
                        bar[j] += line[:totals[total]]
                    for j, line in enumerate(mana_bar_frame_right):
                        bar[j] += line[-totals[total]:]
                for j in range(6):
                    bar[j] += mana_bar_frame_edge[j]

                for r, row in enumerate(bar):
                    for c, item in enumerate(row):
                        if item != 0:
                            pygame.draw.rect(game.ui_layer, mana_bar_frame_colors[item], ((WW*5)//6 - 14 - totals[total]*4 + c*2, 35 + 15*i + 2*r, 2, 2))
                for j in range(0, game.player.mana[total]*4, 2):
                    r, g, b = MANA_COLORS[total][0], MANA_COLORS[total][1], MANA_COLORS[total][2]
                    if j not in [0, game.player.mana[total]*4-2]:
                        pygame.draw.rect(game.ui_layer, (r, g, b), ((WW*5)//6 - 14 - j, 37 + 15*i, 2, 2))
                    pygame.draw.rect(game.ui_layer, (max(r-10,0), max(g-10,0), max(b-10,0)), ((WW*5)//6 - 14 - j, 39 + 15*i, 2, 2))
                    pygame.draw.rect(game.ui_layer, (max(r-20,0), max(g-20,0), max(b-20,0)), ((WW*5)//6 - 14 - j, 41 + 15*i, 2, 2))
                    if j not in [0, game.player.mana[total]*4-2]:
                        pygame.draw.rect(game.ui_layer, (max(r-30,0), max(g-30,0), max(b-30,0)), ((WW*5)//6 - 14 - j, 43 + 15*i, 2, 2))
    
    if isinstance(game, world.World):
        game.boss = False
        for enemy in game.enemies:
            if isinstance(enemy, Enemies.Boss):
                game.boss = True
                for r, row in enumerate(boss_health_bar):
                    for c, item in enumerate(row):
                        if item != 0:
                            pygame.draw.rect(game.ui_layer, boss_health_bar_colors[item], (game.ui_layer.get_width()//2 - 170 + 4*c, 10 + 4*r, 4, 4))
                health_percent = enemy.health / enemy.max_health
                r, g, b = 75 + (1-health_percent)*176, 176 - (1-health_percent)*144, 32
                for i in range(4, int(316 * health_percent)):
                    if i < 8:
                        pygame.draw.rect(game.ui_layer, (r, g, b), (game.ui_layer.get_width()//2 - 150 + i, 50, 1, 4))
                    elif i < 12:
                        pygame.draw.rect(game.ui_layer, (r, g, b), (game.ui_layer.get_width()//2 - 150 + i, 46, 1, 8))
                    elif i < 16:
                        pygame.draw.rect(game.ui_layer, (r, g, b), (game.ui_layer.get_width()//2 - 150 + i, 42, 1, 12))
                    elif i > 311:
                        pygame.draw.rect(game.ui_layer, (r, g, b), (game.ui_layer.get_width()//2 - 150 + i, 42, 1, 8))
                    else:
                        pygame.draw.rect(game.ui_layer, (r, g, b), (game.ui_layer.get_width()//2 - 150 + i, 38, 1, 16))

                for r, row in enumerate(right_arrow):
                    if enemy.rect.left < game.player.rect.left:
                        for c, item in enumerate(row[::-1]):
                            if item != 0:
                                pygame.draw.rect(game.ui_layer, right_arrow_colors[item], (game.ui_layer.get_width()//2 - 188 + 2*c, 38 + 2*r, 2, 2))
                    if enemy.rect.right > game.player.rect.right:
                        for c, item in enumerate(row):
                            if item != 0:
                                pygame.draw.rect(game.ui_layer, right_arrow_colors[item], (game.ui_layer.get_width()//2 + 172 + 2*c, 38 + 2*r, 2, 2))
                break

    drawSoulEnergyBar(game)

def drawSoulEnergyBar(game):
    if game.player.alignment == 0:
        frame_colors = good_frame_colors
    elif game.player.alignment == 1:
        frame_colors = neutral_frame_colors
    elif game.player.alignment == 2:
        frame_colors = evil_frame_colors

    pygame.draw.rect(game.ui_layer, BLACK, [0, 480, WW, 20])
    pygame.draw.rect(game.ui_layer, frame_colors[6], [2, 482, 996, 16], 2)
    pygame.draw.rect(game.ui_layer, frame_colors[5], [0, 480, WW, 20], 2)
    for r, row in enumerate(frame):
        for c, item in enumerate(row):
            if item != 0:
                pygame.draw.rect(game.ui_layer, frame_colors[item], [c*2, 472 + r*2, 2, 2])
                pygame.draw.rect(game.ui_layer, frame_colors[item], [998 - c*2, 472 + r*2, 2, 2])
    soul_energy_percentage = game.player.soul_energy / (2 ** (game.player.get_level() + 1))
    num_cols = int(len(soul_bar[0]) * soul_energy_percentage)
    col_width = int(992 / len(soul_bar[0]))
    for i, c in enumerate(soul_bar[0][:num_cols]):
        pygame.draw.rect(game.ui_layer, soul_bar_colors[c], [col_width*i + 4, 484, col_width + 1, 13])
    write(game.ui_layer, "Soul Energy: " + toRomanNumeral(game.player.soul_energy) + " / " + toRomanNumeral(2 ** (game.player.get_level() + 1)), (10, 485), RED, 2)

    if type(game).__name__ == "WorldMap":
        game.redrawMapInfo()
