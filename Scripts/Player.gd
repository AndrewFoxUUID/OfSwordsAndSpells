extends Character

onready var TextParticle = preload("res://Scenes/UIElements/TextParticle.tscn")

var dimensions = Vector2(72, 72)*scale.x

var hair_style = 0
var colors = Base.default_colors.duplicate()

var hide_equipment

var jump_force = 550.0

var falltime = 0
var shake_intensity = 0
var cooldown = 0
var entering_tile = 0
var leaving_tile = 0
var distorting = false

var savename
var playername = ""
var soul_energy = 0
var inventory = {
	"martial weapon": null,
	"magic weapon": null,
	"helm": null,
	"charm": null,
	"armor": null,
	"ring": null,
	"boots": null,
	"gauntlets": null,
	"shield": null,
	"item": null,
	"coins": {"name": "Coins", "quantity": 0},
	"ammunition": null,
	"inventory": [
		{"name": "Short Sword", "quantity": 1},
		{"name": "Chain Tunic", "quantity": 1},
		{"name": "Old Boots", "quantity": 1},
		{"name": "Old Gloves", "quantity": 1},
		{"name": "Apple", "quantity": 2}
	]
}
var spell_slots = [null, null, null, null, null, null, null, null, null, null] # it takes materials to add a spell from known_spells to spell_slots
var known_spells = [] # limitless
var settings = {
	"autosave": false,
	"zoom": 1.0
}
var dialogue_history = []

var max_energy = {
	"r": 0, # radiant
	"s": 0, # shadow
	"l": 0, # life
	"d": 0, # death
	"f": 0, # forge
	"t": 0, # true
	"n": 0  # null
}
var energy = {
	"r": 0,
	"s": 0,
	"l": 0,
	"d": 0,
	"f": 0,
	"t": 0,
	"n": 0
}

func _ready():
	#for item_name in Constants.ITEM_DATA: # for inventory and item testing purposes
	#	if get_num(item_name) == 0: pickup_item(item_name)
	
	._ready()
	speed = 250.0
	max_health = 8
	health = 8
	
	construct_skin()
	play("Idle")


func generate(playerdata):
	playername = playerdata["playername"]
	hair_style = playerdata["hair_style"]
	colors = {}
	for color in playerdata["colors"]:
		colors[color] = Color(playerdata["colors"][color])
	max_health = playerdata["max_health"]
	health = playerdata["health"]
	soul_energy = playerdata["soul_energy"]
	inventory = playerdata["inventory"]
	spell_slots = playerdata["spell_slots"]
	known_spells = playerdata["known_spells"]
	dialogue_history = playerdata["dialogue_history"]
	
	refresh()
	construct_skin()
	play("Idle")


func refresh():
	.refresh()
	hide_equipment = false
	scale = Vector2(2, 2)


func is_valid():
	return typeof(playername) == TYPE_STRING and not playername.empty()


func get_level():
	if soul_energy > 0:
		return floor(log(soul_energy)/log(2))
	return 0


func gain_soul_energy(amount):
	var prev_level = get_level()
	soul_energy += amount
	var cur_level = get_level()
	if cur_level > prev_level:
		distorting = true
		if cur_level >= 1:
			if not ("Plane Step" in known_spells):
				known_spells.append("Plane Step")
			spell_slots[8] = "Plane Step"
		if cur_level >= 2:
			if not ("World Walk" in known_spells):
				known_spells.append("World Walk")
			spell_slots[9] = "World Walk"


