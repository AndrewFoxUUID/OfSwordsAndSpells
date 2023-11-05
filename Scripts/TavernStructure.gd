extends StaticBody2D

var dimensions = Vector2(80, 64)*scale.x
var index

func generate(data):
	position = Vector2(data["x"], data["y"])
	index = data["index"]


func _process(_delta):
	if $Area2D.overlaps_body(Base.player) and Input.is_action_just_pressed("player_interact"):
		Base.get_entities().remove_child(Base.player)
		Base.building_index = index
		Base.change_scene("res://Scenes/Tavern.tscn")
		
	if $Area2D.overlaps_body(Base.player):
		$TextPopup.playing = true
	else:
		$TextPopup.playing = false
		$TextPopup.frame = 0
	$Label.visible = $TextPopup.frame == 8
	
	
func save_data():
	return {
		"Object": "Tavern",
		"x": position.x,
		"y": position.y,
		"index": index
	}
