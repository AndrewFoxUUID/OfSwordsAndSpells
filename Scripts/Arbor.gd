extends Node2D

const WORLDBASE = [ # 33 * 33
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,3,3,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,1,1,2,2,3,3,4,4,4,3,3,2,2,1,1,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,1,1,2,2,3,3,4,4,5,5,5,4,4,3,3,2,2,1,1,0,0,0,0,0,0,0],
	[0,0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,6,5,5,4,4,3,3,2,2,1,1,0,0,0,0,0],
	[0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0,0],
	[0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0],
	[1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1],
	[1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,10,9,9,8,8,7,7,6,6,5,5,4,4,3,2,1],
	[1,2,3,4,5,6,6,7,7,8,8,9,9,10,10,11,11,11,10,10,9,9,8,8,7,7,6,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,8,9,9,10,10,11,11,12,12,12,11,11,10,10,9,9,8,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,10,11,11,12,12,13,13,13,12,12,11,11,10,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,12,13,13,14,14,14,13,13,12,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,15,15,14,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,16,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,15,14,14,13,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,11,12,12,13,13,14,15,14,13,13,12,12,11,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,9,10,10,11,11,12,12,13,14,13,12,12,11,11,10,10,9,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,7,8,8,9,9,10,10,11,11,12,13,12,11,11,10,10,9,9,8,8,7,6,5,4,3,2,1],
	[1,2,3,4,5,6,6,7,7,8,8,9,9,10,10,11,12,11,10,10,9,9,8,8,7,7,6,6,5,4,3,2,1],
	[1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,11,10,9,9,8,8,7,7,6,6,5,5,4,4,3,2,1],
	[1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,10,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1],
	[1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,8,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1],
	[0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,7,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0],
	[0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,6,6,5,5,4,4,3,3,2,2,1,1,0,0,0,0],
	[0,0,0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,5,5,4,4,3,3,2,2,1,1,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,1,1,2,2,3,3,4,4,5,4,4,3,3,2,2,1,1,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,3,4,3,3,2,2,1,1,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,3,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
]

const MEADOW_BASE = [45]
const MEADOWS = [62, 26, 28, 57, 85]
const WET_MEADOWS = [44, 90, 34]
const FORESTS = [95, 94, 56, 29, 21, 22, 49, 32]
const PLAINS_STRUCTURES = [46, 88, 87, 5]
const MOUNTAINS = [76, 47, 4, 8, 37, 36, 38, 65, 64, 66, 18, 17, 19]
const LAVA = [35, 43]
const PLAINS = [52, 20]
const SNOWY_BASE = [74, 69]
const SNOWY = [77, 80, 73, 72, 82, 84, 83, 81]
const SNOW_STRUCTURES = [75, 79, 78, 71, 70]
const SWAMP_BASE = [2]
const TRANSITION_SWAMP = [60, 86]
const SWAMP = [91, 3, 92, 33, 48, 51]
const SAVANNAH_BASE = [67]
const SAVANNAH = [68, 63, 58, 27, 42, 41, 59, 0, 93, 50]
const DESERT_BASE = [11]
const DESERT = [1, 61, 55]
const DESERT_MOUNTAINS = [13, 14]
const DESERT_STRUCTURES = [16, 15, 12]
const DEADLANDS = [9]
const WATER_BASE = [89]
const WATERS = [7, 31, 24]
const WATER_STRUCTURES = [40, 54, 39, 53]
const DEEP_WATER_BASE = [10]
const DEEP_WATER = [6, 30, 23, 25]
const VILLAGE = [88]

const LEAFY_CAVE_ACCEPTORS = SAVANNAH_BASE
const SNOWY_CAVE_ACCEPTORS = SNOWY_BASE
const DESERT_CAVE_ACCEPTORS = DESERT_BASE
const GRAVEYARD_ACCEPTORS = SWAMP_BASE
const SNOWY_GRAVEYARD_ACCEPTORS = SNOWY_BASE
const OASIS_ACCEPTORS = DESERT_BASE
const CALDERA_ACCEPTORS = SNOWY_BASE + SWAMP_BASE + SAVANNAH_BASE + DESERT_BASE + WATER_BASE
const LAVA_POOL_ACCEPTORS = SNOWY_BASE + SWAMP_BASE + SAVANNAH_BASE + DESERT_BASE + DEEP_WATER_BASE

