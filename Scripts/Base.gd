extends Node

onready var Player = preload("res://Scenes/Player.tscn")
var points = {
	"hair": {},
	"eye": {},
	"dark_eye": {},
	"skin": {},
	"dark_skin": {},
	"shirt": {},
	"pants": {},
	"dark_pants": {},
	"shoe": {},
	"dark_shoe": {},
	"weapon_follow": {},
	"dark_weapon_follow": {},
	"light_weapon": {},
	"weapon": {},
	"dark_weapon": {},
	"weapon_flair": {},
	"light_helm": {},
	"helm": {},
	"dark_helm": {},
	"helm_flair": {},
	"light_shield": {},
	"shield": {},
	"dark_shield": {},
	"shield_flair": {},
	"light_armor": {},
	"armor": {},
	"dark_armor": {},
	"armor_flair": {},
	"light_boot": {},
	"boot": {},
	"dark_boot": {},
	"boot_flair": {},
	"light_gauntlet": {},
	"gauntlet": {},
	"dark_gauntlet": {},
	"gauntlet_flair": {},
	"ring": {},
	"charm": {},
	"charm_flair": {}
}
const animationIndices = {
	"Idle": [1, 2, 3, 4, 5, 6, 7, 8],
	"Run": [9, 10, 11, 12, 13, 14, 15, 16],
	"Jump": [17, 18, 19],
	"Fall": [20],
	"Land": [21, 22],
	"Roll": [23, 24, 25, 26, 27, 28, 29, 30, 31],
	"Jab": [32, 33, 34, 35, 36],
	"Cross": [37, 38, 39, 40, 41],
	"Sword": [42, 43, 44, 45, 46, 47, 48, 49],
	"Spear": [50, 51, 52, 53, 54],
	"Axe": [55, 56, 57, 58, 59, 60, 61],
	"Dagger": [62, 63, 64, 65, 66, 67, 68, 69, 70],
	"Club": [71, 72, 73, 74, 75, 76, 77, 78],
	"Block": [79, 80, 81, 82, 83, 84, 85, 86],
	"Hurt": [87, 88, 89, 90],
	"Die": [91, 92, 93, 94, 95, 96]
}
const animationInfo = {
	"Idle": [6, true],
	"Run": [8, true],
	"Jump": [15, false],
	"Fall": [10, true],
	"Land": [10, false],
	"Roll": [10, false],
	"Jab": [10, false],
	"Cross": [10, false],
	"Sword": [10, false],
	"Spear": [10, false],
	"Axe": [10, false],
	"Dagger": [10, false],
	"Club": [10, false],
	"Block": [6, false],
	"Hurt": [10, false],
	"Die": [5, false]
}
const default_colors = {
	"hair": Color8(29, 15, 27),
	"eye": Color8(38, 68, 144),
	"dark_eye": Color8(14, 14, 16),
	"skin": Color8(214, 182, 148),
	"dark_skin": Color8(206, 157, 130),
	"shirt": Color8(144, 56, 62),
	"pants": Color8(107, 104, 93),
	"dark_pants": Color8(77, 74, 78),
	"shoe": Color8(146, 101, 77),
	"dark_shoe": Color8(121, 84, 64),
	"weapon_follow": Color8(140, 142, 171),
	"dark_weapon_follow": Color8(33, 36, 58),
	"light_weapon": Color8(219, 187, 61),
	"weapon": Color8(179, 184, 212),
	"dark_weapon": Color8(58, 35, 54),
	"weapon_flair": Color8(126, 2, 31),
	"light_helm": Color8(196, 106, 115),
	"helm": Color8(74, 132, 154),
	"dark_helm": Color8(36, 66, 74),
	"helm_flair": Color8(142, 194, 192),
	"light_shield": Color8(81, 146, 113),
	"shield": Color8(127, 188, 73),
	"dark_shield": Color8(112, 154, 248),
	"shield_flair": Color8(94, 110, 218),
	"light_armor": Color8(105, 124, 62),
	"armor": Color8(78, 95, 46),
	"dark_armor": Color8(29, 38, 31),
	"armor_flair": Color8(148, 162, 75),
	"light_boot": Color8(193, 198, 88),
	"boot": Color8(85, 69, 97),
	"dark_boot": Color8(104, 58, 123),
	"boot_flair": Color8(66, 3, 97),
	"light_gauntlet": Color8(216, 152, 77),
	"gauntlet": Color8(209, 119, 58),
	"dark_gauntlet": Color8(232, 193, 112),
	"gauntlet_flair": Color8(244, 238, 192),
	"ring": Color8(255, 255, 255),
	"charm": Color8(0, 102, 51),
	"charm_flair": Color8(83, 0, 0)
}

