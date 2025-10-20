
def gotopos( targetxpos , targetypos ):
	while get_pos_x() < targetxpos:
		move(East)
	while get_pos_x() > targetxpos:
		move(West)
	while get_pos_y() < targetypos:
		move(North)
	while get_pos_y() > targetypos:
		move(South)



def plantingroutine():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Sunflower)
	numofpetals = measure()
	petalcounts[numofpetals].append( [ get_pos_x() , get_pos_y() ] )
	

while num_items(Items.Power) < 1000000:
	# plant and record sunflowers
	gotopos(0,0)
	
	# create a list of lists to store the tuples
	petalcounts = []
	for i in range( 16 ):
		petalcounts.append([])
	
	# do the actual planting, and populate the list	
	for xpos in range( get_world_size() ):
		for ypos in range( get_world_size() ):
			plantingroutine()
			move(North)
		move(East)
	
	# now harvest from biggest to smallest
	for petalsize in range( 15 , 6 , -1 ):
		for listindex in range( len(petalcounts[petalsize]) ):
			gotopos( petalcounts[petalsize][listindex][0] , petalcounts[petalsize][listindex][1] )
			harvest()
							