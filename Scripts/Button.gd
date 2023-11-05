extends Button

var focused = false

func _ready():
	for child in get_children():
		child.visible = true


func _process(_delta):
	if icon != null:
		$Icon.texture = icon
		$Text.rect_position.x = icon.get_width()
		icon = null
		
	$Icon.position.y = 2 if focused else 1
	
	if text != "":
		$Text.text = text
		text = ""
		
	$Text.rect_size.x = rect_size.x - ($Icon.texture.get_width() if $Icon.texture != null else 0)
	$Text.rect_position.y = 2 if focused else 1
	
	$BorderLeft.rect_size.y = rect_size.y + (0 if focused else 1)
	$BorderLeft.rect_position.y = 2 if focused else 1
	$BorderTop.rect_size.x = rect_size.x - 2
	$BorderTop.rect_position.y = 0 if focused else -1
	$BorderRight.rect_size.y = rect_size.y + (0 if focused else 1)
	$BorderRight.rect_position.x = rect_size.x
	$BorderRight.rect_position.y = 2 if focused else 1
	$BorderBottom.rect_size.x = rect_size.x - 2
	$BorderBottom.rect_position.y = rect_size.y + 3
	
	$Shadow.rect_size.x = rect_size.x
	$Shadow.rect_size.y = 1 if focused else 2
	$Shadow.rect_position.y = rect_size.y + (1 if focused else 0)
	$ShadowBottom.rect_size.x = rect_size.x - 2
	$ShadowBottom.rect_position.y = rect_size.y + 2
	
	$Padding.rect_size.x = rect_size.x
	$Padding.rect_size.y = rect_size.y
	$Padding.rect_position.y = 1 if focused else 0
	$PaddingBottom.rect_size.x = rect_size.x - 2
	$PaddingBottom.rect_position.y = rect_size.y + (1 if focused else 0)
	
	$CornerTopLeft.rect_position.y = 1 if focused else 0
	$CornerTopRight.rect_position.x = rect_size.x - 1
	$CornerTopRight.rect_position.y = 1 if focused else 0
	$CornerBottomLeft.rect_position.y = rect_size.y + 2
	$CornerBottomRight.rect_position.x = rect_size.x - 1
	$CornerBottomRight.rect_position.y = rect_size.y + 2
	
	if disabled:
		$BorderLeft.color = Color8(72, 70, 85)
		$BorderTop.color = Color8(72, 70, 85)
		$BorderRight.color = Color8(72, 70, 85)
		$BorderBottom.color = Color8(72, 70, 85)
		$Shadow.color = Color8(80, 85, 103)
		$ShadowBottom.color = Color8(80, 85, 103)
		$Padding.color = Color8(96, 104, 130)
		$PaddingBottom.color = Color8(96, 104, 130)
		$CornerTopLeft.color = Color8(72, 70, 85)
		$CornerTopRight.color = Color8(72, 70, 85)
		$CornerBottomLeft.color = Color8(72, 70, 85)
		$CornerBottomRight.color = Color8(72, 70, 85)
	else:
		$BorderLeft.color = Color8(28, 26, 45)
		$BorderTop.color = Color8(28, 26, 45)
		$BorderRight.color = Color8(28, 26, 45)
		$BorderBottom.color = Color8(28, 26, 45)
		$Shadow.color = Color8(38, 44, 68)
		$ShadowBottom.color = Color8(38, 44, 68)
		$Padding.color = Color8(58, 68, 101)
		$PaddingBottom.color = Color8(58, 68, 101)
		$CornerTopLeft.color = Color8(28, 26, 45)
		$CornerTopRight.color = Color8(28, 26, 45)
		$CornerBottomLeft.color = Color8(28, 26, 45)
		$CornerBottomRight.color = Color8(28, 26, 45)


func _on_Button_button_down():
	if not disabled:
		focused = true


func _on_Button_button_up():
	focused = false
