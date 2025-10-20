def harvest_column():
	for _ in range(get_world_size()):
		harvest()
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Grass)
		move(North)

def runthis():
	
	for dronei in range( max_drones() ):
		if spawn_drone(harvest_column):
			move(East)
		else:
			harvest_column()
			move(East)
	
