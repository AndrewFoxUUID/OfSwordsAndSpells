extends Node2D

var focused = null
var SguilaFocused = false
var ZwiFocused = false
var ArthiliFocused = false
var HellithaneFocused = false
var KarathisFocused = false
var VaeldarFocused = false
var CountermandFocused = false

func _ready():
	if Base.player.get_level() < 2:
		Base.world_name = "Sguila"
		Base.change_scene("res://Scenes/World.tscn")
	

func _unhandled_input(event):
	if event.is_action_pressed("ui_accept") or (event is InputEventMouseButton and event.pressed):
		if focused != null:
			Base.world_name = focused
			Base.change_scene("res://Scenes/World.tscn")
	

func playNext():
	if SguilaFocused:
		$Sguila.scale = Vector2(3.0, 3.0)
		focused = "Sguila"
	elif ZwiFocused:
		$Zwi.scale = Vector2(2.5, 2.5)
		focused = "Zwi"
	elif ArthiliFocused:
		$Arthili.scale = Vector2(2.5, 2.5)
		focused = "Arthili"
	elif HellithaneFocused:
		$Hellithane.scale = Vector2(2.0, 2.0)
		focused = "Hellithane"
	elif KarathisFocused:
		$Karathis.scale = Vector2(2.0, 2.0)
		focused = "Karathis"
	elif VaeldarFocused:
		$Vaeldar.scale = Vector2(1.5, 1.5)
		focused = "Vaeldar"
	elif CountermandFocused:
		$Countermand.scale = Vector2(1.5, 1.5)
		focused = "Countermand"


func _on_SguilaRect_mouse_entered():
	SguilaFocused = true
	if not ZwiFocused and not ArthiliFocused and not HellithaneFocused and not KarathisFocused and not VaeldarFocused and not CountermandFocused:
		$Sguila.scale = Vector2(3.0, 3.0)
		focused = "Sguila"


func _on_SguilaRect_mouse_exited():
	SguilaFocused = false
	$Sguila.scale = Vector2(2.5, 2.5)
	focused = null
	playNext()


func _on_ZwiRect_mouse_entered():
	ZwiFocused = true
	if not SguilaFocused and not ArthiliFocused and not HellithaneFocused and not KarathisFocused and not VaeldarFocused and not CountermandFocused:
		$Zwi.scale = Vector2(2.5, 2.5)
		focused = "Zwi"


func _on_ZwiRect_mouse_exited():
	ZwiFocused = false
	$Zwi.scale = Vector2(2.0, 2.0)
	focused = null
	playNext()


func _on_ArthiliRect_mouse_entered():
	ArthiliFocused = true
	if not SguilaFocused and not ZwiFocused and not HellithaneFocused and not KarathisFocused and not VaeldarFocused and not CountermandFocused:
		$Arthili.scale = Vector2(2.5, 2.5)
		focused = "Arthili"


func _on_ArthiliRect_mouse_exited():
	ArthiliFocused = false
	$Arthili.scale = Vector2(2.0, 2.0)
	focused = null
	playNext()


func _on_HellithaneRect_mouse_entered():
	HellithaneFocused = true
	if not SguilaFocused and not ZwiFocused and not ArthiliFocused and not KarathisFocused and not VaeldarFocused and not CountermandFocused:
		$Hellithane.scale = Vector2(2.0, 2.0)
		focused = "Hellithane"


func _on_HellithaneRect_mouse_exited():
	HellithaneFocused = false
	$Hellithane.scale = Vector2(1.5, 1.5)
	focused = null
	playNext()


func _on_KarathisRect_mouse_entered():
	KarathisFocused = true
	if not SguilaFocused and not ZwiFocused and not ArthiliFocused and not HellithaneFocused and not VaeldarFocused and not CountermandFocused:
		$Karathis.scale = Vector2(2.0, 2.0)
		focused = "Karathis"


func _on_KarathisRect_mouse_exited():
	KarathisFocused = false
	$Karathis.scale = Vector2(1.5, 1.5)
	focused = null
	playNext()


func _on_VaeldarRect_mouse_entered():
	VaeldarFocused = true
	if not SguilaFocused and not ZwiFocused and not ArthiliFocused and not HellithaneFocused and not KarathisFocused and not CountermandFocused:
		$Vaeldar.scale = Vector2(1.5, 1.5)
		focused = "Vaeldar"


func _on_VaeldarRect_mouse_exited():
	VaeldarFocused = false
	$Vaeldar.scale = Vector2(1.0, 1.0)
	focused = null
	playNext()


func _on_CountermandRect_mouse_entered():
	CountermandFocused = true
	if not SguilaFocused and not ZwiFocused and not ArthiliFocused and not HellithaneFocused and not KarathisFocused and not VaeldarFocused:
		$Countermand.scale = Vector2(1.5, 1.5)
		focused = "Countermand"


func _on_CountermandRect_mouse_exited():
	CountermandFocused = false
	$Countermand.scale = Vector2(1.0, 1.0)
	focused = null
	playNext()
