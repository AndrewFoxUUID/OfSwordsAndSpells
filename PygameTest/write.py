import pygame, pyperclip
from bitmaps.characters import *
from position_utilities import *
from constants import *

class TextEntry(pygame.sprite.Sprite):
    def __init__(self, name, coords, font_size, max_width, numeric=False):
        super().__init__()
        self.name = name
        self.rect = pygame.Rect(*coords, 6, font_size*5 + 6)
        self.focused = False
        self.cursor_pos = 0
        self.text_start = 0
        self.text = ""
        self.font_size = font_size
        self.max_width = max_width
        self.numeric = numeric

    def mouseButtonDown(self, pos):
        if self.rect.collidepoint(pos):
            self.focused = True
        else:
            self.focused = False

    def keydown(self, key):
        if not self.focused:
            return

        text = ""
        shift_held = pygame.key.get_pressed()[pygame.K_RSHIFT] or pygame.key.get_pressed()[pygame.K_LSHIFT]
        control_held = pygame.key.get_pressed()[pygame.K_RCTRL] or pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RMETA] or pygame.key.get_pressed()[pygame.K_LMETA]
        if key == pygame.K_RETURN or key == pygame.K_KP_ENTER: self.focused = False
        elif key == pygame.K_UP and self.numeric: self.text = str(int(self.text) + 1)
        elif key == pygame.K_DOWN and self.numeric: self.text = str(int(self.text) - 1)
        elif key == pygame.K_LEFT and self.cursor_pos > 0: self.cursor_pos -= 1
        elif key == pygame.K_RIGHT and self.cursor_pos < len(self.text): self.cursor_pos += 1
        elif key == pygame.K_BACKSPACE and self.cursor_pos > 0: self.text = self.text[:self.cursor_pos - 1] + self.text[self.cursor_pos:]; self.cursor_pos -= 1
        elif control_held and key == pygame.K_c: pyperclip.copy(self.text); return
        elif control_held and key == pygame.K_x: pyperclip.copy(self.text); self.text = ""; self.cursor_pos = 0; self.text_start = 0; return
        elif control_held and key == pygame.K_v: text = pyperclip.paste()
        elif key == pygame.K_SPACE: text = ' '
        elif key == pygame.K_EXCLAIM or key == pygame.K_1 and shift_held: text = '!'
        elif key == pygame.K_QUOTEDBL or key == pygame.K_QUOTE and shift_held: text = '"'
        elif key == pygame.K_QUOTE: text = '\''
        elif key == pygame.K_HASH or key == pygame.K_3 and shift_held: text = '#'
        elif key == pygame.K_DOLLAR or key == pygame.K_4 and shift_held: text = '$'
        elif key == pygame.K_AMPERSAND or key == pygame.K_7 and shift_held: text = '&'
        elif key == pygame.K_LEFTPAREN or key == pygame.K_9 and shift_held: text = '('
        elif key == pygame.K_RIGHTPAREN or key == pygame.K_0 and shift_held: text = ')'
        elif key == pygame.K_ASTERISK or key == pygame.K_8 and shift_held or key == pygame.K_KP_MULTIPLY: text = '*'
        elif key == pygame.K_PLUS or key == pygame.K_EQUALS and shift_held or key == pygame.K_KP_PLUS: text = '+'
        elif key == pygame.K_EQUALS or key == pygame.K_KP_EQUALS: text = '='
        elif key == pygame.K_LESS or key == pygame.K_COMMA and shift_held: text = '<'
        elif key == pygame.K_COMMA: text = ','
        elif key == pygame.K_UNDERSCORE or key == pygame.K_MINUS and shift_held: text = '_'
        elif key == pygame.K_MINUS or key == pygame.K_KP_MINUS: text = '-'
        elif key == pygame.K_GREATER or key == pygame.K_PERIOD and shift_held: text = '>'
        elif key == pygame.K_PERIOD or key == pygame.K_KP_PERIOD: text = '.'
        elif key == pygame.K_QUESTION or key == pygame.K_SLASH and shift_held: text = '?'
        elif key == pygame.K_SLASH or key == pygame.K_KP_DIVIDE: text = '/'
        elif key == pygame.K_COLON or key == pygame.K_SEMICOLON and shift_held: text = ':'
        elif key == pygame.K_SEMICOLON: text = ';'
        elif key == pygame.K_AT or key == pygame.K_2 and shift_held: text = '@'
        elif key == pygame.K_LEFTBRACKET and shift_held: text = '{'
        elif key == pygame.K_LEFTBRACKET: text = '['
        elif key == pygame.K_RIGHTBRACKET and shift_held: text = '}'
        elif key == pygame.K_RIGHTBRACKET: text = ']'
        elif key == pygame.K_BACKSLASH and shift_held: text = '|'
        elif key == pygame.K_BACKSLASH: text = '\\'
        elif key == pygame.K_CARET or key == pygame.K_6 and shift_held: text = '^'
        elif key == pygame.K_BACKQUOTE and shift_held: text = '~'
        elif key == pygame.K_BACKQUOTE: text = '`'
        elif key >= pygame.K_0 and key <= pygame.K_9: text = pygame.key.name(key)
        elif key >= pygame.K_a and key <= pygame.K_z: text = (pygame.key.name(key).upper() if shift_held else pygame.key.name(key))

        if self.numeric and not (text == '' or text.isnumeric()):
            return

        self.text = self.text[:self.cursor_pos] + text + self.text[self.cursor_pos:]
        self.cursor_pos += len(text)

        if self.numeric and not self.text.isnumeric():
            self.text = "0"

        if (writtenlen(self.text) + 6)*self.font_size + 6 > self.max_width:
            length = len(self.text)
            while writtenlen(self.text[self.text_start : self.text_start + length])*self.font_size + 6 > self.max_width:
                length -= 1

            while self.cursor_pos > self.text_start + length:
                self.text_start += 1
            while self.cursor_pos < self.text_start:
                self.text_start -= 1
        else:
            self.text_start = 0

    def draw(self, win, tick):
        self.rect = pygame.Rect(self.rect.left, self.rect.top, min((writtenlen(self.text) + 6)*self.font_size + 6, self.max_width), self.font_size*5 + 6)
        pygame.draw.rect(win, WHITE, self.rect, 0, 4)
        pygame.draw.rect(win, YELLOW if self.focused else (100, 100, 100), self.rect, 1, 4)
        length = len(self.text)
        while writtenlen(self.text[self.text_start : self.text_start + length])*self.font_size + 6 > self.max_width:
            length -= 1
        write(win, self.text[self.text_start : self.text_start + length], (self.rect.left + 3, self.rect.top + 3), BLACK, self.font_size)
        if self.focused and tick % 50 < 40:
            pygame.draw.rect(win, BLACK, (self.rect.left + 2 + writtenlen(self.text[self.text_start : self.cursor_pos])*self.font_size, self.rect.top + 2, self.font_size, 7*self.font_size))