const WORLD_COMPOSITION_MAP = [
	[null],
	DEEP_WATER_BASE,
	DEEP_WATER_BASE + WATER_BASE,
	WATER_BASE,
	WATER_BASE + DESERT_MOUNTAINS,
	DESERT,
	DESERT_BASE + DESERT,
	DESERT_BASE + DESERT_BASE + DESERT,
	DESERT_BASE + SAVANNAH_BASE,
	SAVANNAH_BASE + SAVANNAH_BASE + SAVANNAH,
	SAVANNAH_BASE + SAVANNAH_BASE + SAVANNAH,
	SWAMP_BASE + SWAMP_BASE + TRANSITION_SWAMP + SAVANNAH_BASE + SAVANNAH_BASE + SAVANNAH_BASE + SAVANNAH_BASE,
	SWAMP_BASE + SWAMP_BASE + TRANSITION_SWAMP + SWAMP,
	MEADOW_BASE + MEADOW_BASE + FORESTS + WET_MEADOWS + TRANSITION_SWAMP,
	FORESTS + WET_MEADOWS,
	FORESTS + MEADOWS + PLAINS,
	MEADOW_BASE + MEADOW_BASE + MEADOWS,
	VILLAGE
]

var visible_tiles = []

var left_pressed = false
var right_pressed = false
var up_pressed = false
var down_pressed = false

func _ready():
	Base.world = self
	if Base.player.get_level() < 1:
		Base.tile_index = 544
		Base.change_scene("res://Scenes/Tile.tscn")
		
	if len(visible_tiles) == 1:
		visible_tiles += getSurroundingTiles(visible_tiles[0])
		
	var file = File.new()
	if file.file_exists("user://Players/" + Base.player.savename + "/Sguila/worlddata.json"):
		file.open("user://Players/" + Base.player.savename + "/Sguila/worlddata.json", File.READ)
		
		var save = parse_json(file.get_line())
		for cell in save["Tiles"]:
			$TileMap/Tiles.set_cellv(Vector2(str2var(cell)), save["Tiles"][cell])
		for cell in save["Overlays"]:
			$TileMap/Overlays.set_cellv(Vector2(str2var(cell)), save["Overlays"][cell])
			
		for tile in save["VisibleTiles"]:
			visible_tiles.append(Vector2(str2var(tile)))
			
		file.close()
	else:
		generate()
		visible_tiles = [Vector2(16, 16)]


func getSurroundingTiles(coords):
	return [
		Vector2(coords.x, coords.y-1),
		Vector2(coords.x-1, coords.y-1 + int(coords.x)%2),
		Vector2(coords.x+1, coords.y-1 + int(coords.x)%2),
		Vector2(coords.x-1, coords.y + int(coords.x)%2),
		Vector2(coords.x+1, coords.y + int(coords.x)%2),
		Vector2(coords.x, coords.y+1)
	]


func generate():
	var graveyard_acceptors = []
	for r in len(WORLDBASE):
		for c in len(WORLDBASE[r]):
			var choices = WORLD_COMPOSITION_MAP[WORLDBASE[r][c]]
			var tile = choices[randi() % len(choices)]
			if tile != null:
				$TileMap/Tiles.set_cell(c, r, tile)
				if tile in GRAVEYARD_ACCEPTORS:
					graveyard_acceptors.append(Vector2(c, r))
	
	if len(graveyard_acceptors) == 0:
		for r in len(WORLDBASE):
			for c in len(WORLDBASE[r]):
				if WORLDBASE[r][c] in TRANSITION_SWAMP + SWAMP:
					$TileMap/Tiles.set_cellv(Vector2(c, r), 1)
					graveyard_acceptors.append(Vector2(c, r))
	
	var acceptors_passed = 0
	for acceptor in graveyard_acceptors:
		if randi() % (len(graveyard_acceptors)-acceptors_passed) == 0:
			$TileMap/Overlays.set_cellv(acceptor, 5)
			acceptors_passed = 0
		else:
			acceptors_passed += 1


