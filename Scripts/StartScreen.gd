extends Node2D

var entering = false
var leaving = false
var ticks = 0

func _ready():
	$Label.isvisible = false
	$LogoTop.position.x = -$LogoTop.texture.get_width() * $LogoTop.scale.x
	$LogoBottom.position.x = 1100
	entering = true
	ticks = 2


func _process(_delta):
	if entering:
		$LogoTop.position.x += ticks
		$LogoBottom.position.x -= ticks
		ticks += 2
		if $LogoTop.position.x >= 148:
			entering = false
	elif leaving:
		$LogoTop.position.x += ticks
		$LogoBottom.position.x -= ticks
		if $LogoTop.position.x >= 1000:
			Base.change_scene("res://Scenes/PlayerSelection.tscn")
	
	$Label.isvisible = not entering and not leaving


func _unhandled_key_input(event):
	if not entering and not leaving and event.is_pressed():
		leaving = true
