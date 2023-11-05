extends Sprite

var draw_img
var draw_rect = Rect2(0, 0, 12, 12)

func _ready():
	pass
	
	
func _draw():
	draw_set_transform(Vector2(0, 0), 0, Vector2(-1, 1))
	draw_texture_rect_region(draw_img, Rect2(-6, -6, 12, 12), draw_rect)
