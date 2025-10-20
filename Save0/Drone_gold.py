rowheight = get_world_size()

def plantroutine():
	for _ in range( rowheight ):
		if get_water() < 0.25:
			use_item(Items.Water)
		plant(Entities.Bush)
		move(North)
	for _ in range( rowheight ):
		while not can_harvest():
			pass
		use_item( Items.Weird_Substance , (2**(num_unlocked(Unlocks.Mazes) -1)) )
		harvest()
		move(North)
	
def runthis():
	for _ in range( get_world_size() ):
		if not spawn_drone(plantroutine):
			plantroutine()
		move(East)

while 1:
	runthis()