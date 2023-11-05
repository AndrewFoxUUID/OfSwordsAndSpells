extends Character

onready var droppeditem = preload("res://Scenes/UIElements/DroppedItem.tscn")

var dimensions = Vector2(64, 64)
var shaken = false
var shake_time = 0

func _ready():
	._ready()
	health = 24
	max_health = 24
	speed = 200.0
	
	dimensions *= $AnimatedSprite.scale.x
	$AnimatedSprite.playing = true
	
	Base.boss = self
	

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
	if animation() != "Roll" or type != '':
		var alive = health > 0
		var result = .hurt(amount, type)
		if result:
			shake_time = 20
		if alive and health <= 0:
			var item = droppeditem.instance()
			item.item = "Armadillo Charm"
			item.position = position
			Base.get_entities().add_child(item)
			Base.boss = null
			Base.player.gain_soul_energy(2)
		return result
	return false
	
	
func getArmorClass():
	return 1
	
	
func _physics_process(delta):
	if active:
		if not shaken and is_on_floor():
			shake_time = 50
			shaken = true
			
		if shake_time > 0:
			Base.player.shake_intensity = 4
			shake_time -= 1
		elif health > 0:
			Base.player.shake_intensity = 1
		
		velocity.x = 0
		
		if animation() != "Die":
			if animation() == "Run":
				velocity.x += -speed if $AnimatedSprite.flip_h else speed
			elif animation() == "Roll":
				velocity.x += -speed*2 if $AnimatedSprite.flip_h else speed*2
				
				if $Area2D.overlaps_body(Base.player):
					Base.player.hurt(1, '')
		
		.move(delta)


func _on_AnimatedSprite_animation_finished():
	if animation() != "Die":
		$AnimatedSprite.frame = 0
		if animation() == "Rollup":
			play("Roll")
		elif animation() == "Roll":
			play(["Idle", "Run", "Roll"][randi()%3])
		elif randi()%20 >= health:
			play("Rollup")
		else:
			play(["Idle", "Run", "Run" if animation() == "Run" else "Idle"][randi()%3])
			
		if animation() != "Roll":
			$AnimatedSprite.flip_h = position.x > Base.player.position.x
		
		
func save_data():
	return {
		"Object": "Armadillon",
		"x": position.x,
		"y": position.y,
		"health": health,
		"animation": $AnimatedSprite.animation,
		"frame": $AnimatedSprite.frame,
		"flip": $AnimatedSprite.flip_h
	}
