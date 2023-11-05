extends CanvasLayer

var loadWord = "Loading"
var tick = 0

func _ready():
	$PlaneSpin.opening = 6
	

func _process(_delta):
	$Label.text = loadWord
	if tick % 48 >= 12:
		$Label.text += "."
	if tick % 48 >= 24:
		$Label.text += "."
	if tick % 48 >= 36:
		$Label.text += "."
	tick += 1
