import pygame
from random import randint

from projectile import *
from position_utilities import *
from images import Images

class Spell():
    colors = []
    costs = {}
    image = None
    effect = "ø"
    description = ""

    @classmethod
    def cast(cls, world):
        for color in cls.costs:
            c = cls.costs[color]
            if c == '*':
                c = world.player.get_max_mana(world)[color]
            elif c == 'x':
                c = world.player.mana[color]

            while c > 0:
                world.player.mana[color] -= 1
                c -= 1
        world.player.curIndex = 0
        world.player.casting = True
        world.player.curSpell = cls

    @classmethod
    def effectcast(cls, world):
        pass

    @classmethod
    def can_cast(cls, world):
        for color in cls.costs:
            c = cls.costs[color]
            if c == '*':
                c = world.player.get_max_mana(world)[color]
            elif c == 'x':
                c = world.player.mana[color]

            if world.player.mana[color] < c:
                return False
        return True

class PlanarStep(Spell):
    colors = ['l', 'w', 'f', 'd']
    costs = {'l': '*', 'w': '*', 'f': '*', 'd': '*'}
    image = Images.spellicons[54]
    effect = "ψ"
    description = "Transports the player over the plane, allowing travel to any part of the world"

    @classmethod
    def effectcast(cls, world):
        world.game.running = True
        world.planeswalking = -255

class Planeswalk(Spell):
    colors = ['l', 'w', 'f', 'd']
    costs = {'l': '*', 'w': '*', 'f': '*', 'd': '*'}
    image = Images.spellicons[55]
    effect = "ψ"
    description = "Transports the player into the world stage, allowing travel to any plane"

    @classmethod
    def effectcast(cls, world):
        world.game.running = False
        world.planeswalking = -255

class FireBolt(Spell):
    colors = ['f']
    costs = {'f': 2}
    image = Images.spellicons[13]
    effect = "⌖"
    description = "Throw a tiny fire bolt in the direction you are facing, dealing damage to the first thing it hits"

    @classmethod
    def effectcast(cls, world):
        world.sprites.add(Projectile(
            Coord(
                (world.player.rect.right - 96) if world.player.flip else world.player.rect.left,
                world.player.rect.top - 5
            ),
            (96, 96),
            -6 if world.player.flip else 6,
            0,
            -1,
            True,
            Images.fireball_medium,
            updateCallback=cls.projectile_callback
        ))

    def projectile_callback(projectile, world):
        for enemy in pygame.sprite.spritecollide(projectile, world.enemies, False):
            enemy.damage(world, 2, 'f')
            projectile.kill()

class Shield(Spell):
    colors = ['w']
    costs = {'w': 2}
    image = Images.spellicons[21]
    effect = "▼"
    description = "Ward yourself against the next point of non magical damage"

    @classmethod
    def effectcast(cls, world):
        if world.player.shielded == 0:
            world.player.shielded = 1

class Revitalize(Spell):
    colors = ['l']
    costs = {'l': 2}
    image = Images.spellicons[35]
    effect = "❤"
    description = "Attune with nature and regain one hit point"

    @classmethod
    def effectcast(cls, world):
        if world.player.health < world.player.max_health:
            world.player.health += 1

class Drain(Spell):
    colors = ['d']
    costs = {'d': 2}
    image = Images.spellicons[53]
    effect = "☠"
    description = "Drain the life force of the closest enemy and absorb some of it into yourself"

    @classmethod
    def effectcast(cls, world):
        closest = None
        for enemy in world.enemies:
            if enemy.rect.left < (WW*6)//4 and enemy.rect.right > 0:
                if world.player.flip and enemy.rect.left < world.player.rect.left:
                    if (closest is None or enemy.rect.left > closest.rect.left):
                        closest = enemy
                elif not world.player.flip and enemy.rect.left > world.player.rect.left:
                    if (closest is None or enemy.rect.left < closest.rect.left):
                        closest = enemy

        if closest is not None:
            if closest.damage(world, 3, 'd'):
                world.player.heal(randint(0, 3-closest.alignment), 'd')
                closest.particleCoat(world, (66, 3, 97), BLACK, 20)
            else:
                closest.particleCoat(world, (150, 150, 150), WHITE, 2)

