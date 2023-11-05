import os, pygame

from worldmap import *

class Malleandor(WorldMap):
    
    def __init__(self, game, player):
        super().__init__(game, player)
        pygame.display.set_caption("Malleandor")

        if not os.path.exists(f"data/{self.player.name}/worlds/malleandor/"):
            os.mkdir(f"data/{self.player.name}/worlds/malleandor")
        if not os.path.exists(f"data/{self.player.name}/worlds/malleandor/tileViews/"):
            os.mkdir(f"data/{self.player.name}/worlds/malleandor/tileViews")
        try:
            save = importlib.import_module(f"data.{self.player.name}.worlds.malleandor.worlddata")
            self.map = save.mapsave
            self.player_coords = MapCoord(self, *save.player_coords)
        except Exception as e:

            self.player_coords = MapCoord(self, 16, 32)

        self.save()

        self.run()

    def save(self):
        f = open(f"data/{self.player.name}/worlds/malleandor/worlddata.py", "w")
        f.write(f"player_coords = {self.player_coords.ex()}\n")
        f.write("mapsave = [\n")
        for line in self.map:
            f.write(f"    {line},\n")
        f.write("]\n")
        f.close()
