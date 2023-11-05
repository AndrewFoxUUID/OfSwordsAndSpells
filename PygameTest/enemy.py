import pygame
from random import randint, choice
from images import Images
import items as Items
from particle import *
from position_utilities import *
from utilityclasses import *
import projectile as p
from button import *
from constants import *

class Enemy(pygame.sprite.Sprite):
    alignment = 1 # 0 hits 2; 1 hits 0,1,2; 2 hits 0,1
    max_health = 1
    gravity = True
    incorporeal = False
    description = ""

    def __init__(self, rect, health=1):
        super().__init__()
        self.curIndex = 0
        self.curImageSet = []
        self.masks = []
        self.flip = True
        self.vx, self.vy = 0, 0
        self.rect = None
        self.health = health
        self.fallTime = 0
        self.rect = rect
        self.attackCooldown = 0

        self.hurt = False
        self.dead = False

    def update(self, world):
        if not self.dead: self.move_horizontally(world, self.vx * (-1 if self.flip else 1))
            
        if self.rect.left < 320:
            self.rect.left = 320
            self.flip = False
        if self.rect.right > 8319:
            self.rect.right = 8319
            self.flip = True

        if self.gravity:
            if self.move_vertically(world, self.fallTime//4 + 3):
                self.fallTime += 1
            else:
                self.fallTime = 0
        self.move_vertically(world, self.vy)

        if self.attackCooldown > 0:
            self.attackCooldown -= 1

    def move_horizontally(self, world, vx):
        if vx == 0: return True

        self.rect.left += vx

        move_successful = True
        for tile in pygame.sprite.spritecollide(self, world.solids, False):
            while tile.mask is not None and tile.ramp == 'none' and self.masks[0][1 if self.flip else 0].overlap(tile.mask, (tile.rect.left - self.rect.left, tile.rect.top - self.rect.top)):
                move_successful = False
                self.rect.left += -1 if vx > 0 else 1

        return move_successful

    def move_vertically(self, world, vy):
        if vy == 0: return True

        self.rect.top += vy

        move_successful = True
        for tile in pygame.sprite.spritecollide(self, world.solids, False):
            while tile.mask is not None and self.masks[0][1 if self.flip else 0].overlap(tile.mask, (tile.rect.left - self.rect.left, tile.rect.top - self.rect.top)):
                move_successful = False
                self.rect.top += -1 if vy > 0 else 1

        return move_successful

    def draw(self, world):
        if world.player.debug:
            pygame.draw.rect(world.map_overlay_layer, GREEN, self.rect, 1)

        world.map_overlay_layer.blit(pygame.transform.flip(self.curImageSet[self.curIndex], self.flip, False), (self.rect.left, self.rect.top))

    def damage(self, world, amount, damagetype):
        if self.hurt:
            amount = 0
            damagetype = '-'
        world.particles.add(TextBounce(
            Coord(self.rect.left + self.rect.width//2, self.rect.top + self.rect.height//2),
            ('+' if amount < 1 else {'': '⚔', 'l': '⌖', 'w': '⌖', 'f': '⌖', 'd': '☠', '-': 'ø'}[damagetype]) + str(abs(amount)),
            (50, 200, 100) if amount < 0 else dict({'': (150, 150, 150), '-': (150, 150, 150)}, **MANA_COLORS)[damagetype]
        ))

    def die(self, world, soul_energy=0):
        super().kill()
        self.dead = True
        world.player.gain_soul_energy(soul_energy)
        if self.alignment == 0:
            world.player.earnAchievment(world, 'Tainted')
            if world.player.alignment == 0:
                world.player.changeAlignment(world, 1)

    def onScreen(self, world):
        return self.rect.left >= world.top_left.x and self.rect.right <= world.top_left.x + 2000//3 and self.rect.top >= world.top_left.y and self.rect.bottom <= world.top_left.y + 480

    def particleCoat(self, world, start_color, end_color, duration):
        for i in range(duration):
            world.particles.add(StatusParticle(
                Coord(self.rect.left + self.rect.width//2, self.rect.top + randint(2, self.rect.height//2)),
                start_color,
                end_color
            ))

    def attack(self, world, damage, damagetype=''): # TODO
        fullImage = pygame.sprite.Sprite()
        fullImage.image = pygame.transform.scale(world.player.curImageSet[world.player.curIndex], (200, 110))
        fullImage.rect = pygame.Rect(world.player.rect.left-76, world.player.rect.bottom-106, 200, 110)

        player_mask = pygame.mask.from_surface(pygame.transform.flip(fullImage.image, world.player.flip, False), 254)
        enemy_mask = pygame.mask.from_surface(pygame.transform.flip(
            pygame.transform.scale(
                self.curImageSet[self.curIndex if self.curIndex < len(self.curImageSet) else 0],
                (
                    self.curImageSet[self.curIndex if self.curIndex < len(self.curImageSet) else 0].get_width()*2,
                    self.curImageSet[self.curIndex if self.curIndex < len(self.curImageSet) else 0].get_height()*2
                )
            ),
            self.flip,
            False
        ), 254)
        if player_mask.overlap(enemy_mask, (self.rect.left + self.offset[0] - fullImage.rect.left, self.rect.top + self.offset[1] - fullImage.rect.top)):
            return world.player.damage(world, damage, damagetype)
        return False

    def __str__(self):
        return str([type(self).__name__, (self.rect.left, self.rect.top), self.health])


class Armadillo(Enemy):
    alignment = 0
    description = "a cute little critter with an angry guardian"

    def __init__(self, coords, health=1):
        super().__init__(pygame.Rect(coords[0], coords[1], 64, 64), health)

        self.walking = False
        self.rollingUp = False
        self.rolledUp = False

        self.curImageSet = Images.armadillo_idle
        self.masks = Images.armadillo_idle_masks
        
    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            if not self.rolledUp:
                self.curIndex += 1

            if self.curIndex >= len(self.curImageSet) or (self.rolledUp and randint(0, 20) == 0):
                self.curIndex = 0

                if self.rolledUp:
                    self.rolledUp = False
                    self.curImageSet = Images.armadillo_idle
                    self.masks = Images.armadillo_idle_masks

                if self.hurt:
                    self.hurt = False
                    self.curImageSet = Images.armadillo_idle
                    self.masks = Images.armadillo_idle_masks

                if self.health <= 0:
                    self.dead = True
                elif self.rollingUp or randint(0, 2) == 0:
                    if self.rollingUp:
                        self.rollingUp = False
                        self.rolledUp = True
                        self.curIndex -= 1
                    elif world.player.alignment > 0 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                        self.rollingUp = True
                        self.walking = False
                        self.vx = 0
                        self.curImageSet = Images.armadillo_rollup
                        self.masks = Images.armadillo_rollup_masks
                        self.attackCooldown = 20
                    elif randint(0, 2) == 0:
                        self.flip = choice([True, False])
                        if randint(0, 2) == 0:
                            self.walking = True
                            self.rollingUp = False
                            self.vx = 2
                            self.curImageSet = Images.armadillo_run
                            self.masks = Images.armadillo_run_masks
                        else:
                            self.walking = False
                            self.rollingUp = False
                            self.vx = 0
                            self.curImageSet = Images.armadillo_idle
                            self.masks = Images.armadillo_idle_masks
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            if self.curIndex < 2 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.armadillo_die
            self.masks = Images.armadillo_die_masks
            if self.curIndex == 2:
                self.die(world)
                world.static.add(self)
        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount if not self.rolledUp or type == 's' else 0, type)
        if not self.rolledUp or type == 's' and not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.curImageSet = Images.armadillo_hurt
            self.masks = Images.armadillo_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True

    def die(self, world):
        super().die(world)
        if not world.boss:
            boss = Armadillon((self.rect.left, 0))
            boss.justSummoned = True
            world.boss = True
            world.enemies.add(boss)
            world.sprites.add(boss)


class Dummy(Enemy):
    description = "forged by an ancient wizard, literally indestructable"

    def __init__(self, coords, health=1):
        super().__init__(pygame.Rect(coords[0], coords[1], 70, 76), health)

        self.key_active = False
        self.attackMode = False

        self.curImageSet = Images.dummy_idle
        self.masks = Images.dummy_idle_masks

    def update(self, world):
        self.flip = self.rect.left > world.player.rect.left

        if not self.key_active and self.rect.colliderect(world.player.rect) and pygame.key.get_pressed()[world.player.keybinds['p-interact']]:
            self.attackMode = not self.attackMode

        self.key_active = pygame.key.get_pressed()[world.player.keybinds['p-interact']]

        if world.tick % 5 == 4:
            self.curIndex += 1

            if self.curImageSet == Images.dummy_throw and self.curIndex == 1 and randint(0, 3) == 0:
                projectile = p.Projectile(
                    Coord(self.rect.left + 12 if self.flip else self.rect.right - 12, self.rect.top + 8),
                    (24, 24),
                    -10 if self.flip else 10,
                    0,
                    -1,
                    True,
                    Images.arrow[0],
                    updateCallback=Items.Arrow.projectileupdate
                )
                world.particles.add(projectile)

        if self.curIndex >= len(self.curImageSet):
            self.curIndex = 0
            if self.attackMode:
                self.curImageSet = Images.dummy_throw
                self.masks = Images.dummy_throw_masks
            else:
                self.curImageSet = Images.dummy_idle
                self.masks = Images.dummy_idle_masks

        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        self.curImageSet = Images.dummy_hurt
        self.masks = Images.dummy_hurt_masks
        self.health = 1


class Hedgehog(Enemy):
    alignment = 0
    description = "a cute little critter with a little bit of sting"

    def __init__(self, coords, health=1):
        super().__init__(pygame.Rect(coords[0], coords[1], 64, 64), health)

        self.walking = False
        self.attacking = False

        self.curImageSet = Images.hedgehog_idle
        self.masks = Images.hedgehog_idle_masks
        
    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.attacking and self.curIndex == 3:
                self.attack(world, 1)

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

                self.attacking = False
                if self.health <= 0:
                    self.dead = True
                elif randint(0, 2) == 0:
                    if world.player.alignment > 0 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                        self.attacking = True
                        self.walking = False
                        self.vx = 0
                        self.curImageSet = Images.hedgehog_attack
                        self.masks = Images.hedgehog_attack_masks
                        self.attackCooldown = 20
                    elif randint(0, 2) == 0:
                        self.flip = choice([True, False])
                        if randint(0, 2) == 0:
                            self.walking = True
                            self.vx = 2
                            self.curImageSet = Images.hedgehog_walk
                            self.masks = Images.hedgehog_walk_masks
                        else:
                            self.walking = False
                            self.vx = 0
                            self.curImageSet = Images.hedgehog_idle
                            self.masks = Images.hedgehog_idle_masks
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            if self.curIndex < 2 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.hedgehog_die
            self.masks = Images.hedgehog_die_masks
            if self.curIndex == 2:
                self.die(world)
                world.static.add(self)
        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.vx = 0
            if self.health <= 0:
                self.dead = True


class TwigBlight(Enemy):
    max_health = 2
    description = "a veritable nuisance waiting for you in every treetop"

    def __init__(self, coords, health=2):
        super().__init__(pygame.Rect(coords[0], coords[1], 64, 64), health)

        self.running = False
        self.attacking = False

        self.curImageSet = Images.twigblight_idle
        self.masks = Images.twigblight_idle_masks
       
    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.attacking and self.curIndex == 4:
                self.attack(world, 1)

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0
                if self.attacking:
                    self.attacking = False
                    self.running = True

                if self.hurt:
                    self.hurt = False
                    self.curImageSet = Images.twigblight_idle
                    self.masks = Images.twigblight_idle_masks

                if self.health <= 0:
                    self.dead = True
                elif randint(0, 2) == 0:
                    if world.player.alignment > 0 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                        self.attacking = True
                        self.running = False
                        self.vx = 0
                        self.curImageSet = Images.twigblight_attack
                        self.masks = Images.twigblight_attack_masks
                        self.attackCooldown = 20
                    elif randint(0, 2) == 0:
                        if world.player.alignment == 0:
                            self.flip = choice([True, False])
                        elif world.player.alignment == 2:
                            self.flip = False if world.player.rect.left < self.rect.left else True
                        else:
                            self.flip = True if world.player.rect.left < self.rect.left else False
                        self.running = True
                        self.vx = 4
                        self.curImageSet = Images.twigblight_run
                        self.masks = Images.twigblight_run_masks
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            if self.curIndex < 4 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.twigblight_die
            self.masks = Images.twigblight_die_masks
            if self.curIndex == 4:
                self.die(world)
        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.attacking = False
            self.curImageSet = Images.twigblight_hurt
            self.masks = Images.twigblight_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True

    def die(self, world):
        super().die(world)
        Items.Twigs.drop(world, Coord(self.rect.left, self.rect.top))


class Bat(Enemy):
    gravity = False
    max_health = 2
    description = "like a rat, but with wings"

    def __init__(self, coords, health=2):
        super().__init__(pygame.Rect(coords[0], coords[1], 128, 128), health)

        self.attacking = False

        self.vx = 3
        self.curImageSet = Images.bat_fly
        self.masks = Images.bat_fly_masks
       
    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.attacking and self.curIndex == 4:
                projectile = p.Projectile(
                    Coord(self.rect.left + self.rect.width//2, self.rect.top + self.rect.height//2),
                    (30, 26),
                    -6 if self.flip else 6,
                    1,
                    4,
                    False,
                    Images.wind,
                    [],
                    p.wind_callback
                )
                world.particles.add(projectile)

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0
                if self.attacking:
                    self.attacking = False

                if self.hurt:
                    self.hurt = False
                    self.curImageSet = Images.bat_fly
                    self.masks = Images.bat_fly_masks

                if self.health <= 0:
                    self.dead = True
                elif randint(0, 4) == 0 and self.attackCooldown == 0:
                    self.attacking = True
                    self.curImageSet = Images.bat_attack
                    self.masks = Images.bat_attack_masks
                    self.vx = 0
                    self.attackCooldown = 20
                elif randint(0, 2) == 0:
                    self.flip = True if world.player.rect.left < self.rect.left else False
                    self.vx = 3
                    self.vy = 1 if world.player.rect.top > self.rect.top else -1
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            self.gravity = True
            if self.curIndex < 6 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.bat_die
            self.masks = Images.bat_die_masks
            if self.curIndex == 6:
                self.die(world)
                world.static.add(self)
        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.attacking = False
            self.curImageSet = Images.bat_hurt
            self.masks = Images.bat_hurt_masks
            if self.health <= 0:
                self.dead = True


class Slime(Enemy):
    alignment = 2
    max_health = 4
    description = "a spiky squishy stress toy, just don't get too close"

    def __init__(self, coords, health=4):
        super().__init__(pygame.Rect(coords[0], coords[1], 128, 128), health)

        self.sliding = False
        self.jumping = False
        self.attacking = False

        self.curImageSet = Images.slime_idle
        self.masks = Images.slime_idle_masks
       
    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.hurt:
                self.curImageSet = Images.slime_hurt
                self.masks = Images.slime_hurt_masks
                self.vx = 0
            elif self.jumping:
                self.curImageSet = Images.slime_jump
                self.masks = Images.slime_jump_masks
                if self.curIndex == 0:
                    self.vx = 0
                    self.vy = 0
                elif self.curIndex == 1:
                    self.vx = 0
                    self.vy = 0
                elif self.curIndex == 2:
                    self.vx = 2
                    self.vy = -12
                    self.gravity = False
                elif self.curIndex == 3:
                    self.vx = 2
                    self.vy = -8
                elif self.curIndex == 4:
                    self.vx = 2
                    self.vy = -1
                elif self.curIndex == 5:
                    self.vx = 2
                    self.vy = 8
                    self.gravity = True
                elif self.curIndex == 6:
                    self.vx = 2
                    self.vy = 12
                elif self.curIndex == 7:
                    self.vx = 0
                    self.vy = 0
                    self.attack(world, 1)
            elif self.attacking:
                self.curImageSet = Images.slime_attack
                self.masks = Images.slime_attack_masks
                if self.curIndex == 1:
                    self.attack(world, 2)
            elif self.sliding:
                self.curImageSet = Images.slime_slide
                self.masks = Images.slime_slide_masks
                self.vx = self.curIndex + 1
            else:
                self.curImageSet = Images.slime_idle
                self.masks = Images.slime_idle_masks

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

                self.attacking = False
                self.jumping = False
                self.hurt = False

                if self.health <= 0:
                    self.dead = True
                elif randint(0, 2) == 0:
                    if world.player.alignment < 2 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                        self.attacking = True
                        self.sliding = False
                        self.vx = 0
                        self.curImageSet = Images.slime_attack
                        self.masks = Images.slime_attack_masks
                        self.attackCooldown = 20
                    else:
                        self.flip = True if world.player.rect.left < self.rect.left else False
                        self.sliding = True
                        self.vx = 4
                        self.curImageSet = Images.slime_slide
                        self.masks = Images.slime_slide_masks
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            if self.curIndex < 2 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.slime_die
            self.masks = Images.slime_die_masks
            if self.curIndex == 2:
                self.die(world)
        super().update(world)

    def move_horizontally(self, world, vx):
        success = super().move_horizontally(world, vx)
        if self.sliding and not success:
            self.sliding = False
            self.jumping = True
            self.curIndex = 0
            self.vx = 0

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.attacking = False
            self.jumping = False
            self.curImageSet = Images.slime_hurt
            self.masks = Images.slime_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True


class Ghoul(Enemy):
    alignment = 2
    max_health = 5
    description = "the decaying remains of a once proud ... something"

    def __init__(self, coords, health=5):
        super().__init__(pygame.Rect(*coords, 64, 64), health)

        self.walking = False
        self.attacking = False

        self.curImageSet = Images.ghoul_idle
        self.masks = Images.ghoul_idle_masks

    def update(self, world):
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.hurt:
                self.curImageSet = Images.ghoul_hurt
                self.masks = Images.ghoul_hurt_masks
                self.vx = 0
            elif self.attacking:
                self.curImageSet = Images.ghoul_attack
                self.masks = Images.ghoul_attack_masks
                if self.curIndex == 4:
                    self.attack(world, 3)
            elif self.walking:
                self.curImageSet = Images.ghoul_walk
                self.masks = Images.ghoul_walk_masks
                self.vx = randint(1, 10)/10
            else:
                self.curImageSet = Images.ghoul_idle
                self.masks = Images.ghoul_idle_masks

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

                self.attacking = False
                self.walking = False
                self.hurt = False

                if self.health <= 0:
                    self.dead = True
                elif world.player.alignment < 2 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                    self.attacking = True
                    self.vx = 0
                    self.curImageSet = Images.ghoul_attack
                    self.masks = Images.ghoul_attack_masks
                    self.attackCooldown = 20
                elif randint(0, 2) != 0:
                    self.flip = True if world.player.rect.left < self.rect.left else False
                    self.walking = True
                    self.vx = 1
                    self.curImageSet = Images.ghoul_walk
                    self.masks = Images.ghoul_walk_masks
                else:
                    self.vx = 0
                    self.curImageSet = Images.ghoul_idle
                    self.masks = Images.ghoul_idle_masks
        if self.health <= 0:
            self.health = 0
            self.dead = True
            self.vx = 0
            if self.curIndex < 5 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.ghoul_die
            self.masks = Images.ghoul_die_masks
            if self.curIndex == 5:
                self.die(world)
        super().update(world)

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.attacking = False
            self.walking = False
            self.curImageSet = Images.ghoul_hurt
            self.masks = Images.ghoul_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True

    def die(self, world):
        super().die(world, 1)
        Items.Cloth.drop(world, Coord(self.rect.left, self.rect.top))


class Boss(Enemy):
    pass

class Armadillon(Boss):
    max_health = 10
    description = "an avatar of a recently angered armadillo god"

    def __init__(self, coords, health=10):
        super().__init__(pygame.Rect(coords[0], coords[1], 128, 128), health)

        self.walking = False
        self.rollingUp = False
        self.rolling = False

        self.curImageSet = Images.armadillon_idle
        self.masks = Images.armadillon_idle_masks

        self.justSummoned = False
        
    def update(self, world):
        if self.justSummoned and self.fallTime == 0 and self.onScreen(world):
            self.justSummoned = False
            world.shaking = 40

        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1

            if self.rolling:
                self.attack(world, 1)

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

                if self.hurt:
                    self.hurt = False
                    self.walking = False
                    self.rolling = False
                    self.vx = 0
                    if self.attackCooldown == 0:
                        self.rollingUp = True
                        self.curImageSet = Images.armadillon_rollup
                        self.masks = Images.armadillon_rollup_masks
                        self.attackCooldown = 20
                        self.flip = world.player.rect.left < self.rect.left
                elif self.health <= 0:
                    self.dead = True
                elif self.rollingUp or randint(0, 2) == 0:
                    if self.rolling:
                        self.rolling = False
                        self.curImageSet = Images.armadillon_idle
                        self.masks = Images.armadillon_idle_masks
                        self.vx = 0
                        self.flip = world.player.rect.left < self.rect.left
                    elif self.rollingUp:
                        self.rollingUp = False
                        self.rolling = True
                        self.vx = 6
                        self.curImageSet = Images.armadillon_roll
                        self.masks = Images.armadillon_roll_masks
                    elif randint(0, 1) == 0:
                        self.flip = world.player.rect.left < self.rect.left

                        if randint(0, self.health) == 0 and self.attackCooldown == 0:
                            self.rollingUp = True
                            self.walking = False
                            self.rolling = False
                            self.vx = 0
                            self.curImageSet = Images.armadillon_rollup
                            self.masks = Images.armadillon_rollup_masks
                            self.attackCooldown = 20
                        elif randint(0, 2) == 0:
                            self.walking = False
                            self.rollingUp = False
                            self.rolling = False
                            self.vx = 0
                            self.curImageSet = Images.armadillon_idle
                            self.masks = Images.armadillon_idle_masks
                        else:
                            self.walking = True
                            self.rollingUp = False
                            self.rolling = False
                            self.vx = 3
                            self.curImageSet = Images.armadillon_run
                            self.masks = Images.armadillon_run_masks
        if self.dead:
            self.vx = 0
            if self.curIndex < 2 and world.tick % 5 == 0:
                self.curIndex += 1
            self.curImageSet = Images.armadillon_die
            self.masks = Images.armadillon_die_masks
            if self.curIndex == 2:
                self.die(world)
                world.static.add(self)
        super().update(world)

    def move_horizontally(self, world, vx):
        self.rect.left += vx
        return True

    def damage(self, world, amount, type):
        super().damage(world, amount if not self.rolling or type == 'd' else 0, type)
        if (not self.rolling or type == 'd') and not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.curImageSet = Images.armadillon_hurt
            self.masks = Images.armadillon_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True

    def die(self, world):
        super().die(world, 1 if world.player.get_level() != 1 else 0)
        Items.ArmadilloCharm.drop(world, Coord(self.rect.left, self.rect.top))
        world.player.earnAchievment(world, "For the Rolls")


class Lich(Boss):
    alignment = 2
    max_health = 20
    description = "the dark lord of the swamp, really likes purple, thats why all his magic is made of it"

    def __init__(self, coords, health=20):
        super().__init__(pygame.Rect(coords[0], coords[1], WH, WH), health)

        self.running = False
        self.jumping = False
        self.falling = False
        self.upattacking = False
        self.downattacking = False

        self.curImageSet = Images.lich_idle
        self.masks = Images.lich_idle_masks
        
    def update(self, world):
        if not self.dead and world.player.alignment < 2:
            self.flip = world.player.rect.left < self.rect.left
        if not self.dead and (world.tick % 5 == 0 or (world.tick % 2 == 0 and self.hurt)):
            self.curIndex += 1
            
            self.vy = 0
            if self.hurt:
                self.curImageSet = Images.lich_hurt
                self.masks = Images.lich_hurt_masks
                self.vx = 0
            elif self.jumping:
                self.curImageSet = Images.lich_jump
                self.masks = Images.lich_jump_masks
                self.vy = -8
            elif self.falling:
                self.curImageSet = Images.lich_fall
                self.masks = Images.lich_fall_masks
            elif self.upattacking:
                self.curImageSet = Images.lich_upattack
                self.masks = Images.lich_upattack_masks
                if self.curIndex == 4 and self.attack(world, 2, 'd') and self.health < self.max_health and randint(0, 3) == 0:
                    self.damage(world, -1, 'd')
            elif self.downattacking:
                self.curImageSet = Images.lich_downattack
                self.masks = Images.lich_downattack_masks
                if self.curIndex == 4 and self.attack(world, 4, 'd') and randint(0, 1) == 0:
                    self.damage(world, -2, 'd')
            elif self.running:
                self.curImageSet = Images.lich_run
                self.masks = Images.lich_run_masks
                self.vx = 4
            else:
                self.vx = 0
                self.curImageSet = Images.lich_idle
                self.masks = Images.lich_idle_masks

            if self.curIndex >= len(self.curImageSet):
                self.curIndex = 0

                self.hurt = False
                self.upattacking = False
                self.downattacking = False
                self.jumping = False

                if self.health <= 0:
                    self.dead = True
                elif not self.falling:
                    if world.player.alignment < 2 and self.rect.colliderect(world.player.rect) and self.attackCooldown == 0:
                        self.running = False
                        self.vx = 0
                        if self.health > 7:
                            self.upattacking = True
                            self.curImageSet = Images.lich_upattack
                            self.masks = Images.lich_upattack_masks
                        else:
                            self.downattacking = True
                            self.curImageSet = Images.lich_downattack
                            self.masks = Images.lich_downattack_masks
                        self.attackCooldown = 20
                    else:
                        self.running = True
                        if world.player.alignment == 2:
                            self.flip = choice([True, False])
                        self.curImageSet = Images.lich_run
                        self.masks = Images.lich_run_masks
        if self.dead:
            self.vx = 0
            if self.curIndex < 6 and world.tick % 5 == 0:
                self.curIndex += 1
                if self.curIndex == 1: # warlock choice cutscene
                    world.pausing = 14
                    world.paused = 'warlock'
                    NPCButton([pygame.transform.flip(image, True, False) for image in Images.lich_idle], (260, -139), 3).add(world.buttons)
                    DialogButton("Wait.\n\nI am a powerful Lich.\nSpare me, and I shall\ngive you a taste of \nmy power.", (310, 90), 2).add(world.buttons)
                    CustomTextButton((320, 260), 2, "       Accept       ", [(63, 7, 162), (96, 16, 245), (42, 3, 108), (33, 2, 86), (46, 4, 119), (25, 1, 64)], (222, 61, 51)).add(world.buttons)
                    CustomTextButton((320, 300), 2, "      Decline      ", [(41, 98, 148), (54, 122, 187), (12, 40, 62), (15, 44, 86), (20, 54, 101), (4, 20, 52)], BLACK).add(world.buttons)
            self.curImageSet = Images.lich_die
            self.masks = Images.lich_die_masks
            if self.curIndex == 6:
                self.die(world)
                world.static.add(self)

        super().update(world)

    def move_horizontally(self, world, vx):
        success = super().move_horizontally(world, vx)
        if self.running and not self.jumping and not success:
            self.running = False
            self.jumping = True
            self.curIndex = 0

    def move_vertically(self, world, vy):
        success = super().move_vertically(world, vy)
        self.falling = success and vy > 0

    def damage(self, world, amount, type):
        super().damage(world, amount, type)
        if not self.hurt:
            self.hurt = True
            self.curIndex = 0
            self.health -= amount
            self.curImageSet = Images.lich_hurt
            self.masks = Images.lich_hurt_masks
            self.vx = 0
            if self.health <= 0:
                self.dead = True

    def die(self, world):
        super().die(world, 2)
        world.player.earnAchievment(world, "I'm going to make you an offer you can't refuse")
