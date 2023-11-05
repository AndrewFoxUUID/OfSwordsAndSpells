extends Node2D

onready var pixelmap = preload("res://Scenes/UIElements/PixelMap.tscn")
onready var star = preload("res://Scenes/UIElements/Star.tscn")
const TW = 8000
const TH = 1920
const WW = 668
const WH = 480

const COLORKEY = {
	"grassland": [5, 15, 19, 18, 2, 7, 9, 0, 1, 3],
	"plains": [5, 15, 19, 18, 13, 22, 14, 1, 0],
	"swamp": [4, 15, 19, 18, 2, 8, 10, 3, 1],
	"savannah": [5, 15, 19, 18, 17, 22, 7, 20, 21],
	"desert": [5, 15, 19, 18, 17, 22, 13, 6, 16],
	"barren": [5, 15, 19, 18, 17, 12, 11, 1, 0],
	"water": [],
	"deep water": [],
}

var structures = {
	"apothecary": load("res://Scenes/Entities/Apothecary.tscn"),
	"chest": load("res://Scenes/Entities/Chest.tscn"),
	"lantern": load("res://Scenes/Entities/Lantern.tscn"),
	"lightpost": load("res://Scenes/Entities/Lightpost.tscn"),
	"tavern": load("res://Scenes/Entities/Tavern.tscn"),
	"marketstall": load("res://Scenes/Entities/MarketStall.tscn"),
	"boxes": load("res://Scenes/Entities/Boxes.tscn"),
	"backgroundshorthouse": load("res://Scenes/Entities/BackgroundShortHouse.tscn"),
	"backgroundtallhouse": load("res://Scenes/Entities/BackgroundTallHouse.tscn"),
	"meadowtree": load("res://Scenes/Entities/MeadowTree.tscn"),
	"largerock": load("res://Scenes/Entities/LargeRock.tscn")
}

var enemies = {
	"armadillo": load("res://Scenes/Entities/Armadillo.tscn")
}

var file
var save

var type

var layers = [null, null, null, null, null, null, []]
var armadillonSpawned = false
var mountainwaveStart = 0

var wait_ticks = 0
var ticks = 0

var mutex
var thread

func mountainwave(x):
	x += mountainwaveStart
	return 50 * (sin(0.02*x) + sin(0.01*PI*x) + sin(0.01*x) + 6.5)


