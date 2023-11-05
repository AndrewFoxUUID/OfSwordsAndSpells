import pygame, math, importlib, inspect
from random import random
from constants import *

import items, spells
from position_utilities import *
from maptile import *
from images import Images
from world import World
from worldmap import WorldMap
from button import *
import ui
from particle import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, player_name, player_race=None, skipTutorial=False):
        super().__init__()
        self.name = player_name

        for name, cls in inspect.getmembers(items, inspect.isclass):
            if issubclass(cls, items.Item):
                cls.amount = 0

        try:
            save = importlib.import_module(f"data.{player_name}.player_data")
            self.max_health = save.max_health
            self.health = save.health
            self.soul_energy = save.soul_energy
            self.spellbook = [getattr(spells, spell) for spell in save.spellbook]
            self.spell_slots = [getattr(spells, spell) for spell in save.spell_slots]
            self.inventory = {'inventory': []}
            for key in save.inventory:
                if key == 'inventory':
                    for item in save.inventory['inventory']:
                        split = item.split(' ')
                        item = getattr(items, split[1])
                        item.amount = int(split[0])
                        self.inventory['inventory'].append(item)
                else:
                    split = save.inventory[key].split(' ')
                    item = getattr(items, split[1])
                    item.amount = int(split[0])
                    self.inventory[key] = item
            self.keybinds = save.keybinds
            self.shielded = save.shielded
            self.achievments = save.achievments
            self.style = save.style
            self.alignment = save.alignment
            self.playerclass = save.playerclass
            self.tutorial = save.tutorial
            self.race = save.race
        except ModuleNotFoundError:
            self.max_health = 4
            self.health = self.max_health
            self.soul_energy = 1
            self.spellbook = []
            self.spell_slots = [Spell, Spell, Spell, Spell, Spell, Spell, Spell, Spell, Spell, Spell]
            for item in [items.ShortSword, items.ChainTunic, items.LeatherBoots, items.LeatherGloves, items.MetalShield, items.Hood]:
                item.amount = 1
            self.inventory = {
                'martialweapon': items.ShortSword,
                'magicweapon': items.MagicWeapon,
                'helm': items.Helm,
                'charm': items.Charm,
                'breastplate': items.ChainTunic,
                'ring': items.Ring,
                'boots': items.LeatherBoots,
                'gauntlet': items.LeatherGloves,
                'shield': items.MetalShield,
                'cloak': items.Hood,
                'coins': items.Coins,
                'ammo': items.Ammunition,
                'inventory': []
            }
            self.keybinds = {
                'pause': pygame.K_ESCAPE,
                'm-up': pygame.K_w,
                'm-down': pygame.K_s,
                'm-up_left': pygame.K_q,
                'm-up_right': pygame.K_e,
                'm-down_left': pygame.K_a,
                'm-down_right': pygame.K_d,
                'm-enter': pygame.K_RETURN,
                'm-zoom_in': pygame.K_EQUALS,
                'm-zoom_out': pygame.K_MINUS,
                'p-left': pygame.K_a,
                'p-right': pygame.K_d,
                'p-jump': pygame.K_SPACE,
                'p-roll': pygame.K_s,
                'p-interact': pygame.K_q,
                'p-open_inventory': pygame.K_e,
                'p-open_spellbook': pygame.K_t,
                'p-block': pygame.K_f,
                'p-attack': pygame.K_z,
                'p-special': pygame.K_w,
                'p-spell_1': pygame.K_1,
                'p-spell_2': pygame.K_2,
                'p-spell_3': pygame.K_3,
                'p-spell_4': pygame.K_4,
                'p-spell_5': pygame.K_5,
                'p-spell_6': pygame.K_6,
                'p-spell_7': pygame.K_7,
                'p-spell_8': pygame.K_8,
                'p-spell_planar_step': pygame.K_9,
                'p-spell_planeswalk': pygame.K_0,
            }
            self.shielded = 0
            self.achievments = {
                "Tainted": False, # kill something for the first time
                "Manatee": False, # get to 80 max water mana
                "For the Rolls": False, # kill the Armadillon for the first time and recieve the armadillo charm
                "I'm going to make you an offer you can't refuse": False, # kill the Lich for the first time and make a very important choice
            }
            self.style = 1 # lawful/neutral/chaotic
            self.alignment = 0 # good/neutral/evil
            self.playerclass = "Adventurer"
            self.tutorial = {
                'basics': skipTutorial,
                'combat': skipTutorial,
                'inventory': skipTutorial,
                'spellcasting': skipTutorial,
                'death': skipTutorial
            }
            self.race = player_race

            if player_name == "TEST":
                self.gain_soul_energy(64)
                for name, cls in inspect.getmembers(items, inspect.isclass):
                    if issubclass(cls, items.Item):
                        if cls not in items.nonDropables + list(self.inventory.values()):
                            cls.amount = 1
                            self.inventory['inventory'].append(cls)

        self.inv_page = 0
        self.spellbook_page = 0
        self.achievment_ticks = 0
        self.debug = player_name == "TEST"

        self.rect = pygame.Rect(485, 250, 100, 55)
        self.dead, self.hurting = False, False
        self.reset()
        self.prev_mask = self.mask

        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.curIndex = 7
            self.curImageSet = Images.human_death
            self.mask = Images.human_death_mask

    def update(self, world):
        if self.health > self.max_health:
            self.health = self.max_health

        if world.tick % 5 == 0:
            self.curIndex += 1

        if self.health <= 0:
            self.dead = True

        if isinstance(world, World):
            if self.get_level() > 0:
                tilename = world.game.map[world.game.player_coords.y][world.game.player_coords.x]
                if tilename.find('-') != -1:
                    tilename = tilename[:tilename.find('-')]
                manaTypes = TILE_COMPOSITION_MAP[tilename][4]
                if spells.Revitalize not in self.spellbook and 'l' in manaTypes:
                    self.learnSpell(world, spells.Revitalize)
                elif spells.Shield not in self.spellbook and 'w' in manaTypes:
                    self.learnSpell(world, spells.Shield)
                elif spells.FireBolt not in self.spellbook and 'f' in manaTypes:
                    self.learnSpell(world, spells.FireBolt)

            self.running = False
            if not world.paused and world.planeswalking == 0 and pygame.key.get_pressed()[self.keybinds['p-left']] != pygame.key.get_pressed()[self.keybinds['p-right']]:
                self.running = True

            self.idle(world)
            if self.dead:
                self.die()
            if self.hurting:
                self.hurt()
            if self.running:
                self.run()
            if self.falling:
                self.fall()
            if self.jumping:
                self.jump()
            if self.rolling:
                self.roll(world)
            if self.ledge_grabbing:
                self.ledge_grab()
            if self.wall_sliding:
                self.wall_slide()
            if self.blocking > 0:
                self.block()
            if self.attacking > 0:
                self.melee_attack(world)
            if self.casting:
                self.cast(world)

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

            if self.prev_mask != self.mask:
                left, right, up, down = 0, 0, 0, 0
                while True:
                    if not world.mask.overlap(self.mask, (self.rect.left - left, self.rect.top)):
                        self.move_horizontally(world, -left)
                        break
                    if not world.mask.overlap(self.mask, (self.rect.left + right, self.rect.top)):
                        self.move_horizontally(world, right)
                        break
                    if not world.mask.overlap(self.mask, (self.rect.left, self.rect.top - up)):
                        self.move_vertically(world, -up)
                        break
                    if not world.mask.overlap(self.mask, (self.rect.left, self.rect.top + down)):
                        self.move_vertically(world, down)
                        break
                    left += 1
                    right += 1
                    up += 1
                    down += 1
            
            world.dx, world.dy = 0, 0
            self.move_horizontally(world, self.vx)
            self.falling = self.move_vertically(world, self.vy)
            if not self.falling: self.fallTime = 0

            if not world.planeswalking and not self.dead and self.get_level() > 0 and world.tick % 10 == 0:
                max_mana = self.get_max_mana(world)
                for type in max_mana:
                    if self.mana[type] < max_mana[type]:
                        self.mana[type] += 1

            if self.achievment_ticks > 0:
                self.achievment_ticks -= 1
                if self.achievment_ticks == 0:
                    world.achievment = None

            if world.planeswalking < 0:
                self.curImageSet = Images.human_jump
                self.mask = Images.human_jump_mask
                self.curIndex = 2
                self.move_vertically(world, (world.planeswalking - 255)//20)

        #for i, callback in enumerate(self.updateCallbacks):
        #    callback(world, i)

        if self.curIndex >= len(self.curImageSet):
            self.curIndex = 0

    def draw(self, world, coords=None, ps=None):
        if ps is None: ps = self.rect.width // 100

        draw_layer = world.win
        if coords is None:
            draw_layer = world.map_overlay_layer
            if isinstance(world, WorldMap):
                coords = world.player_coords.screen_coords()
                coords.x -= 47
                coords.y -= 70
                ps = 1
            elif isinstance(world, World):
                coords = Coord(self.rect.left, self.rect.top)
                if self.debug:
                    pygame.draw.rect(world.map_overlay_layer, RED, self.rect, 1)

        if self.curIndex >= len(self.curImageSet):
            self.curIndex = 0

        draw_layer.blit(pygame.transform.flip(pygame.transform.scale(self.curImageSet[self.curIndex], (100*ps, 55*ps)), self.flip, False), (coords.x, coords.y))
        if self.debug: draw_layer.blit(pygame.transform.scale(Images.human_idle_mask.to_surface(setcolor=(0,0,0,255), unsetcolor=(0,0,0,0)), (100*ps, 55*ps)), (coords.x, coords.y))

        if self.wall_sliding:
            draw_layer.blit(pygame.transform.flip(pygame.transform.scale(Images.human_slidedust[self.curIndex], (25*ps, 32*ps)), self.flip, False), ((self.rect.left - 11*ps) if self.flip else (self.rect.right - 14*ps), coords.y - 13*ps))

        if isinstance(world, World):
            for item in self.inventory.values():
                if type(item) != list and issubclass(item, items.Equipable):
                    item.drawCallback(world)


    def idle(self, world=None):
        self.vx = 0
        self.vy = 4 + self.fallTime
        self.curImageSet = Images.human_idle
        self.mask = Images.human_idle_mask

        if world is not None:
            self.rect = pygame.Rect(world.top_left.x + WW//3 - 100 if world.top_left.x > -2 and world.top_left.x < TW - 4*WW//6 - 4 else self.rect.left, world.top_left.y + 240 - 55 if world.top_left.y > 0 and world.top_left.y < 960 - 480 else self.rect.top, self.rect.width, self.rect.height)

        if self.curIndex >= len(self.curImageSet):
            pass

    def face_left(self):
        if not self.flip:
            self.ledge_grabbing = False
        self.flip = True

        if self.curIndex >= len(self.curImageSet):
            pass

    def face_right(self):
        if self.flip:
            self.ledge_grabbing = False
        self.flip = False

        if self.curIndex >= len(self.curImageSet):
            pass

    def die(self):
        flip = self.flip
        fallTime = self.fallTime
        falling = self.falling
        vy = self.vy
        if self.rect.height != 10:
            self.rect.top += self.rect.height - 10
            self.rect.height = 10

        self.reset()

        self.flip = flip
        self.fallTime = fallTime
        self.falling = falling
        self.vy = vy if vy >= 0 else self.vy

        self.curImageSet = Images.human_death
        self.mask = Images.human_death_mask

        if self.curIndex >= len(self.curImageSet):
            self.curIndex = len(self.curImageSet) - 1

    def hurt(self):
        flip = self.flip
        falltime = self.fallTime
        falling = self.falling
        vy = self.vy

        self.reset()

        self.flip = flip
        self.fallTime = falltime
        self.falling = falling
        self.vy = vy if vy >= 0 else self.vy
        self.curImageSet = Images.human_hurt
        self.mask = Images.human_hurt_mask

        if self.curIndex >= len(self.curImageSet):
            self.hurting = False
            self.curImageSet = Images.human_idle
            self.mask = Images.human_idle_mask

    def run(self):
        if self.flip and not pygame.key.get_pressed()[self.keybinds['p-left']]:
            self.running = False
            self.wall_sliding = False
            self.ledge_grabbing = False
            return
        elif not self.flip and not pygame.key.get_pressed()[self.keybinds['p-right']]:
            self.running = False
            self.wall_sliding = False
            self.ledge_grabbing = False
            return

        self.vx = 5 * (-1 if self.flip else 1)
        self.curImageSet = Images.human_run
        self.mask = Images.human_run_mask

        if self.curIndex >= len(self.curImageSet):
            pass

    def fall(self):
        self.fallTime += 1
        if not self.dead:# and self.fallTime > 6:
            self.curImageSet = Images.human_fall
            self.mask = Images.human_fall_mask

        if self.curIndex >= len(self.curImageSet):
            pass

    def jump(self):
        self.wall_sliding, self.ledge_grabbing = False, False
        self.curImageSet = Images.human_jump
        self.mask = Images.human_jump_mask
        self.vy = -6

        if self.curIndex >= len(self.curImageSet):
            self.jumping = False
            self.falling = True
            self.curImageSet = Images.human_fall
            self.mask = Images.human_fall_mask

    def roll(self, world):
        self.running, self.jumping = True, False
        self.curImageSet = Images.human_roll
        self.mask = Images.human_roll_mask
        self.vx = 5 * (-1 if self.flip else 1)

        for item in self.inventory.values():
            if type(item) != list and issubclass(item, items.Equipable):
                item.rollCallback(world)

        if self.curIndex >= len(self.curImageSet):
            self.rolling = False
            self.curImageSet = Images.human_run
            self.mask = Images.human_run_mask
    
    def ledge_grab(self):
        self.running, self.falling, self.jumping, self.rolling = False, False, False, False
        self.curImageSet = Images.human_ledgegrab
        self.mask = Images.human_ledgegrab_mask
        self.vx = 0

        if self.curIndex >= len(self.curImageSet):
            pass

    def wall_slide(self):
        pressed = pygame.key.get_pressed()
        if not self.falling or self.jumping:
            self.wall_sliding = False
            return
        elif self.flip and (not pressed[self.keybinds['p-left']] or pressed[self.keybinds['p-right']]):
            self.wall_sliding = False
            return
        elif not self.flip and (not pressed[self.keybinds['p-right']] or pressed[self.keybinds['p-left']]):
            self.wall_sliding = False
            return

        self.fallTime = 1
        self.running, self.jumping = False, False
        self.curImageSet = Images.human_wallslide
        self.mask = Images.human_wallslide_mask
        self.vx = -1 if self.flip else 1
        self.vy = 4

        if self.curIndex >= len(self.curImageSet):
            pass

    def block(self):
        self.vx = 0

        if self.blocking == 1:
            self.curImageSet = Images.human_blockidle
            self.mask = Images.human_blockidle_mask
        elif self.blocking == 2:
            self.curImageSet = Images.human_block
            self.mask = Images.human_block_mask
        elif self.blocking == 3:
            self.curImageSet = Images.human_blocknoeffect
            self.mask = Images.human_blocknoeffect_mask

        if self.curIndex >= len(self.curImageSet):
            self.blocking = 0
            self.curImageSet = Images.human_idle
            self.mask = Images.human_idle_mask

    def melee_attack(self, world): # None, Sword, Dagger, Rapier, Axe, Pike, Throwing, Bow
        self.vx = 0
        if self.inventory['martialweapon'].attackStyle in range(1, 6):
            hitIndex = -1
            if self.inventory['martialweapon'].attackStyle == 1:
                self.curImageSet = Images.human_attack1
                self.mask = Images.human_attack1_mask
                hitIndex = 2
            elif self.inventory['martialweapon'].attackStyle == 2:
                self.curImageSet = Images.human_attack2
                self.mask = Images.human_attack2_mask
                hitIndex = 1
            elif self.inventory['martialweapon'].attackStyle == 3:
                self.curImageSet = Images.human_attack3
                self.mask = Images.human_attack3_mask
                hitIndex = 2

            if self.curIndex == hitIndex and world.tick%5 == 0:
                damage = 0
                for item in self.inventory:
                    if item != 'inventory' and issubclass(self.inventory[item], items.Equipable):
                        damage += self.inventory[item].damageIncrease
                self.attack(world, damage, '')

        if self.curIndex >= len(self.curImageSet):
            self.attacking = 0
            self.curImageSet = Images.human_idle
            self.mask = Images.human_idle_mask

    def cast(self, world):
        self.vx = 0
        self.curImageSet = Images.human_cast
        self.mask = Images.human_cast_mask

        spell_colors = [MANA_COLORS[color] for color in self.curSpell.colors]
        for i, color in list(enumerate(self.curSpell.colors))[::-1]:
            if self.curSpell.costs[color] == '*' and self.get_max_mana(world)[color] == 0:
                spell_colors.pop(i)

        self.particleCoat(world, choice(spell_colors), choice(spell_colors), 5)

        for i in range(8):
            world.particles.add(Particle(
                Coord(self.rect.left if self.flip else self.rect.right, self.rect.top + 38),
                randint(2, 6),
                randint(20, 60)/10 * (-1 if self.flip else 1),
                randint(-100, 100)/10,
                choice(spell_colors),
                randint(2, 8)
            ))

        if self.curIndex >= len(self.curImageSet):
            self.curSpell.effectcast(world)
            self.casting = False
            self.curImageSet = Images.human_idle
            self.mask = Images.human_idle_mask


    def attack(self, world, damage, damagetype):
        fullImage = pygame.sprite.Sprite()
        fullImage.image = pygame.transform.scale(self.curImageSet[self.curIndex], (200, 110))
        fullImage.rect = pygame.Rect(self.rect.left-76, self.rect.bottom-106, 200, 110)

        for enemy in pygame.sprite.spritecollide(fullImage, world.enemies, False):
            player_mask = pygame.mask.from_surface(pygame.transform.flip(fullImage.image, self.flip, False), 254)
            enemy_mask = pygame.mask.from_surface(pygame.transform.flip(
                pygame.transform.scale(
                    enemy.curImageSet[enemy.curIndex],
                    (enemy.curImageSet[enemy.curIndex].get_width()*2, enemy.curImageSet[enemy.curIndex].get_height()*2)
                ),
                enemy.flip,
                False
            ), 254)
            if player_mask.overlap(enemy_mask, (enemy.rect.left + enemy.offset[0] - fullImage.rect.left, enemy.rect.top + enemy.offset[1] - fullImage.rect.top)):
                enemy.damage(world, damage, damagetype)

    def reset(self):
        if not self.dead and not self.hurting: self.curIndex = 0
        self.flip = False
        self.running = False
        self.falling = False
        self.fallTime = 0
        self.jumping = False
        self.rolling = False
        self.ledge_grabbing = False
        self.wall_sliding = False
        self.blocking = 0
        self.attacking = False
        self.casting = False
        self.curImageSet = Images.human_idle
        self.mask = Images.human_idle_mask
        self.vx = 0
        self.vy = 4
        self.curSpell = None
        self.mana = {
            "l": 0,
            "w": 0,
            "f": 0,
            "d": 0,
        }

    def move_horizontally(self, world, vx):
        if world.paused or self.ledge_grabbing: return False
        if vx == 0: return True

        dx = vx

        move_successful = True
        while world.mask.overlap(self.mask, (self.rect.left + dx, self.rect.top)):
            if not world.mask.overlap(self.mask, (self.rect.left + dx, self.rect.top - 8)):
                #self.move_vertically(world, 1)
                break
            move_successful = False
            dx += -1 if vx > 0 else 1

        self.rect.left += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > TW:
            self.rect.right = TW

        if (world.top_left.x > -2 or self.rect.left >= world.top_left.x + WW//3 - self.rect.width//2) and (world.top_left.x < TW - 4*WW//6 - 4 or self.rect.left <= world.top_left.x + WW//3 - self.rect.width//2):
            world.top_left.x += dx
        if world.top_left.x < -2:
            world.top_left.x = -2
        if world.top_left.x > TW - 4*WW//6 - 4:
            world.top_left.x = TW - 4*WW//6 - 4

        return move_successful

    def move_vertically(self, world, vy):
        if world.paused or self.ledge_grabbing: return False
        if vy == 0: return True

        dy = vy

        move_successful = True
        while world.mask.overlap(self.mask, (self.rect.left, self.rect.top + dy)):
            move_successful = False
            dy += -1 if vy > 0 else 1

        self.rect.top += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > TH:
            self.rect.bottom = TH

        if (world.top_left.y > 0 or self.rect.top >= world.top_left.y + (WH-20)//2 - self.rect.height//2) and (world.top_left.y < TH - 480 or self.rect.top <= world.top_left.y + (WH-20)//2 - self.rect.height//2):
            world.top_left.y += dy
        if world.top_left.y < 0:
            world.top_left.y = 0
        if world.top_left.y > TH - 480:
            world.top_left.y = TH - 480

        return move_successful

    """
    def move_horizontally(self, world, vx):
        if world.paused: return
        if self.ledge_grabbing: return False
        if vx == 0: return True
        shifted_rect = pygame.Rect(self.rect.left + vx, self.rect.top, self.rect.width, self.rect.height)
        world.dx = vx

        sprite = pygame.sprite.Sprite()
        sprite.rect = shifted_rect
        for tile in pygame.sprite.spritecollide(sprite, world.solids, False):
            if tile.ramp == 'none':
                world.dx += tile.rect.left - shifted_rect.right if vx > 0 else tile.rect.right - shifted_rect.left
                shifted_rect.left += tile.rect.left - shifted_rect.right if vx > 0 else tile.rect.right - shifted_rect.left

                if self.falling:
                    x = shifted_rect.right // 32 if vx > 0 else shifted_rect.left // 32 - 1
                    
                    if not self.ledge_grabbing:
                        testpoint = pygame.sprite.Sprite()
                        testpoint.rect = pygame.Rect(shifted_rect.right + 1 if vx > 0 else shifted_rect.left - 1, shifted_rect.top, 1, 1)
                        can_ledge_grab = not pygame.sprite.spritecollideany(testpoint, world.solids)
                        mod = 32 - shifted_rect.top % 32
                        shifted_rect.top += mod
                        testpoint.rect = pygame.Rect(shifted_rect.right + 1 if vx > 0 else shifted_rect.left - 1, shifted_rect.top, 1, 1)
                        can_ledge_grab = can_ledge_grab and pygame.sprite.spritecollideany(testpoint, world.solids)
                        can_ledge_grab = can_ledge_grab and not pygame.sprite.spritecollideany(sprite, world.solids)
                        if can_ledge_grab:
                            self.curIndex = 0
                            self.ledge_grabbing = True
                            world.dy = mod
                        else:
                            shifted_rect.top -= mod

                    if not self.wall_sliding and not self.ledge_grabbing:
                        testpoint = pygame.sprite.Sprite()
                        testpoint.rect = pygame.Rect(shifted_rect.right + 1 if vx > 0 else shifted_rect.left - 1, shifted_rect.top, 1, 1)
                        can_wall_slide = pygame.sprite.spritecollideany(testpoint, world.solids)
                        testpoint.rect = pygame.Rect(shifted_rect.right + 1 if vx > 0 else shifted_rect.left - 1, shifted_rect.bottom, 1, 1)
                        can_wall_slide = can_wall_slide and pygame.sprite.spritecollideany(testpoint, world.solids)

                        if can_wall_slide:
                            self.curIndex = 0
                            self.wall_sliding = True

                return False
                    
        return True

    def move_vertically(self, world, vy):
        if world.paused: return
        if self.ledge_grabbing: return False
        shifted_rect = pygame.Rect(self.rect.left, self.rect.top + vy, self.rect.width, self.rect.height)
        world.dy = vy

        if vy > 0: # down
            top_pos = shifted_rect.bottom
            sprite = pygame.sprite.Sprite()
            sprite.rect = shifted_rect
            for tile in pygame.sprite.spritecollide(sprite, world.solids, False):
                if tile.ramp[1:3] == 'tl':
                    pos = tile.rect.bottom - ((shifted_rect.right - tile.rect.left) / int(tile.ramp[0])) - 16*int(tile.ramp[4])
                    if pos < top_pos and pos >= tile.rect.top:
                        top_pos = pos
                elif tile.ramp[1:3] == 'tr':
                    pos = tile.rect.bottom - ((tile.rect.right - shifted_rect.left) / int(tile.ramp[0])) - 16*int(tile.ramp[4])
                    if pos < top_pos and pos >= tile.rect.top:
                        top_pos = pos
                else:
                    pos = tile.rect.top
                    if pos < top_pos:
                        top_pos = pos
            if top_pos < shifted_rect.bottom:
                world.dy += top_pos - shifted_rect.bottom
                return False
        elif vy < 0: # up
            sprite = pygame.sprite.Sprite()
            sprite.rect = shifted_rect
            for tile in pygame.sprite.spritecollide(sprite, world.solids, False):
                if tile.ramp == 'none':
                    world.dy += shifted_rect.top - tile.rect.bottom
                    return False
                    
        return True
    """

    def keydown(self, world, key):
        if isinstance(world, World):
            if world.planeswalking == 0 and key == self.keybinds['pause']:
                if world.paused:
                    world.paused = False
                else:
                    world.pausing = 14
                    world.paused = 'paused'
                    world.buttons = pygame.sprite.Group()

                if world.paused == 'paused':
                    Xbutton((673, 78)).add(world.buttons)
                    CustomTextButton((310, 105), 2, "controls", [(204, 184, 60), (255, 221, 0), (120, 104, 0), (130, 111, 0), (147, 125, 0), (93, 79, 0)]).add(world.buttons)
                    ToggleButton((410, 100), 1, self.debug, [None, BLACK, (150, 150, 150)], "debug").add(world.buttons)
                    DialogButton("Tutorial\nCompletion:", (310, 150), 3).add(world.buttons)
                    for i, stage in enumerate(self.tutorial.keys()):
                        DialogButton(str(i+1) + ": " + stage, (320, 200 + 24*i), 2).add(world.buttons)
                        CheckBox(stage, (320 + writtenlen(str(i+1) + ": " + stage + " ")*2, 197 + 24*i), checked=self.tutorial[stage]).add(world.buttons)
                    CustomTextButton((555, 110), 2, "      quit      ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)]).add(world.buttons)
                else:
                    world.buttons = pygame.sprite.Group()
            elif not world.paused and world.planeswalking == 0:
                if not self.hurting and not self.dead and not self.rolling and not self.attacking and not self.blocking and not self.casting:
                    if key == self.keybinds['p-left']:
                        self.face_left()
                    elif key == self.keybinds['p-right']:
                        self.face_right()
                    if key == self.keybinds['p-roll'] and self.ledge_grabbing:
                        self.face_right() if self.flip else self.face_left()
                        return
                    if not self.ledge_grabbing and not self.wall_sliding and not self.jumping:
                        if not self.falling:
                            if key == self.keybinds['p-roll']:
                                self.curIndex = 0
                                self.rolling = True

                            if key == self.keybinds['p-spell_1']:
                                spell = self.spell_slots[0]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_2']:
                                spell = self.spell_slots[1]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_3']:
                                spell = self.spell_slots[2]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_4']:
                                spell = self.spell_slots[3]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_5']:
                                spell = self.spell_slots[4]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_6']:
                                spell = self.spell_slots[5]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_7']:
                                spell = self.spell_slots[6]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_8']:
                                spell = self.spell_slots[7]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_planar_step']:
                                spell = self.spell_slots[8]
                                if spell.can_cast(world):
                                    spell.cast(world)
                            if key == self.keybinds['p-spell_planeswalk']:
                                spell = self.spell_slots[9]
                                if spell.can_cast(world):
                                    spell.cast(world)

                            if key == self.keybinds['p-jump']:
                                self.curIndex = 0
                                self.jumping = True

                            if key == self.keybinds['p-block']:
                                self.curIndex = 0
                                self.blocking = 1

                            if key == self.keybinds['p-attack']:
                                self.curIndex = 0
                                self.attacking = True

                            if key == self.keybinds['p-open_inventory']:
                                ui.refreshInventory(world)
                            elif self.get_level() > 0 and key == self.keybinds['p-open_spellbook']:
                                ui.refreshSpellBook(world)

                    elif not self.jumping and key == self.keybinds['p-jump']:
                        if self.ledge_grabbing:
                            world.dy -= 12
                        self.curIndex = 0
                        self.jumping = True
            elif world.paused == 'inventory' and key == self.keybinds['p-open_inventory']:
                world.paused = False
                world.buttons = pygame.sprite.Group()
            elif world.paused == 'spellbook' and key == self.keybinds['p-open_spellbook']:
                world.paused = False
                world.buttons = pygame.sprite.Group()

    def get_level(self):
        if self.soul_energy > 0:
            return math.floor(math.log(self.soul_energy, 2))
        else:
            return 0

    def get_max_mana(self, world):
        totals = {
            "l": 0,
            "w": 0,
            "f": 0,
            "d": 0
        }
        player_coords = world.player_coords if isinstance(world, WorldMap) else world.game.player_coords
        coords = player_coords.get_range()
        for coord in coords:
            if coord.y < 0 or coord.y >= len(world.map) or coord.x < 0 or coord.x >= len(world.map[0]):
                continue

            if isinstance(world, WorldMap):
                tile = world.map[coord.y][coord.x]
            else:
                tile = world.game.map[coord.y][coord.x]
                
            if tile is not None:
                dash = tile.find('-')
                if dash != -1:
                    for manaType in TILE_COMPOSITION_MAP[tile[:dash]][4]:
                        totals[manaType] += 2 if coord == player_coords else 1
                    for manaType in TILE_COMPOSITION_MAP[tile[dash+1:]][3]:
                        totals[manaType] += 2 if coord == player_coords else 1
                else:
                    for manaType in TILE_COMPOSITION_MAP[tile][4]:
                        totals[manaType] += 2 if coord == player_coords else 1
        for manatype in totals:
            if totals[manatype] < self.mana[manatype]:
                self.mana[manatype] = totals[manatype]
        if totals['w'] >= 80:
            self.earnAchievment(world, 'Manatee')
        return totals

    def gain_soul_energy(self, amount):
        lvl = self.get_level()
        self.soul_energy += amount
        while self.get_level() > lvl:
            self.max_health += 1
            self.health += 1
            lvl += 1
            if lvl >= 1:
                self.spell_slots[8] = PlanarStep
            if lvl >= 2:
                self.spell_slots[9] = Planeswalk

    def earnAchievment(self, world, achievment):
        if not self.achievments[achievment]:
            self.achievments[achievment] = True
            world.achievment = achievment
            self.achievment_ticks = 100

    def particleCoat(self, world, start_color, end_color, duration):
        for i in range(duration):
            world.particles.add(StatusParticle(
                Coord(self.rect.left + self.rect.width/2, self.rect.top + randint(10, 40)),
                start_color,
                end_color
            ))

    def changeAlignment(self, world, new_alignment):
        self.particleCoat(world, ALIGNMENT_COLORS[self.alignment][0], ALIGNMENT_COLORS[new_alignment][0], 100)
        self.alignment = new_alignment

    def learnSpell(self, world, spell):
        if spell not in self.spellbook:
            self.spellbook.append(spell)
        
        world.buttons = pygame.sprite.Group()
        world.pausing = 14
        world.paused = 'new_spell'
        Xbutton((673, 78)).add(world.buttons)
        Button(spell.image, spell.image, (320, 90), 6).add(world.buttons)
        colors = [MANA_COLORS[color] for color in spell.colors]
        color = BLACK
        for c in colors:
            color = (color[0] + c[0], color[1] + c[1], color[2] + c[2])
        color = (color[0] // len(colors), color[1] // len(colors), color[2] // len(colors))
        DialogButton("<" + str(color)[1:-1].replace(' ', '') + ":" + spell.__name__ + ">", (310, 250), 3, True).add(world.buttons)
        DialogButton(''.join(["<" + str(MANA_COLORS[color])[1:-1].replace(' ', '') + ":" + color[0] + "> " for color in spell.costs]) + "→ " + spell.effect, (310, 270), 2, True).add(world.buttons)
        text = ""
        curstr = ""
        for word in spell.description.split(' '):
            if writtenlen(curstr + " " + word)*2 < 168:
                curstr += " " + word
            else:
                text += "\n" + curstr
                curstr = word
        text += "\n" + curstr
        DialogButton(text[2:], (310, 285), 2).add(world.buttons)
        Button(Images.icon, Images.icon, (WH, 110), 5).add(world.buttons)

    def damage(self, world, amount, damagetype):
        if not self.dead and not self.hurting and not self.blocking > 1:
            callbacks = []
            for item in self.inventory.values():
                if type(item) != list and issubclass(item, items.Equipable):
                    amount -= item.damageReduction
                    callbacks.append(item.damageCallback)
                    if amount <= 0:
                        amount = 0
                        damagetype = '-'
            for callback in callbacks:
                amount = callback(world, amount, damagetype)
                if amount <= 0:
                    amount = 0
                    damagetype = '-'

            if self.blocking == 1:
                self.curIndex = 0

                blockChance = 0.0
                for item in self.inventory:
                    if item != 'inventory' and issubclass(self.inventory[item], items.Equipable):
                        blockChance += self.inventory[item].blockChanceIncrease
                if random() < blockChance and damagetype == '':
                    self.blocking = 2
                    amount = 0
                    damagetype = '-'
                else:
                    self.blocking = 3
                    if damagetype == '':
                        amount = min(1, amount//2)

            while damagetype == '' and self.shielded > 0:
                amount -= 1
                self.shielded -= 1
                if amount == 0:
                    damagetype = '-'

            self.health -= amount

            if amount > 0:
                self.curIndex = 0
                self.hurting = True

            if self.health <= 0:
                self.health = 0
                self.dead = True

            world.particles.add(TextBounce(
                Coord(self.rect.left + self.rect.width//2, self.rect.top + self.rect.height//2),
                {'': '⚔', 'l': '⌖', 'w': '⌖', 'f': '⌖', 'd': '☠', '-': ''}[damagetype] + str(abs(amount)),
                dict({'': (150, 150, 150), '-': (150, 150, 150)}, **MANA_COLORS)[damagetype]
            ))

            return amount > 0

    def heal(self, world, amount, damagetype):
        self.health += amount
        world.particles.add(TextBounce(
            Coord(self.rect.left + self.rect.width//2, self.rect.top + self.rect.height//2),
            '+' + str(abs(amount)),
            (50, 200, 100)
        ))
        return True

    def save(self):
        data_file = open("data/" + self.name + "/player_data.py", "w")

        data_file.write(f"max_health = {self.max_health}\n")
        data_file.write(f"health = {self.health}\n")
        data_file.write(f"soul_energy = {self.soul_energy}\n")
        data_file.write(f"spellbook = {[spell.__name__ for spell in self.spellbook]}\n")
        data_file.write(f"spell_slots = {[spell.__name__ for spell in self.spell_slots]}\n")
        data_file.write(f"inventory = {dict([(key, ([str(item.amount) + ' ' + item.__name__ for item in self.inventory[key]] if key == 'inventory' else (str(self.inventory[key].amount) + ' ' + self.inventory[key].__name__))) for key in self.inventory])}\n")
        data_file.write(f"keybinds = {self.keybinds}\n")
        data_file.write(f"shielded = {self.shielded}\n")
        data_file.write(f"achievments = {self.achievments}\n")
        data_file.write(f"style = {self.style}\n")
        data_file.write(f"alignment = {self.alignment}\n")
        data_file.write(f"playerclass = '{self.playerclass}'\n")
        data_file.write(f"tutorial = {self.tutorial}\n")
        data_file.write(f"race = '{self.race}'\n")

        data_file.close()
