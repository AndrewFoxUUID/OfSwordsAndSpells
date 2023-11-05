extends StaticBody2D

var dimensions = Vector2(24, 8)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])


func save_data():
	return {
		"Object": "Table",
		"x": position.x,
		"y": position.y
	}
