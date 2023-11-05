extends AnimatedSprite

var tick = 0
var radius = 1
const MAXRADIUS = 4
var thickness = 0
const MAXTHICKNESS = 2
var tickspeed = 40
var mod = 0
var increasing = true
var color = Color8(255, 255, 255, 255)

func _process(_delta):
	if frame == 5:
		frame = 3
	if frame == 6 or frame == 7:
		frame = 4
	if tick%int(tickspeed) == mod and randi()%2 == 0:
		if increasing:
			frame += 1
			if frame >= radius:
				frame = radius
				increasing = false
		else:
			frame -= 1
			if frame <= 0:
				frame = 0
				increasing = true
	if thickness >= 1 and frame == 3:
		frame = 5
	if thickness == 1 and frame == 4:
		frame = 6
	if thickness > 1 and frame == 4:
		frame = 7
	tick += 1
	
	set("shader_param/color", color)
	
func load_data(data):
	position = Vector2(str2var(data["position"]))
	radius = data["radius"]
	thickness = data["thickness"]
	tickspeed = data["tickspeed"]
	mod = data["mod"]
	color = data["color"]
	
func save_data():
	return {
		"position": var2str(position),
		"radius": radius,
		"thickness": thickness,
		"tickspeed": tickspeed,
		"mod": mod,
		"color": color
	}
