extends AnimatedSprite

signal right_arrow_pressed
signal left_arrow_pressed

var target = 0
var tick = 0
const TICKSPEED = 8
const DEFAULTFRAME = 3
const ENDFRAME = 6
var canFlipLeft = false
var canFlipRight = false
export (bool) var activateOnReady = false

func _ready():
	frame = 0
	if activateOnReady:
		visible = true
		target = DEFAULTFRAME


func _process(_delta):
	if target > frame and tick % TICKSPEED == 0:
		frame += 1
	elif frame == ENDFRAME and target == ENDFRAME and tick % TICKSPEED == 0:
		frame = DEFAULTFRAME
		target = DEFAULTFRAME
	if target < frame and tick % TICKSPEED == 0:
		frame -= 1
	
	get_node("LeftPage").visible = frame in [3, 4, 5]
	get_node("RightPage").visible = frame in [2, 3, 6]
	
	$RightArrow.visible = canFlipRight and frame == DEFAULTFRAME
	$LeftArrow.visible = canFlipLeft and frame == DEFAULTFRAME
		

	tick += 1


func _on_RightArrow_pressed():
	if canFlipRight and frame == target:
		tick = 1
		frame = DEFAULTFRAME + 1
		target = ENDFRAME
		emit_signal("right_arrow_pressed")


func _on_LeftArrow_pressed():
	if canFlipLeft and frame == target:
		tick = 1
		frame = ENDFRAME
		target = DEFAULTFRAME
		emit_signal("left_arrow_pressed")