func _ready():
	$LoadLayer/ColorRect/Label.isvisible = false
	$LoadLayer/ColorRect/StoryFrame0.position.x = -$LoadLayer/ColorRect/StoryFrame0.frames.get_frame("default", $LoadLayer/ColorRect/StoryFrame0.frame).get_width() * $LoadLayer/ColorRect/StoryFrame0.scale.x
	$LoadLayer/ColorRect/StoryFrame1.position.y = -$LoadLayer/ColorRect/StoryFrame1.frames.get_frame("default", $LoadLayer/ColorRect/StoryFrame1.frame).get_height() * $LoadLayer/ColorRect/StoryFrame2.scale.y
	$LoadLayer/ColorRect/StoryFrame2.position.y = 500
	ticks = 1
	
	Base.tile = self
	
	type = Base.world.get_tile(Base.tile_index) - 1
	
	mutex = Mutex.new()
	thread = Thread.new()
	file = File.new()
	
	if file.file_exists("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "data.json"):
		file.open("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "data.json", File.READ)
		save = parse_json(file.get_line())
		file.close()
		thread.start(self, "load_data", save)
	else:
		thread.start(self, "generate_tile")


func prepare_player(position):
	Base.player.refresh()
	Base.player.position = position
	Base.player.active = true
	Base.player.get_node("Camera2D").limit_left = -84
	Base.player.get_node("Camera2D").limit_top = -10000000
	Base.player.get_node("Camera2D").limit_right = 4584
	Base.player.get_node("Camera2D").limit_bottom = 10000000
	Base.player.get_node("Camera2D").current = true
	Base.player.get_node("Camera2D").reset_smoothing()
	
	$ParallaxBackground/Entities.add_child(Base.player)


func load_data(data):
	mutex.lock()
	layers[0] = pixelmap.instance()
	layers[0].load_data(data["Skyscape"])
	print("sky loaded")
	for body in save["Celestial Bodies"]:
		var starinst = star.instance()
		starinst.load_data(body)
		layers[0].add_child(starinst)
	print("stars loaded")
	layers[1] = pixelmap.instance()
	layers[1].load_data(data["Mountainscape0"])
	layers[2] = pixelmap.instance()
	layers[2].load_data(data["Mountainscape1"])
	layers[3] = pixelmap.instance()
	layers[3].load_data(data["Mountainscape2"])
	layers[4] = pixelmap.instance()
	layers[4].load_data(data["Mountainscape3"])
	print("mountains loaded")
	layers[5] = pixelmap.instance()
	layers[5].load_data(data["Foreground"])
	layers[5].set_collisions()
	print("foreground loaded")
	armadillonSpawned = save["Armadillon Spawned"]
	layers[6] = []
	for entity in save["Entities"]:
		if entity != null and "Object" in entity and Directory.new().file_exists("res://Scenes/Entities/" + entity["Object"] + ".tscn"):
			var inst = load("res://Scenes/Entities/" + entity["Object"] + ".tscn").instance()
			inst.generate(entity)
			layers[6].append(inst)
	print("entities loaded")
	mutex.unlock()


func generate_mountainscape(index):
	var mountainscape = pixelmap.instance()
	mountainwaveStart = randi()
	
	var extrema = [Vector2(0, WH/4)]
	for x in TW/4:
		if (mountainwave(x-1) < mountainwave(x) and mountainwave(x) > mountainwave(x+1)) or (mountainwave(x-1) > mountainwave(x) and mountainwave(x) < mountainwave(x+1)):
			extrema.append(Vector2(x, mountainwave(x)))
	extrema.append(Vector2(TW/4, WH/4))
	
	var heights = []
	for i in range(len(extrema)-1):
		var x_dif = extrema[i+1][0] - extrema[i][0]
		var y_dif = extrema[i+1][1] - extrema[i][1]
		for j in range(x_dif):
			heights.append(extrema[i][1] + j/x_dif * y_dif + self.mountainwave(extrema[i][0] + j)/2 - 188)
	
	for y in TH/4:
		for x in TW/4:
			if y > TH/4 - heights[x]/4 - 275:
				mountainscape.set_cell(x, y, COLORKEY[Constants.TILE_DATA[type][0]][index+1])
	
	return mountainscape


func generate_tile():
	mutex.lock()
	var colors = COLORKEY[Constants.TILE_DATA[type][0]]
	
	layers[0] = pixelmap.instance()
	for y in TH/4:
		for x in TW/4:
			layers[0].set_cell(x, y, colors[0])
	print("sky generated")
	for y in range(0, TH, 10):
		for x in range(0, TW, 10):
			if randi()%(y/2 + 10) == 0:
				var starinst = star.instance()
				starinst.position = Vector2(x + 2 + randi()%6, y + 2 + randi()%6)
				starinst.radius = 1 + randi()%starinst.MAXRADIUS
				starinst.thickness = randi()%(starinst.MAXTHICKNESS+1)
				starinst.tickspeed = (10 + randi()%4) * (starinst.MAXRADIUS - starinst.radius + 1)
				starinst.mod = randi()%starinst.tickspeed
				starinst.color = Color8(142, 194, 192, 255)
				layers[0].add_child(starinst)
	print("stars generated")
	layers[1] = generate_mountainscape(0)
	layers[2] = generate_mountainscape(1)
	layers[3] = generate_mountainscape(2)
	layers[4] = generate_mountainscape(3)
	print("mountains generated")
	layers[5] = pixelmap.instance()
	layers[6] = []
	
	var height
	var layer1_height
	var layer2_height
	var layer3_height
	var layer4_height
	var x_stretch = 0
	var y_stretch = 0
	var baseline = 100
	var stretch_len = 0
	var pause = 0
	var next_structure = 0
	for x in TW/4:
		if stretch_len == 0:
			baseline += y_stretch
			x_stretch = 20 + randi() % 100
			y_stretch = randi() % 13 - 6
			stretch_len = x_stretch / 2
			
			if len(Constants.TILE_DATA[type][2]) > 0 and randi()%5 == 0: # place structure
				var structure
				var structure_name
				var choice = randi()%100
				for s in Constants.TILE_DATA[type][2]:
					structure_name = s
					if choice < Constants.TILE_DATA[type][2][s]:
						structure = structures[s].instance()
						break
					choice -= Constants.TILE_DATA[type][2][s]
				
				if structure_name in ["tavern", "apothecary"]:
					structure.index = next_structure
					next_structure += 1
				elif structure_name == "marketstall":
					var merchant = structure.MERCHANT_TYPES[randi()%len(structure.MERCHANT_TYPES)].instance()
					merchant.position = Vector2(x*4, (TH/4 - baseline + 1)*4) + Vector2(structure.dimensions.x*2/3 - merchant.dimensions.x/2, -merchant.dimensions.y/2)
					merchant.active = true
					layers[6].append(merchant)
				
				structure.position = Vector2(x*4, (TH/4 - baseline + 1)*4) - Vector2(0, structure.dimensions.y)
				layers[6].append(structure)
				pause = structure.dimensions.x / 4
				
		height = baseline + (y_stretch * sin(PI/x_stretch * (x_stretch/2 - stretch_len)))
		layer1_height = height - (sin(0.5*x) + sin(0.25*PI*x) + 5)
		layer2_height = height - (sin(x) + sin(0.5*PI*x) + 7)
		layer3_height = height - (sin(0.5*x + 50) + sin(0.25*PI*x + 50) + 10)
		layer4_height = height - (2*sin(0.25*x + 50) + 2*sin(0.125*PI*x + 50) + 16)
		
		var yrange = range(TH/4)
		yrange.invert()
		for y in yrange:
			if y > TH/4 - height:
				if y < TH/4 - layer1_height:
					layers[5].set_cell(x, y, colors[5])
				elif y < TH/4 - layer2_height:
					layers[5].set_cell(x, y, colors[6])
				elif y < TH/4 - layer3_height:
					layers[5].set_cell(x, y, colors[7])
				elif y < TH/4 - layer4_height:
					layers[5].set_cell(x, y, colors[8])
				else:
					layers[5].set_cell(x, y, colors[9])
		
		if pause == 0:
			stretch_len -= 1
		else:
			pause -= 1
	layers[5].set_collisions()
	print("foreground generated")
	if len(Constants.TILE_DATA[type][3]) > 0:
		for x in TW:
			if randi()%int(500/len(Constants.TILE_DATA[type][3])) == 0:
				var enemy
				var choice = randi()%100
				for e in Constants.TILE_DATA[type][3]:
					if choice < Constants.TILE_DATA[type][3][e]:
						enemy = enemies[e].instance()
						break
					choice -= Constants.TILE_DATA[type][3][e]
					
				var place_y = -1
				for i in enemy.dimensions.x/4 + 1:
					var top = 0
					while layers[5].get_cell(x/4+i, top) == -1:
						top += 1
					if place_y == -1 or place_y > top:
						place_y = top
				
				enemy.position = Vector2(x, place_y*4 - enemy.dimensions.y)
				enemy.active = true
				layers[6].append(enemy)
	print("entities generated")
	mutex.unlock()


func _process(_delta):
	if thread != null:
		if wait_ticks <= 0:
			if $LoadLayer/ColorRect/StoryFrame0.position.x < -31:
				$LoadLayer/ColorRect/StoryFrame0.position.x += ticks
				ticks += 1
				if $LoadLayer/ColorRect/StoryFrame0.position.x >= -31:
					$LoadLayer/ColorRect/StoryFrame0.playing = true
					$LoadLayer/ColorRect/StoryFrame0.position.x = -31
					ticks = 1
					wait_ticks = 110
			elif $LoadLayer/ColorRect/StoryFrame1.position.y < 46:
				$LoadLayer/ColorRect/StoryFrame1.position.y += ticks
				ticks += 1
				if $LoadLayer/ColorRect/StoryFrame1.position.y >= 46:
					$LoadLayer/ColorRect/StoryFrame1.playing = true
					$LoadLayer/ColorRect/StoryFrame1.position.y = 46
					ticks = 1
					wait_ticks = 250
			elif $LoadLayer/ColorRect/StoryFrame2.position.y > 83:
				$LoadLayer/ColorRect/StoryFrame2.position.y -= ticks
				ticks += 1
				if $LoadLayer/ColorRect/StoryFrame2.position.y <= 83:
					$LoadLayer/ColorRect/StoryFrame2/PlaneSpin.opening = 0
					$LoadLayer/ColorRect/StoryFrame2.position.y = 83
					ticks = 1
		else:
			wait_ticks -= 1
			
		$LoadLayer/ColorRect/Label.isvisible = not thread.is_alive()


func _unhandled_key_input(event):
	if $LoadLayer/ColorRect/Label.isvisible and event.is_pressed():
		thread.wait_to_finish()
		if not (null in layers):
			$ParallaxBackground/Skyscape.add_child(layers[0])
			$ParallaxBackground/Mountainscape0.add_child(layers[1])
			$ParallaxBackground/Mountainscape1.add_child(layers[2])
			$ParallaxBackground/Mountainscape2.add_child(layers[3])
			$ParallaxBackground/Mountainscape3.add_child(layers[4])
			$ParallaxBackground/Foreground.add_child(layers[5])
			for entity in layers[6]:
				$ParallaxBackground/Entities.add_child(entity)
			var pos
			if Base.player.get_level() >= 1:
				pos = Vector2(400, 0)
				Base.player.entering_tile = 1
			else:
				var place_y = -1
				for i in Base.player.dimensions.x:
					i -= Base.player.dimensions.x/2
					var top = 0
					while layers[5].get_cell(100+i, top) == -1:
						top += 1
					if place_y == -1 or top < place_y:
						place_y = top
				pos = Vector2(400, place_y*4 - Base.player.dimensions.y - 4)
			
			prepare_player(pos)
		else:
			print("LAYERS: ", layers)
			printerr("Process in Parallel Thread Failed")
			print_stack()
			push_error("Process in Parallel Thread Failed")
		thread = null
		$LoadLayer/ColorRect/Label.isvisible = false
		$LoadLayer/ColorRect.visible = false


func get_entities():
	return $ParallaxBackground/Entities


func get_uilayer():
	return $UILayer


func save_data():
	print("saving tile")
	if null in layers:
		return
	print("step 1 down")
	var savedata = {
		"Skyscape": layers[0].save_data(),
		"Celestial Bodies": [],
		"Mountainscape0": layers[1].save_data(),
		"Mountainscape1": layers[2].save_data(),
		"Mountainscape2": layers[3].save_data(),
		"Mountainscape3": layers[4].save_data(),
		"Foreground": layers[5].save_data(),
		"Entities": [],
		"Armadillon Spawned": armadillonSpawned
	}
	print("step 2 down")
	for body in layers[0].get_children():
		if body.get_filename() == star.get_path():
			savedata["Celestial Bodies"].append(body.save_data())
	print("step 3 down")
	for entity in layers[6]:
		savedata["Entities"].append(entity.save_data())
	print("step 4 down")
	savedata = to_json(savedata)
	print("opening file")
	var file = File.new()
	file.open("user://Players/" + Base.player.savename + "/" + Base.world_name + "/" + str(Base.tile_index) + "data.json", File.WRITE)
	file.store_line(savedata)
	file.close()
	print("saved")
