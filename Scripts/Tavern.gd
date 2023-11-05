extends Node2D

onready var pixelmap = preload("res://Scenes/UIElements/PixelMap.tscn")
onready var barkeep = preload("res://Scenes/Entities/Barkeep.tscn")
onready var table = preload("res://Scenes/Entities/Table.tscn")
onready var coins = preload("res://Scenes/Entities/Coins.tscn")
onready var drink = preload("res://Scenes/Entities/Drink.tscn")
onready var door = preload("res://Scenes/Entities/Door.tscn")

const SW = 800
const SH = 800
const WW = 668
const WH = 480
var old_position

var layers = [null, []]

var mutex
var thread
var file
var save

func _ready():
	Base.building = self
	
	mutex = Mutex.new()
	thread = Thread.new()
	file = File.new()
	
	old_position = Base.player.position
	
	if file.file_exists("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "-tavern-" + str(Base.building_index) + "-data.json"):
		Base.start_load("Loading Tavern Data")
		file.open("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "-tavern-" + str(Base.building_index) + "-data.json", File.READ)
		save = parse_json(file.get_line())
		file.close()
		#thread.start(self, "load_tavern", save)
		load_tavern(save)
	else:
		Base.start_load("Generating Tavern Data")
		#thread.start(self, "generate_tavern")
		generate_tavern()


func prepare_player():
	Base.player.refresh()
	Base.player.position = Vector2(84, 668)
	Base.player.active = true
	Base.player.get_node("Camera2D").limit_left = -84
	Base.player.get_node("Camera2D").limit_top = -10000000
	Base.player.get_node("Camera2D").limit_right = 4584
	Base.player.get_node("Camera2D").limit_bottom = 10000000
	Base.player.get_node("Camera2D").current = true
	Base.player.get_node("Camera2D").reset_smoothing()
	
	$ParallaxBackground/Entities.add_child(Base.player)


func load_tavern(data):
	mutex.lock()
	layers[0] = pixelmap.instance()
	layers[0].load_data(data["Foreground"])
	layers[0].set_collisions()
	print("foreground loaded")
	layers[1] = []
	for entity in save["Entities"]:
		if entity != null and "Object" in entity and Directory.new().file_exists("res://Scenes/Entities/" + entity["Object"] + ".tscn"):
			var inst = load("res://Scenes/Entities/" + entity["Object"] + ".tscn").instance()
			inst.generate(entity)
			layers[6].append(inst)
	print("layers[1] loaded")
	mutex.unlock()


func generate_tavern():
	mutex.lock()
	
	layers[0] = pixelmap.instance()
	layers[1] = []
	
	for x in SW/4:
		for y in SH/4:
			layers[0].set_cell(x, y, 42)
	
	var floormap = [[42, 0], [42, 0], [42, 0], [42, 0]]
	var pos = 0
	var height = 0
	var stretch = 2 + randi()%5
	while pos < SW/4 - 8:
		for i in 5 + randi()%5:
			floormap.append([42, height])
			pos += 1
		floormap.append([43, height])
		pos += 1
		
		stretch -= 1
		if stretch <= 0:
			stretch = 2 + randi()%5
			height = 0 if height == 1 else 1
	floormap += [[42, 0], [42, 0], [42, 0], [42, 0]]
	var y = SH/4 + 32
	for i in 40:
		for x in SW/4:
			layers[0].set_cell(x, y, 9)
		y -= 1
	for i in 3:
		for x in SW/4:
			layers[0].set_cell(x, y+floormap[x][1], floormap[x][0])
		y -= 1
	for i in 3:
		for x in SW/4:
			layers[0].set_cell(x, y+floormap[x][1]-i, 40)
	for i in 4:
		for x in SW/4:
			if floormap[x][0] == 43:
				if layers[0].get_cell(x+i, y+floormap[x][1]-i) == 40:
					layers[0].set_cell(x+i, y+floormap[x][1]-i, 41)
				if layers[0].get_cell(x+1+i, y+floormap[x][1]-i) == 40:
					layers[0].set_cell(x+1+i, y+floormap[x][1]-i, 41)
	y -= 3
	
	for i in 4:
		for j in SH/4 - 7:
			layers[0].set_cell(i, j, 42)
	for j in SH/4 - 7:
		layers[0].set_cell(4, j, 43)
	for i in 4:
		for j in SH/4 - 10 - i:
			layers[0].set_cell(5 + i, j, 43)
			
	var door_bitmap = [
		[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,43,43],
		[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,43,43],
		[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,3,43,43],
		[0,3,3,3,43,43,9,9,9,9,9,9,9,3,3,3,43,43,0],
		[0,44,3,3,43,43,9,9,9,9,9,9,9,44,3,3,43,43,0],
		[0,44,44,3,43,43,9,9,9,9,9,9,9,44,44,3,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,44,44,44,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,44,44,44,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,44,44,44,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,44,44,44,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,44,44,44,43,43,0],
		[0,44,44,44,43,43,9,9,9,9,9,9,9,3,3,43,43,0,0],
		[0,0,3,3,3,43,9,9,9,9,9,9,9,3,44,43,43,0,0],
		[0,0,44,44,3,43,9,9,9,9,9,9,9,44,44,43,43,0,0],
		[0,0,44,44,44,43,9,9,9,9,9,9,9,44,44,43,43,0,0],
		[0,0,44,44,44,43,9,9,9,9,9,9,9,44,44,43,43,0,0],
		[0,0,44,44,44,43,9,9,9,9,9,9,9,44,44,43,43,0,0],
		[0,0,44,44,44,43,9,9,9,9,9,9,9,44,44,43,43,0,0],
	]
	
	var c = 0
	for row in door_bitmap:
		var r = 0
		for item in row:
			if item != 0:
				if layers[0].get_cell(14 + r, SH/4 - 48 + c) == 42:
					layers[0].set_cell(14 + r, SH/4 - 48 + c, item)
				if layers[0].get_cell(15 + r, SH/4 - 48 + c) == 42:
					layers[0].set_cell(15 + r, SH/4 - 48 + c, item)
				if layers[0].get_cell(14 + r, SH/4 - 47 + c) == 42:
					layers[0].set_cell(14 + r, SH/4 - 47 + c, item)
				if layers[0].get_cell(15 + r, SH/4 - 47 + c) == 42:
					layers[0].set_cell(15 + r, SH/4 - 47 + c, item)
			r += 2
		c += 2
	
	for i in 6:
		for j in SH/4 - 7 + floormap[SW/4-i-1][1]:
			layers[0].set_cell(SW/4-i-1, j, 42 if i >= 2 else 43)
	
	var x = 51
	while x < SW/4 - 72:
		if randi()%10 == 0:
			var tableinstance = table.instance()
			tableinstance.position = layers[0].map_to_world(Vector2(x, SH/4-19+floormap[x][1]))
			layers[1].add_child(tableinstance)
			if randi()%5 != 0:
				var coin = coins.instance()
				coin.position = Vector2(tableinstance.position.x+randi()%int(tableinstance.dimensions.x-coin.dimensions.x), tableinstance.position.y - coin.dimensions.y)
				layers[1].add_child(coin)
			else:
				var drinkinstance = drink.instance()
				drinkinstance.get_node("AnimatedSprite").frame = 0
				drinkinstance.position = Vector2(tableinstance.position.x+randi()%int(tableinstance.dimensions.x-drinkinstance.dimensions.x), tableinstance.position.y - drinkinstance.dimensions.y)
				layers[1].add_child(drinkinstance)
			x += 30
		x += 1
		
	for i in 2:
		for j in 36:
			layers[0].set_cell(SW/4 - 7 - j, SH/4 - 19 + i, 44)
	for j in 34:
		layers[0].set_cell(SW/4 - 7 - j, SH/4 - 17, 3)
	for i in 6:
		for j in 34:
			layers[0].set_cell(SW/4 - 7 - j, SH/4 - 16 + i, 4)
	for j in 34:
		if floormap[SW/4 - 5 - j][1] == 1:
			layers[0].set_cell(SW/4 - 7 - j, SH/4 - 10, 4)
			
	x = SW/4 - 43
	while x < SW/4 - 13:
		if randi()%6 == 0:
			var drinkinstance = drink.instance()
			drinkinstance.get_node("AnimatedSprite").frame = 1 + randi()%4
			drinkinstance.position = layers[0].map_to_world(Vector2(x, SH/4 - 19))
			drinkinstance.position.y -= drinkinstance.dimensions.y
			layers[1].add_child(drinkinstance)
			x += 6
		x += 1
	
	var taverndoor = door.instance()
	taverndoor.set_name("Door")
	taverndoor.position = Vector2(124, 707)
	layers[1].add_child(taverndoor)
	
	var tavernkeep = barkeep.instance()
	tavernkeep.active = true
	tavernkeep.position = Vector2(SW - 144 - tavernkeep.dimensions.x/2, SH - 52 - tavernkeep.dimensions.y/2)
	layers[1].add_child(tavernkeep)
	
	layers[0].set_collisions()
	
	mutex.unlock()


func _process(_delta):
	if thread != null:
		if not thread.is_alive():
			thread.wait_to_finish()
			Base.end_load()
			thread = null
			if not (null in layers):
				$ParallaxBackground/Foreground.add_child(layers[0])
				for entity in layers[1]:
					$ParallaxBackground/Entities.add_child(entity)
				prepare_player()
	else:
		if $ParallaxBackground/Entities/Door.overlaps_body(Base.player) and Input.is_action_just_pressed("player_interact"):
			$ParallaxBackground/Entities.remove_child(Base.player)
			Base.tile.prepare_player(old_position)
			Base.building_index = null
			Base.building = null
			Base.change_scene_to(Base.tile)


func get_entities():
	return $ParallaxBackground/Entities


func get_uilayer():
	return $UILayer


func save_data():
	print("saving tavern")
	if null in layers:
		return
	print("step 1 down")
	var savedata = {
		"Foreground": layers[0].save_data(),
		"Entities": [],
		"Door Position": var2str($ParallaxBackground/Foreground/Door.position),
	}
	print("step 2 down")
	for entity in layers[1]:
		savedata["Entities"].append(entity.save_data())
	print("step 3 down")
	savedata = to_json(savedata)
	print("opening file")
	var file = File.new()
	file.open("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "-tavern-" + str(Base.building_index) + "-data.json", File.WRITE)
	file.store_line(savedata)
	file.close()
	print("saved")
