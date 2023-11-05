extends Node2D

var lifetime = 500

func _process(_delta):
	if lifetime > 0:
		lifetime -= 1
		
	if lifetime > 473:
		position.y += 5
	elif lifetime < 27:
		position.y -= 5
