extends StaticBody2D

const MERCHANT_TYPES = [preload("res://Scenes/Entities/ArmorDealer.tscn"), preload("res://Scenes/Entities/WeaponsDealer.tscn")]

var dimensions = Vector2(72, 50)*scale.x
var index

func _ready():
	$AnimatedSprite.frame = randi()%6


func generate(data):
	position = Vector2(data["x"], data["y"])
	$AnimatedSprite.frame = data["frame"]


func save_data():
	return {
		"Object": "MarketStall",
		"x": position.x,
		"y": position.y,
		"frame": $AnimatedSprite.frame
	}
