player_coords = (16, 32)
mapsave = [
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'water', None, 'rolling_desert', None, 'water', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'beach', None, 'rocky_desert', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None],
    [None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'water', None, 'beach', None, 'rolling_desert', None, 'rolling_desert', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None],
    [None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'beach', None, 'rocky_desert', None, 'rolling_desert', None, 'beach', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None],
    [None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'rolling_desert', None, 'desert', None, 'beach', None, 'beach', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None],
    [None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_plateau', None, 'beach', None, 'rocky_desert', None, 'rocky_desert', None, 'desert', None, 'desert', None, 'rocky_desert', None, 'desert_plateau', None, 'water', None, 'water', None, 'deep_water', None, None, None],
    [None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'rocky_desert', None, 'desert', None, 'savannah', None, 'rolling_desert', None, 'rocky_desert', None, 'beach', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None],
    [None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_mountain', None, 'beach', None, 'rocky_desert', None, 'desert', None, 'desert', None, 'desert', None, 'rolling_desert', None, 'rocky_desert', None, 'beach', None, 'desert_mountain', None, 'water', None, 'water', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'water', None, 'water', None, 'beach', None, 'beach', None, 'rolling_desert', None, 'savannah', None, 'savannah', None, 'savannah', None, 'desert', None, 'rolling_desert', None, 'rolling_desert', None, 'water', None, 'water', None, 'water', None, 'deep_water'],
    [None, 'deep_water', None, 'water', None, 'desert_plateau', None, 'rocky_desert', None, 'rocky_desert', None, 'rocky_desert', None, 'desert', None, 'wooded_growing_savannah', None, 'overgrown_savannah', None, 'savannah', None, 'rolling_desert', None, 'rocky_desert', None, 'rolling_desert', None, 'desert_plateau', None, 'water', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'desert_plateau', None, 'beach', None, 'rolling_desert', None, 'rolling_desert', None, 'desert', None, 'wooded_savannah', None, 'rocky_wooded_savannah', None, 'growing_savannah', None, 'savannah', None, 'beach', None, 'rolling_desert', None, 'beach', None, 'desert_plateau', None, 'water', None, 'deep_water'],
    [None, 'deep_water', None, 'water', None, 'rocky_desert', None, 'desert', None, 'beach', None, 'savannah', None, 'savannah', None, 'wooded_growing_savannah', None, 'rocky_savannah', None, 'rolling_savannah', None, 'savannah', None, 'rocky_desert', None, 'rocky_desert', None, 'rolling_desert', None, 'desert_mountain', None, 'water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'beach', None, 'rolling_desert', None, 'savannah', None, 'rocky_wooded_savannah', None, 'growing_savannah', None, 'savannah', None, 'lightly_wooded_growing_savannah', None, 'wooded_savannah', None, 'desert', None, 'beach', None, 'rocky_desert', None, 'rocky_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_mountain', None, 'beach', None, 'rocky_desert', None, 'desert', None, 'savannah', None, 'wooded_growing_savannah', None, 'swamp', None, 'savannah', None, 'rolling_savannah', None, 'wooded_growing_savannah', None, 'desert', None, 'desert', None, 'beach', None, 'water', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'rocky_desert', None, 'desert', None, 'savannah', None, 'lightly_wooded_growing_savannah', None, 'wooded_savannah', None, 'bog', None, 'rolling_bog', None, 'bog-graveyard', None, 'overgrown_savannah', None, 'overgrown_savannah', None, 'desert', None, 'rolling_desert', None, 'beach', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'water', None, 'beach', None, 'savannah', None, 'savannah', None, 'wooded_growing_savannah', None, 'bog', None, 'jungle_swamp', None, 'jungle_swamp', None, 'savannah', None, 'wooded_growing_savannah', None, 'growing_savannah', None, 'savannah', None, 'rolling_desert', None, 'desert_plateau', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'rolling_desert', None, 'rolling_desert', None, 'rocky_savannah', None, 'savannah', None, 'savannah', None, 'rolling_bog', None, 'rocky_forest', None, 'bog_lake', None, 'savannah', None, 'rocky_wooded_savannah', None, 'rolling_savannah', None, 'rocky_desert', None, 'beach', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_mountain', None, 'beach', None, 'savannah', None, 'wooded_savannah', None, 'rolling_bog', None, 'rolling_bog', None, 'meadow', None, 'hilly_rocky_forest', None, 'rolling_bog', None, 'bog', None, 'savannah', None, 'savannah', None, 'rolling_desert', None, 'desert_mountain', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'beach', None, 'lightly_wooded_growing_savannah', None, 'savannah', None, 'wet_bog', None, 'wetland', None, 'rocky_forest', None, 'wooded_hills', None, 'jungle_swamp', None, 'rolling_bog', None, 'rolling_savannah', None, 'desert', None, 'beach', None, 'water', None, 'deep_water'],
    [None, 'deep_water', None, 'desert_plateau', None, 'beach', None, 'desert', None, 'lightly_wooded_growing_savannah', None, 'bog', None, 'forest', None, 'forest_hills', None, 'jungle', None, 'overgrown_forest', None, 'bog', None, 'rocky_wooded_savannah', None, 'savannah', None, 'rocky_desert', None, 'water', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'rolling_desert', None, 'overgrown_savannah', None, 'swamp', None, 'meadow', None, 'overgrown_forest', None, 'jungle', None, 'wooded_hills', None, 'hilly_rocky_forest', None, 'swamp', None, 'rolling_savannah', None, 'rolling_desert', None, 'rocky_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_plateau', None, 'beach', None, 'savannah', None, 'rocky_wooded_savannah', None, 'wet_bog', None, 'hilly_rocky_forest', None, 'stony_hills', None, 'flooded_plains', None, 'wooded_hills', None, 'wooded_bog', None, 'savannah', None, 'desert', None, 'beach', None, 'desert_plateau', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'rocky_desert', None, 'shrubby_savannah', None, 'bog', None, 'meadow', None, 'wooded_hills', None, 'growing_meadow', None, 'plains', None, 'rolling_bog', None, 'savannah', None, 'lightly_wooded_savannah', None, 'rolling_desert', None, 'beach', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'savannah', None, 'rocky_wooded_savannah', None, 'swamp', None, 'jungle', None, 'growing_meadow', None, 'rolling_meadow', None, 'wetland', None, 'rolling_bog', None, 'rolling_savannah', None, 'desert', None, 'rolling_desert', None, 'desert_plateau', None, 'water', None],
    ['deep_water', None, 'water', None, 'rocky_desert', None, 'desert', None, 'rocky_savannah', None, 'savannah', None, 'rocky_forest', None, 'growing_meadow', None, 'meadow', None, 'stony_hills', None, 'forest_hills', None, 'rolling_bog', None, 'growing_savannah', None, 'desert', None, 'rocky_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'desert', None, 'overgrown_savannah', None, 'overgrown_swamp', None, 'wetland', None, 'meadow', None, 'stony_hills', None, 'forest_hills', None, 'wooded_bog', None, 'rocky_savannah', None, 'desert', None, 'beach', None, 'water', None, 'water', None],
    ['deep_water', None, 'water', None, 'rocky_desert', None, 'beach', None, 'lightly_wooded_savannah', None, 'savannah', None, 'lake', None, 'growing_meadow', None, 'rocky_hills', None, 'overgrown_forest', None, 'rolling_bog', None, 'savannah', None, 'growing_savannah', None, 'rolling_desert', None, 'rolling_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_plateau', None, 'beach', None, 'savannah', None, 'rolling_savannah', None, 'overgrown_bog', None, 'forest_hills', None, 'wooded_hills', None, 'wooded_meadow', None, 'rocky_forest', None, 'wet_bog', None, 'lightly_wooded_growing_savannah', None, 'desert', None, 'beach', None, 'desert_mountain', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'rocky_desert', None, 'beach', None, 'rocky_wooded_savannah', None, 'rolling_bog', None, 'swamp', None, 'lake', None, 'forest', None, 'wooded_meadow', None, 'rolling_bog', None, 'rolling_bog', None, 'shrubby_savannah', None, 'beach', None, 'rolling_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'water', None, 'beach', None, 'desert', None, 'wooded_growing_savannah', None, 'bog', None, 'meadow', None, 'wooded_hills', None, 'wooded_hills', None, 'wooded_meadow', None, 'overgrown_bog', None, 'shrubby_savannah', None, 'desert', None, 'rolling_desert', None, 'desert_plateau', None, 'water', None],
    ['deep_water', None, 'water', None, 'rolling_desert', None, 'beach', None, 'wooded_growing_savannah', None, 'bog', None, 'bog', None, 'wetland', None, 'jungle', None, 'hilly_rocky_forest', None, 'jungle_swamp', None, 'bog', None, 'savannah', None, 'rolling_desert', None, 'rocky_desert', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_mountain', None, 'rocky_desert', None, 'desert', None, 'shrubby_savannah', None, 'savannah', None, 'wet_bog', None, 'lake', None, 'jungle', None, 'overgrown_bog', None, 'savannah', None, 'rocky_wooded_savannah', None, 'savannah', None, 'rocky_desert', None, 'desert_mountain', None, 'water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'desert', None, 'rolling_savannah', None, 'savannah', None, 'bog-graveyard', None, 'overgrown_bog', None, 'meadow', None, 'swamp', None, 'swamp', None, 'rocky_savannah', None, 'wooded_growing_savannah', None, 'rocky_desert', None, 'rolling_desert', None, 'water', None, 'deep_water'],
    [None, 'deep_water', None, 'water', None, 'rocky_desert', None, 'savannah', None, 'rocky_wooded_savannah', None, 'overgrown_savannah', None, 'savannah', None, 'bog', None, 'swamp', None, 'savannah', None, 'wooded_growing_savannah', None, 'growing_savannah', None, 'savannah', None, 'rocky_desert', None, 'desert_plateau', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'beach', None, 'rolling_desert', None, 'desert', None, 'wooded_savannah', None, 'savannah', None, 'savannah', None, 'overgrown_bog', None, 'bog', None, 'overgrown_savannah', None, 'lightly_wooded_savannah', None, 'savannah', None, 'rocky_desert', None, 'beach', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'desert_plateau', None, 'rolling_desert', None, 'rocky_desert', None, 'desert', None, 'overgrown_savannah', None, 'overgrown_savannah', None, 'savannah', None, 'savannah', None, 'overgrown_savannah', None, 'wooded_savannah', None, 'desert', None, 'rolling_desert', None, 'rocky_desert', None, 'desert_mountain', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'rolling_desert', None, 'beach', None, 'desert', None, 'savannah', None, 'growing_savannah', None, 'rocky_wooded_savannah', None, 'savannah', None, 'rolling_savannah', None, 'wooded_growing_savannah', None, 'savannah', None, 'rolling_desert', None, 'rolling_desert', None, 'rocky_desert', None, 'water', None, 'deep_water'],
    [None, 'deep_water', None, 'desert_plateau', None, 'beach', None, 'rolling_desert', None, 'desert', None, 'savannah', None, 'shrubby_savannah', None, 'lightly_wooded_growing_savannah', None, 'rolling_savannah', None, 'lightly_wooded_savannah', None, 'desert', None, 'beach', None, 'desert', None, 'rocky_desert', None, 'desert_plateau', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'water', None, 'rolling_desert', None, 'beach', None, 'desert', None, 'savannah', None, 'rocky_wooded_savannah', None, 'rocky_savannah', None, 'wooded_savannah', None, 'desert', None, 'rocky_desert', None, 'rocky_desert', None, 'beach', None, 'water', None, 'water', None, 'deep_water'],
    [None, 'water', None, 'water', None, 'desert_mountain', None, 'beach', None, 'rocky_desert', None, 'desert', None, 'desert', None, 'lightly_wooded_growing_savannah', None, 'rolling_savannah', None, 'savannah', None, 'desert', None, 'beach', None, 'beach', None, 'desert_mountain', None, 'water', None, 'deep_water', None],
    ['deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'beach', None, 'desert', None, 'desert', None, 'rocky_savannah', None, 'savannah', None, 'desert', None, 'rocky_desert', None, 'rolling_desert', None, 'water', None, 'water', None, 'deep_water', None, 'deep_water'],
    [None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_mountain', None, 'rocky_desert', None, 'beach', None, 'rocky_desert', None, 'savannah', None, 'desert', None, 'desert', None, 'desert', None, 'beach', None, 'water', None, 'water', None, 'deep_water', None, 'deep_water', None],
    [None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'rocky_desert', None, 'beach', None, 'desert', None, 'savannah', None, 'desert', None, 'rolling_desert', None, 'rolling_desert', None, 'desert_mountain', None, 'water', None, 'water', None, 'deep_water', None, None],
    [None, None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_plateau', None, 'rolling_desert', None, 'beach', None, 'desert', None, 'desert', None, 'rocky_desert', None, 'rolling_desert', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None],
    [None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'rocky_desert', None, 'beach', None, 'rocky_desert', None, 'beach', None, 'desert_mountain', None, 'water', None, 'water', None, 'deep_water', None, None, None, None],
    [None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'desert_mountain', None, 'rolling_desert', None, 'rocky_desert', None, 'rocky_desert', None, 'rocky_desert', None, 'desert_mountain', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None],
    [None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'water', None, 'rocky_desert', None, 'beach', None, 'rocky_desert', None, 'desert_plateau', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None],
    [None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_mountain', None, 'beach', None, 'rocky_desert', None, 'desert_mountain', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'rocky_desert', None, 'desert_plateau', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, 'water', None, 'desert_mountain', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'deep_water', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
]
graveyards = [(18, 22), (12, 40)]