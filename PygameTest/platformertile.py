import pygame

from bitmaps.platformerTiles import *

class PlatformerTile(pygame.sprite.Sprite):

    def __init__(self, rect, tilekey, mask):
        super().__init__()
        self.rect = rect
        self.tilekey = tilekey
        self.mask = mask

        self.platform = False # if true, the bottom face becomes transparent
        if tilekey[0] == ['p']:
            self.platform = True
        self.ramp = 'none'
        if tilekey[0] == 'r':
            if tilekey == 'r-arga':
                self.ramp = '2tl-0'
            elif tilekey == 'r-aggr':
                self.ramp = '2tl-1'
            elif tilekey == 'r-aagr':
                self.ramp = '2tr-0'
            elif tilekey == 'r-argg':
                self.ramp = '2tr-1'
            elif tilekey == 'r-aagg-r':
                self.ramp = '1tl-0'
            elif tilekey == 'r-gaag-r':
                self.ramp = '1tr-0'

def getPlatformerTile(tilekey):
    if tilekey[0] in ['g', 'r']:
        if tilekey[2:] in grass_tiles:
            return grass_tiles[tilekey[2:]]
        else:
            return grass_tiles['gggg-5']
    elif tilekey[0] == 'a' and len(tilekey) > 1 and tilekey != 'a_':
        if tilekey == 'a-tree':
            return tree
        elif tilekey == 'a-large_tree':
            return large_tree
        else:
            return air_tiles[int(tilekey[2:])]
    return None