while 1:
	
	xpos = get_pos_x()
	ypos = get_pos_y()
	
	
	
	plant(Entities.Bush)
	while get_water() < 1:
		use_item(Items.Water)
	if can_harvest():
		use_item(Items.Weird_Substance,2**(num_unlocked(Unlocks.Mazes) - 1))
		harvest()
	
	if (xpos == 0) and (ypos == 0):
		move(North)
	if (xpos == 0) and (ypos == 1):
		move(East)
	if (xpos == 1) and (ypos == 1):
		move(South)
	if (xpos == 1) and (ypos == 0):
		move(West)
		
	