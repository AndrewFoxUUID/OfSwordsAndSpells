extends Node2D

onready var droppeditem = preload("res://Scenes/UIElements/DroppedItem.tscn")

var dimensions = Vector2(32, 18)*scale.x

func _ready():
	var rand = randi()%1000
	if rand == 999:
		$AnimatedSprite.frame = 5
	elif rand > 990:
		$AnimatedSprite.frame = 4
	elif rand > 950:
		$AnimatedSprite.frame = 3
	elif rand > 750:
		$AnimatedSprite.frame = 2
	else:
		$AnimatedSprite.frame = 1


func generate(data):
	position = Vector2(data["x"], data["y"])
	$AnimatedSprite.frame = data["frame"]


func _process(_delta):
	if $Area2D.overlaps_body(Base.player) and Input.is_action_just_pressed("player_interact"):
		for i in [1,3,7,12,18,30][$AnimatedSprite.frame]:
			var coin = droppeditem.instance()
			coin.item = "Coins"
			coin.position = Vector2(position.x+dimensions.x/2, position.y)
			Base.get_entities().add_child(coin)
		queue_free()
	
	if $Area2D.overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8


func save_data():
	return {
		"Object": "Coins",
		"x": position.x,
		"y": position.y,
		"frame": $AnimatedSprite.frame
	}