var prepareSpriteFrames = false

var loader

var thread
var mutex
var quitting = false

var player
var world_name = "Sguila"
var world
var tile_index = 544
var tile
var building_index
var building
var curScene
var popup_active = false
var boss

var load_text = "Loading"
var tick = 0

func _ready():
	get_tree().set_auto_accept_quit(false)
	randomize()
		
	if prepareSpriteFrames:
		var temp = Player.instance()
		for layer in temp.get_node("SpriteLayers").get_children():
			var frames = layer.frames
			for animation in animationIndices:
				frames.remove_animation(animation)
				frames.add_animation(animation)
				frames.set_animation_speed(animation, animationInfo[animation][0])
				frames.set_animation_loop(animation, animationInfo[animation][1])
				for frame in animationIndices[animation]:
					var texture = load("res://assets/Player/" + layer.get_name() + "_" + ("0" if frame < 10 else "") + str(frame) + ".png")
					frames.add_frame(animation, texture)
						
			ResourceSaver.save("res://assets/Resources/" + layer.get_name() + ".tres", frames)
	
	curScene = get_tree().get_root().get_child(get_tree().get_root().get_child_count()-1)


func fetch_player(savename):
	var dirpath = "user://Players/" + savename + "/"
	var file = File.new()
	if file.file_exists(dirpath + "playerdata.json"):
		var p = Player.instance()
		p.savename = savename
		
		file.open(dirpath + "playerdata.json", File.READ)
		p.generate(parse_json(file.get_line()))
		file.close()
		
		return p
	return false
	
	
func _process(_delta):
	if loader != null:
		var t = OS.get_ticks_msec()
		while OS.get_ticks_msec() < t + 100:
			var err = loader.poll()
			if err == ERR_FILE_EOF:
				var resource = loader.get_resource()
				loader = null
				end_load()
				curScene = resource.instance()
				get_tree().get_root().add_child(curScene)
				break
			elif err == OK:
				var progress = int(float(loader.get_stage()) / loader.get_stage_count() * 100)
				load_text = "Loading (" + str(progress) + "%)"
			else:
				print("ERROR in loading")
				loader = null
				break
				
	if thread == null:
		if player != null and player.settings["autosave"]:
			mutex = Mutex.new()
			thread = Thread.new()
			thread.start(self, "save")
	elif not thread.is_alive():
		thread.wait_to_finish()
		thread = null
		if quitting:
			get_tree().quit(0)
	
	var text = load_text
	if tick % 48 >= 12:
		text += "."
	if tick % 48 >= 24:
		text += "."
	if tick % 48 >= 36:
		text += "."
	$PlaneSpin/LoadLabel.text = text
	tick += 1
	
	
func get_entities():
	return curScene.get_entities()
	
	
func get_uilayer():
	return curScene.get_uilayer()
	
	
func change_scene(scenepath):
	popup_active = false
	loader = ResourceLoader.load_interactive(scenepath)
	if loader == null:
		return print("ERROR: Resource Loader is null")
	get_tree().get_root().remove_child(curScene)
	start_load("Loading")
	
	
func change_scene_to(scene):
	popup_active = false
	get_tree().get_root().remove_child(curScene)
	curScene = scene
	get_tree().get_root().add_child(scene)
	
	
func _notification(notification):
	if notification == MainLoop.NOTIFICATION_WM_QUIT_REQUEST:
		quitting = true
		if player != null: player.settings["autosave"] = true
		get_tree().get_root().call_deferred("remove_child", curScene)
		start_load("Saving")
	elif notification == MainLoop.NOTIFICATION_WM_FOCUS_OUT:
		get_tree().paused = true # TODO: maybe this shouldn't trigger every time
	
	
func start_load(text):
	$PlaneSpin.visible = true
	$PlaneSpin.open()
	$PlaneSpin/LoadLabel.visible = true
	load_text = text
	
	
func end_load():
	$PlaneSpin.close()
	$PlaneSpin.visible = false
	$PlaneSpin/LoadLabel.visible = false
	
	
func save():
	mutex.lock()
	
	if player != null and is_instance_valid(player): player.save()
	if world != null and is_instance_valid(world): world.save()
	if tile != null and is_instance_valid(tile): tile.save_data()
	if building != null and is_instance_valid(building): building.save()
	
	mutex.unlock()
