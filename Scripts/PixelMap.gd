extends TileMap

var tilemap_merge = load("res://Scripts/MergePixels.gd").new()
var rect_list

func set_collisions():
	rect_list = tilemap_merge.merge(self)
	for rect in rect_list:
		var collision_rect = RectangleShape2D.new()
		collision_rect.set_extents(rect.size * cell_size / 2)
		var collision_shape = CollisionShape2D.new()
		collision_shape.set_shape(collision_rect)
		collision_shape.set_position(rect.position * cell_size + collision_rect.extents)
		$StaticBody2D.add_child(collision_shape)
		
func save_data():
	return var2str(self.tile_data)
	
func load_data(data):
	self.tile_data = str2var(data)