"""
class BoltStrike(Spell):
    colors = ['p', 'c']
    costs = {'p': 3, 'c': 3}
    image = Images.spellicons[33]
    effect = "⚔❤"
    description = "Enhance your blade to deal one more damage and regain one hit point on your next hit"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # boltstrike callback
        # effect: +1 damage and +1 life on next melee hit

    def __str__():
        return 'level1-pc'

class LifeSteal(Spell):
    colors = ['f', 's']
    costs = {'f': 3, 's': 3}
    image = Images.spellicons[39]
    effect = "❤☠"
    description = "Steal the life force of your enemy, draining it and repleneshing yourself"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # lifesteal callback
        # effect: gain 1 life and deal 1 damage to target enemy

    def __str__():
        return 'level1-fs'

class Freeze(Spell):
    colors = ['p', 'w']
    costs = {'p': 3, 'w': 3}
    image = Images.spellicons[18]
    effect = "❅"
    description = "Freeze the closest enemy you are facing for a short period of time"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # freeze callback
        # effect targeted enemy freezes for a random amount of time based on its power level

    def __str__():
        return 'level1-pw'

class Grow(Spell):
    colors = ['f', 'w']
    costs = {'f': 3, 'w': 3}
    image = Images.spellicons[9]
    effect = "⚔♡+"
    description = "Grow yourself to deal more damage, jump higher, and have more hitpoints"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # grow callback
        # during cast grows by 1ps, deals +1 damage for duration, jump height doubled, speed unchanged, gives a number of temp hearts equal to the player's max health

    def __str__():
        return 'level1-fw'

class Agility(Spell):
    colors = ['s', 'w']
    costs = {'s': 3, 'w': 3}
    image = Images.spellicons[29]
    effect = "⚔+"
    description = "Increase your agility in all areas for a duration"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # agility callback
        # doubles speed, jump height, and improves wall climbing and rising from sliding

    def __str__():
        return 'level1-sw'

class Rage(Spell):
    colors = ['f', 'c']
    costs = {'f': 3, 'c': 3}
    image = Images.spellicons[12]
    effect = "⚔+"
    description = "Your Speed and Damage modifiers scale with the amount of damage that you have taken"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # rage callback
        # increases speed and damage by 1, and then an additional 1 when hit

    def __str__():
        return 'level1-fc'

class Vampirism(Spell):
    colors = ['c', 's']
    costs = {'c': 3, 's': 3}
    image = Images.spellicons[16]
    effect = "❤⚔"
    description = "Hits on unwounded enemies heal you, and hits on wounded enemies deal more damage"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # vampirism callback
        # melee hits against unwounded enemies heal 1, and melee hits against wounded enemies deal +2 damage

    def __str__():
        return 'level1-cs'

class Overgrow(Spell):
    colors = ['p', 'f']
    costs = {'p': 3, 'f': 3}
    image = Images.spellicons[37]
    effect = "❤♡❅"
    description = "The power of the forest heals you, absorbs future damage, and vines weaker enemies"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # overgrow callback
        # heal one, get a temp heart, and vines grow over the targeted enemy, who can then attempt to break free

    def __str__():
        return 'level1-pf'

class Summon(Spell):
    colors = ['p', 's']
    costs = {'p': 3, 's': 3}
    image = Images.spellicons[25]
    effect = "†"
    description = "Summon a weak zombie to pursue your enemies"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # summon callback
        # summons a zombie that slowly moves towards the cursor and both deals and takes damage

    def __str__():
        return 'level1-ps'

class Lightning(Spell):
    colors = ['c', 'w']
    costs = {'c': 3, 'w': 3}
    image = Images.spellicons[22]
    effect = "⌖"
    description = "Throw a fast moving lightning bolt that pierces enemies dealing considerable damage"

    @classmethod
    def effectcast(cls, world):
        world.player.curIndex = 0
        world.player.casting = True
        # lightning callback
        # fires a fast moving piercing bolt that deals 3 damage

    def __str__():
        return 'level1-cw'
"""