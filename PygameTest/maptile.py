from images import Images
from utilityclasses import *
from position_utilities import *

class MapTile:

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def draw(self, win, start=Coord(0,0), base=False):
        if type(start) == ScreenCoord:
            start = start.get_topleft()
        win.blit(self.image, (start.x, start.y))
        #if base:
        #    start.y += 15*ps
        #    for r, row in enumerate(tile_base_bitmap):
        #        for c, item in enumerate(row):
        #            if item != 0:
        #                x = start.x + ps * c
        #                y = start.y + ps * r
        #                if color == None:
        #                    c = tile_base_bitmap.colors[item]
        #                else:
        #                    c = color
        #                pygame.draw.rect(win, c, (x, y, ps, ps))

tile_wins = {}
for tile in Images.tiles:
    surface = pygame.Surface((64, 96), pygame.SRCALPHA)
    surface.blit(pygame.transform.scale(Images.tiles[tile], (64, 96)), (0, 0))
    tile_wins[tile] = surface
for overlay in Images.overlays:
    surface = pygame.Surface((64, 96), pygame.SRCALPHA)
    surface.blit(pygame.transform.scale(Images.overlays[overlay], (64, 96)), (0, 0))
    tile_wins[overlay] = surface