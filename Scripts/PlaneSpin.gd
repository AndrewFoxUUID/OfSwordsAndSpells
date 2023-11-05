extends Node2D

signal pressed

export (int) var opening = -1
var closing = false
var spinframe = 0
var tick = 0
export (int) var speed = 4

# spin when opening = 6

func _ready():
	set_planet()
	

func set_planet():
	var centerPlane = 0
	centerPlane = {
		"Sguila": 0,
		"Arthili": 1,
		"Karathis": 2,
		"Countermand": 3,
		"Hellithane": 4,
		"Zwi": 5,
		"Vaeldor": 6
	}[Base.world_name]
	
	$Planet1.frame = centerPlane
	$Planet2.frame = centerPlane + 1 if centerPlane < 6 else -6
	$Planet3.frame = centerPlane + 2 if centerPlane < 5 else -5
	$Planet4.frame = centerPlane + 3 if centerPlane < 4 else -4
	$Planet5.frame = centerPlane + 4 if centerPlane < 3 else -3
	$Planet6.frame = centerPlane + 5 if centerPlane < 2 else -2
	$Planet7.frame = centerPlane + 6 if centerPlane < 1 else -1
	
	
func _process(_delta):
	$Planet1.position = Vector2(0, 0)
	if opening == -1:
		$Planet2.position = Vector2(0, 0)
		$Planet3.position = Vector2(0, 0)
		$Planet4.position = Vector2(0, 0)
		$Planet5.position = Vector2(0, 0)
		$Planet6.position = Vector2(0, 0)
		$Planet7.position = Vector2(0, 0)
	else:
		if spinframe%7 == 0 and tick%speed == 0:
			var temp = $Planet7.frame
			$Planet7.frame = $Planet6.frame
			$Planet6.frame = $Planet5.frame
			$Planet5.frame = $Planet4.frame
			$Planet4.frame = $Planet3.frame
			$Planet3.frame = $Planet2.frame
			$Planet2.frame = temp
		
		$Planet2.position = Vector2(cos(spinframe%7 * PI/21)*opening*2, sin(spinframe%7 * PI/21)*opening*2)
		$Planet3.position = Vector2(cos(spinframe%7 * PI/21 + PI/3)*opening*2, sin(spinframe%7 * PI/21 + PI/3)*opening*2)
		$Planet4.position = Vector2(cos(spinframe%7 * PI/21 + 2*PI/3)*opening*2, sin(spinframe%7 * PI/21 + 2*PI/3)*opening*2)
		$Planet5.position = Vector2(cos(spinframe%7 * PI/21 + 3*PI/3)*opening*2, sin(spinframe%7 * PI/21 + 3*PI/3)*opening*2)
		$Planet6.position = Vector2(cos(spinframe%7 * PI/21 + 4*PI/3)*opening*2, sin(spinframe%7 * PI/21 + 4*PI/3)*opening*2)
		$Planet7.position = Vector2(cos(spinframe%7 * PI/21 + 5*PI/3)*opening*2, sin(spinframe%7 * PI/21 + 5*PI/3)*opening*2)
		
	tick += 1
	if tick >= 1000:
		tick = 0
	if tick % speed == 0:
		spinframe += 1
	if not closing and opening > -1 and opening < 6 and tick % speed == 0:
		opening += 1
	if closing and opening > -1 and tick % speed == 0:
		opening -= 1
		if opening == -1:
			closing = false
			spinframe = -1


func open():
	closing = false
	if opening == -1:
		opening = 0
		
		
func close():
	closing = true


func _on_Area2D_input_event(_viewport, event, _shape_idx):
	if event is InputEventMouseButton and event.pressed and event.button_index == 1:
		emit_signal("pressed")
