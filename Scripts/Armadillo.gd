extends Character

var dimensions = Vector2(32, 32)

func _ready():
	._ready()
	max_health = 2
	health = 2
	speed = 100.0
	
	dimensions.x *= $AnimatedSprite.scale.x
	dimensions.y *= $AnimatedSprite.scale.y
	

func animation():
	return $AnimatedSprite.animation
	
	
func play(animation):
	$AnimatedSprite.play(animation)
	
	
func generate(data):
	position = Vector2(data["x"], data["y"])
	health = data["health"]
	play(data["animation"])
	$AnimatedSprite.frame = data["frame"]
	$AnimatedSprite.flip_h = data["flip"]
	active = true
	
	
func hurt(amount: int, type=''):
	var success = false
	if animation() != "Rollup" or type == 'd':
		var living = health > 0
		success = .hurt(amount, type)
		if living and health <= 0 and not Base.boss and not Base.tile.armadillonSpawned:
			var boss = load("res://Scenes/Entities/Armadillon.tscn").instance()
			boss.active = true
			boss.position = Vector2(position.x, 0)
			Base.get_entities().add_child(boss)
			Base.tile.armadillonSpawned = true
	return success


func _physics_process(delta):
	if active:
		velocity.x = 0
		
		if animation() != "Die":
			if $Area2D.overlaps_body(Base.player):
				play("Rollup")
			elif animation() == "Run":
				velocity.x += -speed if $AnimatedSprite.flip_h else speed
		
		.move(delta)


func _on_AnimatedSprite_animation_finished():
	if active and animation() != "Die":
		if animation() == "Rollup" and randi()%3 != 0:
			$AnimatedSprite.frame -= 1
		else:
			$AnimatedSprite.frame = 0
			play(["Idle", "Run", "Run" if animation() == "Run" else "Idle"][randi()%3])
			$AnimatedSprite.flip_h = [true, false, $AnimatedSprite.flip_h][randi()%3]
		
		
func save_data():
	return {
		"Object": "Armadillo",
		"x": position.x,
		"y": position.y,
		"health": health,
		"animation": animation(),
		"frame": $AnimatedSprite.frame,
		"flip": $AnimatedSprite.flip_h
	}
