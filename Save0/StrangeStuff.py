max_items_to_farm = 1000000
while get_pos_x() > 0:
	move(West)
while get_pos_y() > 0:
	move(South)
change_hat(Hats.Wizard_Hat)
while True:
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			
			# first things forst, harvest anything on this square
			if can_harvest():
				harvest()
			
			if ( get_pos_x() + get_pos_y() ) % 2:
				plant(Entities.Tree)
				use_item(Items.Fertilizer)
			else:
				if get_ground_type() != Grounds.Grassland:
					till()
				plant(Entities.Bush)
			move(North)
		move(East)
			