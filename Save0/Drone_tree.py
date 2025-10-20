
def plant_column():
	for _ in range(get_world_size()):
		if get_ground_type() != Grounds.Soil:
			till()
		if get_water() < 0.5:
			use_item(Items.Water)
		if (get_pos_x() + get_pos_y()) % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		move(North)


def harvest_column():
	for _ in range( get_world_size() ):
		if get_entity_type() == None:
			if (get_pos_x() + get_pos_y()) % 2:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)
			continue
		while not can_harvest():
			pass
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		if get_water() < 0.7:
			use_item(Items.Water)
		if (get_pos_x() + get_pos_y()) % 2:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		move(North)

def runthis():
	for _ in range(get_world_size() - 1):
		spawn_drone(harvest_column)
		move(East)
	harvest_column()
