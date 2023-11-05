extends LineEdit

func _process(_delta):
	$BorderLeft.rect_size.y = rect_size.y
	$BorderTop.rect_size.x = rect_size.x - 2
	$BorderRight.rect_size.y = rect_size.y - 2
	$BorderRight.rect_position.x = rect_size.x
	$BorderBottom.rect_size.x = rect_size.x - 1
	$BorderBottom.rect_position.y = rect_size.y
	$CornerTopRight.rect_position.x = rect_size.x - 1
	$CornerBottomRight.rect_position.x = rect_size.x - 1
	$CornerBottomRight.rect_position.y = rect_size.y - 1
