import pygame

from position_utilities import *
import bitmaps.ui as ui_bitmaps
from button import *
from write import *
from utilities import *
from images import Images

class SkinEditor():

    def __init__(self, player):
        self.player = player
        pygame.init()
        self.win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        pygame.display.set_caption("Edit " + player.name + "'s Skin")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.running = True
        self.tick = 0

        self.open = False
        self.book_stage = 0
        self.direction = 1

        self.buttons = pygame.sprite.Group()
        Xbutton((660, 90)).add(self.buttons)
        CustomTextButton((315, 340), 2, "save", [(60, 94, 139), (45, 70, 110), (37, 58, 94), (45, 70, 110), (37, 58, 94), (10, 20, 50)]).add(self.buttons)
        ColorPickerButton((520, 220)).add(self.buttons)

        self.cur_color = BLACK
        self.focused = 'n'
        self.color_picking = False

        self.run()

    def run(self):
        while self.running:
            self.tick += 1
            self.win.fill(CLEAR)

            self.win.blit(pygame.transform.scale(Images.menubooks[self.book_stage], (190*3, 160*3)), (215, 0))

            if self.open:
                if self.tick % 100 == 0:
                    if self.book_stage != 3:
                        self.book_stage += self.direction
                    if self.book_stage >= 7:
                        self.book_stage = 3

                if self.book_stage == 3:
                    self.player.idle()
                    self.player.curIndex = 0
                    self.player.draw(self, Coord(100, -70), 5)

                    pygame.draw.rect(self.win, self.cur_color, (515, 100, 140, 50), 0, 4)

                    write(self.win, "red:", (520, 160), BLACK, 2)
                    self.red_rect = pygame.Rect(580, 158, 50, 14)
                    pygame.draw.rect(self.win, WHITE, self.red_rect, 0, 4)
                    pygame.draw.rect(self.win, YELLOW if self.focused == 'r' else (150, 150, 150), self.red_rect, 1, 4)
                    write(self.win, str(self.cur_color[0]), (585, 160), BLACK, 2)

                    write(self.win, "green:", (520, 180), BLACK, 2)
                    self.green_rect = pygame.Rect(580, 178, 50, 14)
                    pygame.draw.rect(self.win, WHITE, self.green_rect, 0, 4)
                    pygame.draw.rect(self.win, YELLOW if self.focused == 'g' else (150, 150, 150), self.green_rect, 1, 4)
                    write(self.win, str(self.cur_color[1]), (585, 180), BLACK, 2)

                    write(self.win, "blue:", (520, 200), BLACK, 2)
                    self.blue_rect = pygame.Rect(580, 198, 50, 14)
                    pygame.draw.rect(self.win, WHITE, self.blue_rect, 0, 4)
                    pygame.draw.rect(self.win, YELLOW if self.focused == 'f' else (150, 150, 150), self.blue_rect, 1, 4)
                    write(self.win, str(self.cur_color[2]), (585, 200), BLACK, 2)
                    
                    for button in self.buttons:
                        button.draw(self.win)

            elif self.tick % 100 == 0:
                self.book_stage += 1
                if self.book_stage == 3:
                    self.open = True

            pygame.display.update()

            if self.tick > TICKLIM:
                self.tick = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in self.buttons:
                        if isinstance(button, ColorPickerButton):
                            button.focused = self.color_picking
                        else:
                            button.focused = button.rect.collidepoint(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        if not isinstance(button, ColorPickerButton): button.focused = False
                        if button.rect.collidepoint(event.pos):
                            if isinstance(button, Xbutton):
                                self.running = False
                            elif isinstance(button, CustomTextButton) and button.text == "save":
                                pass
                            elif isinstance(button, ColorPickerButton):
                                self.color_picking = not self.color_picking
                                button.focused = self.color_picking

                    if self.red_rect.collidepoint(event.pos):
                        self.focused = 'r'
                    elif self.green_rect.collidepoint(event.pos):
                        self.focused = 'g'
                    elif self.blue_rect.collidepoint(event.pos):
                        self.focused = 'f'
                    else:
                        self.focused = 'n'
                    
                    if not self.color_picking and event.pos[0] >= 294 and event.pos[0] <= 389 and event.pos[1] >= 94 and event.pos[1] <= 319:
                        coords = Coord((event.pos[0]-295) // 5 + 39, (event.pos[1]-94) // 5 + 33)
                        if type(hero_bitmaps.idle_set[0][coords.y][coords.x]) == str:
                            self.player.colors[hero_bitmaps.idle_set[0][coords.y][coords.x]] = self.cur_color
                    if self.color_picking:
                        self.cur_color = self.win.get_at(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.cur_color = (
                            self.cur_color[0] // 10 if self.focused == 'r' else self.cur_color[0],
                            self.cur_color[1] // 10 if self.focused == 'g' else self.cur_color[1],
                            self.cur_color[2] // 10 if self.focused == 'f' else self.cur_color[2]
                        )
                    elif event.key == pygame.K_UP:
                        self.cur_color = (
                            min(self.cur_color[0] + 1, 255) if self.focused == 'r' else self.cur_color[0],
                            min(self.cur_color[1] + 1, 255) if self.focused == 'g' else self.cur_color[1],
                            min(self.cur_color[2] + 1, 255) if self.focused == 'f' else self.cur_color[2]
                        )
                    elif event.key == pygame.K_DOWN:
                        self.cur_color = (
                            max(self.cur_color[0] - 1, 0) if self.focused == 'r' else self.cur_color[0],
                            max(self.cur_color[1] - 1, 0) if self.focused == 'g' else self.cur_color[1],
                            max(self.cur_color[2] - 1, 0) if self.focused == 'f' else self.cur_color[2]
                        )
                    elif pygame.key.name(event.key) in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.cur_color = (
                            min(self.cur_color[0] * 10 + int(pygame.key.name(event.key)), 255) if self.focused == 'r' else self.cur_color[0],
                            min(self.cur_color[1] * 10 + int(pygame.key.name(event.key)), 255) if self.focused == 'g' else self.cur_color[1],
                            min(self.cur_color[2] * 10 + int(pygame.key.name(event.key)), 255) if self.focused == 'f' else self.cur_color[2]
                        )