func recolor():
	$SpriteLayers/Player.material.set("shader_param/eye", colors["eye"])
	$SpriteLayers/Player.material.set("shader_param/dark_eye", colors["dark_eye"])
	$SpriteLayers/Player.material.set("shader_param/skin", colors["skin"])
	$SpriteLayers/Player.material.set("shader_param/dark_skin", colors["dark_skin"])
	$SpriteLayers/Player.material.set("shader_param/shirt", colors["shirt"])
	$SpriteLayers/Player.material.set("shader_param/pants", colors["pants"])
	$SpriteLayers/Player.material.set("shader_param/dark_pants", colors["dark_pants"])
	$SpriteLayers/Player.material.set("shader_param/shoe", colors["shoe"])
	$SpriteLayers/Player.material.set("shader_param/dark_shoe", colors["dark_shoe"])
	
	$SpriteLayers/Hair1.material.set("shader_param/hair", colors["hair"])
	$SpriteLayers/Hair2.material.set("shader_param/hair", colors["hair"])
	$SpriteLayers/Hair3.material.set("shader_param/hair", colors["hair"])
	$SpriteLayers/Hair4.material.set("shader_param/hair", colors["hair"])
	
	$SpriteLayers/Shield.material.set("shader_param/light_shield", colors["light_shield"])
	$SpriteLayers/Shield.material.set("shader_param/shield", colors["shield"])
	$SpriteLayers/Shield.material.set("shader_param/dark_shield", colors["dark_shield"])
	$SpriteLayers/Shield.material.set("shader_param/shield_flair", colors["shield_flair"])
	
	$SpriteLayers/Armor.material.set("shader_param/light_armor", colors["light_armor"])
	$SpriteLayers/Armor.material.set("shader_param/armor", colors["armor"])
	$SpriteLayers/Armor.material.set("shader_param/dark_armor", colors["dark_armor"])
	$SpriteLayers/Armor.material.set("shader_param/armor_flair", colors["armor_flair"])
	
	$SpriteLayers/Charm.material.set("shader_param/charm", colors["charm"])
	$SpriteLayers/Charm.material.set("shader_param/charm_flair", colors["charm_flair"])
	
	$SpriteLayers/Helm.material.set("shader_param/light_helm", colors["light_helm"])
	$SpriteLayers/Helm.material.set("shader_param/helm", colors["helm"])
	$SpriteLayers/Helm.material.set("shader_param/dark_helm", colors["dark_helm"])
	$SpriteLayers/Helm.material.set("shader_param/helm_flair", colors["helm_flair"])
	
	$SpriteLayers/Boots.material.set("shader_param/light_boot", colors["light_boot"])
	$SpriteLayers/Boots.material.set("shader_param/boot", colors["boot"])
	$SpriteLayers/Boots.material.set("shader_param/dark_boot", colors["dark_boot"])
	$SpriteLayers/Boots.material.set("shader_param/boot_flair", colors["boot_flair"])
	
	$SpriteLayers/Gauntlets.material.set("shader_param/light_gauntlet", colors["light_gauntlet"])
	$SpriteLayers/Gauntlets.material.set("shader_param/gauntlet", colors["gauntlet"])
	$SpriteLayers/Gauntlets.material.set("shader_param/dark_gauntlet", colors["dark_gauntlet"])
	$SpriteLayers/Gauntlets.material.set("shader_param/gauntlet_flair", colors["gauntlet_flair"])
	
	$SpriteLayers/Ring.material.set("shader_param/ring", colors["ring"])
	
	$SpriteLayers/Sword.material.set("shader_param/weapon_follow", colors["weapon_follow"])
	$SpriteLayers/Sword.material.set("shader_param/dark_weapon_follow", colors["dark_weapon_follow"])
	$SpriteLayers/Sword.material.set("shader_param/light_weapon", colors["light_weapon"])
	$SpriteLayers/Sword.material.set("shader_param/weapon", colors["weapon"])
	$SpriteLayers/Sword.material.set("shader_param/dark_weapon", colors["dark_weapon"])
	$SpriteLayers/Sword.material.set("shader_param/weapon_flair", colors["weapon_flair"])
	
	$SpriteLayers/Spear.material.set("shader_param/weapon_follow", colors["weapon_follow"])
	$SpriteLayers/Spear.material.set("shader_param/dark_weapon_follow", colors["dark_weapon_follow"])
	$SpriteLayers/Spear.material.set("shader_param/light_weapon", colors["light_weapon"])
	$SpriteLayers/Spear.material.set("shader_param/weapon", colors["weapon"])
	$SpriteLayers/Spear.material.set("shader_param/dark_weapon", colors["dark_weapon"])
	$SpriteLayers/Spear.material.set("shader_param/weapon_flair", colors["weapon_flair"])
	
	$SpriteLayers/Axe.material.set("shader_param/weapon_follow", colors["weapon_follow"])
	$SpriteLayers/Axe.material.set("shader_param/dark_weapon_follow", colors["dark_weapon_follow"])
	$SpriteLayers/Axe.material.set("shader_param/light_weapon", colors["light_weapon"])
	$SpriteLayers/Axe.material.set("shader_param/weapon", colors["weapon"])
	$SpriteLayers/Axe.material.set("shader_param/dark_weapon", colors["dark_weapon"])
	$SpriteLayers/Axe.material.set("shader_param/weapon_flair", colors["weapon_flair"])
	
	$SpriteLayers/Dagger.material.set("shader_param/weapon_follow", colors["weapon_follow"])
	$SpriteLayers/Dagger.material.set("shader_param/dark_weapon_follow", colors["dark_weapon_follow"])
	$SpriteLayers/Dagger.material.set("shader_param/light_weapon", colors["light_weapon"])
	$SpriteLayers/Dagger.material.set("shader_param/weapon", colors["weapon"])
	$SpriteLayers/Dagger.material.set("shader_param/dark_weapon", colors["dark_weapon"])
	$SpriteLayers/Dagger.material.set("shader_param/weapon_flair", colors["weapon_flair"])
	
	$SpriteLayers/Club.material.set("shader_param/weapon_follow", colors["weapon_follow"])
	$SpriteLayers/Club.material.set("shader_param/dark_weapon_follow", colors["dark_weapon_follow"])
	$SpriteLayers/Club.material.set("shader_param/light_weapon", colors["light_weapon"])
	$SpriteLayers/Club.material.set("shader_param/weapon", colors["weapon"])
	$SpriteLayers/Club.material.set("shader_param/dark_weapon", colors["dark_weapon"])
	$SpriteLayers/Club.material.set("shader_param/weapon_flair", colors["weapon_flair"])


