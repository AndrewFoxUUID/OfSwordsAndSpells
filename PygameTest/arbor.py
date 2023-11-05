import os, pygame
from random import choice

from worldmap import *

class Arbor(WorldMap):

    def __init__(self, game, player):
        super().__init__(game, player)
        pygame.display.set_caption("Arbor")

        if not os.path.exists(f"data/{self.player.name}/worlds/arbor/"):
            os.mkdir(f"data/{self.player.name}/worlds/arbor")
        if not os.path.exists(f"data/{self.player.name}/worlds/arbor/tileViews/"):
            os.mkdir(f"data/{self.player.name}/worlds/arbor/tileViews")
        try:
            save = importlib.import_module(f"data.{self.player.name}.worlds.arbor.worlddata")
            self.map = save.mapsave
            self.graveyards = save.graveyards
            self.player_coords = MapCoord(self, *save.player_coords)
        except Exception as e:
            self.map = []
            self.graveyards = []
            graveyard_acceptors = []
            for row in world_base:
                self.map.append([])
                for item in row:
                    self.map[-1].append(choice(WORLD_COMPOSITION_MAP['arbor'][item]))
                    if self.map[-1][-1] in GRAVEYARD_ACCEPTORS:
                        graveyard_acceptors.append((len(self.map[-1])-1, len(self.map)-1))

            if len(graveyard_acceptors) == 0:
                for r, row in enumerate(world_base):
                    for c, item in enumerate(row):
                        if item in TRANSITION_SWAMP + SWAMP:
                            self.map[r][c] = 'bog'
                            graveyard_acceptors.append((c, r))

            acceptors_passed = 0
            for acceptor in graveyard_acceptors:
                if randint(1, len(graveyard_acceptors)-acceptors_passed) == 1:
                    self.map[acceptor[1]][acceptor[0]] += '-graveyard'
                    acceptors_passed = 0
                    self.graveyards.append(acceptor)
                else:
                    acceptors_passed += 1

            self.player_coords = MapCoord(self, 16, 32)

        self.save()

        self.run()

    def save(self):
        f = open(f"data/{self.player.name}/worlds/arbor/worlddata.py", "w")
        f.write(f"player_coords = {self.player_coords.ex()}\n")
        f.write("mapsave = [\n")
        for line in self.map:
            f.write(f"    {line},\n")
        f.write("]\n")
        f.write(f"graveyards = {self.graveyards}")
        f.close()
