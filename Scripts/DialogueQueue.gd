extends Node2D

onready var Dialogue = preload("res://Scenes/UIElements/Dialogue.tscn")

func push(source, text, image, rect):
	var dialogue = Dialogue.instance()
	dialogue.get_node("Name").text = source
	dialogue.get_node("Label").text = text
	dialogue.get_node("Speaker").draw_img = image
	dialogue.get_node("Speaker").draw_rect = rect
	add_child(dialogue)
	Base.player.dialogue_history.append([source, text, image, rect])
	
	
func _process(_delta):
	if Input.is_action_just_pressed("close_dialogue"):
		if len(get_children()) > 0:
			get_children()[len(get_children())-1].lifetime = 27
			
	if len(get_children()) > 0:
		if get_children()[len(get_children())-1].lifetime == 0:
			remove_child(get_children()[len(get_children())-1])
