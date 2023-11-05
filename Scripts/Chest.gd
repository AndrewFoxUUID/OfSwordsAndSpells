extends Node2D

onready var droppeditem = preload("res://Scenes/UIElements/DroppedItem.tscn")

var dimensions = Vector2(24, 24)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])
	$AnimatedSprite.frame = data["frame"]


func _process(_delta):
	if $Area2D.overlaps_body(Base.player) and $AnimatedSprite.frame == 0 and Input.is_action_just_pressed("player_interact"):
		$AnimatedSprite.playing = true
		var item = droppeditem.instance()
		item.item = Constants.CHEST_LOOT_TABLE[randi()%len(Constants.CHEST_LOOT_TABLE)]
		item.position = position + Vector2(12, 14)*scale.x
		Base.get_entities().add_child(item)
		for i in [0,1,1,1,1,2,2,2,3,3,4,5][randi()%12]:
			var coin = droppeditem.instance()
			coin.item = "Coins"
			coin.position = position + Vector2(12, 14)*scale.x
			Base.get_entities().add_child(coin)
	
	if $AnimatedSprite.frame == 0 and $Area2D.overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8


func save_data():
	return {
		"Object": "Chest",
		"x": position.x,
		"y": position.y,
		"frame": $AnimatedSprite.frame
	}
