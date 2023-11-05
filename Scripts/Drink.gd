extends Node2D

onready var droppeditem = preload("res://Scenes/UIElements/DroppedItem.tscn")

var dimensions = Vector2(12, 11)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])
	$AnimatedSprite.frame = data["frame"]


func _process(_delta):
	if $Area2D.overlaps_body(Base.player) and Input.is_action_just_pressed("player_interact"):
		var drink = droppeditem.instance()
		drink.item = ["Gilded Chalice", "Flask of Regeneration", "Flask of Cleansing", "Vial of Regeneration", "Vial of Cleansing"][$AnimatedSprite.frame]
		drink.position = Vector2(position.x+dimensions.x/2, position.y)
		Base.get_entities().add_child(drink)
		queue_free()
	
	if $Area2D.overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8


func save_data():
	return {
		"Object": "Drink",
		"x": position.x,
		"y": position.y,
		"frame": $AnimatedSprite.frame
	}
