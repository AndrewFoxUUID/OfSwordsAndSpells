extends Character

const POTENTIAL_STOCK = ["Reinforced Buckler", "Plate Shield", "Wooden Buckler", "Plate Helm", "Barbuta", "Plate Boots", "Leather Boots", "Old Hat", "Squire Helm", "Leather Tunic", "Plate Tunic", "Plate Armor", "Leather Gloves", "Inset Gauntlets", "Plate Gauntlets", "Crescent Shield", "Kite", "Heater", "Salade", "Old Plate Tunic"]

var dimensions = Vector2(72, 72)*scale.x

var inventory = []

func _ready():
	._ready()
	max_health = 4
	health = 4
	speed = 200.0
	
	var added_indices = []
	for i in 4:
		var rand = randi()%len(POTENTIAL_STOCK)
		while rand in added_indices:
			rand = randi()%len(POTENTIAL_STOCK)
		added_indices.append(rand)
		inventory.append({"name": POTENTIAL_STOCK[rand], "quantity": [1, 1, 1, 1, 2, 2, 3][randi()%7]})


func animation():
	return $AnimatedSprite.animation


func play(animation):
	$AnimatedSprite.play(animation)


func generate(data):
	position = Vector2(data["x"], data["y"])
	health = data["health"]
	inventory = data["inventory"]
	play(data["animation"])
	$AnimatedSprite.playing = true
	$AnimatedSprite.frame = data["frame"]
	$AnimatedSprite.flip_h = data["flip"]
	active = true


func _physics_process(delta):
	if active:
		velocity.x = 0
		
		if animation() != "Die":
			if $Area2D.overlaps_body(Base.player) and not Base.popup_active and Input.is_action_pressed("player_interact"):
				Base.popup_active = true
				var menu = load("res://Scenes/UIElements/ShopMenu.tscn").instance()
				menu.seller_inv = inventory
				menu.connect("items_purchased", self, "sell")
				menu.connect("items_sold", self, "buy")
				Base.get_uilayer().add_child(menu)
			
		if $Area2D.overlaps_body(Base.player) and animation() != "Die":
			$TextPopup.playing = true
		else:
			$TextPopup.playing = false
			$TextPopup.frame = 0
		$Label.visible = $TextPopup.frame == 8
			
		.move(delta)


func sell(item_name, quantity):
	var price = Constants.ITEM_DATA[item_name]["buy"] * quantity
	if price > int(price):
		price = int(price) + 1
	if Base.player.inventory["coins"]["quantity"] >= price:
		Base.player.inventory["coins"]["quantity"] -= price
		Base.player.pickup_item(item_name, quantity)
		for i in len(inventory):
			if inventory[i]["name"] == item_name:
				inventory[i]["quantity"] -= quantity
				if inventory[i]["quantity"] <= 0:
					inventory.remove(i)
				return


func buy(item_name, quantity):
	var price = int(Constants.ITEM_DATA[item_name]["sell"] * quantity)
	if Base.player.get_num(item_name) >= quantity:
		Base.player.inventory["coins"]["quantity"] += price
		Base.player.drop_item(item_name, quantity)
		for i in len(inventory):
			if inventory[i]["name"] == item_name:
				inventory[i]["quantity"] += quantity
				return
		inventory.append({"name": item_name, "quantity": quantity})


func _on_AnimatedSprite_animation_finished():
	if active:
		$AnimatedSprite.frame = 0
		if animation() == "Idle":
			play(["Idle", "Idle", "Block"][randi()%3])
		else:
			play("Idle")
		$AnimatedSprite.flip_h = [true, false, $AnimatedSprite.flip_h][randi()%3]


func save_data():
	return {
		"Object": "ArmorDealer",
		"x": position.x,
		"y": position.y,
		"health": health,
		"animation": animation(),
		"frame": $AnimatedSprite.frame,
		"flip": $AnimatedSprite.flip_h,
		"inventory": inventory
	}
