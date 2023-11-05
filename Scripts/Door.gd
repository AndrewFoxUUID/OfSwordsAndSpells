extends Area2D

var dimensions = Vector2(71, 148)*scale.x

func generate(data):
	position = Vector2(data["x"], data["y"])


func _process(_delta):
	if overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8


func save_data():
	return {
		"Object": "Door",
		"x": position.x,
		"y": position.y,
	}
