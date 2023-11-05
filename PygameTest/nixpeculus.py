import os, pygame

from worldmap import *

class Nixpeculus(WorldMap):

    def __init__(self, game, player):
        super().__init__(game, player)
        pygame.display.set_caption("Nixpeculus")

        if not os.path.exists(f"data/{self.player.name}/worlds/nixpeculus/"):
            os.mkdir(f"data/{self.player.name}/worlds/nixpeculus")
        if not os.path.exists(f"data/{self.player.name}/worlds/nixpeculus/tileViews/"):
            os.mkdir(f"data/{self.player.name}/worlds/nixpeculus/tileViews")
        try:
            save = importlib.import_module(f"data.{self.player.name}.worlds.nixpeculus.worlddata")
            self.map = save.mapsave
            self.graveyards = save.graveyards
            self.player_coords = MapCoord(self, *save.player_coords)
        except Exception as e:
            arbor = importlib.import_module(f"data.{self.player.name}.worlds.arbor.worlddata")
            self.map = arbor.mapsave
            self.graveyards = arbor.graveyards

            for row in self.map:
                for i, item in enumerate(row):
                    if item is None: continue
                    
                    overlay = None
                    if item.find('-') != -1:
                        overlay = item[item.find('-')+1:]
                        item = item[:item.find('-')]

                    if item == 'meadow':
                        row[i] = 'snow'
                    elif item == 'rolling_meadow':
                        row[i] = 'snowy_meadow'
                    elif item == 'growing_meadow':
                        row[i] = 'snowy_meadow'
                    elif item == 'hills':
                        row[i] = 'snowy_meadow'
                    elif item == 'rocky_hills':
                        row[i] = 'snowy_rocky_hills'
                    elif item == 'stony_hills':
                        row[i] = 'snow_covered_hills'
                    elif item == 'wooded_meadow':
                        row[i] = 'snow_covered_wooded_meadow'
                    elif item == 'wooded_hills':
                        row[i] = 'snowy_wooded_meadow'
                    elif item == 'marsh':
                        row[i] = 'icy_water'
                    elif item == 'wetland':
                        row[i] = 'frozen_water'
                    elif item == 'lake':
                        row[i] = 'icy_deep_water'
                    elif item == 'rocky_forest':
                        row[i] = 'snow_covered_rocky_wooded_hills'
                    elif item == 'hilly_rocky_forest':
                        row[i] = 'snowy_hilly_rocky_forest'
                    elif item == 'forest':
                        row[i] = 'snow_covered_forest'
                    elif item == 'hilly_forest':
                        row[i] = 'snowy_forest'
                    elif item == 'overgrown_forest':
                        row[i] = 'snowy_castle'
                    elif item == 'jungle':
                        row[i] = 'snowy_monument'
                    elif item == 'plains':
                        row[i] = 'snowy_village'
                    elif item == 'flooded_plains':
                        row[i] = 'snowy_town'
                    elif item == 'bog':
                        row[i] = 'snow'
                    elif item == 'wet_bog':
                        row[i] = 'snow'
                    elif item == 'bog_lake':
                        row[i] = 'snow'
                    elif item == 'rolling_bog':
                        row[i] = 'snow'
                    elif item == 'wooded_bog':
                        row[i] = 'snow_covered_wooded_meadow'
                    elif item == 'jungle_swamp':
                        row[i] = 'snow_covered_rocky_wooded_hills'
                    elif item == 'overgrown_bog':
                        row[i] = 'snowy_city'
                    elif item == 'swamp':
                        row[i] = 'snow'
                    elif item == 'overgrown_swamp':
                        row[i] = 'snow_covered_hills'
                    elif item == 'savannah':
                        row[i] = 'snow'
                    elif item == 'shrubby_savannah':
                        row[i] = 'snow'
                    elif item == 'rolling_savannah':
                        row[i] = 'snow'
                    elif item == 'rocky_savannah':
                        row[i] = 'snow_covered_hills'
                    elif item == 'growing_savannah':
                        row[i] = 'snow'
                    elif item == 'lightly_wooded_savannah':
                        row[i] = 'snow_covered_wooded_meadow'
                    elif item == 'lightly_wooded_growing_savannah':
                        row[i] = 'snow_covered_wooded_meadow'
                    elif item == 'rocky_wooded_savannah':
                        row[i] = 'snow_covered_rocky_wooded_hills'
                    elif item == 'wooded_savannah':
                        row[i] = 'snow_covered_forest'
                    elif item == 'wooded_growing_savannah':
                        row[i] = 'snow_covered_forest'
                    elif item == 'overgrown_savannah':
                        row[i] = 'snowy_castle'
                    elif item == 'beach':
                        row[i] = 'snow'
                    elif item == 'desert':
                        row[i] = 'snow'
                    elif item == 'rolling_desert':
                        row[i] = 'snow'
                    elif item == 'rocky_desert':
                        row[i] = 'snow_covered_hills'
                    elif item == 'desert_mountain':
                        row[i] = 'snowy_mountain'
                    elif item == 'desert_plateau':
                        row[i] = 'snowy_mountain'
                    elif item == 'water':
                        row[i] = choice(['cold_water', 'icy_water', 'frozen_water'])
                    elif item == 'deep_water':
                        row[i] = choice(['cold_deep_water', 'icy_deep_water', 'frozen_deep_water', 'glacier'])

                    if overlay is not None:
                        if overlay == 'graveyard':
                            overlay = 'snowy_graveyard'
                        row[i] += '-' + overlay

            self.player_coords = MapCoord(self, 16, 32)

        self.save()

        self.run()

    def save(self):
        f = open(f"data/{self.player.name}/worlds/nixpeculus/worlddata.py", "w")
        f.write(f"player_coords = {self.player_coords.ex()}\n")
        f.write("mapsave = [\n")
        for line in self.map:
            f.write(f"    {line},\n")
        f.write("]\n")
        f.write(f"graveyards = {self.graveyards}")
        f.close()