func construct_skin():
	var data
	$SpriteLayers/Player.visible = true

	$SpriteLayers/Hair1.visible = false
	$SpriteLayers/Hair2.visible = false
	$SpriteLayers/Hair3.visible = false
	$SpriteLayers/Hair4.visible = false
	if hair_style == 1:
		$SpriteLayers/Hair1.visible = true
	elif hair_style == 2:
		$SpriteLayers/Hair2.visible = true
	elif hair_style == 3:
		$SpriteLayers/Hair3.visible = true
	elif hair_style == 4:
		$SpriteLayers/Hair4.visible = true
	
	$SpriteLayers/Helm.visible = false
	if inventory["helm"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["helm"]["name"]]
		colors["light_helm"] = data["light_color"]
		colors["helm"] = data["color"]
		colors["dark_helm"] = data["dark_color"]
		colors["helm_flair"] = data["flair_color"]
		
		match data["player_style"]:
			"helm":
				$SpriteLayers/Hair1.visible = false
				$SpriteLayers/Hair2.visible = false
				$SpriteLayers/Hair3.visible = false
				$SpriteLayers/Hair4.visible = false
				$SpriteLayers/Helm.visible = true
				
	$SpriteLayers/Shield.visible = false
	if inventory["shield"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["shield"]["name"]]
		colors["light_shield"] = data["light_color"]
		colors["shield"] = data["color"]
		colors["dark_shield"] = data["dark_color"]
		colors["shield_flair"] = data["flair_color"]
			
		match data["player_style"]:
			"shield":
				$SpriteLayers/Shield.visible = true
	
	$SpriteLayers/Armor.visible = false
	if inventory["armor"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["armor"]["name"]]
		colors["light_armor"] = data["light_color"]
		colors["armor"] = data["color"]
		colors["dark_armor"] = data["dark_color"]
		colors["armor_flair"] = data["flair_color"]
		
		match data["player_style"]:
			"armor":
				$SpriteLayers/Armor.visible = true
				
	$SpriteLayers/Boots.visible = false
	if inventory["boots"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["boots"]["name"]]
		colors["light_boot"] = data["light_color"]
		colors["boot"] = data["color"]
		colors["dark_boot"] = data["dark_color"]
		colors["boot_flair"] = data["flair_color"]
		
		match data["player_style"]:
			"boots":
				$SpriteLayers/Boots.visible = true
				
	$SpriteLayers/Gauntlets.visible = false
	if inventory["gauntlets"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["gauntlets"]["name"]]
		colors["light_gauntlet"] = data["light_color"]
		colors["gauntlet"] = data["color"]
		colors["dark_gauntlet"] = data["dark_color"]
		colors["gauntlet_flair"] = data["flair_color"]
		
		match data["player_style"]:
			"gauntlets":
				$SpriteLayers/Gauntlets.visible = true
				
	$SpriteLayers/Ring.visible = false
	if inventory["ring"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["ring"]["name"]]
		colors["ring"] = data["color"]
		
		match data["player_style"]:
			"ring":
				$SpriteLayers/Ring.visible = true
				
	$SpriteLayers/Charm.visible = false
	if inventory["charm"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["charm"]["name"]]
		colors["charm"] = data["color"]
		colors["charm_flair"] = data["flair_color"]
		
		match data["player_style"]:
			"charm":
				$SpriteLayers/Charm.visible = true
		
	$SpriteLayers/Sword.visible = false
	$SpriteLayers/Spear.visible = false
	$SpriteLayers/Axe.visible = false
	$SpriteLayers/Dagger.visible = false
	$SpriteLayers/Club.visible = false
	if inventory["martial weapon"] != null and not hide_equipment:
		data = Constants.ITEM_DATA[inventory["martial weapon"]["name"]]
		colors["weapon_follow"] = data["color"]
		colors["dark_weapon_follow"] = Color8(max(0, data["color"].r8 - 50), max(0, data["color"].g8 - 50), max(0, data["color"].b8 - 50))
		colors["light_weapon"] = data["light_color"]
		colors["weapon"] = data["color"]
		colors["dark_weapon"] = data["dark_color"]
		colors["weapon_flair"] = data["flair_color"]
			
		match data["player_style"]:
			"sword":
				$SpriteLayers/Sword.visible = true
			"spear":
				$SpriteLayers/Spear.visible = true
			"axe":
				$SpriteLayers/Axe.visible = true
			"dagger":
				$SpriteLayers/Dagger.visible = true
			"club":
				$SpriteLayers/Club.visible = true


