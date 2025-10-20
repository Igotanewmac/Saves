#pumpkin planter 2
def gotopos( targetxpos , targetypos ):
	while get_pos_x() < targetxpos:
		move(East)
	while get_pos_x() > targetxpos:
		move(West)
	while get_pos_y() < targetypos:
		move(North)
	while get_pos_y() > targetypos:
		move(South)



for x in range( get_world_size() ):
	for y in range( get_world_size() ):
		gotopos(x,y)
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()


while 1:
	curlist = []
	newlist = []
	
	for x in range( get_world_size() ):
		for y in range( get_world_size() ):
			curlist.append( [ x , y ] )
	
	gotopos(0,0)
				
	while len(curlist) > 0:
		for curloc in curlist:
			gotopos( curloc[0] , curloc[1] )
			if len(curlist) < 10:
				if get_water() < 1:
					use_item(Items.Water)
			if get_entity_type() != Entities.Pumpkin:
				plant(Entities.Pumpkin)
				newlist.append( [ curloc[0] , curloc[1] ] )
			if ( get_pos_x() == 0 ) and ( get_pos_y() == 0 ):
				magicnumber = measure()
		curlist = newlist
		newlist = []
	
	
	petcounter = 0
	while (measure() != magicnumber) and (petcounter < 5):
		pet_the_piggy()
		petcounter += 1
		if get_entity_type() == Entities.Dead_Pumpkin:
			plant(Entities.Pumpkin)
			petcounter = 0
	
	harvest()

		