func _process(_delta):
	if Base.player.get_level() == 1:
		$VisibleTiles.visible = true
		for tile in visible_tiles:
			$VisibleTiles/Tiles.set_cellv(tile, $TileMap/Tiles.get_cellv(tile))
			$VisibleTiles/Overlays.set_cellv(tile, $TileMap/Overlays.get_cellv(tile))
		$TileMap.greyscale = true
		$VisibleTiles.greyscale = false
	else:
		$VisibleTiles.visible = false
		$TileMap.greyscale = false
	
	if left_pressed:
		$TileMap.position.x += 10
	if right_pressed:
		$TileMap.position.x -= 10
	if up_pressed:
		$TileMap.position.y += 10
	if down_pressed:
		$TileMap.position.y -= 10
	$VisibleTiles.position = $TileMap.position
		
	if $VisibleTiles.visible:
		$TileMap.selected = $VisibleTiles.selected
	if $TileMap.selected != null:
		$SelectedTileInfo.visible = true
		var name = $TileMap/Tiles.tile_set.tile_get_name($TileMap/Tiles.get_cellv($TileMap.selected))
		var formattedname = ""
		for word in name.split('_'):
			formattedname += word.capitalize() + " "
		name = "" if $TileMap/Overlays.get_cellv($TileMap.selected) == -1 else $TileMap/Overlays.tile_set.tile_get_name($TileMap/Overlays.get_cellv($TileMap.selected))
		for word in name.split('_'):
			formattedname += word.capitalize() + " "
		$SelectedTileInfo/PanelContainer/Panel/TileName.text = formattedname
	else:
		$SelectedTileInfo.visible = false


func get_tile(index):
	return $TileMap/Tiles.get_cell(index%33, index/33)


func get_overlay(index):
	return $TileMap/Overlays.get_cell(index%33, index/33)


func _unhandled_input(event):
	if event.is_action_pressed("ui_left"):
		left_pressed = true
	elif event.is_action_released("ui_left"):
		left_pressed = false
	elif event.is_action_pressed("ui_right"):
		right_pressed = true
	elif event.is_action_released("ui_right"):
		right_pressed = false
	elif event.is_action_pressed("ui_up"):
		up_pressed = true
	elif event.is_action_released("ui_up"):
		up_pressed = false
	elif event.is_action_pressed("ui_down"):
		down_pressed = true
	elif event.is_action_released("ui_down"):
		down_pressed = false
	elif event.is_action_pressed("ui_zoom_in"):
		$TileMap.scale.x += 1
		$TileMap.scale.y += 1
	elif event.is_action_pressed("ui_zoom_out"):
		$TileMap.scale.x = max($TileMap.scale.x - 1, 1)
		$TileMap.scale.y = max($TileMap.scale.y - 1, 1)
	elif event.is_action_pressed("ui_accept") and $TileMap.selected != null and (Base.player.get_level() > 1 or $TileMap.selected in visible_tiles):
		for tile in getSurroundingTiles($TileMap.selected):
			if not (tile in visible_tiles):
				visible_tiles.append(tile)
		save()
		Base.tile_index = int($TileMap.selected.x + 33*$TileMap.selected.y)
		Base.change_scene("res://Scenes/Tile.tscn")


func save():
	var savedata = {
		"Tiles": {},
		"Overlays": {},
		"VisibleTiles": []
	}
	for cell in $TileMap/Tiles.get_used_cells():
		savedata["Tiles"][var2str(cell)] = $TileMap/Tiles.get_cellv(cell)
	for cell in $TileMap/Overlays.get_used_cells():
		savedata["Overlays"][var2str(cell)] = $TileMap/Overlays.get_cellv(cell)
	for tile in visible_tiles:
		savedata["VisibleTiles"].append(var2str(tile))
		
	savedata = to_json(savedata)
		
	var file = File.new()
	file.open("user://Players/" + Base.player.savename + "/Sguila/worlddata.json", File.WRITE)
	file.store_line(savedata)
	file.close()
