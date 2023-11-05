extends Camera2D

var selected = null
export (bool) var greyscale = false

func _ready():
	pass


func _process(_delta):
	$Tiles.material.set("shader_param/greyscale", greyscale)
	# hovered
	var local_coords = $Tiles.get_viewport().get_mouse_position()
	local_coords = Vector2((local_coords.x - position.x)/scale.x, (local_coords.y - position.y)/scale.y) # , -8
	var tile_coords = $Tiles.world_to_map(local_coords)
	var tile_index = $Tiles.get_cellv(tile_coords)
	var tile_center = $Tiles.map_to_world(tile_coords)
	tile_center.x -= 4
	tile_center.y -= 18
	var tile_texture = null if tile_index == -1 else $Tiles.tile_set.tile_get_texture(tile_index)
	if tile_texture != null:
		$HoveredTile.visible = true
		$HoveredTile.position = tile_center
		$HoveredTile.texture = tile_texture
		var overlay_index = $Overlays.get_cellv(tile_coords)
		if overlay_index != -1:
			$HoveredOverlay.visible = true
			$HoveredOverlay.position = tile_center
			$HoveredOverlay.texture = $Overlays.tile_set.tile_get_texture(overlay_index)
		else:
			$HoveredOverlay.visible = false
	else:
		$HoveredTile.visible = false
		$HoveredOverlay.visible = false
	# selected
	if selected != null:
		tile_index = $Tiles.get_cellv(selected)
		tile_center = $Tiles.map_to_world(selected)
		tile_center.x -= 4
		tile_center.y -= 18
		tile_texture = $Tiles.tile_set.tile_get_texture(tile_index)
		$SelectedTile.visible = true
		$SelectedTile.offset = tile_center
		$SelectedTile.texture = tile_texture
		var overlay_index = $Overlays.get_cellv(selected)
		var overlay_texture = null if overlay_index == -1 else $Overlays.tile_set.tile_get_texture(overlay_index)
		$SelectedOverlay.visible = overlay_texture != null
		$SelectedOverlay.offset = tile_center
		$SelectedOverlay.texture = overlay_texture
	else:
		$SelectedTile.visible = false
		$SelectedOverlay.visible = false
		
	var player_tile = Vector2(Base.tile_index % 33, Base.tile_index / 33)
	tile_index = $Tiles.get_cellv(player_tile)
	tile_center = $Tiles.map_to_world(player_tile)
	tile_center.x -= 4
	tile_center.y -= 18
	$PlayerTile.offset = tile_center
	tile_texture = $Tiles.tile_set.tile_get_texture(tile_index)
	$PlayerTile.texture = tile_texture
	var overlay_index = $Overlays.get_cellv(player_tile)
	if overlay_index != -1:
		var overlay_texture = $Overlays.tile_set.tile_get_texture(overlay_index)
		$PlayerTileOverlay.visible = overlay_texture != null
		$PlayerTileOverlay.offset = tile_center
		$PlayerTileOverlay.texture = overlay_texture
	$PlayerProxy.set_player(Base.player)
	$PlayerProxy.position = $Tiles.map_to_world(player_tile)
	$PlayerProxy.position.x += 14
	$PlayerProxy.position.y -= 18
		
		
func _unhandled_input(event):
	if event is InputEventMouseButton and event.pressed:
		var local_coords = $Tiles.get_viewport().get_mouse_position()
		local_coords.x -= position.x
		local_coords.y -= position.y
		local_coords.x /= scale.x
		local_coords.y /= scale.y
		var tile_coords = $Tiles.world_to_map(local_coords)
		if $Tiles.get_cellv(tile_coords) != -1 and tile_coords != selected and not greyscale:
			selected = tile_coords
		else:
			selected = null
