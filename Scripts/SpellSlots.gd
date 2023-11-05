extends Node2D


func _ready():
	pass


func _process(_delta):
	$Label.visible = Base.player.get_level() >= 1
	
	var i = 0
	for slot in $ColorRect6.get_children():
		if Base.player.spell_slots[i] != null:
			var data = Constants.SPELL_DATA[Base.player.spell_slots[i]]
			slot.visible = true
			slot.get_node("AnimatedSprite").frame = data["icon"]
			slot.get_node("AnimatedSprite").material.set("shader_param/greyscale", not Base.player.can_cast(Base.player.spell_slots[i]))
			slot.get_node("Name").text = Base.player.spell_slots[i]
		else:
			slot.visible = false
		i += 1
	
	$KnownSpells.visible = $KnownSpells.frame != 0
	if Input.is_action_just_pressed("open_knownspells"):
		if $KnownSpells.frame == $KnownSpells.DEFAULTFRAME:
			$KnownSpells.target = 0
			Base.popup_active = false
		elif $KnownSpells.frame == 0 and not Base.popup_active:
			$KnownSpells.target = $KnownSpells.DEFAULTFRAME
			Base.popup_active = true
