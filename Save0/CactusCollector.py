# go home
while get_pos_x() > 0:
	move(West)
while get_pos_y() > 0:
	move(South)

	
# clear the field
for x in range( get_world_size() ):
	for y in range( get_world_size() ):
		if can_harvest():
			harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
		move(North)
	move(East)
	
	
for ypos in range( get_world_size() ):
	hasflipped = 1
	while hasflipped == 1:
		hasflipped = 0
		for xpos in range( get_world_size() -1 ):
			curval = measure()
			nextval = measure(East)
			if curval > nextval:
				swap(East)
				hasflipped = 1
			move(East)
		move(East)
	move(North)

for xpos in range( get_world_size() ):
	hasflipped = 1
	while hasflipped == 1:
		hasflipped = 0
		for ypos in range( get_world_size() -1 ):
			curval = measure()
			nextval = measure(North)
			if curval > nextval:
				swap(North)
				hasflipped = 1
			move(North)
		move(North)
	move(East)

harvest()