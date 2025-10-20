
def harvest_column():
	for _ in range( get_world_size() ):
		if get_entity_type() == None:
			plant(Entities.Carrot)
			move(North)
			continue
		while not can_harvest():
			pass
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		if get_water() < 0.75:
			use_item(Items.Water)
		plant(Entities.Carrot)
		move(North)

def runthis():
	for _ in range(get_world_size() - 1):
		spawn_drone(harvest_column)
		move(East)
	harvest_column()
	move(East)

