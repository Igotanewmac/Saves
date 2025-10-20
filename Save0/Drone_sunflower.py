def plantcolumn():
	for _ in range( get_world_size() ):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		if get_water() < 0.75:
			use_item(Items.Water)
		plant(Entities.Sunflower)
		move(North)

def harvestcolumn( petalcount ):
	for _ in range( get_world_size() ):
		if (measure() == petalcount):
			while not can_harvest():
				pass
			harvest()
		move(North)

def doitall():
	plantcolumn()
	harvestcolumn(15)
	harvestcolumn(14)
	harvestcolumn(13)
	harvestcolumn(12)
	harvestcolumn(11)
	harvestcolumn(10)
	harvestcolumn(9)
	harvestcolumn(8)
	harvestcolumn(7)

def harvest15():
	harvestcolumn(15)
def harvest14():
	harvestcolumn(14)
def harvest13():
	harvestcolumn(13)
def harvest12():
	harvestcolumn(12)
def harvest11():
	harvestcolumn(11)
def harvest10():
	harvestcolumn(10)
def harvest9():
	harvestcolumn(9)
def harvest8():
	harvestcolumn(8)
def harvest7():
	harvestcolumn(7)
		



def runthis():
	clear()
	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(plantcolumn)
		quick_print(retval)
		if retval == None:
			plantcolumn()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)

	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest15)
		quick_print(retval)
		if retval == None:
			harvest15()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest14)
		quick_print(retval)
		if retval == None:
			harvest14()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest13)
		quick_print(retval)
		if retval == None:
			harvest13()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)
		

	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest12)
		quick_print(retval)
		if retval == None:
			harvest12()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest11)
		quick_print(retval)
		if retval == None:
			harvest11()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)
		

	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest10)
		quick_print(retval)
		if retval == None:
			harvest10()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest9)
		quick_print(retval)
		if retval == None:
			harvest9()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest8)
		quick_print(retval)
		if retval == None:
			harvest8()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)



	dronelist = []
	for j in range( 1 , max_drones() + 1):
		retval = spawn_drone(harvest7)
		quick_print(retval)
		if retval == None:
			harvest7()
		else:
			dronelist.append(retval)
		move(East)
	for drone in dronelist:
		wait_for(drone)


	