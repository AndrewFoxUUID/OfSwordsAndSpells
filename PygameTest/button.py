import pygame

from bitmaps.ui import *
from utilityclasses import Bitmap
from write import *
from images import Images
from constants import *

class Button(pygame.sprite.Sprite):

    def __init__(self, bitmap, focused_bitmap, coords, ps):
        super().__init__()
        self.ps = ps

        if bitmap is None:
            self.win = pygame.Surface((1, 1), pygame.SRCALPHA)
        elif type(bitmap) == Bitmap:
            self.win = pygame.Surface((len(bitmap[0]), len(bitmap)), pygame.SRCALPHA)
            self.win.fill(CLEAR)
            for r, row in enumerate(bitmap):
                for c, item in enumerate(row):
                    if item != 0:
                        pygame.draw.rect(self.win, bitmap.colors[item], (c, r, 1, 1))
        else:
            self.win = bitmap
        
        if focused_bitmap is None:
            self.focused_win = pygame.Surface((1, 1), pygame.SRCALPHA)
        elif type(focused_bitmap) == Bitmap:
            self.focused_win = pygame.Surface((len(bitmap[0]), len(bitmap)), pygame.SRCALPHA)
            self.focused_win.fill(CLEAR)
            for r, row in enumerate(focused_bitmap):
                for c, item in enumerate(row):
                    if item != 0:
                        pygame.draw.rect(self.focused_win, focused_bitmap.colors[item], (c, r + (len(bitmap) - len(focused_bitmap)), 1, 1))
        else:
            self.focused_win = focused_bitmap
        
        self.rect = pygame.Rect(*coords, self.win.get_width()*ps, self.win.get_height()*ps)
        self.focused = False

    def draw(self, win, game):
        win.blit(pygame.transform.scale(self.focused_win if self.focused else self.win, self.rect.size), self.rect.topleft)

class Xbutton(Button):

    def __init__(self, coords=(965, 10), ps=1):
        super().__init__(
            Bitmap(x_button, x_button_colors),
            Bitmap(x_button_pressed, x_button_pressed_colors),
            coords,
            ps
        )

class CheckBox(Button):

    def __init__(self, name, coords, ps=1, checked=False):
        super().__init__(
            Images.checkbox_empty,
            Images.checkbox_filled,
            coords,
            ps
        )
        self.name = name
        self.checked = checked

    def draw(self, win, game):
        win.blit(pygame.transform.scale(Images.checkbox_filled if self.checked else Images.checkbox_empty, (15*self.ps, 15*self.ps)), self.rect.topleft)

class CustomTextButton(Button):

    def __init__(self, coords, ps, text, colors, text_color=BLACK):
        self.text = text
        super().__init__(
            Bitmap(
                [custom_button_left[i] + [custom_button_middle[i][0] for j in range(writtenlen(text))] + custom_button_right[i] for i in range(13)],
                [None, BLACK] + colors[:3]
            ),
            Bitmap(
                [custom_button_pressed_left[i] + [custom_button_pressed_middle[i][0] for j in range(writtenlen(text))] + custom_button_pressed_right[i] for i in range(12)],
                [None, BLACK] + colors[3:]
            ),
            coords,
            ps
        )
        
        write(self.win, text, (3, 2), text_color)
        write(self.focused_win, text, (3, 3), text_color)

class InventoryButton(Button):

    def __init__(self, coords, item, ps, i):
        self.i = i
        self.h = 0
        self.item = item
        super().__init__(
            Images.itembase[0],
            Images.itembase[12],
            coords,
            ps
        )

    def draw(self, win, game):
        win.blit(pygame.transform.scale(Images.itembase[self.h], (20*self.ps, 20*self.ps)), self.rect.topleft)
        win.blit(pygame.transform.scale(self.item.image, (16*self.ps, 16*self.ps)), (self.rect.left + 2*self.ps, self.rect.top + 2*self.ps))
        write(win, str(self.item.amount), (self.rect.left + 48, self.rect.top + 44), WHITE, 2)