func play(animation):
	for layer in $SpriteLayers.get_children():
		layer.play(animation)


func animation():
	return $SpriteLayers/Player.animation


func get_frame():
	return $SpriteLayers/Player.frame


func set_frame(frame):
	for layer in $SpriteLayers.get_children():
		layer.frame = frame


func get_flip_h():
	return $SpriteLayers/Player.flip_h


func set_flip_h(flip):
	for layer in $SpriteLayers.get_children():
		layer.flip_h = flip


func get_items(exclude=[]):
	var items = []
	
	for slot in inventory:
		if slot in exclude or slot == "inventory":
			continue
		items.append(inventory[slot])
	
	return items


func get_inv():
	return get_items() + inventory["inventory"]


func get_num(item_name):
	for item in get_inv():
		if item != null and item["name"] == item_name:
			return item["quantity"]
	return 0


func inventory_clicked(inv_index):
	var slot = Constants.ITEM_DATA[inventory["inventory"][inv_index]["name"]]["slot"] if "slot" in Constants.ITEM_DATA[inventory["inventory"][inv_index]["name"]] else "item"
	var old_item = inventory[slot]
	inventory[slot] = inventory["inventory"][inv_index]
	inventory["inventory"].pop_at(inv_index)
	if old_item != null:
		inventory["inventory"].append(old_item)


