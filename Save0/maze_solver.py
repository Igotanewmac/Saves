import util






amountofweird = (2**(num_unlocked(Unlocks.Mazes) -1))*get_world_size()

dirleft = { North:West , West:South , South:East , East:North }
dirright = { North:East , East:South , South:West , West:North }


def weirdstuffroutine():
	while num_items(Items.Weird_Substance) < amountofweird*301:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
					plant(Entities.Tree)
					while num_items(Items.Fertilizer) < 1:
						pass
					use_item(Items.Fertilizer)
				else:
					plant(Entities.Bush)
					while num_items(Items.Fertilizer) < 1:
						pass
					use_item(Items.Fertilizer)
				move(North)
			move(East)


def weirdstuffroutine2():
	print(amountofweird)
	#reset to grass and 0,0
	clear()
	#move to 1,1
	move(North)
	move(East)
	plant(Entities.Tree)

	# wait for harvest
	while not can_harvest():
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)
		pass
	harvest()
	# now I have some weird substance
	
	while num_items(Items.Weird_Substance) < amountofweird*301:
	# leave grass in the center
			
		#and now the trees
		move(North)
		plant(Entities.Tree)
		move(South)
		move(East)
		plant(Entities.Tree)
		move(West)
		move(West)
		plant(Entities.Tree)
		move(East)
		move(South)
		plant(Entities.Tree)
		move(North)

		use_item(Items.Weird_Substance)

		move(South)
		if get_water() < 0.75:
			if num_items(Items.Water) > 1:
				use_item(Items.Water)
		while not can_harvest():
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			pass
		harvest()
		move(North)
		move(East)
		if get_water() < 0.75:
			if get_water() < 0.75:
				if num_items(Items.Water) > 1:
					use_item(Items.Water)
			if num_items(Items.Water) > 1:
				use_item(Items.Water)
		while not can_harvest():
			if get_water() < 0.75:
				if num_items(Items.Water) > 1:
					use_item(Items.Water)
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			pass
		harvest()
		move(West)
		move(North)
		if get_water() < 0.75:
			if num_items(Items.Water) > 1:
				use_item(Items.Water)
		while not can_harvest():
			if get_water() < 0.75:
				if num_items(Items.Water) > 1:
					use_item(Items.Water)
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			pass
		harvest()
		move(South)
		move(West)
		if get_water() < 0.75:
			if num_items(Items.Water) > 1:
				use_item(Items.Water)
		while not can_harvest():
			if get_water() < 0.75:
				if num_items(Items.Water) > 1:
					use_item(Items.Water)
			if num_items(Items.Fertilizer) > 0:
				use_item(Items.Fertilizer)
			pass
		harvest()
		move(East)


	
	
	





set_world_size(6)

clear()
weirdstuffroutine2()


while 1:
	pass









