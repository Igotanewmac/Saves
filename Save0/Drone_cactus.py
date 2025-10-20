
# go home
def gohome():
	while get_pos_x() > 0:
		move(West)
	while get_pos_y() > 0:
		move(South)

def plantcolumn():
	for y in range( get_world_size() ):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant( Entities.Cactus )
		move(North)

def sortcolumn():
	hasswapped = 1
	while hasswapped:
		hasswapped = 0
		for y in range( get_world_size() - 1 ):
			if measure() > measure(North):
				swap(North)
				hasswapped = 1
			move(North)
		move(North)
			
def sortrow():
	hasswapped = 1
	while hasswapped:
		hasswapped = 0
		for y in range( get_world_size() - 1 ):
			if measure() > measure(East):
				swap(East)
				hasswapped = 1
			move(East)
		move(East)


def runthis():
	gohome()
	# plant
	dronelist = []
	for x in range( get_world_size() ):
		dronehandle = spawn_drone(plantcolumn)
		if dronehandle == None:
			plantcolumn()
		else:
			dronelist.append( dronehandle )
		move(East)
	for drone in dronelist:
		wait_for(drone)
	
	# sort column
	dronelist = []
	for x in range( get_world_size() ):
		dronehandle = spawn_drone(sortcolumn)
		if dronehandle == None:
			sortcolumn()
		else:
			dronelist.append(dronehandle)
		move(East)
	for drone in dronelist:
		wait_for(drone)
	
	# sort row
	dronelist = []
	for x in range( get_world_size() ):
		dronehandle = spawn_drone(sortrow)
		if dronehandle == None:
			sortrow()
		else:
			dronelist.append(dronehandle)
		move(North)
	for drone in dronelist:
		wait_for(drone)
	
	# harvest
	move(West)
	move(South)
	harvest()
	move(North)
	move(East)		
	
	

