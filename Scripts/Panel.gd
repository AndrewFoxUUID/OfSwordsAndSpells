extends Panel

func _process(_delta):
	$BorderLeft.rect_size.y = rect_size.y
	$BorderTop.rect_size.x = rect_size.x
	$BorderRight.rect_position.x = rect_size.x
	$BorderRight.rect_size.y = rect_size.y
	$BorderBottom.rect_position.y = rect_size.y
	$BorderBottom.rect_size.x = rect_size.x