class SpellButton(Button):
    
    def __init__(self, coords, spell, ps):
        self.h = 0
        self.spell = spell
        super().__init__(
            Images.spellhighlight[0],
            Images.spellhighlight[10],
            coords,
            ps
        )

    def draw(self, win, game):
        self.spell.image.set_alpha(255 if self.spell.can_cast(game) else 50)
        win.blit(pygame.transform.scale(self.spell.image, (24*self.ps, 24*self.ps)), self.rect.topleft)
        win.blit(pygame.transform.scale(Images.spellhighlight[self.h], (24*self.ps, 24*self.ps)), self.rect.topleft)

class ColorPickerButton(Button):

    def __init__(self, coords, ps=2):
        super().__init__(
            Bitmap(color_picker_button, color_picker_button_colors),
            Bitmap(color_picker_button_pressed, color_picker_button_pressed_colors),
            coords,
            ps
        )

class LeftButton(Button):

    def __init__(self, coords, ps=2):
        super().__init__(
            Bitmap([row[::-1] for row in right_arrow], dark_arrow_colors),
            Bitmap([row[::-1] for row in right_arrow], dark_arrow_colors),
            coords,
            ps
        )

class RightButton(Button):

    def __init__(self, coords, ps=2):
        super().__init__(
            Bitmap(right_arrow, dark_arrow_colors),
            Bitmap(right_arrow, dark_arrow_colors),
            coords,
            ps
        )


class NPCButton(Button):

    def __init__(self, imageSet, coords, ps):
        super().__init__(imageSet[0], imageSet[0], coords, ps)
        self.curIndex = 0
        self.imageSet = imageSet
        self.tick = 0

    def draw(self, win, game):
        super().draw(win, game)
        self.tick += 1
        if self.tick % 5 == 0:
            self.curIndex += 1
            if self.curIndex >= len(self.imageSet):
                self.curIndex = 0
            self.win = self.imageSet[self.curIndex]

class DialogButton(Button):

    def __init__(self, text, coords, ps, allowSpecialCharacters = False):
        super().__init__(None, None, coords, ps)
        self.text = text
        self.allowSpecialCharacters = allowSpecialCharacters

    def draw(self, win, game):
        write(win, self.text, self.rect.topleft, BLACK, self.ps, self.allowSpecialCharacters)


class ToggleButton(pygame.sprite.Sprite):

    def __init__(self, coords, ps, active, colors, text):
        super().__init__()
        self.focused = False
        self.rect = pygame.Rect(coords[0], coords[1], 55*ps, 27*ps)
        self.active = active
        self.ps = ps

        self.left_surface = pygame.Surface((55*ps, 27*ps), pygame.SRCALPHA)
        for r, row in enumerate(toggle_button_inactive):
            for c, item in enumerate(row):
                if item != 0:
                    pygame.draw.rect(self.left_surface, colors[item], [c*ps, r*ps, ps, ps])
        self.center_surface = pygame.Surface((55*ps, 27*ps), pygame.SRCALPHA)
        for r, row in enumerate(toggle_button_center):
            for c, item in enumerate(row):
                if item != 0:
                    pygame.draw.rect(self.center_surface, colors[item], [c*ps, r*ps, ps, ps])
        self.right_surface = pygame.Surface((55*ps, 27*ps), pygame.SRCALPHA)
        for r, row in enumerate(toggle_button_active):
            for c, item in enumerate(row):
                if item != 0:
                    pygame.draw.rect(self.right_surface, colors[item], [c*ps, r*ps, ps, ps])

        self.text = text

    def draw(self, win, game):
        write(win, self.text, (self.rect.left, self.rect.top), BLACK, self.ps+1)
        if self.focused:
            win.blit(self.center_surface, (self.rect.left, self.rect.top + 14*self.ps))
        elif self.active:
            win.blit(self.right_surface, (self.rect.left, self.rect.top + 14*self.ps))
        else:
            win.blit(self.left_surface, (self.rect.left, self.rect.top + 14*self.ps))
