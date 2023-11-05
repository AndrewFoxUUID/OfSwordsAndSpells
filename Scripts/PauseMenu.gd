extends Node2D

var unpausing = false

func _ready():
	pass
	
	
func _process(_delta):
	visible = get_tree().paused
	if not visible:
		$MenuBook.frame = 0
	elif unpausing:
		$MenuBook.target = 0
		if $MenuBook.frame == 0:
			unpausing = false
			get_tree().paused = false
	else:
		$MenuBook.target = $MenuBook.DEFAULTFRAME
		
	if Base.player != null: Base.player.settings["zoom"] = $MenuBook/RightPage/Zoom.value
	$MenuBook/RightPage/EditPlayer.visible = Base.player != null


func _unhandled_input(event):
	if event.is_action_pressed("ui_cancel"):
		if get_tree().paused:
			unpausing = true
		else:
			get_tree().paused = true


func _on_EditPlayer_pressed():
	if visible:
		var instance = load("res://Scenes/UIElements/EditPlayer.tscn").instance()
		add_child(instance)
