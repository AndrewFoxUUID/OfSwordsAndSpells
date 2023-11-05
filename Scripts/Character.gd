extends Entity

class_name Character

var active

var max_health
var health
var speed
var velocity

var grounded = false

func _ready() -> void:
	refresh()
	

func refresh() -> void:
	visible = true
	velocity = Vector2.ZERO
	
	
func animation() -> String:
	return "Idle"
	
	
func play(animation: String) -> void:
	pass
	
	
func hurt(amount:int, type='') -> bool:
	if amount > 0:
		amount -= getArmorClass()
		if amount < 0:
			amount = 0
			
		if not (animation() in ["Hurt", "Die"]):
			health -= amount
			if health <= 0:
				health = 0
				play("Die")
			else:
				play("Hurt")
			return true
		else:
			return false
	else:
		health -= amount
		return true
		
		
func getArmorClass():
	return 0
	
	
func move(delta) -> void:
	var zoom = 1.0/float(Base.player.get_node("Camera2D").zoom.x) if Base.player != null else 1.0
	velocity.y += gravity * delta
	velocity *= zoom
	var initial_x = velocity.x
	velocity = move_and_slide(velocity, Vector2.UP, true, 6)
	grounded = velocity.y == 0
	if initial_x != 0 and velocity.x == 0:
		move_and_slide(Vector2(0, -4/delta*zoom), Vector2.UP, true)
		move_and_slide(Vector2(initial_x*0.5, 0), Vector2.UP, true)
		move_and_slide(Vector2(0, 4.1/delta*zoom), Vector2.UP, true)
	position = position.snapped(Vector2.ONE)


func save() -> Dictionary:
	return {}
