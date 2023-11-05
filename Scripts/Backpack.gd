extends AnimatedSprite

signal up_arrow_pressed
signal down_arrow_pressed

var target = 0
var tick = 0
const TICKSPEED = 5
const DEFAULTFRAME = 6
const ENDFRAME = 6
var canFlipUp = false
var canFlipDown = false

func _ready():
	frame = 0
	target = 0
	
	
func _process(_delta):
	if target > frame and tick % TICKSPEED == 0:
		frame += 1
	elif frame == ENDFRAME and target == ENDFRAME and tick % TICKSPEED == 0:
		frame = DEFAULTFRAME
		target = DEFAULTFRAME
	if target < frame and tick % TICKSPEED == 0:
		frame -= 1
	
	get_node("Contents").visible = frame == DEFAULTFRAME
	
	$UpArrow.visible = canFlipUp and frame == DEFAULTFRAME
	$DownArrow.visible = canFlipDown and frame == DEFAULTFRAME
	
	tick += 1


func _on_Up_Arrow_pressed():
	if canFlipUp:
		emit_signal("up_arrow_pressed")


func _on_Down_Arrow_pressed():
	if canFlipDown:
		emit_signal("down_arrow_pressed")
