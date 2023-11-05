extends Label

var x_vel
var initial_y_vel
var y_vel

func _ready():
	x_vel = (randi()%41 - 20)/10
	initial_y_vel = -(randi()%21)/10
	y_vel = initial_y_vel
	
	
func _process(_delta):
	rect_position += Vector2(x_vel, y_vel)
	y_vel += 0.1
	if y_vel >= -initial_y_vel:
		queue_free()
