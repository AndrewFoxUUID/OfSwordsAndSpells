import pygame, os
from random import randint

from write import *
from button import *
from utilities import *
from worlds import *
from player import Player
from images import Images

class NewPlayer():

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)
        pygame.display.set_caption("New Player")
        pygame.mouse.set_cursor((16, 16), (7, 7), *pygame.cursors.compile(cursor, black='X', white='.', xor='o'))

        self.running = True
        self.tick = 0

        self.open = False
        self.book_stage = 0
        self.direction = 1

        self.player_index = 0

        self.nameInput = TextEntry("name", (315, 150), 2, 160)

        self.race = "human"
        self.humanRect = pygame.Rect(315, 220, 55, 70)

        self.buttons = pygame.sprite.Group()

        self.skipTutorial = CheckBox('skipTutorial', (685, 130))
        self.skipTutorial.add(self.buttons)

        Xbutton((675, 90)).add(self.buttons)
        CustomTextButton((555, 330), 2, "create player", [(60, 94, 139), (45, 70, 110), (37, 58, 94), (45, 70, 110), (37, 58, 94), (10, 20, 50)]).add(self.buttons)

        self.run()

    def mouseButtonUp(self, event):
        if self.humanRect.collidepoint(event.pos):
            self.race = "human"

    def create(self):
        if not os.path.exists("data/" + self.nameInput.text + "/"):
            os.mkdir("data/" + self.nameInput.text)
        if not os.path.exists("data/" + self.nameInput.text + "/worlds/"):
            os.mkdir("data/" + self.nameInput.text + "/worlds")
        Worlds(Player(self.nameInput.text, self.race, self.skipTutorial.checked))

    def run(self):
        while self.running:
            self.tick += 1
            self.win.fill(CLEAR)

            self.win.blit(pygame.transform.scale(Images.menubooks[self.book_stage], (157*3, 160*3)), (WH - 157*3//2, 0))

            if self.open:
                if self.tick % 100 == 0:
                    if self.book_stage != 3:
                        self.book_stage += self.direction
                    if self.book_stage >= 7:
                        self.book_stage = 3
                if self.book_stage == 3:
                    write(self.win, "name:", (315, 130), BLACK, 3)
                    self.nameInput.draw(self.win, self.tick)

                    write(self.win, "race:", (315, 200), BLACK, 3)
                    self.win.blit(Images.human_idle[0], (300, 215))
                    write(self.win, "human", (320, 272), BLACK, 2)
                    pygame.draw.rect(self.win, YELLOW if self.race == "human" else (100, 100, 100), self.humanRect, 2, 5)

                    write(self.win, "skip tutorial", (525, 130), BLACK, 3)

                    for button in self.buttons:
                        button.draw(self.win, self)

            elif self.tick % 5 == 0:
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
                    self.nameInput.mouseButtonDown(event.pos)
                    for button in self.buttons:
                        button.focused = button.rect.collidepoint(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP:
                    for button in self.buttons:
                        button.focused = False
                        if button.rect.collidepoint(event.pos):
                            if isinstance(button, Xbutton):
                                self.running = False
                            elif isinstance(button, CustomTextButton) and button.text == "create player":
                                self.running = False
                                self.create()
                            elif isinstance(button, CheckBox):
                                button.checked = not button.checked
                    self.mouseButtonUp(event)
                elif event.type == pygame.KEYDOWN:
                    self.nameInput.keydown(event.key)
                    