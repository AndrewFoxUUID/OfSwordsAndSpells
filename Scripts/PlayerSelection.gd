extends Node2D

onready var Player = preload("res://Scenes/Player.tscn")
var leaving = 0
var dir
var leftIndex = 0
var players = []
var prev_len = 0

func _ready():
	dir = Directory.new()
	dir.open("user://Players/")


func _process(_delta):
	var num_players = 1
	dir.list_dir_begin(true, true)
	while dir.get_next() != "":
		if dir.current_is_dir():
			num_players += 1
	dir.list_dir_end()
	if num_players != prev_len:
		players = []
		for child in $PlayerQueue.get_children():
			$PlayerQueue.remove_child(child)
		dir.list_dir_begin(true, true)
		var file = dir.get_next()
		while file != "":
			if dir.current_is_dir():
				var player = Base.fetch_player(file)
				if player:
					players.append(player)
					$PlayerQueue.add_child(player)
			file = dir.get_next()
		dir.list_dir_end()
		players.append("Create Player")
		refresh()
		prev_len = num_players
	
	if leaving > 0:
		if leftIndex + leaving - 1 == players.size() - 1:
			$MenuBook.visible = false
			var edit_menu = load("res://Scenes/UIElements/EditPlayer.tscn").instance()
			edit_menu.connect("closed", self, "_on_EditPlayer_closed")
			add_child(edit_menu)
			leaving = 0
		else:
			$MenuBook.target = 0
			
		if $MenuBook.frame == 0:
			for child in $PlayerQueue.get_children():
				$PlayerQueue.remove_child(child)
			Base.player = players[leftIndex + leaving - 1]
			Base.change_scene("res://Scenes/WorldStage.tscn")
	
	
func refresh():
	$MenuBook/LeftPage/PlayerProxy.set_player(players[leftIndex])
	$MenuBook/LeftPage/Text.text = players[leftIndex] if players[leftIndex] is String else players[leftIndex].playername
	if leftIndex + 1 < players.size():
		$MenuBook/RightPage/PlayerProxy.set_player(players[leftIndex+1])
		$MenuBook/RightPage/Text.text = players[leftIndex + 1] if players[leftIndex + 1] is String else players[leftIndex + 1].playername
	else:
		$MenuBook/RightPage/PlayerProxy.set_player(null)
		$MenuBook/RightPage/Text.text = ""
		
	$MenuBook.canFlipLeft = leftIndex > 0
	$MenuBook.canFlipRight = leftIndex + 1 < players.size() - 1
	

func _on_LeftPage_pressed():
	if leftIndex < len(players):
		leaving = 1


func _on_RightPage_pressed():
	if leftIndex+1 < len(players):
		leaving = 2


func _on_Menu_Book_left_arrow_pressed():
	leftIndex -= 2
	refresh()


func _on_Menu_Book_right_arrow_pressed():
	leftIndex += 2
	refresh()


func _on_EditPlayer_closed():
	$MenuBook.visible = true
