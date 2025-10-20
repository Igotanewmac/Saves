
mazesize = 5


def dronefunc():
	treasurecount = 0
	while 1:
		if get_entity_type() == Entities.Treasure:
			use_item(Items.Weird_Substance , (2**(num_unlocked(Unlocks.Mazes) -1))*get_world_size() )
			treasurecount += 1
			if treasurecount > 5:
				harvest()
		else:
			treasurecount = 0





clear()
set_world_size(mazesize)

for x in range(get_world_size()):
	for y in range(get_world_size()):
		spawn_drone(dronefunc)
		move(East)
	move(North)




while 1:
	if get_water() < 0.75:
		use_item(Items.Water)
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)
	if not can_harvest():
		use_item(Items.Fertilizer)
	else:
		use_item(Items.Weird_Substance , (2**(num_unlocked(Unlocks.Mazes) -1))*get_world_size() )
	


		