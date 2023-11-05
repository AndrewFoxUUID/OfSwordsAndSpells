extends Area2D

signal pressed

var item
var override_quantity

func _ready():
	pass
	
	
func _process(_delta):
	$Item.frame = Constants.ITEM_DATA[item]["frame"] if item != null else 0
	var quantity = override_quantity if override_quantity != null else Base.player.get_num(item)
	$Quantity.text = str(quantity) if item != null else ""
	
	if item != null:
		var data = Constants.ITEM_DATA[item]
		$Node2D/PopupPanel.rect_position = (get_viewport().get_mouse_position() - global_position) / 3 + Vector2(2, 2)
		var name_size = $Node2D/PopupPanel/Name.rect_size * $Node2D/PopupPanel/Name.rect_scale.x
		var attributes_size = $Node2D/PopupPanel/Attributes.rect_size * $Node2D/PopupPanel/Attributes.rect_scale.x
		$Node2D/PopupPanel.rect_size = Vector2(
			max(name_size.x, attributes_size.x) + 16,
			name_size.y + attributes_size.y - 4
		)
		$Node2D/PopupPanel/Name.text = item
		$Node2D/PopupPanel/Name.set("custom_colors/font_color", [Color8(77, 74, 78), Color8(0, 0, 0), Color8(140, 142, 171), Color8(209, 119, 58), Color8(126, 2, 31)][data["rarity"]])
		
		$Node2D/PopupPanel/Attributes.text = ""
		if "martial" in data and data["martial"] == true:
			$Node2D/PopupPanel/Attributes.text += "martial "
		if "magic" in data and data["magic"] == true:
			$Node2D/PopupPanel/Attributes.text += "magic "
		if "consumable" in data and data["consumable"] == true:
			$Node2D/PopupPanel/Attributes.text += "consumable "
		if $Node2D/PopupPanel/Attributes.text != "":
			$Node2D/PopupPanel/Attributes.text += "\n"
		
		if "style" in data:
			$Node2D/PopupPanel/Attributes.text += str(data["style"]) + "\n"
		if "life_gain" in data:
			$Node2D/PopupPanel/Attributes.text += "Click to restore " + str(data["life_gain"]) + " hit points\n"
		if "damage" in data:
			$Node2D/PopupPanel/Attributes.text += "Damage: " + str(data["damage"]) + "\n"
		if "armor" in data:
			$Node2D/PopupPanel/Attributes.text += "Armor: " + str(data["armor"]) + "\n"
		if "block_chance" in data:
			$Node2D/PopupPanel/Attributes.text += "Block Chance: " + str(data["block_chance"]) + "%\n"
		if "martial_damage_increase" in data:
			$Node2D/PopupPanel/Attributes.text += "Additional Martial Damage: " + str(data["martial_damage_increase"]) + "\n"
		if "block_chance_increase" in data:
			$Node2D/PopupPanel/Attributes.text += "Additional Block Chance: " + str(data["block_chance_increase"]) + "%\n"
		if "critical_chance_increase" in data:
			$Node2D/PopupPanel/Attributes.text += "Additional Critical Chance: " + str(data["critical_chance_increase"]) + "%\n"
		if "speed_increase" in data:
			$Node2D/PopupPanel/Attributes.text += "Additional Speed: " + str(data["speed_increase"]) + "\n"
			
		$Node2D.visible = $Base.frame == 12


func _on_Item_mouse_entered():
	$Base.playing = true


func _on_Item_mouse_exited():
	$Base.frame = 0
	$Base.playing = false


func _on_Item_input_event(_viewport, event, _shape_idx):
	if visible and event is InputEventMouseButton and not event.pressed and event.button_index == 1:
		emit_signal("pressed")