func inventory_slot_clicked(slot):
	if inventory[slot] != null and inventory[slot]["name"] != "Coins":
		inventory["inventory"].append(inventory[slot])
		inventory[slot] = null


func pickup_item(item_name, quantity=1):
	for item in get_inv():
		if item != null and item["name"] == item_name:
			item["quantity"] += quantity
			return
	inventory["inventory"].append({"name": item_name, "quantity": quantity})


func drop_item(item_name, quantity=1):
	for slot in inventory:
		if slot != "inventory" and inventory[slot] != null and inventory[slot]["name"] == item_name:
			inventory[slot]["quantity"] -= quantity
			if inventory[slot]["quantity"] <= 0:
				inventory[slot] = null
			return
	for i in len(inventory["inventory"]):
		if inventory["inventory"][i]["name"] == item_name:
			inventory["inventory"][i]["quantity"] -= quantity
			if inventory["inventory"][i]["quantity"] <= 0:
				inventory["inventory"].remove(i)
			return


func getModifier(name):
	var modifier = 0
	for item in get_items():
		if item != null:
			var data = Constants.ITEM_DATA[item["name"]]
			if name in data:
				modifier += data[name]
	return modifier


func attack(attackArea, amount: int, type='') -> int:
	var successes = 0
	for entity in Base.get_entities().get_children():
		if entity != self and entity is Character and attackArea.overlaps_body(entity):
			if entity.hurt(amount, type):
				var particle = TextParticle.instance()
				particle.rect_position = entity.position # temp
				particle.text = "-" + str(amount)
				particle.set("custom_colors/font_color", {'': Color8(107, 104, 93), 'l': Color8(0, 102, 51), 'w': Color8(38, 68, 144), 'b': Color8(126, 2, 31), 'd': Color8(66, 3, 97), 'c': Color8(219, 187, 61)}[type])
				Base.get_entities().add_child(particle)
				successes += 1
	return successes


func martialAttack(weapon):
	var damage = getModifier("martial_damage_increase")
	var type = ''
	var area
	if weapon is Dictionary:
		var data = Constants.ITEM_DATA[weapon["name"]]
		damage = data["damage"]
		match data["player_style"]:
			"sword":
				area = $SwordArea
			"spear":
				area = $SpearArea
			"axe":
				area = $AxeArea
			"dagger":
				area = $DaggerArea
			"club":
				area = $ClubArea
	elif weapon == 1:
		damage = 1
		area = $JabArea
	elif weapon == 2:
		damage = 2
		area = $CrossArea
	
	area.get_node("CollisionShape2D").position.x = abs(area.get_node("CollisionShape2D").position.x)
	if get_flip_h(): area.get_node("CollisionShape2D").position.x *= -1
	
	var crit_chance = 10 + getModifier("critical_chance_increase")
	if randi()%100 < crit_chance:
		damage *= 2
		type = 'c'
	
	attack(area, damage, type)


func get_speed():
	return speed + getModifier("speed_increase")


func getArmorClass():
	return getModifier("armor")/4


func hurt(amount:int, type='') -> bool:
	if amount > 0:
		if animation() == "Block":
			var block_chance = Constants.ITEM_DATA[inventory["shield"]["name"]]["block_chance"] + getModifier("block_chance_increase")
			if randi()%100 < block_chance:
				return false # TODO: make a block flash particle
	
	return .hurt(amount, type)


func can_cast(spell):
	var spell_cost = {}
	for energy_type in Constants.SPELL_DATA[spell]["cost"]:
		if not (energy_type in spell_cost):
			spell_cost[energy_type] = 0
		spell_cost[energy_type] += 1
	var seen_upper = []
	for energy_type in spell_cost:
		if energy_type.to_upper() == energy_type:
			if energy_type in seen_upper and energy[energy_type] < max_energy[energy_type]:
				return false
			seen_upper.append(energy_type)
		elif spell_cost[energy_type] > energy[energy_type]:
			return false
	return true


