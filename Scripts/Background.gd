extends ColorRect

onready var Star = preload("res://Scenes/UIElements/Star.tscn")

func _ready():
	for i in range(0, 1000, 10):
		for j in range(0, 1000, 10):
			if randi()%50 == 0:
				var starinst = Star.instance()
				starinst.position = Vector2(i + 2 + randi()%6, j + 2 + randi()%6)
				starinst.radius = 1 + randi()%starinst.MAXRADIUS
				starinst.thickness = randi()%(starinst.MAXTHICKNESS+1)
				starinst.tickspeed = (10 + randi()%4) * (starinst.MAXRADIUS - starinst.radius + 1)
				starinst.mod = randi()%starinst.tickspeed
				starinst.set("shader_param/color", Color8(255, 255, 255, 150))
				add_child(starinst)
