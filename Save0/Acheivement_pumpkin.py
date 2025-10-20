def plantcolumn():
	planted = 1
	while planted:
		planted = 0
		for _ in range( get_world_size() ):
			if get_water() < 0.75:
				use_item(Items.Water)
			if get_entity_type() == Entities.Pumpkin:
				while not can_harvest():
					if get_entity_type() == Entities.Dead_Pumpkin:
						break
					pass
			if get_entity_type() != Entities.Pumpkin:
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Pumpkin)
				planted = 1
			move(North)


			
def runthis():
	dronelist = []
	for _ in range( get_world_size() -1 ):
		dronelist.append( spawn_drone(plantcolumn) )
		move(East)
	plantcolumn()
	for drone in dronelist:
		wait_for(drone)
	move(East)
	while not can_harvest():
		pass
	blid = measure()
	move(East)
	move(South)
	while measure() != blid:
		pass
	harvest()

while 1:
	runthis()