func _physics_process(delta):
	recolor()
	if cooldown > 0:
		cooldown -= 1
		
	if active:
		velocity.x = 0
		
		if Input.is_action_just_pressed("ui_focus_next"): # TODO: for testing purposes only
			gain_soul_energy(2)
		
		$Camera2D.zoom = Vector2(settings["zoom"], settings["zoom"])
		$Camera2D.offset = Vector2((randi()%(shake_intensity*20+1)-(shake_intensity*10))/10, (randi()%(shake_intensity*20+1)-(shake_intensity*10))/10)
		shake_intensity = 0
		if distorting:
			Base.get_node("CanvasLayer/DistortionLayer").material.set(
				"shader_param/radius",
				Base.get_node("CanvasLayer/DistortionLayer").material.get("shader_param/radius") + 0.01
			)
			if Base.get_node("CanvasLayer/DistortionLayer").material.get("shader_param/radius") >= 1.0:
				distorting = false
				Base.get_node("CanvasLayer/DistortionLayer").material.set("shader_param/radius", 0.0)
		
		if not entering_tile and animation() in ["Idle", "Run"]:
			if cooldown == 0 and Input.is_action_just_pressed("use_item"):
				if inventory["item"] != null:
					var data = Constants.ITEM_DATA[inventory["item"]["name"]]
					if "consumable" in data and data["consumable"]:
						if "life_gain" in data:
							hurt(-data["life_gain"])
							drop_item(inventory["item"]["name"])
							cooldown = 100
			
			if cooldown == 0 and Input.is_action_pressed("player_jump") and grounded:
				velocity.y = -jump_force
				play("Jump")
			elif cooldown == 0 and Input.is_action_pressed("player_roll"):
				play("Roll")
				cooldown = 100
			elif cooldown == 0 and Input.is_action_pressed("player_attack"):
				if inventory["martial weapon"] != null:
					match Constants.ITEM_DATA[inventory["martial weapon"]["name"]]["player_style"]:
						"sword":
							play("Sword")
						"spear":
							play("Spear")
						"axe":
							play("Axe")
						"dagger":
							play("Dagger")
						"club":
							play("Club")
					cooldown = 100
			elif cooldown == 0 and Input.is_action_pressed("player_jab"):
				play("Jab")
			elif cooldown == 0 and Input.is_action_pressed("player_cross"):
				play("Cross")
				cooldown = 50
			elif Input.is_action_pressed("player_block"):
				if inventory["shield"] != null:
					play("Block")
			elif not grounded and falltime > 10:
				play("Fall")
			elif Input.is_action_pressed("player_move_right"):
				play("Run")
				set_flip_h(false)
			elif Input.is_action_pressed("player_move_left"):
				play("Run")
				set_flip_h(true)
			else:
				play("Idle")
		
		$CollisionShape2D.shape.extents.y = 16.5
		$CollisionShape2D.position.y = 19.5
		match animation():
			"Sword":
				if get_frame() == 4:
					martialAttack(inventory["martial weapon"])
			"Spear":
				if get_frame() == 3:
					martialAttack(inventory["martial weapon"])
			"Axe":
				if get_frame() == 4:
					martialAttack(inventory["martial weapon"])
			"Dagger":
				if get_frame() in [2, 4, 6]:
					martialAttack(inventory["martial weapon"])
			"Club":
				if get_frame() == 4:
					martialAttack(inventory["martial weapon"])
			"Jab":
				if get_frame() == 3:
					martialAttack(1)
			"Cross":
				if get_frame() == 3:
					martialAttack(2)
			"Block":
				pass
			"Roll":
				$CollisionShape2D.shape.extents.y = 8
				$CollisionShape2D.position.y = 28
				velocity.x += -get_speed()-2 if get_flip_h() else get_speed()+2
			"Jump":
				if Input.is_action_pressed("player_move_right"):
					velocity.x += get_speed()
					set_flip_h(false)
				elif Input.is_action_pressed("player_move_left"):
					velocity.x -= get_speed()
					set_flip_h(true)
			"Fall":
				if Input.is_action_pressed("player_move_right"):
					velocity.x += get_speed()
					set_flip_h(false)
				elif Input.is_action_pressed("player_move_left"):
					velocity.x -= get_speed()
					set_flip_h(true)
				if grounded:
					play("Land")
					falltime = 0
			"Land":
				if Input.is_action_pressed("player_move_right"):
					velocity.x += get_speed()*0.9
					set_flip_h(false)
				elif Input.is_action_pressed("player_move_left"):
					velocity.x -= get_speed()*0.9
					set_flip_h(true)
			"Run":
				velocity.x += -get_speed() if get_flip_h() else get_speed()
		
		.move(delta)
		
		if entering_tile:
			if falltime > 0 and grounded:
				if $TileFlash.frame == 12:
					if entering_tile == 2:
						entering_tile = 0
					else:
						$TileFlash.frame = 0
						entering_tile = 2
				elif $TileFlash.frame == 4:
					$SpriteLayers.visible = true
				$EnterProjectile.visible = false
			else:
				$SpriteLayers.visible = false
				$EnterProjectile.visible = true
		elif leaving_tile:
			if $TileFlash.frame == 12:
				if leaving_tile == 2:
					Base.get_entities().remove_child(self)
				else:
					$TileFlash.frame = 0
			elif $TileFlash.frame >= 4:
				$SpriteLayers.visible = false
		
		falltime += 1 if grounded else -falltime
		
		if get_level() >= 1:
			for energy_type in max_energy:
				max_energy[energy_type] = 0
			var world_coords = Vector2(Base.tile_index%33, Base.tile_index/33)
			for energy_type in Constants.TILE_DATA[Base.world.get_node("TileMap").get_node("Tiles").get_cellv(world_coords)][1]:
				max_energy[energy_type] += 2
			for tile in Base.world.getSurroundingTiles(world_coords):
				for energy_type in Constants.TILE_DATA[Base.world.get_node("TileMap").get_node("Tiles").get_cellv(tile)][1]:
					max_energy[energy_type] += 1
		
	construct_skin()
	
	# spell accumulation:
	if get_level() >= 1 and Base.tile != null:
		var energy_types = Constants.TILE_DATA[Base.tile.type][1]
		if "r" in energy_types and not ("Firebolt" in known_spells):
			known_spells.append("Firebolt")
		if "s" in energy_types and not ("Swiftness" in known_spells):
			known_spells.append("Swiftness")
		if "l" in energy_types and not ("Revitalize" in known_spells):
			known_spells.append("Revitalize")
		if "d" in energy_types and not ("Drain" in known_spells):
			known_spells.append("Drain")
		if "f" in energy_types and not ("Smite" in known_spells):
			known_spells.append("Smite")


