extends Sprite

var dimensions = Vector2(68, 54)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])


func save_data():
	return {
		"Object": "BackgroundShortHouse",
		"x": position.x,
		"y": position.y
	}