def write(surface, string, coord, color=WHITE, size=1, allowSpecialCharacters=False):
    if type(coord) == tuple:
        coord = Coord(coord[0], coord[1])
    x_indent = 0
    y_indent = 0
    original_color = color
    detecting_new_color = False
    for letter in string.lower():
        if letter == '\n':
            y_indent += 6*size
            x_indent = 0
        elif allowSpecialCharacters and letter == '<':
            detecting_new_color = True
            color = (0,)
        elif allowSpecialCharacters and letter == '>':
            color = original_color
        elif allowSpecialCharacters and detecting_new_color and letter == ':':
            detecting_new_color = False
        elif allowSpecialCharacters and detecting_new_color and letter == ',':
            color = (*color, 0)
        elif allowSpecialCharacters and detecting_new_color:
            color = tuple(list(color)[:-1] + [color[-1]*10 + int(letter)])
        else:
            for r, row in enumerate(characters[letter]):
                for c, item in enumerate(row):
                    if item == 1:
                        pygame.draw.rect(surface, color, (coord.x + size*x_indent + size*c, coord.y + y_indent + size*r, size, size))
            x_indent += len(characters[letter][0]) + 1

def writtenlen(string):
    length = 0
    for letter in string.lower():
        length += len(characters[letter][0]) + 1
    return length - 1