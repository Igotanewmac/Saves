def gotopos( targetxpos , targetypos ):
	while get_pos_x() < targetxpos:
		move(East)
	while get_pos_x() > targetxpos:
		move(West)
	while get_pos_y() < targetypos:
		move(North)
	while get_pos_y() > targetypos:
		move(South)

def plantplant( planttoplant ):
	if planttoplant == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
		plant(Entities.Grass)
	elif planttoplant == Entities.Carrot:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrot)
	elif planttoplant == Entities.Bush:
		plant(Entities.Bush)
	elif planttoplant == Entities.Tree:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Tree)
	elif planttoplant == Entities.Cactus:
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)		
	else:
		print(planttoplant)