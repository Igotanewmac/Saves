
def gotopos( targetxpos , targetypos ):
	while get_pos_x() < targetxpos:
		move(East)
	while get_pos_x() > targetxpos:
		move(West)
	while get_pos_y() < targetypos:
		move(North)
	while get_pos_y() > targetypos:
		move(South)

def planthay():
	if can_harvest():
		harvest()
	if get_ground_type() != Grounds.Grassland:
		till()




def plantsquare( plantingroutine , startx , starty , size ):
	endx = startx + size
	endy = starty + size
	direction = 0
	
	# first, go to the bottom left corner
	gotopos( startx , starty )
	
	while get_pos_x() < endx:
			if direction == 0:
				plantingroutine()
				move(North)
			else:
				plantingroutine()
				move(South)
			if get_pos_y() == endy:
				plantingroutine()
				direction = 1
				move(East)
			if get_pos_y() == starty:
				plantingroutine()
				direction = 0
				move(East)
	
	# now go back to bottom left
	gotopos( startx , starty )




plantsquare( planthay , 10 , 10 , 4 )