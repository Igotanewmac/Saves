
amountofweird = (2**(num_unlocked(Unlocks.Mazes) -1))*get_world_size()

dirleft = { North:West , West:South , South:East , East:North }
dirright = { North:East , East:South , South:West , West:North }


def weirstuffroutine():
	while num_items(Items.Weird_Substance) < amountofweird*301:
		for x in range(get_world_size()):
			for y in range(get_world_size()):
				if can_harvest():
					harvest()
				if ( ( get_pos_x() + get_pos_y() ) % 2 ) == 0:
					plant(Entities.Tree)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				else:
					plant(Entities.Bush)
					if num_items(Items.Fertilizer) > 0:
						use_item(Items.Fertilizer)
				move(North)
			move(East)

while 1:
	weirstuffroutine()