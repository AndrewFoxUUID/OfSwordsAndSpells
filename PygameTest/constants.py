# -- CONSTANT COLORS --
CLEAR = (0, 0, 0, 0)
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
BLUE = (0, 0, 255, 255)
YELLOW = (255, 255, 0, 255)
TEAL = (0, 255, 255, 255)
PURPLE = (255, 0, 255, 255)
GREY = (127, 127, 127, 255)
LIFE = (0, 102, 51, 255)
WATER = (38, 68, 144, 255)
FIRE = (126, 2, 31, 255)
DEATH = (66, 3, 97, 255)

# -- NUMERICAL CONSTANTS --
# tile width
TW = 8640
# tile height
TH = 1920
# window width
WW = 1000
# window height
WH = 500
# tick limit
TICKLIM = 1000000

# -- WORLD MAP CONSTANTS --
a, b, c, d, e, f, g, h = 10, 11, 12, 13, 14, 15, 16, 17
world_base = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0],
    [0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0],
    [0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0],
    [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0],
    [0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0],
    [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1],
    [0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0],
    [1,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,a,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,1],
    [0,2,0,4,0,5,0,6,0,7,0,8,0,9,0,a,0,a,0,9,0,8,0,7,0,6,0,5,0,4,0,2,0],
    [1,0,3,0,5,0,6,0,7,0,8,0,9,0,a,0,b,0,a,0,9,0,8,0,7,0,6,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,7,0,8,0,9,0,a,0,b,0,b,0,a,0,9,0,8,0,7,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,8,0,9,0,a,0,b,0,c,0,b,0,a,0,9,0,8,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,9,0,a,0,b,0,c,0,c,0,b,0,a,0,9,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,a,0,b,0,c,0,d,0,c,0,b,0,a,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,b,0,c,0,d,0,d,0,c,0,b,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,c,0,d,0,e,0,d,0,c,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,d,0,e,0,e,0,d,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,d,0,e,0,f,0,e,0,d,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,e,0,f,0,f,0,e,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,d,0,f,0,g,0,f,0,d,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,e,0,g,0,g,0,e,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,d,0,f,0,h,0,f,0,d,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,e,0,g,0,g,0,e,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,d,0,f,0,g,0,f,0,d,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,e,0,f,0,f,0,e,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,d,0,e,0,f,0,e,0,d,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,c,0,d,0,e,0,e,0,d,0,c,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,b,0,c,0,d,0,e,0,d,0,c,0,b,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,a,0,b,0,c,0,d,0,d,0,c,0,b,0,a,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,9,0,a,0,b,0,c,0,d,0,c,0,b,0,a,0,9,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,8,0,9,0,a,0,b,0,c,0,c,0,b,0,a,0,9,0,8,0,6,0,4,0,2,0],
    [1,0,3,0,5,0,7,0,8,0,9,0,a,0,b,0,c,0,b,0,a,0,9,0,8,0,7,0,5,0,3,0,1],
    [0,2,0,4,0,6,0,7,0,8,0,9,0,a,0,b,0,b,0,a,0,9,0,8,0,6,0,5,0,4,0,2,0],
    [1,0,3,0,5,0,6,0,7,0,8,0,9,0,a,0,b,0,a,0,9,0,8,0,7,0,5,0,5,0,3,0,1],
    [0,2,0,4,0,5,0,6,0,7,0,8,0,9,0,a,0,a,0,9,0,8,0,7,0,6,0,5,0,4,0,2,0],
    [1,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,a,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,1],
    [0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0],
    [1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,9,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1],
    [0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0],
    [0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,8,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0],
    [0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0],
    [0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,7,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0],
    [0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,6,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,5,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,4,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,3,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

# -- WORLD COMPOSITION CONSTANTS --
MEADOW_BASE = ['meadow']
MEADOWS = ['rolling_meadow', 'growing_meadow', 'hills', 'rocky_hills', 'stony_hills']
WET_MEADOWS = ['marsh', 'wetland', 'lake']
FORESTS = ['wooded_meadow', 'wooded_hills', 'rocky_forest', 'hilly_rocky_forest', 'forest', 'forest_hills', 'overgrown_forest', 'jungle']
PLAINS_STRUCTURES = ['monument', 'village', 'town', 'city']
MOUNTAINS = ['snowy_mountain', 'mountain', 'caldera', 'crater', 'lava_mountain', 'lava_caldera', 'lava_crater', 'running_mountain', 'running_caldera', 'running_crater', 'erupting_mountain', 'erupting_caldera', 'erupting_crater']
LAVA = ['lava', 'magma']
PLAINS = ['plains', 'flooded_plains']
SNOWY_BASE = ['snowy_meadow', 'snow']
SNOWY = ['snowy_rocky_hills', 'snowy_wooded_meadow', 'snowy_hilly_rocky_forest', 'snowy_forest', 'snow_covered_hills', 'snow_covered_wooded_meadow', 'snow_covered_rocky_wooded_hills', 'snow_covered_forest']
SNOW_STRUCTURES = ['snowy_monument', 'snowy_village', 'snowy_town', 'snowy_city', 'snowy_castle']
SWAMP_BASE = ['bog']
TRANSITION_SWAMP = ['rolling_bog', 'swamp']
SWAMP = ['wet_bog', 'bog_lake', 'wooded_bog', 'jungle_swamp', 'overgrown_bog', 'overgrown_swamp']
SAVANNAH_BASE = ['savannah']
SAVANNAH = ['shrubby_savannah', 'rolling_savannah', 'rocky_savannah', 'growing_savannah', 'lightly_wooded_savannah', 'lightly_wooded_growing_savannah', 'rocky_wooded_savannah', 'wooded_savannah', 'wooded_growing_savannah', 'overgrown_savannah']
DESERT_BASE = ['desert']
DESERT = ['beach', 'rolling_desert', 'rocky_desert']
DESERT_MOUNTAINS = ['desert_mountain', 'desert_plateau']
DESERT_STRUCTURES = ['desert_village', 'desert_town', 'desert_city']
DEADLANDS = ['dead_desert']
WATER_BASE = ['water']
WATERS = ['cold_water', 'icy_water', 'frozen_water']
WATER_STRUCTURES = ['left_water_village', 'right_water_village', 'left_cold_water_village', 'right_cold_water_village']
DEEP_WATER_BASE = ['deep_water']
DEEP_WATER = ['cold_deep_water', 'icy_deep_water', 'frozen_deep_water', 'glacier']

LEAFY_CAVE_ACCEPTORS = SAVANNAH_BASE
SNOWY_CAVE_ACCEPTORS = SNOWY_BASE
DESERT_CAVE_ACCEPTORS = DESERT_BASE
GRAVEYARD_ACCEPTORS = SWAMP_BASE
SNOWY_GRAVEYARD_ACCEPTORS = SNOWY_BASE
OASIS_ACCEPTORS = DESERT_BASE
CALDERA_ACCEPTORS = SNOWY_BASE + SWAMP_BASE + SAVANNAH_BASE + DESERT_BASE + WATER_BASE
LAVA_POOL_ACCEPTORS = SNOWY_BASE + SWAMP_BASE + SAVANNAH_BASE + DESERT_BASE + DEEP_WATER_BASE

WORLD_COMPOSITION_MAP = {
    'arbor': [
        [None],
        DEEP_WATER_BASE,
        DEEP_WATER_BASE + WATER_BASE,
        WATER_BASE,
        WATER_BASE + DESERT_MOUNTAINS,
        DESERT,
        DESERT_BASE + DESERT,
        DESERT_BASE*2 + DESERT,
        DESERT_BASE + SAVANNAH_BASE,
        SAVANNAH_BASE*2 + SAVANNAH,
        SAVANNAH_BASE*2 + SAVANNAH,
        SWAMP_BASE*2 + TRANSITION_SWAMP + SAVANNAH_BASE*4,
        SWAMP_BASE*2 + TRANSITION_SWAMP + SWAMP,
        MEADOW_BASE*2 + FORESTS + WET_MEADOWS + TRANSITION_SWAMP,
        FORESTS + WET_MEADOWS,
        FORESTS + MEADOWS + PLAINS,
        MEADOW_BASE*2 + MEADOWS,
        MEADOW_BASE
    ],
    'malleandor': [
        [None],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        'forge'
    ]
}

# -- TILE COMPOSITION CONSTANTS --

# name: [colorkey, {terrain_piece_type: frequency}, [objects], [enemies], manatypes]
# terrain_piece_types: grass, plant, water, rock-formation, tree, large-tree
# objects: chest-closed, axe, fence, wood, cage, boxes, barrel
# stretch len variation, height dif variation, intensity frequency
TILE_COMPOSITION_MAP = {
    'meadow': ['meadow', {'grass': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, [], ['Armadillo'], 'l'],
    'rolling_meadow': ['meadow', {'grass': 6, 'intensity': 15, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['chest-closed', 'boxes', 'barrel'], [], 'l'],
    'growing_meadow': ['meadow', {'grass': 8, 'plant': 6, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['chest-closed', 'boxes', 'barrel'], [], 'll'],
    'hills': ['meadow', {'grass': 6, 'rock-formation': 2, 'intensity': 25, 'stretch-len': (5,10), 'height-dif': (2,6)}, ['chest-closed', 'boxes', 'barrel'], [], 'lb'],
    'rocky_hills': ['meadow', {'grass': 4, 'rock-formation': 4, 'intensity': 30, 'stretch-len': (6,10), 'height-dif': (3,5)}, ['chest-closed', 'boxes', 'barrel'], [], 'lbb'],
    'stony_hills': ['meadow', {'grass': 4, 'rock-formation': 5, 'intensity': 35, 'stretch-len': (6,10), 'height-dif': (3,5)}, ['chest-closed', 'boxes', 'barrel'], [], 'lbb'],
    'wooded_meadow': ['meadow', {'grass': 4, 'tree': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'lll'],
    'wooded_hills': ['meadow', {'grass': 4, 'rock-formation': 2, 'tree': 2, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (3,5)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'lllb'],
    'marsh': ['meadow', {'grass': 8, 'water': 2, 'intensity': 10, 'stretch-len': (12,16), 'height-dif': (1,1)}, ['chest-closed', 'boxes', 'barrel'], [], 'llw'],
    'wetland': ['meadow', {'grass': 8, 'water': 4, 'intensity': 10, 'stretch-len': (12,16), 'height-dif': (1,1)}, ['chest-closed', 'boxes', 'barrel'], [], 'llww'],
    'lake': ['meadow', {'grass': 8, 'water': 6, 'intensity': 10, 'stretch-len': (12,16), 'height-dif': (1,1)}, ['chest-closed', 'boxes', 'barrel'], [], 'lwww'],
    'rocky_forest': ['meadow', {'grass': 4, 'rock-formation': 4, 'tree': 4, 'intensity': 15, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], ['Hedgehog', 'TwigBlight'], 'lllb'],
    'hilly_rocky_forest': ['meadow', {'grass': 4, 'rock-formation': 6, 'tree': 4, 'intensity': 35, 'stretch-len': (6,10), 'height-dif': (3,7)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], ['Hedgehog', 'TwigBlight'], 'lllbb'],
    'forest': ['meadow', {'grass': 4, 'tree': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], ['Hedgehog', 'TwigBlight'], 'llll'],
    'forest_hills': ['meadow', {'grass': 4, 'rock-formation': 2, 'tree': 4, 'intensity': 25, 'stretch-len': (5,10), 'height-dif': (2,6)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], ['Hedgehog', 'TwigBlight'], 'llllb'],
    'overgrown_forest': ['meadow', {'grass': 6, 'tree': 10, 'large-tree': 2, 'intensity': 15, 'stretch-len': (12,16), 'height-dif': (1,2)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], ['Hedgehog', 'TwigBlight'], 'llllll'],
    'jungle': ['meadow', {'grass': 6, 'tree': 10, 'intensity': 15, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'lllll'],
    'plains': ['plains', {'grass': 10, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['fence', 'chest-closed', 'boxes', 'barrel'], [], 'll'],
    'flooded_plains': ['plains', {'grass': 8, 'water': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['fence', 'chest-closed', 'boxes', 'barrel'], [], 'llw'],
    'bog': ['swamp', {'grass': 4, 'water': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['cage'], ['Bat', 'Slime'], 'ld'],
    'wet_bog': ['swamp', {'grass': 6, 'water': 6, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['cage'], ['Bat', 'Slime'], 'lwd'],
    'bog_lake': ['swamp', {'grass': 6, 'water': 8, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['cage'], ['Bat', 'Slime'], 'lwwd'],
    'rolling_bog': ['swamp', {'grass': 6, 'water': 2, 'intensity': 15, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['cage'], ['Bat', 'Slime'], 'ld'],
    'wooded_bog': ['swamp', {'grass': 4, 'water': 2, 'tree': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood', 'cage'], ['Bat', 'Slime'], 'lld'],
    'jungle_swamp': ['swamp', {'grass': 6, 'water': 2, 'tree': 6, 'intensity': 15, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood', 'cage'], ['Bat', 'Slime'], 'lllld'],
    'overgrown_bog': ['swamp', {'grass': 6, 'water': 2, 'tree': 8, 'large-tree': 2, 'intensity': 15, 'stretch-len': (12,16), 'height-dif': (1,2)}, ['axe', 'wood', 'cage'], ['Bat', 'Slime'], 'llllld'],
    'swamp': ['swamp', {'grass': 8, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['cage'], ['Bat', 'Slime'], 'llld'],
    'overgrown_swamp': ['swamp', {'grass': 10, 'tree': 8, 'large-tree': 2, 'intensity': 15, 'stretch-len': (12,16), 'height-dif': (1,2)}, ['axe', 'wood', 'cage'], ['Bat', 'Slime'], 'lllllld'],
    'savannah': ['savannah', {'grass': 4, 'rock-formation': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['chest-closed', 'boxes', 'barrel'], [], 'lb'],
    'shrubby_savannah': ['savannah', {'grass': 6, 'rock-formation': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['chest-closed', 'boxes', 'barrel'], [], 'llb'],
    'rolling_savannah': ['savannah', {'grass': 6, 'rock-formation': 2, 'intensity': 15, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['chest-closed', 'boxes', 'barrel'], [], 'lb'],
    'rocky_savannah': ['savannah', {'grass': 4, 'rock-formation': 6, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['chest-closed', 'boxes', 'barrel'], [], 'lbb'],
    'growing_savannah': ['savannah', {'grass': 6, 'rock-formation': 2, 'plant': 6, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['chest-closed', 'boxes', 'barrel'], [], 'llb'],
    'lightly_wooded_savannah': ['savannah', {'grass': 4, 'rock-formation': 2, 'tree': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'lllb'],
    'lightly_wooded_growing_savannah': ['savannah', {'grass': 6, 'rock-formation': 2, 'tree': 2, 'plant': 5, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'llllb'],
    'rocky_wooded_savannah': ['savannah', {'grass': 4, 'rock-formation': 6, 'tree': 4, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (1,3)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'llllbb'],
    'wooded_savannah': ['savannah', {'grass': 4, 'rock-formation': 2, 'tree': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'llllb'],
    'wooded_growing_savannah': ['savannah', {'grass': 6, 'rock-formation': 2, 'tree': 4, 'plant': 6, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'lllllb'],
    'overgrown_savannah': ['savannah', {'grass': 8, 'rock-formation': 2, 'tree': 6, 'intensity': 15, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood', 'chest-closed', 'boxes', 'barrel'], [], 'llllllb'],
    'beach': ['desert', {'tree': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, ['axe', 'wood'], [], 'lb'],
    'desert': ['desert', {'rock-formation': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, [], ['Ghoul'], 'f'],
    'rolling_desert': ['desert', {'grass': 4, 'rock-formation': 2, 'intensity': 15, 'stretch-len': (6,10), 'height-dif': (1,3)}, [], ['Ghoul'], 'f'],
    'rocky_desert': ['desert', {'rock-formation': 6, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (1,3)}, [], ['Ghoul'], 'bb'],
    'desert_mountain': ['desert', {'rock-formation': 8, 'intensity': 60, 'stretch-len': (2,6), 'height-dif': (6,10)}, [], ['Ghoul'], 'bbb'],
    'desert_plateau': ['desert', {'rock-formation': 10, 'intensity': 50, 'stretch-len': (4,8), 'height-dif': (4,8)}, [], ['Ghoul'], 'bbbb'],
    'water': ['water', {'water': 10, 'rock-formation': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'w'],
    'cold_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'ww'],
    'icy_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'www'],
    'frozen_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'wwww'],
    'deep_water': ['deep_water', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'ww'],
    'cold_deep_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'www'],
    'icy_deep_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'wwww'],
    'frozen_deep_water': ['snow', {'water': 10, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'wwwww'],
    'glacier': ['snow', {'water': 10, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (1,4)}, [], [], 'wwwwww'],
    'snow': ['snow', {'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, [], [], 'lww'],
    'snowy_meadow': ['snow', {'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,2)}, [], [], 'llww'],
    'snowy_rocky_hills': ['snow', {'rock-formation': 4, 'intensity': 25, 'stretch-len': (6,10), 'height-dif': (3,5)}, [], [], 'lbww'],
    'snow_covered_hills': ['snow', {'rock-formation': 5, 'intensity': 20, 'stretch-len': (6,10), 'height-dif': (3,5)}, [], [], 'lbww'],
    'snow_covered_wooded_meadow': ['snow', {'tree': 2, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, [], [], 'lllww'],
    'snowy_wooded_meadow': ['snow', {'rock-formation': 2, 'tree': 2, 'intensity': 10, 'stretch-len': (6,10), 'height-dif': (3,5)}, [], [], 'lllww'],
    'snow_covered_rocky_wooded_hills': ['snow', {'rock-formation': 6, 'tree': 4, 'intensity': 30, 'stretch-len': (6,10), 'height-dif': (3,7)}, [], [], 'lllbww'],
    'snowy_hilly_rocky_forest': ['snow', {'rock-formation': 4, 'intensity': 35, 'stretch-len': (6,10), 'height-dif': (3,5)}, [], [], 'lllbww'],
    'snow_covered_forest': ['snow', {'tree': 4, 'intensity': 10, 'stretch-len': (8,12), 'height-dif': (1,1)}, [], [], 'llllww'],
    'snowy_forest': ['snow', {'rock-formation': 2, 'tree': 4, 'intensity': 10, 'stretch-len': (5,10), 'height-dif': (2,6)}, [], [], 'llllww'],
    'snowy_castle': ['snow', {}, [], [], 'ww'],
    'snowy_monument': ['snow', {}, [], [], 'lww'],
    'snowy_village': ['snow', {}, [], [], 'ww'],
    'snowy_town': ['snow', {}, [], [], 'ww'],
    'snowy_city': ['snow', {}, [], [], 'ww'],
    'snowy_mountain': ['snow', {}, [], [], 'bbww'],
    # Overlays
    'graveyard': [{'grass': -3, 'water': -2}, ['barrel'], ['Lich'], 'ddddd'],
    'snowy_graveyard': [{}, [], [], 'dddddwwwww'],
}

# -- COLOR CONSTANTS --

COLORKEYS = {
    'meadow': {
        'light_grass': (193, 198, 88),
        'dark_grass': (105, 124, 62),
        'dirt': (28, 14, 27),
        'dirt_accent': (58, 35, 54),
        'light_dirt_accent': (85, 69, 97),
        'lighter_dirt_accent': (140, 142, 171),
        'lightest_dirt_accent': (244, 238, 192),
        'water': (111, 222, 244, 150),
        'water_surface': (37, 184, 207, 150),
        'light_leaf': (193, 198, 88),
        'medium_leaf': (149, 161, 75),
        'dark_leaf': (105, 124, 62),
        'darker_leaf': (78, 94, 46),
        'darkest_leaf': (29, 38, 31),
        'darkest_wood': (28, 14, 27),
        'darker_wood': (109, 72, 52),
        'dark_wood': (146, 101, 77),
        'medium_wood': (180, 129, 102),
        'light_wood': (206, 157, 130),
        'background_top': (74, 132, 154),
        'background_bottom': (63, 124, 62)
    }
}

COLORKEYS['plains'] = COLORKEYS['meadow'].copy()
COLORKEYS['plains']['light_grass'] = (231, 203, 61)
COLORKEYS['plains']['dark_grass'] = (171, 151, 49)
COLORKEYS['plains']['background_bottom'] = (202, 204, 62)

COLORKEYS['swamp'] = COLORKEYS['meadow'].copy()
COLORKEYS['swamp']['light_grass'] = (165, 176, 102)
COLORKEYS['swamp']['dark_grass'] = (77, 88, 52)
COLORKEYS['swamp']['water'] = (111, 244, 162, 150)
COLORKEYS['swamp']['water_surface'] = (37, 207, 139, 150)
COLORKEYS['swamp']['background_top'] = (104, 89, 184)
COLORKEYS['swamp']['background_bottom'] = (165, 176, 102)

COLORKEYS['savannah'] = COLORKEYS['meadow'].copy()
COLORKEYS['savannah']['light_grass'] = (176, 182, 60)
COLORKEYS['savannah']['dark_grass'] = (133, 139, 49)
COLORKEYS['savannah']['dirt'] = (130, 47, 19)
COLORKEYS['savannah']['dirt_accent'] = (150, 64, 21)
COLORKEYS['savannah']['light_dirt_accent'] = (176, 105, 76)
COLORKEYS['savannah']['lighter_dirt_accent'] = (67, 30, 7)
COLORKEYS['savannah']['lightest_dirt_accent'] = (211, 148, 105)
COLORKEYS['savannah']['background_bottom'] = (130, 45, 44)

COLORKEYS['desert'] = COLORKEYS['meadow'].copy()
COLORKEYS['desert']['light_grass'] = (214, 149, 88)
COLORKEYS['desert']['dark_grass'] = (167, 87, 52)
COLORKEYS['desert']['dirt'] = (208, 194, 145)
COLORKEYS['desert']['dirt_accent'] = (221, 215, 171)
COLORKEYS['desert']['light_dirt_accent'] = (157, 141, 90)
COLORKEYS['desert']['lighter_dirt_accent'] = (124, 114, 83)
COLORKEYS['desert']['lightest_dirt_accent'] = (225, 222, 180)
COLORKEYS['desert']['background_bottom'] = (201, 169, 93)

COLORKEYS['water'] = COLORKEYS['desert'].copy()
COLORKEYS['water']['background_bottom'] = (64, 194, 231)

COLORKEYS['deep_water'] = COLORKEYS['desert'].copy()
COLORKEYS['deep_water']['water'] = (111, 156, 244, 150)
COLORKEYS['deep_water']['water_surface'] = (37, 125, 207, 150)
COLORKEYS['deep_water']['background_bottom'] = (91, 147, 221)

COLORKEYS['snow'] = COLORKEYS['meadow'].copy()
COLORKEYS['snow']['light_grass'] = (235, 249, 242)
COLORKEYS['snow']['dark_grass'] = (213, 235, 246)
COLORKEYS['snow']['background_bottom'] = (215, 216, 227)

MANA_COLORS = {
    "l": LIFE,
    "w": WATER,
    "f": FIRE,
    "d": DEATH
}

ALIGNMENT_COLORS = [
    (WHITE, (0, 200, 0)),
    (GREY, BLACK),
    (BLACK, RED)
]
