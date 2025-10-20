
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


def runthis():
	while 1:	
		startx = get_pos_x()
		starty = get_pos_y()
		#print(get_companion())
		plant_type , ( xpos , ypos ) = get_companion()
		gotopos(xpos,ypos)
		harvest()
		plantplant(plant_type)
		gotopos( startx , starty )
		while not can_harvest():
			pass
		harvest()
		if get_water() < 0.75:
			use_item(Items.Water)
		plantplant(Entities.Carrot)
		use_item(Items.Fertilizer)
		use_item(Items.Weird_Substance)

clear()		
gotopos( 3 , 3 )
spawn_drone(runthis)
gotopos( 11 , 3 )
spawn_drone(runthis)
gotopos( 19 , 3 )
spawn_drone(runthis)
gotopos( 27 , 3 )
spawn_drone(runthis)

gotopos(7,7)
spawn_drone(runthis)
gotopos(15,7)
spawn_drone(runthis)
gotopos(23,7)
spawn_drone(runthis)

gotopos( 3 , 11 )
spawn_drone(runthis)
gotopos( 11 , 11 )
spawn_drone(runthis)
gotopos( 19 , 11 )
spawn_drone(runthis)
gotopos( 27 , 11 )
spawn_drone(runthis)


gotopos(7,15)
spawn_drone(runthis)
gotopos(15,15)
spawn_drone(runthis)
gotopos(23,15)
spawn_drone(runthis)

gotopos( 3 , 19 )
spawn_drone(runthis)
gotopos( 11 , 19 )
spawn_drone(runthis)
gotopos( 19 , 19 )
spawn_drone(runthis)
gotopos( 27 , 19 )
spawn_drone(runthis)

gotopos(7,23)
spawn_drone(runthis)
gotopos(15,23)
spawn_drone(runthis)
gotopos(23,23)
spawn_drone(runthis)

gotopos( 3 , 27 )
spawn_drone(runthis)
gotopos( 11 , 27 )
spawn_drone(runthis)
gotopos( 19 , 27 )
spawn_drone(runthis)
gotopos( 27 , 27 )
spawn_drone(runthis)

gotopos(0,0)
