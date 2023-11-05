from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import pygame

class Coord():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if other != None:
            if type(other) == type(self):
                return (self.x == other.x) and (self.y == other.y)
        return False

    def __hash__(self):
        return hash((self.x, self.y))

    def ex(self):
        return (self.x, self.y)

class MapCoord(Coord):

    def __init__(self, world, x, y):
        super().__init__(x, y)
        self.world = world

    def screen_coords(self):
        return ScreenCoord(
            self.world,
            (self.x + 7) * 48,
            (self.y + 9) * 28
        )

    def get_range(self, radius: int = 1) -> list:
        lens = []
        for i in range(1, radius+2):
            lens.append(i)
        for i in range(1, radius+1):
            lens.append(radius)
            lens.append(radius+1)
        for i in list(range(1, radius+1))[::-1]:
            lens.append(i)

        tiles = []
        for i, y in enumerate(range(radius*-2, radius*2 + 1)):
            for x in range(1, (lens[i]//2)*2, 2):
                tiles.append(MapCoord(self.world, self.x-x-(lens[i]%2), self.y+y))
                tiles.append(MapCoord(self.world, self.x+x+(lens[i]%2), self.y+y))
            for x in range(lens[i]%2):
                tiles.append(MapCoord(self.world, self.x, self.y+y))

        return tiles

    def __str__(self):
        return "Map: " + super().__str__()

    def hash(self):
        return hash(("mc", self.x, self.y))

class ScreenCoord(Coord):

    def __init__(self, world, x, y):
        super().__init__(x, y)
        self.world = world

    def map_coords(self):
        column_possibilities = [self.x // 48 - 7]
        if self.x - (48 * column_possibilities[0]) < 0:
            column_possibilities.append(self.x // 48 - 8)
        elif (48 * column_possibilities[0]) - (self.x + 64) < 0:
            column_possibilities.append(self.x // 48 - 6)
        base_row = (self.y + 28) // 28 - 9

        for c in column_possibilities:
            if base_row % 2 != c % 2:
                r = base_row - 1
            else:
                r = base_row
            tile = MapCoord(self.world, c, r)
            if tile.screen_coords().check_intersection(self):
                return tile

    def get_vertices(self, ex=False) -> list:
        vertices = [
            ScreenCoord(self.world, self.x - 32, self.y), # left
            ScreenCoord(self.world, self.x - 14, self.y - 28), # top left
            ScreenCoord(self.world, self.x + 16, self.y - 28), # top right
            ScreenCoord(self.world, self.x + 34, self.y), # right
            ScreenCoord(self.world, self.x + 16, self.y + 30), # bottom right
            ScreenCoord(self.world, self.x - 14, self.y + 30), # bottom left
        ]
        if ex:
            return [vert.ex() for vert in vertices]
        else:
            return vertices

    def get_topleft(self):
        return ScreenCoord(self.world, self.x - 30, self.y - 26)

    def check_intersection(self, point: Coord) -> bool:
        polygon = Polygon(self.get_vertices(True))
        point = Point(point.x, point.y)
        return polygon.contains(point)

    def get_spell(self) -> str: # TODO (with spellbook rebuild)
        spell_index = (self.y - 40) // 21
        if spell_index < 0 or spell_index >= len(self.world.player.spell_slots):
            return None
        return self.world.player.spell_slots[spell_index]

    def __str__(self):
        return "Screen: " + super().__str__()

    def __hash__(self):
        return hash(("sc", self.x, self.y))