extends Node2D

signal closed

var tab_names = ["Hair", "Eyes", "Skin", "Shirt", "Pants", "Shoes"]
var color_names = ["hair", "eye", "skin", "shirt", "pants", "shoe"]
var create_player = false
var old_playername
var old_hair_style
var old_colors

func _ready():
	create_player = Base.player == null
	
	if create_player:
		Base.player = load("res://Scenes/Player.tscn").instance()
	
	old_playername = Base.player.playername
	old_hair_style = Base.player.hair_style
	old_colors = Base.player.colors
	$MenuBook/LeftPage/NameInput.text = Base.player.playername
	
	for i in 6:
		$MenuBook/RightPage/TabContainer.get_node(tab_names[i]).get_node("ColorPicker").get_child(3).hide()
		$MenuBook/RightPage/TabContainer.get_node(tab_names[i]).get_node("ColorPicker").get_child(4).hide()
		$MenuBook/RightPage/TabContainer.get_node(tab_names[i]).get_node("ColorPicker").rect_size.y = 300
		$MenuBook/RightPage/TabContainer.get_node(tab_names[i]).get_node("ColorPicker").rect_position = Vector2(2, 2)
		$MenuBook/RightPage/TabContainer.get_node(tab_names[i]).get_node("ColorPicker").color = Base.player.colors[color_names[i]]
	$MenuBook/RightPage/TabContainer/Hair/HairStyle.selected = Base.player.hair_style
	$MenuBook/RightPage/TabContainer/Hair/HairStyle.get_popup() # need to elevate it


func get_tab():
	return $MenuBook/RightPage/TabContainer.current_tab


func _process(_delta):
	Base.player.construct_skin()
	$MenuBook/LeftPage/PlayerProxy.set_player(Base.player, true)
	
	if create_player: Base.player.savename = $MenuBook/LeftPage/NameInput.text
	Base.player.playername = $MenuBook/LeftPage/NameInput.text
	
	var color = $MenuBook/RightPage/TabContainer.get_node(tab_names[get_tab()]).get_node("ColorPicker").color
	var index = color_names[get_tab()]
	if Base.player.colors[index] != color:
		Base.player.colors[index] = color
		if "dark_" + index in Base.player.colors:
			Base.player.colors["dark_" + index] = Color8(max(0, color.r8 - 20), max(0, color.g8 - 20), max(0, color.b8 - 20))


func _unhandled_input(event):
	if event.is_action_pressed("ui_cancel"):
		Base.player.playername = old_playername
		Base.player.hair_style = old_hair_style
		Base.player.colors = old_colors
		emit_signal("closed")
		queue_free()
	elif event.is_action_pressed("ui_accept"):
		_on_Submit_Button_pressed()


func _on_Submit_Button_pressed():
	if Base.player.is_valid():
		Base.player.save()
		emit_signal("closed")
		queue_free()


func _on_HairStyle_item_selected(index):
	Base.player.hair_style = index
