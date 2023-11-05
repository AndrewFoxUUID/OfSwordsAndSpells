extends Character

const POTENTIAL_STOCK = ["Apple", "Cheese", "Omelette", "Pie", "Bread", "Drumstick", "Grapes", "Bananas"]
# for apothecary: const COMPONENT_SELECTION = ["Cleansing Balm", "Plate Bar", "Log", "Twigs", "Wheat", "Mushroom", "Rock", "Mud", "Dye", "Paper", "Milk", "Honey", "Leaf", "Feather"]

var dimensions = Vector2(72, 72)*2

var dialogue
var greeted = false

var inventory = []

func _ready(): # on load, the barkeep is not active, and its animation is not running
	._ready()
	max_health = 4
	health = 4
	speed = 100.0
	
	var added_indices = []
	for i in 4:
		var rand = randi()%len(POTENTIAL_STOCK)
		while rand in added_indices:
			rand = randi()%len(POTENTIAL_STOCK)
		added_indices.append(rand)
		inventory.append({"name": POTENTIAL_STOCK[rand], "quantity": [1, 1, 1, 2, 2, 3, 4, 5][randi()%7]})
	
	
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
			if animation() == "Walk":
				velocity.x += -speed if $AnimatedSprite.flip_h else speed
				
			if not greeted:
				Base.get_node("CanvasLayer").get_node("DialogueQueue").push(
					"Beardo the Barkeep",
					[
						"Howdy there traveler, welcome to Beardo's Beds, Brews, and Bashes, what can I get ya?",
						"We don't want any more visitors, well-wishers ... oh, a customer? Well, what can I get ya?",
						"Belch. Braaaaaaaaap. Exsqueeeeze me, I'm feeling a little queasy, got any gold for meesy?"
					][randi()%3],
					$AnimatedSprite.frames.get_frame("Idle", 0),
					Rect2(28, 38, 12, 12)
				)
				
				greeted = true
				
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
			
		var initial_x = velocity.x
		var old_position = position
		.move(delta)
		if initial_x != 0 and position == old_position:
			$AnimatedSprite.flip_h = not $AnimatedSprite.flip_h
			
			
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
	if active and animation() != "Die":
		$AnimatedSprite.frame = 0
		play(["Idle", "Idle", "Idle" if animation() == "Walk" else "Walk"][randi()%3])
		$AnimatedSprite.flip_h = [true, false, $AnimatedSprite.flip_h][randi()%3]
	elif active:
		health = max_health
		$AnimatedSprite.frame = 0
		play("Idle")
		$AnimatedSprite.flip_h = true
		position = Vector2(656 - dimensions.x/2, 748 - dimensions.y/2)
		
		Base.get_node("CanvasLayer").get_node("DialogueQueue").push(
			"Beardo the Barkeep",
			[
				"Shift Change! Nothing to see here...",
				"Ever 'ad a dream where ye get murdered by someone ye've ne'er met, an' 'en they're in yer tavern?",
				"Belch. Braaaaaaaaap. Exsqueeeeze me, I'm feeling a little queasy, got any gold for meesy?"
			][randi()%3],
			$AnimatedSprite.frames.get_frame("Idle", 0),
			Rect2(28, 38, 12, 12)
		)


func save_data():
	return {
		"Object": "Barkeep",
		"x": position.x,
		"y": position.y,
		"health": health,
		"animation": animation(),
		"frame": $AnimatedSprite.frame,
		"flip": $AnimatedSprite.flip_h,
		"inventory": inventory
	}
