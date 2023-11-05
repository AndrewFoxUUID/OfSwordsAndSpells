extends Entity

var velocity = Vector2.ZERO
var item

func _ready():
	pass
	
	
func _physics_process(delta):
	if $Area2D.overlaps_body(Base.player):
		Base.player.pickup_item(item)
		queue_free()
		
	$AnimatedSprite.frame = Constants.ITEM_DATA[item]["frame"] if item in Constants.ITEM_DATA else 0
		
	velocity.y += gravity * delta
	velocity = move_and_slide(velocity, Vector2.UP, true)
	position = position.snapped(Vector2.ONE)
