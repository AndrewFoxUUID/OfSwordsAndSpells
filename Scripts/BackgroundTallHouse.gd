extends Sprite

var dimensions = Vector2(44, 61)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])


func save_data():
	return {
		"Object": "BackgroundTallHouse",
		"x": position.x,
		"y": position.y
	}
