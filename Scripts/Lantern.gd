extends Node2D

onready var droppeditem = preload("res://Scenes/UIElements/DroppedItem.tscn")

var dimensions = Vector2(16, 16)*scale.x


func _ready():
	pass


func generate(data):
	position = Vector2(data["x"], data["y"])
	$AnimatedSprite.frame = data["frame"]


func _process(_delta):
	if $Area2D.overlaps_body(Base.player) and Input.is_action_just_pressed("player_interact"):
		$AnimatedSprite.frame = 1
		var item = droppeditem.instance()
		item.item = "Candle"
		item.position = position + Vector2(8.5, 10)*scale.x
		Base.get_entities().add_child(item)
	
	if $AnimatedSprite.frame == 0 and $Area2D.overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8
	
	
func save_data():
	return {
		"Object": "Lantern",
		"x": position.x,
		"y": position.y,
		"frame": $AnimatedSprite.frame
	}
