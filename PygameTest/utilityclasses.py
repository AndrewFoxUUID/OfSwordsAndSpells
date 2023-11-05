import pygame

from images import Images
from write import *
from spells import *
from constants import *

class Bitmap():

    def __init__(self, arr, colors, name="", i=0):
        self.bitmap = arr
        self.colors = colors
        self.name = name
        self.i = i

    def __getitem__(self, indices):
        return self.bitmap.__getitem__(indices)

    def __setitem__(self, indices, values):
        return self.bitmap.__setitem__(indices, values)

    def __len__(self):
        return self.bitmap.__len__()


class EquipmentHolder(pygame.sprite.Sprite):

    def __init__(self, c, r):
        super().__init__()
        offset = (WW//6 - 120) // 3
        if c == 0:
            self.rect = pygame.Rect(offset, offset + r * (60 + offset), 60, 60)
        if c == 1:
            self.rect = pygame.Rect(WW//6 - offset - 60, offset + r * (60 + offset), 60, 60)
        self.phase = 0

    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.phase < 12:
                self.phase += 1
        else:
            self.phase = 0

    def draw(self, win):
        win.blit(pygame.transform.scale(Images.itembase[self.phase], (60, 60)), self.rect)


class SpellUI(pygame.sprite.Sprite):

    def __init__(self, i):
        super().__init__()
        self.i = i

        self.rect = pygame.Rect(834, 5 + 52*i, 166, 52)
        if i == 8:
            self.rect = pygame.Rect(859, 425, 48, 48)
        elif i == 9:
            self.rect = pygame.Rect(925, 425, 48, 48)

        self.phase = 0

    def update(self, world):
        spell = world.player.spell_slots[self.i]
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.phase < 10:
                self.phase += 1
        else:
            self.phase = 0

    def draw(self, world):
        spell = world.player.spell_slots[self.i]
        if spell != Spell:
            left = self.rect.left
            if spell not in [PlanarStep, Planeswalk]:
                left += 20
            if spell.can_cast(world):
                spell.image.set_alpha(255)
                world.ui_layer.blit(pygame.transform.scale(spell.image, (48, 48)), (left, self.rect.top))
            else:
                spell.image.set_alpha(50)
                world.ui_layer.blit(pygame.transform.scale(spell.image, (48, 48)), (left, self.rect.top))

            world.ui_layer.blit(pygame.transform.scale(Images.spellhighlight[self.phase], (48, 48)), (left, self.rect.top))

            if spell not in [PlanarStep, Planeswalk]:
                indent = self.rect.left + 74
                for color in spell.colors:
                    write(world.ui_layer, str(spell.costs[color]), (indent, self.rect.top + 18), MANA_COLORS[color], 2)
                    indent += 12
                write(world.ui_layer, "→ " + spell.effect, (indent, self.rect.top + 18), BLACK, 2)