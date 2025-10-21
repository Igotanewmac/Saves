
dirleft = { North:West , West:South , South:East , East:North }
dirright = { North:East , East:South , South:West , West:North }

amount_of_weird = (2**(num_unlocked(Unlocks.Mazes) -1))*2

numofitems = 100000000

def plantroutine():
	if get_water() < 0.25:
		use_item(Items.Water)
	plant(Entities.Bush)
	while not can_harvest():
		pass
	use_item( Items.Weird_Substance , amount_of_weird )
	


def solveroutine():
	curdir = North
	while get_entity_type() == Entities.Hedge:
		if can_move( dirleft[curdir] ):
			curdir = dirleft[curdir]
			move(curdir)
		else:
			curdir = dirright[curdir]
	
		
	
def singlesolver():
	i = 0
	plantroutine()	
	while i < 300:
		i += 1
		solveroutine()
		use_item( Items.Weird_Substance , amount_of_weird )
	solveroutine()
	harvest()


def runthis():
	clear()
	dronelist = []
	for y in range(4):
		for x in range(8):
			if spawn_drone(singlesolver):
				pass
			else:
				singlesolver()
			move(East)
			move(East)
			move(East)
			move(East)
		move(North)
		move(North)
		move(North)
		move(North)
	
	
	for drone in dronelist:
		wait_for(drone)

while 1:
	runthis()

	