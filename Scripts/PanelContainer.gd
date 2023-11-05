extends ColorRect


func _process(_delta):
	$ColorRect1.rect_size = Vector2(rect_size.x-2, rect_size.y-1)
	$ColorRect2.rect_size = Vector2(rect_size.x-4, rect_size.y-2)
	$ColorRect3.rect_size = Vector2(rect_size.x-6, rect_size.y-3)
	$ColorRect4.rect_size = Vector2(rect_size.x-8, rect_size.y-4)
	$ColorRect5.rect_size = Vector2(rect_size.x-10, rect_size.y-5)
	$ColorRect6.rect_size = Vector2(rect_size.x+2, 6)
	$ColorRect7.rect_size = Vector2(rect_size.x, 1)
	$ColorRect8.rect_size = Vector2(rect_size.x, 2)
	$ColorRect9.rect_size = Vector2(rect_size.x, 1)
