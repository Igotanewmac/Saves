def plantrowofbigplants():
	hasplanted = 1
	for y in range( get_world_size() ):
		# are we over a sunflower?
		if get_entity_type() != Entities.Sunflower:
			if can_harvest():
				harvest()
			if get_ground_type() != Grounds.Soil:
				till()
			plant(Entities.Sunflower)
		
		#now we are over a sunflower
		while measure() < 15:
			harvest()
			plant(Entities.Sunflower)
		
		if not can_harvest():
			pass
		move(North)


def harvestrow():
	for y in range( get_world_size() ):
		harvest()
		move(North)

def dofield():		
	dronelist = []	
	for x in range( max_drones() -1 ):
		dronelist.append( spawn_drone( plantrowofbigplants ) )
		move(East)
	
	plantrowofbigplants()
	
	for drone in dronelist:
		wait_for(drone)
	
	while get_pos_x() > 0:
		move(East)
	while get_pos_y() > 0:
		move(South)
	
	dronelist = []	
	for x in range( max_drones() -1 ):
		dronelist.append( spawn_drone( harvestrow ) )
		move(East)
	
	harvestrow()

while 1:
	dofield()
