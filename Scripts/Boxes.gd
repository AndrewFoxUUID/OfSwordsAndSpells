extends StaticBody2D

var dimensions = Vector2(32, 32)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])

func save_data():
	return {
		"Object": "Boxes",
		"x": position.x,
		"y": position.y
	}
