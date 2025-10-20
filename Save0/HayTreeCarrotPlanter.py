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
			
			# now decide what to plant!
			if num_items(Items.Hay) < max_items_to_farm:
				if get_ground_type() != Grounds.Grassland:
					till()
			elif num_items(Items.Wood) < max_items_to_farm:
				if ( get_pos_x() + get_pos_y() ) % 2:
					plant(Entities.Tree)
				else:
					if get_ground_type() != Grounds.Grassland:
						till()
					plant(Entities.Bush)
			elif num_items(Items.Carrot) < max_items_to_farm:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)
			else:
				# in the eeeeeend.....
				max_items_to_farm += 10000
				#do_a_flip()
				plant(Entities.Bush)
				#print(max_items_to_farm)
				#pet_the_piggy()
			move(North)
		move(East)
			