extends Label

export (bool) var flat = false
export (bool) var dark = false
export (bool) var flash = false
export (bool) var isvisible = true # only for use with flash

var tick = 0

func _process(_delta):
	if flat:
		$Layer1.visible = false
		$Layer2.visible = false
		$Layer3.visible = false
		
		if text == "" and $Layer1.text != "":
			text = $Layer1.text
			
		set("custom_colors/font_color", Color8(62, 67, 87) if dark else Color8(238, 244, 255))
	else:
		$Layer1.visible = true
		$Layer2.visible = true
		$Layer3.visible = true
		
		$Layer1.text = text
		$Layer2.text = text
		$Layer3.text = text
	
		$Layer1.align = align
		$Layer2.align = align
		$Layer3.align = align
		
		$Layer1.autowrap = autowrap
		$Layer2.autowrap = autowrap
		$Layer3.autowrap = autowrap
		
		$Layer1.rect_size.x = rect_size.x
		$Layer2.rect_size.x = rect_size.x
		$Layer3.rect_size.x = rect_size.x
		
		set("custom_colors/font_color", Color8(62, 67, 87) if dark else Color8(238, 244, 255))
		$Layer1.set("custom_colors/font_color", Color8(62, 67, 87) if dark else Color8(238, 244, 255))
		$Layer2.set("custom_colors/font_color", Color8(35, 38, 47) if dark else Color8(180, 185, 207))
		$Layer3.set("custom_colors/font_color", Color8(169, 169, 169) if dark else Color8(52, 57, 64))
	
	if flash:
		if isvisible:
			visible = tick % 125 < 100
			tick += 1
			if tick >= 125:
				tick = 0
		else:
			visible = false
