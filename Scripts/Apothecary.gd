extends Node2D

const SW = 800
const SH = 800
const WW = 668
const WH = 480
var old_position


func _ready():
	generate()
	old_position = Base.player.position
	$TileMap.add_child(Base.player)
	Base.player.visible = true
	Base.player.position = Vector2(30, 0)
	Base.player.active = true
	Base.player.get_node("Camera2D").current = true
	
	
func generate():
	var groundShape = $ParallaxBackground/TileMap/StaticBody2D/CollisionPolygon2D.polygon
	
	var floormap = []
	var pos = 0
	var height = 0
	var stretch = 2 + randi()%5
	while pos < SW/4:
		for i in 5 + randi()%5:
			floormap.append([42, height])
			pos += 1
		floormap.append([43, height])
		pos += 1
		
		stretch -= 1
		if stretch <= 0:
			stretch = 2 + randi()%5
			height = 0 if height == 1 else 1
	
	var y = SH/4 - 1
	for i in 6:
		for x in SW/4:
			$TileMap/Foreground/TileMap.set_cellv(Vector2(x, y), 9)
		y -= 1
	for x in SW/4:
		$TileMap/Foreground/TileMap.set_cellv(Vector2(x, y), 9 if floormap[x][1] == 0 else floormap[x][0])
	y -= 1
	for i in 2:
		for x in SW/4:
			$TileMap/Foreground/TileMap.set_cellv(Vector2(x, y), floormap[x][0])
		y -= 1
	for x in SW/4:
		$TileMap/Foreground/TileMap.set_cellv(Vector2(x, y), 40 if floormap[x][1] == 1 else floormap[x][0])
	groundShape = Geometry.merge_polygons_2d(groundShape, PoolVector2Array([Vector2(0, SH), Vector2(SW, SH), Vector2(SW, y*4), Vector2(0, y*4)]))
	
	$TileMap/Foreground/StaticBody2D/CollisionPolygon2D.polygon = groundShape
	$TileMap/Foreground/StaticBody2D/GroundMask.polygon = groundShape


func save():
	var savedata = {
		"Foreground": {},
		"Solid Shape": var2str($TileMap/Foreground/StaticBody2D/CollisionPolygon2D.polygon),
		"Entities": []
	}

	for cell in $TileMap/Foreground/TileMap.get_used_cells():
		savedata["Foreground"][var2str(cell)] = $TileMap/Foreground/TileMap.get_cellv(cell)
	for entity in $TileMap/Entities.get_children():
		savedata["Entities"].append(entity.save())
		
	savedata = to_json(savedata)
	
	var file = File.new()
	# TODO filename, current solution would create a new apothecary each time the player enters from a different pixel
	file.open("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "-apothecary-" + str(old_position.x) + "-data.json", File.WRITE)
	file.store_line(savedata)
	file.close()