func _on_Sprite_animation_finished():
	if not $SpriteLayers/Player.frames.get_animation_loop(animation()):
		if animation() == "Jump":
			play("Fall")
		elif animation() != "Die":
			play("Idle")


func save():
	var save_colors = {}
	for color in colors:
		save_colors[color] = colors[color].to_html()
	var savedata = to_json({
		"playername": playername,
		"hair_style": hair_style,
		"colors": save_colors,
		"max_health": max_health,
		"health": health,
		"soul_energy": soul_energy,
		"inventory": inventory,
		"spell_slots": spell_slots,
		"known_spells": known_spells,
		"dialogue_history": dialogue_history
	})
		
	var dir = Directory.new()
	dir.open("user://")
	dir.make_dir("Players")
	dir.open("user://Players/")
	dir.make_dir(savename)
	dir.open("user://Players/" + savename + "/")
	dir.make_dir("Sguila/")
	var file = File.new()
	file.open("user://Players/" + savename + "/playerdata.json", File.WRITE)
	file.store_line(savedata)
	file.close()


func _on_EnergyRegenerationTimer_timeout():
	var available_energy_types = []
	for energy_type in energy:
		if energy[energy_type] < max_energy[energy_type]:
			available_energy_types.append(energy_type)
	
	if len(available_energy_types) > 0:
		energy[available_energy_types[randi()%len(available_energy_types)]] += 0.5
