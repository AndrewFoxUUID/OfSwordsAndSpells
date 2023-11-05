import pygame
from bitmaps.player import *

pygame.init()
win = pygame.display.set_mode((WW, WH), pygame.SRCALPHA)

colors = colors

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    win.fill((255,255,255))
    for y, row in enumerate(image):
        for x, item in enumerate(row):
            if item != 0:
                pygame.draw.rect(win, colors[item], [x*4 + 16, y*4 + 16, 4, 4])
    pygame.display.update()

pygame.quit()