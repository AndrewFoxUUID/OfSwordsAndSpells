extends CanvasLayer

onready var Heart = preload("res://Scenes/UIElements/Heart.tscn")
onready var EnergyPoint = preload("res://Scenes/UIElements/EnergyPoint.tscn")

var leaving = false

func _ready():
	pass
	
	
func _process(_delta):
	while len($Hearts.get_children()) > (Base.player.max_health+3)/4:
		$Hearts.remove_child($Hearts.get_children()[-1])
	while len($Hearts.get_children()) < (Base.player.max_health+3)/4:
		var heart = Heart.instance()
		heart.position = Vector2(746 - 24*len($Hearts.get_children()), 18)
		$Hearts.add_child(heart)
		
	var i = 0
	for heart in $Hearts.get_children():
		heart.frame = max(min(Base.player.max_health - i, 4), 0)
		heart.get_node("Heart").frame = max(min(Base.player.health - i, 4), 0)
		i += 4
	
	var energy_holders = {
		"r": $RadiantEnergy,
		"s": $ShadowEnergy,
		"l": $LifeEnergy,
		"d": $DeathEnergy,
		"f": $ForgeEnergy,
		"t": $TrueEnergy,
		"n": $NullEnergy
	}
	var energy_colors = {
		"r": Color8(126, 2, 31),
		"s": Color8(14, 14, 16),
		"l": Color8(66, 3, 97),
		"d": Color8(219, 187, 61),
		"f": Color8(209, 119, 58),
		"t": Color8(38, 68, 144),
		"n": Color8(107, 104, 93)
	}
	i = 0
	for energy_type in Base.player.max_energy:
		var num_children = len(energy_holders[energy_type].get_children())
		while num_children > Base.player.max_energy[energy_type]:
			energy_holders[energy_type].remove_child(energy_holders[energy_type].get_children()[-1])
			num_children -= 1
		while num_children < Base.player.max_energy[energy_type]:
			var energypoint = EnergyPoint.instance()
			energypoint.position = Vector2(792 - 20*num_children, 41 + 20*i)
			energy_holders[energy_type].add_child(energypoint)
			num_children += 1
			energypoint.material.set("shader_param/energy_color", energy_colors[energy_type])
			energypoint.material.set("shader_param/offset", float(randi()))
		if num_children == 0:
			continue
			
		var j = 0
		for point in energy_holders[energy_type].get_children():
			point.material.set("shader_param/do_shine", point.frame == 11)
			if not point.playing:
				point.frame = 11 if j < int(Base.player.energy[energy_type]) else 0
			if Base.player.energy[energy_type] == j+0.5:
				point.playing = true
				if point.frame == 11:
					point.playing = false
					Base.player.energy[energy_type] += 0.5
			j += 1
			
		i += 1
	
	if leaving:
		if $PlaneSpin.position.y < 280:
			$PlaneSpin.position.y += 2
			if $PlaneSpin.position.y >= 240:
				$PlaneSpin.open()
		elif $PlaneSpin.opening == 6 and $PlaneSpin.scale.x < 150:
			$PlaneSpin.position.x += 0.08
			$PlaneSpin.scale *= 1.01
		elif $PlaneSpin.scale.x >= 150:
			Base.tile = null
			Base.building = null
			Base.building_index = null
			Base.get_entities().remove_child(Base.player)
			Base.change_scene("res://Scenes/World.tscn")
			
	if Base.boss != null:
		$BossHealthBar.visible = true
		$BossHealthBar/ColorRect.rect_size.x = 101 * (float(Base.boss.health) / float(Base.boss.max_health))
	else:
		$BossHealthBar.visible = false
		
	$SoulEnergyBar/LevelLabel.text = "Level " + str(Base.player.get_level())
	$SoulEnergyBar/Label.text = "¤ " + str(Base.player.soul_energy) + "/" + str(pow(2, Base.player.get_level()+1))
	$SoulEnergyBar/ColorRect3.rect_size.x = 896 * (float(Base.player.soul_energy) / float(pow(2, Base.player.get_level()+1)))


func _on_PlaneSpin_pressed():
	if Base.player.get_level() > 0:
		leaving = true
