extends Node2D

var dimensions = Vector2(32, 48)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])


func save_data():
	return {
		"Object": "MeadowTree",
		"x": position.x,
		"y": position.y
	}
