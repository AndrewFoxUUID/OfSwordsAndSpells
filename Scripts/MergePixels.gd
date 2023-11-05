extends Object

class_name TileMapMerge

func merge(tilemap, exclude_list : Array = []) -> Array:
	var rect_list : Array
	var bottom_right := Vector2(1, 1)
	
	for tile_pos in tilemap.get_used_cells():
		if not (exclude_list.has(tilemap.get_cellv(tile_pos))):
			if (tilemap.get_cell(tile_pos.x, tile_pos.y - 1) == TileMap.INVALID_CELL or
				tilemap.get_cell(tile_pos.x, tile_pos.y + 1) == TileMap.INVALID_CELL or
				tilemap.get_cell(tile_pos.x - 1, tile_pos.y) == TileMap.INVALID_CELL or
				tilemap.get_cell(tile_pos.x + 1, tile_pos.y) == TileMap.INVALID_CELL):
				rect_list.append(Rect2(tile_pos, bottom_right))
	rect_list = join_rects_x(rect_list)
	rect_list = join_rects_y(rect_list)
	
	return rect_list

func join_rects_x(rect_list : Array) -> Array:
	var remove := Rect2(0.1, 0.1, 0.1, 0.1)
	var found := true
	
	while found:
		found = false
		for pos_0 in range(rect_list.size() - 1, -1, -1):
			var rect_0 : Rect2 = rect_list[pos_0]
			for pos_1 in range(rect_list.size() - 1, -1, -1):
				var rect_1 : Rect2 = rect_list[pos_1]
				if (rect_0.position.x + rect_0.size.x == rect_1.position.x and
					rect_0.position.y == rect_1.position.y and
					rect_0.size.y == rect_1.size.y):
					rect_list[pos_0].size.x = rect_0.size.x + rect_1.size.x
					rect_0 = rect_list[pos_0]
					rect_list[pos_1] = remove
		for pos in range(rect_list.size() - 1, 0, -1):
			if rect_list[pos] == remove:
				rect_list.remove(pos)
				found = true

	return rect_list

func join_rects_y(rect_list : Array) -> Array:
	var remove := Rect2(0.1, 0.1, 0.1, 0.1)
	var found := true
	
	while found:
		found = false
		for pos_0 in range(rect_list.size() - 1, 0, -1):
			var rect_0 : Rect2 = rect_list[pos_0]
			for pos_1 in range(rect_list.size() - 1, 0, -1):
				var rect_1 : Rect2 = rect_list[pos_1]
				if (rect_0.position.y + rect_0.size.y == rect_1.position.y and
					rect_0.position.x == rect_1.position.x and
					rect_0.size.x == rect_1.size.x):
					rect_list[pos_0].size.y = rect_0.size.y + rect_1.size.y
					rect_0 = rect_list[pos_0]
					rect_list[pos_1] = remove
		for pos in range(rect_list.size() - 1, 0, -1):
			if rect_list[pos] == remove:
				rect_list.remove(pos)
				found = true

	return rect_list
